use std::env;
use std::fs;
use std::io;
use std::process::Command;

use runtime::{CompactionConfig, ConfigLoader, ConversationRuntime, PermissionMode, Session};
use serde_json::json;

use crate::args::{
    brand_model_name, normalize_permission_mode, permission_mode_from_label, resolve_model_alias,
    AllowedToolSet, CliOutputFormat,
};
use crate::format::{
    format_auto_compaction_notice, format_compact_report, format_cost_report, format_model_report,
    format_model_switch_report, format_permissions_report, format_permissions_switch_report,
    format_resume_report, format_status_report, render_agents_report, render_config_report,
    render_diff_report, render_doctor_report, render_hooks_report, render_last_tool_debug_report,
    render_mcp_report, render_memory_report, render_plugin_report, render_reload_plugins_report,
    render_remote_env_report, render_remote_setup_report, render_repl_help, render_skills_report,
    render_tasks_report, render_teleport_report, render_tools_report, render_version_report,
    status_context, StatusUsage,
};
use crate::render::{Spinner, TerminalRenderer};
use crate::session_manager::{
    create_managed_session_handle, render_session_list, resolve_session_reference, SessionHandle,
};
use crate::tui::status_bar::StatusBarHandle;
use crate::{CliPermissionPrompter, CliToolExecutor, SimcoeRuntimeClient};

pub(crate) struct LiveCli {
    pub(crate) model: String,
    pub(crate) allowed_tools: Option<AllowedToolSet>,
    pub(crate) permission_mode: PermissionMode,
    pub(crate) system_prompt: Vec<String>,
    pub(crate) runtime: ConversationRuntime<SimcoeRuntimeClient, CliToolExecutor>,
    pub(crate) session: SessionHandle,
    pub(crate) status_bar: StatusBarHandle,
}

#[allow(clippy::too_many_lines)]
impl LiveCli {
    pub(crate) fn new(
        model: String,
        enable_tools: bool,
        allowed_tools: Option<AllowedToolSet>,
        permission_mode: PermissionMode,
    ) -> Result<Self, Box<dyn std::error::Error>> {
        let system_prompt = crate::build_system_prompt()?;
        let session = create_managed_session_handle()?;
        let status_bar = Self::create_status_bar(&model, permission_mode, &session);
        let runtime = crate::build_runtime(
            Session::new(),
            model.clone(),
            system_prompt.clone(),
            enable_tools,
            true,
            allowed_tools.clone(),
            permission_mode,
            Some(status_bar.clone()),
        )?;
        let cli = Self {
            model,
            allowed_tools,
            permission_mode,
            system_prompt,
            runtime,
            session,
            status_bar,
        };
        cli.sync_status_bar();
        cli.persist_session()?;
        Ok(cli)
    }

    pub(crate) fn startup_banner(&self) -> String {
        let cwd = env::current_dir().map_or_else(
            |_| "<unknown>".to_string(),
            |path| path.display().to_string(),
        );
        format!(
            "\x1b[38;5;196m\
 ██████╗██╗      █████╗ ██╗    ██╗\n\
██╔════╝██║     ██╔══██╗██║    ██║\n\
██║     ██║     ███████║██║ █╗ ██║\n\
██║     ██║     ██╔══██║██║███╗██║\n\
╚██████╗███████╗██║  ██║╚███╔███╔╝\n\
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝\x1b[0m \x1b[38;5;208mCode\x1b[0m 🦞\n\n\
  \x1b[2mModel\x1b[0m            {}\n\
  \x1b[2mPermissions\x1b[0m      {}\n\
  \x1b[2mDirectory\x1b[0m        {}\n\
  \x1b[2mSession\x1b[0m          {}\n\n\
  Type \x1b[1m/help\x1b[0m for commands · \x1b[2mShift+Enter\x1b[0m for newline",
            brand_model_name(&self.model),
            self.permission_mode.as_str(),
            cwd,
            self.session.id,
        )
    }

