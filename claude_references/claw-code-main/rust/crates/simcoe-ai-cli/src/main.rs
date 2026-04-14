mod app;
mod args;
mod format;
mod init;
mod input;
mod render;
mod session_manager;
mod transport;
mod tui;

use std::collections::BTreeMap;
use std::env;
use std::fs;
use std::io::{self, Read, Write};
use std::net::TcpListener;
use std::path::{Path, PathBuf};
use std::process::Command;

use api::{
    resolve_startup_auth_source, AuthSource, ContentBlockDelta, InputContentBlock, InputMessage,
    MessageRequest, MessageResponse, OutputContentBlock, SimcoeApiClient,
    StreamEvent as ApiStreamEvent, ToolChoice, ToolResultContentBlock,
};

use app::LiveCli;
use args::{default_permission_mode, parse_args, AllowedToolSet, CliAction, CliOutputFormat};
use commands::{
    render_resume_command_help, render_slash_command_help, resume_supported_slash_commands,
    slash_command_specs, SlashCommand,
};
use compat_harness::{extract_manifest, PluginSurfaceKind, UpstreamPaths};
use format::{
    agents_report_snapshot, config_report_snapshot, doctor_snapshot, format_compact_report,
    format_cost_report, format_status_report, hooks_report_snapshot, mcp_report_snapshot,
    memory_report_snapshot, plugin_report_snapshot, reload_plugins_report_snapshot,
    remote_env_report_snapshot, remote_setup_report_snapshot, render_agents_report,
    render_agents_report_from_snapshot, render_config_report, render_config_report_from_snapshot,
    render_diff_report, render_doctor_report, render_doctor_report_from_snapshot,
    render_hooks_report, render_hooks_report_from_snapshot, render_mcp_report,
    render_mcp_report_from_snapshot, render_memory_report, render_memory_report_from_snapshot,
    render_plugin_report, render_plugin_report_from_snapshot, render_reload_plugins_report,
    render_reload_plugins_report_from_snapshot, render_remote_env_report,
    render_remote_env_report_from_snapshot, render_remote_setup_report,
    render_remote_setup_report_from_snapshot, render_repl_help, render_skills_report,
    render_skills_report_from_snapshot, render_tasks_report, render_tasks_report_from_snapshot,
    render_tools_report, render_tools_report_from_snapshot, render_version_report,
    skills_report_snapshot, status_context, tasks_report_snapshot, tools_report_snapshot,
    McpAttentionSnapshot, McpBlockedServerSnapshot, McpCollectionSnapshot, McpServerDetailSnapshot,
    McpServerSnapshot, RemoteEnvReportSnapshot, StatusUsage,
};
use init::initialize_repo;
use render::{MarkdownStreamState, TerminalRenderer};
use runtime::{
    clear_oauth_credentials, generate_pkce_pair, generate_state, load_system_prompt,
    parse_oauth_callback_request_target, save_oauth_credentials, ApiClient, ApiRequest,
    AssistantEvent, CompactionConfig, ConfigLoader, ContentBlock, ConversationMessage,
    ConversationRuntime, MessageRole, OAuthAuthorizationRequest, OAuthConfig,
    OAuthTokenExchangeRequest, PermissionMode, PermissionPolicy, RuntimeError, Session, TokenUsage,
    ToolError, ToolExecutor, UsageTracker,
};
use serde::{Deserialize, Serialize};
use serde_json::json;
use session_manager::{
    list_managed_sessions, load_active_session_handle, render_session_list,
    resolve_session_reference, session_handle_from_path, sessions_dir, ManagedSessionSummary,
    SessionHandle,
};
use tools::{
    execute_tool, mvp_tool_specs, runtime_tool_definitions, tool_name_is_allowed, InspectableTool,
    InspectableToolSource, ToolSpec,
};
use tui::status_bar::StatusBarHandle;

const DEFAULT_MODEL: &str = "simcoe-opus-4-6";
const DEFAULT_ANTHROPIC_BASE_URL: &str = "https://api.anthropic.com";
const DEFAULT_OPENAI_BASE_URL: &str = "https://api.openai.com/v1";
const DEFAULT_OLLAMA_BASE_URL: &str = "http://localhost:11434/v1";
fn max_tokens_for_model(model: &str) -> u32 {
    if model.contains("opus") {
        32_000
    } else {
        64_000
    }
}
const DEFAULT_DATE: &str = "2026-03-31";
const DEFAULT_OAUTH_CALLBACK_PORT: u16 = 4545;
const VERSION: &str = env!("CARGO_PKG_VERSION");
const BUILD_TARGET: Option<&str> = option_env!("TARGET");
const GIT_SHA: Option<&str> = option_env!("GIT_SHA");

#[derive(Debug)]
struct CliExitError {
    message: String,
    exit_code: i32,
    operation: Option<String>,
    command: Option<String>,
}

impl CliExitError {
    fn new(message: impl Into<String>, exit_code: i32) -> Self {
        Self {
            message: message.into(),
            exit_code,
            operation: None,
            command: None,
        }
    }

    fn with_operation(mut self, operation: impl Into<String>) -> Self {
        self.operation = Some(operation.into());
        self
    }

    fn with_command(mut self, command: impl Into<String>) -> Self {
        self.command = Some(command.into());
        self
    }
}

impl std::fmt::Display for CliExitError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.message)
    }
}

impl std::error::Error for CliExitError {}

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if let Err(error) = run(&args) {
        render_cli_error(&args, error.as_ref());
        std::process::exit(exit_code_for_error(error.as_ref()));
    }
}

fn run(args: &[String]) -> Result<(), Box<dyn std::error::Error>> {
    match parse_args(&args)? {
        CliAction::DumpManifests { output_format } => run_dump_manifests(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("dump-manifests"), None))?,
        CliAction::BootstrapPlan { output_format } => run_bootstrap_plan(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("bootstrap-plan"), None))?,
        CliAction::PrintSystemPrompt {
            cwd,
            date,
            output_format,
        } => run_system_prompt(cwd, date, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("system-prompt"), None))?,
        CliAction::Config {
            section,
            output_format,
        } => run_config(section, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("config"), None))?,
        CliAction::Hooks {
            event,
            output_format,
        } => run_hooks(event, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("hooks"), None))?,
        CliAction::Mcp {
            server,
            output_format,
        } => run_mcp(server, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("mcp"), None))?,
        CliAction::Memory { output_format } => run_memory(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("memory"), None))?,
        CliAction::Agents {
            agent,
            output_format,
        } => run_agents(agent, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("agents"), None))?,
        CliAction::Plugin {
            surface,
            output_format,
        } => run_plugin(surface, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("plugin"), None))?,
        CliAction::ReloadPlugins { output_format } => run_reload_plugins(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("reload-plugins"), None))?,
        CliAction::RemoteEnv { output_format } => run_remote_env(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("remote-env"), None))?,
        CliAction::RemoteSetup { output_format } => run_remote_setup(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("remote-setup"), None))?,
        CliAction::Tools {
            tool,
            output_format,
        } => run_tools(tool, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("tools"), None))?,
        CliAction::Doctor { output_format } => run_doctor(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("doctor"), None))?,
        CliAction::Skills {
            skill,
            output_format,
        } => run_skills(skill, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("skills"), None))?,
        CliAction::Tasks {
            task,
            output_format,
        } => run_tasks(task, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("tasks"), None))?,
        CliAction::Export {
            path,
            output_format,
        } => run_export(path, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("export"), None))?,
        CliAction::Session {
            action,
            target,
            output_format,
        } => run_session(action, target, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("session"), None))?,
        CliAction::Version { output_format } => run_version(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("version"), None))?,
        CliAction::ResumeSession {
            session_path,
            commands,
            output_format,
        } => resume_session(&session_path, &commands, output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("resume"), None))?,
        CliAction::Prompt {
            prompt,
            model,
            provider,
            output_format,
            allowed_tools,
            permission_mode,
        } => {
            let mut cli =
                LiveCli::new(model, provider, true, allowed_tools, permission_mode, false)
                    .map_err(|error| with_cli_error_context(error, 1, Some("prompt"), None))?;
            cli.run_turn_with_output(&prompt, output_format)
                .map_err(|error| with_cli_error_context(error, 1, Some("prompt"), None))?;
        }
        CliAction::Login { output_format } => run_login(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("login"), None))?,
        CliAction::Logout { output_format } => run_logout(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("logout"), None))?,
        CliAction::Init { output_format } => run_init(output_format)
            .map_err(|error| with_cli_error_context(error, 1, Some("init"), None))?,
        CliAction::Repl {
            model,
            provider,
            allowed_tools,
            permission_mode,
        } => run_repl(model, provider, allowed_tools, permission_mode)?,
        CliAction::Help => print_help(),
    }
    Ok(())
}

fn inferred_error_output_format(args: &[String]) -> CliOutputFormat {
    let mut index = 0;
    let mut output_format = CliOutputFormat::Text;

    while index < args.len() {
        match args[index].as_str() {
            "--output-format" => {
                if let Some(value) = args.get(index + 1) {
                    output_format = match value.as_str() {
                        "json" => CliOutputFormat::Json,
                        "ndjson" => CliOutputFormat::Ndjson,
                        _ => CliOutputFormat::Text,
                    };
                }
                index += 2;
            }
            flag if flag.starts_with("--output-format=") => {
                output_format = match &flag[16..] {
                    "json" => CliOutputFormat::Json,
                    "ndjson" => CliOutputFormat::Ndjson,
                    _ => CliOutputFormat::Text,
                };
                index += 1;
            }
            _ => {
                index += 1;
            }
        }
    }

    output_format
}

fn inferred_error_metadata(args: &[String]) -> (Option<String>, Option<String>) {
    let mut index = 0;

    while index < args.len() {
        match args[index].as_str() {
            "--version" | "-V" => return (Some("version".to_string()), None),
            "--resume" => {
                let command = args
                    .get(index + 2)
                    .filter(|value| value.starts_with('/'))
                    .cloned();
                return (Some("resume".to_string()), command);
            }
            "--model" | "--provider" | "--output-format" | "--permission-mode"
            | "--allowedTools" | "--allowed-tools" | "--cwd" | "--date" => {
                index += 2;
            }
            arg if arg.starts_with("--") => {
                index += 1;
            }
            "dump-manifests" | "bootstrap-plan" | "system-prompt" | "config" | "hooks" | "mcp"
            | "memory" | "agents" | "plugin" | "reload-plugins" | "remote-env" | "remote-setup"
            | "tools" | "doctor" | "skills" | "tasks" | "export" | "session" | "login"
            | "logout" | "init" | "prompt" => {
                return (Some(args[index].clone()), None);
            }
            arg if !arg.starts_with('/') => return (Some("prompt".to_string()), None),
            _ => {
                index += 1;
            }
        }
    }

    (None, None)
}

fn exit_code_for_error(error: &(dyn std::error::Error + 'static)) -> i32 {
    error
        .downcast_ref::<CliExitError>()
        .map_or(1, |error| error.exit_code)
}

fn with_cli_error_context(
    error: Box<dyn std::error::Error>,
    exit_code: i32,
    operation: Option<&str>,
    command: Option<&str>,
) -> Box<dyn std::error::Error> {
    let existing = error.downcast_ref::<CliExitError>();
    let mut cli_error = CliExitError::new(
        error.to_string(),
        existing.map_or(exit_code, |error| error.exit_code),
    );
    cli_error.operation = existing
        .and_then(|error| error.operation.clone())
        .or_else(|| operation.map(str::to_string));
    cli_error.command = existing
        .and_then(|error| error.command.clone())
        .or_else(|| command.map(str::to_string));
    Box::new(cli_error)
}

#[derive(Debug, Default, PartialEq, Eq)]
struct StructuredCliErrorContext {
    operation: Option<String>,
    command: Option<String>,
    model: Option<String>,
    provider: Option<String>,
}

fn resolved_error_provider_label(provider_override: Option<&str>) -> Option<String> {
    normalize_provider_override(provider_override)
        .map(str::to_string)
        .or_else(|| active_runtime_provider_label(None).ok())
}

fn structured_error_context_from_action(action: CliAction) -> StructuredCliErrorContext {
    match action {
        CliAction::DumpManifests { .. } => StructuredCliErrorContext {
            operation: Some("dump-manifests".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::BootstrapPlan { .. } => StructuredCliErrorContext {
            operation: Some("bootstrap-plan".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::PrintSystemPrompt { .. } => StructuredCliErrorContext {
            operation: Some("system-prompt".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Config { .. } => StructuredCliErrorContext {
            operation: Some("config".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Hooks { .. } => StructuredCliErrorContext {
            operation: Some("hooks".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Mcp { .. } => StructuredCliErrorContext {
            operation: Some("mcp".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Memory { .. } => StructuredCliErrorContext {
            operation: Some("memory".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Agents { .. } => StructuredCliErrorContext {
            operation: Some("agents".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Plugin { .. } => StructuredCliErrorContext {
            operation: Some("plugin".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::ReloadPlugins { .. } => StructuredCliErrorContext {
            operation: Some("reload-plugins".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::RemoteEnv { .. } => StructuredCliErrorContext {
            operation: Some("remote-env".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::RemoteSetup { .. } => StructuredCliErrorContext {
            operation: Some("remote-setup".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Tools { .. } => StructuredCliErrorContext {
            operation: Some("tools".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Doctor { .. } => StructuredCliErrorContext {
            operation: Some("doctor".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Skills { .. } => StructuredCliErrorContext {
            operation: Some("skills".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Tasks { .. } => StructuredCliErrorContext {
            operation: Some("tasks".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Export { .. } => StructuredCliErrorContext {
            operation: Some("export".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Session { .. } => StructuredCliErrorContext {
            operation: Some("session".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Version { .. } => StructuredCliErrorContext {
            operation: Some("version".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::ResumeSession { commands, .. } => StructuredCliErrorContext {
            operation: Some("resume".to_string()),
            command: commands
                .first()
                .filter(|command| command.starts_with('/'))
                .cloned(),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Prompt {
            model, provider, ..
        } => StructuredCliErrorContext {
            operation: Some("prompt".to_string()),
            model: Some(model),
            provider: resolved_error_provider_label(provider.as_deref()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Login { .. } => StructuredCliErrorContext {
            operation: Some("login".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Logout { .. } => StructuredCliErrorContext {
            operation: Some("logout".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Init { .. } => StructuredCliErrorContext {
            operation: Some("init".to_string()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Repl {
            model, provider, ..
        } => StructuredCliErrorContext {
            operation: Some("repl".to_string()),
            model: Some(model),
            provider: resolved_error_provider_label(provider.as_deref()),
            ..StructuredCliErrorContext::default()
        },
        CliAction::Help => StructuredCliErrorContext {
            operation: Some("help".to_string()),
            ..StructuredCliErrorContext::default()
        },
    }
}

fn inferred_error_context_from_raw_args(args: &[String]) -> StructuredCliErrorContext {
    if args.is_empty() {
        return StructuredCliErrorContext {
            operation: Some("repl".to_string()),
            model: Some(DEFAULT_MODEL.to_string()),
            provider: resolved_error_provider_label(None),
            ..StructuredCliErrorContext::default()
        };
    }

    let mut index = 0;
    let mut model = None;
    let mut provider = None;

    while index < args.len() {
        match args[index].as_str() {
            "--version" | "-V" => {
                return StructuredCliErrorContext {
                    operation: Some("version".to_string()),
                    ..StructuredCliErrorContext::default()
                };
            }
            "--resume" => {
                let command = args
                    .get(index + 2)
                    .filter(|value| value.starts_with('/'))
                    .cloned();
                return StructuredCliErrorContext {
                    operation: Some("resume".to_string()),
                    command,
                    ..StructuredCliErrorContext::default()
                };
            }
            "--model" => {
                if let Some(value) = args.get(index + 1) {
                    model = Some(args::resolve_model_alias(value).to_string());
                }
                index += 2;
            }
            flag if flag.starts_with("--model=") => {
                model = Some(args::resolve_model_alias(&flag[8..]).to_string());
                index += 1;
            }
            "--provider" => {
                if let Some(value) = args.get(index + 1) {
                    provider = Some(value.clone());
                }
                index += 2;
            }
            flag if flag.starts_with("--provider=") => {
                provider = Some(flag[11..].to_string());
                index += 1;
            }
            "--output-format" | "--permission-mode" | "--allowedTools" | "--allowed-tools"
            | "--cwd" | "--date" => {
                index += 2;
            }
            arg if arg.starts_with("--") => {
                index += 1;
            }
            "dump-manifests" | "bootstrap-plan" | "system-prompt" | "config" | "hooks" | "mcp"
            | "memory" | "agents" | "plugin" | "reload-plugins" | "remote-env" | "remote-setup"
            | "tools" | "doctor" | "skills" | "tasks" | "export" | "session" | "login"
            | "logout" | "init" => {
                return StructuredCliErrorContext {
                    operation: Some(args[index].clone()),
                    ..StructuredCliErrorContext::default()
                };
            }
            "prompt" => {
                return StructuredCliErrorContext {
                    operation: Some("prompt".to_string()),
                    model: Some(model.unwrap_or_else(|| DEFAULT_MODEL.to_string())),
                    provider: provider.or_else(|| resolved_error_provider_label(None)),
                    ..StructuredCliErrorContext::default()
                };
            }
            arg if !arg.starts_with('/') => {
                return StructuredCliErrorContext {
                    operation: Some("prompt".to_string()),
                    model: Some(model.unwrap_or_else(|| DEFAULT_MODEL.to_string())),
                    provider: provider.or_else(|| resolved_error_provider_label(None)),
                    ..StructuredCliErrorContext::default()
                };
            }
            _ => {
                index += 1;
            }
        }
    }

    StructuredCliErrorContext {
        operation: Some("repl".to_string()),
        model: Some(model.unwrap_or_else(|| DEFAULT_MODEL.to_string())),
        provider: provider.or_else(|| resolved_error_provider_label(None)),
        ..StructuredCliErrorContext::default()
    }
}

fn inferred_error_context(args: &[String]) -> StructuredCliErrorContext {
    parse_args(args)
        .map(structured_error_context_from_action)
        .unwrap_or_else(|_| inferred_error_context_from_raw_args(args))
}

fn structured_error_transport_metadata(provider: &str) -> serde_json::Value {
    let mut metadata = crate::transport::build_turn_transport_metadata(provider);
    let Some(provider_runtime) = metadata
        .get_mut("provider_runtime")
        .and_then(serde_json::Value::as_object_mut)
    else {
        return metadata;
    };
    provider_runtime.insert("delivery_mode".to_string(), serde_json::Value::Null);
    metadata
}

fn cli_error_payload(
    args: &[String],
    error: &(dyn std::error::Error + 'static),
) -> serde_json::Value {
    let cli_error = error.downcast_ref::<CliExitError>();
    let inferred = inferred_error_context(args);
    let operation = cli_error
        .and_then(|error| error.operation.clone())
        .or(inferred.operation);
    let command = cli_error
        .and_then(|error| error.command.clone())
        .or(inferred.command);

    let mut payload = serde_json::Map::from_iter([
        ("type".to_string(), json!("error")),
        ("message".to_string(), json!(error.to_string())),
        ("exit_code".to_string(), json!(exit_code_for_error(error))),
        (
            "help_hint".to_string(),
            json!("Run `claw --help` for usage."),
        ),
    ]);
    if let Some(operation) = operation {
        payload.insert("operation".to_string(), json!(operation));
    }
    if let Some(command) = command {
        payload.insert("command".to_string(), json!(command));
    }
    if let Some(model) = inferred.model {
        payload.insert("model".to_string(), json!(model));
    }
    if let Some(provider) = inferred.provider {
        payload.insert("provider".to_string(), json!(provider));
        payload.insert(
            "transport".to_string(),
            structured_error_transport_metadata(&provider),
        );
    }

    serde_json::Value::Object(payload)
}

fn render_cli_error(args: &[String], error: &(dyn std::error::Error + 'static)) {
    let payload = cli_error_payload(args, error);

    match inferred_error_output_format(args) {
        CliOutputFormat::Text => {
            eprintln!("error: {error}\n\nRun `claw --help` for usage.");
        }
        CliOutputFormat::Json => {
            println!("{payload}");
        }
        CliOutputFormat::Ndjson => {
            println!(
                "{}",
                serde_json::to_string(&payload).expect("error payload should serialize")
            );
        }
    }
}

fn filter_tool_specs(allowed_tools: Option<&AllowedToolSet>) -> Vec<tools::ToolSpec> {
    mvp_tool_specs()
        .into_iter()
    .filter(|spec| allowed_tools.is_none_or(|allowed| tool_name_is_allowed(allowed, spec.name)))
        .collect()
}

fn dump_manifests_report() -> Result<String, Box<dyn std::error::Error>> {
    let (command_count, tool_count, bootstrap_phase_count) = manifest_counts()?;
    Ok(format!(
        "commands: {command_count}\ntools: {tool_count}\nbootstrap phases: {bootstrap_phase_count}",
    ))
}

fn manifest_counts() -> Result<(usize, usize, usize), Box<dyn std::error::Error>> {
    let workspace_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../..");
    let paths = UpstreamPaths::from_workspace_dir(&workspace_dir);
    let manifest = extract_manifest(&paths)?;
    Ok((
        manifest.commands.entries().len(),
        manifest.tools.entries().len(),
        manifest.bootstrap.phases().len(),
    ))
}

fn dump_manifests_payload() -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let (command_count, tool_count, bootstrap_phase_count) = manifest_counts()?;
    Ok(json!({
        "type": "dump_manifests",
        "command_count": command_count,
        "tool_count": tool_count,
        "bootstrap_phase_count": bootstrap_phase_count,
    }))
}

fn content_payload_map(
    kind: &str,
    content: impl Into<String>,
) -> serde_json::Map<String, serde_json::Value> {
    let content = content.into();
    serde_json::Map::from_iter([
        ("type".to_string(), json!(kind)),
        ("content".to_string(), json!(content)),
    ])
}

fn inspection_payload(
    kind: &str,
    selector_key: Option<&str>,
    selector_value: Option<&str>,
    content: &str,
) -> serde_json::Value {
    let mut payload = content_payload_map(kind, content);
    if let Some(selector_key) = selector_key {
        payload.insert(selector_key.to_string(), json!(selector_value));
    }
    serde_json::Value::Object(payload)
}

fn managed_session_summary_payload(
    summary: &ManagedSessionSummary,
    active_session_id: Option<&str>,
) -> serde_json::Value {
    json!({
        "id": summary.id,
        "path": summary.path.display().to_string(),
        "modified_epoch_secs": summary.modified_epoch_secs,
        "message_count": summary.message_count,
        "is_active": active_session_id.is_some_and(|id| summary.id == id),
    })
}

fn session_handle_payload(handle: &SessionHandle, message_count: usize) -> serde_json::Value {
    json!({
        "id": handle.id,
        "path": handle.path.display().to_string(),
        "message_count": message_count,
    })
}

fn session_switch_report(handle: &SessionHandle, message_count: usize) -> String {
    format!(
        "Session switched\n  Active session   {}\n  File             {}\n  Messages         {}",
        handle.id,
        handle.path.display(),
        message_count,
    )
}

fn session_list_report() -> Result<String, Box<dyn std::error::Error>> {
    let active_session_id = load_active_session_handle()?.map(|handle| handle.id);
    render_session_list(active_session_id.as_deref())
}

fn session_list_payload() -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let active_session = load_active_session_handle()?;
    let active_session_id = active_session.as_ref().map(|handle| handle.id.clone());
    let active_session_id_ref = active_session_id.as_deref();
    let sessions = list_managed_sessions()?;
    let content = render_session_list(active_session_id_ref)?;
    let mut payload = content_payload_map("session", content);
    payload.insert("action".to_string(), json!("list"));
    payload.insert(
        "directory".to_string(),
        json!(sessions_dir()?.display().to_string()),
    );
    payload.insert(
        "active_session".to_string(),
        match active_session {
            Some(handle) => session_handle_payload(
                &handle,
                Session::load_from_path(&handle.path)
                    .map(|session| session.messages.len())
                    .unwrap_or_default(),
            ),
            None => serde_json::Value::Null,
        },
    );
    payload.insert(
        "sessions".to_string(),
        json!(sessions
            .iter()
            .map(|session| managed_session_summary_payload(session, active_session_id_ref))
            .collect::<Vec<_>>()),
    );
    Ok(serde_json::Value::Object(payload))
}

fn switch_managed_session(
    target: &str,
) -> Result<(SessionHandle, usize), Box<dyn std::error::Error>> {
    runtime::switch_managed_session(target)
}

fn session_switch_payload(
    handle: &SessionHandle,
    message_count: usize,
) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let mut payload = content_payload_map("session", session_switch_report(handle, message_count));
    payload.insert("action".to_string(), json!("switch"));
    payload.insert(
        "directory".to_string(),
        json!(sessions_dir()?.display().to_string()),
    );
    payload.insert(
        "active_session".to_string(),
        session_handle_payload(handle, message_count),
    );
    Ok(serde_json::Value::Object(payload))
}

fn parse_runtime_json_value(rendered: String) -> Result<serde_json::Value, io::Error> {
    serde_json::from_str(&rendered).map_err(io::Error::other)
}

fn config_payload(
    section: Option<String>,
) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = config_report_snapshot(section.as_deref())?;
    let content = render_config_report_from_snapshot(&snapshot);
    let discovered_files = snapshot
        .discovered_files
        .iter()
        .map(|entry| {
            json!({
                "source": entry.source,
                "status": entry.status,
                "path": entry.path,
            })
        })
        .collect::<Vec<_>>();

    let mut payload = content_payload_map("config", content);
    payload.insert(
        "working_directory".to_string(),
        json!(snapshot.working_directory.as_str()),
    );
    payload.insert(
        "loaded_file_count".to_string(),
        json!(snapshot.loaded_file_count),
    );
    payload.insert(
        "merged_key_count".to_string(),
        json!(snapshot.merged_key_count),
    );
    payload.insert("discovered_files".to_string(), json!(discovered_files));

    if let Some(section) = snapshot.requested_section.as_deref() {
        payload.insert("section".to_string(), json!(section));
        payload.insert(
            "section_supported".to_string(),
            json!(snapshot.section_supported),
        );
        payload.insert(
            "supported_sections".to_string(),
            json!(["env", "hooks", "model", "provider"]),
        );
        payload.insert(
            "section_value".to_string(),
            if snapshot.section_supported && snapshot.section_has_value {
                parse_runtime_json_value(
                    snapshot
                        .section_value_rendered
                        .clone()
                        .unwrap_or_else(|| "null".to_string()),
                )?
            } else {
                serde_json::Value::Null
            },
        );
    } else {
        payload.insert(
            "merged_json".to_string(),
            parse_runtime_json_value(
                snapshot
                    .merged_json_rendered
                    .clone()
                    .unwrap_or_else(|| "{}".to_string()),
            )?,
        );
    }

    Ok(serde_json::Value::Object(payload))
}

fn hooks_payload(event: Option<String>) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = hooks_report_snapshot(event.as_deref())?;
    let content = render_hooks_report_from_snapshot(&snapshot);
    let mut payload = content_payload_map("hooks", content);

    if let Some(selected) = snapshot.selected_event.as_ref() {
        payload.insert("event".to_string(), json!(selected.requested));
        payload.insert("event_label".to_string(), json!(selected.label));
        payload.insert(
            "configured_count".to_string(),
            json!(selected.commands.len()),
        );
        payload.insert("commands".to_string(), json!(selected.commands));
        return Ok(serde_json::Value::Object(payload));
    }

    payload.insert(
        "pre_tool_use_count".to_string(),
        json!(snapshot.pre_commands.len()),
    );
    payload.insert(
        "post_tool_use_count".to_string(),
        json!(snapshot.post_commands.len()),
    );
    payload.insert("pre_tool_use".to_string(), json!(snapshot.pre_commands));
    payload.insert("post_tool_use".to_string(), json!(snapshot.post_commands));
    Ok(serde_json::Value::Object(payload))
}

fn mcp_transport_payload(detail: &McpServerDetailSnapshot) -> serde_json::Value {
    match detail {
        McpServerDetailSnapshot::Stdio {
            command,
            args,
            env_var_count,
        } => json!({
            "kind": "stdio",
            "command": command,
            "args": args,
            "env_var_count": env_var_count,
            "target": if args.is_empty() {
                command.clone()
            } else {
                format!("{} {}", command, args.join(" "))
            },
        }),
        McpServerDetailSnapshot::HttpLike {
            target,
            auth,
            headers_count,
            headers_helper,
        } => json!({
            "kind": "connection",
            "target": target,
            "auth": auth,
            "headers_count": headers_count,
            "headers_helper": headers_helper,
        }),
        McpServerDetailSnapshot::Sdk { name } => json!({
            "kind": "sdk",
            "name": name,
            "target": format!("sdk:{name}"),
        }),
        McpServerDetailSnapshot::SimcoeAiProxy { target, proxy_id } => json!({
            "kind": "simcoe-ai-proxy",
            "target": target,
            "proxy_id": proxy_id,
        }),
    }
}

fn mcp_server_payload(server: &McpServerSnapshot) -> serde_json::Value {
    json!({
        "name": server.name.as_str(),
        "scope": server.scope,
        "transport": server.transport,
        "target": server.target.as_str(),
        "normalized_name": server.normalized_name.as_str(),
        "tool_prefix": server.tool_prefix.as_str(),
        "signature": server.signature.as_deref(),
        "supported_execution": server.supported_execution,
        "execution_detail": server.execution_detail.as_deref(),
        "runtime": {
            "transport": server.runtime.transport.as_str(),
            "status": server.runtime.status.as_str(),
            "reason_kind": server.runtime.reason_kind.map(runtime::McpReasonKind::as_str),
            "detail": server.runtime.detail.as_deref(),
            "auth_kind": server.runtime.auth_kind.as_str(),
            "requires_user_auth": server.runtime.requires_user_auth,
            "supported_execution": server.runtime.supported_execution,
            "interactive_supported": server.runtime.interactive_supported,
            "stored_credentials": server.runtime.stored_credentials,
            "refresh_token_present": server.runtime.refresh_token_present,
            "expires_at": server.runtime.expires_at,
            "scopes": server.runtime.scopes.clone(),
            "client_id": server.runtime.client_id.as_deref(),
            "callback_port": server.runtime.callback_port,
            "auth_server_metadata_url": server.runtime.auth_server_metadata_url.as_deref(),
            "xaa": server.runtime.xaa,
        },
        "details": mcp_transport_payload(&server.detail),
    })
}

fn mcp_attention_payload(server: &McpAttentionSnapshot) -> serde_json::Value {
    let hint = server
        .detail
        .as_deref()
        .and_then(runtime::mcp_reason_remediation_hint);
    json!({
        "name": server.name.as_str(),
        "transport": server.transport,
        "status": server.status.as_str(),
        "reason_kind": server.reason_kind.map(runtime::McpReasonKind::as_str),
        "detail": server.detail.as_deref(),
        "remediation_hint": hint,
    })
}

fn mcp_attention_payloads(servers: &[McpAttentionSnapshot]) -> Vec<serde_json::Value> {
    servers.iter().map(mcp_attention_payload).collect()
}

fn mcp_blocked_server_payload(server: &McpBlockedServerSnapshot) -> serde_json::Value {
    let hint = runtime::mcp_reason_remediation_hint(&server.detail);
    json!({
        "name": server.name.as_str(),
        "transport": server.transport,
        "reason_kind": server.reason_kind.as_str(),
        "detail": server.detail.as_str(),
        "remediation_hint": hint,
    })
}

fn mcp_blocked_server_payloads(servers: &[McpBlockedServerSnapshot]) -> Vec<serde_json::Value> {
    servers.iter().map(mcp_blocked_server_payload).collect()
}

fn mcp_collection_payload_fields(
    collection: Option<&McpCollectionSnapshot>,
) -> serde_json::Map<String, serde_json::Value> {
    let mut payload = serde_json::Map::new();
    payload.insert(
        "server_count".to_string(),
        json!(collection.map(|collection| collection.server_count)),
    );
    payload.insert(
        "transport_counts".to_string(),
        json!(collection.map(|collection| collection.transport_counts.clone())),
    );
    payload.insert(
        "status_counts".to_string(),
        json!(collection.map(|collection| collection.status_counts.clone())),
    );
    payload.insert(
        "supported_execution_count".to_string(),
        json!(collection.map(|collection| collection.supported_execution_count)),
    );
    payload.insert(
        "unsupported_execution_count".to_string(),
        json!(collection.map(|collection| collection.unsupported_execution_count)),
    );
    payload.insert(
        "attention_servers".to_string(),
        json!(collection.map(|collection| mcp_attention_payloads(&collection.attention_servers))),
    );
    payload.insert(
        "unsupported_servers".to_string(),
        json!(collection
            .map(|collection| mcp_blocked_server_payloads(&collection.unsupported_servers))),
    );
    payload
}

fn mcp_payload(server: Option<String>) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = mcp_report_snapshot(server.as_deref())?;
    let content = render_mcp_report_from_snapshot(&snapshot);
    let mut payload = content_payload_map("mcp", content);

    if let Some(server) = snapshot.selected_server.as_ref() {
        payload.insert("server".to_string(), mcp_server_payload(server));
        return Ok(serde_json::Value::Object(payload));
    }

    let entries = snapshot
        .servers
        .iter()
        .map(mcp_server_payload)
        .collect::<Vec<_>>();

    payload.extend(mcp_collection_payload_fields(Some(&snapshot.collection)));

    payload.insert(
        "configured_server_count".to_string(),
        json!(snapshot.collection.server_count),
    );
    payload.insert("servers".to_string(), json!(entries));
    Ok(serde_json::Value::Object(payload))
}

fn remote_transport_metadata_payload(snapshot: &RemoteEnvReportSnapshot) -> serde_json::Value {
    let ready = snapshot.bootstrap.should_enable();
    let live_remote_transport = runtime::upstream_proxy_live_transport_status(
        &snapshot.bootstrap,
        &snapshot.websocket_probe,
    );
    let ws_url = (!snapshot.remote.base_url.is_empty()).then(|| snapshot.bootstrap.ws_url());

    json!({
        "kind": if ready { "upstream-proxy" } else { "local" },
        "active_transport_kind": "api-stream",
        "capabilities": {
            "structured_local_events": true,
            "live_remote_transport": false,
            "live_remote_transport_kind": "upstream-proxy-websocket",
            "live_remote_transport_ready": live_remote_transport.ready,
            "live_remote_transport_path_ready": live_remote_transport.path_ready,
            "live_remote_transport_selected": false,
            "live_remote_transport_blocker_kind": live_remote_transport.blocker_kind,
            "live_remote_transport_blocker_detail": live_remote_transport.blocker_detail,
        },
        "bootstrap": {
            "remote_enabled": snapshot.remote.enabled,
            "session_id": snapshot.remote.session_id.clone(),
            "base_url": (!snapshot.remote.base_url.is_empty()).then(|| snapshot.remote.base_url.clone()),
            "upstream_proxy_enabled": snapshot.bootstrap.upstream_proxy_enabled,
            "ready": ready,
            "ws_url": ws_url,
            "websocket_probe": {
                "requested": snapshot.websocket_probe.requested,
                "attempted": snapshot.websocket_probe.attempted,
                "reachable": snapshot.websocket_probe.reachable,
                "status": snapshot.websocket_probe.status,
                "detail": snapshot.websocket_probe.detail.clone(),
            },
            "token_path": snapshot.bootstrap.token_path.display().to_string(),
            "token_present": snapshot.bootstrap.token.is_some(),
            "ca_bundle_path": snapshot.bootstrap.ca_bundle_path.display().to_string(),
            "system_ca_path": snapshot.bootstrap.system_ca_path.display().to_string(),
            "inherited_proxy_env_count": snapshot.inherited_proxy_env_keys.len(),
            "inherited_proxy_env_keys": snapshot.inherited_proxy_env_keys,
            "missing": snapshot.bootstrap.missing_requirements(),
        },
    })
}

fn remote_env_payload() -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = remote_env_report_snapshot();
    let mut payload = content_payload_map(
        "remote_env",
        render_remote_env_report_from_snapshot(&snapshot),
    );
    payload.insert(
        "transport".to_string(),
        remote_transport_metadata_payload(&snapshot),
    );
    Ok(serde_json::Value::Object(payload))
}

fn remote_setup_payload() -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = remote_setup_report_snapshot()?;
    let mut payload = content_payload_map(
        "remote_setup",
        render_remote_setup_report_from_snapshot(&snapshot),
    );
    payload.insert(
        "transport".to_string(),
        remote_transport_metadata_payload(&snapshot.env),
    );
    payload.insert(
        "snapshot".to_string(),
        json!({
            "archive_name": snapshot.catalog.archive_name,
            "package_name": snapshot.catalog.package_name,
            "module_count": snapshot.catalog.module_count,
            "transport_files": snapshot.catalog.transport_files,
            "upstream_proxy": snapshot.catalog.upstream_proxy.as_ref().map(|proxy| json!({
                "archive_name": proxy.archive_name,
                "package_name": proxy.package_name,
                "module_count": proxy.module_count,
                "files": proxy.files,
            })),
            "command": {
                "name": snapshot.command.name,
                "summary": snapshot.command.summary,
                "source_hints": snapshot.command.source_hints,
                "archived_file_count": snapshot.command.archived_file_count,
            },
        }),
    );
    Ok(serde_json::Value::Object(payload))
}

fn agents_payload(agent: Option<String>) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = agents_report_snapshot(agent.as_deref())?;
    let content = render_agents_report_from_snapshot(&snapshot);
    let mut payload = content_payload_map("agents", content);

    if let Some(profile) = snapshot.selected_profile.as_ref() {
        let counts = snapshot.selected_task_counts.unwrap_or_default();
        payload.insert("profile".to_string(), json!(profile));
        payload.insert(
            "task_counts".to_string(),
            json!({
                "running": counts.running,
                "completed": counts.completed,
                "failed": counts.failed,
            }),
        );
        payload.insert(
            "recent_tasks".to_string(),
            json!(snapshot.selected_recent_tasks),
        );
        return Ok(serde_json::Value::Object(payload));
    }

    let profiles = snapshot
        .profiles
        .iter()
        .map(|profile| {
            json!({
                "name": profile.name,
                "description": profile.description,
                "aliases": profile.aliases,
                "tool_count": profile.tool_count,
                "recent_task_count": profile.recent_task_count,
            })
        })
        .collect::<Vec<_>>();

    payload.insert("available_count".to_string(), json!(profiles.len()));
    payload.insert(
        "persisted_task_count".to_string(),
        json!(snapshot.persisted_task_count),
    );
    payload.insert("profiles".to_string(), json!(profiles));
    Ok(serde_json::Value::Object(payload))
}

fn tasks_payload(task: Option<String>) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = tasks_report_snapshot(task.as_deref())?;
    let content = render_tasks_report_from_snapshot(&snapshot);
    let mut payload = content_payload_map("tasks", content);

    if let Some(loaded) = snapshot.selected_task.as_ref() {
        payload.insert("task".to_string(), json!(loaded.task));
        payload.insert("output".to_string(), json!(loaded.output));
        return Ok(serde_json::Value::Object(payload));
    }

    let counts = snapshot.task_counts.unwrap_or_default();

    payload.insert(
        "task_counts".to_string(),
        json!({
            "persisted": snapshot.tasks.len(),
            "running": counts.running,
            "completed": counts.completed,
            "failed": counts.failed,
        }),
    );
    payload.insert("tasks".to_string(), json!(snapshot.tasks));
    Ok(serde_json::Value::Object(payload))
}

fn memory_payload() -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = memory_report_snapshot()?;
    let content = render_memory_report_from_snapshot(&snapshot);
    let instruction_files = snapshot
        .instruction_files
        .iter()
        .map(|file| {
            json!({
                "path": file.path,
                "line_count": file.line_count,
                "preview": file.preview,
            })
        })
        .collect::<Vec<_>>();

    let mut payload = content_payload_map("memory", content);
    payload.insert(
        "working_directory".to_string(),
        json!(snapshot.working_directory),
    );
    payload.insert(
        "instruction_file_count".to_string(),
        json!(instruction_files.len()),
    );
    payload.insert("instruction_files".to_string(), json!(instruction_files));
    Ok(serde_json::Value::Object(payload))
}

fn skills_payload(skill: Option<String>) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = skills_report_snapshot(skill.as_deref())?;
    let content = render_skills_report_from_snapshot(&snapshot);
    let mut payload = content_payload_map("skills", content);

    if let Some(loaded) = snapshot.selected_skill.as_ref() {
        payload.insert("skill".to_string(), json!(loaded));
        return Ok(serde_json::Value::Object(payload));
    }

    if let Some(archived) = snapshot.selected_archived_skill.as_ref() {
        payload.insert(
            "archived_skill".to_string(),
            archived_skill_payload(archived),
        );
        return Ok(serde_json::Value::Object(payload));
    }

    payload.insert("available_count".to_string(), json!(snapshot.skills.len()));
    payload.insert("skills".to_string(), json!(snapshot.skills));
    if let Some(catalog) = snapshot.archived_catalog.as_ref() {
        payload.insert(
            "archived".to_string(),
            archived_skill_catalog_payload(catalog),
        );
    }
    Ok(serde_json::Value::Object(payload))
}

fn archived_skill_payload(skill: &compat_harness::ArchivedSkillSummary) -> serde_json::Value {
    json!({
        "name": skill.name,
        "summary": skill.summary,
        "source_hints": skill.source_hints,
        "archived_file_count": skill.archived_file_count,
    })
}

fn archived_skill_catalog_payload(catalog: &compat_harness::SkillCatalog) -> serde_json::Value {
    json!({
        "archive_name": catalog.archive_name,
        "package_name": catalog.package_name,
        "module_count": catalog.module_count,
        "bundled_skill_sample_count": catalog.bundled_skill_samples.len(),
        "support_module_count": catalog.support_modules.len(),
        "bundled_skill_samples": catalog
            .bundled_skill_samples
            .iter()
            .map(archived_skill_payload)
            .collect::<Vec<_>>(),
        "support_modules": catalog.support_modules,
    })
}

fn plugin_surface_payload(surface: &compat_harness::PluginSurfaceSummary) -> serde_json::Value {
    json!({
        "name": surface.name,
        "kind": surface.kind.as_str(),
        "summary": surface.summary,
        "source_hints": surface.source_hints,
        "archived_file_count": surface.archived_file_count,
    })
}

fn plugin_payload(
    surface: Option<String>,
) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = plugin_report_snapshot(surface.as_deref())?;
    let content = render_plugin_report_from_snapshot(&snapshot)?;
    let mut payload = content_payload_map("plugin", content);

    if let Some(surface) = snapshot.selected_surface.as_ref() {
        payload.insert("surface".to_string(), plugin_surface_payload(surface));
        return Ok(serde_json::Value::Object(payload));
    }

    let catalog = snapshot
        .catalog
        .as_ref()
        .ok_or_else(|| io::Error::other("plugin catalog snapshot missing"))?;
    let command_count = catalog
        .surfaces
        .iter()
        .filter(|surface| matches!(surface.kind, PluginSurfaceKind::Command))
        .count();
    let module_surface_count = catalog
        .surfaces
        .iter()
        .filter(|surface| matches!(surface.kind, PluginSurfaceKind::Module))
        .count();
    let commands = catalog
        .surfaces
        .iter()
        .filter(|surface| matches!(surface.kind, PluginSurfaceKind::Command))
        .map(plugin_surface_payload)
        .collect::<Vec<_>>();
    let modules = catalog
        .surfaces
        .iter()
        .filter(|surface| matches!(surface.kind, PluginSurfaceKind::Module))
        .map(plugin_surface_payload)
        .collect::<Vec<_>>();

    payload.insert(
        "snapshot".to_string(),
        json!({
            "archive_name": catalog.archive_name,
            "package_name": catalog.package_name,
            "module_count": catalog.module_count,
            "sample_files": catalog.sample_files,
            "command_count": command_count,
            "module_surface_count": module_surface_count,
            "commands": commands,
            "modules": modules,
        }),
    );
    Ok(serde_json::Value::Object(payload))
}

fn reload_plugins_payload() -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = reload_plugins_report_snapshot()?;
    let mut payload = content_payload_map(
        "reload_plugins",
        render_reload_plugins_report_from_snapshot(&snapshot),
    );
    payload.insert(
        "snapshot".to_string(),
        json!({
            "archive_name": snapshot.catalog.archive_name,
            "package_name": snapshot.catalog.package_name,
            "module_count": snapshot.catalog.module_count,
            "sample_files": snapshot.catalog.sample_files,
            "surface": plugin_surface_payload(&snapshot.surface),
        }),
    );
    payload.insert("runtime_support".to_string(), json!("inspection only"));
    Ok(serde_json::Value::Object(payload))
}

fn doctor_payload() -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = doctor_snapshot()?;
    let content = render_doctor_report_from_snapshot(&snapshot);
    let sandbox = snapshot.config.sandbox.as_ref().map(|sandbox| {
        json!({
            "enabled": sandbox.enabled,
            "active": sandbox.active,
            "filesystem_mode": sandbox.filesystem_mode,
            "network_isolation": sandbox.network_isolation,
            "detail": sandbox.detail,
        })
    });

    let mut payload = content_payload_map("doctor", content);
    payload.insert("rust_status".to_string(), json!(snapshot.rust_status));
    payload.insert(
        "working_directory".to_string(),
        json!(snapshot.working_directory),
    );
    payload.insert("project_root".to_string(), json!(snapshot.project_root));
    payload.insert("git_branch".to_string(), json!(snapshot.git_branch));
    payload.insert(
        "instruction_file_count".to_string(),
        json!(snapshot.instruction_file_count),
    );
    payload.insert("issue_count".to_string(), json!(snapshot.issue_count));
    payload.insert("issues".to_string(), json!(snapshot.issues));
    payload.insert(
        "config".to_string(),
        json!({
            "status": snapshot.config.status,
            "discovered_file_count": snapshot.config.discovered_file_count,
            "loaded_file_count": snapshot.config.loaded_file_count,
            "error": snapshot.config.error,
            "provider": snapshot.config.provider,
            "model": snapshot.config.model,
            "permission_mode": snapshot.config.permission_mode,
            "sandbox": sandbox,
        }),
    );
    payload.insert(
        "auth".to_string(),
        json!({
            "oauth_configured": snapshot.auth.oauth_configured,
            "credentials_path": snapshot.auth.credentials_path,
            "stored_credentials_status": snapshot.auth.stored_credentials_status,
            "refresh_token_present": snapshot.auth.refresh_token_present,
            "expires_at": snapshot.auth.expires_at,
            "scopes": snapshot.auth.scopes,
        }),
    );
    payload.insert(
        "hooks".to_string(),
        json!({
            "pre_count": snapshot.hooks.pre_count,
            "post_count": snapshot.hooks.post_count,
        }),
    );
    payload.insert(
        "mcp".to_string(),
        serde_json::Value::Object(mcp_collection_payload_fields(snapshot.mcp.as_ref())),
    );
    payload.insert(
        "remote".to_string(),
        json!({
            "enabled": snapshot.remote.enabled,
            "proxy_ready": snapshot.remote.proxy_ready,
            "ws_path_ready": snapshot.remote.ws_path_ready,
            "live_blocker_kind": snapshot.remote.live_blocker_kind,
            "live_blocker_detail": snapshot.remote.live_blocker_detail,
            "websocket_probe": {
                "requested": snapshot.remote.websocket_probe.requested,
                "attempted": snapshot.remote.websocket_probe.attempted,
                "reachable": snapshot.remote.websocket_probe.reachable,
                "status": snapshot.remote.websocket_probe.status,
                "detail": snapshot.remote.websocket_probe.detail,
            },
            "session_id": snapshot.remote.session_id,
            "base_url": snapshot.remote.base_url,
            "missing_requirements": snapshot.remote.missing_requirements,
        }),
    );
    Ok(serde_json::Value::Object(payload))
}

fn rust_tool_summary_payload(spec: &InspectableTool) -> serde_json::Value {
    json!({
        "name": spec.name,
        "description": spec.description,
        "aliases": spec.aliases,
        "source": spec.source.as_str(),
        "required_permission": spec.required_permission.as_str(),
    })
}

fn rust_tool_detail_payload(spec: &InspectableTool) -> serde_json::Value {
    let mut payload = serde_json::Map::from_iter([
        ("name".to_string(), json!(spec.name)),
        ("description".to_string(), json!(spec.description)),
        ("source".to_string(), json!(spec.source.as_str())),
        (
            "required_permission".to_string(),
            json!(spec.required_permission.as_str()),
        ),
        ("aliases".to_string(), json!(spec.aliases)),
        ("input_schema".to_string(), spec.input_schema.clone()),
    ]);
    if let Some(output_schema) = spec.output_schema.clone() {
        payload.insert("output_schema".to_string(), output_schema);
    }
    serde_json::Value::Object(payload)
}

fn archived_tool_family_payload(
    family: &compat_harness::ArchivedToolFamilySummary,
) -> serde_json::Value {
    json!({
        "name": family.name,
        "summary": family.summary,
        "source_hints": family.source_hints,
        "archived_file_count": family.archived_file_count,
    })
}

fn tools_payload(tool: Option<String>) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let snapshot = tools_report_snapshot(tool.as_deref())?;
    let content = render_tools_report_from_snapshot(&snapshot)?;
    let mut payload = content_payload_map("tools", content);

    if let Some(requested) = snapshot.requested_tool.as_deref() {
        payload.insert("requested".to_string(), json!(requested));
        payload.insert(
            "rust_tool".to_string(),
            json!(snapshot
                .selected_rust_tool
                .as_ref()
                .map(rust_tool_detail_payload)),
        );
        payload.insert(
            "archived_family".to_string(),
            json!(snapshot
                .selected_archived_family
                .as_ref()
                .map(archived_tool_family_payload)),
        );
        return Ok(serde_json::Value::Object(payload));
    }

    let archived_catalog = snapshot.archived_catalog.as_ref();
    let archived_family_count = archived_catalog.map_or(0, |catalog| catalog.families.len());
    let archived_file_count = archived_catalog.map_or(0, |catalog| catalog.archived_file_count);
    let archived_families = archived_catalog.map_or_else(Vec::new, |catalog| {
        catalog
            .families
            .iter()
            .map(archived_tool_family_payload)
            .collect::<Vec<_>>()
    });
    let registry_tool_count = snapshot
        .rust_tools
        .iter()
        .filter(|tool| tool.source == InspectableToolSource::Registry)
        .count();
    let dynamic_mcp_tool_count = snapshot
        .rust_tools
        .iter()
        .filter(|tool| tool.source == InspectableToolSource::DynamicMcp)
        .count();

    payload.insert(
        "rust_registry".to_string(),
        json!({
            "tool_count": snapshot.rust_tools.len(),
            "registry_tool_count": registry_tool_count,
            "dynamic_mcp_tool_count": dynamic_mcp_tool_count,
            "pending_mcp_servers": snapshot
                .pending_mcp_servers
                .iter()
                .map(|entry| entry.server.clone())
                .collect::<Vec<_>>(),
            "pending_mcp_server_details": snapshot.pending_mcp_servers,
            "tools": snapshot
                .rust_tools
                .iter()
                .map(rust_tool_summary_payload)
                .collect::<Vec<_>>(),
        }),
    );
    payload.insert(
        "archived_snapshot".to_string(),
        json!({
            "available": archived_catalog.is_some(),
            "family_count": archived_family_count,
            "archived_file_count": archived_file_count,
            "families": archived_families,
        }),
    );
    Ok(serde_json::Value::Object(payload))
}

fn run_repl(
    model: String,
    provider: Option<String>,
    allowed_tools: Option<AllowedToolSet>,
    permission_mode: PermissionMode,
) -> Result<(), Box<dyn std::error::Error>> {
    let mut cli = LiveCli::new(model, provider, true, allowed_tools, permission_mode, true)?;
    let mut editor = input::LineEditor::new("> ", slash_command_completion_candidates());
    println!("{}", cli.startup_banner());
    let _ = cli.render_status_bar();

    loop {
        let _ = cli.render_status_bar();
        match editor.read_line()? {
            input::ReadOutcome::Submit(input) => {
                let trimmed = input.trim().to_string();
                if trimmed.is_empty() {
                    let _ = cli.render_status_bar();
                    continue;
                }
                if matches!(trimmed.as_str(), "/exit" | "/quit") {
                    let _ = cli.clear_status_bar();
                    cli.persist_session()?;
                    break;
                }
                if let Some(command) = SlashCommand::parse(&trimmed) {
                    let _ = cli.clear_status_bar();
                    if cli.handle_repl_command(command)? {
                        cli.persist_session()?;
                    }
                    let _ = cli.render_status_bar();
                    continue;
                }

                editor.push_history(input);
                let _ = cli.clear_status_bar();
                let result = cli.run_turn(&trimmed);
                let _ = cli.render_status_bar();
                result?;
            }
            input::ReadOutcome::Cancel => {
                println!();
                let _ = cli.render_status_bar();
            }
            input::ReadOutcome::Exit => {
                let _ = cli.clear_status_bar();
                cli.persist_session()?;
                break;
            }
        }
    }

    let _ = cli.clear_status_bar();
    Ok(())
}

pub(crate) fn current_working_directory() -> io::Result<PathBuf> {
    env::current_dir()
}

pub(crate) fn config_loader_in_current_dir() -> io::Result<(PathBuf, ConfigLoader)> {
    let cwd = current_working_directory()?;
    Ok((cwd.clone(), ConfigLoader::default_for(&cwd)))
}

fn init_simcoe_md_at(cwd: &Path) -> Result<String, Box<dyn std::error::Error>> {
    Ok(initialize_repo(cwd)?.render())
}

fn init_simcoe_md() -> Result<String, Box<dyn std::error::Error>> {
    let cwd = current_working_directory()?;
    init_simcoe_md_at(&cwd)
}

fn init_payload() -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let cwd = current_working_directory()?;
    let mut payload = content_payload_map("init", init_simcoe_md_at(&cwd)?);
    payload.insert("cwd".to_string(), json!(cwd.display().to_string()));
    Ok(serde_json::Value::Object(payload))
}

fn run_init(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(output_format, init_simcoe_md, init_payload)
}

pub(crate) fn command_in_current_dir(program: &str) -> io::Result<Command> {
    let mut command = Command::new(program);
    command.current_dir(current_working_directory()?);
    Ok(command)
}

fn git_output(args: &[&str]) -> Result<String, Box<dyn std::error::Error>> {
    let output = command_in_current_dir("git")?.args(args).output()?;
    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr).trim().to_string();
        return Err(format!("git {} failed: {stderr}", args.join(" ")).into());
    }
    Ok(String::from_utf8(output.stdout)?)
}

fn git_status_ok(args: &[&str]) -> Result<(), Box<dyn std::error::Error>> {
    let output = command_in_current_dir("git")?.args(args).output()?;
    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr).trim().to_string();
        return Err(format!("git {} failed: {stderr}", args.join(" ")).into());
    }
    Ok(())
}

fn command_exists(name: &str) -> bool {
    Command::new("which")
        .arg(name)
        .output()
        .map(|output| output.status.success())
        .unwrap_or(false)
}

fn write_temp_text_file(
    file_name: &str,
    contents: &str,
) -> Result<PathBuf, Box<dyn std::error::Error>> {
    let path = std::env::temp_dir().join(file_name);
    fs::write(&path, contents)?;
    Ok(path)
}

fn bootstrap_plan_report() -> String {
    bootstrap_plan_phases()
        .into_iter()
        .map(|phase| format!("- {phase}"))
        .collect::<Vec<_>>()
        .join("\n")
}

fn bootstrap_plan_phases() -> Vec<String> {
    runtime::BootstrapPlan::simcoe_ai_default()
        .phases()
        .iter()
        .map(|phase| format!("{phase:?}"))
        .collect()
}

fn bootstrap_plan_payload() -> serde_json::Value {
    json!({
        "type": "bootstrap_plan",
        "phases": bootstrap_plan_phases(),
    })
}

fn run_text_or_structured_command(
    output_format: CliOutputFormat,
    render_text: impl FnOnce() -> Result<String, Box<dyn std::error::Error>>,
    build_payload: impl FnOnce() -> Result<serde_json::Value, Box<dyn std::error::Error>>,
) -> Result<(), Box<dyn std::error::Error>> {
    match output_format {
        CliOutputFormat::Text => println!("{}", render_text()?),
        CliOutputFormat::Json | CliOutputFormat::Ndjson => {
            emit_noninteractive_payload(output_format, &build_payload()?)?
        }
    }
    Ok(())
}

fn run_selector_text_or_structured_command(
    selector: Option<String>,
    output_format: CliOutputFormat,
    render_text: impl FnOnce(Option<&str>) -> Result<String, Box<dyn std::error::Error>>,
    build_payload: impl FnOnce(Option<String>) -> Result<serde_json::Value, Box<dyn std::error::Error>>,
) -> Result<(), Box<dyn std::error::Error>> {
    let report_selector = selector.clone();
    run_text_or_structured_command(
        output_format,
        move || render_text(report_selector.as_deref()),
        move || build_payload(selector),
    )
}

fn run_bootstrap_plan(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(
        output_format,
        || Ok(bootstrap_plan_report()),
        || Ok(bootstrap_plan_payload()),
    )
}

fn run_config(
    section: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    run_selector_text_or_structured_command(
        section,
        output_format,
        render_config_report,
        config_payload,
    )
}

fn run_hooks(
    event: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    run_selector_text_or_structured_command(
        event,
        output_format,
        render_hooks_report,
        hooks_payload,
    )
}

fn run_mcp(
    server: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    run_selector_text_or_structured_command(server, output_format, render_mcp_report, mcp_payload)
}

fn run_memory(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(output_format, render_memory_report, memory_payload)
}

fn run_agents(
    agent: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    run_selector_text_or_structured_command(
        agent,
        output_format,
        render_agents_report,
        agents_payload,
    )
}

fn run_plugin(
    surface: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    run_selector_text_or_structured_command(
        surface,
        output_format,
        render_plugin_report,
        plugin_payload,
    )
}

fn run_reload_plugins(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(
        output_format,
        render_reload_plugins_report,
        reload_plugins_payload,
    )
}

fn run_remote_env(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(output_format, render_remote_env_report, remote_env_payload)
}

fn run_remote_setup(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(
        output_format,
        render_remote_setup_report,
        remote_setup_payload,
    )
}

fn run_tools(
    tool: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    run_selector_text_or_structured_command(tool, output_format, render_tools_report, tools_payload)
}

fn run_doctor(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(output_format, render_doctor_report, doctor_payload)
}

fn run_skills(
    skill: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    run_selector_text_or_structured_command(
        skill,
        output_format,
        render_skills_report,
        skills_payload,
    )
}

fn run_tasks(
    task: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    run_selector_text_or_structured_command(task, output_format, render_tasks_report, tasks_payload)
}

fn export_report(export_path: &Path, message_count: usize) -> String {
    format!(
        "Export\n  Result           wrote transcript\n  File             {}\n  Messages         {}",
        export_path.display(),
        message_count,
    )
}

fn export_payload(
    handle: &SessionHandle,
    export_path: &Path,
    message_count: usize,
) -> serde_json::Value {
    let mut payload = content_payload_map("export", export_report(export_path, message_count));
    payload.insert("session_id".to_string(), json!(handle.id));
    payload.insert(
        "session_path".to_string(),
        json!(handle.path.display().to_string()),
    );
    payload.insert(
        "export_path".to_string(),
        json!(export_path.display().to_string()),
    );
    payload.insert("message_count".to_string(), json!(message_count));
    serde_json::Value::Object(payload)
}

fn export_active_session(
    requested_path: Option<String>,
) -> Result<(SessionHandle, PathBuf, usize), Box<dyn std::error::Error>> {
    runtime::export_active_session(requested_path.as_deref())
}

fn run_export(
    requested_path: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    let (handle, export_path, message_count) = export_active_session(requested_path)?;
    let report_path = export_path.clone();
    let payload_path = export_path.clone();
    run_text_or_structured_command(
        output_format,
        move || Ok(export_report(&report_path, message_count)),
        move || Ok(export_payload(&handle, &payload_path, message_count)),
    )
}

fn run_session(
    action: Option<String>,
    target: Option<String>,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    match action.as_deref() {
        None | Some("list") => {
            run_text_or_structured_command(output_format, session_list_report, session_list_payload)
        }
        Some("switch") => {
            let target = target.ok_or_else(|| {
                io::Error::new(
                    io::ErrorKind::InvalidInput,
                    "session switch requires a session id or path",
                )
            })?;
            let (handle, message_count) = switch_managed_session(&target)?;
            let report_handle = handle.clone();
            let payload_handle = handle.clone();
            run_text_or_structured_command(
                output_format,
                move || Ok(session_switch_report(&report_handle, message_count)),
                move || session_switch_payload(&payload_handle, message_count),
            )
        }
        Some(other) => Err(io::Error::new(
            io::ErrorKind::InvalidInput,
            format!(
                "unknown session action '{other}'. Use `session list` or `session switch <session-id>`."
            ),
        )
        .into()),
    }
}

fn oauth_config_for_login<'a>(
    oauth: Option<&'a OAuthConfig>,
) -> Result<&'a OAuthConfig, io::Error> {
    oauth.ok_or_else(|| {
        io::Error::new(
            io::ErrorKind::NotFound,
            "missing oauth config; add an `oauth` block to .simcoe.json before running `claw login`",
        )
    })
}

fn login_start_record(redirect_uri: &str) -> serde_json::Value {
    json!({
        "type": "login",
        "event": "start",
        "message": "Starting Simcoe AI OAuth login.",
        "redirect_uri": redirect_uri,
    })
}

fn login_browser_opened_record() -> serde_json::Value {
    json!({
        "type": "login",
        "event": "browser_opened",
        "message": "Opened the authorization URL in a browser.",
    })
}

fn login_browser_warning_record(error: &str, authorize_url: &str) -> serde_json::Value {
    json!({
        "type": "login",
        "event": "browser_warning",
        "message": format!("failed to open browser automatically: {error}"),
        "authorize_url": authorize_url,
    })
}

fn login_complete_record(
    redirect_uri: &str,
    browser_opened: bool,
    browser_open_error: Option<&str>,
) -> serde_json::Value {
    json!({
        "type": "login",
        "event": "complete",
        "message": "Simcoe AI OAuth login complete.",
        "redirect_uri": redirect_uri,
        "browser_opened": browser_opened,
        "browser_open_error": browser_open_error,
    })
}

fn logout_payload() -> serde_json::Value {
    json!({
        "type": "logout",
        "credentials_cleared": true,
        "message": "Simcoe AI OAuth credentials cleared.",
    })
}

fn emit_ndjson_record(record: &serde_json::Value) -> Result<(), Box<dyn std::error::Error>> {
    println!("{}", serde_json::to_string(record)?);
    Ok(())
}

fn run_login(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    if matches!(output_format, CliOutputFormat::Json) {
        return Err(Box::new(CliExitError::new(
            "`claw login` does not support --output-format json; use text or ndjson because the OAuth flow may require manual browser fallback instructions.",
            2,
        )));
    }

    let (_, loader) = config_loader_in_current_dir()?;
    let config = loader.load()?;
    let oauth = oauth_config_for_login(config.oauth())?;
    let callback_port = oauth.callback_port.unwrap_or(DEFAULT_OAUTH_CALLBACK_PORT);
    let redirect_uri = runtime::loopback_redirect_uri(callback_port);
    let pkce = generate_pkce_pair()?;
    let state = generate_state()?;
    let authorize_url =
        OAuthAuthorizationRequest::from_config(oauth, redirect_uri.clone(), state.clone(), &pkce)
            .build_url();

    match output_format {
        CliOutputFormat::Text => {
            println!("Starting Simcoe AI OAuth login...");
            println!("Listening for callback on {redirect_uri}");
        }
        CliOutputFormat::Ndjson => emit_ndjson_record(&login_start_record(&redirect_uri))?,
        CliOutputFormat::Json => unreachable!("login JSON output is rejected above"),
    }

    let (browser_opened, browser_open_error) = match open_browser(&authorize_url) {
        Ok(()) => {
            if matches!(output_format, CliOutputFormat::Ndjson) {
                emit_ndjson_record(&login_browser_opened_record())?;
            }
            (true, None)
        }
        Err(error) => {
            let message = error.to_string();
            match output_format {
                CliOutputFormat::Text => {
                    eprintln!("warning: failed to open browser automatically: {message}");
                    println!("Open this URL manually:\n{authorize_url}");
                }
                CliOutputFormat::Ndjson => {
                    emit_ndjson_record(&login_browser_warning_record(&message, &authorize_url))?;
                }
                CliOutputFormat::Json => unreachable!("login JSON output is rejected above"),
            }
            (false, Some(message))
        }
    };

    let callback = wait_for_oauth_callback(callback_port)?;
    if let Some(error) = callback.error {
        let description = callback
            .error_description
            .unwrap_or_else(|| "authorization failed".to_string());
        return Err(io::Error::other(format!("{error}: {description}")).into());
    }
    let code = callback.code.ok_or_else(|| {
        io::Error::new(io::ErrorKind::InvalidData, "callback did not include code")
    })?;
    let returned_state = callback.state.ok_or_else(|| {
        io::Error::new(io::ErrorKind::InvalidData, "callback did not include state")
    })?;
    if returned_state != state {
        return Err(io::Error::new(io::ErrorKind::InvalidData, "oauth state mismatch").into());
    }

    let client = SimcoeApiClient::from_auth(AuthSource::None);
    let exchange_request =
        OAuthTokenExchangeRequest::from_config(oauth, code, state, pkce.verifier, &redirect_uri);
    let runtime = tokio::runtime::Runtime::new()?;
    let token_set = runtime.block_on(client.exchange_oauth_code(oauth, &exchange_request))?;
    save_oauth_credentials(&runtime::OAuthTokenSet {
        access_token: token_set.access_token,
        refresh_token: token_set.refresh_token,
        expires_at: token_set.expires_at,
        scopes: token_set.scopes,
    })?;
    match output_format {
        CliOutputFormat::Text => println!("Simcoe AI OAuth login complete."),
        CliOutputFormat::Ndjson => emit_ndjson_record(&login_complete_record(
            &redirect_uri,
            browser_opened,
            browser_open_error.as_deref(),
        ))?,
        CliOutputFormat::Json => unreachable!("login JSON output is rejected above"),
    }
    Ok(())
}

fn run_logout(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    clear_oauth_credentials()?;
    run_text_or_structured_command(
        output_format,
        || Ok("Simcoe AI OAuth credentials cleared.".to_string()),
        || Ok(logout_payload()),
    )
}

fn open_browser(url: &str) -> io::Result<()> {
    let commands = if cfg!(target_os = "macos") {
        vec![("open", vec![url])]
    } else if cfg!(target_os = "windows") {
        vec![("cmd", vec!["/C", "start", "", url])]
    } else {
        vec![("xdg-open", vec![url])]
    };
    for (program, args) in commands {
        match Command::new(program).args(args).spawn() {
            Ok(_) => return Ok(()),
            Err(error) if error.kind() == io::ErrorKind::NotFound => {}
            Err(error) => return Err(error),
        }
    }
    Err(io::Error::new(
        io::ErrorKind::NotFound,
        "no supported browser opener command found",
    ))
}

fn wait_for_oauth_callback(
    port: u16,
) -> Result<runtime::OAuthCallbackParams, Box<dyn std::error::Error>> {
    let listener = TcpListener::bind(("127.0.0.1", port))?;
    let (mut stream, _) = listener.accept()?;
    let mut buffer = [0_u8; 4096];
    let bytes_read = stream.read(&mut buffer)?;
    let request = String::from_utf8_lossy(&buffer[..bytes_read]);
    let request_line = request.lines().next().ok_or_else(|| {
        io::Error::new(io::ErrorKind::InvalidData, "missing callback request line")
    })?;
    let target = request_line.split_whitespace().nth(1).ok_or_else(|| {
        io::Error::new(
            io::ErrorKind::InvalidData,
            "missing callback request target",
        )
    })?;
    let callback = parse_oauth_callback_request_target(target)
        .map_err(|error| io::Error::new(io::ErrorKind::InvalidData, error))?;
    let body = if callback.error.is_some() {
        "Simcoe AI OAuth login failed. You can close this window."
    } else {
        "Simcoe AI OAuth login succeeded. You can close this window."
    };
    let response = format!(
        "HTTP/1.1 200 OK\r\ncontent-type: text/plain; charset=utf-8\r\ncontent-length: {}\r\nconnection: close\r\n\r\n{}",
        body.len(),
        body
    );
    stream.write_all(response.as_bytes())?;
    Ok(callback)
}

fn parse_system_prompt_command_args(
    args: Option<&str>,
) -> Result<(PathBuf, String), Box<dyn std::error::Error>> {
    let mut cwd = current_working_directory()?;
    let mut date = DEFAULT_DATE.to_string();
    let tokens = args
        .map(str::trim)
        .filter(|value| !value.is_empty())
        .map(|value| value.split_whitespace().collect::<Vec<_>>())
        .unwrap_or_default();
    let mut index = 0;

    while index < tokens.len() {
        match tokens[index] {
            "--cwd" => {
                let value = tokens.get(index + 1).ok_or_else(|| {
                    io::Error::new(io::ErrorKind::InvalidInput, "missing value for --cwd")
                })?;
                cwd = PathBuf::from(value);
                index += 2;
            }
            "--date" => {
                let value = tokens.get(index + 1).ok_or_else(|| {
                    io::Error::new(io::ErrorKind::InvalidInput, "missing value for --date")
                })?;
                date = (*value).to_string();
                index += 2;
            }
            other => {
                return Err(io::Error::new(
                    io::ErrorKind::InvalidInput,
                    format!("unknown system-prompt option: {other}"),
                )
                .into())
            }
        }
    }

    Ok((cwd, date))
}

fn system_prompt_report(cwd: PathBuf, date: String) -> Result<String, Box<dyn std::error::Error>> {
    let sections = system_prompt_sections(&cwd, &date)?;
    Ok(sections.join("\n\n"))
}

fn system_prompt_sections(
    cwd: &Path,
    date: &str,
) -> Result<Vec<String>, Box<dyn std::error::Error>> {
    Ok(load_system_prompt(
        cwd.to_path_buf(),
        date.to_string(),
        env::consts::OS,
        "unknown",
    )?)
}

fn system_prompt_payload(
    cwd: &Path,
    date: &str,
) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let sections = system_prompt_sections(cwd, date)?;
    let mut payload = content_payload_map(
        "system_prompt",
        system_prompt_report(cwd.to_path_buf(), date.to_string())?,
    );
    payload.insert("cwd".to_string(), json!(cwd.display().to_string()));
    payload.insert("date".to_string(), json!(date));
    payload.insert("sections".to_string(), json!(sections));
    Ok(serde_json::Value::Object(payload))
}

fn run_system_prompt(
    cwd: PathBuf,
    date: String,
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    let report_cwd = cwd.clone();
    let report_date = date.clone();
    run_text_or_structured_command(
        output_format,
        move || system_prompt_report(report_cwd, report_date),
        move || system_prompt_payload(&cwd, &date),
    )
}

fn version_payload() -> serde_json::Value {
    let mut payload = content_payload_map("version", render_version_report());
    payload.insert("version".to_string(), json!(VERSION));
    payload.insert("build_target".to_string(), json!(BUILD_TARGET));
    payload.insert("git_sha".to_string(), json!(GIT_SHA));
    serde_json::Value::Object(payload)
}

fn run_version(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(
        output_format,
        || Ok(render_version_report()),
        || Ok(version_payload()),
    )
}

fn run_dump_manifests(output_format: CliOutputFormat) -> Result<(), Box<dyn std::error::Error>> {
    run_text_or_structured_command(output_format, dump_manifests_report, dump_manifests_payload)
}

fn emit_noninteractive_payload(
    output_format: CliOutputFormat,
    payload: &serde_json::Value,
) -> Result<(), Box<dyn std::error::Error>> {
    match output_format {
        CliOutputFormat::Text => println!("{payload}"),
        CliOutputFormat::Json => println!("{payload}"),
        CliOutputFormat::Ndjson => println!("{}", serde_json::to_string(payload)?),
    }
    Ok(())
}

fn resume_session(
    session_path: &Path,
    commands: &[String],
    output_format: CliOutputFormat,
) -> Result<(), Box<dyn std::error::Error>> {
    let session = Session::load_from_path(session_path).map_err(|error| {
        Box::new(
            CliExitError::new(format!("failed to restore session: {error}"), 1)
                .with_operation("resume"),
        ) as Box<dyn std::error::Error>
    })?;

    let mut current_session_path = session_path.to_path_buf();
    let initial_message_count = session.messages.len();

    if commands.is_empty() {
        match output_format {
            CliOutputFormat::Text => {
                println!(
                    "{}",
                    restored_session_message(session_path, initial_message_count)
                );
            }
            CliOutputFormat::Json => {
                println!(
                    "{}",
                    build_resume_json_payload(
                        current_session_path.as_path(),
                        initial_message_count,
                        Vec::new(),
                        initial_message_count,
                    )
                );
            }
            CliOutputFormat::Ndjson => {
                println!(
                    "{}",
                    build_resume_start_record(session_path, initial_message_count)
                );
                println!(
                    "{}",
                    build_resume_summary_record(
                        current_session_path.as_path(),
                        initial_message_count,
                        initial_message_count,
                        0,
                    )
                );
            }
        }
        return Ok(());
    }

    let mut session = session;
    let mut command_records = Vec::new();
    if matches!(output_format, CliOutputFormat::Ndjson) {
        println!(
            "{}",
            build_resume_start_record(session_path, initial_message_count)
        );
    }
    for (index, raw_command) in commands.iter().enumerate() {
        let Some(command) = SlashCommand::parse(raw_command) else {
            return Err(Box::new(
                CliExitError::new(format!("unsupported resumed command: {raw_command}"), 2)
                    .with_operation("resume")
                    .with_command(raw_command.clone()),
            ));
        };
        match run_resume_command(current_session_path.as_path(), &session, &command) {
            Ok(ResumeCommandOutcome {
                session: next_session,
                session_path: next_session_path,
                message,
            }) => {
                let changed_session =
                    next_session != session || next_session_path != current_session_path;
                match output_format {
                    CliOutputFormat::Text => {
                        if let Some(message) = &message {
                            println!("{message}");
                        }
                    }
                    CliOutputFormat::Json => command_records.push(build_resume_command_record(
                        index,
                        raw_command,
                        message.as_deref(),
                        next_session.messages.len(),
                        changed_session,
                    )),
                    CliOutputFormat::Ndjson => println!(
                        "{}",
                        build_resume_command_record(
                            index,
                            raw_command,
                            message.as_deref(),
                            next_session.messages.len(),
                            changed_session,
                        )
                    ),
                }
                current_session_path = next_session_path;
                session = next_session;
            }
            Err(error) => {
                return Err(Box::new(
                    CliExitError::new(error.to_string(), 2)
                        .with_operation("resume")
                        .with_command(raw_command.clone()),
                ));
            }
        }
    }

    match output_format {
        CliOutputFormat::Text => {}
        CliOutputFormat::Json => println!(
            "{}",
            build_resume_json_payload(
                current_session_path.as_path(),
                initial_message_count,
                command_records,
                session.messages.len(),
            )
        ),
        CliOutputFormat::Ndjson => println!(
            "{}",
            build_resume_summary_record(
                current_session_path.as_path(),
                initial_message_count,
                session.messages.len(),
                commands.len(),
            )
        ),
    }

    Ok(())
}

fn restored_session_message(session_path: &Path, message_count: usize) -> String {
    format!(
        "Restored session from {} ({} messages).",
        session_path.display(),
        message_count
    )
}

#[derive(Debug, Clone)]
struct ResumeCommandOutcome {
    session: Session,
    session_path: PathBuf,
    message: Option<String>,
}

fn resume_command_outcome(
    session_path: &Path,
    session: Session,
    message: Option<String>,
) -> ResumeCommandOutcome {
    ResumeCommandOutcome {
        session,
        session_path: session_path.to_path_buf(),
        message,
    }
}

fn render_resume_read_only_message(
    command: &SlashCommand,
) -> Result<Option<String>, Box<dyn std::error::Error>> {
    match command {
        SlashCommand::Help => Ok(Some(render_repl_help())),
        SlashCommand::DumpManifests => Ok(Some(dump_manifests_report()?)),
        SlashCommand::BootstrapPlan => Ok(Some(bootstrap_plan_report())),
        SlashCommand::Config { section } => Ok(Some(render_config_report(section.as_deref())?)),
        SlashCommand::SystemPrompt { args } => {
            let (cwd, date) = parse_system_prompt_command_args(args.as_deref())?;
            Ok(Some(system_prompt_report(cwd, date)?))
        }
        SlashCommand::Hooks { event } => Ok(Some(render_hooks_report(event.as_deref())?)),
        SlashCommand::Mcp { server } => Ok(Some(render_mcp_report(server.as_deref())?)),
        SlashCommand::Memory => Ok(Some(render_memory_report()?)),
        SlashCommand::Agents { agent } => Ok(Some(render_agents_report(agent.as_deref())?)),
        SlashCommand::Plugin { surface } => Ok(Some(render_plugin_report(surface.as_deref())?)),
        SlashCommand::ReloadPlugins => Ok(Some(render_reload_plugins_report()?)),
        SlashCommand::RemoteEnv => Ok(Some(render_remote_env_report()?)),
        SlashCommand::RemoteSetup => Ok(Some(render_remote_setup_report()?)),
        SlashCommand::Tools { tool } => Ok(Some(render_tools_report(tool.as_deref())?)),
        SlashCommand::Doctor => Ok(Some(render_doctor_report()?)),
        SlashCommand::Skills { skill } => Ok(Some(render_skills_report(skill.as_deref())?)),
        SlashCommand::Tasks { task } => Ok(Some(render_tasks_report(task.as_deref())?)),
        SlashCommand::Init => Ok(Some(init_simcoe_md()?)),
        SlashCommand::Diff => Ok(Some(render_diff_report()?)),
        SlashCommand::Version => Ok(Some(render_version_report())),
        _ => Ok(None),
    }
}

fn build_resume_json_payload(
    session_path: &Path,
    initial_message_count: usize,
    commands: Vec<serde_json::Value>,
    final_message_count: usize,
) -> serde_json::Value {
    json!({
        "session_path": session_path.display().to_string(),
        "restored_message": restored_session_message(session_path, initial_message_count),
        "initial_message_count": initial_message_count,
        "command_count": commands.len(),
        "commands": commands,
        "final_message_count": final_message_count,
    })
}

fn build_resume_start_record(
    session_path: &Path,
    initial_message_count: usize,
) -> serde_json::Value {
    json!({
        "type": "resume",
        "session_path": session_path.display().to_string(),
        "message": restored_session_message(session_path, initial_message_count),
        "initial_message_count": initial_message_count,
    })
}

fn build_resume_command_record(
    index: usize,
    command: &str,
    message: Option<&str>,
    message_count: usize,
    changed_session: bool,
) -> serde_json::Value {
    json!({
        "type": "resume_command",
        "index": index,
        "command": command,
        "message": message,
        "message_count": message_count,
        "changed_session": changed_session,
    })
}

fn build_resume_summary_record(
    session_path: &Path,
    initial_message_count: usize,
    final_message_count: usize,
    command_count: usize,
) -> serde_json::Value {
    json!({
        "type": "resume_summary",
        "session_path": session_path.display().to_string(),
        "initial_message_count": initial_message_count,
        "final_message_count": final_message_count,
        "command_count": command_count,
    })
}

fn parse_git_status_metadata(status: Option<&str>) -> (Option<PathBuf>, Option<String>) {
    let Some(status) = status else {
        return (None, None);
    };
    let branch = status.lines().next().and_then(|line| {
        line.strip_prefix("## ")
            .map(|line| {
                line.split(['.', ' '])
                    .next()
                    .unwrap_or_default()
                    .to_string()
            })
            .filter(|value| !value.is_empty())
    });
    let project_root = find_git_root().ok();
    (project_root, branch)
}

fn find_git_root() -> Result<PathBuf, Box<dyn std::error::Error>> {
    let output = command_in_current_dir("git")?
        .args(["rev-parse", "--show-toplevel"])
        .output()?;
    if !output.status.success() {
        return Err("not a git repository".into());
    }
    let path = String::from_utf8(output.stdout)?.trim().to_string();
    if path.is_empty() {
        return Err("empty git root".into());
    }
    Ok(PathBuf::from(path))
}

#[allow(clippy::too_many_lines)]
fn run_resume_command(
    session_path: &Path,
    session: &Session,
    command: &SlashCommand,
) -> Result<ResumeCommandOutcome, Box<dyn std::error::Error>> {
    match command {
        SlashCommand::Help => Ok(resume_command_outcome(
            session_path,
            session.clone(),
            Some(render_resume_command_help()),
        )),
        SlashCommand::Compact => {
            let result = runtime::compact_session(
                session,
                CompactionConfig {
                    max_estimated_tokens: 0,
                    ..CompactionConfig::default()
                },
            );
            let removed = result.removed_message_count;
            let kept = result.compacted_session.messages.len();
            let skipped = removed == 0;
            result.compacted_session.save_to_path(session_path)?;
            Ok(resume_command_outcome(
                session_path,
                result.compacted_session,
                Some(format_compact_report(removed, kept, skipped)),
            ))
        }
        SlashCommand::Clear { confirm } => {
            if !confirm {
                return Ok(resume_command_outcome(
                    session_path,
                    session.clone(),
                    Some(
                        "clear: confirmation required; rerun with /clear --confirm".to_string(),
                    ),
                ));
            }
            let cleared = Session::new();
            cleared.save_to_path(session_path)?;
            Ok(resume_command_outcome(
                session_path,
                cleared,
                Some(format!(
                    "Cleared resumed session file {}.",
                    session_path.display()
                )),
            ))
        }
        SlashCommand::Status => {
            let tracker = UsageTracker::from_session(session);
            let usage = tracker.cumulative_usage();
            Ok(resume_command_outcome(
                session_path,
                session.clone(),
                Some(format_status_report(
                    "restored-session",
                    StatusUsage {
                        message_count: session.messages.len(),
                        turns: tracker.turns(),
                        latest: tracker.current_turn_usage(),
                        cumulative: usage,
                        estimated_tokens: 0,
                    },
                    default_permission_mode().as_str(),
                    &status_context(Some(session_path))?,
                )),
            ))
        }
        SlashCommand::Cost => {
            let usage = UsageTracker::from_session(session).cumulative_usage();
            Ok(resume_command_outcome(
                session_path,
                session.clone(),
                Some(format_cost_report(usage)),
            ))
        }
        SlashCommand::Export { path } => {
            let export_path = resolve_export_path(path.as_deref(), session)?;
            fs::write(&export_path, render_export_text(session))?;
            Ok(resume_command_outcome(
                session_path,
                session.clone(),
                Some(format!(
                    "Export\n  Result           wrote transcript\n  File             {}\n  Messages         {}",
                    export_path.display(),
                    session.messages.len(),
                )),
            ))
        }
        SlashCommand::Session { action, target } => match action.as_deref() {
            None | Some("list") => {
                let active_session = session_handle_from_path(session_path);
                Ok(resume_command_outcome(
                    session_path,
                    session.clone(),
                    Some(render_session_list(Some(&active_session.id))?),
                ))
            }
            Some("switch") => {
                let target = target.as_deref().ok_or_else(|| {
                    io::Error::new(
                        io::ErrorKind::InvalidInput,
                        "session switch requires a session id or path",
                    )
                })?;
                let handle = resolve_session_reference(target)?;
                let next_session = Session::load_from_path(&handle.path)?;
                let message_count = next_session.messages.len();
                Ok(ResumeCommandOutcome {
                    session: next_session,
                    session_path: handle.path.clone(),
                    message: Some(session_switch_report(&handle, message_count)),
                })
            }
            Some(other) => Err(io::Error::new(
                io::ErrorKind::InvalidInput,
                format!(
                    "unknown session action '{other}'. Use /session list or /session switch <session-id>."
                ),
            )
            .into()),
        }
        command => {
            if let Some(message) = render_resume_read_only_message(command)? {
                Ok(resume_command_outcome(
                    session_path,
                    session.clone(),
                    Some(message),
                ))
            } else {
                Err("unsupported resumed slash command".into())
            }
        }
    }
}

fn recent_user_context(session: &Session, limit: usize) -> String {
    let requests = session
        .messages
        .iter()
        .filter(|message| message.role == MessageRole::User)
        .filter_map(|message| {
            message.blocks.iter().find_map(|block| match block {
                ContentBlock::Text { text } => Some(text.trim().to_string()),
                _ => None,
            })
        })
        .rev()
        .take(limit)
        .collect::<Vec<_>>();

    if requests.is_empty() {
        "<no prior user messages>".to_string()
    } else {
        requests
            .into_iter()
            .rev()
            .enumerate()
            .map(|(index, text)| format!("{}. {}", index + 1, text))
            .collect::<Vec<_>>()
            .join("\n")
    }
}

fn truncate_for_prompt(value: &str, limit: usize) -> String {
    if value.chars().count() <= limit {
        value.trim().to_string()
    } else {
        let truncated = value.chars().take(limit).collect::<String>();
        format!("{}\n…[truncated]", truncated.trim_end())
    }
}

fn sanitize_generated_message(value: &str) -> String {
    value.trim().trim_matches('`').trim().replace("\r\n", "\n")
}

fn parse_titled_body(value: &str) -> Option<(String, String)> {
    let normalized = sanitize_generated_message(value);
    let title = normalized
        .lines()
        .find_map(|line| line.strip_prefix("TITLE:").map(str::trim))?;
    let body_start = normalized.find("BODY:")?;
    let body = normalized[body_start + "BODY:".len()..].trim();
    Some((title.to_string(), body.to_string()))
}

fn render_export_text(session: &Session) -> String {
    runtime::render_export_text(session)
}

fn resolve_export_path(
    requested_path: Option<&str>,
    session: &Session,
) -> Result<PathBuf, Box<dyn std::error::Error>> {
    runtime::resolve_export_path(requested_path, session)
}

fn build_system_prompt() -> Result<Vec<String>, Box<dyn std::error::Error>> {
    Ok(load_system_prompt(
        current_working_directory()?,
        DEFAULT_DATE,
        env::consts::OS,
        "unknown",
    )?)
}

fn build_runtime_feature_config(
) -> Result<runtime::RuntimeFeatureConfig, Box<dyn std::error::Error>> {
    let (_, loader) = config_loader_in_current_dir()?;
    Ok(loader.load()?.feature_config().clone())
}

fn normalize_provider_override(provider: Option<&str>) -> Option<&str> {
    provider.map(str::trim).filter(|value| !value.is_empty())
}

fn active_runtime_provider_label(
    provider_override: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let feature_config = build_runtime_feature_config()?;
    let provider = resolve_runtime_provider(
        normalize_provider_override(provider_override).or(feature_config.provider()),
    )?;
    Ok(provider.as_str().to_string())
}

fn build_runtime(
    session: Session,
    model: String,
    provider_override: Option<String>,
    system_prompt: Vec<String>,
    enable_tools: bool,
    emit_output: bool,
    allowed_tools: Option<AllowedToolSet>,
    permission_mode: PermissionMode,
    status_bar: Option<StatusBarHandle>,
) -> Result<ConversationRuntime<SimcoeRuntimeClient, CliToolExecutor>, Box<dyn std::error::Error>> {
    let feature_config = build_runtime_feature_config()?;
    let provider = resolve_runtime_provider(
        normalize_provider_override(provider_override.as_deref()).or(feature_config.provider()),
    )?;
    Ok(ConversationRuntime::new_with_features(
        session,
        SimcoeRuntimeClient::new_with_provider(
            model,
            provider,
            enable_tools,
            emit_output,
            allowed_tools.clone(),
            status_bar,
        )?,
        CliToolExecutor::new(allowed_tools, emit_output),
        permission_policy(permission_mode),
        system_prompt,
        feature_config,
    ))
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum RuntimeProvider {
    Simcoe,
    Anthropic,
    OpenAi,
    Ollama,
}

impl RuntimeProvider {
    fn as_str(self) -> &'static str {
        match self {
            Self::Simcoe => "simcoe",
            Self::Anthropic => "anthropic",
            Self::OpenAi => "openai",
            Self::Ollama => "ollama",
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum ProviderDeliveryMode {
    StreamingSse,
    BufferedJsonFallback,
}

impl ProviderDeliveryMode {
    fn as_str(self) -> &'static str {
        match self {
            Self::StreamingSse => "streaming-sse",
            Self::BufferedJsonFallback => "buffered-json-fallback",
        }
    }
}

fn resolve_runtime_provider(provider: Option<&str>) -> Result<RuntimeProvider, RuntimeError> {
    let Some(provider) = provider.map(str::trim).filter(|value| !value.is_empty()) else {
        return Ok(RuntimeProvider::Simcoe);
    };
    let normalized = provider.to_ascii_lowercase();
    match normalized.as_str() {
        "simcoe" | "simcoe-ai" => Ok(RuntimeProvider::Simcoe),
        "anthropic" | "claude" => Ok(RuntimeProvider::Anthropic),
        "openai" | "chatgpt" => Ok(RuntimeProvider::OpenAi),
        "ollama" | "local" => Ok(RuntimeProvider::Ollama),
        _ => Err(RuntimeError::new(format!(
            "unsupported provider '{provider}'; expected simcoe, anthropic, openai, or ollama"
        ))),
    }
}

fn read_optional_env_non_empty(key: &str) -> Result<Option<String>, RuntimeError> {
    match env::var(key) {
        Ok(value) if !value.trim().is_empty() => Ok(Some(value)),
        Ok(_) | Err(env::VarError::NotPresent) => Ok(None),
        Err(error) => Err(RuntimeError::new(format!("failed to read {key}: {error}"))),
    }
}

fn read_required_env_non_empty(key: &str) -> Result<String, RuntimeError> {
    read_optional_env_non_empty(key)?.ok_or_else(|| {
        RuntimeError::new(format!(
            "{key} is not set; configure it before using this provider"
        ))
    })
}

fn anthropic_api_key() -> Result<String, RuntimeError> {
    read_required_env_non_empty("ANTHROPIC_API_KEY")
}

fn anthropic_base_url() -> Result<String, RuntimeError> {
    Ok(read_optional_env_non_empty("ANTHROPIC_BASE_URL")?
        .unwrap_or_else(|| DEFAULT_ANTHROPIC_BASE_URL.to_string()))
}

fn openai_api_key() -> Result<String, RuntimeError> {
    read_required_env_non_empty("OPENAI_API_KEY")
}

fn openai_base_url() -> Result<String, RuntimeError> {
    Ok(read_optional_env_non_empty("OPENAI_BASE_URL")?
        .unwrap_or_else(|| DEFAULT_OPENAI_BASE_URL.to_string()))
}

fn ollama_api_key() -> Result<String, RuntimeError> {
    Ok(read_optional_env_non_empty("OLLAMA_API_KEY")?.unwrap_or_else(|| "ollama".to_string()))
}

fn ollama_base_url() -> Result<String, RuntimeError> {
    Ok(read_optional_env_non_empty("OLLAMA_BASE_URL")?
        .unwrap_or_else(|| DEFAULT_OLLAMA_BASE_URL.to_string()))
}

#[derive(Debug, Clone, PartialEq, Eq)]
struct OpenAiCompatibleTransportConfig {
    provider: RuntimeProvider,
    api_key: String,
    base_url: String,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
struct OpenAiChatCompletionRequest {
    model: String,
    messages: Vec<OpenAiChatMessage>,
    #[serde(skip_serializing_if = "Option::is_none")]
    tools: Option<Vec<OpenAiToolDefinition>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    tool_choice: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    max_tokens: Option<u32>,
    #[serde(skip_serializing_if = "Option::is_none")]
    stream_options: Option<OpenAiStreamOptions>,
    stream: bool,
}

impl OpenAiChatCompletionRequest {
    #[must_use]
    fn with_streaming(mut self) -> Self {
        self.stream = true;
        self.stream_options = Some(OpenAiStreamOptions {
            include_usage: true,
        });
        self
    }
}

#[derive(Debug, Clone, Serialize, PartialEq)]
struct OpenAiStreamOptions {
    include_usage: bool,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
struct OpenAiChatMessage {
    role: String,
    content: serde_json::Value,
    #[serde(skip_serializing_if = "Option::is_none")]
    tool_calls: Option<Vec<OpenAiToolCall>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    tool_call_id: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
struct OpenAiToolCall {
    id: String,
    #[serde(rename = "type")]
    kind: String,
    function: OpenAiToolFunctionCall,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
struct OpenAiToolFunctionCall {
    name: String,
    arguments: String,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
struct OpenAiToolDefinition {
    #[serde(rename = "type")]
    kind: String,
    function: OpenAiFunctionDefinition,
}

#[derive(Debug, Clone, Serialize, PartialEq)]
struct OpenAiFunctionDefinition {
    name: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    description: Option<String>,
    parameters: serde_json::Value,
}

#[derive(Debug, Clone, Deserialize, PartialEq)]
struct OpenAiChatCompletionResponse {
    id: String,
    choices: Vec<OpenAiChatCompletionChoice>,
    #[serde(default)]
    usage: Option<OpenAiChatCompletionUsage>,
}

#[derive(Debug, Clone, Deserialize, PartialEq)]
struct OpenAiChatCompletionChoice {
    message: OpenAiAssistantMessage,
}

#[derive(Debug, Clone, Deserialize, PartialEq)]
struct OpenAiAssistantMessage {
    #[serde(default)]
    content: Option<serde_json::Value>,
    #[serde(default)]
    tool_calls: Option<Vec<OpenAiToolCall>>,
}

#[derive(Debug, Clone, Deserialize, PartialEq)]
struct OpenAiChatCompletionUsage {
    prompt_tokens: u32,
    completion_tokens: u32,
}

#[derive(Debug, Clone, Deserialize, PartialEq)]
struct OpenAiChatCompletionChunk {
    #[serde(default)]
    choices: Vec<OpenAiChatCompletionChunkChoice>,
    #[serde(default)]
    usage: Option<OpenAiChatCompletionUsage>,
}

#[derive(Debug, Clone, Deserialize, PartialEq)]
struct OpenAiChatCompletionChunkChoice {
    index: usize,
    #[serde(default)]
    delta: OpenAiChatCompletionChunkDelta,
    #[serde(default)]
    finish_reason: Option<String>,
}

#[derive(Debug, Clone, Default, Deserialize, PartialEq)]
struct OpenAiChatCompletionChunkDelta {
    #[serde(default)]
    content: Option<String>,
    #[serde(default)]
    tool_calls: Option<Vec<OpenAiToolCallDelta>>,
}

#[derive(Debug, Clone, Default, Deserialize, PartialEq)]
struct OpenAiToolCallDelta {
    index: usize,
    #[serde(default)]
    id: Option<String>,
    #[serde(rename = "type", default)]
    kind: Option<String>,
    #[serde(default)]
    function: Option<OpenAiToolFunctionDelta>,
}

#[derive(Debug, Clone, Default, Deserialize, PartialEq)]
struct OpenAiToolFunctionDelta {
    #[serde(default)]
    name: Option<String>,
    #[serde(default)]
    arguments: Option<String>,
}

#[derive(Debug, Clone, PartialEq)]
enum OpenAiSseFrame {
    Chunk(OpenAiChatCompletionChunk),
    Done,
}

#[derive(Debug, Default)]
struct OpenAiSseParser {
    buffer: Vec<u8>,
}

impl OpenAiSseParser {
    #[must_use]
    fn new() -> Self {
        Self::default()
    }

    fn push(&mut self, chunk: &[u8]) -> Result<Vec<OpenAiSseFrame>, RuntimeError> {
        self.buffer.extend_from_slice(chunk);
        let mut frames = Vec::new();

        while let Some(frame) = self.next_frame() {
            if let Some(parsed) = parse_openai_sse_frame(&frame)? {
                frames.push(parsed);
            }
        }

        Ok(frames)
    }

    fn finish(&mut self) -> Result<Vec<OpenAiSseFrame>, RuntimeError> {
        if self.buffer.is_empty() {
            return Ok(Vec::new());
        }

        let trailing = std::mem::take(&mut self.buffer);
        match parse_openai_sse_frame(&String::from_utf8_lossy(&trailing))? {
            Some(frame) => Ok(vec![frame]),
            None => Ok(Vec::new()),
        }
    }

    fn next_frame(&mut self) -> Option<String> {
        let separator = self
            .buffer
            .windows(2)
            .position(|window| window == b"\n\n")
            .map(|position| (position, 2))
            .or_else(|| {
                self.buffer
                    .windows(4)
                    .position(|window| window == b"\r\n\r\n")
                    .map(|position| (position, 4))
            })?;

        let (position, separator_len) = separator;
        let frame = self
            .buffer
            .drain(..position + separator_len)
            .collect::<Vec<_>>();
        let frame_len = frame.len().saturating_sub(separator_len);
        Some(String::from_utf8_lossy(&frame[..frame_len]).into_owned())
    }
}

#[derive(Debug, Clone, Default, PartialEq, Eq)]
struct PendingOpenAiToolCall {
    id: String,
    name: String,
    arguments: String,
}

fn openai_compatible_transport_config(
    provider: RuntimeProvider,
) -> Result<OpenAiCompatibleTransportConfig, RuntimeError> {
    match provider {
        RuntimeProvider::OpenAi => Ok(OpenAiCompatibleTransportConfig {
            provider,
            api_key: openai_api_key()?,
            base_url: openai_base_url()?,
        }),
        RuntimeProvider::Ollama => Ok(OpenAiCompatibleTransportConfig {
            provider,
            api_key: ollama_api_key()?,
            base_url: ollama_base_url()?,
        }),
        RuntimeProvider::Simcoe | RuntimeProvider::Anthropic => Err(RuntimeError::new(format!(
            "provider '{}' uses the Anthropic-compatible transport and cannot use the OpenAI-compatible adapter",
            provider.as_str()
        ))),
    }
}

fn openai_chat_completion_url(base_url: &str) -> String {
    let trimmed = base_url.trim().trim_end_matches('/');
    if trimmed.ends_with("/chat/completions") {
        trimmed.to_string()
    } else if trimmed.ends_with("/v1") {
        format!("{trimmed}/chat/completions")
    } else {
        format!("{trimmed}/v1/chat/completions")
    }
}

fn normalize_openai_tool_arguments(arguments: &str) -> Result<String, RuntimeError> {
    let trimmed = arguments.trim();
    if trimmed.is_empty() {
        return Ok("{}".to_string());
    }
    let value = serde_json::from_str::<serde_json::Value>(trimmed).map_err(|error| {
        RuntimeError::new(format!("tool call arguments were not valid JSON: {error}"))
    })?;
    serde_json::to_string(&value).map_err(|error| RuntimeError::new(error.to_string()))
}

fn joined_text_blocks(blocks: &[ContentBlock]) -> String {
    blocks
        .iter()
        .filter_map(|block| match block {
            ContentBlock::Text { text } if !text.trim().is_empty() => Some(text.as_str()),
            ContentBlock::Text { .. }
            | ContentBlock::ToolUse { .. }
            | ContentBlock::ToolResult { .. } => None,
        })
        .collect::<Vec<_>>()
        .join("\n\n")
}

fn openai_tool_calls_from_blocks(
    blocks: &[ContentBlock],
) -> Result<Option<Vec<OpenAiToolCall>>, RuntimeError> {
    let tool_calls = blocks
        .iter()
        .filter_map(|block| match block {
            ContentBlock::ToolUse { id, name, input } => Some((id, name, input)),
            ContentBlock::Text { .. } | ContentBlock::ToolResult { .. } => None,
        })
        .map(|(id, name, input)| {
            Ok(OpenAiToolCall {
                id: id.clone(),
                kind: "function".to_string(),
                function: OpenAiToolFunctionCall {
                    name: name.clone(),
                    arguments: normalize_openai_tool_arguments(input)?,
                },
            })
        })
        .collect::<Result<Vec<_>, RuntimeError>>()?;
    Ok((!tool_calls.is_empty()).then_some(tool_calls))
}

fn build_openai_chat_messages(
    request: &ApiRequest,
) -> Result<Vec<OpenAiChatMessage>, RuntimeError> {
    let mut messages = Vec::new();

    if !request.system_prompt.is_empty() {
        messages.push(OpenAiChatMessage {
            role: "system".to_string(),
            content: json!(request.system_prompt.join("\n\n")),
            tool_calls: None,
            tool_call_id: None,
        });
    }

    for message in &request.messages {
        match message.role {
            MessageRole::System => {
                let text = joined_text_blocks(&message.blocks);
                if !text.is_empty() {
                    messages.push(OpenAiChatMessage {
                        role: "system".to_string(),
                        content: json!(text),
                        tool_calls: None,
                        tool_call_id: None,
                    });
                }
            }
            MessageRole::User => {
                let text = joined_text_blocks(&message.blocks);
                if !text.is_empty() {
                    messages.push(OpenAiChatMessage {
                        role: "user".to_string(),
                        content: json!(text),
                        tool_calls: None,
                        tool_call_id: None,
                    });
                }
            }
            MessageRole::Assistant => {
                let text = joined_text_blocks(&message.blocks);
                let tool_calls = openai_tool_calls_from_blocks(&message.blocks)?;
                if !text.is_empty() || tool_calls.is_some() {
                    messages.push(OpenAiChatMessage {
                        role: "assistant".to_string(),
                        content: if text.is_empty() {
                            serde_json::Value::Null
                        } else {
                            json!(text)
                        },
                        tool_calls,
                        tool_call_id: None,
                    });
                }
            }
            MessageRole::Tool => {
                for block in &message.blocks {
                    if let ContentBlock::ToolResult {
                        tool_use_id,
                        output,
                        ..
                    } = block
                    {
                        messages.push(OpenAiChatMessage {
                            role: "tool".to_string(),
                            content: json!(output),
                            tool_calls: None,
                            tool_call_id: Some(tool_use_id.clone()),
                        });
                    }
                }
            }
        }
    }

    Ok(messages)
}

fn build_openai_tool_definitions(
    allowed_tools: Option<&AllowedToolSet>,
) -> Vec<OpenAiToolDefinition> {
    runtime_tool_definitions(allowed_tools)
        .into_iter()
        .map(|definition| OpenAiToolDefinition {
            kind: "function".to_string(),
            function: OpenAiFunctionDefinition {
                name: definition.name,
                description: definition.description,
                parameters: definition.input_schema,
            },
        })
        .collect()
}

fn build_openai_chat_completion_request(
    request: &ApiRequest,
    model: &str,
    enable_tools: bool,
    allowed_tools: Option<&AllowedToolSet>,
) -> Result<OpenAiChatCompletionRequest, RuntimeError> {
    let tools = enable_tools.then(|| build_openai_tool_definitions(allowed_tools));
    Ok(OpenAiChatCompletionRequest {
        model: model.to_string(),
        messages: build_openai_chat_messages(request)?,
        tools: tools.filter(|definitions| !definitions.is_empty()),
        tool_choice: enable_tools.then(|| "auto".to_string()),
        max_tokens: Some(max_tokens_for_model(model)),
        stream_options: None,
        stream: false,
    })
}

fn openai_message_text(content: Option<serde_json::Value>) -> String {
    match content {
        None | Some(serde_json::Value::Null) => String::new(),
        Some(serde_json::Value::String(text)) => text,
        Some(serde_json::Value::Array(parts)) => parts
            .into_iter()
            .filter_map(|part| {
                part.get("text")
                    .and_then(serde_json::Value::as_str)
                    .map(str::to_string)
            })
            .collect::<Vec<_>>()
            .join(""),
        Some(other) => other.to_string(),
    }
}

fn parse_openai_sse_frame(frame: &str) -> Result<Option<OpenAiSseFrame>, RuntimeError> {
    let trimmed = frame.trim();
    if trimmed.is_empty() {
        return Ok(None);
    }

    let mut data_lines = Vec::new();

    for line in trimmed.lines() {
        if line.starts_with(':') {
            continue;
        }
        if let Some(data) = line.strip_prefix("data:") {
            data_lines.push(data.trim_start());
        }
    }

    if data_lines.is_empty() {
        return Ok(None);
    }

    let payload = data_lines.join("\n");
    if payload == "[DONE]" {
        return Ok(Some(OpenAiSseFrame::Done));
    }

    serde_json::from_str::<OpenAiChatCompletionChunk>(&payload)
        .map(OpenAiSseFrame::Chunk)
        .map(Some)
        .map_err(|error| RuntimeError::new(format!("failed to parse OpenAI SSE frame: {error}")))
}

fn update_pending_openai_tool_call(
    delta: OpenAiToolCallDelta,
    pending_tool_calls: &mut BTreeMap<usize, PendingOpenAiToolCall>,
) {
    let entry = pending_tool_calls.entry(delta.index).or_default();
    if let Some(id) = delta.id {
        entry.id = id;
    }
    if let Some(function) = delta.function {
        if let Some(name) = function.name {
            entry.name = name;
        }
        if let Some(arguments) = function.arguments {
            entry.arguments.push_str(&arguments);
        }
    }
}

fn flush_openai_stream_buffers(
    renderer: &TerminalRenderer,
    markdown_stream: &mut MarkdownStreamState,
    pending_tool_calls: &mut BTreeMap<usize, PendingOpenAiToolCall>,
    events: &mut Vec<AssistantEvent>,
    out: &mut dyn Write,
) -> Result<(), RuntimeError> {
    if let Some(rendered) = markdown_stream.flush(renderer) {
        write!(out, "{rendered}")
            .and_then(|()| out.flush())
            .map_err(|error| RuntimeError::new(error.to_string()))?;
    }

    let pending = std::mem::take(pending_tool_calls);
    for (_, tool_call) in pending {
        let input = normalize_openai_tool_arguments(&tool_call.arguments)?;
        writeln!(out, "\n{}", format_tool_call_start(&tool_call.name, &input))
            .and_then(|()| out.flush())
            .map_err(|error| RuntimeError::new(error.to_string()))?;
        events.push(AssistantEvent::ToolUse {
            id: tool_call.id,
            name: tool_call.name,
            input,
        });
    }

    Ok(())
}

fn apply_openai_stream_chunk(
    chunk: OpenAiChatCompletionChunk,
    renderer: &TerminalRenderer,
    markdown_stream: &mut MarkdownStreamState,
    pending_tool_calls: &mut BTreeMap<usize, PendingOpenAiToolCall>,
    events: &mut Vec<AssistantEvent>,
    out: &mut dyn Write,
    status_bar: Option<&StatusBarHandle>,
) -> Result<bool, RuntimeError> {
    let mut saw_finish_reason = false;

    for choice in chunk.choices {
        if let Some(content) = choice.delta.content.filter(|text| !text.is_empty()) {
            if let Some(rendered) = markdown_stream.push(renderer, &content) {
                write!(out, "{rendered}")
                    .and_then(|()| out.flush())
                    .map_err(|error| RuntimeError::new(error.to_string()))?;
            }
            events.push(AssistantEvent::TextDelta(content));
            if let Some(status_bar) = status_bar {
                let _ = status_bar.render();
            }
        }

        if let Some(tool_calls) = choice.delta.tool_calls {
            for tool_call in tool_calls {
                update_pending_openai_tool_call(tool_call, pending_tool_calls);
            }
        }

        if choice.finish_reason.is_some() {
            saw_finish_reason = true;
            flush_openai_stream_buffers(
                renderer,
                markdown_stream,
                pending_tool_calls,
                events,
                out,
            )?;
        }
    }

    if let Some(usage) = chunk.usage {
        let usage = TokenUsage {
            input_tokens: usage.prompt_tokens,
            output_tokens: usage.completion_tokens,
            cache_creation_input_tokens: 0,
            cache_read_input_tokens: 0,
        };
        if let Some(status_bar) = status_bar {
            status_bar.update_turn_usage(usage);
            let _ = status_bar.render();
        }
        events.push(AssistantEvent::Usage(usage));
    }

    Ok(saw_finish_reason)
}

struct CliPermissionPrompter {
    current_mode: PermissionMode,
}

impl CliPermissionPrompter {
    fn new(current_mode: PermissionMode) -> Self {
        Self { current_mode }
    }
}

impl runtime::PermissionPrompter for CliPermissionPrompter {
    fn decide(
        &mut self,
        request: &runtime::PermissionRequest,
    ) -> runtime::PermissionPromptDecision {
        println!();
        println!("Permission approval required");
        println!("  Tool             {}", request.tool_name);
        println!("  Current mode     {}", self.current_mode.as_str());
        println!("  Required mode    {}", request.required_mode.as_str());
        println!("  Input            {}", request.input);
        print!("Approve this tool call? [y/N]: ");
        let _ = io::stdout().flush();

        let mut response = String::new();
        match io::stdin().read_line(&mut response) {
            Ok(_) => {
                let normalized = response.trim().to_ascii_lowercase();
                if matches!(normalized.as_str(), "y" | "yes") {
                    runtime::PermissionPromptDecision::Allow
                } else {
                    runtime::PermissionPromptDecision::Deny {
                        reason: format!(
                            "tool '{}' denied by user approval prompt",
                            request.tool_name
                        ),
                    }
                }
            }
            Err(error) => runtime::PermissionPromptDecision::Deny {
                reason: format!("permission approval failed: {error}"),
            },
        }
    }
}

struct SimcoeRuntimeClient {
    runtime: tokio::runtime::Runtime,
    provider: RuntimeProvider,
    last_delivery_mode: Option<ProviderDeliveryMode>,
    model: String,
    enable_tools: bool,
    emit_output: bool,
    allowed_tools: Option<AllowedToolSet>,
    status_bar: Option<StatusBarHandle>,
}

impl SimcoeRuntimeClient {
    fn new(
        model: String,
        enable_tools: bool,
        emit_output: bool,
        allowed_tools: Option<AllowedToolSet>,
        status_bar: Option<StatusBarHandle>,
    ) -> Result<Self, Box<dyn std::error::Error>> {
        Self::new_with_provider(
            model,
            RuntimeProvider::Simcoe,
            enable_tools,
            emit_output,
            allowed_tools,
            status_bar,
        )
    }

    fn new_with_provider(
        model: String,
        provider: RuntimeProvider,
        enable_tools: bool,
        emit_output: bool,
        allowed_tools: Option<AllowedToolSet>,
        status_bar: Option<StatusBarHandle>,
    ) -> Result<Self, Box<dyn std::error::Error>> {
        Ok(Self {
            runtime: tokio::runtime::Runtime::new()?,
            provider,
            last_delivery_mode: None,
            model,
            enable_tools,
            emit_output,
            allowed_tools,
            status_bar,
        })
    }

    fn last_delivery_mode(&self) -> Option<&'static str> {
        self.last_delivery_mode.map(ProviderDeliveryMode::as_str)
    }

    fn stream_anthropic_with_writer(
        &mut self,
        request: ApiRequest,
        out: &mut dyn Write,
    ) -> Result<Vec<AssistantEvent>, RuntimeError> {
        self.last_delivery_mode = None;
        let client = build_runtime_api_client_for_provider(self.provider)?;
        let message_request = MessageRequest {
            model: self.model.clone(),
            max_tokens: max_tokens_for_model(&self.model),
            messages: convert_messages(&request.messages),
            system: (!request.system_prompt.is_empty()).then(|| request.system_prompt.join("\n\n")),
            tools: self
                .enable_tools
                .then(|| runtime_tool_definitions(self.allowed_tools.as_ref())),
            tool_choice: self.enable_tools.then_some(ToolChoice::Auto),
            stream: true,
        };

        let (events, delivery_mode) = self.runtime.block_on(async {
            let mut stream = client
                .stream_message(&message_request)
                .await
                .map_err(|error| RuntimeError::new(error.to_string()))?;
            let mut sink = io::sink();
            let render_out: &mut dyn Write = if self.emit_output { out } else { &mut sink };
            let renderer = TerminalRenderer::new();
            let mut markdown_stream = MarkdownStreamState::default();
            let mut events = Vec::new();
            let mut pending_tool: Option<(String, String, String)> = None;
            let mut saw_stop = false;

            while let Some(event) = stream
                .next_event()
                .await
                .map_err(|error| RuntimeError::new(error.to_string()))?
            {
                match event {
                    ApiStreamEvent::MessageStart(start) => {
                        for block in start.message.content {
                            push_output_block(
                                block,
                                render_out,
                                &mut events,
                                &mut pending_tool,
                                true,
                            )?;
                        }
                    }
                    ApiStreamEvent::ContentBlockStart(start) => {
                        push_output_block(
                            start.content_block,
                            render_out,
                            &mut events,
                            &mut pending_tool,
                            true,
                        )?;
                    }
                    ApiStreamEvent::ContentBlockDelta(delta) => match delta.delta {
                        ContentBlockDelta::TextDelta { text } => {
                            if !text.is_empty() {
                                if let Some(rendered) = markdown_stream.push(&renderer, &text) {
                                    write!(render_out, "{rendered}")
                                        .and_then(|()| render_out.flush())
                                        .map_err(|error| RuntimeError::new(error.to_string()))?;
                                }
                                events.push(AssistantEvent::TextDelta(text));
                                if let Some(status_bar) = self.status_bar.as_ref() {
                                    let _ = status_bar.render();
                                }
                            }
                        }
                        ContentBlockDelta::InputJsonDelta { partial_json } => {
                            if let Some((_, _, input)) = &mut pending_tool {
                                input.push_str(&partial_json);
                            }
                        }
                    },
                    ApiStreamEvent::ContentBlockStop(_) => {
                        if let Some(rendered) = markdown_stream.flush(&renderer) {
                            write!(render_out, "{rendered}")
                                .and_then(|()| render_out.flush())
                                .map_err(|error| RuntimeError::new(error.to_string()))?;
                        }
                        if let Some((id, name, input)) = pending_tool.take() {
                            writeln!(render_out, "\n{}", format_tool_call_start(&name, &input))
                                .and_then(|()| render_out.flush())
                                .map_err(|error| RuntimeError::new(error.to_string()))?;
                            events.push(AssistantEvent::ToolUse { id, name, input });
                        }
                    }
                    ApiStreamEvent::MessageDelta(delta) => {
                        let usage = TokenUsage {
                            input_tokens: delta.usage.input_tokens,
                            output_tokens: delta.usage.output_tokens,
                            cache_creation_input_tokens: 0,
                            cache_read_input_tokens: 0,
                        };
                        if let Some(status_bar) = self.status_bar.as_ref() {
                            status_bar.update_turn_usage(usage);
                            let _ = status_bar.render();
                        }
                        events.push(AssistantEvent::Usage(usage));
                    }
                    ApiStreamEvent::MessageStop(_) => {
                        saw_stop = true;
                        if let Some(rendered) = markdown_stream.flush(&renderer) {
                            write!(render_out, "{rendered}")
                                .and_then(|()| render_out.flush())
                                .map_err(|error| RuntimeError::new(error.to_string()))?;
                        }
                        if let Some(status_bar) = self.status_bar.as_ref() {
                            let _ = status_bar.render();
                        }
                        events.push(AssistantEvent::MessageStop);
                    }
                }
            }

            if !saw_stop
                && events.iter().any(|event| {
                    matches!(event, AssistantEvent::TextDelta(text) if !text.is_empty())
                        || matches!(event, AssistantEvent::ToolUse { .. })
                })
            {
                events.push(AssistantEvent::MessageStop);
            }

            if events
                .iter()
                .any(|event| matches!(event, AssistantEvent::MessageStop))
            {
                return Ok((events, ProviderDeliveryMode::StreamingSse));
            }

            let response = client
                .send_message(&MessageRequest {
                    stream: false,
                    ..message_request.clone()
                })
                .await
                .map_err(|error| RuntimeError::new(error.to_string()))?;
            response_to_events(response, render_out)
                .map(|events| (events, ProviderDeliveryMode::BufferedJsonFallback))
        })?;
        self.last_delivery_mode = Some(delivery_mode);
        Ok(events)
    }

    fn stream_openai_compatible_with_writer(
        &mut self,
        request: ApiRequest,
        out: &mut dyn Write,
    ) -> Result<Vec<AssistantEvent>, RuntimeError> {
        self.last_delivery_mode = None;
        let transport = openai_compatible_transport_config(self.provider)?;
        let request = build_openai_chat_completion_request(
            &request,
            &self.model,
            self.enable_tools,
            self.allowed_tools.as_ref(),
        )?;

        let (events, delivery_mode) = self.runtime.block_on(async {
            let mut sink = io::sink();
            let render_out: &mut dyn Write = if self.emit_output { out } else { &mut sink };
            let streaming_request = request.clone().with_streaming();
            let mut response =
                send_openai_chat_completion_raw(&transport, &streaming_request).await?;
            let content_type = response
                .headers()
                .get("content-type")
                .and_then(|value| value.to_str().ok())
                .unwrap_or("")
                .to_ascii_lowercase();

            if !content_type.contains("text/event-stream") {
                let response =
                    decode_openai_chat_completion_response(response, transport.provider).await?;
                return render_openai_chat_completion_response(
                    response,
                    render_out,
                    self.status_bar.as_ref(),
                )
                .map(|events| (events, ProviderDeliveryMode::BufferedJsonFallback));
            }

            let renderer = TerminalRenderer::new();
            let mut markdown_stream = MarkdownStreamState::default();
            let mut parser = OpenAiSseParser::new();
            let mut pending_tool_calls = BTreeMap::new();
            let mut events = Vec::new();
            let mut saw_done = false;
            let mut saw_finish_reason = false;

            while let Some(chunk) = response.chunk().await.map_err(|error| {
                RuntimeError::new(format!(
                    "failed to read {} provider stream: {error}",
                    transport.provider.as_str()
                ))
            })? {
                for frame in parser.push(&chunk)? {
                    match frame {
                        OpenAiSseFrame::Chunk(chunk) => {
                            saw_finish_reason |= apply_openai_stream_chunk(
                                chunk,
                                &renderer,
                                &mut markdown_stream,
                                &mut pending_tool_calls,
                                &mut events,
                                render_out,
                                self.status_bar.as_ref(),
                            )?;
                        }
                        OpenAiSseFrame::Done => {
                            saw_done = true;
                        }
                    }
                }
                if saw_done {
                    break;
                }
            }

            for frame in parser.finish()? {
                match frame {
                    OpenAiSseFrame::Chunk(chunk) => {
                        saw_finish_reason |= apply_openai_stream_chunk(
                            chunk,
                            &renderer,
                            &mut markdown_stream,
                            &mut pending_tool_calls,
                            &mut events,
                            render_out,
                            self.status_bar.as_ref(),
                        )?;
                    }
                    OpenAiSseFrame::Done => {
                        saw_done = true;
                    }
                }
            }

            flush_openai_stream_buffers(
                &renderer,
                &mut markdown_stream,
                &mut pending_tool_calls,
                &mut events,
                render_out,
            )?;
            if let Some(status_bar) = self.status_bar.as_ref() {
                let _ = status_bar.render();
            }

            if saw_done
                || saw_finish_reason
                || events.iter().any(|event| {
                    matches!(event, AssistantEvent::TextDelta(text) if !text.is_empty())
                        || matches!(event, AssistantEvent::ToolUse { .. })
                        || matches!(event, AssistantEvent::Usage(_))
                })
            {
                events.push(AssistantEvent::MessageStop);
            }

            Ok((events, ProviderDeliveryMode::StreamingSse))
        })?;
        self.last_delivery_mode = Some(delivery_mode);
        Ok(events)
    }

    fn stream_with_writer(
        &mut self,
        request: ApiRequest,
        out: &mut dyn Write,
    ) -> Result<Vec<AssistantEvent>, RuntimeError> {
        match self.provider {
            RuntimeProvider::Simcoe | RuntimeProvider::Anthropic => {
                self.stream_anthropic_with_writer(request, out)
            }
            RuntimeProvider::OpenAi | RuntimeProvider::Ollama => {
                self.stream_openai_compatible_with_writer(request, out)
            }
        }
    }
}

async fn send_openai_chat_completion_raw(
    transport: &OpenAiCompatibleTransportConfig,
    request: &OpenAiChatCompletionRequest,
) -> Result<reqwest::Response, RuntimeError> {
    let request_url = openai_chat_completion_url(&transport.base_url);
    let mut request_builder = reqwest::Client::new()
        .post(&request_url)
        .header("content-type", "application/json");
    if !transport.api_key.trim().is_empty() {
        request_builder = request_builder.bearer_auth(&transport.api_key);
    }

    let response = request_builder
        .json(request)
        .send()
        .await
        .map_err(|error| {
            RuntimeError::new(format!(
                "failed to call {} provider: {error}",
                transport.provider.as_str()
            ))
        })?;

    Ok(response)
}

async fn decode_openai_chat_completion_response(
    response: reqwest::Response,
    provider: RuntimeProvider,
) -> Result<OpenAiChatCompletionResponse, RuntimeError> {
    let status = response.status();
    if !status.is_success() {
        let body = response
            .text()
            .await
            .unwrap_or_else(|_| "<failed to read response body>".to_string());
        return Err(RuntimeError::new(format!(
            "{} provider request failed with {status}: {}",
            provider.as_str(),
            body.trim()
        )));
    }

    response
        .json::<OpenAiChatCompletionResponse>()
        .await
        .map_err(|error| {
            RuntimeError::new(format!(
                "failed to decode {} provider response: {error}",
                provider.as_str()
            ))
        })
}

fn render_openai_chat_completion_response(
    response: OpenAiChatCompletionResponse,
    out: &mut dyn Write,
    status_bar: Option<&StatusBarHandle>,
) -> Result<Vec<AssistantEvent>, RuntimeError> {
    let choice = response.choices.into_iter().next().ok_or_else(|| {
        RuntimeError::new("OpenAI-compatible provider response did not include any choices")
    })?;

    let mut events = Vec::new();
    let text = openai_message_text(choice.message.content);
    if !text.is_empty() {
        let rendered = TerminalRenderer::new().markdown_to_ansi(&text);
        write!(out, "{rendered}")
            .and_then(|()| out.flush())
            .map_err(|error| RuntimeError::new(error.to_string()))?;
        events.push(AssistantEvent::TextDelta(text));
    }

    if let Some(tool_calls) = choice.message.tool_calls {
        for tool_call in tool_calls {
            let input = normalize_openai_tool_arguments(&tool_call.function.arguments)?;
            writeln!(
                out,
                "\n{}",
                format_tool_call_start(&tool_call.function.name, &input)
            )
            .and_then(|()| out.flush())
            .map_err(|error| RuntimeError::new(error.to_string()))?;
            events.push(AssistantEvent::ToolUse {
                id: tool_call.id,
                name: tool_call.function.name,
                input,
            });
        }
    }

    if let Some(usage) = response.usage {
        let usage = TokenUsage {
            input_tokens: usage.prompt_tokens,
            output_tokens: usage.completion_tokens,
            cache_creation_input_tokens: 0,
            cache_read_input_tokens: 0,
        };
        if let Some(status_bar) = status_bar {
            status_bar.update_turn_usage(usage);
            let _ = status_bar.render();
        }
        events.push(AssistantEvent::Usage(usage));
    }

    events.push(AssistantEvent::MessageStop);
    Ok(events)
}

fn resolve_cli_auth_source() -> Result<AuthSource, Box<dyn std::error::Error>> {
    Ok(resolve_startup_auth_source(|| {
        let (_, loader) = config_loader_in_current_dir().map_err(api::ApiError::from)?;
        let config = loader.load().map_err(|error| {
            api::ApiError::Auth(format!("failed to load runtime OAuth config: {error}"))
        })?;
        Ok(config.oauth().cloned())
    })?)
}

fn build_runtime_api_client_for_provider(
    provider: RuntimeProvider,
) -> Result<SimcoeApiClient, RuntimeError> {
    match provider {
        RuntimeProvider::Simcoe => {
            let auth =
                resolve_cli_auth_source().map_err(|error| RuntimeError::new(error.to_string()))?;
            let base_url = api::read_base_url().map_err(|error| RuntimeError::new(error.to_string()))?;
            Ok(SimcoeApiClient::from_auth(auth).with_base_url(base_url))
        }
        RuntimeProvider::Anthropic => Ok(SimcoeApiClient::from_auth(AuthSource::ApiKey(
            anthropic_api_key()?,
        ))
        .with_base_url(anthropic_base_url()?)),
        RuntimeProvider::OpenAi | RuntimeProvider::Ollama => Err(RuntimeError::new(format!(
            "provider '{}' uses the OpenAI-compatible transport and should not be constructed with the Anthropic client builder",
            provider.as_str()
        ))),
    }
}

impl ApiClient for SimcoeRuntimeClient {
    #[allow(clippy::too_many_lines)]
    fn stream(&mut self, request: ApiRequest) -> Result<Vec<AssistantEvent>, RuntimeError> {
        let mut stdout = io::stdout();
        self.stream_with_writer(request, &mut stdout)
    }
}

fn final_assistant_text(summary: &runtime::TurnSummary) -> String {
    summary
        .assistant_messages
        .last()
        .map(|message| {
            message
                .blocks
                .iter()
                .filter_map(|block| match block {
                    ContentBlock::Text { text } => Some(text.as_str()),
                    _ => None,
                })
                .collect::<Vec<_>>()
                .join("")
        })
        .unwrap_or_default()
}

fn collect_tool_uses(summary: &runtime::TurnSummary) -> Vec<serde_json::Value> {
    summary
        .assistant_messages
        .iter()
        .flat_map(|message| message.blocks.iter())
        .filter_map(|block| match block {
            ContentBlock::ToolUse { id, name, input } => Some(json!({
                "id": id,
                "name": name,
                "input": input,
            })),
            _ => None,
        })
        .collect()
}

fn collect_tool_results(summary: &runtime::TurnSummary) -> Vec<serde_json::Value> {
    summary
        .tool_results
        .iter()
        .flat_map(|message| message.blocks.iter())
        .filter_map(|block| match block {
            ContentBlock::ToolResult {
                tool_use_id,
                tool_name,
                output,
                is_error,
            } => Some(json!({
                "tool_use_id": tool_use_id,
                "tool_name": tool_name,
                "output": output,
                "is_error": is_error,
            })),
            _ => None,
        })
        .collect()
}

fn slash_command_completion_candidates() -> Vec<String> {
    slash_command_specs()
        .iter()
        .map(|spec| format!("/{}", spec.name))
        .collect()
}

fn resolve_tool_render_name(name: &str) -> &str {
    let mut canonical = name
        .chars()
        .filter(char::is_ascii_alphanumeric)
        .flat_map(char::to_lowercase)
        .collect::<String>();
    if let Some(stripped) = canonical.strip_suffix("tool") {
        canonical = stripped.to_string();
    }

    match canonical.as_str() {
        "agent" => "Agent",
        "askuserquestion" => "AskUserQuestionTool",
        "bash" => "bash",
        "brief" | "sendmessage" | "sendusermessage" => "SendUserMessage",
        "config" => "Config",
        "edit" | "editfile" | "fileedit" => "edit_file",
        "glob" | "globsearch" => "glob_search",
        "grep" | "grepsearch" => "grep_search",
        "notebookedit" => "NotebookEdit",
        "powershell" => "PowerShell",
        "read" | "readfile" | "fileread" => "read_file",
        "repl" => "REPL",
        "sessionexport" => "SessionExportTool",
        "skill" => "Skill",
        "sleep" => "Sleep",
        "todowrite" => "TodoWrite",
        "toolsearch" => "ToolSearch",
        "webfetch" => "WebFetch",
        "websearch" => "WebSearch",
        "write" | "writefile" | "filewrite" => "write_file",
        "enterplanmode" => "EnterPlanModeTool",
        "exitplanmode" | "exitplanmodev2" => "ExitPlanModeV2Tool",
        "enterworktree" => "EnterWorktreeTool",
        "exitworktree" => "ExitWorktreeTool",
        _ => name,
    }
}

fn format_tool_call_start(name: &str, input: &str) -> String {
    let resolved_name = resolve_tool_render_name(name);
    let parsed: serde_json::Value =
        serde_json::from_str(input).unwrap_or(serde_json::Value::String(input.to_string()));

    let detail = match resolved_name {
        "bash" | "Bash" => format_shell_call("$", &parsed),
        "PowerShell" => format_shell_call("PS>", &parsed),
        "read_file" | "Read" => {
            let path = extract_tool_path(&parsed);
            format!("\x1b[2m📄 Reading {path}…\x1b[0m")
        }
        "write_file" | "Write" => {
            let path = extract_tool_path(&parsed);
            let lines = parsed
                .get("content")
                .and_then(|value| value.as_str())
                .map_or(0, |content| content.lines().count());
            format!("\x1b[1;32m✏️ Writing {path}\x1b[0m \x1b[2m({lines} lines)\x1b[0m")
        }
        "edit_file" | "Edit" => {
            let path = extract_tool_path(&parsed);
            let old_value = parsed
                .get("old_string")
                .or_else(|| parsed.get("oldString"))
                .and_then(|value| value.as_str())
                .unwrap_or_default();
            let new_value = parsed
                .get("new_string")
                .or_else(|| parsed.get("newString"))
                .and_then(|value| value.as_str())
                .unwrap_or_default();
            format!(
                "\x1b[1;33m📝 Editing {path}\x1b[0m{}",
                format_patch_preview(old_value, new_value)
                    .map(|preview| format!("\n{preview}"))
                    .unwrap_or_default()
            )
        }
        "glob_search" | "Glob" => format_search_start("🔎 Glob", &parsed),
        "grep_search" | "Grep" => format_search_start("🔎 Grep", &parsed),
        "WebFetch" => {
            let url = parsed.get("url").and_then(|v| v.as_str()).unwrap_or("?");
            format!(
                "\x1b[2m↯ WebFetch {}\x1b[0m",
                truncate_for_summary(url, 80)
            )
        }
        "StructuredOutput" => {
            let fields = parsed.as_object().map(|items| items.len()).unwrap_or(0);
            format!("\x1b[2m⬢ StructuredOutput ({fields} fields)\x1b[0m")
        }
        "REPL" => {
            let language = parsed
                .get("language")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!("\x1b[2m⌁ REPL {language}\x1b[0m")
        }
        "SyntheticOutputTool" => {
            let output_type = parsed
                .get("outputType")
                .and_then(|v| v.as_str())
                .unwrap_or("text");
            format!("\x1b[2m~ SyntheticOutputTool [{output_type}]\x1b[0m")
        }
        "Sleep" => {
            let duration = parsed
                .get("duration_ms")
                .and_then(|v| v.as_u64())
                .unwrap_or(0);
            format!("\x1b[2m⏱ Sleep {duration}ms\x1b[0m")
        }
        "TodoWrite" => {
            let todos = parsed
                .get("todos")
                .and_then(|v| v.as_array())
                .map(|items| items.len())
                .unwrap_or(0);
            format!("\x1b[2m☑ TodoWrite ({todos} items)\x1b[0m")
        }
        "Skill" => {
            let skill = parsed.get("skill").and_then(|v| v.as_str()).unwrap_or("?");
            format!("\x1b[2m✦ Skill {skill}\x1b[0m")
        }
        "SessionExportTool" => {
            let path = parsed.get("path").and_then(|v| v.as_str()).unwrap_or("(auto)");
            format!(
                "\x1b[2m⇪ SessionExportTool {}\x1b[0m",
                truncate_for_summary(path, 80)
            )
        }
        "NotebookEdit" => {
            let notebook_path = parsed
                .get("notebook_path")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            let edit_mode = parsed
                .get("edit_mode")
                .and_then(|v| v.as_str())
                .unwrap_or("replace");
            format!(
                "\x1b[2m✎ NotebookEdit [{edit_mode}] {}\x1b[0m",
                truncate_for_summary(notebook_path, 80)
            )
        }
        "Config" => {
            let setting = parsed
                .get("setting")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            let value = parsed.get("value").or_else(|| parsed.get("newValue"));
            let value_summary = value
                .map(summarize_json_value)
                .filter(|summary| !summary.is_empty())
                .unwrap_or_default();
            if value_summary.is_empty() {
                format!("\x1b[2m⚙ Config {setting}\x1b[0m")
            } else {
                format!(
                    "\x1b[2m⚙ Config {setting}: {}\x1b[0m",
                    truncate_for_summary(&value_summary, 80)
                )
            }
        }
        "AskUserQuestionTool" => {
            let question = parsed
                .get("question")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!("\x1b[1;36m? {}\x1b[0m", truncate_for_summary(question, 120))
        }
        "SendUserMessage" | "Brief" | "BriefTool" => {
            let message = parsed
                .get("message")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!(
                "\x1b[2m✉ {name}: {}\x1b[0m",
                truncate_for_summary(message, 120)
            )
        }
        "Agent" => {
            let description = parsed
                .get("description")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!(
                "\x1b[38;5;99m⊕ Launching agent:\x1b[0m {}",
                truncate_for_summary(description, 100)
            )
        }
        "TaskCreateTool" => {
            let description = parsed
                .get("description")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!(
                "\x1b[38;5;99m⊕ Creating task:\x1b[0m {}",
                truncate_for_summary(description, 100)
            )
        }
        "TaskGetTool" | "TaskOutputTool" => {
            let task_id = parsed
                .get("task_id")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!(
                "\x1b[2m↩ {name} {}\x1b[0m",
                truncate_for_summary(task_id, 40)
            )
        }
        "TaskListTool" => {
            let status_hint = parsed
                .get("status")
                .and_then(|v| v.as_str())
                .map(|s| format!(" [{s}]"))
                .unwrap_or_default();
            format!("\x1b[2m↩ TaskListTool{status_hint}\x1b[0m")
        }
        "TaskStopTool" => {
            let task_id = parsed
                .get("task_id")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!(
                "\x1b[38;5;203m⊗ Stopping task {}\x1b[0m",
                truncate_for_summary(task_id, 40)
            )
        }
        "TaskUpdateTool" => {
            let task_id = parsed
                .get("task_id")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!(
                "\x1b[38;5;99m✎ Updating task {}\x1b[0m",
                truncate_for_summary(task_id, 40)
            )
        }
        "LSPTool" => {
            let command = parsed
                .get("command")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!("\x1b[2m⬡ LSP {command}\x1b[0m")
        }
        "RemoteTriggerTool" => {
            let event = parsed.get("event").and_then(|v| v.as_str()).unwrap_or("?");
            format!("\x1b[2m⇝ trigger '{event}'\x1b[0m")
        }
        "TeamCreateTool" => {
            let name_val = parsed.get("name").and_then(|v| v.as_str()).unwrap_or("?");
            format!("\x1b[2m⊕ TeamCreate '{name_val}'\x1b[0m")
        }
        "TeamDeleteTool" => {
            let team_id = parsed
                .get("team_id")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!(
                "\x1b[2m⊗ TeamDelete {}\x1b[0m",
                truncate_for_summary(team_id, 40)
            )
        }
        "CronCreateTool" => {
            let schedule = parsed
                .get("schedule")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            let command = parsed
                .get("command")
                .and_then(|v| v.as_str())
                .unwrap_or("?");
            format!(
                "\x1b[2m⊕ CronCreate [{schedule}] {}\x1b[0m",
                truncate_for_summary(command, 60)
            )
        }
        "CronDeleteTool" | "CronListTool" => {
            format!("\x1b[2m{name}\x1b[0m")
        }
        "EnterPlanModeTool" => format!("\x1b[38;5;99m⊞ Enter plan mode\x1b[0m"),
        "ExitPlanModeV2Tool" => format!("\x1b[38;5;99m⊟ Exit plan mode\x1b[0m"),
        "EnterWorktreeTool" => {
            let path = parsed
                .get("worktree_path")
                .and_then(|v| v.as_str())
                .unwrap_or("(default)");
            format!(
                "\x1b[2m⎇ EnterWorktree {}\x1b[0m",
                truncate_for_summary(path, 60)
            )
        }
        "ExitWorktreeTool" => format!("\x1b[2m⎇ ExitWorktree\x1b[0m"),
        "TestingPermissionTool" => {
            let action = parsed.get("action").and_then(|v| v.as_str()).unwrap_or("?");
            format!("\x1b[2m⚑ TestingPermission: {action}\x1b[0m")
        }
        "web_search" | "WebSearch" => parsed
            .get("query")
            .and_then(|value| value.as_str())
            .unwrap_or("?")
            .to_string(),
        _ => summarize_tool_payload(input),
    };

    let border = "─".repeat(name.len() + 8);
    format!(
        "\x1b[38;5;245m╭─ \x1b[1;36m{name}\x1b[0;38;5;245m ─╮\x1b[0m\n\x1b[38;5;245m│\x1b[0m {detail}\n\x1b[38;5;245m╰{border}╯\x1b[0m"
    )
}

fn format_tool_result(name: &str, output: &str, is_error: bool) -> String {
    let resolved_name = resolve_tool_render_name(name);
    let icon = if is_error {
        "\x1b[1;31m✗\x1b[0m"
    } else {
        "\x1b[1;32m✓\x1b[0m"
    };
    if is_error {
        if matches!(
            name,
            "ListMcpResourcesTool" | "ReadMcpResourceTool" | "MCPTool" | "McpAuthTool"
        ) || name.starts_with("mcp__")
        {
            return format_mcp_error_result(icon, name, output);
        }
        let summary = truncate_for_summary(output.trim(), 160);
        return if summary.is_empty() {
            format!("{icon} \x1b[38;5;245m{name}\x1b[0m")
        } else {
            format!("{icon} \x1b[38;5;245m{name}\x1b[0m\n\x1b[38;5;203m{summary}\x1b[0m")
        };
    }

    let parsed: serde_json::Value =
        serde_json::from_str(output).unwrap_or(serde_json::Value::String(output.to_string()));
    match resolved_name {
        "bash" | "Bash" => format_bash_result(icon, &parsed),
        "PowerShell" => format_powershell_result(icon, &parsed),
        "read_file" | "Read" => format_read_result(icon, &parsed),
        "write_file" | "Write" => format_write_result(icon, &parsed),
        "edit_file" | "Edit" => format_edit_result(icon, &parsed),
        "glob_search" | "Glob" => format_glob_result(icon, &parsed),
        "grep_search" | "Grep" => format_grep_result(icon, &parsed),
        "ListMcpResourcesTool" => format_list_mcp_resources_result(icon, &parsed),
        "ReadMcpResourceTool" => format_read_mcp_resource_result(icon, &parsed),
        "MCPTool" => format_mcp_tool_result(icon, "MCPTool", &parsed),
        "McpAuthTool" => format_mcp_auth_result(icon, &parsed),
        "WebFetch" => format_web_fetch_result(icon, &parsed),
        "web_search" | "WebSearch" => format_web_search_result(icon, &parsed),
        "StructuredOutput" => format_structured_output_result(icon, &parsed),
        "REPL" => format_repl_result(icon, &parsed),
        "Sleep" => format_sleep_result(icon, &parsed),
        "TodoWrite" => format_todo_write_result(icon, &parsed),
        "Skill" => format_skill_result(icon, &parsed),
        "SessionExportTool" => format_session_export_result(icon, &parsed),
        "ToolSearch" => format_tool_search_result(icon, &parsed),
        "NotebookEdit" => format_notebook_edit_result(icon, &parsed),
        "Config" => format_config_result(icon, &parsed),
        "AskUserQuestionTool" => format_ask_user_question_result(icon, &parsed),
        "Agent" => format_task_manifest_result(icon, name, &parsed),
        "TaskCreateTool" | "TaskGetTool" | "TaskStopTool" | "TaskUpdateTool" => {
            format_task_manifest_result(icon, name, &parsed)
        }
        "TaskListTool" => format_task_list_result(icon, &parsed),
        "TaskOutputTool" => format_task_output_result(icon, &parsed),
        "SendUserMessage" | "Brief" | "BriefTool" => format_brief_result(icon, name, &parsed),
        "TestingPermissionTool" => format_testing_permission_result(icon, &parsed),
        "TeamCreateTool" | "TeamDeleteTool" => format_team_result(icon, name, &parsed),
        "CronCreateTool" | "CronDeleteTool" => format_cron_result(icon, name, &parsed),
        "CronListTool" => format_cron_list_result(icon, &parsed),
        "EnterPlanModeTool" | "ExitPlanModeV2Tool" => format_plan_mode_result(icon, name, &parsed),
        "EnterWorktreeTool" | "ExitWorktreeTool" => format_worktree_result(icon, name, &parsed),
        "LSPTool" => format_lsp_result(icon, &parsed),
        "RemoteTriggerTool" => format_remote_trigger_result(icon, &parsed),
        "SyntheticOutputTool" => format_synthetic_output_result(icon, &parsed),
        _ if name.starts_with("mcp__") => format_mcp_tool_result(icon, name, &parsed),
        _ => format_stub_tool_result(icon, name, output),
    }
}

fn extract_tool_path(parsed: &serde_json::Value) -> String {
    parsed
        .get("file_path")
        .or_else(|| parsed.get("filePath"))
        .or_else(|| parsed.get("path"))
        .and_then(|value| value.as_str())
        .unwrap_or("?")
        .to_string()
}

fn format_search_start(label: &str, parsed: &serde_json::Value) -> String {
    let pattern = parsed
        .get("pattern")
        .and_then(|value| value.as_str())
        .unwrap_or("?");
    let scope = parsed
        .get("path")
        .and_then(|value| value.as_str())
        .unwrap_or(".");
    format!("{label} {pattern}\n\x1b[2min {scope}\x1b[0m")
}

fn format_patch_preview(old_value: &str, new_value: &str) -> Option<String> {
    if old_value.is_empty() && new_value.is_empty() {
        return None;
    }
    Some(format!(
        "\x1b[38;5;203m- {}\x1b[0m\n\x1b[38;5;70m+ {}\x1b[0m",
        truncate_for_summary(first_visible_line(old_value), 72),
        truncate_for_summary(first_visible_line(new_value), 72)
    ))
}

fn format_shell_call(prompt: &str, parsed: &serde_json::Value) -> String {
    let command = parsed
        .get("command")
        .and_then(|value| value.as_str())
        .unwrap_or_default();
    if command.is_empty() {
        String::new()
    } else {
        format!(
            "\x1b[48;5;236;38;5;255m {prompt} {} \x1b[0m",
            truncate_for_summary(command, 160)
        )
    }
}

fn first_visible_line(text: &str) -> &str {
    text.lines()
        .find(|line| !line.trim().is_empty())
        .unwrap_or(text)
}

fn format_shell_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let mut lines = vec![format!("{icon} \x1b[38;5;245m{label}\x1b[0m")];
    if let Some(task_id) = parsed
        .get("backgroundTaskId")
        .and_then(|value| value.as_str())
    {
        lines[0].push_str(&format!(" backgrounded ({task_id})"));
    } else if let Some(status) = parsed
        .get("returnCodeInterpretation")
        .and_then(|value| value.as_str())
        .filter(|status| !status.is_empty())
    {
        lines[0].push_str(&format!(" {status}"));
    }

    if let Some(stdout) = parsed.get("stdout").and_then(|value| value.as_str()) {
        if !stdout.trim().is_empty() {
            lines.push(stdout.trim_end().to_string());
        }
    }
    if let Some(stderr) = parsed.get("stderr").and_then(|value| value.as_str()) {
        if !stderr.trim().is_empty() {
            lines.push(format!("\x1b[38;5;203m{}\x1b[0m", stderr.trim_end()));
        }
    }

    lines.join("\n\n")
}

fn format_bash_result(icon: &str, parsed: &serde_json::Value) -> String {
    format_shell_result(icon, "bash", parsed)
}

fn format_powershell_result(icon: &str, parsed: &serde_json::Value) -> String {
    format_shell_result(icon, "PowerShell", parsed)
}

fn format_read_result(icon: &str, parsed: &serde_json::Value) -> String {
    let file = parsed.get("file").unwrap_or(parsed);
    let path = extract_tool_path(file);
    let start_line = file
        .get("startLine")
        .and_then(|value| value.as_u64())
        .unwrap_or(1);
    let num_lines = file
        .get("numLines")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);
    let total_lines = file
        .get("totalLines")
        .and_then(|value| value.as_u64())
        .unwrap_or(num_lines);
    let content = file
        .get("content")
        .and_then(|value| value.as_str())
        .unwrap_or_default();
    let end_line = start_line.saturating_add(num_lines.saturating_sub(1));

    format!(
        "{icon} \x1b[2m📄 Read {path} (lines {}-{} of {})\x1b[0m\n{}",
        start_line,
        end_line.max(start_line),
        total_lines,
        content
    )
}

fn format_write_result(icon: &str, parsed: &serde_json::Value) -> String {
    let path = extract_tool_path(parsed);
    let kind = parsed
        .get("type")
        .and_then(|value| value.as_str())
        .unwrap_or("write");
    let line_count = parsed
        .get("content")
        .and_then(|value| value.as_str())
        .map(|content| content.lines().count())
        .unwrap_or(0);
    format!(
        "{icon} \x1b[1;32m✏️ {} {path}\x1b[0m \x1b[2m({line_count} lines)\x1b[0m",
        if kind == "create" { "Wrote" } else { "Updated" },
    )
}

fn format_structured_patch_preview(parsed: &serde_json::Value) -> Option<String> {
    let hunks = parsed.get("structuredPatch")?.as_array()?;
    let mut preview = Vec::new();
    for hunk in hunks.iter().take(2) {
        let lines = hunk.get("lines")?.as_array()?;
        for line in lines.iter().filter_map(|value| value.as_str()).take(6) {
            match line.chars().next() {
                Some('+') => preview.push(format!("\x1b[38;5;70m{line}\x1b[0m")),
                Some('-') => preview.push(format!("\x1b[38;5;203m{line}\x1b[0m")),
                _ => preview.push(line.to_string()),
            }
        }
    }
    if preview.is_empty() {
        None
    } else {
        Some(preview.join("\n"))
    }
}

fn format_edit_result(icon: &str, parsed: &serde_json::Value) -> String {
    let path = extract_tool_path(parsed);
    let suffix = if parsed
        .get("replaceAll")
        .and_then(|value| value.as_bool())
        .unwrap_or(false)
    {
        " (replace all)"
    } else {
        ""
    };
    let preview = format_structured_patch_preview(parsed).or_else(|| {
        let old_value = parsed
            .get("oldString")
            .and_then(|value| value.as_str())
            .unwrap_or_default();
        let new_value = parsed
            .get("newString")
            .and_then(|value| value.as_str())
            .unwrap_or_default();
        format_patch_preview(old_value, new_value)
    });

    match preview {
        Some(preview) => format!("{icon} \x1b[1;33m📝 Edited {path}{suffix}\x1b[0m\n{preview}"),
        None => format!("{icon} \x1b[1;33m📝 Edited {path}{suffix}\x1b[0m"),
    }
}

fn format_glob_result(icon: &str, parsed: &serde_json::Value) -> String {
    let num_files = parsed
        .get("numFiles")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);
    let filenames = parsed
        .get("filenames")
        .and_then(|value| value.as_array())
        .map(|files| {
            files
                .iter()
                .filter_map(|value| value.as_str())
                .take(8)
                .collect::<Vec<_>>()
                .join("\n")
        })
        .unwrap_or_default();
    if filenames.is_empty() {
        format!("{icon} \x1b[38;5;245mglob_search\x1b[0m matched {num_files} files")
    } else {
        format!("{icon} \x1b[38;5;245mglob_search\x1b[0m matched {num_files} files\n{filenames}")
    }
}

fn format_grep_result(icon: &str, parsed: &serde_json::Value) -> String {
    let num_matches = parsed
        .get("numMatches")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);
    let num_files = parsed
        .get("numFiles")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);
    let content = parsed
        .get("content")
        .and_then(|value| value.as_str())
        .unwrap_or_default();
    let filenames = parsed
        .get("filenames")
        .and_then(|value| value.as_array())
        .map(|files| {
            files
                .iter()
                .filter_map(|value| value.as_str())
                .take(8)
                .collect::<Vec<_>>()
                .join("\n")
        })
        .unwrap_or_default();
    let summary = format!(
        "{icon} \x1b[38;5;245mgrep_search\x1b[0m {num_matches} matches across {num_files} files"
    );
    if !content.trim().is_empty() {
        format!("{summary}\n{}", content.trim_end())
    } else if !filenames.is_empty() {
        format!("{summary}\n{filenames}")
    } else {
        summary
    }
}

fn format_tool_search_result(icon: &str, parsed: &serde_json::Value) -> String {
    let query = parsed
        .get("query")
        .and_then(|value| value.as_str())
        .filter(|value| !value.is_empty())
        .unwrap_or("<empty query>");
    let match_count = parsed
        .get("match_details")
        .and_then(|value| value.as_array())
        .map_or_else(
            || {
                parsed
                    .get("matches")
                    .and_then(|value| value.as_array())
                    .map_or(0, Vec::len)
            },
            Vec::len,
        );
    let mut lines = vec![if match_count == 0 {
        format!("{icon} \x1b[38;5;245mToolSearch\x1b[0m no matches for {query}")
    } else {
        format!(
            "{icon} \x1b[38;5;245mToolSearch\x1b[0m {match_count} match{} for {query}",
            if match_count == 1 { "" } else { "es" }
        )
    }];

    if let Some(details) = parsed
        .get("match_details")
        .and_then(|value| value.as_array())
    {
        let rendered = details
            .iter()
            .take(4)
            .filter_map(|detail| {
                let name = detail.get("name")?.as_str()?;
                let aliases = detail
                    .get("aliases")
                    .and_then(|value| value.as_array())
                    .map(|entries| {
                        entries
                            .iter()
                            .filter_map(|entry| entry.as_str())
                            .collect::<Vec<_>>()
                    })
                    .unwrap_or_default();
                let name = if aliases.is_empty() {
                    name.to_string()
                } else {
                    format!("{name} ({})", aliases.join(", "))
                };
                let source = detail
                    .get("source")
                    .and_then(|value| value.as_str())
                    .unwrap_or("unknown");
                let permission = detail
                    .get("required_permission")
                    .and_then(|value| value.as_str())
                    .unwrap_or("unknown");
                let source_label = if source == "dynamic-mcp" {
                    detail
                        .get("mcp_server")
                        .and_then(|value| value.as_str())
                        .map(|server| format!("dynamic-mcp:{server}"))
                        .unwrap_or_else(|| source.to_string())
                } else {
                    source.to_string()
                };
                let description = detail
                    .get("description")
                    .and_then(|value| value.as_str())
                    .map(|value| truncate_for_summary(value, 72))
                    .unwrap_or_default();
                let description = if description.is_empty() {
                    String::new()
                } else {
                    format!(" {description}")
                };
                Some(format!(
                    "  - {name} [{source_label}, {permission}]{description}"
                ))
            })
            .collect::<Vec<_>>();
        if !rendered.is_empty() {
            lines.push(String::from("Matches"));
            lines.extend(rendered);
            if details.len() > 4 {
                lines.push(format!("  - +{} more", details.len() - 4));
            }
        }
    } else if let Some(matches) = parsed.get("matches").and_then(|value| value.as_array()) {
        let rendered = matches
            .iter()
            .take(4)
            .filter_map(|value| value.as_str())
            .map(|name| format!("  - {name}"))
            .collect::<Vec<_>>();
        if !rendered.is_empty() {
            lines.push(String::from("Matches"));
            lines.extend(rendered);
            if matches.len() > 4 {
                lines.push(format!("  - +{} more", matches.len() - 4));
            }
        }
    }

    if let Some(entries) = parsed
        .get("pending_mcp_server_details")
        .and_then(|value| value.as_array())
        .filter(|entries| !entries.is_empty())
    {
        lines.push(String::from("Pending MCP discovery"));
        lines.extend(entries.iter().take(3).filter_map(|entry| {
            let server = entry.get("server")?.as_str()?;
            let reason_kind = entry
                .get("reason_kind")
                .and_then(|value| value.as_str())
                .unwrap_or("unknown");
            let detail = entry
                .get("detail")
                .and_then(|value| value.as_str())
                .map(|value| truncate_for_summary(value, 96))
                .unwrap_or_default();
            let detail = if detail.is_empty() {
                String::new()
            } else {
                format!(" {detail}")
            };
            Some(format!("  - {server} [{reason_kind}]{detail}"))
        }));
        if entries.len() > 3 {
            lines.push(format!("  - +{} more pending servers", entries.len() - 3));
        }
    }

    lines.join("\n")
}

fn format_task_manifest_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let agent_id = parsed
        .get("agentId")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let status = parsed.get("status").and_then(|v| v.as_str()).unwrap_or("?");
    let name = parsed.get("name").and_then(|v| v.as_str()).unwrap_or("");
    let description = parsed
        .get("description")
        .and_then(|v| v.as_str())
        .unwrap_or("");
    let status_color = match status {
        "completed" => "\x1b[1;32m",
        "running" => "\x1b[1;33m",
        "failed" => "\x1b[1;31m",
        "stopped" => "\x1b[38;5;203m",
        _ => "\x1b[38;5;245m",
    };
    let name_suffix = if name.is_empty() {
        String::new()
    } else {
        format!(" {name}")
    };
    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245m{label}\x1b[0m{name_suffix}\n  \x1b[2mid:\x1b[0m {}\n  \x1b[2mstatus:\x1b[0m {status_color}{status}\x1b[0m",
        truncate_for_summary(agent_id, 40)
    )];
    if !description.is_empty() {
        lines.push(format!(
            "  \x1b[2mdescription:\x1b[0m {}",
            truncate_for_summary(description, 100)
        ));
    }
    lines.join("\n")
}

fn format_task_list_result(icon: &str, parsed: &serde_json::Value) -> String {
    let total = parsed.get("total").and_then(|v| v.as_u64()).unwrap_or(0);
    let tasks = parsed
        .get("tasks")
        .and_then(|v| v.as_array())
        .map(|arr| arr.as_slice())
        .unwrap_or(&[]);
    let filter_hint = parsed
        .get("filteredBy")
        .and_then(|v| v.as_str())
        .map(|s| format!(" [{s}]"))
        .unwrap_or_default();
    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mTaskListTool\x1b[0m{filter_hint} \x1b[2m({total} tasks)\x1b[0m"
    )];
    for task in tasks.iter().take(5) {
        let id = task.get("agentId").and_then(|v| v.as_str()).unwrap_or("?");
        let status = task.get("status").and_then(|v| v.as_str()).unwrap_or("?");
        let name = task.get("name").and_then(|v| v.as_str()).unwrap_or("?");
        lines.push(format!(
            "  \x1b[2m{}\x1b[0m {} [{status}]",
            truncate_for_summary(id, 20),
            truncate_for_summary(name, 30)
        ));
    }
    if total > 5 {
        lines.push(format!("  \x1b[2m+{} more\x1b[0m", total - 5));
    }
    lines.join("\n")
}

fn format_task_output_result(icon: &str, parsed: &serde_json::Value) -> String {
    let task_id = parsed.get("taskId").and_then(|v| v.as_str()).unwrap_or("?");
    let status = parsed.get("status").and_then(|v| v.as_str()).unwrap_or("?");
    let output = parsed.get("output").and_then(|v| v.as_str()).unwrap_or("");
    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mTaskOutputTool\x1b[0m {}\n  \x1b[2mstatus:\x1b[0m {status}",
        truncate_for_summary(task_id, 40)
    )];
    if !output.trim().is_empty() {
        lines.push(format!(
            "  \x1b[2moutput:\x1b[0m {}",
            truncate_for_summary(output.trim(), 120)
        ));
    }
    lines.join("\n")
}

fn format_team_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let team_id = parsed.get("teamId").and_then(|v| v.as_str()).unwrap_or("?");
    let name = parsed.get("name").and_then(|v| v.as_str()).unwrap_or("?");
    let description = parsed
        .get("description")
        .and_then(|v| v.as_str())
        .unwrap_or("");
    let created_at = parsed
        .get("createdAt")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let deleted_at = parsed.get("deletedAt").and_then(|v| v.as_str());
    let message = parsed.get("message").and_then(|v| v.as_str()).unwrap_or("");

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245m{label}\x1b[0m {}",
        truncate_for_summary(name, 40)
    )];
    lines.push(format!(
        "  \x1b[2mid:\x1b[0m {}",
        truncate_for_summary(team_id, 40)
    ));
    lines.push(format!("  \x1b[2mcreated:\x1b[0m {created_at}"));
    if let Some(deleted_at) = deleted_at {
        lines.push(format!("  \x1b[2mdeleted:\x1b[0m {deleted_at}"));
    }
    if !description.is_empty() {
        lines.push(format!(
            "  \x1b[2mdescription:\x1b[0m {}",
            truncate_for_summary(description, 72)
        ));
    }
    if !message.is_empty() {
        lines.push(format!(
            "  \x1b[2mnote:\x1b[0m {}",
            truncate_for_summary(message, 96)
        ));
    }
    lines.join("\n")
}

fn format_cron_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let cron_id = parsed.get("cronId").and_then(|v| v.as_str()).unwrap_or("?");
    let schedule = parsed
        .get("schedule")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let command = parsed
        .get("command")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let description = parsed
        .get("description")
        .and_then(|v| v.as_str())
        .unwrap_or("");
    let created_at = parsed
        .get("createdAt")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let deleted_at = parsed.get("deletedAt").and_then(|v| v.as_str());
    let message = parsed.get("message").and_then(|v| v.as_str()).unwrap_or("");
    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245m{label}\x1b[0m [{schedule}] {}",
        truncate_for_summary(command, 60)
    )];
    lines.push(format!(
        "  \x1b[2mid:\x1b[0m {}",
        truncate_for_summary(cron_id, 40)
    ));
    lines.push(format!("  \x1b[2mcreated:\x1b[0m {created_at}"));
    if let Some(deleted_at) = deleted_at {
        lines.push(format!("  \x1b[2mdeleted:\x1b[0m {deleted_at}"));
    }
    if !description.is_empty() {
        lines.push(format!(
            "  \x1b[2mdescription:\x1b[0m {}",
            truncate_for_summary(description, 72)
        ));
    }
    if !message.is_empty() {
        lines.push(format!(
            "  \x1b[2mnote:\x1b[0m {}",
            truncate_for_summary(message, 96)
        ));
    }
    lines.join("\n")
}

fn format_cron_list_result(icon: &str, parsed: &serde_json::Value) -> String {
    let total = parsed.get("total").and_then(|v| v.as_u64()).unwrap_or(0);
    let crons = parsed
        .get("crons")
        .and_then(|v| v.as_array())
        .map(|arr| arr.as_slice())
        .unwrap_or(&[]);
    let message = parsed.get("message").and_then(|v| v.as_str()).unwrap_or("");
    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mCronListTool\x1b[0m \x1b[2m({total} jobs)\x1b[0m"
    )];
    for cron in crons.iter().take(5) {
        let cron_id = cron.get("cronId").and_then(|v| v.as_str()).unwrap_or("?");
        let schedule = cron.get("schedule").and_then(|v| v.as_str()).unwrap_or("?");
        let command = cron.get("command").and_then(|v| v.as_str()).unwrap_or("?");
        lines.push(format!(
            "  \x1b[2m{}\x1b[0m [{schedule}] {}",
            truncate_for_summary(cron_id, 20),
            truncate_for_summary(command, 40)
        ));
    }
    if total > 5 {
        lines.push(format!("  \x1b[2m+{} more\x1b[0m", total - 5));
    }
    if !message.is_empty() {
        lines.push(format!("  \x1b[2m{message}\x1b[0m"));
    }
    lines.join("\n")
}

fn format_worktree_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let active = parsed
        .get("active")
        .and_then(|value| value.as_bool())
        .unwrap_or(false);
    let worktree_path = parsed
        .get("worktreePath")
        .and_then(|value| value.as_str())
        .unwrap_or("");
    let previous_path = parsed
        .get("previousPath")
        .and_then(|value| value.as_str())
        .unwrap_or("");
    let message = parsed
        .get("message")
        .and_then(|value| value.as_str())
        .unwrap_or("");

    let mut lines = vec![if active {
        format!(
            "{icon} \x1b[38;5;245m{label}\x1b[0m active {}",
            truncate_for_summary(worktree_path, 72)
        )
    } else {
        format!("{icon} \x1b[38;5;245m{label}\x1b[0m inactive")
    }];
    if !worktree_path.is_empty() {
        lines.push(format!("  \x1b[2mworktree:\x1b[0m {worktree_path}"));
    }
    if !previous_path.is_empty() {
        lines.push(format!("  \x1b[2mprevious:\x1b[0m {previous_path}"));
    }
    if !message.is_empty() {
        lines.push(format!("  \x1b[2mnote:\x1b[0m {message}"));
    }
    lines.join("\n")
}

fn format_plan_mode_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let active = parsed
        .get("active")
        .and_then(|value| value.as_bool())
        .unwrap_or(false);
    let previous_active = parsed
        .get("previousActive")
        .and_then(|value| value.as_bool())
        .unwrap_or(false);
    let message = parsed
        .get("message")
        .and_then(|value| value.as_str())
        .unwrap_or("");

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245m{label}\x1b[0m {}",
        if active { "active" } else { "inactive" }
    )];
    lines.push(format!(
        "  \x1b[2mprevious:\x1b[0m {}",
        if previous_active { "active" } else { "inactive" }
    ));
    if !message.is_empty() {
        lines.push(format!("  \x1b[2mnote:\x1b[0m {message}"));
    }
    lines.join("\n")
}

fn format_stub_tool_result(icon: &str, name: &str, output: &str) -> String {
    let summary = truncate_for_summary(output.trim(), 120);
    if summary.is_empty() {
        format!("{icon} \x1b[38;5;245m{name}\x1b[0m")
    } else {
        format!("{icon} \x1b[38;5;245m{name}\x1b[0m\n  \x1b[2m{summary}\x1b[0m")
    }
}

fn format_brief_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let message = parsed.get("message").and_then(|v| v.as_str()).unwrap_or("");
    let sent_at = parsed.get("sentAt").and_then(|v| v.as_str()).unwrap_or("?");
    let attachments = parsed
        .get("attachments")
        .and_then(|v| v.as_array())
        .map(|items| items.as_slice())
        .unwrap_or(&[]);

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245m{label}\x1b[0m {}",
        truncate_for_summary(message, 100)
    )];
    lines.push(format!("  \x1b[2msent:\x1b[0m {sent_at}"));
    if !attachments.is_empty() {
        let preview = attachments
            .iter()
            .take(3)
            .filter_map(|item| item.get("path").and_then(|v| v.as_str()))
            .map(|path| truncate_for_summary(path, 40))
            .collect::<Vec<_>>()
            .join(", ");
        let suffix = if attachments.len() > 3 {
            format!(" (+{} more)", attachments.len() - 3)
        } else {
            String::new()
        };
        lines.push(format!(
            "  \x1b[2mattachments:\x1b[0m {} {}{}",
            attachments.len(),
            preview,
            suffix
        ));
    }
    lines.join("\n")
}

fn format_notebook_edit_result(icon: &str, parsed: &serde_json::Value) -> String {
    let notebook_path = parsed
        .get("notebook_path")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let edit_mode = parsed
        .get("edit_mode")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let cell_id = parsed.get("cell_id").and_then(|v| v.as_str()).unwrap_or("(new cell)");
    let cell_type = parsed
        .get("cell_type")
        .and_then(|v| v.as_str())
        .unwrap_or("none");
    let language = parsed
        .get("language")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let new_source = parsed
        .get("new_source")
        .and_then(|v| v.as_str())
        .unwrap_or("");
    let error = parsed.get("error").and_then(|v| v.as_str()).unwrap_or("");

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mNotebookEdit\x1b[0m [{edit_mode}] {}",
        truncate_for_summary(notebook_path, 80)
    )];
    lines.push(format!(
        "  \x1b[2mcell:\x1b[0m {} [{} / {}]",
        truncate_for_summary(cell_id, 40),
        cell_type,
        language
    ));
    if !new_source.is_empty() {
        lines.push(format!(
            "  \x1b[2msource:\x1b[0m {}",
            truncate_for_summary(new_source, 100)
        ));
    }
    if !error.is_empty() {
        lines.push(format!(
            "  \x1b[2merror:\x1b[0m {}",
            truncate_for_summary(error, 100)
        ));
    }
    lines.join("\n")
}

fn format_config_result(icon: &str, parsed: &serde_json::Value) -> String {
    let success = parsed
        .get("success")
        .and_then(|v| v.as_bool())
        .unwrap_or(false);
    let operation = parsed
        .get("operation")
        .and_then(|v| v.as_str())
        .unwrap_or("unknown");
    let setting = parsed
        .get("setting")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let error = parsed.get("error").and_then(|v| v.as_str()).unwrap_or("");
    let value = parsed.get("value").map(summarize_json_value).unwrap_or_default();
    let previous_value = parsed
        .get("previousValue")
        .map(summarize_json_value)
        .unwrap_or_default();
    let new_value = parsed
        .get("newValue")
        .map(summarize_json_value)
        .unwrap_or_default();

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mConfig\x1b[0m {setting} [{}]",
        if success { operation } else { "error" }
    )];
    if !value.is_empty() && value != "null" {
        lines.push(format!(
            "  \x1b[2mvalue:\x1b[0m {}",
            truncate_for_summary(&value, 100)
        ));
    }
    if !previous_value.is_empty() && previous_value != "null" {
        lines.push(format!(
            "  \x1b[2mprevious:\x1b[0m {}",
            truncate_for_summary(&previous_value, 100)
        ));
    }
    if !new_value.is_empty() && new_value != "null" {
        lines.push(format!(
            "  \x1b[2mnew:\x1b[0m {}",
            truncate_for_summary(&new_value, 100)
        ));
    }
    if !error.is_empty() {
        lines.push(format!(
            "  \x1b[2merror:\x1b[0m {}",
            truncate_for_summary(error, 100)
        ));
    }
    lines.join("\n")
}

fn format_todo_write_result(icon: &str, parsed: &serde_json::Value) -> String {
    let old_todos = parsed
        .get("oldTodos")
        .and_then(|v| v.as_array())
        .map(|items| items.as_slice())
        .unwrap_or(&[]);
    let new_todos = parsed
        .get("newTodos")
        .and_then(|v| v.as_array())
        .map(|items| items.as_slice())
        .unwrap_or(&[]);
    let verification_nudge_needed = parsed
        .get("verificationNudgeNeeded")
        .and_then(|v| v.as_bool())
        .unwrap_or(false);

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mTodoWrite\x1b[0m \x1b[2m({} -> {} items)\x1b[0m",
        old_todos.len(),
        new_todos.len()
    )];

    for todo in new_todos.iter().take(3) {
        let status = todo.get("status").and_then(|v| v.as_str()).unwrap_or("?");
        let content = todo.get("content").and_then(|v| v.as_str()).unwrap_or("?");
        lines.push(format!(
            "  \x1b[2m[{status}]\x1b[0m {}",
            truncate_for_summary(content, 80)
        ));
    }
    if new_todos.len() > 3 {
        lines.push(format!("  \x1b[2m+{} more\x1b[0m", new_todos.len() - 3));
    }
    if verification_nudge_needed {
        lines.push(String::from(
            "  \x1b[2mverification nudge suggested before marking everything complete\x1b[0m",
        ));
    }

    lines.join("\n")
}

fn format_skill_result(icon: &str, parsed: &serde_json::Value) -> String {
    let skill = parsed.get("skill").and_then(|v| v.as_str()).unwrap_or("?");
    let path = parsed.get("path").and_then(|v| v.as_str()).unwrap_or("?");
    let args = parsed.get("args").and_then(|v| v.as_str()).unwrap_or("");
    let description = parsed
        .get("description")
        .and_then(|v| v.as_str())
        .unwrap_or("");
    let prompt = parsed.get("prompt").and_then(|v| v.as_str()).unwrap_or("");

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mSkill\x1b[0m {skill}"
    )];
    lines.push(format!(
        "  \x1b[2mpath:\x1b[0m {}",
        truncate_for_summary(path, 80)
    ));
    if !args.is_empty() {
        lines.push(format!(
            "  \x1b[2margs:\x1b[0m {}",
            truncate_for_summary(args, 80)
        ));
    }
    if !description.is_empty() {
        lines.push(format!(
            "  \x1b[2mdescription:\x1b[0m {}",
            truncate_for_summary(description, 100)
        ));
    }
    if !prompt.is_empty() {
        lines.push(format!(
            "  \x1b[2mprompt:\x1b[0m {}",
            truncate_for_summary(prompt, 100)
        ));
    }

    lines.join("\n")
}

fn format_session_export_result(icon: &str, parsed: &serde_json::Value) -> String {
    let session_id = parsed.get("sessionId").and_then(|v| v.as_str()).unwrap_or("?");
    let session_path = parsed
        .get("sessionPath")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let export_path = parsed
        .get("exportPath")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let message_count = parsed
        .get("messageCount")
        .and_then(|v| v.as_u64())
        .unwrap_or(0);

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mSessionExportTool\x1b[0m {session_id} \x1b[2m({message_count} messages)\x1b[0m"
    )];
    lines.push(format!(
        "  \x1b[2mfile:\x1b[0m {}",
        truncate_for_summary(export_path, 100)
    ));
    if !session_path.is_empty() {
        lines.push(format!(
            "  \x1b[2msession:\x1b[0m {}",
            truncate_for_summary(session_path, 100)
        ));
    }
    lines.join("\n")
}

fn format_web_fetch_result(icon: &str, parsed: &serde_json::Value) -> String {
    let url = parsed.get("url").and_then(|v| v.as_str()).unwrap_or("?");
    let code = parsed.get("code").and_then(|v| v.as_u64()).unwrap_or(0);
    let code_text = parsed
        .get("codeText")
        .and_then(|v| v.as_str())
        .unwrap_or("");
    let bytes = parsed.get("bytes").and_then(|v| v.as_u64()).unwrap_or(0);
    let duration_ms = parsed
        .get("durationMs")
        .and_then(|v| v.as_u64())
        .unwrap_or(0);
    let result = parsed.get("result").and_then(|v| v.as_str()).unwrap_or("");

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mWebFetch\x1b[0m [{code} {code_text}] {}",
        truncate_for_summary(url, 80)
    )];
    lines.push(format!("  \x1b[2mbytes:\x1b[0m {bytes}"));
    lines.push(format!("  \x1b[2mduration:\x1b[0m {duration_ms}ms"));
    if !result.is_empty() {
        lines.push(format!(
            "  \x1b[2mresult:\x1b[0m {}",
            truncate_for_summary(result, 100)
        ));
    }
    lines.join("\n")
}

fn format_web_search_result(icon: &str, parsed: &serde_json::Value) -> String {
    let query = parsed.get("query").and_then(|v| v.as_str()).unwrap_or("?");
    let duration_seconds = parsed
        .get("durationSeconds")
        .and_then(|v| v.as_f64())
        .unwrap_or(0.0);
    let results = parsed
        .get("results")
        .and_then(|v| v.as_array())
        .map(|items| items.as_slice())
        .unwrap_or(&[]);

    let mut commentary = String::new();
    let mut hits: Vec<&serde_json::Value> = Vec::new();
    for item in results {
        if let Some(text) = item.as_str() {
            if commentary.is_empty() {
                commentary = text.to_string();
            }
            continue;
        }
        if let Some(content) = item.get("content").and_then(|v| v.as_array()) {
            hits.extend(content.iter());
        }
    }

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mWebSearch\x1b[0m {} \x1b[2m({:.2}s, {} hits)\x1b[0m",
        truncate_for_summary(query, 80),
        duration_seconds,
        hits.len()
    )];
    if !commentary.is_empty() {
        lines.push(format!(
            "  \x1b[2msummary:\x1b[0m {}",
            truncate_for_summary(&commentary, 100)
        ));
    }
    for hit in hits.iter().take(3) {
        let title = hit.get("title").and_then(|v| v.as_str()).unwrap_or("?");
        let url = hit.get("url").and_then(|v| v.as_str()).unwrap_or("?");
        lines.push(format!(
            "  \x1b[2m•\x1b[0m {} {}",
            truncate_for_summary(title, 50),
            truncate_for_summary(url, 60)
        ));
    }
    if hits.len() > 3 {
        lines.push(format!("  \x1b[2m+{} more hits\x1b[0m", hits.len() - 3));
    }
    lines.join("\n")
}

fn format_structured_output_result(icon: &str, parsed: &serde_json::Value) -> String {
    let data = parsed.get("data").and_then(|v| v.as_str()).unwrap_or("");
    let structured = parsed
        .get("structured_output")
        .map(summarize_json_value)
        .unwrap_or_default();

    let mut lines = vec![format!("{icon} \x1b[38;5;245mStructuredOutput\x1b[0m")];
    if !data.is_empty() {
        lines.push(format!(
            "  \x1b[2mdata:\x1b[0m {}",
            truncate_for_summary(data, 100)
        ));
    }
    if !structured.is_empty() {
        lines.push(format!(
            "  \x1b[2mstructured:\x1b[0m {}",
            truncate_for_summary(&structured, 100)
        ));
    }
    lines.join("\n")
}

fn format_repl_result(icon: &str, parsed: &serde_json::Value) -> String {
    let language = parsed
        .get("language")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let exit_code = parsed
        .get("exitCode")
        .and_then(|v| v.as_i64())
        .unwrap_or(1);
    let duration_ms = parsed
        .get("durationMs")
        .and_then(|v| v.as_u64())
        .unwrap_or(0);
    let stdout = parsed.get("stdout").and_then(|v| v.as_str()).unwrap_or("");
    let stderr = parsed.get("stderr").and_then(|v| v.as_str()).unwrap_or("");

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mREPL\x1b[0m {language} [exit {exit_code}]"
    )];
    lines.push(format!("  \x1b[2mduration:\x1b[0m {duration_ms}ms"));
    if !stdout.is_empty() {
        lines.push(format!(
            "  \x1b[2mstdout:\x1b[0m {}",
            truncate_for_summary(stdout, 100)
        ));
    }
    if !stderr.is_empty() {
        lines.push(format!(
            "  \x1b[2mstderr:\x1b[0m {}",
            truncate_for_summary(stderr, 100)
        ));
    }
    lines.join("\n")
}

fn format_sleep_result(icon: &str, parsed: &serde_json::Value) -> String {
    let duration_ms = parsed
        .get("duration_ms")
        .and_then(|v| v.as_u64())
        .unwrap_or(0);
    let message = parsed.get("message").and_then(|v| v.as_str()).unwrap_or("");

    format!(
        "{icon} \x1b[38;5;245mSleep\x1b[0m {duration_ms}ms\n  \x1b[2m{}\x1b[0m",
        truncate_for_summary(message, 100)
    )
}

fn format_synthetic_output_result(icon: &str, parsed: &serde_json::Value) -> String {
    let content = parsed.get("content").and_then(|v| v.as_str()).unwrap_or("");
    let output_type = parsed
        .get("outputType")
        .and_then(|v| v.as_str())
        .unwrap_or("text");
    format!(
        "{icon} \x1b[38;5;245mSyntheticOutputTool\x1b[0m [{output_type}]\n  \x1b[2m{}\x1b[0m",
        truncate_for_summary(content, 100)
    )
}

fn format_lsp_result(icon: &str, parsed: &serde_json::Value) -> String {
    let command = parsed.get("command").and_then(|v| v.as_str()).unwrap_or("?");
    let connected = parsed
        .get("connected")
        .and_then(|v| v.as_bool())
        .unwrap_or(false);
    let reason_kind = parsed
        .get("reasonKind")
        .and_then(|v| v.as_str())
        .unwrap_or("unknown");
    let message = parsed.get("message").and_then(|v| v.as_str()).unwrap_or("");
    let supported = parsed
        .get("supportedCommands")
        .and_then(|v| v.as_array())
        .map(|items| {
            items
                .iter()
                .filter_map(|item| item.as_str())
                .collect::<Vec<_>>()
                .join(", ")
        })
        .unwrap_or_default();

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mLSPTool\x1b[0m {command} [{}]",
        if connected { "connected" } else { reason_kind }
    )];
    if !supported.is_empty() {
        lines.push(format!(
            "  \x1b[2msupported:\x1b[0m {}",
            truncate_for_summary(&supported, 100)
        ));
    }
    if !message.is_empty() {
        lines.push(format!(
            "  \x1b[2mnote:\x1b[0m {}",
            truncate_for_summary(message, 100)
        ));
    }
    lines.join("\n")
}

fn format_remote_trigger_result(icon: &str, parsed: &serde_json::Value) -> String {
    let event = parsed.get("event").and_then(|v| v.as_str()).unwrap_or("?");
    let triggered = parsed
        .get("triggered")
        .and_then(|v| v.as_bool())
        .unwrap_or(false);
    let remote_enabled = parsed
        .get("remoteEnabled")
        .and_then(|v| v.as_bool())
        .unwrap_or(false);
    let path_ready = parsed
        .get("pathReady")
        .and_then(|v| v.as_bool())
        .unwrap_or(false);
    let session_id = parsed.get("sessionId").and_then(|v| v.as_str()).unwrap_or("");
    let base_url = parsed.get("baseUrl").and_then(|v| v.as_str()).unwrap_or("");
    let blocker_kind = parsed
        .get("blockerKind")
        .and_then(|v| v.as_str())
        .unwrap_or("unknown");
    let blocker_detail = parsed
        .get("blockerDetail")
        .and_then(|v| v.as_str())
        .unwrap_or("");
    let message = parsed.get("message").and_then(|v| v.as_str()).unwrap_or("");

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mRemoteTriggerTool\x1b[0m '{}' [{}]",
        truncate_for_summary(event, 40),
        if triggered { "triggered" } else { blocker_kind }
    )];
    lines.push(format!(
        "  \x1b[2mremote:\x1b[0m {} | \x1b[2mpath:\x1b[0m {}",
        if remote_enabled { "enabled" } else { "disabled" },
        if path_ready { "ready" } else { "blocked" }
    ));
    if !session_id.is_empty() {
        lines.push(format!(
            "  \x1b[2msession:\x1b[0m {}",
            truncate_for_summary(session_id, 48)
        ));
    }
    if !base_url.is_empty() {
        lines.push(format!(
            "  \x1b[2mbase:\x1b[0m {}",
            truncate_for_summary(base_url, 80)
        ));
    }
    if !blocker_detail.is_empty() {
        lines.push(format!(
            "  \x1b[2mblocker:\x1b[0m {}",
            truncate_for_summary(blocker_detail, 100)
        ));
    }
    if !message.is_empty() {
        lines.push(format!(
            "  \x1b[2mnote:\x1b[0m {}",
            truncate_for_summary(message, 100)
        ));
    }
    lines.join("\n")
}

fn format_testing_permission_result(icon: &str, parsed: &serde_json::Value) -> String {
    let action = parsed
        .get("action")
        .and_then(|value| value.as_str())
        .unwrap_or("?");
    let tool_name = parsed
        .get("toolName")
        .and_then(|value| value.as_str())
        .unwrap_or("?");
    let current_mode = parsed
        .get("currentMode")
        .and_then(|value| value.as_str())
        .unwrap_or("?");
    let required_mode = parsed
        .get("requiredMode")
        .and_then(|value| value.as_str())
        .unwrap_or("?");
    let outcome = parsed
        .get("outcome")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let path = parsed
        .get("path")
        .and_then(|value| value.as_str())
        .unwrap_or("");
    let reason = parsed
        .get("reason")
        .and_then(|value| value.as_str())
        .unwrap_or("");
    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mTestingPermissionTool\x1b[0m {action} -> {tool_name} [{outcome}] {current_mode} -> {required_mode}"
    )];
    if !path.is_empty() {
        lines.push(format!(
            "  \x1b[2mPath\x1b[0m {}",
            truncate_for_summary(path, 100)
        ));
    }
    if !reason.is_empty() {
        lines.push(format!(
            "  \x1b[2mReason\x1b[0m {}",
            truncate_for_summary(reason, 180)
        ));
    }
    lines.join("\n")
}

fn format_ask_user_question_result(icon: &str, parsed: &serde_json::Value) -> String {
    let question = parsed
        .get("question")
        .and_then(|v| v.as_str())
        .unwrap_or("?");
    let answer = parsed.get("answer").and_then(|v| v.as_str()).unwrap_or("");
    let mut lines = vec![format!("{icon} \x1b[38;5;245mAskUserQuestionTool\x1b[0m")];
    lines.push(format!(
        "  \x1b[2mQ:\x1b[0m {}",
        truncate_for_summary(question, 100)
    ));
    if !answer.is_empty() {
        lines.push(format!(
            "  \x1b[2mA:\x1b[0m {}",
            truncate_for_summary(answer, 100)
        ));
    }
    lines.join("\n")
}

fn format_mcp_error_result(icon: &str, label: &str, output: &str) -> String {
    let trimmed = output.trim();
    let summary = truncate_for_summary(trimmed, 160);
    let server = extract_mcp_server_name_from_error(trimmed);
    let reason_kind = runtime::classify_mcp_reason_kind(trimmed).as_str();
    let context = extract_mcp_error_context(trimmed);
    let mut tags = vec![reason_kind.to_string()];
    if let Some(operation) = context.operation {
        tags.push(operation.to_string());
    }
    if let Some(http_status) = context.http_status {
        tags.push(format!("HTTP {http_status}"));
    }
    let tags = tags.join(", ");

    let header = match server {
        Some(server) => format!("{icon} \x1b[38;5;245m{label}\x1b[0m {server} [{tags}]"),
        None => format!("{icon} \x1b[38;5;245m{label}\x1b[0m [{tags}]"),
    };

    let mut lines = vec![header];
    if !summary.is_empty() {
        lines.push(format!("\x1b[38;5;203m{summary}\x1b[0m"));
    }
    if let Some(hint) = runtime::mcp_reason_remediation_hint(trimmed) {
        lines.push(format!("\x1b[38;5;246mHint {hint}\x1b[0m"));
    }
    lines.join("\n")
}

fn extract_mcp_server_name_from_error(output: &str) -> Option<&str> {
    let marker = "MCP server `";
    let start = output.find(marker)? + marker.len();
    let remainder = &output[start..];
    let end = remainder.find('`')?;
    Some(&remainder[..end])
}

#[derive(Debug, Clone, Copy, Default, PartialEq, Eq)]
struct McpErrorContext<'a> {
    operation: Option<&'a str>,
    http_status: Option<u16>,
}

fn extract_mcp_error_context(output: &str) -> McpErrorContext<'_> {
    if let Some((http_status, operation)) = extract_mcp_http_error_context(output) {
        return McpErrorContext {
            operation,
            http_status: Some(http_status),
        };
    }
    if let Some(operation) = extract_mcp_jsonrpc_error_operation(output) {
        return McpErrorContext {
            operation: Some(operation),
            http_status: None,
        };
    }
    if let Some(operation) = extract_mcp_request_failure_operation(output) {
        return McpErrorContext {
            operation: Some(operation),
            http_status: None,
        };
    }
    McpErrorContext::default()
}

fn extract_mcp_http_error_context(output: &str) -> Option<(u16, Option<&str>)> {
    let marker = " failed with HTTP ";
    if let Some(position) = output.find(marker) {
        let status_and_detail = &output[position + marker.len()..];
        let status_end = status_and_detail
            .find(':')
            .unwrap_or(status_and_detail.len());
        let http_status = status_and_detail[..status_end].trim().parse().ok()?;
        let operation = if output.starts_with("OAuth refresh for MCP server `") {
            Some("oauth-refresh")
        } else if output.starts_with("OAuth metadata request for MCP server `") {
            Some("oauth-metadata")
        } else {
            None
        };
        return Some((http_status, operation));
    }

    let marker = " returned HTTP ";
    let position = output.find(marker)?;
    let status_and_rest = &output[position + marker.len()..];
    let (status, rest) = status_and_rest.split_once(" for ")?;
    let http_status = status.trim().parse().ok()?;
    let operation_end = rest.find(':').unwrap_or(rest.len());
    let operation = rest[..operation_end].trim();
    let operation = (!operation.is_empty()).then_some(operation);
    Some((http_status, operation))
}

fn extract_mcp_jsonrpc_error_operation(output: &str) -> Option<&str> {
    let marker = " returned JSON-RPC error for ";
    let position = output.find(marker)?;
    let rest = &output[position + marker.len()..];
    let operation_end = rest.find(':').unwrap_or(rest.len());
    let operation = rest[..operation_end].trim();
    (!operation.is_empty()).then_some(operation)
}

fn extract_mcp_request_failure_operation(output: &str) -> Option<&str> {
    let marker = " request failed";
    let position = output.find(marker)?;
    let prefix = &output[..position];
    let operation = prefix.rsplit_once(' ')?.1.trim();
    (!operation.is_empty()).then_some(operation)
}

fn format_list_mcp_resources_result(icon: &str, parsed: &serde_json::Value) -> String {
    let server = parsed
        .get("server")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let transport = parsed
        .get("transport")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let resource_count = parsed
        .get("resourceCount")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mListMcpResourcesTool\x1b[0m {server} [{transport}] {resource_count} resource{}",
        if resource_count == 1 { "" } else { "s" }
    )];

    if let Some(resources) = parsed.get("resources").and_then(|value| value.as_array()) {
        let rendered = resources
            .iter()
            .take(4)
            .filter_map(format_mcp_resource_entry)
            .collect::<Vec<_>>();
        if !rendered.is_empty() {
            lines.push(String::from("Resources"));
            lines.extend(rendered);
            if resources.len() > 4 {
                lines.push(format!("  - +{} more resources", resources.len() - 4));
            }
        }
    }

    lines.join("\n")
}

fn summarize_json_value(value: &serde_json::Value) -> String {
    match value {
        serde_json::Value::Null => String::from("null"),
        serde_json::Value::Bool(flag) => flag.to_string(),
        serde_json::Value::Number(number) => number.to_string(),
        serde_json::Value::String(text) => text.clone(),
        _ => serde_json::to_string(value).unwrap_or_default(),
    }
}

fn format_read_mcp_resource_result(icon: &str, parsed: &serde_json::Value) -> String {
    let server = parsed
        .get("server")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let transport = parsed
        .get("transport")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let uri = parsed
        .get("uri")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let content_count = parsed
        .get("contentCount")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mReadMcpResourceTool\x1b[0m {uri} from {server} [{transport}] {content_count} item{}",
        if content_count == 1 { "" } else { "s" }
    )];

    if let Some(contents) = parsed.get("contents").and_then(|value| value.as_array()) {
        let rendered = contents
            .iter()
            .take(4)
            .map(format_mcp_resource_content_entry)
            .collect::<Vec<_>>();
        if !rendered.is_empty() {
            lines.push(String::from("Contents"));
            lines.extend(rendered);
            if contents.len() > 4 {
                lines.push(format!("  - +{} more content items", contents.len() - 4));
            }
        }
    }

    lines.join("\n")
}

fn format_mcp_resource_entry(entry: &serde_json::Value) -> Option<String> {
    let uri = entry.get("uri")?.as_str()?;
    let mut details = Vec::new();
    if let Some(name) = entry.get("name").and_then(|value| value.as_str()) {
        if !name.is_empty() {
            details.push(name.to_string());
        }
    }
    if let Some(mime_type) = entry.get("mimeType").and_then(|value| value.as_str()) {
        if !mime_type.is_empty() {
            details.push(format!("[{mime_type}]"));
        }
    }
    if let Some(description) = entry.get("description").and_then(|value| value.as_str()) {
        if !description.is_empty() {
            details.push(truncate_for_summary(description, 72));
        }
    }
    let details = if details.is_empty() {
        String::new()
    } else {
        format!(" {}", details.join(" "))
    };
    Some(format!("  - {uri}{details}"))
}

fn format_mcp_resource_content_entry(entry: &serde_json::Value) -> String {
    let uri = entry
        .get("uri")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let mime_type = entry
        .get("mimeType")
        .and_then(|value| value.as_str())
        .filter(|value| !value.is_empty())
        .map(|value| format!(" [{value}]"))
        .unwrap_or_default();

    if let Some(text) = entry.get("text").and_then(|value| value.as_str()) {
        return format!("  - {uri}{mime_type} {}", truncate_for_summary(text, 96));
    }

    if let Some(blob) = entry.get("blob").and_then(|value| value.as_str()) {
        return format!("  - {uri}{mime_type} blob {} chars", blob.chars().count());
    }

    format!("  - {uri}{mime_type}")
}

fn format_mcp_tool_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    match parsed
        .get("action")
        .and_then(|value| value.as_str())
        .unwrap_or_default()
    {
        "list_tools" => format_mcp_tool_list_result(icon, label, parsed),
        "call_tool" => format_mcp_tool_call_result(icon, label, parsed),
        _ => {
            let summary = truncate_for_summary(&parsed.to_string(), 200);
            format!("{icon} \x1b[38;5;245m{label}:\x1b[0m {summary}")
        }
    }
}

fn format_mcp_tool_list_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let server = parsed
        .get("server")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let transport = parsed
        .get("transport")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let tool_count = parsed
        .get("toolCount")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245m{label}\x1b[0m list_tools {server} [{transport}] {tool_count} tool{}",
        if tool_count == 1 { "" } else { "s" }
    )];

    if let Some(tools) = parsed.get("tools").and_then(|value| value.as_array()) {
        let rendered = tools
            .iter()
            .take(4)
            .filter_map(|tool| {
                let name = tool.get("name")?.as_str()?;
                let description = tool
                    .get("description")
                    .and_then(|value| value.as_str())
                    .map(|value| truncate_for_summary(value, 72))
                    .unwrap_or_default();
                let description = if description.is_empty() {
                    String::new()
                } else {
                    format!(" {description}")
                };
                Some(format!("  - {name}{description}"))
            })
            .collect::<Vec<_>>();
        if !rendered.is_empty() {
            lines.push(String::from("Tools"));
            lines.extend(rendered);
            if tools.len() > 4 {
                lines.push(format!("  - +{} more tools", tools.len() - 4));
            }
        }
    }

    lines.join("\n")
}

fn format_mcp_tool_call_result(icon: &str, label: &str, parsed: &serde_json::Value) -> String {
    let server = parsed
        .get("server")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let transport = parsed
        .get("transport")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let tool = parsed
        .get("tool")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let qualified_name = parsed
        .get("qualifiedToolName")
        .and_then(|value| value.as_str())
        .unwrap_or(tool);
    let is_error = parsed
        .get("isError")
        .and_then(|value| value.as_bool())
        .unwrap_or(false);

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245m{label}\x1b[0m call_tool {qualified_name} on {server} [{transport}]{}",
        if is_error { " error" } else { "" }
    )];

    if let Some(content) = parsed.get("content").and_then(|value| value.as_array()) {
        let rendered = content
            .iter()
            .take(3)
            .map(format_mcp_tool_content_entry)
            .collect::<Vec<_>>();
        if !rendered.is_empty() {
            lines.push(String::from("Content"));
            lines.extend(rendered);
            if content.len() > 3 {
                lines.push(format!("  - +{} more content items", content.len() - 3));
            }
        }
    }

    if let Some(structured) = parsed.get("structuredContent") {
        if !structured.is_null() {
            lines.push(format!(
                "Structured {}",
                truncate_for_summary(&structured.to_string(), 120)
            ));
        }
    }

    lines.join("\n")
}

fn format_mcp_tool_content_entry(entry: &serde_json::Value) -> String {
    match entry.get("type").and_then(|value| value.as_str()) {
        Some("text") => {
            let text = entry
                .get("text")
                .and_then(|value| value.as_str())
                .map(|value| truncate_for_summary(value, 96))
                .unwrap_or_else(|| truncate_for_summary(&entry.to_string(), 96));
            format!("  - text {text}")
        }
        Some(content_type) => format!(
            "  - {content_type} {}",
            truncate_for_summary(&entry.to_string(), 96)
        ),
        None => format!("  - {}", truncate_for_summary(&entry.to_string(), 96)),
    }
}

fn format_mcp_auth_result(icon: &str, parsed: &serde_json::Value) -> String {
    let action = parsed
        .get("action")
        .and_then(|value| value.as_str())
        .filter(|value| !value.is_empty())
        .unwrap_or("status");
    let server_count = parsed
        .get("serverCount")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);
    let supported_count = parsed
        .get("supportedExecutionCount")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);
    let unsupported_count = parsed
        .get("unsupportedExecutionCount")
        .and_then(|value| value.as_u64())
        .unwrap_or(0);

    let mut lines = vec![format!(
        "{icon} \x1b[38;5;245mMcpAuthTool\x1b[0m {action} {server_count} server{} ({supported_count} executable, {unsupported_count} blocked)",
        if server_count == 1 { "" } else { "s" }
    )];

    if let Some(status_counts) = parsed
        .get("statusCounts")
        .and_then(|value| value.as_object())
    {
        let mut rendered = status_counts
            .iter()
            .filter_map(|(status, count)| count.as_u64().map(|count| format!("{status}={count}")))
            .collect::<Vec<_>>();
        rendered.sort();
        if !rendered.is_empty() {
            lines.push(format!("Statuses {}", rendered.join(", ")));
        }
    }

    if let Some(entries) = parsed
        .get("attentionServers")
        .and_then(|value| value.as_array())
        .filter(|entries| !entries.is_empty())
    {
        lines.push(String::from("Attention"));
        lines.extend(
            entries
                .iter()
                .take(3)
                .filter_map(format_mcp_auth_attention_entry),
        );
        if entries.len() > 3 {
            lines.push(format!("  - +{} more attention servers", entries.len() - 3));
        }
    }

    if let Some(entries) = parsed
        .get("servers")
        .and_then(|value| value.as_array())
        .filter(|entries| !entries.is_empty() && (action != "status" || entries.len() <= 2))
    {
        let rendered = entries
            .iter()
            .take(3)
            .filter_map(format_mcp_auth_server_entry)
            .collect::<Vec<_>>();
        if !rendered.is_empty() {
            lines.push(String::from("Servers"));
            lines.extend(rendered);
            if entries.len() > 3 {
                lines.push(format!("  - +{} more servers", entries.len() - 3));
            }
        }
    }

    lines.join("\n")
}

fn format_mcp_auth_attention_entry(entry: &serde_json::Value) -> Option<String> {
    let server = entry.get("server")?.as_str()?;
    let transport = entry
        .get("transport")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let status = entry
        .get("status")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let reason_kind = entry
        .get("reasonKind")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");
    let detail = entry
        .get("detail")
        .and_then(|value| value.as_str())
        .map(|value| truncate_for_summary(value, 96))
        .unwrap_or_default();
    let detail = if detail.is_empty() {
        String::new()
    } else {
        format!(" {detail}")
    };

    Some(format!(
        "  - {server} [{transport}, {status}, {reason_kind}]{detail}"
    ))
}

fn format_mcp_auth_server_entry(entry: &serde_json::Value) -> Option<String> {
    let server = entry.get("server")?.as_str()?;
    let status = entry
        .get("status")
        .and_then(|value| value.as_str())
        .unwrap_or("unknown");

    let mut tags = Vec::new();
    if let Some(auth_kind) = entry.get("authKind").and_then(|value| value.as_str()) {
        if auth_kind != "none" {
            tags.push(auth_kind.to_string());
        }
    }
    if let Some(reason_kind) = entry.get("reasonKind").and_then(|value| value.as_str()) {
        tags.push(reason_kind.to_string());
    }
    if entry
        .get("storedCredentials")
        .and_then(|value| value.as_bool())
        .unwrap_or(false)
    {
        tags.push(String::from("stored-credentials"));
    }
    if entry
        .get("refreshTokenPresent")
        .and_then(|value| value.as_bool())
        .unwrap_or(false)
    {
        tags.push(String::from("refresh-token"));
    }

    let tags = if tags.is_empty() {
        String::new()
    } else {
        format!(" {}", tags.join(", "))
    };
    let detail = entry
        .get("detail")
        .and_then(|value| value.as_str())
        .map(|value| truncate_for_summary(value, 96))
        .unwrap_or_default();
    let detail = if detail.is_empty() {
        String::new()
    } else {
        format!(" {detail}")
    };

    Some(format!("  - {server} [{status}]{tags}{detail}"))
}

fn summarize_tool_payload(payload: &str) -> String {
    let compact = match serde_json::from_str::<serde_json::Value>(payload) {
        Ok(value) => value.to_string(),
        Err(_) => payload.trim().to_string(),
    };
    truncate_for_summary(&compact, 96)
}

fn truncate_for_summary(value: &str, limit: usize) -> String {
    let mut chars = value.chars();
    let truncated = chars.by_ref().take(limit).collect::<String>();
    if chars.next().is_some() {
        format!("{truncated}…")
    } else {
        truncated
    }
}

fn push_output_block(
    block: OutputContentBlock,
    out: &mut (impl Write + ?Sized),
    events: &mut Vec<AssistantEvent>,
    pending_tool: &mut Option<(String, String, String)>,
    streaming_tool_input: bool,
) -> Result<(), RuntimeError> {
    match block {
        OutputContentBlock::Text { text } => {
            if !text.is_empty() {
                let rendered = TerminalRenderer::new().markdown_to_ansi(&text);
                write!(out, "{rendered}")
                    .and_then(|()| out.flush())
                    .map_err(|error| RuntimeError::new(error.to_string()))?;
                events.push(AssistantEvent::TextDelta(text));
            }
        }
        OutputContentBlock::ToolUse { id, name, input } => {
            // During streaming, the initial content_block_start has an empty input ({}).
            // The real input arrives via input_json_delta events. In
            // non-streaming responses, preserve a legitimate empty object.
            let initial_input = if streaming_tool_input
                && input.is_object()
                && input.as_object().is_some_and(serde_json::Map::is_empty)
            {
                String::new()
            } else {
                input.to_string()
            };
            *pending_tool = Some((id, name, initial_input));
        }
    }
    Ok(())
}

fn response_to_events(
    response: MessageResponse,
    out: &mut (impl Write + ?Sized),
) -> Result<Vec<AssistantEvent>, RuntimeError> {
    let mut events = Vec::new();
    let mut pending_tool = None;

    for block in response.content {
        push_output_block(block, out, &mut events, &mut pending_tool, false)?;
        if let Some((id, name, input)) = pending_tool.take() {
            events.push(AssistantEvent::ToolUse { id, name, input });
        }
    }

    events.push(AssistantEvent::Usage(TokenUsage {
        input_tokens: response.usage.input_tokens,
        output_tokens: response.usage.output_tokens,
        cache_creation_input_tokens: response.usage.cache_creation_input_tokens,
        cache_read_input_tokens: response.usage.cache_read_input_tokens,
    }));
    events.push(AssistantEvent::MessageStop);
    Ok(events)
}

struct CliToolExecutor {
    renderer: TerminalRenderer,
    emit_output: bool,
    allowed_tools: Option<AllowedToolSet>,
}

impl CliToolExecutor {
    fn new(allowed_tools: Option<AllowedToolSet>, emit_output: bool) -> Self {
        Self {
            renderer: TerminalRenderer::new(),
            emit_output,
            allowed_tools,
        }
    }

    fn execute_with_writer(
        &mut self,
        tool_name: &str,
        input: &str,
        out: &mut impl Write,
    ) -> Result<String, ToolError> {
        if self
            .allowed_tools
            .as_ref()
            .is_some_and(|allowed| !tool_name_is_allowed(allowed, tool_name))
        {
            return Err(ToolError::new(format!(
                "tool `{tool_name}` is not enabled by the current --allowedTools setting"
            )));
        }
        let value = serde_json::from_str(input)
            .map_err(|error| ToolError::new(format!("invalid tool input JSON: {error}")))?;
        match execute_tool(tool_name, &value) {
            Ok(output) => {
                if self.emit_output {
                    let markdown = format_tool_result(tool_name, &output, false);
                    self.renderer
                        .stream_markdown(&markdown, out)
                        .map_err(|error| ToolError::new(error.to_string()))?;
                }
                Ok(output)
            }
            Err(error) => {
                if self.emit_output {
                    let markdown = format_tool_result(tool_name, &error, true);
                    self.renderer
                        .stream_markdown(&markdown, out)
                        .map_err(|stream_error| ToolError::new(stream_error.to_string()))?;
                }
                Err(ToolError::new(error))
            }
        }
    }
}

impl ToolExecutor for CliToolExecutor {
    fn execute(&mut self, tool_name: &str, input: &str) -> Result<String, ToolError> {
        self.execute_with_writer(tool_name, input, &mut io::stdout())
    }
}

fn permission_policy(mode: PermissionMode) -> PermissionPolicy {
    tool_permission_specs()
        .into_iter()
        .fold(PermissionPolicy::new(mode), |policy, spec| {
            policy.with_tool_requirement(spec.name, spec.required_permission)
        })
}

fn tool_permission_specs() -> Vec<ToolSpec> {
    mvp_tool_specs()
}

fn convert_messages(messages: &[ConversationMessage]) -> Vec<InputMessage> {
    messages
        .iter()
        .filter_map(|message| {
            let role = match message.role {
                MessageRole::System | MessageRole::User | MessageRole::Tool => "user",
                MessageRole::Assistant => "assistant",
            };
            let content = message
                .blocks
                .iter()
                .map(|block| match block {
                    ContentBlock::Text { text } => InputContentBlock::Text { text: text.clone() },
                    ContentBlock::ToolUse { id, name, input } => InputContentBlock::ToolUse {
                        id: id.clone(),
                        name: name.clone(),
                        input: serde_json::from_str(input)
                            .unwrap_or_else(|_| serde_json::json!({ "raw": input })),
                    },
                    ContentBlock::ToolResult {
                        tool_use_id,
                        output,
                        is_error,
                        ..
                    } => InputContentBlock::ToolResult {
                        tool_use_id: tool_use_id.clone(),
                        content: vec![ToolResultContentBlock::Text {
                            text: output.clone(),
                        }],
                        is_error: *is_error,
                    },
                })
                .collect::<Vec<_>>();
            (!content.is_empty()).then(|| InputMessage {
                role: role.to_string(),
                content,
            })
        })
        .collect()
}

fn print_help_to(out: &mut impl Write) -> io::Result<()> {
    writeln!(out, "claw v{VERSION}")?;
    writeln!(out)?;
    writeln!(out, "Usage:")?;
    writeln!(
        out,
        "  claw [--model MODEL] [--provider PROVIDER] [--allowedTools TOOL[,TOOL...]]"
    )?;
    writeln!(out, "      Start the interactive REPL")?;
    writeln!(
        out,
        "  claw [--model MODEL] [--provider PROVIDER] [--output-format text|json|ndjson] prompt TEXT"
    )?;
    writeln!(out, "      Send one prompt and exit")?;
    writeln!(
        out,
        "  claw [--model MODEL] [--provider PROVIDER] [--output-format text|json|ndjson] TEXT"
    )?;
    writeln!(out, "      Shorthand non-interactive prompt mode")?;
    writeln!(
        out,
        "  claw [--output-format text|json|ndjson] --resume SESSION.json [/status] [/compact] [...]"
    )?;
    writeln!(
        out,
        "      Inspect or maintain a saved session without entering the REPL"
    )?;
    writeln!(out, "  claw dump-manifests")?;
    writeln!(out, "  claw bootstrap-plan")?;
    writeln!(out, "  claw system-prompt [--cwd PATH] [--date YYYY-MM-DD]")?;
    writeln!(out, "  claw config [env|hooks|model|provider]")?;
    writeln!(out, "  claw hooks [pre|post]")?;
    writeln!(out, "  claw mcp [server]")?;
    writeln!(out, "  claw memory")?;
    writeln!(out, "  claw agents [name]")?;
    writeln!(out, "  claw plugin [name]")?;
    writeln!(out, "  claw reload-plugins")?;
    writeln!(out, "  claw remote-env")?;
    writeln!(out, "  claw remote-setup")?;
    writeln!(out, "  claw tools [name]")?;
    writeln!(out, "  claw doctor")?;
    writeln!(out, "  claw skills [skill]")?;
    writeln!(out, "  claw tasks [id]")?;
    writeln!(out, "  claw export [file]")?;
    writeln!(out, "  claw session [list|switch <session-id>]")?;
    writeln!(out, "  claw login")?;
    writeln!(out, "      OAuth login; supports text and ndjson output")?;
    writeln!(out, "  claw logout")?;
    writeln!(
        out,
        "      Clear saved OAuth credentials; supports text, json, and ndjson output"
    )?;
    writeln!(out, "  claw init")?;
    writeln!(out)?;
    writeln!(out, "Flags:")?;
    writeln!(
        out,
        "  --model MODEL              Override the active model"
    )?;
    writeln!(
        out,
        "  --provider PROVIDER        Override the active provider (simcoe, anthropic, openai, ollama)"
    )?;
    writeln!(
        out,
        "  --output-format FORMAT     Non-interactive output format: text, json, or ndjson"
    )?;
    writeln!(
        out,
        "  --permission-mode MODE     Set read-only, workspace-write, or danger-full-access"
    )?;
    writeln!(
        out,
        "  --dangerously-skip-permissions  Skip all permission checks"
    )?;
    writeln!(out, "  --allowedTools TOOLS       Restrict enabled tools (repeatable; aliases supported, e.g. read or FileReadTool)")?;
    writeln!(
        out,
        "  --version, -V              Print version and build information locally"
    )?;
    writeln!(out)?;
    writeln!(out, "Interactive slash commands:")?;
    writeln!(out, "{}", render_slash_command_help())?;
    writeln!(out)?;
    let resume_commands = resume_supported_slash_commands()
        .into_iter()
        .map(|spec| match spec.argument_hint {
            Some(argument_hint) => format!("/{} {}", spec.name, argument_hint),
            None => format!("/{}", spec.name),
        })
        .collect::<Vec<_>>()
        .join(", ");
    writeln!(out, "Resume-safe commands: {resume_commands}")?;
    writeln!(out, "Examples:")?;
    writeln!(out, "  claw --model simcoe-opus \"summarize this repo\"")?;
    writeln!(
        out,
        "  claw --output-format json prompt \"explain src/main.rs\""
    )?;
    writeln!(
        out,
        "  claw --output-format ndjson prompt \"trace the assistant turn\""
    )?;
    writeln!(
        out,
        "  claw --allowedTools read,glob \"summarize Cargo.toml\""
    )?;
    writeln!(
        out,
        "  claw --resume session.json /status /diff /export notes.txt"
    )?;
    writeln!(
        out,
        "  claw --output-format json --resume session.json /status /cost"
    )?;
    writeln!(out, "  claw --output-format json dump-manifests")?;
    writeln!(out, "  claw --output-format json config hooks")?;
    writeln!(out, "  claw --output-format ndjson mcp repo-server")?;
    writeln!(out, "  claw --output-format json agents reviewer")?;
    writeln!(out, "  claw --output-format json remote-env")?;
    writeln!(out, "  claw --output-format ndjson login")?;
    writeln!(out, "  claw --output-format json logout")?;
    writeln!(out, "  claw login")?;
    writeln!(out, "  claw init")?;
    Ok(())
}

fn print_help() {
    let _ = print_help_to(&mut io::stdout());
}

#[cfg(test)]
mod tests {
    use crate::args::{
        named_cli_subcommands, normalize_permission_mode, resolve_model_alias, CliOutputFormat,
    };
    use crate::VERSION;

    use super::format::{
        format_compact_report, format_cost_report, format_model_report, format_model_switch_report,
        format_permissions_report, format_permissions_switch_report, format_resume_report,
        format_status_report, render_agents_report, render_config_report, render_doctor_report,
        render_hooks_report, render_mcp_report, render_memory_report, render_plugin_report,
        render_reload_plugins_report, render_remote_env_report, render_remote_setup_report,
        render_repl_help, render_skills_report, render_tasks_report, render_tools_report,
        render_version_report, status_context, StatusContext, StatusUsage,
    };
    use super::{
        active_runtime_provider_label, apply_openai_stream_chunk, bootstrap_plan_payload,
        build_openai_chat_completion_request, build_resume_command_record,
        build_resume_json_payload, build_resume_start_record, build_resume_summary_record,
        build_runtime_api_client_for_provider, filter_tool_specs, flush_openai_stream_buffers,
        format_tool_call_start, format_tool_result, inferred_error_metadata,
        inferred_error_output_format, oauth_config_for_login, openai_chat_completion_url,
        openai_compatible_transport_config, parse_args, parse_git_status_metadata,
        parse_openai_sse_frame, print_help_to, push_output_block,
        render_openai_chat_completion_response, resolve_runtime_provider, response_to_events,
        resume_supported_slash_commands, run_resume_command, slash_command_specs, version_payload,
        CliAction, CliExitError, CliToolExecutor, OpenAiAssistantMessage,
        OpenAiChatCompletionChoice, OpenAiChatCompletionChunk, OpenAiChatCompletionChunkChoice,
        OpenAiChatCompletionChunkDelta, OpenAiChatCompletionResponse, OpenAiChatCompletionUsage,
        OpenAiSseFrame, OpenAiSseParser, OpenAiToolCall, OpenAiToolCallDelta,
        OpenAiToolFunctionCall, OpenAiToolFunctionDelta, PendingOpenAiToolCall, RuntimeProvider,
        SimcoeRuntimeClient, SlashCommand, DEFAULT_ANTHROPIC_BASE_URL, DEFAULT_MODEL,
        DEFAULT_OLLAMA_BASE_URL, DEFAULT_OPENAI_BASE_URL,
    };
    use crate::render::{MarkdownStreamState, TerminalRenderer};
    use api::{MessageResponse, OutputContentBlock, Usage};
    use compat_harness::{load_parity_manifest, ParityStatus, UpstreamPaths};
    use runtime::{
        mcp_credentials_key, ApiRequest, AssistantEvent, ConfigSource, ContentBlock,
        ConversationMessage, McpOAuthConfig, McpRemoteServerConfig, McpServerConfig, MessageRole,
        PermissionMode, ScopedMcpServerConfig,
    };
    use serde_json::json;
    use std::collections::{BTreeMap, BTreeSet};
    use std::fs;
    use std::io::{Read, Write};
    use std::net::TcpListener;
    use std::path::PathBuf;
    use std::process::Command;
    use std::sync::{Mutex, OnceLock};
    use std::thread;
    use tools::mvp_tool_specs;

    #[test]
    fn defaults_to_repl_when_no_args() {
        assert_eq!(
            parse_args(&[]).expect("args should parse"),
            CliAction::Repl {
                model: DEFAULT_MODEL.to_string(),
                provider: None,
                allowed_tools: None,
                permission_mode: PermissionMode::DangerFullAccess,
            }
        );
    }

    fn current_repo_root() -> PathBuf {
        PathBuf::from(env!("CARGO_MANIFEST_DIR"))
            .join("../../..")
            .canonicalize()
            .expect("canonical repo root")
    }

    fn current_parity_manifest() -> compat_harness::ParityManifest {
        load_parity_manifest(&UpstreamPaths::from_repo_root(current_repo_root()))
            .expect("load parity manifest")
    }

    fn cli_action_name(action: &CliAction) -> &'static str {
        match action {
            CliAction::DumpManifests { .. } => "dump-manifests",
            CliAction::BootstrapPlan { .. } => "bootstrap-plan",
            CliAction::PrintSystemPrompt { .. } => "system-prompt",
            CliAction::Config { .. } => "config",
            CliAction::Hooks { .. } => "hooks",
            CliAction::Mcp { .. } => "mcp",
            CliAction::Memory { .. } => "memory",
            CliAction::Agents { .. } => "agents",
            CliAction::Plugin { .. } => "plugin",
            CliAction::ReloadPlugins { .. } => "reload-plugins",
            CliAction::RemoteEnv { .. } => "remote-env",
            CliAction::RemoteSetup { .. } => "remote-setup",
            CliAction::Tools { .. } => "tools",
            CliAction::Doctor { .. } => "doctor",
            CliAction::Skills { .. } => "skills",
            CliAction::Tasks { .. } => "tasks",
            CliAction::Export { .. } => "export",
            CliAction::Session { .. } => "session",
            CliAction::Version { .. } => "version",
            CliAction::ResumeSession { .. } => "resume",
            CliAction::Prompt { .. } => "prompt",
            CliAction::Login { .. } => "login",
            CliAction::Logout { .. } => "logout",
            CliAction::Init { .. } => "init",
            CliAction::Repl { .. } => "repl",
            CliAction::Help => "help",
        }
    }

    fn minimal_named_cli_args(command: &str) -> Vec<String> {
        match command {
            "prompt" => vec![command.to_string(), "test prompt".to_string()],
            _ => vec![command.to_string()],
        }
    }

    #[test]
    fn runtime_client_initializes_without_auth() {
        assert!(
            SimcoeRuntimeClient::new(DEFAULT_MODEL.to_string(), true, false, None, None,).is_ok()
        );
    }

    #[test]
    fn resolve_runtime_provider_accepts_supported_aliases() {
        assert_eq!(
            resolve_runtime_provider(None).expect("default provider"),
            RuntimeProvider::Simcoe
        );
        assert_eq!(
            resolve_runtime_provider(Some("simcoe")).expect("simcoe provider"),
            RuntimeProvider::Simcoe
        );
        assert_eq!(
            resolve_runtime_provider(Some("claude")).expect("claude provider"),
            RuntimeProvider::Anthropic
        );
        assert_eq!(
            resolve_runtime_provider(Some("chatgpt")).expect("chatgpt provider"),
            RuntimeProvider::OpenAi
        );
        assert_eq!(
            resolve_runtime_provider(Some("local")).expect("local provider"),
            RuntimeProvider::Ollama
        );
    }

    #[test]
    fn resolve_runtime_provider_rejects_unknown_values() {
        let error =
            resolve_runtime_provider(Some("mystery")).expect_err("unknown provider should fail");
        assert!(error.to_string().contains("unsupported provider 'mystery'"));
    }

    #[test]
    fn active_runtime_provider_label_prefers_cli_override() {
        let label =
            active_runtime_provider_label(Some(" claude ")).expect("provider label should resolve");
        assert_eq!(label, "anthropic");
    }

    #[test]
    fn runtime_api_client_supports_anthropic_provider() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let _anthropic_key_guard = ScopedEnvVar::set("ANTHROPIC_API_KEY", "anthropic-test-key");
        let _anthropic_base_guard =
            ScopedEnvVar::set("ANTHROPIC_BASE_URL", "https://anthropic.test");
        let _simcoe_key_guard = ScopedEnvVar::remove("SIMCOE_AI_API_KEY");
        let _simcoe_auth_guard = ScopedEnvVar::remove("SIMCOE_AI_AUTH_TOKEN");
        let _simcoe_base_guard = ScopedEnvVar::remove("SIMCOE_AI_BASE_URL");

        let client = build_runtime_api_client_for_provider(RuntimeProvider::Anthropic)
            .expect("anthropic client should build");
        assert_eq!(client.auth_source().api_key(), Some("anthropic-test-key"));
        assert_eq!(client.auth_source().bearer_token(), None);
        assert_eq!(client.base_url(), "https://anthropic.test");
    }

    #[test]
    fn runtime_api_client_uses_default_anthropic_base_url() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let _anthropic_key_guard = ScopedEnvVar::set("ANTHROPIC_API_KEY", "anthropic-test-key");
        let _anthropic_base_guard = ScopedEnvVar::remove("ANTHROPIC_BASE_URL");

        let client = build_runtime_api_client_for_provider(RuntimeProvider::Anthropic)
            .expect("anthropic client should build");
        assert_eq!(client.base_url(), DEFAULT_ANTHROPIC_BASE_URL);
    }

    #[test]
    fn runtime_api_client_builder_rejects_openai_compatible_providers() {
        let error = build_runtime_api_client_for_provider(RuntimeProvider::OpenAi)
            .expect_err("openai provider should use the OpenAI-compatible adapter");
        assert!(error
            .to_string()
            .contains("provider 'openai' uses the OpenAI-compatible transport"));
    }

    #[test]
    fn openai_transport_config_reads_api_overrides() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let _openai_key_guard = ScopedEnvVar::set("OPENAI_API_KEY", "openai-test-key");
        let _openai_base_guard = ScopedEnvVar::set("OPENAI_BASE_URL", "https://openai.test/v1");

        let config = openai_compatible_transport_config(RuntimeProvider::OpenAi)
            .expect("openai transport config should resolve");
        assert_eq!(config.api_key, "openai-test-key");
        assert_eq!(config.base_url, "https://openai.test/v1");
        assert_eq!(
            openai_chat_completion_url(&config.base_url),
            "https://openai.test/v1/chat/completions"
        );
    }

    #[test]
    fn ollama_transport_config_defaults_to_local_openai_compat_endpoint() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let _ollama_key_guard = ScopedEnvVar::remove("OLLAMA_API_KEY");
        let _ollama_base_guard = ScopedEnvVar::remove("OLLAMA_BASE_URL");

        let config = openai_compatible_transport_config(RuntimeProvider::Ollama)
            .expect("ollama transport config should resolve");
        assert_eq!(config.api_key, "ollama");
        assert_eq!(config.base_url, DEFAULT_OLLAMA_BASE_URL);
        assert_eq!(
            openai_chat_completion_url(DEFAULT_OPENAI_BASE_URL),
            "https://api.openai.com/v1/chat/completions"
        );
    }

    #[test]
    fn openai_request_builder_preserves_tool_history() {
        let request = ApiRequest {
            system_prompt: vec!["System guidance".to_string()],
            messages: vec![
                ConversationMessage::user_text("Read the repo"),
                ConversationMessage::assistant_with_usage(
                    vec![
                        ContentBlock::Text {
                            text: "Checking files".to_string(),
                        },
                        ContentBlock::ToolUse {
                            id: "toolu_123".to_string(),
                            name: "read_file".to_string(),
                            input: "{\"path\":\"README.md\"}".to_string(),
                        },
                    ],
                    None,
                ),
                ConversationMessage::tool_result("toolu_123", "read_file", "# Readme", false),
            ],
        };

        let request = build_openai_chat_completion_request(&request, DEFAULT_MODEL, true, None)
            .expect("openai request should build");
        assert_eq!(request.model, DEFAULT_MODEL);
        assert_eq!(request.messages[0].role, "system");
        assert_eq!(request.messages[0].content, json!("System guidance"));
        assert_eq!(request.messages[1].role, "user");
        assert_eq!(request.messages[1].content, json!("Read the repo"));
        assert_eq!(request.messages[2].role, "assistant");
        assert_eq!(request.messages[2].content, json!("Checking files"));
        assert_eq!(
            request.messages[2].tool_calls.as_ref().expect("tool calls")[0]
                .function
                .name,
            "read_file"
        );
        assert_eq!(
            request.messages[2].tool_calls.as_ref().expect("tool calls")[0]
                .function
                .arguments,
            "{\"path\":\"README.md\"}"
        );
        assert_eq!(request.messages[3].role, "tool");
        assert_eq!(
            request.messages[3].tool_call_id.as_deref(),
            Some("toolu_123")
        );
        assert_eq!(request.messages[3].content, json!("# Readme"));
        assert!(request
            .tools
            .as_ref()
            .is_some_and(|tools| !tools.is_empty()));
        assert_eq!(request.tool_choice.as_deref(), Some("auto"));
    }

    #[test]
    fn openai_response_rendering_emits_text_tool_use_and_usage() {
        let response = OpenAiChatCompletionResponse {
            id: "chatcmpl_123".to_string(),
            choices: vec![OpenAiChatCompletionChoice {
                message: OpenAiAssistantMessage {
                    content: Some(json!("Need file contents.")),
                    tool_calls: Some(vec![OpenAiToolCall {
                        id: "call_123".to_string(),
                        kind: "function".to_string(),
                        function: OpenAiToolFunctionCall {
                            name: "read_file".to_string(),
                            arguments: "{\"path\":\"README.md\"}".to_string(),
                        },
                    }]),
                },
            }],
            usage: Some(OpenAiChatCompletionUsage {
                prompt_tokens: 11,
                completion_tokens: 7,
            }),
        };

        let mut output = Vec::new();
        let events = render_openai_chat_completion_response(response, &mut output, None)
            .expect("openai response should render");

        assert_eq!(
            events,
            vec![
                AssistantEvent::TextDelta("Need file contents.".to_string()),
                AssistantEvent::ToolUse {
                    id: "call_123".to_string(),
                    name: "read_file".to_string(),
                    input: "{\"path\":\"README.md\"}".to_string(),
                },
                AssistantEvent::Usage(runtime::TokenUsage {
                    input_tokens: 11,
                    output_tokens: 7,
                    cache_creation_input_tokens: 0,
                    cache_read_input_tokens: 0,
                }),
                AssistantEvent::MessageStop,
            ]
        );

        let rendered = String::from_utf8(output).expect("rendered output should be utf8");
        assert!(rendered.contains("Need file contents."));
        assert!(rendered.contains("read_file"));
    }

    #[test]
    fn openai_sse_parser_handles_chunked_frames_and_done() {
        let mut parser = OpenAiSseParser::new();
        assert!(parser
            .push(b"data: {\"choices\":[{\"index\":0,\"delta\":{\"content\":\"Hel")
            .expect("first chunk should buffer")
            .is_empty());

        let frames = parser
            .push(b"lo\"},\"finish_reason\":null}]}\n\n")
            .expect("second chunk should parse");
        assert_eq!(
            frames,
            vec![OpenAiSseFrame::Chunk(OpenAiChatCompletionChunk {
                choices: vec![OpenAiChatCompletionChunkChoice {
                    index: 0,
                    delta: OpenAiChatCompletionChunkDelta {
                        content: Some("Hello".to_string()),
                        tool_calls: None,
                    },
                    finish_reason: None,
                }],
                usage: None,
            })]
        );
        assert_eq!(
            parse_openai_sse_frame("data: [DONE]\n\n").expect("done should parse"),
            Some(OpenAiSseFrame::Done)
        );
    }

    #[test]
    fn openai_stream_chunk_application_accumulates_tool_calls_until_finish() {
        let renderer = TerminalRenderer::new();
        let mut markdown_stream = MarkdownStreamState::default();
        let mut pending_tool_calls: BTreeMap<usize, PendingOpenAiToolCall> = BTreeMap::new();
        let mut events = Vec::new();
        let mut output = Vec::new();

        let first_chunk = OpenAiChatCompletionChunk {
            choices: vec![OpenAiChatCompletionChunkChoice {
                index: 0,
                delta: OpenAiChatCompletionChunkDelta {
                    content: Some("Need ".to_string()),
                    tool_calls: Some(vec![OpenAiToolCallDelta {
                        index: 0,
                        id: Some("call_123".to_string()),
                        kind: Some("function".to_string()),
                        function: Some(OpenAiToolFunctionDelta {
                            name: Some("read_file".to_string()),
                            arguments: Some("{\"path\":".to_string()),
                        }),
                    }]),
                },
                finish_reason: None,
            }],
            usage: None,
        };

        let second_chunk = OpenAiChatCompletionChunk {
            choices: vec![OpenAiChatCompletionChunkChoice {
                index: 0,
                delta: OpenAiChatCompletionChunkDelta {
                    content: Some("repo.".to_string()),
                    tool_calls: Some(vec![OpenAiToolCallDelta {
                        index: 0,
                        id: None,
                        kind: None,
                        function: Some(OpenAiToolFunctionDelta {
                            name: None,
                            arguments: Some("\"README.md\"}".to_string()),
                        }),
                    }]),
                },
                finish_reason: Some("tool_calls".to_string()),
            }],
            usage: Some(OpenAiChatCompletionUsage {
                prompt_tokens: 9,
                completion_tokens: 5,
            }),
        };

        assert!(!apply_openai_stream_chunk(
            first_chunk,
            &renderer,
            &mut markdown_stream,
            &mut pending_tool_calls,
            &mut events,
            &mut output,
            None,
        )
        .expect("first chunk should apply"));
        assert_eq!(pending_tool_calls.len(), 1);

        assert!(apply_openai_stream_chunk(
            second_chunk,
            &renderer,
            &mut markdown_stream,
            &mut pending_tool_calls,
            &mut events,
            &mut output,
            None,
        )
        .expect("second chunk should apply"));
        flush_openai_stream_buffers(
            &renderer,
            &mut markdown_stream,
            &mut pending_tool_calls,
            &mut events,
            &mut output,
        )
        .expect("final flush should succeed");

        assert!(pending_tool_calls.is_empty());
        assert_eq!(
            events,
            vec![
                AssistantEvent::TextDelta("Need ".to_string()),
                AssistantEvent::TextDelta("repo.".to_string()),
                AssistantEvent::ToolUse {
                    id: "call_123".to_string(),
                    name: "read_file".to_string(),
                    input: "{\"path\":\"README.md\"}".to_string(),
                },
                AssistantEvent::Usage(runtime::TokenUsage {
                    input_tokens: 9,
                    output_tokens: 5,
                    cache_creation_input_tokens: 0,
                    cache_read_input_tokens: 0,
                }),
            ]
        );

        let rendered = String::from_utf8(output).expect("rendered output should be utf8");
        assert!(rendered.contains("Need repo."));
        assert!(rendered.contains("read_file"));
    }

    #[test]
    fn parity_manifest_matches_slash_command_registry() {
        let manifest = current_parity_manifest();
        let expected = manifest
            .slash_commands
            .into_iter()
            .map(|command| (command.name, command.resume_supported))
            .collect::<Vec<_>>();
        let actual = slash_command_specs()
            .iter()
            .map(|spec| (spec.name.to_string(), spec.resume_supported))
            .collect::<Vec<_>>();

        assert_eq!(actual, expected);
    }

    #[test]
    fn parity_manifest_matches_named_cli_subcommands() {
        let manifest = current_parity_manifest();
        let expected = manifest
            .named_cli_subcommands
            .into_iter()
            .map(|command| command.name)
            .collect::<Vec<_>>();
        let actual = named_cli_subcommands()
            .iter()
            .map(|command| (*command).to_string())
            .collect::<Vec<_>>();

        assert_eq!(actual, expected);

        for command in named_cli_subcommands() {
            let args = minimal_named_cli_args(command);
            let action = parse_args(&args).expect("named CLI subcommand should parse");
            assert_eq!(cli_action_name(&action), *command);
        }
    }

    #[test]
    fn parity_manifest_matches_native_tool_registry() {
        let manifest = current_parity_manifest();
        let actual = mvp_tool_specs()
            .into_iter()
            .map(|spec| spec.name.to_string())
            .collect::<Vec<_>>();

        assert_eq!(manifest.native_tools, actual);
    }

    #[test]
    fn parity_manifest_tracks_current_subsystem_status_rows() {
        let manifest = current_parity_manifest();
        let expected_names = vec![
            "auth",
            "sessions",
            "cli",
            "structured-output",
            "tools",
            "hooks",
            "skills",
            "plugins",
            "remote",
            "assistant",
            "services",
        ];
        let actual_names = manifest
            .subsystems
            .iter()
            .map(|subsystem| subsystem.name.as_str())
            .collect::<Vec<_>>();

        assert_eq!(actual_names, expected_names);
        assert_eq!(
            manifest
                .subsystems
                .iter()
                .find(|subsystem| subsystem.name == "plugins")
                .expect("plugins row")
                .status,
            ParityStatus::InspectionOnly
        );
        assert_eq!(
            manifest
                .subsystems
                .iter()
                .find(|subsystem| subsystem.name == "remote")
                .expect("remote row")
                .status,
            ParityStatus::DiagnosticOnly
        );
        assert_eq!(
            manifest
                .subsystems
                .iter()
                .find(|subsystem| subsystem.name == "cli")
                .expect("cli row")
                .status,
            ParityStatus::Partial
        );
    }

    #[test]
    fn resumed_help_uses_resume_filtered_help() {
        let session = runtime::Session::new();
        let session_path = PathBuf::from("session.json");

        let outcome = run_resume_command(session_path.as_path(), &session, &SlashCommand::Help)
            .expect("resumed help should render");
        let message = outcome.message.expect("help message");

        assert!(message.contains("Resume-compatible slash commands"));
        assert!(message.contains("/help"));
        assert!(message.contains("/config [env|hooks|model|provider]"));
        assert!(message.contains("/session [list|switch <session-id>]"));
        assert!(!message.contains("/review [context]"));
        assert!(!message.contains("/login"));
    }

    #[test]
    fn login_requires_explicit_oauth_config() {
        let error = oauth_config_for_login(None).expect_err("login should require oauth config");
        assert!(error.to_string().contains("missing oauth config"));
        assert!(error.to_string().contains(".simcoe.json"));
    }

    #[test]
    fn parses_prompt_subcommand() {
        let args = vec![
            "prompt".to_string(),
            "hello".to_string(),
            "world".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::Prompt {
                prompt: "hello world".to_string(),
                model: DEFAULT_MODEL.to_string(),
                provider: None,
                output_format: CliOutputFormat::Text,
                allowed_tools: None,
                permission_mode: PermissionMode::DangerFullAccess,
            }
        );
    }

    #[test]
    fn parses_bare_prompt_and_json_output_flag() {
        let args = vec![
            "--output-format=json".to_string(),
            "--model".to_string(),
            "simcoe-opus".to_string(),
            "explain".to_string(),
            "this".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::Prompt {
                prompt: "explain this".to_string(),
                model: "simcoe-opus-4-6".to_string(),
                provider: None,
                output_format: CliOutputFormat::Json,
                allowed_tools: None,
                permission_mode: PermissionMode::DangerFullAccess,
            }
        );
    }

    #[test]
    fn parses_bare_prompt_and_ndjson_output_flag() {
        let args = vec![
            "--output-format=ndjson".to_string(),
            "trace".to_string(),
            "this".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::Prompt {
                prompt: "trace this".to_string(),
                model: DEFAULT_MODEL.to_string(),
                provider: None,
                output_format: CliOutputFormat::Ndjson,
                allowed_tools: None,
                permission_mode: PermissionMode::DangerFullAccess,
            }
        );
    }

    #[test]
    fn resolves_model_aliases_in_args() {
        let args = vec![
            "--model".to_string(),
            "opus".to_string(),
            "explain".to_string(),
            "this".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::Prompt {
                prompt: "explain this".to_string(),
                model: "simcoe-opus-4-6".to_string(),
                provider: None,
                output_format: CliOutputFormat::Text,
                allowed_tools: None,
                permission_mode: PermissionMode::DangerFullAccess,
            }
        );
    }

    #[test]
    fn parses_provider_flag_for_prompt_and_repl() {
        let prompt_args = vec![
            "--provider=anthropic".to_string(),
            "prompt".to_string(),
            "hello".to_string(),
        ];
        assert_eq!(
            parse_args(&prompt_args).expect("prompt args should parse"),
            CliAction::Prompt {
                prompt: "hello".to_string(),
                model: DEFAULT_MODEL.to_string(),
                provider: Some("anthropic".to_string()),
                output_format: CliOutputFormat::Text,
                allowed_tools: None,
                permission_mode: PermissionMode::DangerFullAccess,
            }
        );

        let repl_args = vec!["--provider".to_string(), "local".to_string()];
        assert_eq!(
            parse_args(&repl_args).expect("repl args should parse"),
            CliAction::Repl {
                model: DEFAULT_MODEL.to_string(),
                provider: Some("local".to_string()),
                allowed_tools: None,
                permission_mode: PermissionMode::DangerFullAccess,
            }
        );
    }

    #[test]
    fn resolves_known_model_aliases() {
        assert_eq!(resolve_model_alias("simcoe-opus"), "simcoe-opus-4-6");
        assert_eq!(resolve_model_alias("simcoe-sonnet"), "simcoe-sonnet-4-6");
        assert_eq!(
            resolve_model_alias("simcoe-haiku"),
            "simcoe-haiku-4-5-20251213"
        );
        assert_eq!(resolve_model_alias("simcoe-custom"), "simcoe-custom");
    }

    #[test]
    fn parses_version_flags_without_initializing_prompt_mode() {
        assert_eq!(
            parse_args(&["--version".to_string()]).expect("args should parse"),
            CliAction::Version {
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["-V".to_string()]).expect("args should parse"),
            CliAction::Version {
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["--output-format=json".to_string(), "--version".to_string()])
                .expect("args should parse"),
            CliAction::Version {
                output_format: CliOutputFormat::Json,
            }
        );
    }

    #[test]
    fn parses_permission_mode_flag() {
        let args = vec!["--permission-mode=read-only".to_string()];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::Repl {
                model: DEFAULT_MODEL.to_string(),
                provider: None,
                allowed_tools: None,
                permission_mode: PermissionMode::ReadOnly,
            }
        );
    }

    #[test]
    fn parses_allowed_tools_flags_with_aliases_and_lists() {
        let args = vec![
            "--allowedTools".to_string(),
            "read,glob,FileReadTool,SendMessageTool,ExitPlanModeTool".to_string(),
            "--allowed-tools=write_file".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::Repl {
                model: DEFAULT_MODEL.to_string(),
                provider: None,
                allowed_tools: Some(
                    [
                        "ExitPlanModeV2Tool",
                        "SendUserMessage",
                        "glob_search",
                        "read_file",
                        "write_file",
                    ]
                        .into_iter()
                        .map(str::to_string)
                        .collect()
                ),
                permission_mode: PermissionMode::DangerFullAccess,
            }
        );
    }

    #[test]
    fn rejects_unknown_allowed_tools() {
        let error = parse_args(&["--allowedTools".to_string(), "teleport".to_string()])
            .expect_err("tool should be rejected");
        assert!(error.contains("unsupported tool in --allowedTools: teleport"));
    }

    #[test]
    fn parses_system_prompt_options() {
        let args = vec![
            "system-prompt".to_string(),
            "--cwd".to_string(),
            "/tmp/project".to_string(),
            "--date".to_string(),
            "2026-04-01".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::PrintSystemPrompt {
                cwd: PathBuf::from("/tmp/project"),
                date: "2026-04-01".to_string(),
                output_format: CliOutputFormat::Text,
            }
        );
    }

    #[test]
    fn parses_direct_inspection_subcommands() {
        assert_eq!(
            parse_args(&["config".to_string()]).expect("config should parse"),
            CliAction::Config {
                section: None,
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&[
                "--output-format=json".to_string(),
                "config".to_string(),
                "hooks".to_string(),
            ])
            .expect("config section should parse"),
            CliAction::Config {
                section: Some("hooks".to_string()),
                output_format: CliOutputFormat::Json,
            }
        );
        assert_eq!(
            parse_args(&["hooks".to_string(), "pre".to_string()]).expect("hooks should parse"),
            CliAction::Hooks {
                event: Some("pre".to_string()),
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&[
                "--output-format=ndjson".to_string(),
                "mcp".to_string(),
                "repo-server".to_string(),
            ])
            .expect("mcp should parse"),
            CliAction::Mcp {
                server: Some("repo-server".to_string()),
                output_format: CliOutputFormat::Ndjson,
            }
        );
        assert_eq!(
            parse_args(&["memory".to_string()]).expect("memory should parse"),
            CliAction::Memory {
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["agents".to_string(), "reviewer".to_string()])
                .expect("agents should parse"),
            CliAction::Agents {
                agent: Some("reviewer".to_string()),
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["--output-format=json".to_string(), "plugin".to_string()])
                .expect("plugin should parse"),
            CliAction::Plugin {
                surface: None,
                output_format: CliOutputFormat::Json,
            }
        );
        assert_eq!(
            parse_args(&["reload-plugins".to_string()]).expect("reload-plugins should parse"),
            CliAction::ReloadPlugins {
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["--output-format=json".to_string(), "remote-env".to_string()])
                .expect("remote-env should parse"),
            CliAction::RemoteEnv {
                output_format: CliOutputFormat::Json,
            }
        );
        assert_eq!(
            parse_args(&["remote-setup".to_string()]).expect("remote-setup should parse"),
            CliAction::RemoteSetup {
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["tools".to_string(), "grep_search".to_string()])
                .expect("tools should parse"),
            CliAction::Tools {
                tool: Some("grep_search".to_string()),
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["session".to_string()]).expect("session should parse"),
            CliAction::Session {
                action: None,
                target: None,
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["export".to_string()]).expect("export should parse"),
            CliAction::Export {
                path: None,
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&[
                "--output-format=json".to_string(),
                "session".to_string(),
                "switch".to_string(),
                "session-123".to_string(),
            ])
            .expect("session switch should parse"),
            CliAction::Session {
                action: Some("switch".to_string()),
                target: Some("session-123".to_string()),
                output_format: CliOutputFormat::Json,
            }
        );
        assert_eq!(
            parse_args(&["--output-format=json".to_string(), "doctor".to_string()])
                .expect("doctor should parse"),
            CliAction::Doctor {
                output_format: CliOutputFormat::Json,
            }
        );
        assert_eq!(
            parse_args(&["skills".to_string(), "review".to_string()]).expect("skills should parse"),
            CliAction::Skills {
                skill: Some("review".to_string()),
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&[
                "--output-format=ndjson".to_string(),
                "tasks".to_string(),
                "7".to_string()
            ])
            .expect("tasks should parse"),
            CliAction::Tasks {
                task: Some("7".to_string()),
                output_format: CliOutputFormat::Ndjson,
            }
        );
    }

    #[test]
    fn rejects_extra_direct_inspection_arguments() {
        let memory_error = parse_args(&["memory".to_string(), "extra".to_string()])
            .expect_err("memory extra args should fail");
        assert!(memory_error.contains("memory does not accept positional arguments"));

        let config_error =
            parse_args(&["config".to_string(), "env".to_string(), "hooks".to_string()])
                .expect_err("config extra args should fail");
        assert!(config_error.contains("config accepts at most one argument"));

        let remote_env_error = parse_args(&["remote-env".to_string(), "extra".to_string()])
            .expect_err("remote-env extra args should fail");
        assert!(remote_env_error.contains("remote-env does not accept positional arguments"));

        let tasks_error = parse_args(&["tasks".to_string(), "1".to_string(), "2".to_string()])
            .expect_err("tasks extra args should fail");
        assert!(tasks_error.contains("tasks accepts at most one argument"));
    }

    #[test]
    fn parses_login_and_logout_subcommands() {
        assert_eq!(
            parse_args(&["login".to_string()]).expect("login should parse"),
            CliAction::Login {
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["logout".to_string()]).expect("logout should parse"),
            CliAction::Logout {
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&["--output-format=ndjson".to_string(), "login".to_string()])
                .expect("ndjson login should parse"),
            CliAction::Login {
                output_format: CliOutputFormat::Ndjson,
            }
        );
        assert_eq!(
            parse_args(&["--output-format=json".to_string(), "logout".to_string()])
                .expect("json logout should parse"),
            CliAction::Logout {
                output_format: CliOutputFormat::Json,
            }
        );
        assert_eq!(
            parse_args(&["init".to_string()]).expect("init should parse"),
            CliAction::Init {
                output_format: CliOutputFormat::Text,
            }
        );
        assert_eq!(
            parse_args(&[
                "--output-format=json".to_string(),
                "dump-manifests".to_string()
            ])
            .expect("dump-manifests should parse"),
            CliAction::DumpManifests {
                output_format: CliOutputFormat::Json,
            }
        );
        assert_eq!(
            parse_args(&[
                "--output-format=ndjson".to_string(),
                "bootstrap-plan".to_string()
            ])
            .expect("bootstrap-plan should parse"),
            CliAction::BootstrapPlan {
                output_format: CliOutputFormat::Ndjson,
            }
        );
    }

    #[test]
    fn direct_command_structured_payloads_render_expected_shapes() {
        let version = version_payload();
        assert_eq!(version["type"], json!("version"));
        assert_eq!(version["version"], json!(VERSION));
        assert_eq!(version["content"], json!(render_version_report()));

        let bootstrap = bootstrap_plan_payload();
        assert_eq!(bootstrap["type"], json!("bootstrap_plan"));
        assert!(bootstrap["phases"]
            .as_array()
            .is_some_and(|phases| !phases.is_empty()));

        let logout = super::logout_payload();
        assert_eq!(logout["type"], json!("logout"));
        assert_eq!(logout["credentials_cleared"], json!(true));
        assert_eq!(
            logout["message"],
            json!("Simcoe AI OAuth credentials cleared."),
        );

        let config = super::inspection_payload("config", Some("section"), Some("env"), "report");
        assert_eq!(config["type"], json!("config"));
        assert_eq!(config["section"], json!("env"));
        assert_eq!(config["content"], json!("report"));

        let memory = super::inspection_payload("memory", None, None, "report");
        assert_eq!(memory["type"], json!("memory"));
        assert_eq!(memory["content"], json!("report"));
        assert!(memory
            .as_object()
            .is_some_and(|payload| !payload.contains_key("section")));
    }

    #[test]
    fn login_ndjson_records_render_expected_shapes() {
        assert_eq!(
            super::login_start_record("http://127.0.0.1:4545/callback"),
            json!({
                "type": "login",
                "event": "start",
                "message": "Starting Simcoe AI OAuth login.",
                "redirect_uri": "http://127.0.0.1:4545/callback",
            })
        );
        assert_eq!(
            super::login_browser_opened_record(),
            json!({
                "type": "login",
                "event": "browser_opened",
                "message": "Opened the authorization URL in a browser.",
            })
        );
        assert_eq!(
            super::login_browser_warning_record("xdg-open missing", "https://example.test/auth"),
            json!({
                "type": "login",
                "event": "browser_warning",
                "message": "failed to open browser automatically: xdg-open missing",
                "authorize_url": "https://example.test/auth",
            })
        );
        assert_eq!(
            super::login_complete_record(
                "http://127.0.0.1:4545/callback",
                false,
                Some("xdg-open missing"),
            ),
            json!({
                "type": "login",
                "event": "complete",
                "message": "Simcoe AI OAuth login complete.",
                "redirect_uri": "http://127.0.0.1:4545/callback",
                "browser_opened": false,
                "browser_open_error": "xdg-open missing",
            })
        );
    }

    #[test]
    fn login_rejects_single_json_output_format() {
        let args = vec!["--output-format=json".to_string(), "login".to_string()];
        let error = super::with_cli_error_context(
            super::run_login(CliOutputFormat::Json).expect_err("json login should fail"),
            1,
            Some("login"),
            None,
        );
        let payload = super::cli_error_payload(&args, error.as_ref());

        assert_eq!(payload["type"], json!("error"));
        assert_eq!(payload["exit_code"], json!(2));
        assert_eq!(payload["operation"], json!("login"));
        assert!(payload["message"]
            .as_str()
            .is_some_and(|message| message.contains("does not support --output-format json")));
    }

    #[test]
    fn infers_structured_error_output_format_from_raw_args() {
        assert_eq!(
            inferred_error_output_format(&[
                "--output-format=json".to_string(),
                "prompt".to_string(),
                "hello".to_string(),
            ]),
            CliOutputFormat::Json,
        );
        assert_eq!(
            inferred_error_output_format(&[
                "--output-format".to_string(),
                "ndjson".to_string(),
                "--resume".to_string(),
                "session.json".to_string(),
            ]),
            CliOutputFormat::Ndjson,
        );
        assert_eq!(
            inferred_error_output_format(&[
                "--output-format=unsupported".to_string(),
                "prompt".to_string(),
            ]),
            CliOutputFormat::Text,
        );
    }

    #[test]
    fn infers_structured_error_metadata_from_raw_args() {
        assert_eq!(
            inferred_error_metadata(&[
                "--resume".to_string(),
                "session.json".to_string(),
                "/status".to_string(),
            ]),
            (Some("resume".to_string()), Some("/status".to_string())),
        );
        assert_eq!(
            inferred_error_metadata(&["system-prompt".to_string()]),
            (Some("system-prompt".to_string()), None),
        );
        assert_eq!(
            inferred_error_metadata(&["hello".to_string()]),
            (Some("prompt".to_string()), None),
        );
    }

    #[test]
    fn infers_structured_error_context_for_empty_args_as_repl() {
        let context = super::inferred_error_context(&[]);

        assert_eq!(context.operation, Some("repl".to_string()));
        assert_eq!(context.model, Some(DEFAULT_MODEL.to_string()));
    }

    #[test]
    fn infers_structured_error_context_for_prompt_includes_model_and_provider() {
        let context = super::inferred_error_context(&[
            "--model".to_string(),
            DEFAULT_MODEL.to_string(),
            "--provider".to_string(),
            "openai".to_string(),
            "prompt".to_string(),
            "hello".to_string(),
        ]);

        assert_eq!(context.operation, Some("prompt".to_string()));
        assert_eq!(context.model, Some(DEFAULT_MODEL.to_string()));
        assert_eq!(context.provider, Some("openai".to_string()));
    }

    #[test]
    fn infers_structured_error_context_from_raw_prompt_args_when_parse_fails() {
        let context = super::inferred_error_context(&[
            "--output-format=unsupported".to_string(),
            "--model".to_string(),
            DEFAULT_MODEL.to_string(),
            "--provider".to_string(),
            "anthropic".to_string(),
            "prompt".to_string(),
            "hello".to_string(),
        ]);

        assert_eq!(context.operation, Some("prompt".to_string()));
        assert_eq!(context.model, Some(DEFAULT_MODEL.to_string()));
        assert_eq!(context.provider, Some("anthropic".to_string()));
    }

    #[test]
    fn structured_error_payload_includes_exit_code_help_hint_and_metadata() {
        let args = vec![
            "--output-format".to_string(),
            "json".to_string(),
            "--resume".to_string(),
            "session.json".to_string(),
            "/status".to_string(),
        ];
        let error = CliExitError::new("resume failed", 2)
            .with_operation("resume")
            .with_command("/status");
        let payload = super::cli_error_payload(&args, &error);

        assert_eq!(payload["type"], json!("error"));
        assert_eq!(payload["message"], json!("resume failed"));
        assert_eq!(payload["exit_code"], json!(2));
        assert_eq!(payload["help_hint"], json!("Run `claw --help` for usage."),);
        assert_eq!(payload["operation"], json!("resume"));
        assert_eq!(payload["command"], json!("/status"));
    }

    #[test]
    fn structured_error_payload_includes_prompt_provider_and_model_context() {
        let args = vec![
            "--output-format".to_string(),
            "json".to_string(),
            "--model".to_string(),
            DEFAULT_MODEL.to_string(),
            "--provider".to_string(),
            "ollama".to_string(),
            "prompt".to_string(),
            "hello".to_string(),
        ];
        let error = CliExitError::new("request failed", 1).with_operation("prompt");

        let payload = super::cli_error_payload(&args, &error);

        assert_eq!(payload["type"], json!("error"));
        assert_eq!(payload["operation"], json!("prompt"));
        assert_eq!(payload["model"], json!(DEFAULT_MODEL));
        assert_eq!(payload["provider"], json!("ollama"));
        assert_eq!(
            payload["transport"]["active_transport_kind"],
            json!("api-stream")
        );
        assert_eq!(
            payload["transport"]["provider_runtime"]["provider"],
            json!("ollama")
        );
        assert_eq!(
            payload["transport"]["provider_runtime"]["family"],
            json!("openai-compatible")
        );
        assert_eq!(
            payload["transport"]["capabilities"]["live_remote_transport_ready"],
            json!(false)
        );
        assert_eq!(
            payload["transport"]["capabilities"]["live_remote_transport_selected"],
            json!(false)
        );
        assert!(payload["transport"]["provider_runtime"]["delivery_mode"].is_null());
    }

    #[test]
    fn parses_resume_flag_with_slash_command() {
        let args = vec![
            "--resume".to_string(),
            "session.json".to_string(),
            "/compact".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::ResumeSession {
                session_path: PathBuf::from("session.json"),
                commands: vec!["/compact".to_string()],
                output_format: CliOutputFormat::Text,
            }
        );
    }

    #[test]
    fn parses_resume_flag_with_multiple_slash_commands() {
        let args = vec![
            "--resume".to_string(),
            "session.json".to_string(),
            "/status".to_string(),
            "/compact".to_string(),
            "/cost".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::ResumeSession {
                session_path: PathBuf::from("session.json"),
                commands: vec![
                    "/status".to_string(),
                    "/compact".to_string(),
                    "/cost".to_string(),
                ],
                output_format: CliOutputFormat::Text,
            }
        );
    }

    #[test]
    fn parses_resume_flag_with_json_output_format() {
        let args = vec![
            "--output-format=json".to_string(),
            "--resume".to_string(),
            "session.json".to_string(),
            "/status".to_string(),
        ];
        assert_eq!(
            parse_args(&args).expect("args should parse"),
            CliAction::ResumeSession {
                session_path: PathBuf::from("session.json"),
                commands: vec!["/status".to_string()],
                output_format: CliOutputFormat::Json,
            }
        );
    }

    #[test]
    fn resume_structured_output_helpers_render_expected_shapes() {
        let session_path = PathBuf::from("session.json");
        let command = build_resume_command_record(0, "/compact", Some("Compacted"), 3, true);

        assert_eq!(
            build_resume_start_record(session_path.as_path(), 5),
            json!({
                "type": "resume",
                "session_path": "session.json",
                "message": "Restored session from session.json (5 messages).",
                "initial_message_count": 5,
            })
        );
        assert_eq!(
            command,
            json!({
                "type": "resume_command",
                "index": 0,
                "command": "/compact",
                "message": "Compacted",
                "message_count": 3,
                "changed_session": true,
            })
        );
        assert_eq!(
            build_resume_summary_record(session_path.as_path(), 5, 3, 1),
            json!({
                "type": "resume_summary",
                "session_path": "session.json",
                "initial_message_count": 5,
                "final_message_count": 3,
                "command_count": 1,
            })
        );
        assert_eq!(
            build_resume_json_payload(session_path.as_path(), 5, vec![command], 3),
            json!({
                "session_path": "session.json",
                "restored_message": "Restored session from session.json (5 messages).",
                "initial_message_count": 5,
                "command_count": 1,
                "commands": [
                    {
                        "type": "resume_command",
                        "index": 0,
                        "command": "/compact",
                        "message": "Compacted",
                        "message_count": 3,
                        "changed_session": true,
                    }
                ],
                "final_message_count": 3,
            })
        );
    }

    #[test]
    fn filtered_tool_specs_respect_allowlist() {
        let allowed = ["FileReadTool", "grep_search"]
            .into_iter()
            .map(str::to_string)
            .collect();
        let filtered = filter_tool_specs(Some(&allowed));
        let names = filtered
            .into_iter()
            .map(|spec| spec.name)
            .collect::<Vec<_>>();
        assert_eq!(names, vec!["read_file", "grep_search"]);
    }

    #[test]
    fn shared_help_uses_resume_annotation_copy() {
        let help = commands::render_slash_command_help();
        assert!(help.contains("Slash commands"));
        assert!(help.contains("works with --resume SESSION.json"));
    }

    #[test]
    fn repl_help_includes_shared_commands_and_exit() {
        let help = render_repl_help();
        assert!(help.contains("REPL"));
        assert!(help.contains("/help"));
        assert!(help.contains("/status"));
        assert!(help.contains("/model [model]"));
        assert!(help.contains("/permissions [read-only|workspace-write|danger-full-access]"));
        assert!(help.contains("/clear [--confirm]"));
        assert!(help.contains("/cost"));
        assert!(help.contains("/dump-manifests"));
        assert!(help.contains("/bootstrap-plan"));
        assert!(help.contains("/login"));
        assert!(help.contains("/logout"));
        assert!(help.contains("/resume <session-path>"));
        assert!(help.contains("/system-prompt [--cwd PATH] [--date YYYY-MM-DD]"));
        assert!(help.contains("/config [env|hooks|model|provider]"));
        assert!(help.contains("/hooks [pre|post]"));
        assert!(help.contains("/mcp [server]"));
        assert!(help.contains("/memory"));
        assert!(help.contains("/agents [name]"));
        assert!(help.contains("/plugin [name]"));
        assert!(help.contains("/reload-plugins"));
        assert!(help.contains("/remote-env"));
        assert!(help.contains("/remote-setup"));
        assert!(help.contains("/tools [name]"));
        assert!(help.contains("/doctor"));
        assert!(help.contains("/skills [skill]"));
        assert!(help.contains("/tasks [id]"));
        assert!(help.contains("/review [context]"));
        assert!(help.contains("/plan [task]"));
        assert!(help.contains("/init"));
        assert!(help.contains("/diff"));
        assert!(help.contains("/version"));
        assert!(help.contains("/export [file]"));
        assert!(help.contains("/session [list|switch <session-id>]"));
        assert!(help.contains("/exit"));
    }

    #[test]
    fn resume_supported_command_list_matches_expected_surface() {
        let names = resume_supported_slash_commands()
            .into_iter()
            .map(|spec| spec.name)
            .collect::<Vec<_>>();
        assert_eq!(
            names,
            vec![
                "help",
                "status",
                "compact",
                "clear",
                "cost",
                "dump-manifests",
                "bootstrap-plan",
                "system-prompt",
                "config",
                "hooks",
                "mcp",
                "memory",
                "agents",
                "plugin",
                "reload-plugins",
                "remote-env",
                "remote-setup",
                "tools",
                "doctor",
                "skills",
                "tasks",
                "init",
                "diff",
                "version",
                "export",
                "session",
            ]
        );
    }

    fn sample_session(message_count: usize) -> runtime::Session {
        runtime::Session {
            version: 1,
            messages: (0..message_count)
                .map(|index| runtime::ConversationMessage::user_text(format!("message {index}")))
                .collect(),
        }
    }

    #[test]
    fn session_list_payload_reports_saved_and_active_sessions() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("session-list-payload");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let sessions_root = nested_cwd.join(".simcoe").join("sessions");
        let session_a_path = sessions_root.join("session-alpha.json");
        let session_b_path = sessions_root.join("session-beta.json");
        fs::create_dir_all(&sessions_root).expect("create sessions root");
        sample_session(2)
            .save_to_path(&session_a_path)
            .expect("write first session");
        sample_session(1)
            .save_to_path(&session_b_path)
            .expect("write second session");

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);
            let active = crate::session_manager::session_handle_from_path(&session_a_path);
            crate::session_manager::set_active_session_handle(&active).expect("set active session");

            let report = super::session_list_report().expect("session list report should render");
            assert!(report.contains("Sessions"));
            assert!(report.contains("session-alpha"));
            assert!(report.contains("● current"));

            let payload =
                super::session_list_payload().expect("session list payload should render");
            assert_eq!(payload["type"], json!("session"));
            assert_eq!(payload["action"], json!("list"));
            assert_eq!(payload["active_session"]["id"], json!("session-alpha"));
            assert!(payload["sessions"].as_array().is_some_and(
                |sessions: &Vec<serde_json::Value>| sessions
                    .iter()
                    .any(|session| session["id"] == json!("session-alpha")
                        && session["is_active"] == json!(true))
            ));
            assert!(payload["sessions"].as_array().is_some_and(
                |sessions: &Vec<serde_json::Value>| sessions
                    .iter()
                    .any(|session| session["id"] == json!("session-beta")
                        && session["is_active"] == json!(false))
            ));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn direct_session_switch_updates_active_session_pointer() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("session-switch-direct");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let sessions_root = nested_cwd.join(".simcoe").join("sessions");
        let session_path = sessions_root.join("session-target.json");
        fs::create_dir_all(&sessions_root).expect("create sessions root");
        sample_session(3)
            .save_to_path(&session_path)
            .expect("write target session");

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);
            let (handle, message_count) = super::switch_managed_session("session-target")
                .expect("session switch should succeed");
            let active = crate::session_manager::load_active_session_handle()
                .expect("load active session")
                .expect("active session should exist");
            assert_eq!(active.id, "session-target");
            assert_eq!(message_count, 3);

            let payload = super::session_switch_payload(&handle, message_count)
                .expect("session switch payload should render");
            assert_eq!(payload["type"], json!("session"));
            assert_eq!(payload["action"], json!("switch"));
            assert_eq!(payload["active_session"]["id"], json!("session-target"));
            assert_eq!(payload["active_session"]["message_count"], json!(3));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn direct_export_uses_active_managed_session() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("session-export-direct");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let sessions_root = nested_cwd.join(".simcoe").join("sessions");
        let session_path = sessions_root.join("session-export.json");
        fs::create_dir_all(&sessions_root).expect("create sessions root");
        sample_session(2)
            .save_to_path(&session_path)
            .expect("write export session");

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);
            let active = crate::session_manager::session_handle_from_path(&session_path);
            crate::session_manager::set_active_session_handle(&active).expect("set active session");

            let (handle, export_path, message_count) =
                super::export_active_session(Some("session-notes".to_string()))
                    .expect("direct export should succeed");
            assert_eq!(handle.id, "session-export");
            assert_eq!(message_count, 2);
            assert!(export_path.ends_with("session-notes.txt"));

            let exported = fs::read_to_string(&export_path).expect("read exported transcript");
            assert!(exported.contains("## 1. user"));
            assert!(exported.contains("message 0"));

            let payload = super::export_payload(&handle, &export_path, message_count);
            assert_eq!(payload["type"], json!("export"));
            assert_eq!(payload["session_id"], json!("session-export"));
            assert_eq!(payload["message_count"], json!(2));
            assert!(payload["export_path"]
                .as_str()
                .is_some_and(|path| path.ends_with("session-notes.txt")));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn resumed_session_command_lists_and_switches_sessions() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("session-resume-command");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let sessions_root = nested_cwd.join(".simcoe").join("sessions");
        let session_a_path = sessions_root.join("session-alpha.json");
        let session_b_path = sessions_root.join("session-beta.json");
        fs::create_dir_all(&sessions_root).expect("create sessions root");
        let session_a = sample_session(1);
        let session_b = sample_session(4);
        session_a
            .save_to_path(&session_a_path)
            .expect("write session alpha");
        session_b
            .save_to_path(&session_b_path)
            .expect("write session beta");

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let listed = run_resume_command(
                session_a_path.as_path(),
                &session_a,
                &SlashCommand::Session {
                    action: Some("list".to_string()),
                    target: None,
                },
            )
            .expect("resume session list should succeed");
            assert_eq!(listed.session_path, session_a_path);
            assert!(listed.message.as_deref().is_some_and(|message| message
                .contains("session-alpha")
                && message.contains("● current")));

            let switched = run_resume_command(
                session_a_path.as_path(),
                &session_a,
                &SlashCommand::Session {
                    action: Some("switch".to_string()),
                    target: Some("session-beta".to_string()),
                },
            )
            .expect("resume session switch should succeed");
            assert_eq!(switched.session_path, session_b_path);
            assert_eq!(switched.session.messages.len(), 4);
            assert!(switched
                .message
                .as_deref()
                .is_some_and(|message| message.contains("Session switched")
                    && message.contains("session-beta")));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    fn write_plugin_snapshots(repo_root: &std::path::Path) {
        let reference_data = repo_root.join("src/reference_data");
        let subsystems = reference_data.join("subsystems");
        fs::create_dir_all(&subsystems).expect("create snapshot dirs");
        fs::write(
            reference_data.join("commands_snapshot.json"),
            r#"[
  {"name":"plugin","source_hint":"commands/plugin/index.tsx","responsibility":"plugin index"},
  {"name":"plugin","source_hint":"commands/plugin/plugin.tsx","responsibility":"plugin flow"},
    {"name":"reload-plugins","source_hint":"commands/reload-plugins/index.ts","responsibility":"reload index"},
    {"name":"reload-plugins","source_hint":"commands/reload-plugins/reload-plugins.ts","responsibility":"reload flow"}
]"#,
        )
        .expect("write commands snapshot");
        fs::write(
            subsystems.join("plugins.json"),
            r#"{
  "archive_name": "plugins",
  "package_name": "plugins",
  "module_count": 2,
  "sample_files": ["plugins/builtinPlugins.ts", "plugins/bundled/index.ts"]
}"#,
        )
        .expect("write plugin snapshot");
    }

    fn write_remote_snapshots(repo_root: &std::path::Path) {
        let reference_data = repo_root.join("src/reference_data");
        let subsystems = reference_data.join("subsystems");
        fs::create_dir_all(&subsystems).expect("create snapshot dirs");
        fs::write(
                        reference_data.join("commands_snapshot.json"),
                        r#"[
    {"name":"remote-env","source_hint":"commands/remote-env/index.ts","responsibility":"remote env index"},
    {"name":"remote-env","source_hint":"commands/remote-env/remote-env.tsx","responsibility":"remote env flow"},
    {"name":"api","source_hint":"commands/remote-setup/api.ts","responsibility":"remote setup api"},
    {"name":"remote-setup","source_hint":"commands/remote-setup/index.ts","responsibility":"remote setup index"},
    {"name":"remote-setup","source_hint":"commands/remote-setup/remote-setup.tsx","responsibility":"remote setup flow"}
]"#,
                )
                .expect("write commands snapshot");
        fs::write(
            subsystems.join("cli.json"),
            r#"{
    "archive_name": "cli",
    "package_name": "cli",
    "module_count": 6,
    "sample_files": [
        "cli/handlers/plugins.ts",
        "cli/remoteIO.ts",
        "cli/structuredIO.ts",
        "cli/transports/HybridTransport.ts",
        "cli/transports/WebSocketTransport.ts",
        "cli/transports/transportUtils.ts"
    ]
}"#,
        )
        .expect("write cli snapshot");
        fs::write(
            subsystems.join("upstreamproxy.json"),
            r#"{
    "archive_name": "upstreamproxy",
    "package_name": "upstreamproxy",
    "module_count": 2,
    "sample_files": [
        "upstreamproxy/relay.ts",
        "upstreamproxy/upstreamproxy.ts"
    ]
}"#,
        )
        .expect("write upstreamproxy snapshot");
    }

    fn write_tools_snapshot(repo_root: &std::path::Path) {
        let reference_data = repo_root.join("src/reference_data");
        fs::create_dir_all(&reference_data).expect("create snapshot dir");
        fs::write(
            reference_data.join("tools_snapshot.json"),
            r#"[
  {"name":"BashTool","source_hint":"tools/BashTool/BashTool.tsx","responsibility":"bash tool"},
  {"name":"bashPermissions","source_hint":"tools/BashTool/bashPermissions.ts","responsibility":"bash permissions"},
  {"name":"ToolSearchTool","source_hint":"tools/ToolSearchTool/ToolSearchTool.ts","responsibility":"tool search"},
  {"name":"queryParser","source_hint":"tools/ToolSearchTool/queryParser.ts","responsibility":"query parser"}
]"#,
        )
        .expect("write tools snapshot");
    }

    fn write_doctor_settings(config_home: &std::path::Path) {
        fs::create_dir_all(config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
    "hooks": {
        "PreToolUse": ["python pre_hook.py"],
        "PostToolUse": ["python post_hook.py"]
    },
    "mcpServers": {
        "local": {
            "command": "node",
            "args": ["server.js"]
        },
        "remote": {
            "type": "http",
            "url": "https://example.test/mcp",
            "headersHelper": "helper.sh"
        }
    },
    "oauth": {
        "clientId": "simcoe-cli",
        "authorizeUrl": "https://console.test/oauth/authorize",
        "tokenUrl": "https://console.test/oauth/token",
        "scopes": ["openid", "profile"]
    },
    "provider": "simcoe",
    "model": "simcoe-sonnet-4-6",
    "permissionMode": "workspace-write",
    "sandbox": {
        "enabled": true,
        "filesystemMode": "workspace-only"
    }
}"#,
        )
        .expect("write doctor settings");
    }

    #[test]
    fn hooks_report_lists_configured_commands() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("hooks-report");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
              "hooks": {
                "PreToolUse": ["python scripts/pre_hook.py"],
                "PostToolUse": ["python scripts/post_hook.py", "./notify.sh"]
              }
            }"#,
        )
        .expect("write settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_hooks_report(None).expect("hooks report should render");
            assert!(report.contains("Hooks"));
            assert!(report.contains("Pre-tool hooks    1"));
            assert!(report.contains("Post-tool hooks   2"));
            assert!(report.contains("PreToolUse"));
            assert!(report.contains("PostToolUse"));
            assert!(report.contains("python scripts/pre_hook.py"));
            assert!(report.contains("./notify.sh"));

            let payload = super::hooks_payload(None).expect("hooks payload should render");
            assert_eq!(payload["type"], json!("hooks"));
            assert_eq!(payload["pre_tool_use_count"], json!(1));
            assert_eq!(payload["post_tool_use_count"], json!(2));
            assert_eq!(
                payload["pre_tool_use"],
                json!(["python scripts/pre_hook.py"])
            );
            assert_eq!(
                payload["post_tool_use"],
                json!(["python scripts/post_hook.py", "./notify.sh"])
            );
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn hooks_report_renders_selected_event() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("hooks-selected");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
              "hooks": {
                "PreToolUse": ["python scripts/pre_hook.py"]
              }
            }"#,
        )
        .expect("write settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report =
                render_hooks_report(Some("pre")).expect("selected hooks report should render");
            assert!(report.contains("Hooks"));
            assert!(report.contains("Event             PreToolUse"));
            assert!(report.contains("Configured        1"));
            assert!(report.contains("python scripts/pre_hook.py"));
            assert!(report.contains("exit 2 denies, other non-zero exits warn"));

            let payload =
                super::hooks_payload(Some("pre".to_string())).expect("hooks payload should render");
            assert_eq!(payload["type"], json!("hooks"));
            assert_eq!(payload["event"], json!("pre"));
            assert_eq!(payload["event_label"], json!("PreToolUse"));
            assert_eq!(payload["configured_count"], json!(1));
            assert_eq!(payload["commands"], json!(["python scripts/pre_hook.py"]));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    fn env_lock() -> &'static Mutex<()> {
        static LOCK: OnceLock<Mutex<()>> = OnceLock::new();
        LOCK.get_or_init(|| Mutex::new(()))
    }

    struct ScopedEnvVar {
        key: &'static str,
        original: Option<std::ffi::OsString>,
    }

    impl ScopedEnvVar {
        fn set(key: &'static str, value: impl AsRef<std::ffi::OsStr>) -> Self {
            let original = std::env::var_os(key);
            std::env::set_var(key, value);
            Self { key, original }
        }

        fn remove(key: &'static str) -> Self {
            let original = std::env::var_os(key);
            std::env::remove_var(key);
            Self { key, original }
        }
    }

    impl Drop for ScopedEnvVar {
        fn drop(&mut self) {
            match &self.original {
                Some(value) => std::env::set_var(self.key, value),
                None => std::env::remove_var(self.key),
            }
        }
    }

    struct ScopedCurrentDir {
        original: PathBuf,
    }

    impl ScopedCurrentDir {
        fn change_to(path: &std::path::Path) -> Self {
            let original = std::env::current_dir().expect("current dir");
            std::env::set_current_dir(path).expect("set current dir");
            Self { original }
        }
    }

    impl Drop for ScopedCurrentDir {
        fn drop(&mut self) {
            std::env::set_current_dir(&self.original).expect("restore cwd");
        }
    }

    fn temp_path(name: &str) -> PathBuf {
        let nanos = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .expect("time should be monotonic")
            .as_nanos();
        std::env::temp_dir().join(format!("claw-cli-{name}-{nanos}"))
    }

    fn detect_first_command(candidates: &[&str]) -> String {
        candidates
            .iter()
            .find(|candidate| Command::new(candidate).arg("--version").output().is_ok())
            .map(|candidate| (*candidate).to_string())
            .unwrap_or_else(|| panic!("no command found in {:?}", candidates))
    }

    fn write_tools_mcp_server_script() -> PathBuf {
        let root = temp_path("tools-mcp-server-script");
        fs::create_dir_all(&root).expect("create mcp server root");
        let script_path = root.join("tools-mcp-server.py");
        let script = [
            "#!/usr/bin/env python3",
            "import json, sys",
            "",
            "def read_message():",
            "    header = b''",
            r"    while not header.endswith(b'\r\n\r\n'):",
            "        chunk = sys.stdin.buffer.read(1)",
            "        if not chunk:",
            "            return None",
            "        header += chunk",
            "    length = 0",
            r"    for line in header.decode().split('\r\n'):",
            r"        if line.lower().startswith('content-length:'):",
            r"            length = int(line.split(':', 1)[1].strip())",
            "    payload = sys.stdin.buffer.read(length)",
            "    return json.loads(payload.decode())",
            "",
            "def send_message(message):",
            "    payload = json.dumps(message).encode()",
            r"    sys.stdout.buffer.write(f'Content-Length: {len(payload)}\r\n\r\n'.encode() + payload)",
            "    sys.stdout.buffer.flush()",
            "",
            "while True:",
            "    request = read_message()",
            "    if request is None:",
            "        break",
            "    method = request['method']",
            "    if method == 'initialize':",
            "        send_message({",
            "            'jsonrpc': '2.0',",
            "            'id': request['id'],",
            "            'result': {",
            "                'protocolVersion': request['params']['protocolVersion'],",
            "                'capabilities': {'tools': {}, 'resources': {}},",
            "                'serverInfo': {'name': 'alpha', 'version': '1.0.0'}",
            "            }",
            "        })",
            "    elif method == 'tools/list':",
            "        send_message({",
            "            'jsonrpc': '2.0',",
            "            'id': request['id'],",
            "            'result': {",
            "                'tools': [",
            "                    {",
            "                        'name': 'echo',",
            "                        'description': 'Echoes back the provided text',",
            "                        'inputSchema': {",
            "                            'type': 'object',",
            "                            'properties': {'text': {'type': 'string'}},",
            "                            'required': ['text']",
            "                        }",
            "                    }",
            "                ]",
            "            }",
            "        })",
            "    elif method == 'tools/call':",
            "        args = request['params'].get('arguments') or {}",
            "        text = args.get('text', '')",
            "        send_message({",
            "            'jsonrpc': '2.0',",
            "            'id': request['id'],",
            "            'result': {",
            "                'content': [{'type': 'text', 'text': f'echo:{text}'}],",
            "                'structuredContent': {'echoed': text, 'server': 'alpha'},",
            "                'isError': False",
            "            }",
            "        })",
            "    elif method == 'resources/list':",
            "        send_message({",
            "            'jsonrpc': '2.0',",
            "            'id': request['id'],",
            "            'result': {",
            "                'resources': [",
            "                    {",
            "                        'uri': 'file://guide.txt',",
            "                        'name': 'guide',",
            "                        'description': 'Guide file',",
            "                        'mimeType': 'text/plain'",
            "                    }",
            "                ]",
            "            }",
            "        })",
            "    elif method == 'resources/read':",
            "        uri = request['params']['uri']",
            "        send_message({",
            "            'jsonrpc': '2.0',",
            "            'id': request['id'],",
            "            'result': {",
            "                'contents': [",
            "                    {",
            "                        'uri': uri,",
            "                        'mimeType': 'text/plain',",
            "                        'text': f'contents for {uri}'",
            "                    }",
            "                ]",
            "            }",
            "        })",
            "    else:",
            "        send_message({",
            "            'jsonrpc': '2.0',",
            "            'id': request['id'],",
            "            'error': {'code': -32601, 'message': f'unknown method: {method}'},",
            "        })",
            "",
        ]
        .join("\n");
        fs::write(&script_path, script).expect("write mcp server script");
        script_path
    }

    fn spawn_http_server(response: String) -> String {
        let listener = TcpListener::bind("127.0.0.1:0").expect("bind listener");
        let address = listener.local_addr().expect("listener addr");
        thread::spawn(move || {
            let (mut stream, _) = listener.accept().expect("accept connection");
            let mut buffer = [0_u8; 8192];
            let _ = stream.read(&mut buffer).expect("read request");
            stream
                .write_all(response.as_bytes())
                .expect("write response");
        });
        format!("http://{address}")
    }

    fn http_response(status: &str, content_type: &str, body: &str) -> String {
        format!(
            "HTTP/1.1 {status}\r\ncontent-type: {content_type}\r\ncontent-length: {}\r\n\r\n{body}",
            body.len()
        )
    }

    #[test]
    fn resume_report_uses_sectioned_layout() {
        let report = format_resume_report("session.json", 14, 6);
        assert!(report.contains("Session resumed"));
        assert!(report.contains("Session file     session.json"));
        assert!(report.contains("Messages         14"));
        assert!(report.contains("Turns            6"));
    }

    #[test]
    fn compact_report_uses_structured_output() {
        let compacted = format_compact_report(8, 5, false);
        assert!(compacted.contains("Compact"));
        assert!(compacted.contains("Result           compacted"));
        assert!(compacted.contains("Messages removed 8"));
        let skipped = format_compact_report(0, 3, true);
        assert!(skipped.contains("Result           skipped"));
    }

    #[test]
    fn cost_report_uses_sectioned_layout() {
        let report = format_cost_report(runtime::TokenUsage {
            input_tokens: 20,
            output_tokens: 8,
            cache_creation_input_tokens: 3,
            cache_read_input_tokens: 1,
        });
        assert!(report.contains("Cost"));
        assert!(report.contains("Input tokens     20"));
        assert!(report.contains("Output tokens    8"));
        assert!(report.contains("Cache create     3"));
        assert!(report.contains("Cache read       1"));
        assert!(report.contains("Total tokens     32"));
    }

    #[test]
    fn permissions_report_uses_sectioned_layout() {
        let report = format_permissions_report("workspace-write");
        assert!(report.contains("Permissions"));
        assert!(report.contains("Active mode      workspace-write"));
        assert!(report.contains("Modes"));
        assert!(report.contains("read-only          ○ available Read/search tools only"));
        assert!(report.contains("workspace-write    ● current   Edit files inside the workspace"));
        assert!(report.contains("danger-full-access ○ available Unrestricted tool access"));
    }

    #[test]
    fn permissions_switch_report_is_structured() {
        let report = format_permissions_switch_report("read-only", "workspace-write");
        assert!(report.contains("Permissions updated"));
        assert!(report.contains("Result           mode switched"));
        assert!(report.contains("Previous mode    read-only"));
        assert!(report.contains("Active mode      workspace-write"));
        assert!(report.contains("Applies to       subsequent tool calls"));
    }

    #[test]
    fn init_help_mentions_direct_subcommand() {
        let mut help = Vec::new();
        print_help_to(&mut help).expect("help should render");
        let help = String::from_utf8(help).expect("help should be utf8");
        assert!(help.contains("claw init"));
        assert!(help.contains("FileReadTool"));
        assert!(help.contains("text, json, or ndjson"));
        assert!(help.contains("claw config [env|hooks|model|provider]"));
        assert!(help.contains("claw hooks [pre|post]"));
        assert!(help.contains("claw mcp [server]"));
        assert!(help.contains("claw memory"));
        assert!(help.contains("claw agents [name]"));
        assert!(help.contains("claw plugin [name]"));
        assert!(help.contains("claw reload-plugins"));
        assert!(help.contains("claw remote-env"));
        assert!(help.contains("claw remote-setup"));
        assert!(help.contains("claw tools [name]"));
        assert!(help.contains("claw doctor"));
        assert!(help.contains("claw skills [skill]"));
        assert!(help.contains("claw tasks [id]"));
        assert!(help.contains("OAuth login; supports text and ndjson output"));
        assert!(help.contains("supports text, json, and ndjson output"));
        assert!(help.contains("claw --output-format ndjson prompt"));
        assert!(help.contains("claw --output-format json --resume session.json /status /cost"));
        assert!(help.contains("claw --output-format json dump-manifests"));
        assert!(help.contains("claw --output-format json config hooks"));
        assert!(help.contains("claw --output-format ndjson mcp repo-server"));
        assert!(help.contains("claw --output-format json agents reviewer"));
        assert!(help.contains("claw --output-format json remote-env"));
        assert!(help.contains("claw --output-format ndjson login"));
        assert!(help.contains("claw --output-format json logout"));
    }

    #[test]
    fn model_report_uses_sectioned_layout() {
        let report = format_model_report("simcoe-sonnet", 12, 4);
        assert!(report.contains("Model"));
        assert!(report.contains("Current model    simcoe-sonnet"));
        assert!(report.contains("Session messages 12"));
        assert!(report.contains("Switch models with /model <name>"));
    }

    #[test]
    fn skills_report_lists_local_skills() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("skills-report");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let skill_dir = repo_root.join("skills");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&skill_dir).expect("create skill dir");
        fs::write(
            skill_dir.join("electrical-estimating.md"),
            "---\nid: electrical-estimating\ntitle: Electrical Estimating\nsummary: Structure estimate answers around scope and uncertainty.\naliases:\n  - estimate\n---\nUse this skill for structured estimate answers.\n",
        )
        .expect("write estimating skill prompt");
        fs::write(
            skill_dir.join("revit-family-reference.md"),
            "---\nid: revit-family-reference\ntitle: Revit Family Reference\nsummary: Present Revit answers with exact family and type labels.\naliases:\n  - revit\n---\nKeep entity names verbatim.\n",
        )
        .expect("write revit skill prompt");

        {
            let _codex_home_guard = ScopedEnvVar::remove("CODEX_HOME");
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_skills_report(None).expect("skills report should render");
            assert!(report.contains("Skills"));
            assert!(report.contains("Available        2"));
            assert!(report.contains("electrical-estimating"));
            assert!(report.contains("Structure estimate answers around scope and uncertainty."));
            assert!(report.contains("revit-family-reference"));
            assert!(report.contains("Present Revit answers with exact family and type labels."));

            let payload = super::skills_payload(None).expect("skills payload should render");
            assert_eq!(payload["type"], json!("skills"));
            assert_eq!(payload["available_count"], json!(2));
            assert_eq!(payload["skills"].as_array().map(Vec::len), Some(2));
            assert!(payload["skills"]
                .as_array()
                .is_some_and(|skills| skills.iter().any(|skill| {
                    skill["name"] == json!("electrical-estimating")
                        && skill["description"]
                            == json!("Structure estimate answers around scope and uncertainty.")
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn skills_report_renders_selected_skill_prompt() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("skills-selected");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let skill_dir = repo_root.join("skills");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&skill_dir).expect("create skill dir");
        fs::write(
            skill_dir.join("context-map.md"),
            "---\nid: context-map\ntitle: Context Map\nsummary: Map relevant files before editing.\naliases:\n  - map\n---\nPrompt text\n",
        )
        .expect("write skill prompt");

        {
            let _codex_home_guard = ScopedEnvVar::remove("CODEX_HOME");
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_skills_report(Some("context-map"))
                .expect("selected skill report should render");
            assert!(report.contains("Skill"));
            assert!(report.contains("Name             context-map"));
            assert!(report.contains("Description      Map relevant files before editing."));
            assert!(report.contains("Prompt text"));

            let payload = super::skills_payload(Some("context-map".to_string()))
                .expect("selected skills payload should render");
            assert_eq!(payload["type"], json!("skills"));
            assert_eq!(payload["skill"]["skill"], json!("context-map"));
            assert_eq!(
                payload["skill"]["description"],
                json!("Map relevant files before editing.")
            );
            assert!(payload["skill"]["path"]
                .as_str()
                .is_some_and(|path| path.ends_with("skills/context-map.md")));
            assert!(payload["skill"]["prompt"]
                .as_str()
                .is_some_and(|prompt| prompt.contains("Prompt text")));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn skills_report_lists_archived_bundled_skill_samples() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("skills-archived-report");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let reference_data = repo_root.join("src/reference_data");
        let subsystems_dir = reference_data.join("subsystems");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&subsystems_dir).expect("create subsystem dir");
        fs::write(reference_data.join("commands_snapshot.json"), "[]\n")
            .expect("write commands snapshot");
        fs::write(
            subsystems_dir.join("skills.json"),
            r#"{
  "archive_name": "skills",
  "package_name": "skills",
  "module_count": 6,
  "sample_files": [
    "skills/bundled/batch.ts",
    "skills/bundled/verify.ts",
    "skills/bundled/index.ts",
    "skills/bundledSkills.ts",
    "skills/loadSkillsDir.ts",
    "skills/mcpSkillBuilders.ts"
  ]
}"#,
        )
        .expect("write skills snapshot");

        {
            let _codex_home_guard = ScopedEnvVar::remove("CODEX_HOME");
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_skills_report(None).expect("skills report should render");
            assert!(report.contains("Skills"));
            assert!(report.contains("Local available  0"));
            assert!(report.contains("Archived bundled samples"));
            assert!(report.contains("verify"));
            assert!(report.contains("skills/bundled/verify.ts"));
            assert!(report.contains("Archived support modules"));
            assert!(report.contains("skills/mcpSkillBuilders.ts"));

            let payload = super::skills_payload(None).expect("skills payload should render");
            assert_eq!(payload["type"], json!("skills"));
            assert_eq!(payload["available_count"], json!(0));
            assert_eq!(payload["archived"]["bundled_skill_sample_count"], json!(2));
            assert_eq!(payload["archived"]["support_module_count"], json!(4));
            assert!(payload["archived"]["bundled_skill_samples"]
                .as_array()
                .is_some_and(|skills| skills.iter().any(|skill| {
                    skill["name"] == json!("verify")
                        && skill["source_hints"].as_array().is_some_and(|hints| {
                            hints
                                .iter()
                                .any(|hint| hint == &json!("skills/bundled/verify.ts"))
                        })
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn skills_report_renders_selected_archived_skill_surface() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("skills-archived-selected");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let reference_data = repo_root.join("src/reference_data");
        let subsystems_dir = reference_data.join("subsystems");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&subsystems_dir).expect("create subsystem dir");
        fs::write(reference_data.join("commands_snapshot.json"), "[]\n")
            .expect("write commands snapshot");
        fs::write(
            subsystems_dir.join("skills.json"),
            r#"{
  "archive_name": "skills",
  "package_name": "skills",
  "module_count": 2,
  "sample_files": [
    "skills/bundled/verify.ts",
    "skills/bundled/index.ts"
  ]
}"#,
        )
        .expect("write skills snapshot");

        {
            let _codex_home_guard = ScopedEnvVar::remove("CODEX_HOME");
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_skills_report(Some("verify"))
                .expect("selected archived skill report should render");
            assert!(report.contains("Skill"));
            assert!(report.contains("Name             verify"));
            assert!(report.contains("Rust status      inspection only"));
            assert!(report.contains("Path             skills/bundled/verify.ts"));

            let payload = super::skills_payload(Some("verify".to_string()))
                .expect("selected archived skills payload should render");
            assert_eq!(payload["type"], json!("skills"));
            assert_eq!(payload["archived_skill"]["name"], json!("verify"));
            assert_eq!(payload["archived_skill"]["archived_file_count"], json!(1));
            assert!(payload["archived_skill"]["source_hints"]
                .as_array()
                .is_some_and(|hints| hints
                    .iter()
                    .any(|hint| hint == &json!("skills/bundled/verify.ts"))));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn agents_report_lists_built_in_profiles_and_recent_tasks() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("agents-report");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let agent_store = repo_root.join(".clawd-agents");
        let manifest_path_a = agent_store.join("agent-123.json");
        let manifest_path_b = agent_store.join("agent-456.json");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&agent_store).expect("create agent store");
        fs::write(
            &manifest_path_a,
            format!(
                r#"{{
  "agentId": "agent-123",
  "name": "audit-repo",
  "description": "Audit the repo",
  "subagentType": "Explore",
  "model": "simcoe-opus-4-6",
  "status": "completed",
  "outputFile": "{}",
  "manifestFile": "{}",
  "createdAt": "2026-04-05T00:00:00Z",
  "startedAt": "2026-04-05T00:00:00Z",
  "completedAt": "2026-04-05T00:01:00Z"
}}"#,
                agent_store.join("agent-123.md").display(),
                manifest_path_a.display(),
            ),
        )
        .expect("write explore manifest");
        fs::write(
            &manifest_path_b,
            format!(
                r#"{{
  "agentId": "agent-456",
  "name": "verify-release",
  "description": "Verify the release",
  "subagentType": "Verification",
  "model": "simcoe-sonnet-4-6",
  "status": "running",
  "outputFile": "{}",
  "manifestFile": "{}",
  "createdAt": "2026-04-05T00:02:00Z",
  "startedAt": "2026-04-05T00:02:00Z"
}}"#,
                agent_store.join("agent-456.md").display(),
                manifest_path_b.display(),
            ),
        )
        .expect("write verification manifest");

        {
            let _agent_store_guard = ScopedEnvVar::set("CLAWD_AGENT_STORE", &agent_store);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_agents_report(None).expect("agents report should render");
            assert!(report.contains("Agents"));
            assert!(report.contains("Available        6"));
            assert!(report.contains("Persisted tasks  2"));
            assert!(report.contains("Explore"));
            assert!(report.contains("Read-heavy repo exploration and research sub-agent."));
            assert!(report.contains("Verification"));
            assert!(report.contains("Validation-oriented sub-agent with shell access."));
            assert!(report.contains("1 recent"));

            let payload = super::agents_payload(None).expect("agents payload should render");
            assert_eq!(payload["type"], json!("agents"));
            assert_eq!(payload["available_count"], json!(6));
            assert_eq!(payload["persisted_task_count"], json!(2));
            assert_eq!(payload["profiles"].as_array().map(Vec::len), Some(6));
            assert!(payload["profiles"]
                .as_array()
                .is_some_and(|profiles| profiles.iter().any(|profile| {
                    profile["name"] == json!("Explore")
                        && profile["tool_count"] == json!(11)
                        && profile["recent_task_count"] == json!(1)
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn agents_report_renders_selected_profile_details() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("agents-selected");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let agent_store = repo_root.join(".clawd-agents");
        let manifest_path_a = agent_store.join("agent-123.json");
        let manifest_path_b = agent_store.join("agent-999.json");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&agent_store).expect("create agent store");
        fs::write(
            &manifest_path_a,
            format!(
                r#"{{
  "agentId": "agent-123",
  "name": "audit-repo",
  "description": "Audit the repo",
  "subagentType": "Explore",
  "model": "simcoe-opus-4-6",
  "status": "completed",
  "outputFile": "{}",
  "manifestFile": "{}",
  "createdAt": "2026-04-05T00:00:00Z",
  "startedAt": "2026-04-05T00:00:00Z",
  "completedAt": "2026-04-05T00:01:00Z"
}}"#,
                agent_store.join("agent-123.md").display(),
                manifest_path_a.display(),
            ),
        )
        .expect("write completed explore manifest");
        fs::write(
            &manifest_path_b,
            format!(
                r#"{{
  "agentId": "agent-999",
  "name": "scan-docs",
  "description": "Scan docs",
  "subagentType": "Explore",
  "model": "simcoe-sonnet-4-6",
  "status": "running",
  "outputFile": "{}",
  "manifestFile": "{}",
  "createdAt": "2026-04-05T00:05:00Z",
  "startedAt": "2026-04-05T00:05:00Z"
}}"#,
                agent_store.join("agent-999.md").display(),
                manifest_path_b.display(),
            ),
        )
        .expect("write running explore manifest");

        {
            let _agent_store_guard = ScopedEnvVar::set("CLAWD_AGENT_STORE", &agent_store);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_agents_report(Some("explorer"))
                .expect("selected agents report should render");
            assert!(report.contains("Agent"));
            assert!(report.contains("Name             Explore"));
            assert!(report.contains("Aliases          explore, explorer, exploreagent"));
            assert!(report.contains("Allowed tools    11"));
            assert!(report.contains("Running          1"));
            assert!(report.contains("Completed        1"));
            assert!(report.contains("Failed           0"));
            assert!(report.contains("read_file"));
            assert!(report.contains("agent-123"));
            assert!(report.contains("agent-999"));

            let payload = super::agents_payload(Some("explorer".to_string()))
                .expect("agent payload should render");
            assert_eq!(payload["type"], json!("agents"));
            assert_eq!(payload["profile"]["name"], json!("Explore"));
            assert_eq!(
                payload["profile"]["aliases"],
                json!(["explore", "explorer", "exploreagent"])
            );
            assert_eq!(payload["task_counts"]["running"], json!(1));
            assert_eq!(payload["task_counts"]["completed"], json!(1));
            assert_eq!(payload["task_counts"]["failed"], json!(0));
            assert_eq!(payload["recent_tasks"].as_array().map(Vec::len), Some(2));
            assert!(payload["recent_tasks"].as_array().is_some_and(|tasks| tasks
                .iter()
                .any(|task| task["agentId"] == json!("agent-123"))));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn plugin_report_lists_archived_plugin_surfaces() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("plugin-report");
        let nested_cwd = repo_root.join("rust");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        write_plugin_snapshots(&repo_root);

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_plugin_report(None).expect("plugin report should render");
            assert!(report.contains("Plugin"));
            assert!(report.contains("Archive           plugins"));
            assert!(report.contains("Rust status       inspection only"));
            assert!(report.contains("Archived commands 2"));
            assert!(report.contains("plugins/builtinPlugins.ts"));
            assert!(report.contains("reload-plugins"));

            let payload = super::plugin_payload(None).expect("plugin payload should render");
            assert_eq!(payload["type"], json!("plugin"));
            assert_eq!(payload["snapshot"]["archive_name"], json!("plugins"));
            assert_eq!(payload["snapshot"]["package_name"], json!("plugins"));
            assert_eq!(payload["snapshot"]["module_count"], json!(2));
            assert_eq!(payload["snapshot"]["command_count"], json!(2));
            assert_eq!(payload["snapshot"]["module_surface_count"], json!(2));
            assert_eq!(
                payload["snapshot"]["commands"].as_array().map(Vec::len),
                Some(2)
            );
            assert_eq!(
                payload["snapshot"]["modules"].as_array().map(Vec::len),
                Some(2)
            );
            assert!(payload["snapshot"]["commands"]
                .as_array()
                .is_some_and(|surfaces| surfaces.iter().any(|surface| {
                    surface["name"] == json!("reload-plugins")
                        && surface["kind"] == json!("command")
                        && surface["archived_file_count"] == json!(2)
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn plugin_report_renders_selected_surface() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("plugin-selected");
        let nested_cwd = repo_root.join("rust");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        write_plugin_snapshots(&repo_root);

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_plugin_report(Some("reload-plugins"))
                .expect("selected plugin report should render");
            assert!(report.contains("Plugin"));
            assert!(report.contains("Name             reload-plugins"));
            assert!(report.contains("Kind             command"));
            assert!(report.contains("Rust status      inspection only"));
            assert!(report.contains("Archived files   2"));
            assert!(report.contains("commands/reload-plugins/index.ts"));
            assert!(report.contains("commands/reload-plugins/reload-plugins.ts"));

            let payload = super::plugin_payload(Some("reload-plugins".to_string()))
                .expect("selected plugin payload should render");
            assert_eq!(payload["type"], json!("plugin"));
            assert_eq!(payload["surface"]["name"], json!("reload-plugins"));
            assert_eq!(payload["surface"]["kind"], json!("command"));
            assert_eq!(payload["surface"]["archived_file_count"], json!(2));
            assert!(payload["surface"]["source_hints"]
                .as_array()
                .is_some_and(|hints| hints
                    .iter()
                    .any(|hint| { hint == &json!("commands/reload-plugins/reload-plugins.ts") })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn reload_plugins_report_is_inspection_only() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("reload-plugins-report");
        let nested_cwd = repo_root.join("rust");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        write_plugin_snapshots(&repo_root);

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_reload_plugins_report().expect("reload report should render");
            assert!(report.contains("Reload plugins"));
            assert!(report.contains("Rust status      inspection only"));
            assert!(report
                .contains("Runtime support  no plugin loader or live reload flow is implemented"));
            assert!(report.contains("Archived files   2"));
            assert!(report.contains("Archived modules 2"));
            assert!(report.contains("commands/reload-plugins/index.ts"));
            assert!(report.contains("commands/reload-plugins/reload-plugins.ts"));

            let payload = super::reload_plugins_payload().expect("reload payload should render");
            assert_eq!(payload["type"], json!("reload_plugins"));
            assert_eq!(payload["runtime_support"], json!("inspection only"));
            assert_eq!(payload["snapshot"]["archive_name"], json!("plugins"));
            assert_eq!(payload["snapshot"]["module_count"], json!(2));
            assert_eq!(
                payload["snapshot"]["surface"]["name"],
                json!("reload-plugins")
            );
            assert_eq!(
                payload["snapshot"]["surface"]["archived_file_count"],
                json!(2)
            );
            assert!(payload["snapshot"]["surface"]["source_hints"]
                .as_array()
                .is_some_and(|hints| hints
                    .iter()
                    .any(|hint| { hint == &json!("commands/reload-plugins/reload-plugins.ts") })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn remote_env_report_reads_bootstrap_state() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let root = temp_path("remote-env-report");
        let token_path = root.join("session_token");
        let ca_bundle = root.join("ca-bundle.crt");
        fs::create_dir_all(&root).expect("create temp dir");
        fs::write(&token_path, "secret-token\n").expect("write token");
        fs::write(&ca_bundle, "ca").expect("write ca bundle");

        {
            let _remote_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE", "1");
            let _session_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE_SESSION_ID", "session-123");
            let _base_guard = ScopedEnvVar::set("SIMCOE_AI_BASE_URL", "https://remote.test");
            let _proxy_guard = ScopedEnvVar::set("CCR_UPSTREAM_PROXY_ENABLED", "true");
            let _token_path_guard = ScopedEnvVar::set("CCR_SESSION_TOKEN_PATH", &token_path);
            let _ca_bundle_guard = ScopedEnvVar::set("CCR_CA_BUNDLE_PATH", &ca_bundle);

            let report = render_remote_env_report().expect("remote env report should render");
            assert!(report.contains("Remote env"));
            assert!(report.contains("Rust status      bootstrap foundation only"));
            assert!(report.contains("Remote enabled   yes"));
            assert!(report.contains("Session id       session-123"));
            assert!(report.contains("Base URL         https://remote.test"));
            assert!(report.contains("Upstream proxy   yes"));
            assert!(report.contains("Proxy ready      yes"));
            assert!(report.contains("WS path ready    yes"));
            assert!(report.contains("Live blocker     adapter-not-ported ("));
            assert!(report.contains("Token present    yes"));
            assert!(report.contains("WS target        wss://remote.test/v1/code/upstreamproxy/ws"));
            assert!(report.contains("WS probe         skipped"));
            assert!(report.contains("Missing          <none>"));

            let payload = super::remote_env_payload().expect("remote env payload should render");
            assert_eq!(payload["type"], json!("remote_env"));
            assert_eq!(payload["transport"]["kind"], json!("upstream-proxy"));
            assert_eq!(
                payload["transport"]["active_transport_kind"],
                json!("api-stream")
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport"],
                json!(false)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_kind"],
                json!("upstream-proxy-websocket")
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_ready"],
                json!(false)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_path_ready"],
                json!(true)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_selected"],
                json!(false)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_blocker_kind"],
                json!("adapter-not-ported")
            );
            assert!(
                payload["transport"]["capabilities"]["live_remote_transport_blocker_detail"]
                    .as_str()
                    .is_some_and(|detail| detail.contains("not ported in Rust"))
            );
            assert_eq!(payload["transport"]["bootstrap"]["ready"], json!(true));
            assert_eq!(
                payload["transport"]["bootstrap"]["websocket_probe"]["status"],
                json!("skipped")
            );
            assert_eq!(
                payload["transport"]["bootstrap"]["token_present"],
                json!(true)
            );
            assert_eq!(payload["transport"]["bootstrap"]["missing"], json!([]));
            assert!(payload["content"]
                .as_str()
                .is_some_and(|content| content.contains("Remote env")));
        }

        let _ = fs::remove_dir_all(root);
    }

    #[test]
    fn remote_setup_report_combines_runtime_and_archive_state() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("remote-setup-report");
        let nested_cwd = repo_root.join("rust");
        let token_path = repo_root.join("session_token");
        let ca_bundle = repo_root.join("ca-bundle.crt");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::write(&token_path, "secret-token\n").expect("write token");
        fs::write(&ca_bundle, "ca").expect("write ca bundle");
        write_remote_snapshots(&repo_root);

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);
            let _remote_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE", "1");
            let _session_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE_SESSION_ID", "session-setup");
            let _base_guard = ScopedEnvVar::set("SIMCOE_AI_BASE_URL", "https://remote.test");
            let _proxy_guard = ScopedEnvVar::set("CCR_UPSTREAM_PROXY_ENABLED", "true");
            let _token_path_guard = ScopedEnvVar::set("CCR_SESSION_TOKEN_PATH", &token_path);
            let _ca_bundle_guard = ScopedEnvVar::set("CCR_CA_BUNDLE_PATH", &ca_bundle);

            let report = render_remote_setup_report().expect("remote setup report should render");
            assert!(report.contains("Remote setup"));
            assert!(report.contains("Rust status       bootstrap foundation only"));
            assert!(report.contains("Proxy ready       yes"));
            assert!(report.contains("WS path ready     yes"));
            assert!(report.contains("Live blocker      adapter-not-ported ("));
            assert!(report.contains("Remote enabled    yes"));
            assert!(report.contains("Session id        session-setup"));
            assert!(report.contains("Archive           cli"));
            assert!(report.contains("Proxy archive     upstreamproxy"));
            assert!(report.contains("Archived files    3"));
            assert!(report.contains("Transport files   5"));
            assert!(report.contains("Proxy files       2"));
            assert!(report.contains("Summary           remote setup flow"));
            assert!(report.contains("WS probe          skipped"));
            assert!(report.contains("Missing           <none>"));
            assert!(report.contains("commands/remote-setup/api.ts"));
            assert!(report.contains("cli/structuredIO.ts"));
            assert!(report.contains("upstreamproxy/relay.ts"));

            let payload =
                super::remote_setup_payload().expect("remote setup payload should render");
            assert_eq!(payload["type"], json!("remote_setup"));
            assert_eq!(payload["transport"]["kind"], json!("upstream-proxy"));
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_kind"],
                json!("upstream-proxy-websocket")
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_ready"],
                json!(false)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_path_ready"],
                json!(true)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_selected"],
                json!(false)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_blocker_kind"],
                json!("adapter-not-ported")
            );
            assert!(
                payload["transport"]["capabilities"]["live_remote_transport_blocker_detail"]
                    .as_str()
                    .is_some_and(|detail| detail.contains("not ported in Rust"))
            );
            assert_eq!(
                payload["transport"]["bootstrap"]["websocket_probe"]["status"],
                json!("skipped")
            );
            assert_eq!(payload["snapshot"]["archive_name"], json!("cli"));
            assert_eq!(payload["snapshot"]["package_name"], json!("cli"));
            assert_eq!(payload["snapshot"]["module_count"], json!(6));
            assert_eq!(
                payload["snapshot"]["upstream_proxy"]["archive_name"],
                json!("upstreamproxy")
            );
            assert_eq!(
                payload["snapshot"]["upstream_proxy"]["package_name"],
                json!("upstreamproxy")
            );
            assert_eq!(
                payload["snapshot"]["upstream_proxy"]["module_count"],
                json!(2)
            );
            assert_eq!(
                payload["snapshot"]["upstream_proxy"]["files"],
                json!(["upstreamproxy/relay.ts", "upstreamproxy/upstreamproxy.ts",])
            );
            assert_eq!(
                payload["snapshot"]["transport_files"],
                json!([
                    "cli/remoteIO.ts",
                    "cli/structuredIO.ts",
                    "cli/transports/HybridTransport.ts",
                    "cli/transports/WebSocketTransport.ts",
                    "cli/transports/transportUtils.ts",
                ])
            );
            assert_eq!(
                payload["snapshot"]["command"]["name"],
                json!("remote-setup")
            );
            assert_eq!(
                payload["snapshot"]["command"]["summary"],
                json!("remote setup flow")
            );
            assert_eq!(
                payload["snapshot"]["command"]["archived_file_count"],
                json!(3)
            );
            assert!(payload["content"]
                .as_str()
                .is_some_and(|content| content.contains("Remote setup")));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn remote_env_payload_reports_failed_websocket_probe_when_requested() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let root = temp_path("remote-env-probe-failure");
        let token_path = root.join("session_token");
        let ca_bundle = root.join("ca-bundle.crt");
        fs::create_dir_all(&root).expect("create temp dir");
        fs::write(&token_path, "secret-token\n").expect("write token");
        fs::write(&ca_bundle, "ca").expect("write ca bundle");
        let unused_port = std::net::TcpListener::bind("127.0.0.1:0")
            .expect("bind port")
            .local_addr()
            .expect("local addr")
            .port();

        {
            let _remote_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE", "1");
            let _session_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE_SESSION_ID", "session-123");
            let _base_guard = ScopedEnvVar::set(
                "SIMCOE_AI_BASE_URL",
                &format!("http://127.0.0.1:{unused_port}"),
            );
            let _proxy_guard = ScopedEnvVar::set("CCR_UPSTREAM_PROXY_ENABLED", "true");
            let _token_path_guard = ScopedEnvVar::set("CCR_SESSION_TOKEN_PATH", &token_path);
            let _ca_bundle_guard = ScopedEnvVar::set("CCR_CA_BUNDLE_PATH", &ca_bundle);
            let _probe_guard = ScopedEnvVar::set("CCR_UPSTREAM_PROXY_PROBE", "1");

            let report = render_remote_env_report().expect("remote env report should render");
            assert!(report.contains("WS path ready    no"));
            assert!(report.contains("Live blocker     probe-failed ("));
            assert!(report.contains("WS probe         failed"));

            let payload = super::remote_env_payload().expect("remote env payload should render");
            assert_eq!(
                payload["transport"]["bootstrap"]["websocket_probe"]["status"],
                json!("failed")
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_ready"],
                json!(false)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_path_ready"],
                json!(false)
            );
            assert_eq!(
                payload["transport"]["capabilities"]["live_remote_transport_blocker_kind"],
                json!("probe-failed")
            );
            assert!(
                payload["transport"]["capabilities"]["live_remote_transport_blocker_detail"]
                    .as_str()
                    .is_some_and(|detail| detail.contains("failed to connect"))
            );
        }

        let _ = fs::remove_dir_all(root);
    }

    #[test]
    fn tools_report_lists_rust_and_archived_tools() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("tools-report");
        let nested_cwd = repo_root.join("rust");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        write_tools_snapshot(&repo_root);

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_tools_report(None).expect("tools report should render");
            assert!(report.contains("Tools"));
            assert!(report.contains(&format!("Rust tools         {}", mvp_tool_specs().len())));
            assert!(report.contains("Archived families  2"));
            assert!(report.contains("Archived files     4"));
            assert!(report.contains("Rust registry"));
            assert!(report.contains("bash"));
            assert!(report.contains("read_file (FileReadTool)"));
            assert!(report.contains("ToolSearchTool"));

            let payload = super::tools_payload(None).expect("tools payload should render");
            assert_eq!(payload["type"], json!("tools"));
            assert_eq!(
                payload["rust_registry"]["tool_count"],
                json!(mvp_tool_specs().len())
            );
            assert_eq!(payload["rust_registry"]["dynamic_mcp_tool_count"], json!(0));
            assert_eq!(payload["rust_registry"]["pending_mcp_servers"], json!([]));
            assert_eq!(
                payload["rust_registry"]["pending_mcp_server_details"],
                json!([])
            );
            assert_eq!(payload["archived_snapshot"]["available"], json!(true));
            assert_eq!(payload["archived_snapshot"]["family_count"], json!(2));
            assert_eq!(
                payload["archived_snapshot"]["archived_file_count"],
                json!(4)
            );
            assert_eq!(
                payload["archived_snapshot"]["families"]
                    .as_array()
                    .map(Vec::len),
                Some(2)
            );
            assert!(payload["rust_registry"]["tools"]
                .as_array()
                .is_some_and(|tools| tools.iter().any(|tool| {
                    tool["name"] == json!("bash")
                        && tool["required_permission"] == json!("danger-full-access")
                })));
            assert!(payload["rust_registry"]["tools"]
                .as_array()
                .is_some_and(|tools| tools.iter().any(|tool| {
                    tool["name"] == json!("read_file")
                        && tool["aliases"] == json!(["FileReadTool"])
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn tools_report_renders_selected_tool_and_archived_family() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("tools-selected");
        let nested_cwd = repo_root.join("rust");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        write_tools_snapshot(&repo_root);

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report =
                render_tools_report(Some("bash")).expect("selected tools report should render");
            assert!(report.contains("Tool"));
            assert!(report.contains("Name             bash"));
            assert!(report.contains("Source           rust tool registry"));
            assert!(report.contains("Required mode    danger-full-access"));
            assert!(report.contains("dangerouslyDisableSandbox"));
            assert!(report.contains("Archived TS family"));
            assert!(report.contains("Name             BashTool"));
            assert!(report.contains("Archived files   2"));
            assert!(report.contains("tools/BashTool/BashTool.tsx"));

            let payload = super::tools_payload(Some("bash".to_string()))
                .expect("selected tools payload should render");
            assert_eq!(payload["type"], json!("tools"));
            assert_eq!(payload["requested"], json!("bash"));
            assert_eq!(payload["rust_tool"]["name"], json!("bash"));
            assert_eq!(
                payload["rust_tool"]["required_permission"],
                json!("danger-full-access")
            );
            assert_eq!(payload["archived_family"]["name"], json!("BashTool"));
            assert_eq!(payload["archived_family"]["archived_file_count"], json!(2));
            assert!(payload["archived_family"]["source_hints"]
                .as_array()
                .is_some_and(|hints| hints
                    .iter()
                    .any(|hint| hint == &json!("tools/BashTool/BashTool.tsx"))));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn tools_report_matches_live_rust_tool_aliases() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("tools-selected-alias");
        fs::create_dir_all(&cwd).expect("create cwd");

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&cwd);

            let report = render_tools_report(Some("FileReadTool"))
                .expect("selected alias tools report should render");
            assert!(report.contains("Tool"));
            assert!(report.contains("Name             read_file"));
            assert!(report.contains("Source           rust tool registry"));
            assert!(report.contains("Aliases          FileReadTool"));

            let payload = super::tools_payload(Some("FileReadTool".to_string()))
                .expect("selected alias tools payload should render");
            assert_eq!(payload["requested"], json!("FileReadTool"));
            assert_eq!(payload["rust_tool"]["name"], json!("read_file"));
            assert_eq!(payload["rust_tool"]["aliases"], json!(["FileReadTool"]));
        }

        let _ = fs::remove_dir_all(cwd);
    }

    #[test]
    fn tools_report_renders_mcp_auth_output_schema() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("tools-mcp-auth-selected");
        let nested_cwd = repo_root.join("rust");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_tools_report(Some("McpAuthTool"))
                .expect("selected MCP auth tools report should render");
            assert!(report.contains("Tool"));
            assert!(report.contains("Name             McpAuthTool"));
            assert!(report.contains("Output schema"));
            assert!(report.contains("transportCounts"));
            assert!(report.contains("attentionServers"));

            let payload = super::tools_payload(Some("McpAuthTool".to_string()))
                .expect("selected MCP auth tools payload should render");
            assert_eq!(payload["type"], json!("tools"));
            assert_eq!(payload["requested"], json!("McpAuthTool"));
            assert_eq!(payload["rust_tool"]["name"], json!("McpAuthTool"));
            assert_eq!(
                payload["rust_tool"]["output_schema"]["type"],
                json!("object")
            );
            assert_eq!(
                payload["rust_tool"]["output_schema"]["properties"]["transportCounts"]["type"],
                json!("object")
            );
            assert_eq!(
                payload["rust_tool"]["output_schema"]["properties"]["attentionServers"]["type"],
                json!("array")
            );
            assert_eq!(
                payload["rust_tool"]["output_schema"]["properties"]["attentionServers"]["items"]
                    ["properties"]["reasonKind"]["type"],
                json!("string")
            );
            assert_eq!(
                payload["rust_tool"]["output_schema"]["properties"]["servers"]["items"]
                    ["properties"]["reasonKind"]["type"],
                json!("string")
            );
            assert!(payload["archived_family"].is_null());
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn tools_report_renders_mcp_tool_family_output_schemas() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("tools-mcp-family-selected");
        let nested_cwd = repo_root.join("rust");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let mcp_tool_report = render_tools_report(Some("MCPTool"))
                .expect("selected MCP tool report should render");
            assert!(mcp_tool_report.contains("Name             MCPTool"));
            assert!(mcp_tool_report.contains("Output schema"));
            assert!(mcp_tool_report.contains("list_tools"));
            assert!(mcp_tool_report.contains("call_tool"));

            let mcp_tool_payload = super::tools_payload(Some("MCPTool".to_string()))
                .expect("selected MCP tool payload should render");
            assert_eq!(mcp_tool_payload["rust_tool"]["name"], json!("MCPTool"));
            assert!(mcp_tool_payload["rust_tool"]["output_schema"]["oneOf"]
                .as_array()
                .is_some_and(|variants| variants.len() == 2));

            let list_resources_report = render_tools_report(Some("ListMcpResourcesTool"))
                .expect("selected list resources report should render");
            assert!(list_resources_report.contains("Name             ListMcpResourcesTool"));
            assert!(list_resources_report.contains("resourceCount"));
            assert!(list_resources_report.contains("nextCursor"));

            let list_resources_payload =
                super::tools_payload(Some("ListMcpResourcesTool".to_string()))
                    .expect("selected list resources payload should render");
            assert_eq!(
                list_resources_payload["rust_tool"]["output_schema"]["properties"]["resourceCount"]
                    ["type"],
                json!("integer")
            );
            assert_eq!(
                list_resources_payload["rust_tool"]["output_schema"]["properties"]["resources"]
                    ["type"],
                json!("array")
            );

            let read_resource_report = render_tools_report(Some("ReadMcpResourceTool"))
                .expect("selected read resource report should render");
            assert!(read_resource_report.contains("Name             ReadMcpResourceTool"));
            assert!(read_resource_report.contains("contentCount"));
            assert!(read_resource_report.contains("mimeType"));

            let read_resource_payload =
                super::tools_payload(Some("ReadMcpResourceTool".to_string()))
                    .expect("selected read resource payload should render");
            assert_eq!(
                read_resource_payload["rust_tool"]["output_schema"]["properties"]["contentCount"]
                    ["type"],
                json!("integer")
            );
            assert_eq!(
                read_resource_payload["rust_tool"]["output_schema"]["properties"]["contents"]
                    ["type"],
                json!("array")
            );
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn tools_report_renders_tool_search_output_schema() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("tools-tool-search-selected");
        let nested_cwd = repo_root.join("rust");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");

        {
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_tools_report(Some("ToolSearch"))
                .expect("selected ToolSearch report should render");
            assert!(report.contains("Name             ToolSearch"));
            assert!(report.contains("Output schema"));
            assert!(report.contains("match_details"));
            assert!(report.contains("aliases"));
            assert!(report.contains("pending_mcp_server_details"));
            assert!(report.contains("reason_kind"));

            let payload = super::tools_payload(Some("ToolSearch".to_string()))
                .expect("selected ToolSearch payload should render");
            assert_eq!(payload["type"], json!("tools"));
            assert_eq!(payload["requested"], json!("ToolSearch"));
            assert_eq!(payload["rust_tool"]["name"], json!("ToolSearch"));
            assert_eq!(
                payload["rust_tool"]["output_schema"]["properties"]["match_details"]["type"],
                json!("array")
            );
            assert_eq!(
                payload["rust_tool"]["output_schema"]["properties"]["match_details"]["items"]
                    ["properties"]["aliases"]["type"],
                json!("array")
            );
            assert_eq!(
                payload["rust_tool"]["output_schema"]["properties"]["pending_mcp_server_details"]
                    ["items"]["properties"]["reason_kind"]["type"],
                json!("string")
            );
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn tools_report_lists_dynamic_mcp_tools_and_renders_selected_dynamic_tool() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("tools-dynamic-mcp-selected");
        let nested_cwd = repo_root.join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        let script_path = write_tools_mcp_server_script();
        let python = detect_first_command(&["python3", "python"]);
        fs::write(
            config_home.join("settings.json"),
            serde_json::to_string_pretty(&json!({
                "mcpServers": {
                    "vendor": {
                        "command": python,
                        "args": [script_path.to_string_lossy().into_owned()]
                    },
                    "remote": {
                        "type": "http",
                        "url": "https://example.test/mcp",
                        "headersHelper": "helper.sh"
                    }
                }
            }))
            .expect("serialize dynamic MCP settings"),
        )
        .expect("write dynamic MCP settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_tools_report(None).expect("tools report should render");
            assert!(report.contains("Dynamic MCP tools"));
            assert!(report.contains("mcp__vendor__echo"));
            assert!(report.contains("Pending MCP discovery"));
            assert!(report.contains("remote"));
            assert!(report.contains("unsupported-runtime"));
            assert!(report.contains("headersHelper"));

            let payload = super::tools_payload(None).expect("tools payload should render");
            assert_eq!(payload["type"], json!("tools"));
            assert_eq!(payload["rust_registry"]["dynamic_mcp_tool_count"], json!(1));
            assert_eq!(
                payload["rust_registry"]["pending_mcp_servers"],
                json!(["remote"])
            );
            assert!(payload["rust_registry"]["pending_mcp_server_details"]
                .as_array()
                .is_some_and(|entries| entries.iter().any(|entry| {
                    entry["server"] == json!("remote")
                        && entry["reason_kind"] == json!("unsupported-runtime")
                        && entry["detail"]
                            .as_str()
                            .is_some_and(|detail| detail.contains("headersHelper"))
                })));
            assert!(payload["rust_registry"]["tools"]
                .as_array()
                .is_some_and(|tools| tools.iter().any(|tool| {
                    tool["name"] == json!("mcp__vendor__echo")
                        && tool["source"] == json!("dynamic-mcp")
                        && tool["required_permission"] == json!("danger-full-access")
                })));

            let selected = render_tools_report(Some("mcp__vendor__echo"))
                .expect("selected dynamic tool report should render");
            assert!(selected.contains("Tool"));
            assert!(selected.contains("Name             mcp__vendor__echo"));
            assert!(selected.contains("Source           dynamic MCP tool"));
            assert!(selected.contains("qualifiedToolName"));

            let selected_payload = super::tools_payload(Some("mcp__vendor__echo".to_string()))
                .expect("selected dynamic tool payload should render");
            assert_eq!(selected_payload["requested"], json!("mcp__vendor__echo"));
            assert_eq!(
                selected_payload["rust_tool"]["name"],
                json!("mcp__vendor__echo")
            );
            assert_eq!(
                selected_payload["rust_tool"]["source"],
                json!("dynamic-mcp")
            );
            assert_eq!(
                selected_payload["rust_tool"]["output_schema"]["properties"]["qualifiedToolName"]
                    ["type"],
                json!("string")
            );
            assert!(selected_payload["archived_family"].is_null());
        }

        let _ = fs::remove_dir_all(repo_root);
        let _ = fs::remove_dir_all(script_path.parent().expect("script parent"));
    }

    #[test]
    fn doctor_report_summarizes_runtime_health() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("doctor-report");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        write_doctor_settings(&config_home);
        fs::write(
            config_home.join("credentials.json"),
            r#"{
  "oauth": {
    "accessToken": "token-value",
    "refreshToken": "refresh-value",
    "expiresAt": 4102444800,
    "scopes": ["openid", "profile"]
  }
}"#,
        )
        .expect("write oauth credentials");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_doctor_report().expect("doctor report should render");
            assert!(report.contains("Doctor"));
            assert!(report.contains("Status            ok"));
            assert!(report.contains("Provider          simcoe"));
            assert!(report.contains("Permission mode   workspace-write"));
            assert!(report.contains("OAuth config      yes"));
            assert!(report.contains("Stored creds      yes"));
            assert!(report.contains("Refresh token     yes"));
            assert!(report.contains("MCP servers       2"));
            assert!(report.contains("MCP transports    http=1, stdio=1"));
            assert!(report.contains("MCP executable    1"));
            assert!(report.contains("MCP blocked       1"));
            assert!(report.contains("MCP statuses      ready=1, unsupported-transport=1"));
            assert!(report.contains("MCP blockers      remote (http, unsupported-runtime)"));
            assert!(report.contains("MCP attention     remote (unsupported-runtime)"));
            assert!(report.contains("Pre hooks         1"));
            assert!(report.contains("Post hooks        1"));
            assert!(report.contains("Filesystem mode   workspace-only"));
            assert!(report.contains("Live blocker      disabled ("));
            assert!(report.contains("no instruction files discovered"));
            assert!(report.contains(
                "MCP server `remote` (http) is configured but not executable by the Rust runtime"
            ));

            let payload = super::doctor_payload().expect("doctor payload should render");
            assert_eq!(payload["type"], json!("doctor"));
            assert_eq!(payload["config"]["status"], json!("ok"));
            assert_eq!(payload["config"]["provider"], json!("simcoe"));
            assert_eq!(
                payload["config"]["permission_mode"],
                json!("workspace-write")
            );
            assert_eq!(payload["auth"]["oauth_configured"], json!(true));
            assert_eq!(payload["auth"]["stored_credentials_status"], json!("yes"));
            assert_eq!(payload["auth"]["refresh_token_present"], json!(true));
            assert_eq!(payload["auth"]["scopes"], json!(["openid", "profile"]));
            assert_eq!(payload["hooks"]["pre_count"], json!(1));
            assert_eq!(payload["hooks"]["post_count"], json!(1));
            assert_eq!(payload["remote"]["proxy_ready"], json!(false));
            assert_eq!(payload["remote"]["ws_path_ready"], json!(false));
            assert_eq!(payload["remote"]["live_blocker_kind"], json!("disabled"));
            assert!(payload["remote"]["live_blocker_detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("SIMCOE_AI_REMOTE disabled")));
            assert_eq!(payload["mcp"]["server_count"], json!(2));
            assert_eq!(payload["mcp"]["supported_execution_count"], json!(1));
            assert_eq!(payload["mcp"]["unsupported_execution_count"], json!(1));
            assert_eq!(payload["mcp"]["transport_counts"]["stdio"], json!(1));
            assert_eq!(payload["mcp"]["transport_counts"]["http"], json!(1));
            assert_eq!(payload["mcp"]["status_counts"]["ready"], json!(1));
            assert_eq!(
                payload["mcp"]["status_counts"]["unsupported-transport"],
                json!(1)
            );
            assert!(payload["mcp"]["unsupported_servers"]
                .as_array()
                .is_some_and(|servers| servers.iter().any(|server| {
                    server["name"] == json!("remote")
                        && server["transport"] == json!("http")
                        && server["reason_kind"] == json!("unsupported-runtime")
                        && server["detail"]
                            .as_str()
                            .is_some_and(|detail| detail.contains("headersHelper"))
                        && server["remediation_hint"]
                            .as_str()
                            .is_some_and(|hint| hint.contains("Remove headersHelper"))
                })));
            assert!(payload["mcp"]["attention_servers"]
                .as_array()
                .is_some_and(|servers| servers.iter().any(|server| {
                    server["name"] == json!("remote")
                        && server["status"] == json!("unsupported-transport")
                        && server["reason_kind"] == json!("unsupported-runtime")
                        && server["detail"]
                            .as_str()
                            .is_some_and(|detail| detail.contains("headersHelper"))
                        && server["remediation_hint"]
                            .as_str()
                            .is_some_and(|hint| hint.contains("Remove headersHelper"))
                })));
            assert_eq!(
                payload["config"]["sandbox"]["filesystem_mode"],
                json!("workspace-only")
            );
            assert!(payload["issues"].as_array().is_some_and(|issues| issues
                .iter()
                .any(|issue| issue == &json!("no instruction files discovered"))));
            assert!(payload["issues"]
                .as_array()
                .is_some_and(|issues| issues.iter().any(|issue| {
                    issue.as_str().is_some_and(|text| {
                        text.contains("MCP server `remote` (http) is configured but not executable")
                    })
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn doctor_report_surfaces_mcp_auth_attention() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("doctor-mcp-auth");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
    "mcpServers": {
        "local": {
            "command": "node",
            "args": ["server.js"]
        },
        "remote-auth": {
            "type": "http",
            "url": "https://example.test/mcp",
            "oauth": {
                "clientId": "mcp-client"
            }
        }
    },
    "model": "simcoe-sonnet-4-6",
    "permissionMode": "workspace-write"
}"#,
        )
        .expect("write doctor auth settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_doctor_report().expect("doctor report should render");
            assert!(report.contains("MCP executable    2"));
            assert!(report.contains("MCP blocked       0"));
            assert!(report.contains("MCP statuses      ready=1, user-auth-required=1"));
            assert!(report.contains("MCP attention     remote-auth (auth-required)"));
            assert!(report.contains(
                "MCP server `remote-auth` (http) requires stored OAuth credentials before execution"
            ));
            assert!(report.contains("; hint: Save MCP OAuth credentials with McpAuthTool action"));

            let payload = super::doctor_payload().expect("doctor payload should render");
            assert_eq!(payload["mcp"]["server_count"], json!(2));
            assert_eq!(payload["mcp"]["supported_execution_count"], json!(2));
            assert_eq!(payload["mcp"]["unsupported_execution_count"], json!(0));
            assert_eq!(payload["mcp"]["status_counts"]["ready"], json!(1));
            assert_eq!(
                payload["mcp"]["status_counts"]["user-auth-required"],
                json!(1)
            );
            assert!(payload["mcp"]["attention_servers"]
                .as_array()
                .is_some_and(|servers| servers.iter().any(|server| {
                    server["name"] == json!("remote-auth")
                        && server["status"] == json!("user-auth-required")
                        && server["reason_kind"] == json!("auth-required")
                        && server["detail"]
                            .as_str()
                            .is_some_and(|detail| detail.contains("McpAuthTool action `save`"))
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn doctor_report_handles_invalid_config() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("doctor-invalid-config");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(config_home.join("settings.json"), "[]\n").expect("write invalid settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_doctor_report().expect("doctor report should still render");
            assert!(report.contains("Doctor"));
            assert!(report.contains("Status            error"));
            assert!(report.contains("config load failed"));
            assert!(report.contains("Stored creds      no"));

            let payload = super::doctor_payload().expect("doctor payload should render");
            assert_eq!(payload["type"], json!("doctor"));
            assert_eq!(payload["config"]["status"], json!("error"));
            assert_eq!(payload["config"]["loaded_file_count"], json!(0));
            assert_eq!(payload["auth"]["stored_credentials_status"], json!("no"));
            assert!(payload["issues"]
                .as_array()
                .is_some_and(|issues| issues.iter().any(|issue| {
                    issue
                        .as_str()
                        .is_some_and(|text| text.contains("config load failed"))
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn doctor_report_surfaces_failed_remote_websocket_probe() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("doctor-remote-websocket-probe");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        let session_token_path = repo_root.join("session-token.txt");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        write_doctor_settings(&config_home);
        fs::write(&session_token_path, "probe-token").expect("write session token");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _remote_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE", "1");
            let _session_id_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE_SESSION_ID", "session-123");
            let _base_url_guard = ScopedEnvVar::set("SIMCOE_AI_BASE_URL", "http://127.0.0.1:9");
            let _proxy_enabled_guard = ScopedEnvVar::set("CCR_UPSTREAM_PROXY_ENABLED", "1");
            let _token_path_guard =
                ScopedEnvVar::set("CCR_SESSION_TOKEN_PATH", &session_token_path);
            let _probe_guard = ScopedEnvVar::set("CCR_UPSTREAM_PROXY_PROBE", "1");
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_doctor_report().expect("doctor report should render");
            assert!(report.contains("Proxy ready       yes"));
            assert!(report.contains("WS path ready     no"));
            assert!(report.contains("Live blocker      probe-failed ("));
            assert!(report.contains("WS probe          failed ("));
            assert!(report.contains("remote websocket probe failed:"));

            let payload = super::doctor_payload().expect("doctor payload should render");
            assert_eq!(payload["remote"]["proxy_ready"], json!(true));
            assert_eq!(payload["remote"]["ws_path_ready"], json!(false));
            assert_eq!(
                payload["remote"]["live_blocker_kind"],
                json!("probe-failed")
            );
            assert!(payload["remote"]["live_blocker_detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("failed to connect")));
            assert_eq!(
                payload["remote"]["websocket_probe"]["requested"],
                json!(true)
            );
            assert_eq!(
                payload["remote"]["websocket_probe"]["attempted"],
                json!(true)
            );
            assert_eq!(
                payload["remote"]["websocket_probe"]["reachable"],
                json!(false)
            );
            assert_eq!(
                payload["remote"]["websocket_probe"]["status"],
                json!("failed")
            );
            assert!(payload["issues"]
                .as_array()
                .is_some_and(|issues| issues.iter().any(|issue| {
                    issue
                        .as_str()
                        .is_some_and(|text| text.starts_with("remote websocket probe failed:"))
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn doctor_report_surfaces_unported_remote_adapter_blocker() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("doctor-remote-adapter-blocker");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        let session_token_path = repo_root.join("session-token.txt");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        write_doctor_settings(&config_home);
        fs::write(&session_token_path, "adapter-token").expect("write session token");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _remote_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE", "1");
            let _session_id_guard = ScopedEnvVar::set("SIMCOE_AI_REMOTE_SESSION_ID", "session-456");
            let _base_url_guard = ScopedEnvVar::set("SIMCOE_AI_BASE_URL", "https://remote.test");
            let _proxy_enabled_guard = ScopedEnvVar::set("CCR_UPSTREAM_PROXY_ENABLED", "1");
            let _token_path_guard =
                ScopedEnvVar::set("CCR_SESSION_TOKEN_PATH", &session_token_path);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_doctor_report().expect("doctor report should render");
            assert!(report.contains("Proxy ready       yes"));
            assert!(report.contains("WS path ready     yes"));
            assert!(report.contains("Live blocker      adapter-not-ported ("));
            assert!(report.contains("remote live transport blocked:"));

            let payload = super::doctor_payload().expect("doctor payload should render");
            assert_eq!(payload["remote"]["proxy_ready"], json!(true));
            assert_eq!(payload["remote"]["ws_path_ready"], json!(true));
            assert_eq!(
                payload["remote"]["live_blocker_kind"],
                json!("adapter-not-ported")
            );
            assert!(payload["remote"]["live_blocker_detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("not ported in Rust")));
            assert!(payload["issues"]
                .as_array()
                .is_some_and(|issues| issues.iter().any(|issue| {
                    issue.as_str().is_some_and(|text| {
                        text.starts_with("remote live transport blocked:")
                            && text.contains("not ported in Rust")
                    })
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn tasks_report_lists_persisted_agent_tasks() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("tasks-report");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let agent_store = repo_root.join(".clawd-agents");
        let output_path_a = agent_store.join("agent-123.md");
        let manifest_path_a = agent_store.join("agent-123.json");
        let output_path_b = agent_store.join("agent-456.md");
        let manifest_path_b = agent_store.join("agent-456.json");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&agent_store).expect("create agent store");
        fs::write(
            &output_path_a,
            "# Agent Task\n\n## Result\n\n- status: completed\n",
        )
        .expect("write completed output");
        fs::write(
            &output_path_b,
            "# Agent Task\n\n## Result\n\n- status: running\n",
        )
        .expect("write running output");
        fs::write(
            &manifest_path_a,
            format!(
                r#"{{
  "agentId": "agent-123",
  "name": "audit-repo",
  "description": "Audit the repo",
  "subagentType": "Explore",
  "model": "simcoe-opus-4-6",
  "status": "completed",
  "outputFile": "{}",
  "manifestFile": "{}",
  "createdAt": "2026-04-05T00:00:00Z",
  "startedAt": "2026-04-05T00:00:00Z",
  "completedAt": "2026-04-05T00:01:00Z"
}}"#,
                output_path_a.display(),
                manifest_path_a.display(),
            ),
        )
        .expect("write completed manifest");
        fs::write(
            &manifest_path_b,
            format!(
                r#"{{
  "agentId": "agent-456",
  "name": "verify-release",
  "description": "Verify the release",
  "subagentType": "Verification",
  "model": "simcoe-sonnet-4-6",
  "status": "running",
  "outputFile": "{}",
  "manifestFile": "{}",
  "createdAt": "2026-04-05T00:02:00Z",
  "startedAt": "2026-04-05T00:02:00Z"
}}"#,
                output_path_b.display(),
                manifest_path_b.display(),
            ),
        )
        .expect("write running manifest");

        {
            let _agent_store_guard = ScopedEnvVar::set("CLAWD_AGENT_STORE", &agent_store);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_tasks_report(None).expect("tasks report should render");
            assert!(report.contains("Tasks"));
            assert!(report.contains("Persisted tasks   2"));
            assert!(report.contains("Running          1"));
            assert!(report.contains("Completed        1"));
            assert!(report.contains("audit-repo"));
            assert!(report.contains("verify-release"));
            assert!(report.contains("agent-123"));
            assert!(report.contains("agent-456"));

            let payload = super::tasks_payload(None).expect("tasks payload should render");
            assert_eq!(payload["type"], json!("tasks"));
            assert_eq!(payload["task_counts"]["persisted"], json!(2));
            assert_eq!(payload["task_counts"]["running"], json!(1));
            assert_eq!(payload["task_counts"]["completed"], json!(1));
            assert_eq!(payload["task_counts"]["failed"], json!(0));
            assert_eq!(payload["tasks"].as_array().map(Vec::len), Some(2));
            assert!(payload["tasks"].as_array().is_some_and(|tasks| tasks
                .iter()
                .any(|task| task["agentId"] == json!("agent-123"))));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn tasks_report_renders_selected_agent_task() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("tasks-selected");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let agent_store = repo_root.join(".clawd-agents");
        let output_path = agent_store.join("agent-789.md");
        let manifest_path = agent_store.join("agent-789.json");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&agent_store).expect("create agent store");
        fs::write(
            &output_path,
            "# Agent Task\n\n## Result\n\n- status: failed\n\n### Error\n\nnetwork timeout\n",
        )
        .expect("write task output");
        fs::write(
            &manifest_path,
            format!(
                r#"{{
  "agentId": "agent-789",
  "name": "ship-audit",
  "description": "Ship audit",
  "subagentType": "Explore",
  "model": "simcoe-opus-4-6",
  "status": "failed",
  "outputFile": "{}",
  "manifestFile": "{}",
  "createdAt": "2026-04-05T01:00:00Z",
  "startedAt": "2026-04-05T01:00:00Z",
  "completedAt": "2026-04-05T01:02:00Z",
  "error": "network timeout"
}}"#,
                output_path.display(),
                manifest_path.display(),
            ),
        )
        .expect("write task manifest");

        {
            let _agent_store_guard = ScopedEnvVar::set("CLAWD_AGENT_STORE", &agent_store);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report =
                render_tasks_report(Some("agent-789")).expect("selected task report should render");
            assert!(report.contains("Task"));
            assert!(report.contains("Id               agent-789"));
            assert!(report.contains("Name             ship-audit"));
            assert!(report.contains("Status           failed"));
            assert!(report.contains("Type             Explore"));
            assert!(report.contains("Error            network timeout"));
            assert!(report.contains("# Agent Task"));
            assert!(report.contains("network timeout"));

            let payload = super::tasks_payload(Some("agent-789".to_string()))
                .expect("task payload should render");
            assert_eq!(payload["type"], json!("tasks"));
            assert_eq!(payload["task"]["agentId"], json!("agent-789"));
            assert_eq!(payload["task"]["status"], json!("failed"));
            assert_eq!(payload["task"]["subagentType"], json!("Explore"));
            assert_eq!(payload["task"]["error"], json!("network timeout"));
            assert!(payload["output"]
                .as_str()
                .is_some_and(|output| output.contains("network timeout")));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn mcp_report_lists_configured_servers() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("mcp-report");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
                            "mcpServers": {
                                "stdio-server": {
                                    "command": "uvx",
                                    "args": ["mcp-server"]
                                },
                                "remote-server": {
                                    "type": "http",
                                    "url": "https://example.test/mcp"
                                },
                                "proxy-server": {
                                    "type": "simcoeai-proxy",
                                    "url": "https://api.anthropic.com/v2/ccr-sessions/1?mcp_url=wss%3A%2F%2Fvendor.example%2Fmcp",
                                    "id": "proxy-123"
                                }
                            }
                        }"#,
        )
        .expect("write settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_mcp_report(None).expect("mcp report should render");
            assert!(report.contains("MCP"));
            assert!(report.contains("Configured servers 3"));
            assert!(report.contains("Transports        http=1, simcoe-ai-proxy=1, stdio=1"));
            assert!(report.contains("Executable now    2"));
            assert!(report.contains("Blocked now       1"));
            assert!(report.contains("Status counts     ready=2, unsupported-transport=1"));
            assert!(report
                .contains("Blockers          proxy-server (simcoe-ai-proxy, unsupported-runtime)"));
            assert!(report.contains("Attention         proxy-server (unsupported-runtime)"));
            assert!(report.contains("stdio-server"));
            assert!(report.contains("remote-server"));
            assert!(report.contains("proxy-server"));
            assert!(report.contains("https://example.test/mcp"));

            let payload = super::mcp_payload(None).expect("mcp payload should render");
            let servers = payload["servers"]
                .as_array()
                .expect("servers should be an array");
            assert_eq!(payload["type"], json!("mcp"));
            assert_eq!(payload["server_count"], json!(3));
            assert_eq!(payload["configured_server_count"], json!(3));
            assert_eq!(payload["supported_execution_count"], json!(2));
            assert_eq!(payload["unsupported_execution_count"], json!(1));
            assert_eq!(payload["transport_counts"]["http"], json!(1));
            assert_eq!(payload["transport_counts"]["simcoe-ai-proxy"], json!(1));
            assert_eq!(payload["transport_counts"]["stdio"], json!(1));
            assert_eq!(payload["status_counts"]["ready"], json!(2));
            assert_eq!(payload["status_counts"]["unsupported-transport"], json!(1));
            assert_eq!(servers.len(), 3);
            assert!(payload["unsupported_servers"]
                .as_array()
                .is_some_and(|servers| servers.iter().any(|server| {
                    server["name"] == json!("proxy-server")
                        && server["transport"] == json!("simcoe-ai-proxy")
                        && server["reason_kind"] == json!("unsupported-runtime")
                        && server["detail"].as_str().is_some_and(|detail| {
                            detail.contains("proxy `proxy-123` targets `wss://vendor.example/mcp`")
                        })
                        && server["remediation_hint"].as_str().is_some_and(|hint| {
                            hint.contains("proxy-backed server inspection-only")
                        })
                })));
            assert!(payload["attention_servers"]
                .as_array()
                .is_some_and(|servers| servers.iter().any(|server| {
                    server["name"] == json!("proxy-server")
                        && server["status"] == json!("unsupported-transport")
                        && server["reason_kind"] == json!("unsupported-runtime")
                        && server["detail"].as_str().is_some_and(|detail| {
                            detail.contains("proxy `proxy-123` targets `wss://vendor.example/mcp`")
                        })
                        && server["remediation_hint"].as_str().is_some_and(|hint| {
                            hint.contains("proxy-backed server inspection-only")
                        })
                })));
            assert!(servers.iter().any(|server| {
                server["name"] == json!("stdio-server")
                    && server["transport"] == json!("stdio")
                    && server["supported_execution"] == json!(true)
                    && server["details"]["command"] == json!("uvx")
            }));
            assert!(servers.iter().any(|server| {
                server["name"] == json!("remote-server")
                    && server["transport"] == json!("http")
                    && server["supported_execution"] == json!(true)
                    && server["target"] == json!("https://example.test/mcp")
            }));
            assert!(servers.iter().any(|server| {
                server["name"] == json!("proxy-server")
                    && server["transport"] == json!("simcoe-ai-proxy")
                    && server["supported_execution"] == json!(false)
                    && server["execution_detail"].as_str().is_some_and(|detail| {
                        detail.contains("proxy `proxy-123` targets `wss://vendor.example/mcp`")
                    })
            }));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn mcp_report_renders_selected_server_details() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("mcp-selected");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
                            "mcpServers": {
                                "remote-server": {
                                    "type": "http",
                                    "url": "https://example.test/mcp",
                                    "headers": {"Authorization": "Bearer token"},
                                    "headersHelper": "helper.sh",
                                    "oauth": {"clientId": "mcp-client"}
                                }
                            }
                        }"#,
        )
        .expect("write settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_mcp_report(Some("remote-server"))
                .expect("selected mcp report should render");
            assert!(report.contains("MCP server"));
            assert!(report.contains("Name              remote-server"));
            assert!(report.contains("Transport         http"));
            assert!(report.contains("Status            unsupported-transport"));
            assert!(report.contains("Reason kind       unsupported-runtime"));
            assert!(report.contains("Executable        no"));
            assert!(report.contains("User auth         yes"));
            assert!(report.contains("Stored creds      no"));
            assert!(report.contains(
                "http transport with headersHelper is not executed by the Rust MCP runtime yet"
            ));
            assert!(report.contains("Target            https://example.test/mcp"));
            assert!(report.contains("Auth              oauth"));
            assert!(report.contains("Headers           1"));
            assert!(report.contains("Headers helper    helper.sh"));

            let payload = super::mcp_payload(Some("remote-server".to_string()))
                .expect("selected mcp payload should render");
            assert_eq!(payload["type"], json!("mcp"));
            assert_eq!(payload["server"]["name"], json!("remote-server"));
            assert_eq!(payload["server"]["transport"], json!("http"));
            assert_eq!(payload["server"]["supported_execution"], json!(false));
            assert_eq!(
                payload["server"]["execution_detail"],
                json!(
                    "http transport with headersHelper is not executed by the Rust MCP runtime yet"
                )
            );
            assert_eq!(
                payload["server"]["runtime"]["status"],
                json!("unsupported-transport")
            );
            assert_eq!(
                payload["server"]["runtime"]["reason_kind"],
                json!("unsupported-runtime")
            );
            assert_eq!(payload["server"]["runtime"]["auth_kind"], json!("oauth"));
            assert_eq!(
                payload["server"]["runtime"]["requires_user_auth"],
                json!(true)
            );
            assert_eq!(
                payload["server"]["runtime"]["stored_credentials"],
                json!(false)
            );
            assert_eq!(
                payload["server"]["runtime"]["detail"],
                json!(
                    "http transport with headersHelper is not executed by the Rust MCP runtime yet"
                )
            );
            assert_eq!(
                payload["server"]["details"]["target"],
                json!("https://example.test/mcp")
            );
            assert_eq!(payload["server"]["details"]["auth"], json!("oauth"));
            assert_eq!(payload["server"]["details"]["headers_count"], json!(1));
            assert_eq!(
                payload["server"]["details"]["headers_helper"],
                json!("helper.sh")
            );
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn mcp_report_renders_oauth_auth_required_status() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("mcp-auth-required");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
                            "mcpServers": {
                                "oauth-server": {
                                    "type": "http",
                                    "url": "https://example.test/mcp",
                                    "oauth": {
                                        "clientId": "mcp-client",
                                        "callbackPort": 4545,
                                        "authServerMetadataUrl": "https://issuer.example/.well-known/oauth-authorization-server",
                                        "xaa": true
                                    }
                                }
                            }
                        }"#,
        )
        .expect("write settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_mcp_report(Some("oauth-server"))
                .expect("selected oauth mcp report should render");
            assert!(report.contains("Status            user-auth-required"));
            assert!(report.contains("Reason kind       auth-required"));
            assert!(report.contains("Executable        yes"));
            assert!(report.contains("User auth         yes"));
            assert!(report.contains("Stored creds      no"));
            assert!(report.contains("Client id         mcp-client"));
            assert!(report.contains("Callback port     4545"));
            assert!(report.contains(
                "Metadata URL      https://issuer.example/.well-known/oauth-authorization-server"
            ));
            assert!(report.contains("XAA               yes"));
            assert!(report.contains(
                "stored OAuth credentials are required before this server can be executed"
            ));
            assert!(report
                .contains("Hint              Save MCP OAuth credentials with McpAuthTool action"));

            let payload = super::mcp_payload(Some("oauth-server".to_string()))
                .expect("selected oauth mcp payload should render");
            assert_eq!(payload["server"]["supported_execution"], json!(true));
            assert_eq!(payload["server"]["execution_detail"], json!(null));
            assert_eq!(
                payload["server"]["runtime"]["status"],
                json!("user-auth-required")
            );
            assert_eq!(
                payload["server"]["runtime"]["reason_kind"],
                json!("auth-required")
            );
            assert_eq!(payload["server"]["runtime"]["auth_kind"], json!("oauth"));
            assert_eq!(
                payload["server"]["runtime"]["requires_user_auth"],
                json!(true)
            );
            assert_eq!(
                payload["server"]["runtime"]["stored_credentials"],
                json!(false)
            );
            assert_eq!(
                payload["server"]["runtime"]["client_id"],
                json!("mcp-client")
            );
            assert_eq!(payload["server"]["runtime"]["callback_port"], json!(4545));
            assert_eq!(
                payload["server"]["runtime"]["auth_server_metadata_url"],
                json!("https://issuer.example/.well-known/oauth-authorization-server")
            );
            assert_eq!(payload["server"]["runtime"]["xaa"], json!(true));
            assert!(payload["server"]["runtime"]["detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("McpAuthTool action `save`")));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn mcp_report_renders_expired_oauth_status() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("mcp-expired");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
                            "mcpServers": {
                                "expired-server": {
                                    "type": "http",
                                    "url": "https://example.test/mcp",
                                    "oauth": {
                                        "clientId": "mcp-client",
                                        "callbackPort": 4545,
                                        "authServerMetadataUrl": "https://issuer.example/.well-known/oauth-authorization-server",
                                        "xaa": true
                                    }
                                }
                            }
                        }"#,
        )
        .expect("write settings");

        let server_key = mcp_credentials_key(
            "expired-server",
            &ScopedMcpServerConfig {
                scope: ConfigSource::User,
                config: McpServerConfig::Http(McpRemoteServerConfig {
                    url: "https://example.test/mcp".to_string(),
                    headers: std::collections::BTreeMap::new(),
                    headers_helper: None,
                    oauth: Some(McpOAuthConfig {
                        client_id: Some("mcp-client".to_string()),
                        callback_port: Some(4545),
                        auth_server_metadata_url: Some(
                            "https://issuer.example/.well-known/oauth-authorization-server"
                                .to_string(),
                        ),
                        xaa: Some(true),
                    }),
                }),
            },
        );
        fs::write(
            config_home.join("credentials.json"),
            serde_json::to_string_pretty(&json!({
                "mcp": {
                    server_key: {
                        "accessToken": "expired-token",
                        "expiresAt": 1,
                        "scopes": ["mcp:read"]
                    }
                }
            }))
            .expect("serialize expired credentials"),
        )
        .expect("write expired credentials");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_mcp_report(Some("expired-server"))
                .expect("selected expired mcp report should render");
            assert!(report.contains("Status            expired"));
            assert!(report.contains("Reason kind       expired-credentials"));
            assert!(report.contains("Executable        yes"));
            assert!(report.contains("Stored creds      yes"));
            assert!(report.contains("Refresh token     no"));
            assert!(report.contains("Expiry            expired at 1"));
            assert!(report.contains("Scopes            mcp:read"));
            assert!(report.contains(
                "stored OAuth access token is expired and no refresh token is available"
            ));
            assert!(report.contains(
                "Hint              Re-authenticate and save fresh MCP OAuth credentials with McpAuthTool action"
            ));

            let payload = super::mcp_payload(Some("expired-server".to_string()))
                .expect("selected expired mcp payload should render");
            assert_eq!(payload["server"]["supported_execution"], json!(true));
            assert_eq!(payload["server"]["execution_detail"], json!(null));
            assert_eq!(payload["server"]["runtime"]["status"], json!("expired"));
            assert_eq!(
                payload["server"]["runtime"]["reason_kind"],
                json!("expired-credentials")
            );
            assert_eq!(
                payload["server"]["runtime"]["stored_credentials"],
                json!(true)
            );
            assert_eq!(
                payload["server"]["runtime"]["refresh_token_present"],
                json!(false)
            );
            assert_eq!(payload["server"]["runtime"]["expires_at"], json!(1));
            assert_eq!(payload["server"]["runtime"]["scopes"], json!(["mcp:read"]));
            assert!(payload["server"]["runtime"]["detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("expired and no refresh token")));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn mcp_report_renders_proxy_execution_blocker_details() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("mcp-proxy-selected");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
                            "mcpServers": {
                                "proxy-server": {
                                    "type": "simcoeai-proxy",
                                    "url": "https://api.anthropic.com/v2/ccr-sessions/1?mcp_url=wss%3A%2F%2Fvendor.example%2Fmcp",
                                    "id": "proxy-123"
                                }
                            }
                        }"#,
        )
        .expect("write settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_mcp_report(Some("proxy-server"))
                .expect("selected proxy mcp report should render");
            assert!(report.contains("Transport         simcoe-ai-proxy"));
            assert!(report.contains("Executable        no"));
            assert!(report.contains("Proxy id          proxy-123"));
            assert!(report.contains("proxy `proxy-123` targets `wss://vendor.example/mcp`"));
            assert!(report.contains("SessionsWebSocket.ts"));
            assert!(
                report.contains("Hint              Keep this proxy-backed server inspection-only")
            );

            let payload = super::mcp_payload(Some("proxy-server".to_string()))
                .expect("selected proxy mcp payload should render");
            assert_eq!(payload["server"]["transport"], json!("simcoe-ai-proxy"));
            assert_eq!(payload["server"]["supported_execution"], json!(false));
            assert_eq!(payload["server"]["details"]["proxy_id"], json!("proxy-123"));
            assert!(payload["server"]["execution_detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("sdkMessageAdapter.ts")));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn doctor_report_surfaces_expired_mcp_auth_attention() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("doctor-mcp-expired");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
    "mcpServers": {
        "local": {
            "command": "node",
            "args": ["server.js"]
        },
        "remote-expired": {
            "type": "http",
            "url": "https://example.test/mcp",
            "oauth": {
                "clientId": "mcp-client",
                "callbackPort": 4545,
                "authServerMetadataUrl": "https://issuer.example/.well-known/oauth-authorization-server",
                "xaa": true
            }
        }
    },
    "model": "simcoe-sonnet-4-6",
    "permissionMode": "workspace-write"
}"#,
        )
        .expect("write doctor expired settings");

        let server_key = mcp_credentials_key(
            "remote-expired",
            &ScopedMcpServerConfig {
                scope: ConfigSource::User,
                config: McpServerConfig::Http(McpRemoteServerConfig {
                    url: "https://example.test/mcp".to_string(),
                    headers: std::collections::BTreeMap::new(),
                    headers_helper: None,
                    oauth: Some(McpOAuthConfig {
                        client_id: Some("mcp-client".to_string()),
                        callback_port: Some(4545),
                        auth_server_metadata_url: Some(
                            "https://issuer.example/.well-known/oauth-authorization-server"
                                .to_string(),
                        ),
                        xaa: Some(true),
                    }),
                }),
            },
        );
        fs::write(
            config_home.join("credentials.json"),
            serde_json::to_string_pretty(&json!({
                "mcp": {
                    server_key: {
                        "accessToken": "expired-token",
                        "expiresAt": 1,
                        "scopes": ["mcp:read"]
                    }
                }
            }))
            .expect("serialize expired doctor credentials"),
        )
        .expect("write expired doctor credentials");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report = render_doctor_report().expect("doctor report should render");
            assert!(report.contains("MCP executable    2"));
            assert!(report.contains("MCP blocked       0"));
            assert!(report.contains("MCP statuses      expired=1, ready=1"));
            assert!(report.contains("MCP attention     remote-expired (expired-credentials)"));
            assert!(report.contains(
                "MCP server `remote-expired` (http) has expired stored OAuth credentials"
            ));
            assert!(report.contains("; hint: Re-authenticate and save fresh MCP OAuth credentials with McpAuthTool action"));

            let payload = super::doctor_payload().expect("doctor payload should render");
            assert_eq!(payload["mcp"]["server_count"], json!(2));
            assert_eq!(payload["mcp"]["supported_execution_count"], json!(2));
            assert_eq!(payload["mcp"]["unsupported_execution_count"], json!(0));
            assert_eq!(payload["mcp"]["status_counts"]["expired"], json!(1));
            assert_eq!(payload["mcp"]["status_counts"]["ready"], json!(1));
            assert!(payload["mcp"]["attention_servers"]
                .as_array()
                .is_some_and(|servers| servers.iter().any(|server| {
                    server["name"] == json!("remote-expired")
                        && server["status"] == json!("expired")
                        && server["reason_kind"] == json!("expired-credentials")
                        && server["detail"]
                            .as_str()
                            .is_some_and(|detail| detail.contains("expired and no refresh token"))
                })));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn runtime_client_suppresses_stream_rendering_when_output_disabled() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let sse = concat!(
            "event: message_start\n",
            "data: {\"type\":\"message_start\",\"message\":{\"id\":\"msg_stream\",\"type\":\"message\",\"role\":\"assistant\",\"content\":[],\"model\":\"simcoe-opus-4-6\",\"stop_reason\":null,\"stop_sequence\":null,\"usage\":{\"input_tokens\":3,\"output_tokens\":0}}}\n\n",
            "event: content_block_start\n",
            "data: {\"type\":\"content_block_start\",\"index\":0,\"content_block\":{\"type\":\"text\",\"text\":\"Checking repo-local skills\"}}\n\n",
            "event: content_block_stop\n",
            "data: {\"type\":\"content_block_stop\",\"index\":0}\n\n",
            "event: content_block_start\n",
            "data: {\"type\":\"content_block_start\",\"index\":1,\"content_block\":{\"type\":\"tool_use\",\"id\":\"toolu_1\",\"name\":\"read_file\",\"input\":{}}}\n\n",
            "event: content_block_delta\n",
            "data: {\"type\":\"content_block_delta\",\"index\":1,\"delta\":{\"type\":\"input_json_delta\",\"partial_json\":\"{\\\"path\\\":\\\"Cargo.toml\\\"}\"}}\n\n",
            "event: content_block_stop\n",
            "data: {\"type\":\"content_block_stop\",\"index\":1}\n\n",
            "event: message_delta\n",
            "data: {\"type\":\"message_delta\",\"delta\":{\"stop_reason\":\"tool_use\",\"stop_sequence\":null},\"usage\":{\"input_tokens\":3,\"output_tokens\":1}}\n\n",
            "event: message_stop\n",
            "data: {\"type\":\"message_stop\"}\n\n",
            "data: [DONE]\n\n"
        );
        let base_url = spawn_http_server(http_response("200 OK", "text/event-stream", sse));

        {
            let _base_url_guard = ScopedEnvVar::set("SIMCOE_AI_BASE_URL", &base_url);
            let _api_key_guard = ScopedEnvVar::set("SIMCOE_AI_API_KEY", "test-key");
            let _auth_token_guard = ScopedEnvVar::remove("SIMCOE_AI_AUTH_TOKEN");

            let mut client =
                SimcoeRuntimeClient::new(DEFAULT_MODEL.to_string(), true, false, None, None)
                    .expect("runtime client");
            let mut out = Vec::new();
            let events = client
                .stream_with_writer(
                    ApiRequest {
                        system_prompt: Vec::new(),
                        messages: vec![ConversationMessage::user_text("Inspect Cargo.toml")],
                    },
                    &mut out,
                )
                .expect("stream request should succeed");

            assert!(out.is_empty());
            assert!(events.iter().any(|event| matches!(
                event,
                AssistantEvent::TextDelta(text) if text == "Checking repo-local skills"
            )));
            assert!(events.iter().any(|event| matches!(
                event,
                AssistantEvent::ToolUse { name, input, .. }
                    if name == "read_file" && input == "{\"path\":\"Cargo.toml\"}"
            )));
        }
    }

    fn live_smoke_request(token: &str) -> ApiRequest {
        ApiRequest {
            system_prompt: Vec::new(),
            messages: vec![ConversationMessage::user_text(format!(
                "Reply with exactly {token} and no other text."
            ))],
        }
    }

    fn live_smoke_text(events: &[AssistantEvent]) -> String {
        events
            .iter()
            .filter_map(|event| match event {
                AssistantEvent::TextDelta(text) => Some(text.as_str()),
                _ => None,
            })
            .collect::<String>()
    }

    fn should_run_live_provider_smoke(flag: &str, required_env: &[&str]) -> bool {
        if std::env::var_os(flag).is_none() {
            eprintln!("skipping live smoke test because {flag} is not set");
            return false;
        }

        for key in required_env {
            if std::env::var_os(key).is_none() {
                eprintln!("skipping live smoke test because {key} is not set");
                return false;
            }
        }

        true
    }

    fn run_live_provider_smoke(provider: RuntimeProvider, model_env: &str, default_model: &str) {
        let token = format!("SMOKE_OK_{}", provider.as_str().to_ascii_uppercase());
        let model = std::env::var(model_env).unwrap_or_else(|_| default_model.to_string());
        let mut client =
            SimcoeRuntimeClient::new_with_provider(model, provider, false, false, None, None)
                .expect("live runtime client should initialize");
        let mut out = Vec::new();
        let events = client
            .stream_with_writer(live_smoke_request(&token), &mut out)
            .expect("live provider request should succeed");
        let text = live_smoke_text(&events);

        assert!(out.is_empty());
        assert!(
            text.to_ascii_uppercase().contains(&token),
            "expected live provider response to include {token}, got {text:?}"
        );
        assert!(events
            .iter()
            .any(|event| matches!(event, AssistantEvent::MessageStop)));
        assert!(client.last_delivery_mode().is_some());
    }

    #[test]
    #[ignore = "requires live provider credentials and network"]
    fn live_anthropic_provider_smoke_test() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        if !should_run_live_provider_smoke("CLAW_LIVE_ANTHROPIC_SMOKE", &["ANTHROPIC_API_KEY"]) {
            return;
        }

        run_live_provider_smoke(
            RuntimeProvider::Anthropic,
            "CLAW_LIVE_ANTHROPIC_MODEL",
            "claude-3-5-haiku-latest",
        );
    }

    #[test]
    #[ignore = "requires live provider credentials and network"]
    fn live_openai_provider_smoke_test() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        if !should_run_live_provider_smoke("CLAW_LIVE_OPENAI_SMOKE", &["OPENAI_API_KEY"]) {
            return;
        }

        run_live_provider_smoke(
            RuntimeProvider::OpenAi,
            "CLAW_LIVE_OPENAI_MODEL",
            "gpt-4o-mini",
        );
    }

    #[test]
    #[ignore = "requires live provider credentials and network"]
    fn live_ollama_provider_smoke_test() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        if !should_run_live_provider_smoke("CLAW_LIVE_OLLAMA_SMOKE", &[]) {
            return;
        }

        run_live_provider_smoke(
            RuntimeProvider::Ollama,
            "CLAW_LIVE_OLLAMA_MODEL",
            "llama3.2",
        );
    }

    #[test]
    fn tool_executor_suppresses_rendering_when_output_disabled() {
        let mut executor = CliToolExecutor::new(None, false);
        let mut out = Vec::new();
        let output = executor
            .execute_with_writer("StructuredOutput", r#"{"ok":true}"#, &mut out)
            .expect("tool execution should succeed");

        assert!(out.is_empty());
        let payload = serde_json::from_str::<serde_json::Value>(&output).expect("valid json");
        assert_eq!(payload["structured_output"], json!({"ok": true}));
    }

    #[test]
    fn tool_executor_allows_archived_alias_when_canonical_tool_is_allowed() {
        let path = temp_path("cli-tool-executor-allowed-alias.txt");
        std::fs::write(&path, "alias executor").expect("write input file");

        let mut executor = CliToolExecutor::new(
            Some(BTreeSet::from([String::from("read_file")])),
            false,
        );
        let mut out = Vec::new();
        let output = executor
            .execute_with_writer(
                "FileReadTool",
                &format!(r#"{{"path":"{}"}}"#, path.display()),
                &mut out,
            )
            .expect("archived alias should be allowed when canonical tool is enabled");

        assert!(out.is_empty());
        let payload = serde_json::from_str::<serde_json::Value>(&output).expect("valid json");
        assert_eq!(payload["file"]["filePath"], json!(path.display().to_string()));
        assert_eq!(payload["file"]["content"], json!("alias executor"));

        let _ = std::fs::remove_file(path);
    }

    #[test]
    fn model_switch_report_preserves_context_summary() {
        let report = format_model_switch_report("simcoe-sonnet", "simcoe-opus", 9);
        assert!(report.contains("Model updated"));
        assert!(report.contains("Previous         simcoe-sonnet"));
        assert!(report.contains("Current          simcoe-opus"));
        assert!(report.contains("Preserved msgs   9"));
    }

    #[test]
    fn status_line_reports_model_and_token_totals() {
        let status = format_status_report(
            "simcoe-sonnet",
            StatusUsage {
                message_count: 7,
                turns: 3,
                latest: runtime::TokenUsage {
                    input_tokens: 5,
                    output_tokens: 4,
                    cache_creation_input_tokens: 1,
                    cache_read_input_tokens: 0,
                },
                cumulative: runtime::TokenUsage {
                    input_tokens: 20,
                    output_tokens: 8,
                    cache_creation_input_tokens: 2,
                    cache_read_input_tokens: 1,
                },
                estimated_tokens: 128,
            },
            "workspace-write",
            &StatusContext {
                cwd: PathBuf::from("/tmp/project"),
                provider: "anthropic".to_string(),
                session_path: Some(PathBuf::from("session.json")),
                loaded_config_files: 2,
                discovered_config_files: 3,
                memory_file_count: 4,
                project_root: Some(PathBuf::from("/tmp")),
                git_branch: Some("main".to_string()),
            },
        );
        assert!(status.contains("Status"));
        assert!(status.contains("Provider         anthropic"));
        assert!(status.contains("Model            simcoe-sonnet"));
        assert!(status.contains("Permission mode  workspace-write"));
        assert!(status.contains("Messages         7"));
        assert!(status.contains("Latest total     10"));
        assert!(status.contains("Cumulative total 31"));
        assert!(status.contains("Cwd              /tmp/project"));
        assert!(status.contains("Project root     /tmp"));
        assert!(status.contains("Git branch       main"));
        assert!(status.contains("Session          session.json"));
        assert!(status.contains("Config files     loaded 2/3"));
        assert!(status.contains("Memory files     4"));
    }

    #[test]
    fn config_report_supports_section_views() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let report = render_config_report(Some("env")).expect("config report should render");
        assert!(report.contains("Merged section: env"));

        let payload =
            super::config_payload(Some("env".to_string())).expect("config payload should render");
        assert_eq!(payload["type"], json!("config"));
        assert_eq!(payload["section"], json!("env"));
        assert_eq!(payload["section_supported"], json!(true));
        assert_eq!(
            payload["supported_sections"],
            json!(["env", "hooks", "model", "provider"])
        );
        assert!(payload["content"]
            .as_str()
            .is_some_and(|content| content.contains("Merged section: env")));
    }

    #[test]
    fn config_report_supports_provider_section_views() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("config-provider-report");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let config_home = repo_root.join("home").join(".simcoe");
        fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            config_home.join("settings.json"),
            r#"{
    "provider": "openai",
    "model": "gpt-5.4"
}"#,
        )
        .expect("write provider settings");

        {
            let _config_home_guard = ScopedEnvVar::set("SIMCOE_CONFIG_HOME", &config_home);
            let _cwd_guard = ScopedCurrentDir::change_to(&nested_cwd);

            let report =
                render_config_report(Some("provider")).expect("config report should render");
            assert!(report.contains("Merged section: provider"));
            assert!(report.contains("openai"));

            let payload = super::config_payload(Some("provider".to_string()))
                .expect("config payload should render");
            assert_eq!(payload["type"], json!("config"));
            assert_eq!(payload["section"], json!("provider"));
            assert_eq!(payload["section_supported"], json!(true));
            assert_eq!(payload["section_value"], json!("openai"));
        }

        let _ = fs::remove_dir_all(repo_root);
    }

    #[test]
    fn memory_report_uses_sectioned_layout() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let report = render_memory_report().expect("memory report should render");
        assert!(report.contains("Memory"));
        assert!(report.contains("Working directory"));
        assert!(report.contains("Instruction files"));
        assert!(report.contains("Discovered files"));

        let payload = super::memory_payload().expect("memory payload should render");
        let instruction_files = payload["instruction_files"]
            .as_array()
            .expect("instruction files should be an array");
        assert_eq!(payload["type"], json!("memory"));
        assert_eq!(
            payload["working_directory"],
            json!(std::env::current_dir()
                .expect("cwd should resolve")
                .display()
                .to_string())
        );
        assert_eq!(
            payload["instruction_file_count"],
            json!(instruction_files.len())
        );
        assert!(payload["content"]
            .as_str()
            .is_some_and(|content| content.contains("Memory")));
    }

    #[test]
    fn config_report_uses_sectioned_layout() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let report = render_config_report(None).expect("config report should render");
        assert!(report.contains("Config"));
        assert!(report.contains("Discovered files"));
        assert!(report.contains("Merged JSON"));

        let payload = super::config_payload(None).expect("config payload should render");
        let discovered_files = payload["discovered_files"]
            .as_array()
            .expect("discovered files should be an array");
        assert_eq!(payload["type"], json!("config"));
        assert_eq!(
            payload["working_directory"],
            json!(std::env::current_dir()
                .expect("cwd should resolve")
                .display()
                .to_string())
        );
        assert_eq!(payload["merged_json"].is_object(), true);
        assert!(!discovered_files.is_empty());
    }

    #[test]
    fn parses_git_status_metadata() {
        let (root, branch) = parse_git_status_metadata(Some(
            "## rcc/cli...origin/rcc/cli
 M src/main.rs",
        ));
        assert_eq!(branch.as_deref(), Some("rcc/cli"));
        let _ = root;
    }

    #[test]
    fn status_context_reads_real_workspace_metadata() {
        let context = status_context(None).expect("status context should load");
        assert!(context.cwd.is_absolute());
        assert!(!context.provider.is_empty());
        assert!(context.discovered_config_files >= 5);
        assert!(context.loaded_config_files <= context.discovered_config_files);
    }

    #[test]
    fn normalizes_supported_permission_modes() {
        assert_eq!(normalize_permission_mode("read-only"), Some("read-only"));
        assert_eq!(
            normalize_permission_mode("workspace-write"),
            Some("workspace-write")
        );
        assert_eq!(
            normalize_permission_mode("danger-full-access"),
            Some("danger-full-access")
        );
        assert_eq!(normalize_permission_mode("unknown"), None);
    }

    #[test]
    fn clear_command_requires_explicit_confirmation_flag() {
        assert_eq!(
            SlashCommand::parse("/clear"),
            Some(SlashCommand::Clear { confirm: false })
        );
        assert_eq!(
            SlashCommand::parse("/clear --confirm"),
            Some(SlashCommand::Clear { confirm: true })
        );
    }

    #[test]
    fn parses_resume_and_config_slash_commands() {
        assert_eq!(
            SlashCommand::parse("/resume saved-session.json"),
            Some(SlashCommand::Resume {
                session_path: Some("saved-session.json".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/clear --confirm"),
            Some(SlashCommand::Clear { confirm: true })
        );
        assert_eq!(
            SlashCommand::parse("/dump-manifests"),
            Some(SlashCommand::DumpManifests)
        );
        assert_eq!(
            SlashCommand::parse("/bootstrap-plan"),
            Some(SlashCommand::BootstrapPlan)
        );
        assert_eq!(SlashCommand::parse("/login"), Some(SlashCommand::Login));
        assert_eq!(SlashCommand::parse("/logout"), Some(SlashCommand::Logout));
        assert_eq!(
            SlashCommand::parse("/system-prompt"),
            Some(SlashCommand::SystemPrompt { args: None })
        );
        assert_eq!(
            SlashCommand::parse("/system-prompt --cwd repo --date 2026-04-05"),
            Some(SlashCommand::SystemPrompt {
                args: Some("--cwd repo --date 2026-04-05".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/config"),
            Some(SlashCommand::Config { section: None })
        );
        assert_eq!(
            SlashCommand::parse("/config env"),
            Some(SlashCommand::Config {
                section: Some("env".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/hooks pre"),
            Some(SlashCommand::Hooks {
                event: Some("pre".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/mcp remote-server"),
            Some(SlashCommand::Mcp {
                server: Some("remote-server".to_string())
            })
        );
        assert_eq!(SlashCommand::parse("/memory"), Some(SlashCommand::Memory));
        assert_eq!(
            SlashCommand::parse("/agents explorer"),
            Some(SlashCommand::Agents {
                agent: Some("explorer".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/plugin reload-plugins"),
            Some(SlashCommand::Plugin {
                surface: Some("reload-plugins".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/reload-plugins"),
            Some(SlashCommand::ReloadPlugins)
        );
        assert_eq!(
            SlashCommand::parse("/remote-env"),
            Some(SlashCommand::RemoteEnv)
        );
        assert_eq!(
            SlashCommand::parse("/remote-setup"),
            Some(SlashCommand::RemoteSetup)
        );
        assert_eq!(
            SlashCommand::parse("/tools"),
            Some(SlashCommand::Tools { tool: None })
        );
        assert_eq!(
            SlashCommand::parse("/tools bash"),
            Some(SlashCommand::Tools {
                tool: Some("bash".to_string())
            })
        );
        assert_eq!(SlashCommand::parse("/doctor"), Some(SlashCommand::Doctor));
        assert_eq!(
            SlashCommand::parse("/skills context-map"),
            Some(SlashCommand::Skills {
                skill: Some("context-map".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/tasks agent-123"),
            Some(SlashCommand::Tasks {
                task: Some("agent-123".to_string())
            })
        );
        assert_eq!(SlashCommand::parse("/init"), Some(SlashCommand::Init));
    }

    #[test]
    fn init_template_mentions_detected_rust_workspace() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let rendered = crate::init::render_init_simcoe_md(std::path::Path::new("."));
        assert!(rendered.contains("# SIMCOE.md"));
        assert!(rendered.contains("cargo clippy --workspace --all-targets -- -D warnings"));
    }

    #[test]
    fn converts_tool_roundtrip_messages() {
        let messages = vec![
            ConversationMessage::user_text("hello"),
            ConversationMessage::assistant(vec![ContentBlock::ToolUse {
                id: "tool-1".to_string(),
                name: "bash".to_string(),
                input: "{\"command\":\"pwd\"}".to_string(),
            }]),
            ConversationMessage {
                role: MessageRole::Tool,
                blocks: vec![ContentBlock::ToolResult {
                    tool_use_id: "tool-1".to_string(),
                    tool_name: "bash".to_string(),
                    output: "ok".to_string(),
                    is_error: false,
                }],
                usage: None,
            },
        ];

        let converted = super::convert_messages(&messages);
        assert_eq!(converted.len(), 3);
        assert_eq!(converted[1].role, "assistant");
        assert_eq!(converted[2].role, "user");
    }
    #[test]
    fn repl_help_mentions_history_completion_and_multiline() {
        let help = render_repl_help();
        assert!(help.contains("Up/Down"));
        assert!(help.contains("Tab"));
        assert!(help.contains("Shift+Enter/Ctrl+J"));
    }

    #[test]
    fn tool_rendering_helpers_compact_output() {
        let start = format_tool_call_start("read_file", r#"{"path":"src/main.rs"}"#);
        assert!(start.contains("read_file"));
        assert!(start.contains("src/main.rs"));

        let powershell_start = format_tool_call_start(
            "PowerShell",
            r#"{"command":"Get-ChildItem src"}"#,
        );
        assert!(powershell_start.contains("PowerShell"));
        assert!(powershell_start.contains("PS> Get-ChildItem src"));

        let bash_tool_start = format_tool_call_start(
            "BashTool",
            r#"{"command":"ls src"}"#,
        );
        assert!(bash_tool_start.contains("BashTool"));
        assert!(bash_tool_start.contains("$ ls src"));

        let web_fetch_start = format_tool_call_start(
            "WebFetch",
            r#"{"url":"https://example.com","prompt":"Summarize"}"#,
        );
        assert!(web_fetch_start.contains("WebFetch"));
        assert!(web_fetch_start.contains("example.com"));

        let structured_start = format_tool_call_start(
            "StructuredOutput",
            r#"{"plan":"ok","count":2}"#,
        );
        assert!(structured_start.contains("StructuredOutput"));

        let repl_start = format_tool_call_start(
            "REPL",
            r#"{"language":"python","code":"print(1)"}"#,
        );
        assert!(repl_start.contains("REPL python"));

        let synthetic_start = format_tool_call_start(
            "SyntheticOutputTool",
            r##"{"content":"preview","outputType":"markdown"}"##,
        );
        assert!(synthetic_start.contains("SyntheticOutputTool"));
        assert!(synthetic_start.contains("markdown"));

        let sleep_start = format_tool_call_start(
            "Sleep",
            r#"{"duration_ms":250}"#,
        );
        assert!(sleep_start.contains("Sleep 250ms"));

        let todo_start = format_tool_call_start(
            "TodoWrite",
            r#"{"todos":[{"content":"Add tool","activeForm":"Adding tool","status":"in_progress"}]}"#,
        );
        assert!(todo_start.contains("TodoWrite"));
        assert!(todo_start.contains("1 items"));

        let skill_start = format_tool_call_start(
            "Skill",
            r#"{"skill":"help","args":"overview"}"#,
        );
        assert!(skill_start.contains("Skill help"));

        let session_export_start = format_tool_call_start(
            "SessionExportTool",
            r#"{"path":"session-notes"}"#,
        );
        assert!(session_export_start.contains("SessionExportTool"));
        assert!(session_export_start.contains("session-notes"));

        let notebook_start = format_tool_call_start(
            "NotebookEdit",
            r#"{"notebook_path":"demo.ipynb","edit_mode":"replace"}"#,
        );
        assert!(notebook_start.contains("NotebookEdit"));
        assert!(notebook_start.contains("demo.ipynb"));
        assert!(notebook_start.contains("replace"));

        let config_start = format_tool_call_start(
            "Config",
            r#"{"setting":"verbose","value":true}"#,
        );
        assert!(config_start.contains("Config"));
        assert!(config_start.contains("verbose"));

        let agent_start = format_tool_call_start(
            "Agent",
            r#"{"description":"Inspect repo layout","prompt":"Summarize modules"}"#,
        );
        assert!(agent_start.contains("Launching agent"));
        assert!(agent_start.contains("Inspect repo layout"));

        let brief_start = format_tool_call_start(
            "BriefTool",
            r#"{"message":"share this summary","status":"normal"}"#,
        );
        assert!(brief_start.contains("BriefTool"));
        assert!(brief_start.contains("share this summary"));

        let done = format_tool_result(
            "read_file",
            r#"{"file":{"filePath":"src/main.rs","content":"hello","numLines":1,"startLine":1,"totalLines":1}}"#,
            false,
        );
        assert!(done.contains("📄 Read src/main.rs"));
        assert!(done.contains("hello"));

        let powershell_result = format_tool_result(
            "PowerShell",
            r#"{"stdout":"item\n","stderr":"","rawOutputPath":null,"interrupted":false,"isImage":null,"backgroundTaskId":null,"backgroundedByUser":null,"assistantAutoBackgrounded":null,"dangerouslyDisableSandbox":null,"returnCodeInterpretation":"completed successfully","noOutputExpected":null,"structuredContent":null,"persistedOutputPath":null,"persistedOutputSize":null,"sandboxStatus":null}"#,
            false,
        );
        assert!(powershell_result.contains("PowerShell"));
        assert!(powershell_result.contains("completed successfully"));
        assert!(powershell_result.contains("item"));

        let web_fetch_result = format_tool_result(
            "WebFetch",
            r#"{"bytes":128,"code":200,"codeText":"OK","result":"Fetched https://example.com\nSummary line","durationMs":42,"url":"https://example.com"}"#,
            false,
        );
        assert!(web_fetch_result.contains("WebFetch"));
        assert!(web_fetch_result.contains("200 OK"));
        assert!(web_fetch_result.contains("example.com"));
        assert!(web_fetch_result.contains("bytes:"));
        assert!(web_fetch_result.contains("duration:"));
        assert!(web_fetch_result.contains("Summary line"));

        let web_search_result = format_tool_result(
            "WebSearch",
            r#"{"query":"rust web search","results":["Search results for \"rust web search\".",{"tool_use_id":"web_search_1","content":[{"title":"Reqwest docs","url":"https://docs.rs/reqwest"},{"title":"Tokio docs","url":"https://docs.rs/tokio"}]}],"durationSeconds":0.42}"#,
            false,
        );
        assert!(web_search_result.contains("WebSearch"));
        assert!(web_search_result.contains("rust web search"));
        assert!(web_search_result.contains("2 hits"));
        assert!(web_search_result.contains("Reqwest docs"));
        assert!(web_search_result.contains("docs.rs/reqwest"));

        let structured_result = format_tool_result(
            "StructuredOutput",
            r#"{"data":"Structured output provided successfully","structured_output":{"ok":true,"items":[1,2,3]}}"#,
            false,
        );
        assert!(structured_result.contains("StructuredOutput"));
        assert!(structured_result.contains("Structured output provided successfully"));
        assert!(structured_result.contains("items"));

        let repl_result = format_tool_result(
            "REPL",
            r#"{"language":"python","stdout":"hello\n","stderr":"","exitCode":0,"durationMs":12}"#,
            false,
        );
        assert!(repl_result.contains("REPL"));
        assert!(repl_result.contains("python"));
        assert!(repl_result.contains("exit 0"));
        assert!(repl_result.contains("duration:"));
        assert!(repl_result.contains("hello"));

        let synthetic_result = format_tool_result(
            "SyntheticOutputTool",
            r##"{"content":"# heading","outputType":"markdown","synthetic":true}"##,
            false,
        );
        assert!(synthetic_result.contains("SyntheticOutputTool"));
        assert!(synthetic_result.contains("markdown"));
        assert!(synthetic_result.contains("heading"));

        let sleep_result = format_tool_result(
            "Sleep",
            r#"{"duration_ms":250,"message":"Slept for 250ms"}"#,
            false,
        );
        assert!(sleep_result.contains("Sleep"));
        assert!(sleep_result.contains("250ms"));
        assert!(sleep_result.contains("Slept for 250ms"));

        let todo_result = format_tool_result(
            "TodoWrite",
            r#"{"oldTodos":[{"content":"Add tool","activeForm":"Adding tool","status":"in_progress"}],"newTodos":[{"content":"Add tool","activeForm":"Adding tool","status":"completed"},{"content":"Run tests","activeForm":"Running tests","status":"pending"}],"verificationNudgeNeeded":true}"#,
            false,
        );
        assert!(todo_result.contains("TodoWrite"));
        assert!(todo_result.contains("1 -> 2 items"));
        assert!(todo_result.contains("[completed]"));
        assert!(todo_result.contains("Run tests"));
        assert!(todo_result.contains("verification nudge suggested"));

        let skill_result = format_tool_result(
            "Skill",
            r##"{"skill":"help","path":"/tmp/help/SKILL.md","args":"overview","description":"Guide on using the help skill","prompt":"# Help\n\nGuide on using the help skill"}"##,
            false,
        );
        assert!(skill_result.contains("Skill"));
        assert!(skill_result.contains("help"));
        assert!(skill_result.contains("/tmp/help/SKILL.md"));
        assert!(skill_result.contains("overview"));
        assert!(skill_result.contains("Guide on using the help skill"));

        let session_export_result = format_tool_result(
            "SessionExportTool",
            r#"{"sessionId":"session-123","sessionPath":"/tmp/session-123.json","exportPath":"/tmp/session-notes.txt","messageCount":4}"#,
            false,
        );
        assert!(session_export_result.contains("SessionExportTool"));
        assert!(session_export_result.contains("session-123"));
        assert!(session_export_result.contains("4 messages"));
        assert!(session_export_result.contains("session-notes.txt"));

        let notebook_result = format_tool_result(
            "NotebookEdit",
            r#"{"new_source":"print(2)\n","cell_id":"cell-a","cell_type":"code","language":"python","edit_mode":"replace","error":null,"notebook_path":"demo.ipynb","original_file":"{}","updated_file":"{}"}"#,
            false,
        );
        assert!(notebook_result.contains("NotebookEdit"));
        assert!(notebook_result.contains("demo.ipynb"));
        assert!(notebook_result.contains("cell-a"));
        assert!(notebook_result.contains("code / python"));
        assert!(notebook_result.contains("print(2)"));

        let config_result = format_tool_result(
            "Config",
            r#"{"success":true,"operation":"set","setting":"permissions.defaultMode","value":"plan","previousValue":null,"newValue":"plan","error":null}"#,
            false,
        );
        assert!(config_result.contains("Config"));
        assert!(config_result.contains("permissions.defaultMode"));
        assert!(config_result.contains("set"));
        assert!(config_result.contains("value:"));
        assert!(config_result.contains("new:"));
        assert!(config_result.contains("plan"));

        let agent_result = format_tool_result(
            "Agent",
            r#"{"agentId":"agent-123","name":"inspect-repo-layout","description":"Inspect repo layout","subagentType":"Explore","model":"simcoe-opus-4-6","status":"running","outputFile":"/tmp/agent-123.md","manifestFile":"/tmp/agent-123.json","createdAt":"1775962415","startedAt":"1775962415"}"#,
            false,
        );
        assert!(agent_result.contains("Agent"));
        assert!(agent_result.contains("inspect-repo-layout"));
        assert!(agent_result.contains("agent-123"));
        assert!(agent_result.contains("Inspect repo layout"));
        assert!(agent_result.contains("running"));

        let brief_result = format_tool_result(
            "BriefTool",
            r#"{"message":"hello user","attachments":[{"path":"/tmp/demo.png","size":8,"isImage":true}],"sentAt":"2026-04-12T10:00:00Z"}"#,
            false,
        );
        assert!(brief_result.contains("BriefTool"));
        assert!(brief_result.contains("hello user"));
        assert!(brief_result.contains("sent:"));
        assert!(brief_result.contains("attachments:"));
        assert!(brief_result.contains("demo.png"));

        let file_read_tool_result = format_tool_result(
            "FileReadTool",
            r#"{"file":{"filePath":"demo.txt","content":"hello","numLines":1,"startLine":1,"totalLines":1}}"#,
            false,
        );
        assert!(file_read_tool_result.contains("📄 Read demo.txt"));
        assert!(file_read_tool_result.contains("hello"));

        let send_message_tool_result = format_tool_result(
            "SendMessageTool",
            r#"{"message":"hello alias","attachments":null,"sentAt":"2026-04-12T10:00:00Z"}"#,
            false,
        );
        assert!(send_message_tool_result.contains("SendMessageTool"));
        assert!(send_message_tool_result.contains("hello alias"));
        assert!(send_message_tool_result.contains("sent:"));

        let tool_search = format_tool_result(
            "ToolSearch",
            r#"{"query":"vendor echo","matches":["mcp__vendor__echo","read_file"],"match_details":[{"name":"mcp__vendor__echo","aliases":[],"description":"Invoke MCP tool echo on configured vendor server.","source":"dynamic-mcp","required_permission":"danger-full-access","mcp_server":"vendor","mcp_tool":"echo"},{"name":"read_file","aliases":["FileReadTool"],"description":"Read a file from disk.","source":"registry","required_permission":"read-only"}],"pending_mcp_server_details":[{"server":"remote","reason_kind":"unsupported-runtime","detail":"http transport with headersHelper is not executed by the Rust MCP runtime yet"}]}"#,
            false,
        );
        assert!(tool_search.contains("ToolSearch"));
        assert!(tool_search.contains("2 matches for vendor echo"));
        assert!(tool_search.contains("mcp__vendor__echo [dynamic-mcp:vendor, danger-full-access]"));
        assert!(tool_search.contains("read_file (FileReadTool) [registry, read-only]"));
        assert!(tool_search.contains("Pending MCP discovery"));
        assert!(tool_search.contains("remote [unsupported-runtime]"));

        let list_mcp_resources = format_tool_result(
            "ListMcpResourcesTool",
            r#"{"server":"alpha","transport":"stdio","resourceCount":2,"resources":[{"uri":"file://guide.txt","name":"Guide","description":"Primary guide for the MCP server.","mimeType":"text/plain"},{"uri":"file://schema.json","name":"Schema","mimeType":"application/json"}]}"#,
            false,
        );
        assert!(list_mcp_resources.contains("ListMcpResourcesTool"));
        assert!(list_mcp_resources.contains("alpha [stdio] 2 resources"));
        assert!(list_mcp_resources.contains("Resources"));
        assert!(list_mcp_resources
            .contains("file://guide.txt Guide [text/plain] Primary guide for the MCP server."));
        assert!(list_mcp_resources.contains("file://schema.json Schema [application/json]"));

        let read_mcp_resource = format_tool_result(
            "ReadMcpResourceTool",
            r#"{"server":"alpha","transport":"http","uri":"file://guide.txt","contentCount":2,"contents":[{"uri":"file://guide.txt","mimeType":"text/plain","text":"contents for file://guide.txt"},{"uri":"file://diagram.png","mimeType":"image/png","blob":"aGVsbG8="}]}"#,
            false,
        );
        assert!(read_mcp_resource.contains("ReadMcpResourceTool"));
        assert!(read_mcp_resource.contains("file://guide.txt from alpha [http] 2 items"));
        assert!(read_mcp_resource.contains("Contents"));
        assert!(read_mcp_resource
            .contains("file://guide.txt [text/plain] contents for file://guide.txt"));
        assert!(read_mcp_resource.contains("file://diagram.png [image/png] blob 8 chars"));

        let mcp_tool_list = format_tool_result(
            "MCPTool",
            r#"{"server":"alpha","transport":"stdio","action":"list_tools","toolCount":2,"tools":[{"name":"echo","description":"Echo text back from the MCP server."},{"name":"search","description":"Search the remote catalog."}]}"#,
            false,
        );
        assert!(mcp_tool_list.contains("MCPTool"));
        assert!(mcp_tool_list.contains("list_tools alpha [stdio] 2 tools"));
        assert!(mcp_tool_list.contains("Tools"));
        assert!(mcp_tool_list.contains("echo Echo text back from the MCP server."));
        assert!(mcp_tool_list.contains("search Search the remote catalog."));

        let mcp_tool_call = format_tool_result(
            "MCPTool",
            r#"{"server":"alpha","transport":"http","action":"call_tool","tool":"echo","qualifiedToolName":"mcp__alpha__echo","content":[{"type":"text","text":"hello from alpha"}],"structuredContent":{"server":"alpha","echoed":"hello from alpha"},"isError":false}"#,
            false,
        );
        assert!(mcp_tool_call.contains("call_tool mcp__alpha__echo on alpha [http]"));
        assert!(mcp_tool_call.contains("Content"));
        assert!(mcp_tool_call.contains("text hello from alpha"));
        assert!(mcp_tool_call
            .contains("Structured {\"echoed\":\"hello from alpha\",\"server\":\"alpha\"}"));

        let dynamic_mcp_tool_call = format_tool_result(
            "mcp__alpha__echo",
            r#"{"server":"alpha","transport":"http","action":"call_tool","tool":"echo","qualifiedToolName":"mcp__alpha__echo","content":[{"type":"text","text":"hello from alpha"}],"structuredContent":{"server":"alpha","echoed":"hello from alpha"},"isError":false}"#,
            false,
        );
        assert!(dynamic_mcp_tool_call.contains("mcp__alpha__echo"));
        assert!(dynamic_mcp_tool_call.contains("call_tool mcp__alpha__echo on alpha [http]"));
        assert!(dynamic_mcp_tool_call.contains("text hello from alpha"));

        let mcp_tool_auth_error = format_tool_result(
            "MCPTool",
            "MCP server `remote` requires stored OAuth credentials; save them with McpAuthTool action `save`",
            true,
        );
        assert!(mcp_tool_auth_error.contains("MCPTool"));
        assert!(mcp_tool_auth_error.contains("remote [auth-required]"));
        assert!(mcp_tool_auth_error.contains("requires stored OAuth credentials"));
        assert!(mcp_tool_auth_error
            .contains("Hint Save MCP OAuth credentials with McpAuthTool action `save`."));

        let mcp_resource_blocked_error = format_tool_result(
            "ReadMcpResourceTool",
            "MCP server `remote` uses http transport; http transport with headersHelper is not executed by the Rust MCP runtime yet",
            true,
        );
        assert!(mcp_resource_blocked_error.contains("ReadMcpResourceTool"));
        assert!(mcp_resource_blocked_error.contains("remote [unsupported-runtime]"));
        assert!(mcp_resource_blocked_error.contains("headersHelper"));
        assert!(mcp_resource_blocked_error
            .contains("Hint Remove headersHelper for direct Rust execution"));

        let dynamic_mcp_blocked_error = format_tool_result(
            "mcp__remote__echo",
            "MCP server `remote` uses http transport; http transport with headersHelper is not executed by the Rust MCP runtime yet",
            true,
        );
        assert!(dynamic_mcp_blocked_error.contains("mcp__remote__echo"));
        assert!(dynamic_mcp_blocked_error.contains("remote [unsupported-runtime]"));
        assert!(dynamic_mcp_blocked_error.contains("headersHelper"));

        let mcp_http_error = format_tool_result(
            "MCPTool",
            "MCP server `remote` returned HTTP 502 for tools/list: upstream timeout",
            true,
        );
        assert!(mcp_http_error.contains("MCPTool"));
        assert!(mcp_http_error.contains("remote [discovery-error, tools/list, HTTP 502]"));
        assert!(mcp_http_error.contains("upstream timeout"));
        assert!(mcp_http_error.contains("Hint Check the MCP endpoint, upstream service health"));

        let mcp_refresh_error = format_tool_result(
            "MCPTool",
            "OAuth refresh for MCP server `remote` failed with HTTP 401: invalid_grant",
            true,
        );
        assert!(mcp_refresh_error.contains("MCPTool"));
        assert!(mcp_refresh_error.contains("remote [expired-credentials, oauth-refresh, HTTP 401]"));
        assert!(mcp_refresh_error.contains("invalid_grant"));
        assert!(
            mcp_refresh_error.contains("Hint Re-authenticate and save fresh MCP OAuth credentials")
        );

        let mcp_jsonrpc_error = format_tool_result(
            "mcp__remote__echo",
            "MCP server `remote` returned JSON-RPC error for tools/call: tool not found (-32601)",
            true,
        );
        assert!(mcp_jsonrpc_error.contains("mcp__remote__echo"));
        assert!(mcp_jsonrpc_error.contains("remote [discovery-error, tools/call]"));
        assert!(mcp_jsonrpc_error.contains("tool not found"));
        assert!(mcp_jsonrpc_error.contains(
            "Hint Check the remote MCP server logs and confirm the requested tool or resource still exists."
        ));

        let mcp_auth = format_tool_result(
            "McpAuthTool",
            r#"{"action":"status","serverCount":3,"supportedExecutionCount":2,"unsupportedExecutionCount":1,"statusCounts":{"ready":1,"unsupported-transport":1,"user-auth-required":1},"attentionServers":[{"server":"vendor","transport":"http","status":"user-auth-required","reasonKind":"auth-required"},{"server":"sdk-server","transport":"sdk","status":"unsupported-transport","reasonKind":"unsupported-runtime","detail":"SDK adapter runtime missing"}],"unsupportedServers":[{"server":"sdk-server","transport":"sdk","reasonKind":"unsupported-runtime","detail":"SDK adapter runtime missing"}],"servers":[{"server":"repo","status":"ready","transport":"stdio","authKind":"none","requiresUserAuth":false,"supportedExecution":true,"interactiveSupported":true,"storedCredentials":false,"refreshTokenPresent":false},{"server":"vendor","status":"user-auth-required","transport":"http","authKind":"oauth","requiresUserAuth":true,"supportedExecution":true,"interactiveSupported":true,"reasonKind":"auth-required","storedCredentials":false,"refreshTokenPresent":false},{"server":"sdk-server","status":"unsupported-transport","transport":"sdk","authKind":"none","requiresUserAuth":false,"supportedExecution":false,"interactiveSupported":false,"reasonKind":"unsupported-runtime","storedCredentials":false,"refreshTokenPresent":false,"detail":"SDK adapter runtime missing"}]}"#,
            false,
        );
        assert!(mcp_auth.contains("McpAuthTool"));
        assert!(mcp_auth.contains("status 3 servers (2 executable, 1 blocked)"));
        assert!(
            mcp_auth.contains("Statuses ready=1, unsupported-transport=1, user-auth-required=1")
        );
        assert!(mcp_auth.contains("Attention"));
        assert!(mcp_auth.contains("vendor [http, user-auth-required, auth-required]"));
        assert!(mcp_auth.contains("sdk-server [sdk, unsupported-transport, unsupported-runtime] SDK adapter runtime missing"));

        let mcp_auth_save = format_tool_result(
            "McpAuthTool",
            r#"{"action":"save","serverCount":1,"supportedExecutionCount":1,"unsupportedExecutionCount":0,"statusCounts":{"ready":1},"unsupportedServers":[],"attentionServers":[],"servers":[{"server":"vendor","status":"ready","transport":"http","authKind":"oauth","requiresUserAuth":false,"supportedExecution":true,"interactiveSupported":true,"storedCredentials":true,"refreshTokenPresent":true}]}"#,
            false,
        );
        assert!(mcp_auth_save.contains("save 1 server (1 executable, 0 blocked)"));
        assert!(mcp_auth_save.contains("Servers"));
        assert!(mcp_auth_save.contains("vendor [ready] oauth, stored-credentials, refresh-token"));

        let testing_permission = format_tool_result(
            "TestingPermissionTool",
            r#"{"action":"bash","path":"/tmp/demo","toolName":"bash","currentMode":"workspace-write","requiredMode":"danger-full-access","outcome":"prompt","reason":"tool 'bash' requires approval to escalate from workspace-write to danger-full-access"}"#,
            false,
        );
        assert!(testing_permission.contains("TestingPermissionTool"));
        assert!(testing_permission
            .contains("bash -> bash [prompt] workspace-write -> danger-full-access"));
        assert!(testing_permission.contains("Path"));
        assert!(testing_permission.contains("/tmp/demo"));
        assert!(testing_permission.contains("Reason"));
        assert!(testing_permission.contains("requires approval to escalate"));

        let team_created = format_tool_result(
            "TeamCreateTool",
            r#"{"teamId":"team-123","name":"alpha","description":"First responders","createdAt":"1775962415","message":"stored in the local team registry only; no connected backend collaboration service or multi-user sync is active"}"#,
            false,
        );
        assert!(team_created.contains("TeamCreateTool"));
        assert!(team_created.contains("alpha"));
        assert!(team_created.contains("id:"));
        assert!(team_created.contains("team-123"));
        assert!(team_created.contains("description:"));
        assert!(team_created.contains("First responders"));
        assert!(team_created.contains("local team registry"));

        let team_deleted = format_tool_result(
            "TeamDeleteTool",
            r#"{"teamId":"team-123","name":"alpha","createdAt":"1775962415","deletedAt":"1775962999","message":"removed from the local team registry; no backend collaboration service was managing this team"}"#,
            false,
        );
        assert!(team_deleted.contains("TeamDeleteTool"));
        assert!(team_deleted.contains("alpha"));
        assert!(team_deleted.contains("deleted:"));
        assert!(team_deleted.contains("1775962999"));
        assert!(team_deleted.contains("removed from the local team registry"));

        let remote_trigger = format_tool_result(
            "RemoteTriggerTool",
            r#"{"event":"sync","triggered":false,"remoteEnabled":true,"sessionId":"session-123","baseUrl":"http://127.0.0.1:8765","pathReady":true,"blockerKind":"adapter-not-ported","blockerDetail":"upstream proxy websocket/session adapter is not ported in Rust","message":"remote trigger transport path is configured, but the upstream websocket/session adapter is not ported in Rust yet"}"#,
            false,
        );
        assert!(remote_trigger.contains("RemoteTriggerTool"));
        assert!(remote_trigger.contains("sync"));
        assert!(remote_trigger.contains("adapter-not-ported"));
        assert!(remote_trigger.contains("remote:"));
        assert!(remote_trigger.contains("path:"));
        assert!(remote_trigger.contains("session-123"));
        assert!(remote_trigger.contains("127.0.0.1:8765"));
        assert!(remote_trigger.contains("adapter is not ported"));

        let lsp_diagnostic = format_tool_result(
            "LSPTool",
            r#"{"command":"diagnostics","connected":false,"reasonKind":"unsupported-runtime","supportedCommands":["diagnostics","hover","completions","definition","references"],"message":"no language server is connected in this Rust session; attach an LSP-aware editor or connect via the remote transport"}"#,
            false,
        );
        assert!(lsp_diagnostic.contains("LSPTool"));
        assert!(lsp_diagnostic.contains("diagnostics"));
        assert!(lsp_diagnostic.contains("unsupported-runtime"));
        assert!(lsp_diagnostic.contains("supported:"));
        assert!(lsp_diagnostic.contains("hover"));
        assert!(lsp_diagnostic.contains("no language server is connected"));

        let cron_created = format_tool_result(
            "CronCreateTool",
            r#"{"cronId":"cron-123","schedule":"0 * * * *","command":"backup --now","description":"Hourly backup","createdAt":"1775962415","message":"stored in the local cron registry only; no scheduler service is executing jobs"}"#,
            false,
        );
        assert!(cron_created.contains("CronCreateTool"));
        assert!(cron_created.contains("[0 * * * *] backup --now"));
        assert!(cron_created.contains("id:"));
        assert!(cron_created.contains("cron-123"));
        assert!(cron_created.contains("description:"));
        assert!(cron_created.contains("Hourly backup"));
        assert!(cron_created.contains("local cron registry"));

        let cron_list = format_tool_result(
            "CronListTool",
            r#"{"crons":[{"cronId":"cron-123","schedule":"0 * * * *","command":"backup --now","createdAt":"1775962415"}],"total":1,"message":"local cron registry only; stored schedules are not executed by a scheduler service"}"#,
            false,
        );
        assert!(cron_list.contains("CronListTool"));
        assert!(cron_list.contains("(1 jobs)"));
        assert!(cron_list.contains("cron-123"));
        assert!(cron_list.contains("backup --now"));
        assert!(cron_list.contains("not executed by a scheduler service"));

        let plan_mode_entered = format_tool_result(
            "EnterPlanModeTool",
            r#"{"active":true,"previousActive":false,"message":"plan mode enabled; state-changing tools are now blocked"}"#,
            false,
        );
        assert!(plan_mode_entered.contains("EnterPlanModeTool"));
        assert!(plan_mode_entered.contains("active"));
        assert!(plan_mode_entered.contains("previous:"));
        assert!(plan_mode_entered.contains("inactive"));
        assert!(plan_mode_entered.contains("state-changing tools are now blocked"));

        let plan_mode_exited = format_tool_result(
            "ExitPlanModeV2Tool",
            r#"{"active":false,"previousActive":true,"message":"plan mode disabled; state-changing tools may run again"}"#,
            false,
        );
        assert!(plan_mode_exited.contains("ExitPlanModeV2Tool"));
        assert!(plan_mode_exited.contains("inactive"));
        assert!(plan_mode_exited.contains("previous:"));
        assert!(plan_mode_exited.contains("active"));
        assert!(plan_mode_exited.contains("may run again"));

        let worktree_entered = format_tool_result(
            "EnterWorktreeTool",
            r#"{"active":true,"worktreePath":"/tmp/repo","message":"relative bash and file tools now resolve from the active git worktree root"}"#,
            false,
        );
        assert!(worktree_entered.contains("EnterWorktreeTool"));
        assert!(worktree_entered.contains("active /tmp/repo"));
        assert!(worktree_entered.contains("worktree:"));
        assert!(worktree_entered.contains("relative bash and file tools now resolve"));

        let worktree_exited = format_tool_result(
            "ExitWorktreeTool",
            r#"{"active":false,"previousPath":"/tmp/repo","message":"cleared the active git worktree override; relative bash and file tools now resolve from the process cwd"}"#,
            false,
        );
        assert!(worktree_exited.contains("ExitWorktreeTool"));
        assert!(worktree_exited.contains("inactive"));
        assert!(worktree_exited.contains("previous:"));
        assert!(worktree_exited.contains("/tmp/repo"));
        assert!(worktree_exited.contains("process cwd"));
    }

    #[test]
    fn push_output_block_renders_markdown_text() {
        let mut out = Vec::new();
        let mut events = Vec::new();
        let mut pending_tool = None;

        push_output_block(
            OutputContentBlock::Text {
                text: "# Heading".to_string(),
            },
            &mut out,
            &mut events,
            &mut pending_tool,
            false,
        )
        .expect("text block should render");

        let rendered = String::from_utf8(out).expect("utf8");
        assert!(rendered.contains("Heading"));
        assert!(rendered.contains('\u{1b}'));
    }

    #[test]
    fn push_output_block_skips_empty_object_prefix_for_tool_streams() {
        let mut out = Vec::new();
        let mut events = Vec::new();
        let mut pending_tool = None;

        push_output_block(
            OutputContentBlock::ToolUse {
                id: "tool-1".to_string(),
                name: "read_file".to_string(),
                input: json!({}),
            },
            &mut out,
            &mut events,
            &mut pending_tool,
            true,
        )
        .expect("tool block should accumulate");

        assert!(events.is_empty());
        assert_eq!(
            pending_tool,
            Some(("tool-1".to_string(), "read_file".to_string(), String::new(),))
        );
    }

    #[test]
    fn response_to_events_preserves_empty_object_json_input_outside_streaming() {
        let mut out = Vec::new();
        let events = response_to_events(
            MessageResponse {
                id: "msg-1".to_string(),
                kind: "message".to_string(),
                model: "simcoe-opus-4-6".to_string(),
                role: "assistant".to_string(),
                content: vec![OutputContentBlock::ToolUse {
                    id: "tool-1".to_string(),
                    name: "read_file".to_string(),
                    input: json!({}),
                }],
                stop_reason: Some("tool_use".to_string()),
                stop_sequence: None,
                usage: Usage {
                    input_tokens: 1,
                    output_tokens: 1,
                    cache_creation_input_tokens: 0,
                    cache_read_input_tokens: 0,
                },
                request_id: None,
            },
            &mut out,
        )
        .expect("response conversion should succeed");

        assert!(matches!(
            &events[0],
            AssistantEvent::ToolUse { name, input, .. }
                if name == "read_file" && input == "{}"
        ));
    }

    #[test]
    fn response_to_events_preserves_non_empty_json_input_outside_streaming() {
        let mut out = Vec::new();
        let events = response_to_events(
            MessageResponse {
                id: "msg-2".to_string(),
                kind: "message".to_string(),
                model: "simcoe-opus-4-6".to_string(),
                role: "assistant".to_string(),
                content: vec![OutputContentBlock::ToolUse {
                    id: "tool-2".to_string(),
                    name: "read_file".to_string(),
                    input: json!({ "path": "rust/Cargo.toml" }),
                }],
                stop_reason: Some("tool_use".to_string()),
                stop_sequence: None,
                usage: Usage {
                    input_tokens: 1,
                    output_tokens: 1,
                    cache_creation_input_tokens: 0,
                    cache_read_input_tokens: 0,
                },
                request_id: None,
            },
            &mut out,
        )
        .expect("response conversion should succeed");

        assert!(matches!(
            &events[0],
            AssistantEvent::ToolUse { name, input, .. }
                if name == "read_file" && input == "{\"path\":\"rust/Cargo.toml\"}"
        ));
    }
}
