use std::collections::BTreeMap;
use std::env;
use std::io;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::time::{SystemTime, UNIX_EPOCH};

use crate::args::brand_model_name;
use commands::render_slash_command_help;
use compat_harness::{
    load_plugin_catalog_from_cwd, load_plugin_surface_from_cwd, load_remote_catalog_from_cwd,
    load_remote_command_from_cwd, load_tool_catalog_from_cwd, load_tool_family_from_cwd,
    ArchivedToolFamilySummary, PluginCatalog, PluginSurfaceKind, PluginSurfaceSummary,
    RemoteCatalog, RemoteCommandSummary, ToolCatalog,
};
use runtime::{
    credentials_path, inherited_upstream_proxy_env, load_oauth_credentials,
    mcp_client_transport_display_name, mcp_server_auth_status, mcp_transport_display_name,
    ConfigSource, ContentBlock, McpClientAuth, McpClientBootstrap, McpClientTransport,
    McpServerAuthStatusSnapshot, ProjectContext, RemoteSessionContext, ResolvedPermissionMode,
    Session, TokenUsage, UpstreamProxyBootstrap,
};
use tools::{
    list_agent_profiles, list_agent_tasks, list_skills, load_agent_profile, load_agent_task,
    load_skill, mvp_tool_specs, AgentTaskSummary, LoadedAgentProfile, LoadedAgentTask, LoadedSkill,
    SkillSummary, ToolSpec,
};

#[derive(Debug, Clone)]
pub(crate) struct StatusContext {
    pub(crate) cwd: PathBuf,
    pub(crate) session_path: Option<PathBuf>,
    pub(crate) loaded_config_files: usize,
    pub(crate) discovered_config_files: usize,
    pub(crate) memory_file_count: usize,
    pub(crate) project_root: Option<PathBuf>,
    pub(crate) git_branch: Option<String>,
}

#[derive(Debug, Clone, Copy)]
pub(crate) struct StatusUsage {
    pub(crate) message_count: usize,
    pub(crate) turns: u32,
    pub(crate) latest: TokenUsage,
    pub(crate) cumulative: TokenUsage,
    pub(crate) estimated_tokens: usize,
}

#[derive(Debug, Clone)]
pub(crate) struct DoctorSnapshot {
    pub(crate) rust_status: &'static str,
    pub(crate) working_directory: String,
    pub(crate) project_root: Option<String>,
    pub(crate) git_branch: Option<String>,
    pub(crate) instruction_file_count: usize,
    pub(crate) issue_count: usize,
    pub(crate) issues: Vec<String>,
    pub(crate) config: DoctorConfigSnapshot,
    pub(crate) auth: DoctorAuthSnapshot,
    pub(crate) hooks: DoctorHooksSnapshot,
    pub(crate) mcp: DoctorMcpSnapshot,
    pub(crate) remote: DoctorRemoteSnapshot,
}

#[derive(Debug, Clone)]
pub(crate) struct DoctorConfigSnapshot {
    pub(crate) status: String,
    pub(crate) discovered_file_count: usize,
    pub(crate) loaded_file_count: usize,
    pub(crate) error: Option<String>,
    pub(crate) model: Option<String>,
    pub(crate) permission_mode: Option<String>,
    pub(crate) sandbox: Option<DoctorSandboxSnapshot>,
}

#[derive(Debug, Clone)]
pub(crate) struct DoctorSandboxSnapshot {
    pub(crate) enabled: bool,
    pub(crate) active: bool,
    pub(crate) filesystem_mode: String,
    pub(crate) network_isolation: bool,
    pub(crate) detail: Option<String>,
}

#[derive(Debug, Clone)]
pub(crate) struct DoctorAuthSnapshot {
    pub(crate) oauth_configured: Option<bool>,
    pub(crate) credentials_path: String,
    pub(crate) stored_credentials_status: String,
    pub(crate) refresh_token_present: Option<bool>,
    pub(crate) expires_at: Option<u64>,
    pub(crate) scopes: Option<Vec<String>>,
    pub(crate) load_error: Option<String>,
}

#[derive(Debug, Clone)]
pub(crate) struct DoctorHooksSnapshot {
    pub(crate) pre_count: Option<usize>,
    pub(crate) post_count: Option<usize>,
}

#[derive(Debug, Clone)]
pub(crate) struct DoctorMcpSnapshot {
    pub(crate) collection: Option<McpCollectionSnapshot>,
}

#[derive(Debug, Clone)]
pub(crate) struct McpBlockedServerSnapshot {
    pub(crate) name: String,
    pub(crate) transport: &'static str,
    pub(crate) detail: String,
}

#[derive(Debug, Clone)]
pub(crate) struct DoctorRemoteSnapshot {
    pub(crate) enabled: bool,
    pub(crate) proxy_ready: bool,
    pub(crate) session_id: Option<String>,
    pub(crate) base_url: Option<String>,
    pub(crate) missing_requirements: Vec<String>,
}

#[derive(Debug, Clone)]
pub(crate) struct ConfigReportSnapshot {
    pub(crate) working_directory: String,
    pub(crate) loaded_file_count: usize,
    pub(crate) merged_key_count: usize,
    pub(crate) discovered_files: Vec<ConfigDiscoveredFileSnapshot>,
    pub(crate) requested_section: Option<String>,
    pub(crate) section_supported: bool,
    pub(crate) section_has_value: bool,
    pub(crate) section_value_rendered: Option<String>,
    pub(crate) merged_json_rendered: Option<String>,
}

#[derive(Debug, Clone)]
pub(crate) struct ConfigDiscoveredFileSnapshot {
    pub(crate) source: &'static str,
    pub(crate) status: &'static str,
    pub(crate) path: String,
}

#[derive(Debug, Clone)]
pub(crate) struct HooksReportSnapshot {
    pub(crate) selected_event: Option<HookEventSnapshot>,
    pub(crate) pre_commands: Vec<String>,
    pub(crate) post_commands: Vec<String>,
}

#[derive(Debug, Clone)]
pub(crate) struct HookEventSnapshot {
    pub(crate) requested: String,
    pub(crate) label: &'static str,
    pub(crate) commands: Vec<String>,
}

#[derive(Debug, Clone, Default)]
pub(crate) struct McpCollectionSnapshot {
    pub(crate) server_count: usize,
    pub(crate) transport_counts: BTreeMap<String, usize>,
    pub(crate) supported_execution_count: usize,
    pub(crate) unsupported_execution_count: usize,
    pub(crate) status_counts: BTreeMap<String, usize>,
    pub(crate) unsupported_servers: Vec<McpBlockedServerSnapshot>,
    pub(crate) attention_servers: Vec<McpAttentionSnapshot>,
}

#[derive(Debug, Clone)]
pub(crate) struct McpReportSnapshot {
    pub(crate) selected_server: Option<McpServerSnapshot>,
    pub(crate) collection: McpCollectionSnapshot,
    pub(crate) servers: Vec<McpServerSnapshot>,
}

#[derive(Debug, Clone)]
pub(crate) struct McpAttentionSnapshot {
    pub(crate) name: String,
    pub(crate) transport: &'static str,
    pub(crate) status: String,
    pub(crate) detail: Option<String>,
}

#[derive(Debug, Clone)]
pub(crate) struct McpServerSnapshot {
    pub(crate) name: String,
    pub(crate) scope: &'static str,
    pub(crate) transport: &'static str,
    pub(crate) target: String,
    pub(crate) normalized_name: String,
    pub(crate) tool_prefix: String,
    pub(crate) signature: Option<String>,
    pub(crate) supported_execution: bool,
    pub(crate) execution_detail: Option<String>,
    pub(crate) runtime: McpServerAuthStatusSnapshot,
    pub(crate) detail: McpServerDetailSnapshot,
}

#[derive(Debug, Clone)]
pub(crate) enum McpServerDetailSnapshot {
    Stdio {
        command: String,
        args: Vec<String>,
        env_var_count: usize,
    },
    HttpLike {
        target: String,
        auth: &'static str,
        headers_count: usize,
        headers_helper: Option<String>,
    },
    Sdk {
        name: String,
    },
    SimcoeAiProxy {
        target: String,
        proxy_id: String,
    },
}

#[derive(Debug, Clone)]
pub(crate) struct MemoryReportSnapshot {
    pub(crate) working_directory: String,
    pub(crate) instruction_files: Vec<MemoryInstructionFileSnapshot>,
}

#[derive(Debug, Clone)]
pub(crate) struct MemoryInstructionFileSnapshot {
    pub(crate) path: String,
    pub(crate) line_count: usize,
    pub(crate) preview: String,
}

#[derive(Debug, Clone)]
pub(crate) struct AgentsReportSnapshot {
    pub(crate) selected_profile: Option<LoadedAgentProfile>,
    pub(crate) selected_task_counts: Option<TaskStatusCountsSnapshot>,
    pub(crate) selected_recent_tasks: Vec<AgentTaskSummary>,
    pub(crate) profiles: Vec<AgentProfileListEntrySnapshot>,
    pub(crate) persisted_task_count: usize,
}

#[derive(Debug, Clone)]
pub(crate) struct AgentProfileListEntrySnapshot {
    pub(crate) name: String,
    pub(crate) description: String,
    pub(crate) aliases: Vec<String>,
    pub(crate) tool_count: usize,
    pub(crate) recent_task_count: usize,
}

#[derive(Debug, Clone)]
pub(crate) struct SkillsReportSnapshot {
    pub(crate) selected_skill: Option<LoadedSkill>,
    pub(crate) skills: Vec<SkillSummary>,
}

#[derive(Debug, Clone)]
pub(crate) struct TasksReportSnapshot {
    pub(crate) selected_task: Option<LoadedAgentTask>,
    pub(crate) task_counts: Option<TaskStatusCountsSnapshot>,
    pub(crate) tasks: Vec<AgentTaskSummary>,
}

#[derive(Debug, Clone)]
pub(crate) struct ToolsReportSnapshot {
    pub(crate) requested_tool: Option<String>,
    pub(crate) selected_rust_tool: Option<ToolSpec>,
    pub(crate) selected_archived_family: Option<ArchivedToolFamilySummary>,
    pub(crate) rust_tools: Vec<ToolSpec>,
    pub(crate) archived_catalog: Option<ToolCatalog>,
}

#[derive(Debug, Clone)]
pub(crate) struct PluginReportSnapshot {
    pub(crate) selected_surface: Option<PluginSurfaceSummary>,
    pub(crate) catalog: Option<PluginCatalog>,
}

#[derive(Debug, Clone)]
pub(crate) struct ReloadPluginsReportSnapshot {
    pub(crate) catalog: PluginCatalog,
    pub(crate) surface: PluginSurfaceSummary,
}

#[derive(Debug, Clone)]
pub(crate) struct RemoteEnvReportSnapshot {
    pub(crate) remote: RemoteSessionContext,
    pub(crate) bootstrap: UpstreamProxyBootstrap,
    pub(crate) inherited_proxy_env_keys: Vec<String>,
}