    pub(crate) fn run_turn(&mut self, input: &str) -> Result<(), Box<dyn std::error::Error>> {
        self.status_bar
            .begin_turn(self.runtime.usage().cumulative_usage());
        let _ = self.status_bar.render();
        let mut spinner = Spinner::new();
        let mut stdout = io::stdout();
        spinner.tick(
            "🦀 Thinking...",
            TerminalRenderer::new().color_theme(),
            &mut stdout,
        )?;
        let mut permission_prompter = CliPermissionPrompter::new(self.permission_mode);
        let result = self.runtime.run_turn(input, Some(&mut permission_prompter));
        match result {
            Ok(summary) => {
                spinner.finish(
                    "✨ Done",
                    TerminalRenderer::new().color_theme(),
                    &mut stdout,
                )?;
                println!();
                if let Some(event) = summary.auto_compaction {
                    println!(
                        "{}",
                        format_auto_compaction_notice(event.removed_message_count)
                    );
                }
                self.sync_status_bar();
                let _ = self.status_bar.render();
                self.persist_session()?;
                Ok(())
            }
            Err(error) => {
                spinner.fail(
                    "❌ Request failed",
                    TerminalRenderer::new().color_theme(),
                    &mut stdout,
                )?;
                self.sync_status_bar();
                let _ = self.status_bar.render();
                Err(Box::new(error))
            }
        }
    }

    pub(crate) fn run_turn_with_output(
        &mut self,
        input: &str,
        output_format: CliOutputFormat,
    ) -> Result<(), Box<dyn std::error::Error>> {
        match output_format {
            CliOutputFormat::Text => self.run_turn(input),
            CliOutputFormat::Json => self.run_prompt_json(input),
        }
    }

    pub(crate) fn run_prompt_json(
        &mut self,
        input: &str,
    ) -> Result<(), Box<dyn std::error::Error>> {
        let session = self.runtime.session().clone();
        let mut runtime = crate::build_runtime(
            session,
            self.model.clone(),
            self.system_prompt.clone(),
            true,
            false,
            self.allowed_tools.clone(),
            self.permission_mode,
            None,
        )?;
        let mut permission_prompter = CliPermissionPrompter::new(self.permission_mode);
        let summary = runtime.run_turn(input, Some(&mut permission_prompter))?;
        self.runtime = runtime;
        self.persist_session()?;
        println!(
            "{}",
            json!({
                "message": crate::final_assistant_text(&summary),
                "model": self.model,
                "iterations": summary.iterations,
                "auto_compaction": summary.auto_compaction.map(|event| json!({
                    "removed_messages": event.removed_message_count,
                    "notice": format_auto_compaction_notice(event.removed_message_count),
                })),
                "tool_uses": crate::collect_tool_uses(&summary),
                "tool_results": crate::collect_tool_results(&summary),
                "usage": {
                    "input_tokens": summary.usage.input_tokens,
                    "output_tokens": summary.usage.output_tokens,
                    "cache_creation_input_tokens": summary.usage.cache_creation_input_tokens,
                    "cache_read_input_tokens": summary.usage.cache_read_input_tokens,
                }
            })
        );
        Ok(())
    }

