use std::collections::{BTreeMap, BTreeSet};
use std::env;
use std::path::PathBuf;

use runtime::PermissionMode;
use tools::{matches_tool_request, mvp_tool_specs};

pub(crate) type AllowedToolSet = BTreeSet<String>;

const NAMED_CLI_SUBCOMMANDS: &[&str] = &[
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
    "export",
    "session",
    "login",
    "logout",
    "init",
    "prompt",
];

#[derive(Debug, Clone, PartialEq, Eq)]
pub(crate) enum CliAction {
    DumpManifests {
        output_format: CliOutputFormat,
    },
    BootstrapPlan {
        output_format: CliOutputFormat,
    },
    PrintSystemPrompt {
        cwd: PathBuf,
        date: String,
        output_format: CliOutputFormat,
    },
    Config {
        section: Option<String>,
        output_format: CliOutputFormat,
    },
    Hooks {
        event: Option<String>,
        output_format: CliOutputFormat,
    },
    Mcp {
        server: Option<String>,
        output_format: CliOutputFormat,
    },
    Memory {
        output_format: CliOutputFormat,
    },
    Agents {
        agent: Option<String>,
        output_format: CliOutputFormat,
    },
    Plugin {
        surface: Option<String>,
        output_format: CliOutputFormat,
    },
    ReloadPlugins {
        output_format: CliOutputFormat,
    },
    RemoteEnv {
        output_format: CliOutputFormat,
    },
    RemoteSetup {
        output_format: CliOutputFormat,
    },
    Tools {
        tool: Option<String>,
        output_format: CliOutputFormat,
    },
    Doctor {
        output_format: CliOutputFormat,
    },
    Skills {
        skill: Option<String>,
        output_format: CliOutputFormat,
    },
    Tasks {
        task: Option<String>,
        output_format: CliOutputFormat,
    },
    Export {
        path: Option<String>,
        output_format: CliOutputFormat,
    },
    Session {
        action: Option<String>,
        target: Option<String>,
        output_format: CliOutputFormat,
    },
    Version {
        output_format: CliOutputFormat,
    },
    ResumeSession {
        session_path: PathBuf,
        commands: Vec<String>,
        output_format: CliOutputFormat,
    },
    Prompt {
        prompt: String,
        model: String,
        provider: Option<String>,
        output_format: CliOutputFormat,
        allowed_tools: Option<AllowedToolSet>,
        permission_mode: PermissionMode,
    },
    Login {
        output_format: CliOutputFormat,
    },
    Logout {
        output_format: CliOutputFormat,
    },
    Init {
        output_format: CliOutputFormat,
    },
    Repl {
        model: String,
        provider: Option<String>,
        allowed_tools: Option<AllowedToolSet>,
        permission_mode: PermissionMode,
    },
    Help,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(crate) enum CliOutputFormat {
    Text,
    Json,
    Ndjson,
}

impl CliOutputFormat {
    fn parse(value: &str) -> Result<Self, String> {
        match value {
            "text" => Ok(Self::Text),
            "json" => Ok(Self::Json),
            "ndjson" => Ok(Self::Ndjson),
            other => Err(format!(
                "unsupported value for --output-format: {other} (expected text, json, or ndjson)"
            )),
        }
    }
}

pub(crate) fn named_cli_subcommands() -> &'static [&'static str] {
    NAMED_CLI_SUBCOMMANDS
}