#[derive(Debug, Clone)]
pub(crate) struct RemoteSetupReportSnapshot {
    pub(crate) env: RemoteEnvReportSnapshot,
    pub(crate) catalog: RemoteCatalog,
    pub(crate) command: RemoteCommandSummary,
}

#[derive(Debug, Clone, Copy, Default)]
pub(crate) struct TaskStatusCountsSnapshot {
    pub(crate) running: usize,
    pub(crate) completed: usize,
    pub(crate) failed: usize,
}

pub(crate) fn format_model_report(model: &str, message_count: usize, turns: u32) -> String {
    format!(
        "Model
  Current model    {model}
  Session messages {message_count}
  Session turns    {turns}

Usage
  Inspect current model with /model
    Switch models with /model <name>",
        model = brand_model_name(model),
        message_count = message_count,
        turns = turns,
    )
}

pub(crate) fn format_model_switch_report(
    previous: &str,
    next: &str,
    message_count: usize,
) -> String {
    format!(
        "Model updated
  Previous         {previous}
  Current          {next}
  Preserved msgs   {message_count}",
        previous = brand_model_name(previous),
        next = brand_model_name(next),
        message_count = message_count,
    )
}

pub(crate) fn format_permissions_report(mode: &str) -> String {
    let modes = [
        ("read-only", "Read/search tools only", mode == "read-only"),
        (
            "workspace-write",
            "Edit files inside the workspace",
            mode == "workspace-write",
        ),
        (
            "danger-full-access",
            "Unrestricted tool access",
            mode == "danger-full-access",
        ),
    ]
    .into_iter()
    .map(|(name, description, is_current)| {
        let marker = if is_current {
            "● current"
        } else {
            "○ available"
        };
        format!("  {name:<18} {marker:<11} {description}")
    })
    .collect::<Vec<_>>()
    .join("\n");

    format!(
        "Permissions
  Active mode      {mode}
  Mode status      live session default

Modes
{modes}

Usage
  Inspect current mode with /permissions
  Switch modes with /permissions <mode>"
    )
}

pub(crate) fn format_permissions_switch_report(previous: &str, next: &str) -> String {
    format!(
        "Permissions updated
  Result           mode switched
  Previous mode    {previous}
  Active mode      {next}
  Applies to       subsequent tool calls
  Usage            /permissions to inspect current mode"
    )
}

pub(crate) fn format_cost_report(usage: TokenUsage) -> String {
    format!(
        "Cost
  Input tokens     {}
  Output tokens    {}
  Cache create     {}
  Cache read       {}
  Total tokens     {}",
        usage.input_tokens,
        usage.output_tokens,
        usage.cache_creation_input_tokens,
        usage.cache_read_input_tokens,
        usage.total_tokens(),
    )
}

pub(crate) fn format_resume_report(session_path: &str, message_count: usize, turns: u32) -> String {
    format!(
        "Session resumed
  Session file     {session_path}
  Messages         {message_count}
  Turns            {turns}"
    )
}

pub(crate) fn format_compact_report(
    removed: usize,
    resulting_messages: usize,
    skipped: bool,
) -> String {
    if skipped {
        format!(
            "Compact
  Result           skipped
  Reason           session below compaction threshold
  Messages kept    {resulting_messages}"
        )
    } else {
        format!(
            "Compact
  Result           compacted
  Messages removed {removed}
  Messages kept    {resulting_messages}"
        )
    }
}

pub(crate) fn format_auto_compaction_notice(removed: usize) -> String {
    format!("[auto-compacted: removed {removed} messages]")
}

pub(crate) fn render_repl_help() -> String {
    [
        "REPL".to_string(),
        "  /exit                Quit the REPL".to_string(),
        "  /quit                Quit the REPL".to_string(),
        "  Up/Down              Navigate prompt history".to_string(),
        "  Tab                  Complete slash commands".to_string(),
        "  Ctrl-C               Clear input (or exit on empty prompt)".to_string(),
        "  Shift+Enter/Ctrl+J   Insert a newline".to_string(),
        String::new(),
        render_slash_command_help(),
    ]
    .join("\n")
}

fn trimmed_non_empty(value: Option<&str>) -> Option<&str> {
    value.map(str::trim).filter(|value| !value.is_empty())
}

fn not_found_io_error(error: impl Into<Box<dyn std::error::Error + Send + Sync>>) -> io::Error {
    io::Error::new(io::ErrorKind::NotFound, error)
}

fn render_snapshot_report<Snapshot>(
    load_snapshot: impl FnOnce() -> Result<Snapshot, Box<dyn std::error::Error>>,
    render_snapshot: impl FnOnce(&Snapshot) -> String,
) -> Result<String, Box<dyn std::error::Error>> {
    let snapshot = load_snapshot()?;
    Ok(render_snapshot(&snapshot))
}

fn render_fallible_snapshot_report<Snapshot>(
    load_snapshot: impl FnOnce() -> Result<Snapshot, Box<dyn std::error::Error>>,
    render_snapshot: impl FnOnce(&Snapshot) -> Result<String, Box<dyn std::error::Error>>,
) -> Result<String, Box<dyn std::error::Error>> {
    let snapshot = load_snapshot()?;
    render_snapshot(&snapshot)
}

pub(crate) fn status_context(
    session_path: Option<&Path>,
) -> Result<StatusContext, Box<dyn std::error::Error>> {
    let (cwd, loader) = crate::config_loader_in_current_dir()?;
    let discovered_config_files = loader.discover().len();
    let runtime_config = loader.load()?;
    let project_context = ProjectContext::discover_with_git(&cwd, crate::DEFAULT_DATE)?;
    let (project_root, git_branch) =
        crate::parse_git_status_metadata(project_context.git_status.as_deref());
    Ok(StatusContext {
        cwd,
        session_path: session_path.map(Path::to_path_buf),
        loaded_config_files: runtime_config.loaded_entries().len(),
        discovered_config_files,
        memory_file_count: project_context.instruction_files.len(),
        project_root,
        git_branch,
    })
}

pub(crate) fn format_status_report(
    model: &str,
    usage: StatusUsage,
    permission_mode: &str,
    context: &StatusContext,
) -> String {
    [
        format!(
            "Status
  Model            {model}
  Permission mode  {permission_mode}
  Messages         {}
  Turns            {}
  Estimated tokens {}",
            usage.message_count,
            usage.turns,
            usage.estimated_tokens,
            model = brand_model_name(model),
        ),
        format!(
            "Usage
  Latest total     {}
  Cumulative input {}
  Cumulative output {}
  Cumulative total {}",
            usage.latest.total_tokens(),
            usage.cumulative.input_tokens,
            usage.cumulative.output_tokens,
            usage.cumulative.total_tokens(),
        ),
        format!(
            "Workspace
  Cwd              {}
  Project root     {}
  Git branch       {}
  Session          {}
  Config files     loaded {}/{}
  Memory files     {}",
            context.cwd.display(),
            context
                .project_root
                .as_ref()
                .map_or_else(|| "unknown".to_string(), |path| path.display().to_string()),
            context.git_branch.as_deref().unwrap_or("unknown"),
            context.session_path.as_ref().map_or_else(
                || "live-repl".to_string(),
                |path| path.display().to_string()
            ),
            context.loaded_config_files,
            context.discovered_config_files,
            context.memory_file_count,
        ),
    ]
    .join("\n\n")
}

pub(crate) fn config_report_snapshot(
    section: Option<&str>,
) -> Result<ConfigReportSnapshot, Box<dyn std::error::Error>> {
    let (cwd, loader) = crate::config_loader_in_current_dir()?;
    let discovered = loader.discover();
    let runtime_config = loader.load()?;

    let loaded_paths = runtime_config
        .loaded_entries()
        .iter()
        .map(|entry| entry.path.clone())
        .collect::<Vec<_>>();
    let discovered_files = discovered
        .into_iter()
        .map(|entry| ConfigDiscoveredFileSnapshot {
            source: config_source_label(entry.source),
            status: if loaded_paths.iter().any(|loaded| loaded == &entry.path) {
                "loaded"
            } else {
                "missing"
            },
            path: entry.path.display().to_string(),
        })
        .collect::<Vec<_>>();
    let requested_section = trimmed_non_empty(section).map(str::to_string);
    let include_merged_json = requested_section.is_none();
    let mut section_supported = false;
    let mut section_has_value = false;
    let mut section_value_rendered = None;

    if let Some(requested) = requested_section.as_deref() {
        let value = match requested {
            "env" => {
                section_supported = true;
                runtime_config.get("env")
            }
            "hooks" => {
                section_supported = true;
                runtime_config.get("hooks")
            }
            "model" => {
                section_supported = true;
                runtime_config.get("model")
            }
            _ => None,
        };
        if let Some(value) = value {
            section_has_value = true;
            section_value_rendered = Some(value.render());
        }
    }

    Ok(ConfigReportSnapshot {
        working_directory: cwd.display().to_string(),
        loaded_file_count: runtime_config.loaded_entries().len(),
        merged_key_count: runtime_config.merged().len(),
        discovered_files,
        requested_section,
        section_supported,
        section_has_value,
        section_value_rendered,
        merged_json_rendered: if include_merged_json {
            Some(runtime_config.as_json().render())
        } else {
            None
        },
    })
}

pub(crate) fn render_config_report_from_snapshot(snapshot: &ConfigReportSnapshot) -> String {
    let mut lines = vec![
        format!(
            "Config
  Working directory {}
  Loaded files      {}
  Merged keys       {}",
            snapshot.working_directory, snapshot.loaded_file_count, snapshot.merged_key_count,
        ),
        "Discovered files".to_string(),
    ];
    for entry in &snapshot.discovered_files {
        lines.push(format!(
            "  {source:<7} {status:<7} {path}",
            source = entry.source,
            status = entry.status,
            path = entry.path,
        ));
    }

    if let Some(section) = snapshot.requested_section.as_deref() {
        lines.push(format!("Merged section: {section}"));
        if !snapshot.section_supported {
            lines.push(format!(
                "  Unsupported config section '{section}'. Use env, hooks, or model."
            ));
            return lines.join("\n");
        }
        lines.push(format!(
            "  {}",
            snapshot
                .section_value_rendered
                .as_deref()
                .unwrap_or("<unset>"),
        ));
        return lines.join("\n");
    }

    lines.push("Merged JSON".to_string());
    lines.push(format!(
        "  {}",
        snapshot.merged_json_rendered.as_deref().unwrap_or("{}"),
    ));
    lines.join("\n")
}

pub(crate) fn render_config_report(
    section: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        || config_report_snapshot(section),
        render_config_report_from_snapshot,
    )
}