    pub(crate) fn handle_repl_command(
        &mut self,
        command: commands::SlashCommand,
    ) -> Result<bool, Box<dyn std::error::Error>> {
        Ok(match command {
            commands::SlashCommand::Help => {
                println!("{}", render_repl_help());
                false
            }
            commands::SlashCommand::Status => {
                self.print_status();
                false
            }
            commands::SlashCommand::Bughunter { scope } => {
                self.run_bughunter(scope.as_deref())?;
                false
            }
            commands::SlashCommand::Review { context } => {
                self.run_review(context.as_deref())?;
                false
            }
            commands::SlashCommand::Plan { task } => {
                self.run_plan(task.as_deref())?;
                false
            }
            commands::SlashCommand::Commit => {
                self.run_commit()?;
                true
            }
            commands::SlashCommand::Pr { context } => {
                self.run_pr(context.as_deref())?;
                false
            }
            commands::SlashCommand::Issue { context } => {
                self.run_issue(context.as_deref())?;
                false
            }
            commands::SlashCommand::Ultraplan { task } => {
                self.run_ultraplan(task.as_deref())?;
                false
            }
            commands::SlashCommand::Teleport { target } => {
                self.run_teleport(target.as_deref())?;
                false
            }
            commands::SlashCommand::DebugToolCall => {
                self.run_debug_tool_call()?;
                false
            }
            commands::SlashCommand::Compact => {
                self.compact()?;
                false
            }
            commands::SlashCommand::Model { model } => self.set_model(model)?,
            commands::SlashCommand::Permissions { mode } => self.set_permissions(mode)?,
            commands::SlashCommand::Clear { confirm } => self.clear_session(confirm)?,
            commands::SlashCommand::Cost => {
                self.print_cost();
                false
            }
            commands::SlashCommand::Login => {
                crate::run_login()?;
                false
            }
            commands::SlashCommand::Logout => {
                crate::run_logout()?;
                false
            }
            commands::SlashCommand::Resume { session_path } => self.resume_session(session_path)?,
            commands::SlashCommand::Config { section } => {
                Self::print_config(section.as_deref())?;
                false
            }
            commands::SlashCommand::Hooks { event } => {
                Self::print_hooks(event.as_deref())?;
                false
            }
            commands::SlashCommand::Mcp { server } => {
                Self::print_mcp(server.as_deref())?;
                false
            }
            commands::SlashCommand::Memory => {
                Self::print_memory()?;
                false
            }
            commands::SlashCommand::Agents { agent } => {
                Self::print_agents(agent.as_deref())?;
                false
            }
            commands::SlashCommand::Plugin { surface } => {
                Self::print_plugin(surface.as_deref())?;
                false
            }
            commands::SlashCommand::ReloadPlugins => {
                Self::print_reload_plugins()?;
                false
            }
            commands::SlashCommand::RemoteEnv => {
                Self::print_remote_env()?;
                false
            }
            commands::SlashCommand::RemoteSetup => {
                Self::print_remote_setup()?;
                false
            }
            commands::SlashCommand::Tools { tool } => {
                Self::print_tools(tool.as_deref())?;
                false
            }
            commands::SlashCommand::Doctor => {
                Self::print_doctor()?;
                false
            }
            commands::SlashCommand::Skills { skill } => {
                Self::print_skills(skill.as_deref())?;
                false
            }
            commands::SlashCommand::Tasks { task } => {
                Self::print_tasks(task.as_deref())?;
                false
            }
            commands::SlashCommand::Init => {
                crate::run_init()?;
                false
            }
            commands::SlashCommand::Diff => {
                Self::print_diff()?;
                false
            }
            commands::SlashCommand::Version => {
                Self::print_version();
                false
            }
            commands::SlashCommand::Export { path } => {
                self.export_session(path.as_deref())?;
                false
            }
            commands::SlashCommand::Session { action, target } => {
                self.handle_session_command(action.as_deref(), target.as_deref())?
            }
            commands::SlashCommand::Unknown(name) => {
                eprintln!("unknown slash command: /{name}");
                false
            }
        })
    }

    pub(crate) fn persist_session(&self) -> Result<(), Box<dyn std::error::Error>> {
        self.runtime.session().save_to_path(&self.session.path)?;
        Ok(())
    }

    pub(crate) fn render_status_bar(&self) -> io::Result<()> {
        self.status_bar.render()
    }

    pub(crate) fn clear_status_bar(&self) -> io::Result<()> {
        self.status_bar.clear()
    }

    fn print_status(&self) {
        let cumulative = self.runtime.usage().cumulative_usage();
        let latest = self.runtime.usage().current_turn_usage();
        println!(
            "{}",
            format_status_report(
                &self.model,
                StatusUsage {
                    message_count: self.runtime.session().messages.len(),
                    turns: self.runtime.usage().turns(),
                    latest,
                    cumulative,
                    estimated_tokens: self.runtime.estimated_tokens(),
                },
                self.permission_mode.as_str(),
                &status_context(Some(&self.session.path)).expect("status context should load"),
            )
        );
    }