#[allow(clippy::too_many_lines)]
pub(crate) fn parse_args(args: &[String]) -> Result<CliAction, String> {
    let mut model = crate::DEFAULT_MODEL.to_string();
    let mut provider = None;
    let mut output_format = CliOutputFormat::Text;
    let mut permission_mode = default_permission_mode();
    let mut wants_version = false;
    let mut allowed_tool_values = Vec::new();
    let mut rest = Vec::new();
    let mut index = 0;

    while index < args.len() {
        match args[index].as_str() {
            "--version" | "-V" => {
                wants_version = true;
                index += 1;
            }
            "--model" => {
                let value = args
                    .get(index + 1)
                    .ok_or_else(|| "missing value for --model".to_string())?;
                model = resolve_model_alias(value).to_string();
                index += 2;
            }
            flag if flag.starts_with("--model=") => {
                model = resolve_model_alias(&flag[8..]).to_string();
                index += 1;
            }
            "--provider" => {
                let value = args
                    .get(index + 1)
                    .ok_or_else(|| "missing value for --provider".to_string())?;
                provider = Some(value.clone());
                index += 2;
            }
            flag if flag.starts_with("--provider=") => {
                provider = Some(flag[11..].to_string());
                index += 1;
            }
            "--output-format" => {
                let value = args
                    .get(index + 1)
                    .ok_or_else(|| "missing value for --output-format".to_string())?;
                output_format = CliOutputFormat::parse(value)?;
                index += 2;
            }
            "--permission-mode" => {
                let value = args
                    .get(index + 1)
                    .ok_or_else(|| "missing value for --permission-mode".to_string())?;
                permission_mode = parse_permission_mode_arg(value)?;
                index += 2;
            }
            flag if flag.starts_with("--output-format=") => {
                output_format = CliOutputFormat::parse(&flag[16..])?;
                index += 1;
            }
            flag if flag.starts_with("--permission-mode=") => {
                permission_mode = parse_permission_mode_arg(&flag[18..])?;
                index += 1;
            }
            "--dangerously-skip-permissions" => {
                permission_mode = PermissionMode::DangerFullAccess;
                index += 1;
            }
            "-p" => {
                let prompt = args[index + 1..].join(" ");
                if prompt.trim().is_empty() {
                    return Err("-p requires a prompt string".to_string());
                }
                return Ok(CliAction::Prompt {
                    prompt,
                    model: resolve_model_alias(&model).to_string(),
                    provider,
                    output_format,
                    allowed_tools: normalize_allowed_tools(&allowed_tool_values)?,
                    permission_mode,
                });
            }
            "--print" => {
                output_format = CliOutputFormat::Text;
                index += 1;
            }
            "--allowedTools" | "--allowed-tools" => {
                let value = args
                    .get(index + 1)
                    .ok_or_else(|| "missing value for --allowedTools".to_string())?;
                allowed_tool_values.push(value.clone());
                index += 2;
            }
            flag if flag.starts_with("--allowedTools=") => {
                allowed_tool_values.push(flag[15..].to_string());
                index += 1;
            }
            flag if flag.starts_with("--allowed-tools=") => {
                allowed_tool_values.push(flag[16..].to_string());
                index += 1;
            }
            other => {
                rest.push(other.to_string());
                index += 1;
            }
        }
    }

    if wants_version {
        return Ok(CliAction::Version { output_format });
    }

    let allowed_tools = normalize_allowed_tools(&allowed_tool_values)?;

    if rest.is_empty() {
        return Ok(CliAction::Repl {
            model,
            provider,
            allowed_tools,
            permission_mode,
        });
    }
    if matches!(rest.first().map(String::as_str), Some("--help" | "-h")) {
        return Ok(CliAction::Help);
    }
    if rest.first().map(String::as_str) == Some("--resume") {
        return parse_resume_args(&rest[1..], output_format);
    }

    match rest[0].as_str() {
        "dump-manifests" => Ok(CliAction::DumpManifests { output_format }),
        "bootstrap-plan" => Ok(CliAction::BootstrapPlan { output_format }),
        "system-prompt" => parse_system_prompt_args(&rest[1..], output_format),
        "config" => parse_config_args(&rest[1..], output_format),
        "hooks" => parse_hooks_args(&rest[1..], output_format),
        "mcp" => parse_mcp_args(&rest[1..], output_format),
        "memory" => parse_memory_args(&rest[1..], output_format),
        "agents" => parse_agents_args(&rest[1..], output_format),
        "plugin" => parse_plugin_args(&rest[1..], output_format),
        "reload-plugins" => parse_reload_plugins_args(&rest[1..], output_format),
        "remote-env" => parse_remote_env_args(&rest[1..], output_format),
        "remote-setup" => parse_remote_setup_args(&rest[1..], output_format),
        "tools" => parse_tools_args(&rest[1..], output_format),
        "doctor" => parse_doctor_args(&rest[1..], output_format),
        "skills" => parse_skills_args(&rest[1..], output_format),
        "tasks" => parse_tasks_args(&rest[1..], output_format),
        "export" => parse_export_args(&rest[1..], output_format),
        "session" => parse_session_args(&rest[1..], output_format),
        "login" => Ok(CliAction::Login { output_format }),
        "logout" => Ok(CliAction::Logout { output_format }),
        "init" => Ok(CliAction::Init { output_format }),
        "prompt" => {
            let prompt = rest[1..].join(" ");
            if prompt.trim().is_empty() {
                return Err("prompt subcommand requires a prompt string".to_string());
            }
            Ok(CliAction::Prompt {
                prompt,
                model,
                provider,
                output_format,
                allowed_tools,
                permission_mode,
            })
        }
        other if !other.starts_with('/') => Ok(CliAction::Prompt {
            prompt: rest.join(" "),
            model,
            provider,
            output_format,
            allowed_tools,
            permission_mode,
        }),
        other => Err(format!("unknown subcommand: {other}")),
    }
}