pub(crate) fn hooks_report_snapshot(
    event: Option<&str>,
) -> Result<HooksReportSnapshot, Box<dyn std::error::Error>> {
    let (_, loader) = crate::config_loader_in_current_dir()?;
    let runtime_config = loader.load()?;
    let hooks = runtime_config.hooks();
    let pre_commands = hooks.pre_tool_use().to_vec();
    let post_commands = hooks.post_tool_use().to_vec();
    let selected_event = if let Some(requested) = trimmed_non_empty(event) {
        let selection = parse_hook_selection(requested).ok_or_else(|| {
            io::Error::new(
                io::ErrorKind::InvalidInput,
                format!("unsupported hooks selector '{requested}'. Use pre or post."),
            )
        })?;
        let (label, commands) = match selection {
            HookSelection::Pre => ("PreToolUse", pre_commands.clone()),
            HookSelection::Post => ("PostToolUse", post_commands.clone()),
        };
        Some(HookEventSnapshot {
            requested: requested.to_string(),
            label,
            commands,
        })
    } else {
        None
    };

    Ok(HooksReportSnapshot {
        selected_event,
        pre_commands,
        post_commands,
    })
}

pub(crate) fn render_hooks_report_from_snapshot(snapshot: &HooksReportSnapshot) -> String {
    if let Some(event) = snapshot.selected_event.as_ref() {
        return format!(
            "Hooks\n  Event             {label}\n  Configured        {configured}\n  Usage             /hooks\n  Runtime           exit 2 denies, other non-zero exits warn\n\nCommands\n{commands}",
            label = event.label,
            configured = event.commands.len(),
            commands = render_hook_command_entries(&event.commands),
        );
    }

    if snapshot.pre_commands.is_empty() && snapshot.post_commands.is_empty() {
        return String::from(
            "Hooks\n  Pre-tool hooks    0\n  Post-tool hooks   0\n  Usage             /hooks [pre|post]\n  Runtime           exit 2 denies, other non-zero exits warn\n  Detail            no hooks configured",
        );
    }

    let mut lines = vec![format!(
        "Hooks\n  Pre-tool hooks    {}\n  Post-tool hooks   {}\n  Usage             /hooks [pre|post]\n  Runtime           exit 2 denies, other non-zero exits warn",
        snapshot.pre_commands.len(),
        snapshot.post_commands.len(),
    )];

    if !snapshot.pre_commands.is_empty() {
        lines.push(String::new());
        lines.push(String::from("PreToolUse"));
        lines.push(render_hook_command_entries(&snapshot.pre_commands));
    }

    if !snapshot.post_commands.is_empty() {
        lines.push(String::new());
        lines.push(String::from("PostToolUse"));
        lines.push(render_hook_command_entries(&snapshot.post_commands));
    }

    lines.join("\n")
}

pub(crate) fn render_hooks_report(
    event: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        || hooks_report_snapshot(event),
        render_hooks_report_from_snapshot,
    )
}

pub(crate) fn memory_report_snapshot() -> Result<MemoryReportSnapshot, Box<dyn std::error::Error>> {
    let cwd = crate::current_working_directory()?;
    let project_context = ProjectContext::discover(&cwd, crate::DEFAULT_DATE)?;

    Ok(MemoryReportSnapshot {
        working_directory: cwd.display().to_string(),
        instruction_files: project_context
            .instruction_files
            .iter()
            .map(|file| {
                let preview = file.content.lines().next().unwrap_or("").trim();
                let preview = if preview.is_empty() {
                    "<empty>"
                } else {
                    preview
                };
                MemoryInstructionFileSnapshot {
                    path: file.path.display().to_string(),
                    line_count: file.content.lines().count(),
                    preview: preview.to_string(),
                }
            })
            .collect(),
    })
}

pub(crate) fn render_memory_report_from_snapshot(snapshot: &MemoryReportSnapshot) -> String {
    let mut lines = vec![format!(
        "Memory
  Working directory {}
  Instruction files {}",
        snapshot.working_directory,
        snapshot.instruction_files.len()
    )];
    if snapshot.instruction_files.is_empty() {
        lines.push("Discovered files".to_string());
        lines.push(
            "  No SIMCOE instruction files discovered in the current directory ancestry."
                .to_string(),
        );
    } else {
        lines.push("Discovered files".to_string());
        for (index, file) in snapshot.instruction_files.iter().enumerate() {
            lines.push(format!("  {}. {}", index + 1, file.path));
            lines.push(format!(
                "     lines={} preview={}",
                file.line_count, file.preview
            ));
        }
    }
    lines.join("\n")
}

pub(crate) fn render_memory_report() -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(memory_report_snapshot, render_memory_report_from_snapshot)
}

pub(crate) fn mcp_report_snapshot(
    server: Option<&str>,
) -> Result<McpReportSnapshot, Box<dyn std::error::Error>> {
    let (_, loader) = crate::config_loader_in_current_dir()?;
    let runtime_config = loader.load()?;
    let servers = runtime_config.mcp().servers();
    let requested = trimmed_non_empty(server);

    if let Some(requested) = requested {
        let (name, config) = servers
            .iter()
            .find(|(name, _)| name.eq_ignore_ascii_case(requested))
            .ok_or_else(|| not_found_io_error(format!("unknown MCP server: {requested}")))?;
        let bootstrap = McpClientBootstrap::from_scoped_config(name, config);
        return Ok(McpReportSnapshot {
            selected_server: Some(mcp_server_snapshot(name, config, &bootstrap)?),
            collection: McpCollectionSnapshot::default(),
            servers: Vec::new(),
        });
    }

    let (collection, servers) = mcp_collection_snapshot(servers)?;
    Ok(McpReportSnapshot {
        selected_server: None,
        collection,
        servers,
    })
}

fn mcp_collection_snapshot(
    servers: &BTreeMap<String, runtime::ScopedMcpServerConfig>,
) -> io::Result<(McpCollectionSnapshot, Vec<McpServerSnapshot>)> {
    let server_snapshots = mcp_server_snapshots(servers)?;
    let attention_servers = mcp_attention_servers(&server_snapshots);

    Ok((
        McpCollectionSnapshot {
            server_count: servers.len(),
            transport_counts: mcp_transport_counts(servers),
            supported_execution_count: server_snapshots
                .iter()
                .filter(|server| server.supported_execution)
                .count(),
            unsupported_execution_count: server_snapshots
                .iter()
                .filter(|server| !server.supported_execution)
                .count(),
            status_counts: mcp_status_counts(&server_snapshots),
            unsupported_servers: mcp_blocked_servers(&attention_servers),
            attention_servers,
        },
        server_snapshots,
    ))
}

fn mcp_server_snapshots(
    servers: &BTreeMap<String, runtime::ScopedMcpServerConfig>,
) -> io::Result<Vec<McpServerSnapshot>> {
    servers
        .iter()
        .map(|(name, config)| {
            let bootstrap = McpClientBootstrap::from_scoped_config(name, config);
            mcp_server_snapshot(name, config, &bootstrap)
        })
        .collect()
}

