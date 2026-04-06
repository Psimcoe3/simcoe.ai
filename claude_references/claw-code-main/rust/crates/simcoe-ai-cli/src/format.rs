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
    PluginSurfaceKind,
};
use runtime::{
    credentials_path, inherited_upstream_proxy_env, load_oauth_credentials, ConfigLoader,
    ConfigSource, ContentBlock, McpClientAuth, McpClientBootstrap, McpClientTransport,
    McpTransport, ProjectContext, RemoteSessionContext, ResolvedPermissionMode, Session,
    TokenUsage, UpstreamProxyBootstrap,
};
use tools::{
    list_agent_profiles, list_agent_tasks, list_skills, load_agent_profile, load_agent_task,
    load_skill, mvp_tool_specs, ToolSpec,
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

pub(crate) fn status_context(
    session_path: Option<&Path>,
) -> Result<StatusContext, Box<dyn std::error::Error>> {
    let cwd = env::current_dir()?;
    let loader = ConfigLoader::default_for(&cwd);
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

pub(crate) fn render_config_report(
    section: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let cwd = env::current_dir()?;
    let loader = ConfigLoader::default_for(&cwd);
    let discovered = loader.discover();
    let runtime_config = loader.load()?;

    let mut lines = vec![
        format!(
            "Config
  Working directory {}
  Loaded files      {}
  Merged keys       {}",
            cwd.display(),
            runtime_config.loaded_entries().len(),
            runtime_config.merged().len()
        ),
        "Discovered files".to_string(),
    ];
    for entry in discovered {
        let source = match entry.source {
            ConfigSource::User => "user",
            ConfigSource::Project => "project",
            ConfigSource::Local => "local",
        };
        let status = if runtime_config
            .loaded_entries()
            .iter()
            .any(|loaded_entry| loaded_entry.path == entry.path)
        {
            "loaded"
        } else {
            "missing"
        };
        lines.push(format!(
            "  {source:<7} {status:<7} {}",
            entry.path.display()
        ));
    }

    if let Some(section) = section {
        lines.push(format!("Merged section: {section}"));
        let value = match section {
            "env" => runtime_config.get("env"),
            "hooks" => runtime_config.get("hooks"),
            "model" => runtime_config.get("model"),
            other => {
                lines.push(format!(
                    "  Unsupported config section '{other}'. Use env, hooks, or model."
                ));
                return Ok(lines.join("\n"));
            }
        };
        lines.push(format!(
            "  {}",
            match value {
                Some(value) => value.render(),
                None => "<unset>".to_string(),
            }
        ));
        return Ok(lines.join("\n"));
    }

    lines.push("Merged JSON".to_string());
    lines.push(format!("  {}", runtime_config.as_json().render()));
    Ok(lines.join("\n"))
}

pub(crate) fn render_hooks_report(
    event: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let cwd = env::current_dir()?;
    let runtime_config = ConfigLoader::default_for(&cwd).load()?;
    let hooks = runtime_config.hooks();
    let requested = event.map(str::trim).filter(|value| !value.is_empty());

    if let Some(requested) = requested {
        let selection = parse_hook_selection(requested).ok_or_else(|| {
            io::Error::new(
                io::ErrorKind::InvalidInput,
                format!("unsupported hooks selector '{requested}'. Use pre or post."),
            )
        })?;
        let (label, commands) = match selection {
            HookSelection::Pre => ("PreToolUse", hooks.pre_tool_use()),
            HookSelection::Post => ("PostToolUse", hooks.post_tool_use()),
        };
        return Ok(format!(
            "Hooks\n  Event             {label}\n  Configured        {}\n  Usage             /hooks\n  Runtime           exit 2 denies, other non-zero exits warn\n\nCommands\n{}",
            commands.len(),
            render_hook_command_entries(commands),
        ));
    }

    let pre = hooks.pre_tool_use();
    let post = hooks.post_tool_use();

    if pre.is_empty() && post.is_empty() {
        return Ok(String::from(
            "Hooks\n  Pre-tool hooks    0\n  Post-tool hooks   0\n  Usage             /hooks [pre|post]\n  Runtime           exit 2 denies, other non-zero exits warn\n  Detail            no hooks configured",
        ));
    }

    let mut lines = vec![format!(
        "Hooks\n  Pre-tool hooks    {}\n  Post-tool hooks   {}\n  Usage             /hooks [pre|post]\n  Runtime           exit 2 denies, other non-zero exits warn",
        pre.len(),
        post.len(),
    )];

    if !pre.is_empty() {
        lines.push(String::new());
        lines.push(String::from("PreToolUse"));
        lines.push(render_hook_command_entries(pre));
    }

    if !post.is_empty() {
        lines.push(String::new());
        lines.push(String::from("PostToolUse"));
        lines.push(render_hook_command_entries(post));
    }

    Ok(lines.join("\n"))
}

pub(crate) fn render_memory_report() -> Result<String, Box<dyn std::error::Error>> {
    let cwd = env::current_dir()?;
    let project_context = ProjectContext::discover(&cwd, crate::DEFAULT_DATE)?;
    let mut lines = vec![format!(
        "Memory
  Working directory {}
  Instruction files {}",
        cwd.display(),
        project_context.instruction_files.len()
    )];
    if project_context.instruction_files.is_empty() {
        lines.push("Discovered files".to_string());
        lines.push(
            "  No SIMCOE instruction files discovered in the current directory ancestry."
                .to_string(),
        );
    } else {
        lines.push("Discovered files".to_string());
        for (index, file) in project_context.instruction_files.iter().enumerate() {
            let preview = file.content.lines().next().unwrap_or("").trim();
            let preview = if preview.is_empty() {
                "<empty>"
            } else {
                preview
            };
            lines.push(format!("  {}. {}", index + 1, file.path.display()));
            lines.push(format!(
                "     lines={} preview={}",
                file.content.lines().count(),
                preview
            ));
        }
    }
    Ok(lines.join("\n"))
}

pub(crate) fn render_mcp_report(
    server: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let cwd = env::current_dir()?;
    let runtime_config = ConfigLoader::default_for(&cwd).load()?;
    let servers = runtime_config.mcp().servers();
    let requested = server.map(str::trim).filter(|value| !value.is_empty());

    if let Some(requested) = requested {
        let (name, config) = servers
            .iter()
            .find(|(name, _)| name.eq_ignore_ascii_case(requested))
            .ok_or_else(|| {
                io::Error::new(
                    io::ErrorKind::NotFound,
                    format!("unknown MCP server: {requested}"),
                )
            })?;
        let bootstrap = McpClientBootstrap::from_scoped_config(name, config);
        return Ok(render_mcp_server_detail(name, config.scope, &bootstrap));
    }

    if servers.is_empty() {
        return Ok(String::from(
            "MCP\n  Configured servers 0\n  Usage             /mcp <server>\n  Detail            no MCP servers configured",
        ));
    }

    let name_width = servers.keys().map(String::len).max().unwrap_or(6) + 2;
    let entries = servers
        .iter()
        .map(|(name, config)| {
            let bootstrap = McpClientBootstrap::from_scoped_config(name, config);
            format!(
                "  {name:<name_width$}{scope:<8}{transport:<14}{target}",
                name = name,
                name_width = name_width,
                scope = config_source_label(config.scope),
                transport = transport_label(&bootstrap.transport),
                target = transport_target_summary(&bootstrap.transport),
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    Ok(format!(
        "MCP\n  Configured servers {}\n  Usage             /mcp <server>\n\nServers\n{}",
        servers.len(),
        entries,
    ))
}

pub(crate) fn render_agents_report(
    agent: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let requested = agent.map(str::trim).filter(|value| !value.is_empty());
    let tasks = list_agent_tasks().map_err(io::Error::other)?;

    if let Some(requested) = requested {
        let profile = load_agent_profile(requested)
            .map_err(|error| io::Error::new(io::ErrorKind::NotFound, error))?;
        let matching_tasks = tasks
            .iter()
            .filter(|task| task.subagent_type.as_deref() == Some(profile.name.as_str()))
            .collect::<Vec<_>>();
        let running = matching_tasks
            .iter()
            .filter(|task| task.status == "running")
            .count();
        let completed = matching_tasks
            .iter()
            .filter(|task| task.status == "completed")
            .count();
        let failed = matching_tasks
            .iter()
            .filter(|task| task.status == "failed")
            .count();
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
        let recent_tasks = if matching_tasks.is_empty() {
            String::from("  None")
        } else {
            matching_tasks
                .iter()
                .take(5)
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

        return Ok(format!(
            "Agent\n  Name             {name}\n  Description      {description}\n  Aliases          {aliases}\n  Allowed tools    {tool_count}\n  Running          {running}\n  Completed        {completed}\n  Failed           {failed}\n\nTools\n{tools}\n\nRecent tasks\n{recent_tasks}",
            name = profile.name,
            description = profile.description,
            aliases = aliases,
            tool_count = profile.tools.len(),
            running = running,
            completed = completed,
            failed = failed,
            tools = tools,
            recent_tasks = recent_tasks,
        ));
    }

    let profiles = list_agent_profiles();
    if profiles.is_empty() {
        return Ok(String::from(
            "Agents\n  Available        0\n  Usage            /agents <name>\n  Detail           no built-in sub-agent profiles found",
        ));
    }

    let profile_count = profiles.len();
    let name_width = profiles
        .iter()
        .map(|profile| profile.name.len())
        .max()
        .unwrap_or(6)
        + 2;
    let entries = profiles
        .into_iter()
        .map(|profile| {
            let recent = tasks
                .iter()
                .filter(|task| task.subagent_type.as_deref() == Some(profile.name.as_str()))
                .count();
            format!(
                "  {name:<name_width$}{tool_count:>2} tools  {recent:>2} recent  {description}",
                name = profile.name,
                tool_count = profile.tool_count,
                recent = recent,
                description = profile.description,
                name_width = name_width,
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    Ok(format!(
        "Agents\n  Available        {profile_count}\n  Persisted tasks  {task_count}\n  Usage            /agents <name>\n\nProfiles\n{entries}",
        task_count = tasks.len(),
        entries = entries,
    ))
}

pub(crate) fn render_doctor_report() -> Result<String, Box<dyn std::error::Error>> {
    let cwd = env::current_dir()?;
    let loader = ConfigLoader::default_for(&cwd);
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

    let (stored_creds, refresh_token, expiry, scopes, has_stored_creds) =
        if credentials_path_result.is_ok() {
            match load_oauth_credentials() {
                Ok(Some(token_set)) => (
                    String::from("yes"),
                    yes_no(token_set.refresh_token.is_some()).to_string(),
                    oauth_expiry_summary(token_set.expires_at),
                    summarize_scopes(&token_set.scopes),
                    true,
                ),
                Ok(None) => (
                    String::from("no"),
                    String::from("<unavailable>"),
                    String::from("<unavailable>"),
                    String::from("<none>"),
                    false,
                ),
                Err(error) => {
                    issues.push(format!("failed to load oauth credentials: {error}"));
                    (
                        String::from("error"),
                        String::from("<unavailable>"),
                        format!("<error: {error}>"),
                        String::from("<unavailable>"),
                        false,
                    )
                }
            }
        } else {
            (
                String::from("error"),
                String::from("<unavailable>"),
                String::from("<unavailable>"),
                String::from("<unavailable>"),
                false,
            )
        };

    let remote_missing = if remote.enabled {
        remote_setup_gaps(&bootstrap)
    } else {
        String::from("<disabled>")
    };
    if remote.enabled && !bootstrap.should_enable() {
        issues.push(format!("remote bootstrap incomplete: {remote_missing}"));
    }

    let project_root_display = project_root.as_ref().map_or_else(
        || String::from("unknown"),
        |path| path.display().to_string(),
    );
    let git_branch_display = git_branch.as_deref().unwrap_or("unknown");
    let session_id = remote
        .session_id
        .clone()
        .unwrap_or_else(|| String::from("<unset>"));
    let base_url = if remote.base_url.is_empty() {
        String::from("<unset>")
    } else {
        remote.base_url.clone()
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

            Ok(format!(
                "Doctor\n  Rust status       inspection only\n  Working directory {cwd}\n  Project root      {project_root}\n  Git branch        {git_branch}\n  Instruction files {instruction_files}\n  Issues            {issue_count}\n\nConfig\n  Status            ok\n  Discovered files  {discovered_files}\n  Loaded files      {loaded_files}\n  Model             {model}\n  Permission mode   {permission_mode}\n  Sandbox enabled   {sandbox_enabled}\n  Sandbox active    {sandbox_active}\n  Filesystem mode   {filesystem_mode}\n  Network isolation {network_isolation}\n  Detail            {sandbox_detail}\n\nAuth\n  OAuth config      {oauth_config}\n  Credentials path  {credentials_path}\n  Stored creds      {stored_creds}\n  Refresh token     {refresh_token}\n  Expiry            {expiry}\n  Scopes            {scopes}\n\nHooks + MCP\n  Pre hooks         {pre_hooks}\n  Post hooks        {post_hooks}\n  MCP servers       {mcp_servers}\n  MCP transports    {mcp_transports}\n\nRemote\n  Enabled           {remote_enabled}\n  Proxy ready       {proxy_ready}\n  Session id        {session_id}\n  Base URL          {base_url}\n  Missing           {remote_missing}\n\nIssues\n{issue_lines}",
                cwd = cwd.display(),
                project_root = project_root_display,
                git_branch = git_branch_display,
                instruction_files = instruction_file_count,
                issue_count = issues.len(),
                discovered_files = discovered.len(),
                loaded_files = runtime_config.loaded_entries().len(),
                model = runtime_config.model().unwrap_or("<unset>"),
                permission_mode = runtime_config
                    .permission_mode()
                    .map(resolved_permission_mode_label)
                    .unwrap_or("<unset>"),
                sandbox_enabled = yes_no(sandbox_status.enabled),
                sandbox_active = yes_no(sandbox_status.active),
                filesystem_mode = sandbox_status.filesystem_mode.as_str(),
                network_isolation = yes_no(sandbox_status.network_active),
                sandbox_detail = sandbox_status.fallback_reason.as_deref().unwrap_or("<none>"),
                oauth_config = yes_no(runtime_config.oauth().is_some()),
                credentials_path = credentials_path_display,
                stored_creds = stored_creds,
                refresh_token = refresh_token,
                expiry = expiry,
                scopes = scopes,
                pre_hooks = hooks.pre_tool_use().len(),
                post_hooks = hooks.post_tool_use().len(),
                mcp_servers = mcp_servers.len(),
                mcp_transports = summarize_mcp_transports(mcp_servers),
                remote_enabled = yes_no(remote.enabled),
                proxy_ready = yes_no(bootstrap.should_enable()),
                session_id = session_id,
                base_url = base_url,
                remote_missing = remote_missing,
                issue_lines = summarize_doctor_issues(&issues),
            ))
        }
        Err(error) => {
            issues.push(format!("config load failed: {error}"));

            Ok(format!(
                "Doctor\n  Rust status       inspection only\n  Working directory {cwd}\n  Project root      {project_root}\n  Git branch        {git_branch}\n  Instruction files {instruction_files}\n  Issues            {issue_count}\n\nConfig\n  Status            error\n  Discovered files  {discovered_files}\n  Loaded files      0\n  Model             <unavailable>\n  Permission mode   <unavailable>\n  Sandbox enabled   <unavailable>\n  Sandbox active    <unavailable>\n  Filesystem mode   <unavailable>\n  Network isolation <unavailable>\n  Detail            {config_error}\n\nAuth\n  OAuth config      <unavailable>\n  Credentials path  {credentials_path}\n  Stored creds      {stored_creds}\n  Refresh token     {refresh_token}\n  Expiry            {expiry}\n  Scopes            {scopes}\n\nHooks + MCP\n  Pre hooks         <unavailable>\n  Post hooks        <unavailable>\n  MCP servers       <unavailable>\n  MCP transports    <unavailable>\n\nRemote\n  Enabled           {remote_enabled}\n  Proxy ready       {proxy_ready}\n  Session id        {session_id}\n  Base URL          {base_url}\n  Missing           {remote_missing}\n\nIssues\n{issue_lines}",
                cwd = cwd.display(),
                project_root = project_root_display,
                git_branch = git_branch_display,
                instruction_files = instruction_file_count,
                issue_count = issues.len(),
                discovered_files = discovered.len(),
                config_error = error,
                credentials_path = credentials_path_display,
                stored_creds = stored_creds,
                refresh_token = refresh_token,
                expiry = expiry,
                scopes = scopes,
                remote_enabled = yes_no(remote.enabled),
                proxy_ready = yes_no(bootstrap.should_enable()),
                session_id = session_id,
                base_url = base_url,
                remote_missing = remote_missing,
                issue_lines = summarize_doctor_issues(&issues),
            ))
        }
    }
}

pub(crate) fn render_tools_report(
    tool: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let requested = tool.map(str::trim).filter(|value| !value.is_empty());
    let rust_tools = mvp_tool_specs();
    let archived_catalog = load_tool_catalog_from_cwd().ok();

    if let Some(requested) = requested {
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

        let mut sections = Vec::new();
        if let Some(spec) = rust_match {
            sections.push(render_tool_detail(spec)?);
        }
        if let Some(family) = archived_match {
            let source_hints = family
                .source_hints
                .iter()
                .map(|hint| format!("  - {hint}"))
                .collect::<Vec<_>>()
                .join("\n");
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

    let rust_width = rust_tools
        .iter()
        .map(|spec| spec.name.len())
        .max()
        .unwrap_or(4)
        + 2;
    let rust_entries = rust_tools
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
        if let Some(catalog) = archived_catalog {
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
        rust_tool_count = rust_tools.len(),
        archived_family_count = archived_family_count,
        archived_file_count = archived_file_count,
        rust_entries = rust_entries,
        archived_entries = archived_entries,
    ))
}

pub(crate) fn render_plugin_report(
    surface: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let requested = surface.map(str::trim).filter(|value| !value.is_empty());

    if let Some(requested) = requested {
        let surface = load_plugin_surface_from_cwd(requested)
            .map_err(|error| io::Error::new(io::ErrorKind::NotFound, error))?;
        let source_hints = surface
            .source_hints
            .iter()
            .map(|hint| format!("  - {hint}"))
            .collect::<Vec<_>>()
            .join("\n");
        return Ok(format!(
            "Plugin\n  Name             {name}\n  Kind             {kind}\n  Rust status      inspection only\n  Archived files   {archived_files}\n  Summary          {summary}\n\nSource hints\n{source_hints}",
            name = surface.name,
            kind = surface.kind.as_str(),
            archived_files = surface.archived_file_count,
            summary = surface.summary,
            source_hints = source_hints,
        ));
    }

    let catalog = load_plugin_catalog_from_cwd()?;
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

pub(crate) fn render_reload_plugins_report() -> Result<String, Box<dyn std::error::Error>> {
    let catalog = load_plugin_catalog_from_cwd()?;
    let surface = load_plugin_surface_from_cwd("reload-plugins")
        .map_err(|error| io::Error::new(io::ErrorKind::NotFound, error))?;
    let source_hints = surface
        .source_hints
        .iter()
        .map(|hint| format!("  - {hint}"))
        .collect::<Vec<_>>()
        .join("\n");

    Ok(format!(
        "Reload plugins\n  Rust status      inspection only\n  Runtime support  no plugin loader or live reload flow is implemented\n  Archive          {archive}\n  Package          {package}\n  Archived files   {archived_files}\n  Archived modules {module_count}\n  Summary          {summary}\n\nSource hints\n{source_hints}",
        archive = catalog.archive_name,
        package = catalog.package_name,
        archived_files = surface.archived_file_count,
        module_count = catalog.module_count,
        summary = surface.summary,
        source_hints = source_hints,
    ))
}

pub(crate) fn render_remote_env_report() -> Result<String, Box<dyn std::error::Error>> {
    let env_map = env::vars().collect::<BTreeMap<String, String>>();
    let remote = RemoteSessionContext::from_env_map(&env_map);
    let bootstrap = UpstreamProxyBootstrap::from_env_map(&env_map);
    let inherited = inherited_upstream_proxy_env(&env_map);
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

    Ok(format!(
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
        inherited_count = inherited.len(),
        missing = missing,
    ))
}

pub(crate) fn render_remote_setup_report() -> Result<String, Box<dyn std::error::Error>> {
    let env_map = env::vars().collect::<BTreeMap<String, String>>();
    let remote = RemoteSessionContext::from_env_map(&env_map);
    let bootstrap = UpstreamProxyBootstrap::from_env_map(&env_map);
    let catalog = load_remote_catalog_from_cwd()?;
    let surface = load_remote_command_from_cwd("remote-setup")
        .map_err(|error| io::Error::new(io::ErrorKind::NotFound, error))?;
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
    let source_hints = surface
        .source_hints
        .iter()
        .map(|hint| format!("  - {hint}"))
        .collect::<Vec<_>>()
        .join("\n");
    let transport_hints = catalog
        .transport_files
        .iter()
        .map(|hint| format!("  - {hint}"))
        .collect::<Vec<_>>()
        .join("\n");

    Ok(format!(
        "Remote setup\n  Rust status       bootstrap foundation only\n  Remote ready      {ready}\n  Remote enabled    {remote_enabled}\n  Session id        {session_id}\n  Base URL          {base_url}\n  Token present     {token_present}\n  Archive           {archive}\n  Package           {package}\n  Archived files    {archived_files}\n  Transport files   {transport_files}\n  Summary           {summary}\n  Missing           {missing}\n  Usage             /remote-env\n\nSource hints\n{source_hints}\n\nTransport hints\n{transport_hints}",
        ready = yes_no(bootstrap.should_enable()),
        remote_enabled = yes_no(remote.enabled),
        session_id = session_id,
        base_url = base_url,
        token_present = yes_no(bootstrap.token.is_some()),
        archive = catalog.archive_name,
        package = catalog.package_name,
        archived_files = surface.archived_file_count,
        transport_files = catalog.transport_files.len(),
        summary = surface.summary,
        missing = missing,
        source_hints = source_hints,
        transport_hints = transport_hints,
    ))
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

fn summarize_mcp_transports(servers: &BTreeMap<String, runtime::ScopedMcpServerConfig>) -> String {
    if servers.is_empty() {
        return String::from("<none>");
    }

    let mut counts = BTreeMap::<&'static str, usize>::new();
    for server in servers.values() {
        let label = match server.transport() {
            McpTransport::Stdio => "stdio",
            McpTransport::Sse => "sse",
            McpTransport::Http => "http",
            McpTransport::Ws => "ws",
            McpTransport::Sdk => "sdk",
            McpTransport::SimcoeAiProxy => "simcoe-ai-proxy",
        };
        *counts.entry(label).or_default() += 1;
    }

    counts
        .into_iter()
        .map(|(label, count)| format!("{label}={count}"))
        .collect::<Vec<_>>()
        .join(", ")
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

fn remote_setup_gaps(bootstrap: &UpstreamProxyBootstrap) -> String {
    let mut missing = Vec::new();
    if !bootstrap.remote.enabled {
        missing.push("SIMCOE_AI_REMOTE disabled");
    }
    if bootstrap.remote.session_id.is_none() {
        missing.push("missing remote session id");
    }
    if bootstrap.remote.base_url.is_empty() {
        missing.push("missing base URL");
    }
    if !bootstrap.upstream_proxy_enabled {
        missing.push("CCR_UPSTREAM_PROXY_ENABLED disabled");
    }
    if bootstrap.token.is_none() {
        missing.push("missing session token");
    }
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

pub(crate) fn render_skills_report(
    skill: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let requested = skill.map(str::trim).filter(|value| !value.is_empty());

    if let Some(requested) = requested {
        let loaded = load_skill(requested, None)
            .map_err(|error| io::Error::new(io::ErrorKind::NotFound, error))?;
        let name = loaded
            .skill
            .trim()
            .trim_start_matches('/')
            .trim_start_matches('$')
            .to_string();
        let description = loaded
            .description
            .unwrap_or_else(|| "not provided".to_string());
        return Ok(format!(
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
        ));
    }

    let skills = list_skills();
    let skill_count = skills.len();
    if skills.is_empty() {
        return Ok(String::from(
            "Skills
  Available        0
  Usage            /skills <name>
    Search paths     ./skills/*.md, CODEX_HOME/skills/<name>/SKILL.md",
        ));
    }

    let width = skills
        .iter()
        .map(|entry| entry.name.len())
        .max()
        .unwrap_or(5)
        + 2;
    let entries = skills
        .into_iter()
        .map(|entry| {
            let summary = entry.description.unwrap_or_else(|| entry.path.clone());
            format!(
                "  {name:<width$}{summary}",
                name = entry.name,
                width = width
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    Ok(format!(
        "Skills
  Available        {count}
  Usage            /skills <name>

Entries
{entries}",
        count = skill_count,
        entries = entries,
    ))
}

pub(crate) fn render_tasks_report(
    task: Option<&str>,
) -> Result<String, Box<dyn std::error::Error>> {
    let requested = task.map(str::trim).filter(|value| !value.is_empty());

    if let Some(requested) = requested {
        let loaded = load_agent_task(requested)
            .map_err(|error| io::Error::new(io::ErrorKind::NotFound, error))?;
        let task = loaded.task;
        let output = loaded
            .output
            .unwrap_or_else(|| String::from("<missing output file>"));
        return Ok(format!(
            "Task\n  Id               {id}\n  Name             {name}\n  Status           {status}\n  Type             {kind}\n  Model            {model}\n  Created          {created}\n  Completed        {completed}\n  Output file      {output_file}\n  Manifest file    {manifest_file}\n  Error            {error}\n\nOutput\n{output}",
            id = task.agent_id,
            name = task.name,
            status = task.status,
            kind = task.subagent_type.unwrap_or_else(|| "unknown".to_string()),
            model = task.model.unwrap_or_else(|| "default".to_string()),
            created = task.created_at,
            completed = task.completed_at.unwrap_or_else(|| "<running>".to_string()),
            output_file = task.output_file,
            manifest_file = task.manifest_file,
            error = task.error.unwrap_or_else(|| "<none>".to_string()),
            output = output.trim_end(),
        ));
    }

    let tasks = list_agent_tasks().map_err(io::Error::other)?;
    if tasks.is_empty() {
        return Ok(String::from(
            "Tasks\n  Persisted tasks   0\n  Usage            /tasks <id>\n  Detail           no persisted sub-agent tasks found",
        ));
    }

    let task_count = tasks.len();
    let running = tasks.iter().filter(|task| task.status == "running").count();
    let completed = tasks
        .iter()
        .filter(|task| task.status == "completed")
        .count();
    let failed = tasks.iter().filter(|task| task.status == "failed").count();
    let name_width = tasks.iter().map(|task| task.name.len()).max().unwrap_or(4) + 2;
    let entries = tasks
        .into_iter()
        .map(|task| {
            format!(
                "  {id:<24}{status:<11}{kind:<14}{name:<name_width$}{created}",
                id = task.agent_id,
                status = task.status,
                kind = task.subagent_type.unwrap_or_else(|| "unknown".to_string()),
                name = task.name,
                name_width = name_width,
                created = task.created_at,
            )
        })
        .collect::<Vec<_>>()
        .join("\n");

    Ok(format!(
        "Tasks\n  Persisted tasks   {task_count}\n  Running          {running}\n  Completed        {completed}\n  Failed           {failed}\n  Usage            /tasks <id>\n\nEntries\n{entries}",
        entries = entries,
    ))
}

pub(crate) fn render_diff_report() -> Result<String, Box<dyn std::error::Error>> {
    let output = Command::new("git")
        .args(["diff", "--", ":(exclude).omx"])
        .current_dir(env::current_dir()?)
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
    let cwd = env::current_dir()?;

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
    match transport {
        McpClientTransport::Stdio(_) => "stdio",
        McpClientTransport::Sse(_) => "sse",
        McpClientTransport::Http(_) => "http",
        McpClientTransport::WebSocket(_) => "ws",
        McpClientTransport::Sdk(_) => "sdk",
        McpClientTransport::SimcoeAiProxy(_) => "simcoe-ai-proxy",
    }
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

fn render_mcp_server_detail(
    name: &str,
    scope: ConfigSource,
    bootstrap: &McpClientBootstrap,
) -> String {
    let mut lines = vec![format!(
        "MCP server\n  Name              {name}\n  Scope             {scope}\n  Transport         {transport}\n  Normalized name   {normalized}\n  Tool prefix       {tool_prefix}\n  Signature         {signature}",
        name = name,
        scope = config_source_label(scope),
        transport = transport_label(&bootstrap.transport),
        normalized = bootstrap.normalized_name,
        tool_prefix = bootstrap.tool_prefix,
        signature = bootstrap.signature.as_deref().unwrap_or("<none>"),
    )];

    match &bootstrap.transport {
        McpClientTransport::Stdio(config) => {
            lines.push(String::from(""));
            lines.push(format!(
                "Execution\n  Command           {}\n  Args              {}\n  Env vars          {}",
                config.command,
                if config.args.is_empty() {
                    "<none>".to_string()
                } else {
                    config.args.join(" ")
                },
                config.env.len(),
            ));
        }
        McpClientTransport::Sse(config)
        | McpClientTransport::Http(config)
        | McpClientTransport::WebSocket(config) => {
            lines.push(String::from(""));
            lines.push(format!(
                "Connection\n  Target            {}\n  Auth              {}\n  Headers           {}\n  Headers helper    {}",
                config.url,
                auth_label(&config.auth),
                config.headers.len(),
                config.headers_helper.as_deref().unwrap_or("<none>"),
            ));
        }
        McpClientTransport::Sdk(config) => {
            lines.push(String::from(""));
            lines.push(format!("Connection\n  SDK name          {}", config.name));
        }
        McpClientTransport::SimcoeAiProxy(config) => {
            lines.push(String::from(""));
            lines.push(format!(
                "Connection\n  Target            {}\n  Proxy id          {}",
                config.url, config.id,
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