pub(crate) fn resolve_model_alias(model: &str) -> &str {
    match model {
        "opus" | "simcoe-opus" => "simcoe-opus-4-6",
        "sonnet" | "simcoe-sonnet" => "simcoe-sonnet-4-6",
        "haiku" | "simcoe-haiku" => "simcoe-haiku-4-5-20251213",
        _ => model,
    }
}

pub(crate) fn brand_model_name(model: &str) -> &str {
    match model {
        "claude-opus-4-6" | "simcoe-opus-4-6" => "simcoe-opus",
        "claude-sonnet-4-6" | "simcoe-sonnet-4-6" => "simcoe-sonnet",
        "claude-haiku-4-5-20251213" | "simcoe-haiku-4-5-20251213" => "simcoe-haiku",
        _ => model,
    }
}

pub(crate) fn normalize_permission_mode(mode: &str) -> Option<&'static str> {
    match mode.trim() {
        "read-only" => Some("read-only"),
        "workspace-write" => Some("workspace-write"),
        "danger-full-access" => Some("danger-full-access"),
        _ => None,
    }
}

pub(crate) fn permission_mode_from_label(mode: &str) -> PermissionMode {
    match mode {
        "read-only" => PermissionMode::ReadOnly,
        "workspace-write" => PermissionMode::WorkspaceWrite,
        "danger-full-access" => PermissionMode::DangerFullAccess,
        other => panic!("unsupported permission mode label: {other}"),
    }
}

pub(crate) fn default_permission_mode() -> PermissionMode {
    env::var("SIMCOE_PERMISSION_MODE")
        .ok()
        .as_deref()
        .and_then(normalize_permission_mode)
        .map_or(PermissionMode::DangerFullAccess, permission_mode_from_label)
}

fn normalize_allowed_tools(values: &[String]) -> Result<Option<AllowedToolSet>, String> {
    if values.is_empty() {
        return Ok(None);
    }

    let specs = mvp_tool_specs();
    let canonical_names = specs
        .iter()
        .map(|spec| spec.name.to_string())
        .collect::<Vec<_>>();
    let short_aliases = [
        ("read", "read_file"),
        ("write", "write_file"),
        ("edit", "edit_file"),
        ("glob", "glob_search"),
        ("grep", "grep_search"),
    ]
    .into_iter()
    .map(|(alias, canonical)| (alias.to_string(), canonical.to_string()))
    .collect::<BTreeMap<_, _>>();

    let mut allowed = AllowedToolSet::new();
    for value in values {
        for token in value
            .split(|ch: char| ch == ',' || ch.is_whitespace())
            .filter(|token| !token.is_empty())
        {
            let normalized = normalize_tool_name(token);
            let canonical = short_aliases
                .get(&normalized)
                .cloned()
                .or_else(|| {
                    specs.iter()
                        .find(|spec| matches_tool_request(spec.name, token))
                        .map(|spec| spec.name.to_string())
                })
                .ok_or_else(|| {
                    format!(
                        "unsupported tool in --allowedTools: {token} (expected one of: {})",
                        canonical_names.join(", ")
                    )
                })?;
            allowed.insert(canonical);
        }
    }

    Ok(Some(allowed))
}

fn normalize_tool_name(value: &str) -> String {
    value.trim().replace('-', "_").to_ascii_lowercase()
}

fn parse_permission_mode_arg(value: &str) -> Result<PermissionMode, String> {
    normalize_permission_mode(value)
        .ok_or_else(|| {
            format!(
                "unsupported permission mode '{value}'. Use read-only, workspace-write, or danger-full-access."
            )
        })
        .map(permission_mode_from_label)
}

fn parse_system_prompt_args(
    args: &[String],
    output_format: CliOutputFormat,
) -> Result<CliAction, String> {
    let mut cwd = env::current_dir().map_err(|error| error.to_string())?;
    let mut date = crate::DEFAULT_DATE.to_string();
    let mut index = 0;

    while index < args.len() {
        match args[index].as_str() {
            "--cwd" => {
                let value = args
                    .get(index + 1)
                    .ok_or_else(|| "missing value for --cwd".to_string())?;
                cwd = PathBuf::from(value);
                index += 2;
            }
            "--date" => {
                let value = args
                    .get(index + 1)
                    .ok_or_else(|| "missing value for --date".to_string())?;
                date.clone_from(value);
                index += 2;
            }
            other => return Err(format!("unknown system-prompt option: {other}")),
        }
    }

    Ok(CliAction::PrintSystemPrompt {
        cwd,
        date,
        output_format,
    })
}