pub(crate) fn render_mcp_report_from_snapshot(snapshot: &McpReportSnapshot) -> String {
    if let Some(server) = snapshot.selected_server.as_ref() {
        return render_mcp_server_detail(server);
    }

    if snapshot.servers.is_empty() {
        return String::from(
            "MCP\n  Configured servers 0\n  Usage             /mcp <server>\n  Detail            no MCP servers configured",
        );
    }

    let name_width = snapshot
        .servers
        .iter()
        .map(|server| server.name.len())
        .max()
        .unwrap_or(6)
        + 2;
    let entries = snapshot
        .servers
        .iter()
        .map(|server| {
            format!(
                "  {name:<name_width$}{scope:<8}{transport:<14}{status:<24}{executable:<6}{target}",
                name = server.name,
                name_width = name_width,
                scope = server.scope,
                transport = server.transport,
                status = server.runtime.status,
                executable = yes_no(server.supported_execution),
                target = server.target,
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    let transport_counts =
        summarize_recorded_mcp_transports(Some(&snapshot.collection.transport_counts));
    let status_counts = summarize_doctor_mcp_statuses(Some(&snapshot.collection.status_counts));
    let blockers = summarize_mcp_blockers(Some(&snapshot.collection.unsupported_servers));
    let attention = snapshot
        .collection
        .attention_servers
        .iter()
        .map(|server| format!("{} ({})", server.name, server.status))
        .collect::<Vec<_>>();
    let attention = if attention.is_empty() {
        String::from("<none>")
    } else {
        attention.join(", ")
    };

    format!(
        "MCP\n  Configured servers {}\n  Transports        {}\n  Executable now    {}\n  Blocked now       {}\n  Status counts     {}\n  Blockers          {}\n  Attention         {}\n  Usage             /mcp <server>\n\nServers\n{}",
        snapshot.collection.server_count,
        transport_counts,
        snapshot.collection.supported_execution_count,
        snapshot.collection.unsupported_execution_count,
        status_counts,
        blockers,
        attention,
        entries,
    )
}

pub(crate) fn render_mcp_report(
    server: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        || mcp_report_snapshot(server),
        render_mcp_report_from_snapshot,
    )
}

fn task_status_counts(tasks: &[AgentTaskSummary]) -> TaskStatusCountsSnapshot {
    TaskStatusCountsSnapshot {
        running: tasks.iter().filter(|task| task.status == "running").count(),
        completed: tasks
            .iter()
            .filter(|task| task.status == "completed")
            .count(),
        failed: tasks.iter().filter(|task| task.status == "failed").count(),
    }
}

pub(crate) fn agents_report_snapshot(
    agent: Option<&str>,
) -> Result<AgentsReportSnapshot, Box<dyn std::error::Error>> {
    let requested = trimmed_non_empty(agent);
    let tasks = list_agent_tasks().map_err(io::Error::other)?;

    if let Some(requested) = requested {
        let profile = load_agent_profile(requested).map_err(not_found_io_error)?;
        let matching_tasks = tasks
            .into_iter()
            .filter(|task| task.subagent_type.as_deref() == Some(profile.name.as_str()))
            .collect::<Vec<_>>();
        return Ok(AgentsReportSnapshot {
            selected_profile: Some(profile),
            selected_task_counts: Some(task_status_counts(&matching_tasks)),
            selected_recent_tasks: matching_tasks.into_iter().take(5).collect(),
            profiles: Vec::new(),
            persisted_task_count: 0,
        });
    }

    let profiles = list_agent_profiles();
    Ok(AgentsReportSnapshot {
        selected_profile: None,
        selected_task_counts: None,
        selected_recent_tasks: Vec::new(),
        profiles: profiles
            .into_iter()
            .map(|profile| AgentProfileListEntrySnapshot {
                recent_task_count: tasks
                    .iter()
                    .filter(|task| task.subagent_type.as_deref() == Some(profile.name.as_str()))
                    .count(),
                name: profile.name,
                description: profile.description,
                aliases: profile.aliases,
                tool_count: profile.tool_count,
            })
            .collect(),
        persisted_task_count: tasks.len(),
    })
}

pub(crate) fn render_agents_report_from_snapshot(snapshot: &AgentsReportSnapshot) -> String {
    if let Some(profile) = snapshot.selected_profile.as_ref() {
        let counts = snapshot.selected_task_counts.unwrap_or_default();
        let aliases = if profile.aliases.is_empty() {
            String::from("<none>")
        } else {
            profile.aliases.join(", ")
        };
        let tools = profile
            .tools
            .iter()
            .enumerate()
            .map(|(index, tool)| format!("  {:>2}. {tool}", index + 1))
            .collect::<Vec<_>>()
            .join("\n");
        let recent_tasks = if snapshot.selected_recent_tasks.is_empty() {
            String::from("  None")
        } else {
            snapshot
                .selected_recent_tasks
                .iter()
                .map(|task| {
                    format!(
                        "  {id:<24}{status:<11}{name:<24}{created}",
                        id = task.agent_id,
                        status = task.status,
                        name = task.name,
                        created = task.created_at,
                    )
                })
                .collect::<Vec<_>>()
                .join("\n")
        };

        return format!(
            "Agent\n  Name             {name}\n  Description      {description}\n  Aliases          {aliases}\n  Allowed tools    {tool_count}\n  Running          {running}\n  Completed        {completed}\n  Failed           {failed}\n\nTools\n{tools}\n\nRecent tasks\n{recent_tasks}",
            name = profile.name,
            description = profile.description,
            aliases = aliases,
            tool_count = profile.tools.len(),
            running = counts.running,
            completed = counts.completed,
            failed = counts.failed,
            tools = tools,
            recent_tasks = recent_tasks,
        );
    }

    if snapshot.profiles.is_empty() {
        return String::from(
            "Agents\n  Available        0\n  Usage            /agents <name>\n  Detail           no built-in sub-agent profiles found",
        );
    }

    let profile_count = snapshot.profiles.len();
    let name_width = snapshot
        .profiles
        .iter()
        .map(|profile| profile.name.len())
        .max()
        .unwrap_or(6)
        + 2;
    let entries = snapshot
        .profiles
        .iter()
        .map(|profile| {
            format!(
                "  {name:<name_width$}{tool_count:>2} tools  {recent:>2} recent  {description}",
                name = profile.name,
                tool_count = profile.tool_count,
                recent = profile.recent_task_count,
                description = profile.description,
                name_width = name_width,
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    format!(
        "Agents\n  Available        {profile_count}\n  Persisted tasks  {task_count}\n  Usage            /agents <name>\n\nProfiles\n{entries}",
        task_count = snapshot.persisted_task_count,
        entries = entries,
    )
}

pub(crate) fn render_agents_report(
    agent: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        || agents_report_snapshot(agent),
        render_agents_report_from_snapshot,
    )
}

pub(crate) fn doctor_snapshot() -> Result<DoctorSnapshot, Box<dyn std::error::Error>> {
    let (cwd, loader) = crate::config_loader_in_current_dir()?;
    let discovered = loader.discover();
    let project_context = ProjectContext::discover_with_git(&cwd, crate::DEFAULT_DATE)?;
    let (project_root, git_branch) =
        crate::parse_git_status_metadata(project_context.git_status.as_deref());
    let instruction_file_count = project_context.instruction_files.len();
    let env_map = env::vars().collect::<BTreeMap<String, String>>();
    let remote = RemoteSessionContext::from_env_map(&env_map);
    let bootstrap = UpstreamProxyBootstrap::from_env_map(&env_map);

    let mut issues = Vec::new();
    if instruction_file_count == 0 {
        issues.push(String::from("no instruction files discovered"));
    }

    let credentials_path_result = credentials_path();
    let credentials_path_display = match &credentials_path_result {
        Ok(path) => path.display().to_string(),
        Err(error) => {
            issues.push(format!("oauth credentials path unavailable: {error}"));
            format!("<error: {error}>")
        }
    };

    let (stored_creds, refresh_token_present, expires_at, scopes, load_error, has_stored_creds) =
        if credentials_path_result.is_ok() {
            match load_oauth_credentials() {
                Ok(Some(token_set)) => (
                    String::from("yes"),
                    Some(token_set.refresh_token.is_some()),
                    token_set.expires_at,
                    Some(token_set.scopes),
                    None,
                    true,
                ),
                Ok(None) => (
                    String::from("no"),
                    None,
                    None,
                    Some(Vec::new()),
                    None,
                    false,
                ),
                Err(error) => {
                    issues.push(format!("failed to load oauth credentials: {error}"));
                    (
                        String::from("error"),
                        None,
                        None,
                        None,
                        Some(error.to_string()),
                        false,
                    )
                }
            }
        } else {
            (String::from("error"), None, None, None, None, false)
        };

    let missing_requirements = if remote.enabled {
        bootstrap
            .missing_requirements()
            .into_iter()
            .map(str::to_string)
            .collect::<Vec<_>>()
    } else {
        Vec::new()
    };
    if remote.enabled && !bootstrap.should_enable() {
        issues.push(format!(
            "remote bootstrap incomplete: {}",
            if missing_requirements.is_empty() {
                String::from("<none>")
            } else {
                missing_requirements.join(", ")
            }
        ));
    }

    let auth = DoctorAuthSnapshot {
        oauth_configured: None,
        credentials_path: credentials_path_display,
        stored_credentials_status: stored_creds,
        refresh_token_present,
        expires_at,
        scopes,
        load_error,
    };

    let remote_snapshot = DoctorRemoteSnapshot {
        enabled: remote.enabled,
        proxy_ready: bootstrap.should_enable(),
        session_id: remote.session_id.clone(),
        base_url: if remote.base_url.is_empty() {
            None
        } else {
            Some(remote.base_url.clone())
        },
        missing_requirements,
    };

    match loader.load() {
        Ok(runtime_config) => {
            if runtime_config.loaded_entries().is_empty() {
                issues.push(String::from("no config files loaded"));
            }

            let sandbox_status =
                runtime::sandbox::resolve_sandbox_status(runtime_config.sandbox(), &cwd);
            if sandbox_status.enabled && !sandbox_status.active {
                issues.push(match &sandbox_status.fallback_reason {
                    Some(reason) => format!("sandbox requested but inactive: {reason}"),
                    None => String::from("sandbox requested but inactive"),
                });
            }

            if runtime_config.oauth().is_some() && !has_stored_creds {
                issues.push(String::from(
                    "oauth is configured but no stored credentials were found",
                ));
            }

            let hooks = runtime_config.hooks();
            let mcp_servers = runtime_config.mcp().servers();
            let (mcp_snapshot, mcp_issues) = doctor_mcp_snapshot(mcp_servers)?;
            issues.extend(mcp_issues);

            Ok(DoctorSnapshot {
                rust_status: "inspection only",
                working_directory: cwd.display().to_string(),
                project_root: project_root.map(|path| path.display().to_string()),
                git_branch,
                instruction_file_count,
                issue_count: issues.len(),
                issues,
                config: DoctorConfigSnapshot {
                    status: String::from("ok"),
                    discovered_file_count: discovered.len(),
                    loaded_file_count: runtime_config.loaded_entries().len(),
                    error: None,
                    model: runtime_config.model().map(str::to_string),
                    permission_mode: runtime_config
                        .permission_mode()
                        .map(resolved_permission_mode_label)
                        .map(str::to_string),
                    sandbox: Some(DoctorSandboxSnapshot {
                        enabled: sandbox_status.enabled,
                        active: sandbox_status.active,
                        filesystem_mode: sandbox_status.filesystem_mode.as_str().to_string(),
                        network_isolation: sandbox_status.network_active,
                        detail: sandbox_status.fallback_reason,
                    }),
                },
                auth: DoctorAuthSnapshot {
                    oauth_configured: Some(runtime_config.oauth().is_some()),
                    ..auth
                },
                hooks: DoctorHooksSnapshot {
                    pre_count: Some(hooks.pre_tool_use().len()),
                    post_count: Some(hooks.post_tool_use().len()),
                },
                mcp: mcp_snapshot,
                remote: remote_snapshot,
            })
        }
        Err(error) => {
            let config_error = error.to_string();
            issues.push(format!("config load failed: {config_error}"));

            Ok(DoctorSnapshot {
                rust_status: "inspection only",
                working_directory: cwd.display().to_string(),
                project_root: project_root.map(|path| path.display().to_string()),
                git_branch,
                instruction_file_count,
                issue_count: issues.len(),
                issues,
                config: DoctorConfigSnapshot {
                    status: String::from("error"),
                    discovered_file_count: discovered.len(),
                    loaded_file_count: 0,
                    error: Some(config_error),
                    model: None,
                    permission_mode: None,
                    sandbox: None,
                },
                auth,
                hooks: DoctorHooksSnapshot {
                    pre_count: None,
                    post_count: None,
                },
                mcp: DoctorMcpSnapshot { collection: None },
                remote: remote_snapshot,
            })
        }
    }
}

pub(crate) fn render_doctor_report_from_snapshot(snapshot: &DoctorSnapshot) -> String {
    let project_root = snapshot.project_root.as_deref().unwrap_or("unknown");
    let git_branch = snapshot.git_branch.as_deref().unwrap_or("unknown");
    let session_id = snapshot.remote.session_id.as_deref().unwrap_or("<unset>");
    let base_url = snapshot.remote.base_url.as_deref().unwrap_or("<unset>");
    let remote_missing = if !snapshot.remote.enabled {
        String::from("<disabled>")
    } else if snapshot.remote.missing_requirements.is_empty() {
        String::from("<none>")
    } else {
        snapshot.remote.missing_requirements.join(", ")
    };

    if snapshot.config.status == "ok" {
        let sandbox = snapshot.config.sandbox.as_ref();
        let oauth_config = snapshot
            .auth
            .oauth_configured
            .map_or("<unavailable>", yes_no);
        let refresh_token = match snapshot.auth.stored_credentials_status.as_str() {
            "yes" => snapshot.auth.refresh_token_present.map_or_else(
                || String::from("<unavailable>"),
                |present| yes_no(present).to_string(),
            ),
            _ => String::from("<unavailable>"),
        };
        let expiry = match snapshot.auth.stored_credentials_status.as_str() {
            "yes" => oauth_expiry_summary(snapshot.auth.expires_at),
            "error" => snapshot.auth.load_error.as_ref().map_or_else(
                || String::from("<unavailable>"),
                |error| format!("<error: {error}>"),
            ),
            _ => String::from("<unavailable>"),
        };
        let scopes = snapshot.auth.scopes.as_ref().map_or_else(
            || String::from("<unavailable>"),
            |scopes| summarize_scopes(scopes),
        );

        return format!(
            "Doctor\n  Rust status       {rust_status}\n  Working directory {cwd}\n  Project root      {project_root}\n  Git branch        {git_branch}\n  Instruction files {instruction_files}\n  Issues            {issue_count}\n\nConfig\n  Status            ok\n  Discovered files  {discovered_files}\n  Loaded files      {loaded_files}\n  Model             {model}\n  Permission mode   {permission_mode}\n  Sandbox enabled   {sandbox_enabled}\n  Sandbox active    {sandbox_active}\n  Filesystem mode   {filesystem_mode}\n  Network isolation {network_isolation}\n  Detail            {sandbox_detail}\n\nAuth\n  OAuth config      {oauth_config}\n  Credentials path  {credentials_path}\n  Stored creds      {stored_creds}\n  Refresh token     {refresh_token}\n  Expiry            {expiry}\n  Scopes            {scopes}\n\nHooks + MCP\n  Pre hooks         {pre_hooks}\n  Post hooks        {post_hooks}\n  MCP servers       {mcp_servers}\n  MCP transports    {mcp_transports}\n  MCP executable    {mcp_executable}\n  MCP blocked       {mcp_blocked}\n  MCP statuses      {mcp_statuses}\n  MCP blockers      {mcp_blockers}\n  MCP attention     {mcp_attention}\n\nRemote\n  Enabled           {remote_enabled}\n  Proxy ready       {proxy_ready}\n  Session id        {session_id}\n  Base URL          {base_url}\n  Missing           {remote_missing}\n\nIssues\n{issue_lines}",
            rust_status = snapshot.rust_status,
            cwd = snapshot.working_directory.as_str(),
            project_root = project_root,
            git_branch = git_branch,
            instruction_files = snapshot.instruction_file_count,
            issue_count = snapshot.issue_count,
            discovered_files = snapshot.config.discovered_file_count,
            loaded_files = snapshot.config.loaded_file_count,
            model = snapshot.config.model.as_deref().unwrap_or("<unset>"),
            permission_mode = snapshot.config.permission_mode.as_deref().unwrap_or("<unset>"),
            sandbox_enabled = sandbox.map_or("<unavailable>", |value| yes_no(value.enabled)),
            sandbox_active = sandbox.map_or("<unavailable>", |value| yes_no(value.active)),
            filesystem_mode = sandbox.map_or("<unavailable>", |value| value.filesystem_mode.as_str()),
            network_isolation = sandbox.map_or("<unavailable>", |value| yes_no(value.network_isolation)),
            sandbox_detail = sandbox
                .and_then(|value| value.detail.as_deref())
                .unwrap_or("<none>"),
            oauth_config = oauth_config,
            credentials_path = snapshot.auth.credentials_path.as_str(),
            stored_creds = snapshot.auth.stored_credentials_status.as_str(),
            refresh_token = refresh_token,
            expiry = expiry,
            scopes = scopes,
            pre_hooks = snapshot.hooks.pre_count.unwrap_or_default(),
            post_hooks = snapshot.hooks.post_count.unwrap_or_default(),
            mcp_servers = snapshot.mcp.collection.as_ref().map_or(0, |collection| collection.server_count),
            mcp_transports = summarize_recorded_mcp_transports(snapshot.mcp.collection.as_ref().map(|collection| &collection.transport_counts)),
            mcp_executable = snapshot.mcp.collection.as_ref().map_or(0, |collection| collection.supported_execution_count),
            mcp_blocked = snapshot.mcp.collection.as_ref().map_or(0, |collection| collection.unsupported_execution_count),
            mcp_statuses = summarize_doctor_mcp_statuses(snapshot.mcp.collection.as_ref().map(|collection| &collection.status_counts)),
            mcp_blockers = summarize_mcp_blockers(snapshot.mcp.collection.as_ref().map(|collection| collection.unsupported_servers.as_slice())),
            mcp_attention = summarize_doctor_mcp_attention(snapshot.mcp.collection.as_ref().map(|collection| collection.attention_servers.as_slice())),
            remote_enabled = yes_no(snapshot.remote.enabled),
            proxy_ready = yes_no(snapshot.remote.proxy_ready),
            session_id = session_id,
            base_url = base_url,
            remote_missing = remote_missing,
            issue_lines = summarize_doctor_issues(&snapshot.issues),
        );
    }

    let expiry = snapshot.auth.load_error.as_ref().map_or_else(
        || String::from("<unavailable>"),
        |error| format!("<error: {error}>"),
    );
    let scopes = snapshot.auth.scopes.as_ref().map_or_else(
        || String::from("<unavailable>"),
        |scopes| summarize_scopes(scopes),
    );

    format!(
        "Doctor\n  Rust status       {rust_status}\n  Working directory {cwd}\n  Project root      {project_root}\n  Git branch        {git_branch}\n  Instruction files {instruction_files}\n  Issues            {issue_count}\n\nConfig\n  Status            error\n  Discovered files  {discovered_files}\n  Loaded files      0\n  Model             <unavailable>\n  Permission mode   <unavailable>\n  Sandbox enabled   <unavailable>\n  Sandbox active    <unavailable>\n  Filesystem mode   <unavailable>\n  Network isolation <unavailable>\n  Detail            {config_error}\n\nAuth\n  OAuth config      <unavailable>\n  Credentials path  {credentials_path}\n  Stored creds      {stored_creds}\n  Refresh token     <unavailable>\n  Expiry            {expiry}\n  Scopes            {scopes}\n\nHooks + MCP\n  Pre hooks         <unavailable>\n  Post hooks        <unavailable>\n  MCP servers       <unavailable>\n  MCP transports    <unavailable>\n  MCP executable    <unavailable>\n  MCP blocked       <unavailable>\n  MCP statuses      <unavailable>\n  MCP blockers      <unavailable>\n  MCP attention     <unavailable>\n\nRemote\n  Enabled           {remote_enabled}\n  Proxy ready       {proxy_ready}\n  Session id        {session_id}\n  Base URL          {base_url}\n  Missing           {remote_missing}\n\nIssues\n{issue_lines}",
        rust_status = snapshot.rust_status,
        cwd = snapshot.working_directory.as_str(),
        project_root = project_root,
        git_branch = git_branch,
        instruction_files = snapshot.instruction_file_count,
        issue_count = snapshot.issue_count,
        discovered_files = snapshot.config.discovered_file_count,
        config_error = snapshot.config.error.as_deref().unwrap_or("<unknown>"),
        credentials_path = snapshot.auth.credentials_path.as_str(),
        stored_creds = snapshot.auth.stored_credentials_status.as_str(),
        expiry = expiry,
        scopes = scopes,
        remote_enabled = yes_no(snapshot.remote.enabled),
        proxy_ready = yes_no(snapshot.remote.proxy_ready),
        session_id = session_id,
        base_url = base_url,
        remote_missing = remote_missing,
        issue_lines = summarize_doctor_issues(&snapshot.issues),
    )
}

pub(crate) fn render_doctor_report() -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(doctor_snapshot, render_doctor_report_from_snapshot)
}

pub(crate) fn tools_report_snapshot(
    tool: Option<&str>,
) -> Result<ToolsReportSnapshot, Box<dyn std::error::Error>> {
    let requested = trimmed_non_empty(tool).map(str::to_owned);
    let rust_tools = mvp_tool_specs();

    if let Some(requested) = requested.as_deref() {
        let rust_match = rust_tools
            .iter()
            .find(|spec| matches_tool_request(spec.name, requested));
        let archived_match = load_tool_family_from_cwd(requested).ok();

        if rust_match.is_none() && archived_match.is_none() {
            return Err(io::Error::new(
                io::ErrorKind::NotFound,
                format!("unknown Rust tool or archived tool family: {requested}"),
            )
            .into());
        }

        return Ok(ToolsReportSnapshot {
            requested_tool: Some(requested.to_string()),
            selected_rust_tool: rust_match.cloned(),
            selected_archived_family: archived_match,
            rust_tools: Vec::new(),
            archived_catalog: None,
        });
    }

    Ok(ToolsReportSnapshot {
        requested_tool: None,
        selected_rust_tool: None,
        selected_archived_family: None,
        rust_tools,
        archived_catalog: load_tool_catalog_from_cwd().ok(),
    })
}

pub(crate) fn render_tools_report_from_snapshot(
    snapshot: &ToolsReportSnapshot,
) -> Result<String, Box<dyn std::error::Error>> {
    if snapshot.selected_rust_tool.is_some() || snapshot.selected_archived_family.is_some() {
        let mut sections = Vec::new();
        if let Some(spec) = snapshot.selected_rust_tool.as_ref() {
            sections.push(render_tool_detail(spec)?);
        }
        if let Some(family) = snapshot.selected_archived_family.as_ref() {
            let source_hints = render_bulleted_items(&family.source_hints);
            sections.push(format!(
                "Archived TS family\n  Name             {name}\n  Archived files   {archived_files}\n  Summary          {summary}\n\nSource hints\n{source_hints}",
                name = family.name,
                archived_files = family.archived_file_count,
                summary = family.summary,
                source_hints = source_hints,
            ));
        }

        return Ok(sections.join("\n\n"));
    }

    let rust_width = snapshot
        .rust_tools
        .iter()
        .map(|spec| spec.name.len())
        .max()
        .unwrap_or(4)
        + 2;
    let rust_entries = snapshot
        .rust_tools
        .iter()
        .map(|spec| {
            format!(
                "  {name:<rust_width$}{mode:<20}{description}",
                name = spec.name,
                mode = spec.required_permission.as_str(),
                description = spec.description,
                rust_width = rust_width,
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    let (archived_family_count, archived_file_count, archived_entries) =
        if let Some(catalog) = snapshot.archived_catalog.as_ref() {
            let family_width = catalog
                .families
                .iter()
                .map(|family| family.name.len())
                .max()
                .unwrap_or(6)
                + 2;
            let entries = catalog
                .families
                .iter()
                .map(|family| {
                    format!(
                        "  {name:<family_width$}{count:>2} files  {summary}",
                        name = family.name,
                        count = family.archived_file_count,
                        summary = family.summary,
                        family_width = family_width,
                    )
                })
                .collect::<Vec<_>>()
                .join("\n");
            (catalog.families.len(), catalog.archived_file_count, entries)
        } else {
            (
                0,
                0,
                String::from("  Snapshot unavailable from current directory"),
            )
        };

    Ok(format!(
        "Tools\n  Rust tools         {rust_tool_count}\n  Archived families  {archived_family_count}\n  Archived files     {archived_file_count}\n  Usage              /tools <name>\n\nRust registry\n{rust_entries}\n\nArchived TS families\n{archived_entries}",
        rust_tool_count = snapshot.rust_tools.len(),
        archived_family_count = archived_family_count,
        archived_file_count = archived_file_count,
        rust_entries = rust_entries,
        archived_entries = archived_entries,
    ))
}

pub(crate) fn render_tools_report(
    tool: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    render_fallible_snapshot_report(
        || tools_report_snapshot(tool),
        render_tools_report_from_snapshot,
    )
}

pub(crate) fn plugin_report_snapshot(
    surface: Option<&str>,
) -> Result<PluginReportSnapshot, Box<dyn std::error::Error>> {
    let requested = trimmed_non_empty(surface);

    if let Some(requested) = requested {
        let surface = load_plugin_surface_from_cwd(requested).map_err(not_found_io_error)?;
        return Ok(PluginReportSnapshot {
            selected_surface: Some(surface),
            catalog: None,
        });
    }

    Ok(PluginReportSnapshot {
        selected_surface: None,
        catalog: Some(load_plugin_catalog_from_cwd()?),
    })
}

pub(crate) fn render_plugin_report_from_snapshot(
    snapshot: &PluginReportSnapshot,
) -> Result<String, Box<dyn std::error::Error>> {
    if let Some(surface) = snapshot.selected_surface.as_ref() {
        let source_hints = render_bulleted_items(&surface.source_hints);
        return Ok(format!(
            "Plugin\n  Name             {name}\n  Kind             {kind}\n  Rust status      inspection only\n  Archived files   {archived_files}\n  Summary          {summary}\n\nSource hints\n{source_hints}",
            name = surface.name,
            kind = surface.kind.as_str(),
            archived_files = surface.archived_file_count,
            summary = surface.summary,
            source_hints = source_hints,
        ));
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
    let command_width = catalog
        .surfaces
        .iter()
        .filter(|surface| matches!(surface.kind, PluginSurfaceKind::Command))
        .map(|surface| surface.name.len())
        .max()
        .unwrap_or(7)
        + 2;
    let commands = catalog
        .surfaces
        .iter()
        .filter(|surface| matches!(surface.kind, PluginSurfaceKind::Command))
        .map(|surface| {
            format!(
                "  {name:<command_width$}{count:>2} files  {summary}",
                name = surface.name,
                count = surface.archived_file_count,
                summary = surface.summary,
                command_width = command_width,
            )
        })
        .collect::<Vec<_>>()
        .join("\n");
    let modules = catalog
        .surfaces
        .iter()
        .filter(|surface| matches!(surface.kind, PluginSurfaceKind::Module))
        .map(|surface| format!("  {}", surface.source_hints.join(", ")))
        .collect::<Vec<_>>()
        .join("\n");

    Ok(format!(
        "Plugin\n  Archive           {archive}\n  Package           {package}\n  Rust status       inspection only\n  Runtime support   no plugin loader, install flow, or marketplace support\n  Archived commands {command_count}\n  Archived modules  {module_count}\n  Visible modules   {module_surface_count}\n  Usage             /plugin <name>\n\nCommands\n{commands}\n\nModules\n{modules}",
        archive = catalog.archive_name,
        package = catalog.package_name,
        module_count = catalog.module_count,
        commands = commands,
        modules = modules,
    ))
}

pub(crate) fn render_plugin_report(
    surface: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    render_fallible_snapshot_report(
        || plugin_report_snapshot(surface),
        render_plugin_report_from_snapshot,
    )
}

pub(crate) fn reload_plugins_report_snapshot(
) -> Result<ReloadPluginsReportSnapshot, Box<dyn std::error::Error>> {
    let catalog = load_plugin_catalog_from_cwd()?;
    let surface = load_plugin_surface_from_cwd("reload-plugins").map_err(not_found_io_error)?;

    Ok(ReloadPluginsReportSnapshot { catalog, surface })
}

pub(crate) fn render_reload_plugins_report_from_snapshot(
    snapshot: &ReloadPluginsReportSnapshot,
) -> String {
    let source_hints = render_bulleted_items(&snapshot.surface.source_hints);

    format!(
        "Reload plugins\n  Rust status      inspection only\n  Runtime support  no plugin loader or live reload flow is implemented\n  Archive          {archive}\n  Package          {package}\n  Archived files   {archived_files}\n  Archived modules {module_count}\n  Summary          {summary}\n\nSource hints\n{source_hints}",
        archive = snapshot.catalog.archive_name,
        package = snapshot.catalog.package_name,
        archived_files = snapshot.surface.archived_file_count,
        module_count = snapshot.catalog.module_count,
        summary = snapshot.surface.summary,
        source_hints = source_hints,
    )
}

pub(crate) fn render_reload_plugins_report() -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        reload_plugins_report_snapshot,
        render_reload_plugins_report_from_snapshot,
    )
}

fn remote_env_snapshot_from_env_map(env_map: &BTreeMap<String, String>) -> RemoteEnvReportSnapshot {
    let remote = RemoteSessionContext::from_env_map(env_map);
    let bootstrap = UpstreamProxyBootstrap::from_env_map(env_map);
    let inherited = inherited_upstream_proxy_env(env_map);

    RemoteEnvReportSnapshot {
        remote,
        bootstrap,
        inherited_proxy_env_keys: inherited.keys().cloned().collect(),
    }
}

pub(crate) fn remote_env_report_snapshot() -> RemoteEnvReportSnapshot {
    let env_map = env::vars().collect::<BTreeMap<String, String>>();
    remote_env_snapshot_from_env_map(&env_map)
}

pub(crate) fn render_remote_env_report_from_snapshot(snapshot: &RemoteEnvReportSnapshot) -> String {
    let remote = &snapshot.remote;
    let bootstrap = &snapshot.bootstrap;
    let missing = remote_setup_gaps(&bootstrap);
    let session_id = remote
        .session_id
        .clone()
        .unwrap_or_else(|| String::from("<unset>"));
    let base_url = if remote.base_url.is_empty() {
        String::from("<unset>")
    } else {
        remote.base_url.clone()
    };
    let ws_target = if remote.base_url.is_empty() {
        String::from("<unavailable>")
    } else {
        bootstrap.ws_url()
    };

    format!(
        "Remote env\n  Rust status      bootstrap foundation only\n  Remote enabled   {remote_enabled}\n  Session id       {session_id}\n  Base URL         {base_url}\n  Upstream proxy   {upstream_proxy}\n  Proxy ready      {proxy_ready}\n  Token path       {token_path}\n  Token present    {token_present}\n  CA bundle path   {ca_bundle}\n  System CA path   {system_ca}\n  WS target        {ws_target}\n  Inherited proxy  {inherited_count} vars\n  Missing          {missing}\n  Usage            /remote-setup",
        remote_enabled = yes_no(remote.enabled),
        session_id = session_id,
        base_url = base_url,
        upstream_proxy = yes_no(bootstrap.upstream_proxy_enabled),
        proxy_ready = yes_no(bootstrap.should_enable()),
        token_path = bootstrap.token_path.display(),
        token_present = yes_no(bootstrap.token.is_some()),
        ca_bundle = bootstrap.ca_bundle_path.display(),
        system_ca = bootstrap.system_ca_path.display(),
        ws_target = ws_target,
        inherited_count = snapshot.inherited_proxy_env_keys.len(),
        missing = missing,
    )
}

pub(crate) fn render_remote_env_report() -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        || Ok(remote_env_report_snapshot()),
        render_remote_env_report_from_snapshot,
    )
}

pub(crate) fn remote_setup_report_snapshot(
) -> Result<RemoteSetupReportSnapshot, Box<dyn std::error::Error>> {
    let env_map = env::vars().collect::<BTreeMap<String, String>>();
    let catalog = load_remote_catalog_from_cwd()?;
    let command = load_remote_command_from_cwd("remote-setup").map_err(not_found_io_error)?;
    Ok(RemoteSetupReportSnapshot {
        env: remote_env_snapshot_from_env_map(&env_map),
        catalog,
        command,
    })
}

pub(crate) fn render_remote_setup_report_from_snapshot(
    snapshot: &RemoteSetupReportSnapshot,
) -> String {
    let remote = &snapshot.env.remote;
    let bootstrap = &snapshot.env.bootstrap;
    let missing = remote_setup_gaps(&bootstrap);
    let session_id = remote
        .session_id
        .clone()
        .unwrap_or_else(|| String::from("<unset>"));
    let base_url = if remote.base_url.is_empty() {
        String::from("<unset>")
    } else {
        remote.base_url.clone()
    };
    let source_hints = render_bulleted_items(&snapshot.command.source_hints);
    let transport_hints = render_bulleted_items(&snapshot.catalog.transport_files);

    format!(
        "Remote setup\n  Rust status       bootstrap foundation only\n  Remote ready      {ready}\n  Remote enabled    {remote_enabled}\n  Session id        {session_id}\n  Base URL          {base_url}\n  Token present     {token_present}\n  Archive           {archive}\n  Package           {package}\n  Archived files    {archived_files}\n  Transport files   {transport_files}\n  Summary           {summary}\n  Missing           {missing}\n  Usage             /remote-env\n\nSource hints\n{source_hints}\n\nTransport hints\n{transport_hints}",
        ready = yes_no(bootstrap.should_enable()),
        remote_enabled = yes_no(remote.enabled),
        session_id = session_id,
        base_url = base_url,
        token_present = yes_no(bootstrap.token.is_some()),
        archive = snapshot.catalog.archive_name,
        package = snapshot.catalog.package_name,
        archived_files = snapshot.command.archived_file_count,
        transport_files = snapshot.catalog.transport_files.len(),
        summary = snapshot.command.summary,
        missing = missing,
        source_hints = source_hints,
        transport_hints = transport_hints,
    )
}

pub(crate) fn render_remote_setup_report() -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        remote_setup_report_snapshot,
        render_remote_setup_report_from_snapshot,
    )
}

fn yes_no(value: bool) -> &'static str {
    if value {
        "yes"
    } else {
        "no"
    }
}