    fn set_model(&mut self, model: Option<String>) -> Result<bool, Box<dyn std::error::Error>> {
        let Some(model) = model else {
            println!(
                "{}",
                format_model_report(
                    &self.model,
                    self.runtime.session().messages.len(),
                    self.runtime.usage().turns(),
                )
            );
            return Ok(false);
        };

        let model = resolve_model_alias(&model).to_string();

        if model == self.model {
            println!(
                "{}",
                format_model_report(
                    &self.model,
                    self.runtime.session().messages.len(),
                    self.runtime.usage().turns(),
                )
            );
            return Ok(false);
        }

        let previous = self.model.clone();
        let session = self.runtime.session().clone();
        let message_count = session.messages.len();
        self.runtime = crate::build_runtime(
            session,
            model.clone(),
            self.system_prompt.clone(),
            true,
            true,
            self.allowed_tools.clone(),
            self.permission_mode,
            Some(self.status_bar.clone()),
        )?;
        self.model.clone_from(&model);
        self.sync_status_bar();
        println!(
            "{}",
            format_model_switch_report(&previous, &model, message_count)
        );
        Ok(true)
    }

    fn set_permissions(
        &mut self,
        mode: Option<String>,
    ) -> Result<bool, Box<dyn std::error::Error>> {
        let Some(mode) = mode else {
            println!(
                "{}",
                format_permissions_report(self.permission_mode.as_str())
            );
            return Ok(false);
        };

        let normalized = normalize_permission_mode(&mode).ok_or_else(|| {
            format!(
                "unsupported permission mode '{mode}'. Use read-only, workspace-write, or danger-full-access."
            )
        })?;

        if normalized == self.permission_mode.as_str() {
            println!("{}", format_permissions_report(normalized));
            return Ok(false);
        }

        let previous = self.permission_mode.as_str().to_string();
        let session = self.runtime.session().clone();
        self.permission_mode = permission_mode_from_label(normalized);
        self.runtime = crate::build_runtime(
            session,
            self.model.clone(),
            self.system_prompt.clone(),
            true,
            true,
            self.allowed_tools.clone(),
            self.permission_mode,
            Some(self.status_bar.clone()),
        )?;
        self.sync_status_bar();
        println!(
            "{}",
            format_permissions_switch_report(&previous, normalized)
        );
        Ok(true)
    }

    fn clear_session(&mut self, confirm: bool) -> Result<bool, Box<dyn std::error::Error>> {
        if !confirm {
            println!(
                "clear: confirmation required; run /clear --confirm to start a fresh session."
            );
            return Ok(false);
        }

        self.session = create_managed_session_handle()?;
        self.runtime = crate::build_runtime(
            Session::new(),
            self.model.clone(),
            self.system_prompt.clone(),
            true,
            true,
            self.allowed_tools.clone(),
            self.permission_mode,
            Some(self.status_bar.clone()),
        )?;
        self.sync_status_bar();
        println!(
            "Session cleared\n  Mode             fresh session\n  Preserved model  {}\n  Permission mode  {}\n  Session          {}",
            self.model,
            self.permission_mode.as_str(),
            self.session.id,
        );
        Ok(true)
    }

    fn print_cost(&self) {
        let cumulative = self.runtime.usage().cumulative_usage();
        println!("{}", format_cost_report(cumulative));
    }

    fn resume_session(
        &mut self,
        session_path: Option<String>,
    ) -> Result<bool, Box<dyn std::error::Error>> {
        let Some(session_ref) = session_path else {
            println!("Usage: /resume <session-path>");
            return Ok(false);
        };

        let handle = resolve_session_reference(&session_ref)?;
        let session = Session::load_from_path(&handle.path)?;
        let message_count = session.messages.len();
        self.runtime = crate::build_runtime(
            session,
            self.model.clone(),
            self.system_prompt.clone(),
            true,
            true,
            self.allowed_tools.clone(),
            self.permission_mode,
            Some(self.status_bar.clone()),
        )?;
        self.session = handle;
        self.sync_status_bar();
        println!(
            "{}",
            format_resume_report(
                &self.session.path.display().to_string(),
                message_count,
                self.runtime.usage().turns(),
            )
        );
        Ok(true)
    }