fn parse_resume_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    let session_path = args
        .first()
        .ok_or_else(|| "missing session path for --resume".to_string())
        .map(PathBuf::from)?;
    let commands = args[1..].to_vec();
    if commands
        .iter()
        .any(|command| !command.trim_start().starts_with('/'))
    {
        return Err("--resume trailing arguments must be slash commands".to_string());
    }
    Ok(CliAction::ResumeSession {
        session_path,
        commands,
        output_format,
    })
}

fn parse_optional_selector_arg(args: &[String], command: &str) -> Result<Option<String>, String> {
    match args {
        [] => Ok(None),
        [value] => Ok(Some(value.clone())),
        _ => Err(format!("{command} accepts at most one argument")),
    }
}

fn parse_no_arg_command(args: &[String], command: &str) -> Result<(), String> {
    if args.is_empty() {
        Ok(())
    } else {
        Err(format!("{command} does not accept positional arguments"))
    }
}

fn parse_selector_command(
    args: &[String],
    output_format: CliOutputFormat,
    command: &str,
    build_action: impl FnOnce(Option<String>, CliOutputFormat) -> CliAction,
) -> Result<CliAction, String> {
    Ok(build_action(
        parse_optional_selector_arg(args, command)?,
        output_format,
    ))
}

fn parse_no_arg_output_command(
    args: &[String],
    output_format: CliOutputFormat,
    command: &str,
    build_action: impl FnOnce(CliOutputFormat) -> CliAction,
) -> Result<CliAction, String> {
    parse_no_arg_command(args, command)?;
    Ok(build_action(output_format))
}

fn parse_config_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "config", |section, output_format| {
        CliAction::Config {
            section,
            output_format,
        }
    })
}

fn parse_hooks_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "hooks", |event, output_format| {
        CliAction::Hooks {
            event,
            output_format,
        }
    })
}

fn parse_mcp_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "mcp", |server, output_format| {
        CliAction::Mcp {
            server,
            output_format,
        }
    })
}

fn parse_memory_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_no_arg_output_command(args, output_format, "memory", |output_format| {
        CliAction::Memory { output_format }
    })
}

fn parse_agents_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "agents", |agent, output_format| {
        CliAction::Agents {
            agent,
            output_format,
        }
    })
}

fn parse_plugin_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "plugin", |surface, output_format| {
        CliAction::Plugin {
            surface,
            output_format,
        }
    })
}

fn parse_reload_plugins_args(
    args: &[String],
    output_format: CliOutputFormat,
) -> Result<CliAction, String> {
    parse_no_arg_output_command(args, output_format, "reload-plugins", |output_format| {
        CliAction::ReloadPlugins { output_format }
    })
}

fn parse_remote_env_args(
    args: &[String],
    output_format: CliOutputFormat,
) -> Result<CliAction, String> {
    parse_no_arg_output_command(args, output_format, "remote-env", |output_format| {
        CliAction::RemoteEnv { output_format }
    })
}

fn parse_remote_setup_args(
    args: &[String],
    output_format: CliOutputFormat,
) -> Result<CliAction, String> {
    parse_no_arg_output_command(args, output_format, "remote-setup", |output_format| {
        CliAction::RemoteSetup { output_format }
    })
}

fn parse_tools_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "tools", |tool, output_format| {
        CliAction::Tools {
            tool,
            output_format,
        }
    })
}

fn parse_doctor_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_no_arg_output_command(args, output_format, "doctor", |output_format| {
        CliAction::Doctor { output_format }
    })
}

fn parse_skills_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "skills", |skill, output_format| {
        CliAction::Skills {
            skill,
            output_format,
        }
    })
}

fn parse_tasks_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "tasks", |task, output_format| {
        CliAction::Tasks {
            task,
            output_format,
        }
    })
}

fn parse_export_args(args: &[String], output_format: CliOutputFormat) -> Result<CliAction, String> {
    parse_selector_command(args, output_format, "export", |path, output_format| {
        CliAction::Export {
            path,
            output_format,
        }
    })
}

fn parse_session_args(
    args: &[String],
    output_format: CliOutputFormat,
) -> Result<CliAction, String> {
    match args {
        [] => Ok(CliAction::Session {
            action: None,
            target: None,
            output_format,
        }),
        [action] => Ok(CliAction::Session {
            action: Some(action.clone()),
            target: None,
            output_format,
        }),
        [action, target] => Ok(CliAction::Session {
            action: Some(action.clone()),
            target: Some(target.clone()),
            output_format,
        }),
        _ => Err("session accepts at most two positional arguments".to_string()),
    }
}