fn resolved_permission_mode_label(mode: ResolvedPermissionMode) -> &'static str {
    match mode {
        ResolvedPermissionMode::ReadOnly => "read-only",
        ResolvedPermissionMode::WorkspaceWrite => "workspace-write",
        ResolvedPermissionMode::DangerFullAccess => "danger-full-access",
    }
}

fn mcp_transport_counts(
    servers: &BTreeMap<String, runtime::ScopedMcpServerConfig>,
) -> BTreeMap<String, usize> {
    let mut counts = BTreeMap::<String, usize>::new();
    for server in servers.values() {
        let label = mcp_transport_display_name(server.transport());
        *counts.entry(label.to_string()).or_default() += 1;
    }
    counts
}

fn mcp_status_counts(servers: &[McpServerSnapshot]) -> BTreeMap<String, usize> {
    let mut counts = BTreeMap::<String, usize>::new();
    for server in servers {
        *counts.entry(server.runtime.status.clone()).or_default() += 1;
    }
    counts
}

fn mcp_attention_servers(servers: &[McpServerSnapshot]) -> Vec<McpAttentionSnapshot> {
    servers
        .iter()
        .filter(|server| server.runtime.status != "ready")
        .map(|server| McpAttentionSnapshot {
            name: server.name.clone(),
            transport: server.transport,
            status: server.runtime.status.clone(),
            detail: server.runtime.detail.clone(),
        })
        .collect()
}