    fn print_config(section: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_config_report(section)?);
        Ok(())
    }

    fn print_hooks(event: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_hooks_report(event)?);
        Ok(())
    }

    fn print_memory() -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_memory_report()?);
        Ok(())
    }

    fn print_mcp(server: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_mcp_report(server)?);
        Ok(())
    }

    fn print_skills(skill: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_skills_report(skill)?);
        Ok(())
    }

    fn print_agents(agent: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_agents_report(agent)?);
        Ok(())
    }

    fn print_plugin(surface: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_plugin_report(surface)?);
        Ok(())
    }

    fn print_reload_plugins() -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_reload_plugins_report()?);
        Ok(())
    }

    fn print_remote_env() -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_remote_env_report()?);
        Ok(())
    }

    fn print_remote_setup() -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_remote_setup_report()?);
        Ok(())
    }

    fn print_tools(tool: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_tools_report(tool)?);
        Ok(())
    }

    fn print_doctor() -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_doctor_report()?);
        Ok(())
    }

    fn print_tasks(task: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_tasks_report(task)?);
        Ok(())
    }

    fn print_diff() -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_diff_report()?);
        Ok(())
    }

    fn print_version() {
        println!("{}", render_version_report());
    }

    fn export_session(
        &self,
        requested_path: Option<&str>,
    ) -> Result<(), Box<dyn std::error::Error>> {
        let export_path = crate::resolve_export_path(requested_path, self.runtime.session())?;
        fs::write(
            &export_path,
            crate::render_export_text(self.runtime.session()),
        )?;
        println!(
            "Export\n  Result           wrote transcript\n  File             {}\n  Messages         {}",
            export_path.display(),
            self.runtime.session().messages.len(),
        );
        Ok(())
    }

    fn handle_session_command(
        &mut self,
        action: Option<&str>,
        target: Option<&str>,
    ) -> Result<bool, Box<dyn std::error::Error>> {
        match action {
            None | Some("list") => {
                println!("{}", render_session_list(&self.session.id)?);
                Ok(false)
            }
            Some("switch") => {
                let Some(target) = target else {
                    println!("Usage: /session switch <session-id>");
                    return Ok(false);
                };
                let handle = resolve_session_reference(target)?;
                let session = Session::load_from_path(&handle.path)?;
                let message_count = session.messages.len();
                self.runtime = crate::build_runtime(
                    session,
                    self.model.clone(),
                    self.system_prompt.clone(),
                    true,
                    true,
                    self.allowed_tools.clone(),
                    self.permission_mode,
                    Some(self.status_bar.clone()),
                )?;
                self.session = handle;
                self.sync_status_bar();
                println!(
                    "Session switched\n  Active session   {}\n  File             {}\n  Messages         {}",
                    self.session.id,
                    self.session.path.display(),
                    message_count,
                );
                Ok(true)
            }
            Some(other) => {
                println!("Unknown /session action '{other}'. Use /session list or /session switch <session-id>.");
                Ok(false)
            }
        }
    }

    fn compact(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        let result = self.runtime.compact(CompactionConfig::default());
        let removed = result.removed_message_count;
        let kept = result.compacted_session.messages.len();
        let skipped = removed == 0;
        self.runtime = crate::build_runtime(
            result.compacted_session,
            self.model.clone(),
            self.system_prompt.clone(),
            true,
            true,
            self.allowed_tools.clone(),
            self.permission_mode,
            Some(self.status_bar.clone()),
        )?;
        self.sync_status_bar();
        self.persist_session()?;
        println!("{}", format_compact_report(removed, kept, skipped));
        Ok(())
    }

    fn run_internal_prompt_text(
        &self,
        prompt: &str,
        enable_tools: bool,
    ) -> Result<String, Box<dyn std::error::Error>> {
        let session = self.runtime.session().clone();
        let mut runtime = crate::build_runtime(
            session,
            self.model.clone(),
            self.system_prompt.clone(),
            enable_tools,
            false,
            self.allowed_tools.clone(),
            self.permission_mode,
            None,
        )?;
        let mut permission_prompter = CliPermissionPrompter::new(self.permission_mode);
        let summary = runtime.run_turn(prompt, Some(&mut permission_prompter))?;
        Ok(crate::final_assistant_text(&summary).trim().to_string())
    }

    fn run_bughunter(&self, scope: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        let scope = scope.unwrap_or("the current repository");
        let prompt = format!(
            "You are /bughunter. Inspect {scope} and identify the most likely bugs or correctness issues. Prioritize concrete findings with file paths, severity, and suggested fixes. Use tools if needed."
        );
        println!("{}", self.run_internal_prompt_text(&prompt, true)?);
        Ok(())
    }

    fn run_review(&self, context: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        let context = context.unwrap_or("the current change or active code path");
        let prompt = format!(
            "You are /review. Review {context}. Prioritize concrete findings with severity, file paths, behavioral regressions, and missing tests. Put findings first. If no significant issues are found, say that explicitly and mention residual risks or test gaps. Use tools if needed."
        );
        println!("{}", self.run_internal_prompt_text(&prompt, true)?);
        Ok(())
    }

    fn run_plan(&self, task: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        let task = task.unwrap_or("the current repo work");
        let prompt = format!(
            "You are /plan. Produce a practical implementation plan for {task}. Keep it concise but actionable. Include goals, ordered steps, main risks, and verification. Use tools if needed."
        );
        println!("{}", self.run_internal_prompt_text(&prompt, true)?);
        Ok(())
    }

    fn run_ultraplan(&self, task: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        let task = task.unwrap_or("the current repo work");
        let prompt = format!(
            "You are /ultraplan. Produce a deep multi-step execution plan for {task}. Include goals, risks, implementation sequence, verification steps, and rollback considerations. Use tools if needed."
        );
        println!("{}", self.run_internal_prompt_text(&prompt, true)?);
        Ok(())
    }

    fn run_teleport(&self, target: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        let Some(target) = target.map(str::trim).filter(|value| !value.is_empty()) else {
            println!("Usage: /teleport <symbol-or-path>");
            return Ok(());
        };

        println!("{}", render_teleport_report(target)?);
        Ok(())
    }

    fn run_debug_tool_call(&self) -> Result<(), Box<dyn std::error::Error>> {
        println!("{}", render_last_tool_debug_report(self.runtime.session())?);
        Ok(())
    }

    fn create_status_bar(
        model: &str,
        permission_mode: PermissionMode,
        session: &SessionHandle,
    ) -> StatusBarHandle {
        let show_turn_duration = env::current_dir()
            .ok()
            .and_then(|cwd| ConfigLoader::default_for(cwd).load().ok())
            .and_then(|config| {
                config
                    .get("showTurnDuration")
                    .and_then(|value| value.as_bool())
            })
            .unwrap_or(false);
        let git_branch = status_context(Some(&session.path))
            .ok()
            .and_then(|context| context.git_branch);

        StatusBarHandle::new(
            model.to_string(),
            permission_mode.as_str().to_string(),
            session.id.clone(),
            git_branch,
            show_turn_duration,
        )
    }

    fn sync_status_bar(&self) {
        self.status_bar.set_model(self.model.clone());
        self.status_bar
            .set_permission_mode(self.permission_mode.as_str().to_string());
        self.status_bar.set_session_id(self.session.id.clone());
        self.status_bar
            .set_cumulative_usage(self.runtime.usage().cumulative_usage());
        self.status_bar
            .finish_turn(self.runtime.usage().cumulative_usage());
        if let Ok(context) = status_context(Some(&self.session.path)) {
            self.status_bar.set_git_branch(context.git_branch);
        }
    }

    fn run_commit(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        let status = crate::git_output(&["status", "--short"])?;
        if status.trim().is_empty() {
            println!("Commit\n  Result           skipped\n  Reason           no workspace changes");
            return Ok(());
        }

        crate::git_status_ok(&["add", "-A"])?;
        let staged_stat = crate::git_output(&["diff", "--cached", "--stat"])?;
        let prompt = format!(
            "Generate a git commit message in plain text Lore format only. Base it on this staged diff summary:\n\n{}\n\nRecent conversation context:\n{}",
            crate::truncate_for_prompt(&staged_stat, 8_000),
            crate::recent_user_context(self.runtime.session(), 6)
        );
        let message =
            crate::sanitize_generated_message(&self.run_internal_prompt_text(&prompt, false)?);
        if message.trim().is_empty() {
            return Err("generated commit message was empty".into());
        }

        let path = crate::write_temp_text_file("claw-commit-message.txt", &message)?;
        let output = Command::new("git")
            .args(["commit", "--file"])
            .arg(&path)
            .current_dir(env::current_dir()?)
            .output()?;
        if !output.status.success() {
            let stderr = String::from_utf8_lossy(&output.stderr).trim().to_string();
            return Err(format!("git commit failed: {stderr}").into());
        }

        println!(
            "Commit\n  Result           created\n  Message file     {}\n\n{}",
            path.display(),
            message.trim(),
        );
        Ok(())
    }

    fn run_pr(&self, context: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        let staged = crate::git_output(&["diff", "--stat"])?;
        let prompt = format!(
            "Generate a pull request title and body from this conversation and diff summary. Output plain text in this format exactly:\nTITLE: <title>\nBODY:\n<body markdown>\n\nContext hint: {}\n\nDiff summary:\n{}",
            context.unwrap_or("none"),
            crate::truncate_for_prompt(&staged, 10_000)
        );
        let draft =
            crate::sanitize_generated_message(&self.run_internal_prompt_text(&prompt, false)?);
        let (title, body) = crate::parse_titled_body(&draft)
            .ok_or_else(|| "failed to parse generated PR title/body".to_string())?;

        if crate::command_exists("gh") {
            let body_path = crate::write_temp_text_file("claw-pr-body.md", &body)?;
            let output = Command::new("gh")
                .args(["pr", "create", "--title", &title, "--body-file"])
                .arg(&body_path)
                .current_dir(env::current_dir()?)
                .output()?;
            if output.status.success() {
                let stdout = String::from_utf8_lossy(&output.stdout).trim().to_string();
                println!(
                    "PR\n  Result           created\n  Title            {title}\n  URL              {}",
                    if stdout.is_empty() { "<unknown>" } else { &stdout }
                );
                return Ok(());
            }
        }

        println!("PR draft\n  Title            {title}\n\n{body}");
        Ok(())
    }

    fn run_issue(&self, context: Option<&str>) -> Result<(), Box<dyn std::error::Error>> {
        let prompt = format!(
            "Generate a GitHub issue title and body from this conversation. Output plain text in this format exactly:\nTITLE: <title>\nBODY:\n<body markdown>\n\nContext hint: {}\n\nConversation context:\n{}",
            context.unwrap_or("none"),
            crate::truncate_for_prompt(&crate::recent_user_context(self.runtime.session(), 10), 10_000)
        );
        let draft =
            crate::sanitize_generated_message(&self.run_internal_prompt_text(&prompt, false)?);
        let (title, body) = crate::parse_titled_body(&draft)
            .ok_or_else(|| "failed to parse generated issue title/body".to_string())?;

        if crate::command_exists("gh") {
            let body_path = crate::write_temp_text_file("claw-issue-body.md", &body)?;
            let output = Command::new("gh")
                .args(["issue", "create", "--title", &title, "--body-file"])
                .arg(&body_path)
                .current_dir(env::current_dir()?)
                .output()?;
            if output.status.success() {
                let stdout = String::from_utf8_lossy(&output.stdout).trim().to_string();
                println!(
                    "Issue\n  Result           created\n  Title            {title}\n  URL              {}",
                    if stdout.is_empty() { "<unknown>" } else { &stdout }
                );
                return Ok(());
            }
        }

        println!("Issue draft\n  Title            {title}\n\n{body}");
        Ok(())
    }
}