fn mcp_blocked_servers(
    attention_servers: &[McpAttentionSnapshot],
) -> Vec<McpBlockedServerSnapshot> {
    attention_servers
        .iter()
        .filter(|server| server.status == "unsupported-transport")
        .map(|server| McpBlockedServerSnapshot {
            name: server.name.clone(),
            transport: server.transport,
            detail: server
                .detail
                .clone()
                .unwrap_or_else(|| String::from("<unknown>")),
        })
        .collect()
}

fn doctor_mcp_issues(attention_servers: &[McpAttentionSnapshot]) -> Vec<String> {
    attention_servers
        .iter()
        .map(|server| {
            let detail = server.detail.as_deref().unwrap_or("<unknown>");
            match server.status.as_str() {
                "unsupported-transport" => format!(
                    "MCP server `{}` ({}) is configured but not executable by the Rust runtime: {}",
                    server.name, server.transport, detail
                ),
                "user-auth-required" => format!(
                    "MCP server `{}` ({}) requires stored OAuth credentials before execution: {}",
                    server.name, server.transport, detail
                ),
                "expired" => format!(
                    "MCP server `{}` ({}) has expired stored OAuth credentials: {}",
                    server.name, server.transport, detail
                ),
                other => format!(
                    "MCP server `{}` ({}) is in `{}` state: {}",
                    server.name, server.transport, other, detail
                ),
            }
        })
        .collect()
}

fn doctor_mcp_snapshot(
    mcp_servers: &BTreeMap<String, runtime::ScopedMcpServerConfig>,
) -> io::Result<(DoctorMcpSnapshot, Vec<String>)> {
    let (collection, _) = mcp_collection_snapshot(mcp_servers)?;
    let issues = doctor_mcp_issues(&collection.attention_servers);
    Ok((
        DoctorMcpSnapshot {
            collection: Some(collection),
        },
        issues,
    ))
}

fn summarize_recorded_mcp_transports(counts: Option<&BTreeMap<String, usize>>) -> String {
    match counts {
        None => String::from("<unavailable>"),
        Some(counts) if counts.is_empty() => String::from("<none>"),
        Some(counts) => counts
            .iter()
            .map(|(label, count)| format!("{label}={count}"))
            .collect::<Vec<_>>()
            .join(", "),
    }
}

fn summarize_doctor_mcp_statuses(counts: Option<&BTreeMap<String, usize>>) -> String {
    match counts {
        None => String::from("<unavailable>"),
        Some(counts) if counts.is_empty() => String::from("<none>"),
        Some(counts) => counts
            .iter()
            .map(|(status, count)| format!("{status}={count}"))
            .collect::<Vec<_>>()
            .join(", "),
    }
}

fn summarize_mcp_blockers(blocked_servers: Option<&[McpBlockedServerSnapshot]>) -> String {
    match blocked_servers {
        None => String::from("<unavailable>"),
        Some(blocked_servers) if blocked_servers.is_empty() => String::from("<none>"),
        Some(blocked_servers) => blocked_servers
            .iter()
            .map(|server| format!("{} ({})", server.name, server.transport))
            .collect::<Vec<_>>()
            .join(", "),
    }
}

fn summarize_doctor_mcp_attention(attention_servers: Option<&[McpAttentionSnapshot]>) -> String {
    match attention_servers {
        None => String::from("<unavailable>"),
        Some(attention_servers) if attention_servers.is_empty() => String::from("<none>"),
        Some(attention_servers) => attention_servers
            .iter()
            .map(|server| format!("{} ({})", server.name, server.status))
            .collect::<Vec<_>>()
            .join(", "),
    }
}

fn oauth_expiry_summary(expires_at: Option<u64>) -> String {
    match expires_at {
        Some(timestamp) => match current_unix_timestamp() {
            Some(now) if timestamp <= now => format!("expired at {timestamp}"),
            Some(_) => format!("valid until {timestamp}"),
            None => format!("unix {timestamp}"),
        },
        None => String::from("<unset>"),
    }
}

fn current_unix_timestamp() -> Option<u64> {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .ok()
        .map(|duration| duration.as_secs())
}

fn summarize_scopes(scopes: &[String]) -> String {
    if scopes.is_empty() {
        String::from("<none>")
    } else {
        scopes.join(", ")
    }
}

fn summarize_doctor_issues(issues: &[String]) -> String {
    if issues.is_empty() {
        String::from("  <none>")
    } else {
        issues
            .iter()
            .map(|issue| format!("  - {issue}"))
            .collect::<Vec<_>>()
            .join("\n")
    }
}

fn render_tool_detail(spec: &ToolSpec) -> Result<String, Box<dyn std::error::Error>> {
    Ok(format!(
        "Tool\n  Name             {name}\n  Source           rust tool registry\n  Required mode    {required_mode}\n  Description      {description}\n\nInput schema\n{schema}",
        name = spec.name,
        required_mode = spec.required_permission.as_str(),
        description = spec.description,
        schema = render_json_block(&spec.input_schema)?,
    ))
}

fn render_json_block(value: &serde_json::Value) -> Result<String, serde_json::Error> {
    Ok(serde_json::to_string_pretty(value)?
        .lines()
        .map(|line| format!("  {line}"))
        .collect::<Vec<_>>()
        .join("\n"))
}

fn render_bulleted_items(items: &[String]) -> String {
    items
        .iter()
        .map(|item| format!("  - {item}"))
        .collect::<Vec<_>>()
        .join("\n")
}

fn remote_setup_gaps(bootstrap: &UpstreamProxyBootstrap) -> String {
    let missing = bootstrap.missing_requirements();
    if missing.is_empty() {
        String::from("<none>")
    } else {
        missing.join(", ")
    }
}

fn matches_tool_request(name: &str, requested: &str) -> bool {
    canonical_tool_query(name) == canonical_tool_query(requested)
        || canonical_token(name) == canonical_token(requested)
}

fn canonical_tool_query(value: &str) -> String {
    let canonical = canonical_token(value);
    canonical
        .strip_suffix("tool")
        .unwrap_or(canonical.as_str())
        .to_string()
}

fn canonical_token(value: &str) -> String {
    value
        .chars()
        .filter(char::is_ascii_alphanumeric)
        .flat_map(char::to_lowercase)
        .collect()
}

pub(crate) fn skills_report_snapshot(
    skill: Option<&str>,
) -> Result<SkillsReportSnapshot, Box<dyn std::error::Error>> {
    let requested = trimmed_non_empty(skill);

    if let Some(requested) = requested {
        let loaded = load_skill(requested, None).map_err(not_found_io_error)?;
        return Ok(SkillsReportSnapshot {
            selected_skill: Some(loaded),
            skills: Vec::new(),
        });
    }

    Ok(SkillsReportSnapshot {
        selected_skill: None,
        skills: list_skills(),
    })
}

pub(crate) fn render_skills_report_from_snapshot(snapshot: &SkillsReportSnapshot) -> String {
    if let Some(loaded) = snapshot.selected_skill.as_ref() {
        let name = loaded
            .skill
            .trim()
            .trim_start_matches('/')
            .trim_start_matches('$')
            .to_string();
        let description = loaded.description.as_deref().unwrap_or("not provided");
        return format!(
            "Skill
  Name             {name}
  Path             {path}
  Description      {description}

Prompt
{prompt}",
            name = name,
            path = loaded.path,
            description = description,
            prompt = loaded.prompt.trim_end(),
        );
    }

    let skill_count = snapshot.skills.len();
    if snapshot.skills.is_empty() {
        return String::from(
            "Skills
  Available        0
  Usage            /skills <name>
    Search paths     ./skills/*.md, CODEX_HOME/skills/<name>/SKILL.md",
        );
    }

    let width = snapshot
        .skills
        .iter()
        .map(|entry| entry.name.len())
        .max()
        .unwrap_or(5)
        + 2;
    let entries = snapshot
        .skills
        .iter()
        .map(|entry| {
            let summary = entry.description.as_deref().unwrap_or(entry.path.as_str());
            format!(
                "  {name:<width$}{summary}",
                name = entry.name,
                width = width
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    format!(
        "Skills
  Available        {count}
  Usage            /skills <name>

Entries
{entries}",
        count = skill_count,
        entries = entries,
    )
}

pub(crate) fn render_skills_report(
    skill: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        || skills_report_snapshot(skill),
        render_skills_report_from_snapshot,
    )
}

pub(crate) fn tasks_report_snapshot(
    task: Option<&str>,
) -> Result<TasksReportSnapshot, Box<dyn std::error::Error>> {
    let requested = trimmed_non_empty(task);

    if let Some(requested) = requested {
        let loaded = load_agent_task(requested).map_err(not_found_io_error)?;
        return Ok(TasksReportSnapshot {
            selected_task: Some(loaded),
            task_counts: None,
            tasks: Vec::new(),
        });
    }

    let tasks = list_agent_tasks().map_err(io::Error::other)?;
    let task_counts = task_status_counts(&tasks);
    Ok(TasksReportSnapshot {
        selected_task: None,
        task_counts: Some(task_counts),
        tasks,
    })
}

pub(crate) fn render_tasks_report_from_snapshot(snapshot: &TasksReportSnapshot) -> String {
    if let Some(loaded) = snapshot.selected_task.as_ref() {
        let task = &loaded.task;
        let output = loaded.output.as_deref().unwrap_or("<missing output file>");
        return format!(
            "Task\n  Id               {id}\n  Name             {name}\n  Status           {status}\n  Type             {kind}\n  Model            {model}\n  Created          {created}\n  Completed        {completed}\n  Output file      {output_file}\n  Manifest file    {manifest_file}\n  Error            {error}\n\nOutput\n{output}",
            id = task.agent_id,
            name = task.name,
            status = task.status,
            kind = task.subagent_type.as_deref().unwrap_or("unknown"),
            model = task.model.as_deref().unwrap_or("default"),
            created = task.created_at,
            completed = task.completed_at.as_deref().unwrap_or("<running>"),
            output_file = task.output_file,
            manifest_file = task.manifest_file,
            error = task.error.as_deref().unwrap_or("<none>"),
            output = output.trim_end(),
        );
    }

    if snapshot.tasks.is_empty() {
        return String::from(
            "Tasks\n  Persisted tasks   0\n  Usage            /tasks <id>\n  Detail           no persisted sub-agent tasks found",
        );
    }

    let counts = snapshot.task_counts.unwrap_or_default();
    let task_count = snapshot.tasks.len();
    let name_width = snapshot
        .tasks
        .iter()
        .map(|task| task.name.len())
        .max()
        .unwrap_or(4)
        + 2;
    let entries = snapshot
        .tasks
        .iter()
        .map(|task| {
            format!(
                "  {id:<24}{status:<11}{kind:<14}{name:<name_width$}{created}",
                id = task.agent_id,
                status = task.status,
                kind = task.subagent_type.as_deref().unwrap_or("unknown"),
                name = task.name,
                name_width = name_width,
                created = task.created_at,
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    format!(
        "Tasks\n  Persisted tasks   {task_count}\n  Running          {running}\n  Completed        {completed}\n  Failed           {failed}\n  Usage            /tasks <id>\n\nEntries\n{entries}",
        running = counts.running,
        completed = counts.completed,
        failed = counts.failed,
        entries = entries,
    )
}

pub(crate) fn render_tasks_report(
    task: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    render_snapshot_report(
        || tasks_report_snapshot(task),
        render_tasks_report_from_snapshot,
    )
}

pub(crate) fn render_diff_report() -> Result<String, Box<dyn std::error::Error>> {
    let output = crate::command_in_current_dir("git")?
        .args(["diff", "--", ":(exclude).omx"])
        .output()?;
    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr).trim().to_string();
        return Err(format!("git diff failed: {stderr}").into());
    }
    let diff = String::from_utf8(output.stdout)?;
    if diff.trim().is_empty() {
        return Ok(
            "Diff\n  Result           clean working tree\n  Detail           no current changes"
                .to_string(),
        );
    }
    Ok(format!("Diff\n\n{}", diff.trim_end()))
}

pub(crate) fn render_teleport_report(target: &str) -> Result<String, Box<dyn std::error::Error>> {
    let cwd = crate::current_working_directory()?;

    let file_list = Command::new("rg")
        .args(["--files"])
        .current_dir(&cwd)
        .output()?;
    let file_matches = if file_list.status.success() {
        String::from_utf8(file_list.stdout)?
            .lines()
            .filter(|line| line.contains(target))
            .take(10)
            .map(ToOwned::to_owned)
            .collect::<Vec<_>>()
    } else {
        Vec::new()
    };

    let content_output = Command::new("rg")
        .args(["-n", "-S", "--color", "never", target, "."])
        .current_dir(&cwd)
        .output()?;

    let mut lines = vec![format!("Teleport\n  Target           {target}")];
    if !file_matches.is_empty() {
        lines.push(String::new());
        lines.push("File matches".to_string());
        lines.extend(file_matches.into_iter().map(|path| format!("  {path}")));
    }

    if content_output.status.success() {
        let matches = String::from_utf8(content_output.stdout)?;
        if !matches.trim().is_empty() {
            lines.push(String::new());
            lines.push("Content matches".to_string());
            lines.push(crate::truncate_for_prompt(&matches, 4_000));
        }
    }

    if lines.len() == 1 {
        lines.push("  Result           no matches found".to_string());
    }

    Ok(lines.join("\n"))
}

pub(crate) fn render_last_tool_debug_report(
    session: &Session,
) -> Result<String, Box<dyn std::error::Error>> {
    let last_tool_use = session
        .messages
        .iter()
        .rev()
        .find_map(|message| {
            message.blocks.iter().rev().find_map(|block| match block {
                ContentBlock::ToolUse { id, name, input } => {
                    Some((id.clone(), name.clone(), input.clone()))
                }
                _ => None,
            })
        })
        .ok_or_else(|| "no prior tool call found in session".to_string())?;

    let tool_result = session.messages.iter().rev().find_map(|message| {
        message.blocks.iter().rev().find_map(|block| match block {
            ContentBlock::ToolResult {
                tool_use_id,
                tool_name,
                output,
                is_error,
            } if tool_use_id == &last_tool_use.0 => {
                Some((tool_name.clone(), output.clone(), *is_error))
            }
            _ => None,
        })
    });

    let mut lines = vec![
        "Debug tool call".to_string(),
        format!("  Tool id          {}", last_tool_use.0),
        format!("  Tool name        {}", last_tool_use.1),
        "  Input".to_string(),
        indent_block(&last_tool_use.2, 4),
    ];

    match tool_result {
        Some((tool_name, output, is_error)) => {
            lines.push("  Result".to_string());
            lines.push(format!("    name           {tool_name}"));
            lines.push(format!(
                "    status         {}",
                if is_error { "error" } else { "ok" }
            ));
            lines.push(indent_block(&output, 4));
        }
        None => lines.push("  Result           missing tool result".to_string()),
    }

    Ok(lines.join("\n"))
}

fn config_source_label(source: ConfigSource) -> &'static str {
    match source {
        ConfigSource::User => "user",
        ConfigSource::Project => "project",
        ConfigSource::Local => "local",
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum HookSelection {
    Pre,
    Post,
}

fn parse_hook_selection(value: &str) -> Option<HookSelection> {
    match value.trim().to_ascii_lowercase().as_str() {
        "pre" | "pretooluse" | "pre-tool-use" => Some(HookSelection::Pre),
        "post" | "posttooluse" | "post-tool-use" => Some(HookSelection::Post),
        _ => None,
    }
}

fn render_hook_command_entries(commands: &[String]) -> String {
    if commands.is_empty() {
        return String::from("  No commands configured for this event.");
    }

    commands
        .iter()
        .enumerate()
        .map(|(index, command)| format!("  {}. {}", index + 1, command))
        .collect::<Vec<_>>()
        .join("\n")
}

fn transport_label(transport: &McpClientTransport) -> &'static str {
    mcp_client_transport_display_name(transport)
}

fn auth_label(auth: &McpClientAuth) -> &'static str {
    match auth {
        McpClientAuth::None => "none",
        McpClientAuth::OAuth(_) => "oauth",
    }
}

fn transport_target_summary(transport: &McpClientTransport) -> String {
    match transport {
        McpClientTransport::Stdio(config) => {
            let args = if config.args.is_empty() {
                String::new()
            } else {
                format!(" {}", config.args.join(" "))
            };
            format!("{}{}", config.command, args)
        }
        McpClientTransport::Sse(config)
        | McpClientTransport::Http(config)
        | McpClientTransport::WebSocket(config) => config.url.clone(),
        McpClientTransport::Sdk(config) => format!("sdk:{}", config.name),
        McpClientTransport::SimcoeAiProxy(config) => format!("{} ({})", config.url, config.id),
    }
}

fn mcp_server_snapshot(
    name: &str,
    config: &runtime::ScopedMcpServerConfig,
    bootstrap: &McpClientBootstrap,
) -> io::Result<McpServerSnapshot> {
    let runtime = mcp_server_auth_status(name, config)?;
    let detail = match &bootstrap.transport {
        McpClientTransport::Stdio(config) => McpServerDetailSnapshot::Stdio {
            command: config.command.clone(),
            args: config.args.clone(),
            env_var_count: config.env.len(),
        },
        McpClientTransport::Sse(config)
        | McpClientTransport::Http(config)
        | McpClientTransport::WebSocket(config) => McpServerDetailSnapshot::HttpLike {
            target: config.url.clone(),
            auth: auth_label(&config.auth),
            headers_count: config.headers.len(),
            headers_helper: config.headers_helper.clone(),
        },
        McpClientTransport::Sdk(config) => McpServerDetailSnapshot::Sdk {
            name: config.name.clone(),
        },
        McpClientTransport::SimcoeAiProxy(config) => McpServerDetailSnapshot::SimcoeAiProxy {
            target: config.url.clone(),
            proxy_id: config.id.clone(),
        },
    };

    Ok(McpServerSnapshot {
        name: name.to_string(),
        scope: config_source_label(config.scope),
        transport: transport_label(&bootstrap.transport),
        target: transport_target_summary(&bootstrap.transport),
        normalized_name: bootstrap.normalized_name.clone(),
        tool_prefix: bootstrap.tool_prefix.clone(),
        signature: bootstrap.signature.clone(),
        supported_execution: runtime.supported_execution,
        execution_detail: if runtime.supported_execution {
            None
        } else {
            runtime.detail.clone()
        },
        runtime,
        detail,
    })
}

fn render_mcp_server_detail(server: &McpServerSnapshot) -> String {
    let stored_creds = if server.runtime.requires_user_auth {
        yes_no(server.runtime.stored_credentials).to_string()
    } else {
        String::from("<n/a>")
    };
    let refresh_token = if server.runtime.requires_user_auth {
        yes_no(server.runtime.refresh_token_present).to_string()
    } else {
        String::from("<n/a>")
    };
    let expiry = if server.runtime.requires_user_auth {
        oauth_expiry_summary(server.runtime.expires_at)
    } else {
        String::from("<n/a>")
    };
    let scopes = if server.runtime.requires_user_auth {
        summarize_scopes(&server.runtime.scopes)
    } else {
        String::from("<n/a>")
    };

    let mut lines = vec![format!(
        "MCP server\n  Name              {name}\n  Scope             {scope}\n  Transport         {transport}\n  Normalized name   {normalized}\n  Tool prefix       {tool_prefix}\n  Signature         {signature}",
        name = server.name,
        scope = server.scope,
        transport = server.transport,
        normalized = server.normalized_name,
        tool_prefix = server.tool_prefix,
        signature = server.signature.as_deref().unwrap_or("<none>"),
    )];

    lines.push(String::from(""));
    lines.push(format!(
        "Runtime\n  Status            {}\n  Executable        {}\n  Auth kind         {}\n  User auth         {}\n  Stored creds      {}\n  Refresh token     {}\n  Expiry            {}\n  Scopes            {}\n  Detail            {}",
        server.runtime.status,
        yes_no(server.runtime.supported_execution),
        server.runtime.auth_kind,
        yes_no(server.runtime.requires_user_auth),
        stored_creds,
        refresh_token,
        expiry,
        scopes,
        server.runtime.detail.as_deref().unwrap_or("<none>"),
    ));

    if server.runtime.requires_user_auth {
        let callback_port = server
            .runtime
            .callback_port
            .map_or_else(|| String::from("<unset>"), |port| port.to_string());
        let xaa = server.runtime.xaa.map_or_else(
            || String::from("<unset>"),
            |value| yes_no(value).to_string(),
        );
        lines.push(String::from(""));
        lines.push(format!(
            "OAuth\n  Client id         {}\n  Callback port     {}\n  Metadata URL      {}\n  XAA               {}",
            server.runtime.client_id.as_deref().unwrap_or("<unset>"),
            callback_port,
            server
                .runtime
                .auth_server_metadata_url
                .as_deref()
                .unwrap_or("<unset>"),
            xaa,
        ));
    }

    match &server.detail {
        McpServerDetailSnapshot::Stdio {
            command,
            args,
            env_var_count,
        } => {
            lines.push(String::from(""));
            lines.push(format!(
                "Execution\n  Command           {}\n  Args              {}\n  Env vars          {}",
                command,
                if args.is_empty() {
                    "<none>".to_string()
                } else {
                    args.join(" ")
                },
                env_var_count,
            ));
        }
        McpServerDetailSnapshot::HttpLike {
            target,
            auth,
            headers_count,
            headers_helper,
        } => {
            lines.push(String::from(""));
            lines.push(format!(
                "Connection\n  Target            {}\n  Auth              {}\n  Headers           {}\n  Headers helper    {}",
                target,
                auth,
                headers_count,
                headers_helper.as_deref().unwrap_or("<none>"),
            ));
        }
        McpServerDetailSnapshot::Sdk { name } => {
            lines.push(String::from(""));
            lines.push(format!("Connection\n  SDK name          {name}"));
        }
        McpServerDetailSnapshot::SimcoeAiProxy { target, proxy_id } => {
            lines.push(String::from(""));
            lines.push(format!(
                "Connection\n  Target            {}\n  Proxy id          {}",
                target, proxy_id,
            ));
        }
    }

    lines.join("\n")
}

fn indent_block(value: &str, spaces: usize) -> String {
    let indent = " ".repeat(spaces);
    value
        .lines()
        .map(|line| format!("{indent}{line}"))
        .collect::<Vec<_>>()
        .join("\n")
}

pub(crate) fn render_version_report() -> String {
    let git_sha = crate::GIT_SHA.unwrap_or("unknown");
    let target = crate::BUILD_TARGET.unwrap_or("unknown");
    format!(
        "Claw Code\n  Version          {}\n  Git SHA          {git_sha}\n  Target           {target}\n  Build date       {}",
        crate::VERSION,
        crate::DEFAULT_DATE,
    )
}
