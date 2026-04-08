use runtime::{compact_session, CompactionConfig, Session};

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct CommandManifestEntry {
    pub name: String,
    pub source: CommandSource,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum CommandSource {
    Builtin,
    InternalOnly,
    FeatureGated,
}

#[derive(Debug, Clone, Default, PartialEq, Eq)]
pub struct CommandRegistry {
    entries: Vec<CommandManifestEntry>,
}

impl CommandRegistry {
    #[must_use]
    pub fn new(entries: Vec<CommandManifestEntry>) -> Self {
        Self { entries }
    }

    #[must_use]
    pub fn entries(&self) -> &[CommandManifestEntry] {
        &self.entries
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct SlashCommandSpec {
    pub name: &'static str,
    pub summary: &'static str,
    pub argument_hint: Option<&'static str>,
    pub resume_supported: bool,
}

const SLASH_COMMAND_SPECS: &[SlashCommandSpec] = &[
    SlashCommandSpec {
        name: "help",
        summary: "Show available slash commands",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "status",
        summary: "Show current session status",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "compact",
        summary: "Compact local session history",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "model",
        summary: "Show or switch the active model",
        argument_hint: Some("[model]"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "permissions",
        summary: "Show or switch the active permission mode",
        argument_hint: Some("[read-only|workspace-write|danger-full-access]"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "clear",
        summary: "Start a fresh local session",
        argument_hint: Some("[--confirm]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "cost",
        summary: "Show cumulative token usage for this session",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "dump-manifests",
        summary: "Show archived manifest counts for commands, tools, and bootstrap",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "bootstrap-plan",
        summary: "Show the default runtime bootstrap phases",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "login",
        summary: "Authenticate with Simcoe AI using OAuth",
        argument_hint: None,
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "logout",
        summary: "Clear stored Simcoe AI OAuth credentials",
        argument_hint: None,
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "resume",
        summary: "Load a saved session into the REPL",
        argument_hint: Some("<session-path>"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "system-prompt",
        summary: "Render the current system prompt scaffold",
        argument_hint: Some("[--cwd PATH] [--date YYYY-MM-DD]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "config",
        summary: "Inspect Simcoe AI config files or merged sections",
        argument_hint: Some("[env|hooks|model]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "hooks",
        summary: "Inspect configured pre/post tool hooks",
        argument_hint: Some("[pre|post]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "mcp",
        summary: "Inspect configured MCP servers or one server",
        argument_hint: Some("[server]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "memory",
        summary: "Inspect loaded Simcoe AI instruction memory files",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "agents",
        summary: "Inspect built-in sub-agent profiles or one profile",
        argument_hint: Some("[name]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "plugin",
        summary: "Inspect archived plugin surfaces or one surface",
        argument_hint: Some("[name]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "reload-plugins",
        summary: "Inspect the archived plugin reload flow",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "remote-env",
        summary: "Inspect current remote-session bootstrap environment",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "remote-setup",
        summary: "Inspect archived remote setup and transport surfaces",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "tools",
        summary: "Inspect Rust tool specs or archived TS tool families",
        argument_hint: Some("[name]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "doctor",
        summary: "Inspect workspace and runtime readiness diagnostics",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "skills",
        summary: "List available local skills or inspect one",
        argument_hint: Some("[skill]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "tasks",
        summary: "Inspect persisted sub-agent tasks or one task",
        argument_hint: Some("[id]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "init",
        summary: "Create a starter SIMCOE.md for this repo",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "diff",
        summary: "Show git diff for current workspace changes",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "version",
        summary: "Show CLI version and build information",
        argument_hint: None,
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "bughunter",
        summary: "Inspect the codebase for likely bugs",
        argument_hint: Some("[scope]"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "review",
        summary: "Review a change, file, or code path for issues",
        argument_hint: Some("[context]"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "plan",
        summary: "Generate a practical implementation plan",
        argument_hint: Some("[task]"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "commit",
        summary: "Generate a commit message and create a git commit",
        argument_hint: None,
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "pr",
        summary: "Draft or create a pull request from the conversation",
        argument_hint: Some("[context]"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "issue",
        summary: "Draft or create a GitHub issue from the conversation",
        argument_hint: Some("[context]"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "ultraplan",
        summary: "Run a deep planning prompt with multi-step reasoning",
        argument_hint: Some("[task]"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "teleport",
        summary: "Jump to a file or symbol by searching the workspace",
        argument_hint: Some("<symbol-or-path>"),
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "debug-tool-call",
        summary: "Replay the last tool call with debug details",
        argument_hint: None,
        resume_supported: false,
    },
    SlashCommandSpec {
        name: "export",
        summary: "Export the current conversation to a file",
        argument_hint: Some("[file]"),
        resume_supported: true,
    },
    SlashCommandSpec {
        name: "session",
        summary: "List or switch managed local sessions",
        argument_hint: Some("[list|switch <session-id>]"),
        resume_supported: true,
    },
];

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum SlashCommand {
    Help,
    Status,
    Compact,
    Bughunter {
        scope: Option<String>,
    },
    Review {
        context: Option<String>,
    },
    Plan {
        task: Option<String>,
    },
    Commit,
    Pr {
        context: Option<String>,
    },
    Issue {
        context: Option<String>,
    },
    Ultraplan {
        task: Option<String>,
    },
    Teleport {
        target: Option<String>,
    },
    DebugToolCall,
    Model {
        model: Option<String>,
    },
    Permissions {
        mode: Option<String>,
    },
    Clear {
        confirm: bool,
    },
    Cost,
    DumpManifests,
    BootstrapPlan,
    Login,
    Logout,
    Resume {
        session_path: Option<String>,
    },
    SystemPrompt {
        args: Option<String>,
    },
    Config {
        section: Option<String>,
    },
    Hooks {
        event: Option<String>,
    },
    Mcp {
        server: Option<String>,
    },
    Memory,
    Agents {
        agent: Option<String>,
    },
    Plugin {
        surface: Option<String>,
    },
    ReloadPlugins,
    RemoteEnv,
    RemoteSetup,
    Tools {
        tool: Option<String>,
    },
    Doctor,
    Skills {
        skill: Option<String>,
    },
    Tasks {
        task: Option<String>,
    },
    Init,
    Diff,
    Version,
    Export {
        path: Option<String>,
    },
    Session {
        action: Option<String>,
        target: Option<String>,
    },
    Unknown(String),
}

impl SlashCommand {
    #[must_use]
    pub fn parse(input: &str) -> Option<Self> {
        let trimmed = input.trim();
        if !trimmed.starts_with('/') {
            return None;
        }

        let mut parts = trimmed.trim_start_matches('/').split_whitespace();
        let command = parts.next().unwrap_or_default();
        Some(match command {
            "help" => Self::Help,
            "status" => Self::Status,
            "compact" => Self::Compact,
            "bughunter" => Self::Bughunter {
                scope: remainder_after_command(trimmed, command),
            },
            "review" => Self::Review {
                context: remainder_after_command(trimmed, command),
            },
            "plan" => Self::Plan {
                task: remainder_after_command(trimmed, command),
            },
            "commit" => Self::Commit,
            "pr" => Self::Pr {
                context: remainder_after_command(trimmed, command),
            },
            "issue" => Self::Issue {
                context: remainder_after_command(trimmed, command),
            },
            "ultraplan" => Self::Ultraplan {
                task: remainder_after_command(trimmed, command),
            },
            "teleport" => Self::Teleport {
                target: remainder_after_command(trimmed, command),
            },
            "debug-tool-call" => Self::DebugToolCall,
            "model" => Self::Model {
                model: parts.next().map(ToOwned::to_owned),
            },
            "permissions" => Self::Permissions {
                mode: parts.next().map(ToOwned::to_owned),
            },
            "clear" => Self::Clear {
                confirm: parts.next() == Some("--confirm"),
            },
            "cost" => Self::Cost,
            "dump-manifests" => Self::DumpManifests,
            "bootstrap-plan" => Self::BootstrapPlan,
            "login" => Self::Login,
            "logout" => Self::Logout,
            "resume" => Self::Resume {
                session_path: parts.next().map(ToOwned::to_owned),
            },
            "system-prompt" => Self::SystemPrompt {
                args: remainder_after_command(trimmed, command),
            },
            "config" => Self::Config {
                section: parts.next().map(ToOwned::to_owned),
            },
            "hooks" => Self::Hooks {
                event: remainder_after_command(trimmed, command),
            },
            "mcp" => Self::Mcp {
                server: remainder_after_command(trimmed, command),
            },
            "memory" => Self::Memory,
            "agents" => Self::Agents {
                agent: remainder_after_command(trimmed, command),
            },
            "plugin" => Self::Plugin {
                surface: remainder_after_command(trimmed, command),
            },
            "reload-plugins" => Self::ReloadPlugins,
            "remote-env" => Self::RemoteEnv,
            "remote-setup" => Self::RemoteSetup,
            "tools" => Self::Tools {
                tool: remainder_after_command(trimmed, command),
            },
            "doctor" => Self::Doctor,
            "skills" => Self::Skills {
                skill: remainder_after_command(trimmed, command),
            },
            "tasks" => Self::Tasks {
                task: remainder_after_command(trimmed, command),
            },
            "init" => Self::Init,
            "diff" => Self::Diff,
            "version" => Self::Version,
            "export" => Self::Export {
                path: parts.next().map(ToOwned::to_owned),
            },
            "session" => Self::Session {
                action: parts.next().map(ToOwned::to_owned),
                target: parts.next().map(ToOwned::to_owned),
            },
            other => Self::Unknown(other.to_string()),
        })
    }
}

fn remainder_after_command(input: &str, command: &str) -> Option<String> {
    input
        .trim()
        .strip_prefix(&format!("/{command}"))
        .map(str::trim)
        .filter(|value| !value.is_empty())
        .map(ToOwned::to_owned)
}

#[must_use]
pub fn slash_command_specs() -> &'static [SlashCommandSpec] {
    SLASH_COMMAND_SPECS
}

#[must_use]
pub fn resume_supported_slash_commands() -> Vec<&'static SlashCommandSpec> {
    slash_command_specs()
        .iter()
        .filter(|spec| spec.resume_supported)
        .collect()
}

#[must_use]
pub fn render_slash_command_help() -> String {
    let mut lines = vec![
        "Slash commands".to_string(),
        "  [resume] means the command also works with --resume SESSION.json".to_string(),
    ];
    for spec in slash_command_specs() {
        let name = match spec.argument_hint {
            Some(argument_hint) => format!("/{} {}", spec.name, argument_hint),
            None => format!("/{}", spec.name),
        };
        let resume = if spec.resume_supported {
            " [resume]"
        } else {
            ""
        };
        lines.push(format!("  {name:<20} {}{}", spec.summary, resume));
    }
    lines.join("\n")
}

#[must_use]
pub fn render_resume_command_help() -> String {
    let mut lines = vec![
        "Resume-compatible slash commands".to_string(),
        "  These commands work with --resume SESSION.json.".to_string(),
    ];
    for spec in resume_supported_slash_commands() {
        let name = match spec.argument_hint {
            Some(argument_hint) => format!("/{} {}", spec.name, argument_hint),
            None => format!("/{}", spec.name),
        };
        lines.push(format!("  {name:<20} {}", spec.summary));
    }
    lines.join("\n")
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct SlashCommandResult {
    pub message: String,
    pub session: Session,
}

#[must_use]
pub fn handle_slash_command(
    input: &str,
    session: &Session,
    compaction: CompactionConfig,
) -> Option<SlashCommandResult> {
    match SlashCommand::parse(input)? {
        SlashCommand::Compact => {
            let result = compact_session(session, compaction);
            let message = if result.removed_message_count == 0 {
                "Compaction skipped: session is below the compaction threshold.".to_string()
            } else {
                format!(
                    "Compacted {} messages into a resumable system summary.",
                    result.removed_message_count
                )
            };
            Some(SlashCommandResult {
                message,
                session: result.compacted_session,
            })
        }
        SlashCommand::Help => Some(SlashCommandResult {
            message: render_slash_command_help(),
            session: session.clone(),
        }),
        SlashCommand::Status
        | SlashCommand::Bughunter { .. }
        | SlashCommand::Review { .. }
        | SlashCommand::Plan { .. }
        | SlashCommand::Commit
        | SlashCommand::Pr { .. }
        | SlashCommand::Issue { .. }
        | SlashCommand::Ultraplan { .. }
        | SlashCommand::Teleport { .. }
        | SlashCommand::DebugToolCall
        | SlashCommand::Model { .. }
        | SlashCommand::Permissions { .. }
        | SlashCommand::Clear { .. }
        | SlashCommand::Cost
        | SlashCommand::DumpManifests
        | SlashCommand::BootstrapPlan
        | SlashCommand::Login
        | SlashCommand::Logout
        | SlashCommand::Resume { .. }
        | SlashCommand::SystemPrompt { .. }
        | SlashCommand::Config { .. }
        | SlashCommand::Hooks { .. }
        | SlashCommand::Mcp { .. }
        | SlashCommand::Memory
        | SlashCommand::Agents { .. }
        | SlashCommand::Plugin { .. }
        | SlashCommand::ReloadPlugins
        | SlashCommand::RemoteEnv
        | SlashCommand::RemoteSetup
        | SlashCommand::Tools { .. }
        | SlashCommand::Doctor
        | SlashCommand::Skills { .. }
        | SlashCommand::Tasks { .. }
        | SlashCommand::Init
        | SlashCommand::Diff
        | SlashCommand::Version
        | SlashCommand::Export { .. }
        | SlashCommand::Session { .. }
        | SlashCommand::Unknown(_) => None,
    }
}

#[cfg(test)]
mod tests {
    use super::{
        handle_slash_command, render_resume_command_help, render_slash_command_help,
        resume_supported_slash_commands, slash_command_specs, SlashCommand,
    };
    use runtime::{CompactionConfig, ContentBlock, ConversationMessage, MessageRole, Session};

    #[test]
    fn parses_supported_slash_commands() {
        assert_eq!(SlashCommand::parse("/help"), Some(SlashCommand::Help));
        assert_eq!(SlashCommand::parse(" /status "), Some(SlashCommand::Status));
        assert_eq!(
            SlashCommand::parse("/bughunter runtime"),
            Some(SlashCommand::Bughunter {
                scope: Some("runtime".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/review auth flow"),
            Some(SlashCommand::Review {
                context: Some("auth flow".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/plan ship hook runner"),
            Some(SlashCommand::Plan {
                task: Some("ship hook runner".to_string())
            })
        );
        assert_eq!(SlashCommand::parse("/commit"), Some(SlashCommand::Commit));
        assert_eq!(
            SlashCommand::parse("/pr ready for review"),
            Some(SlashCommand::Pr {
                context: Some("ready for review".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/issue flaky test"),
            Some(SlashCommand::Issue {
                context: Some("flaky test".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/ultraplan ship both features"),
            Some(SlashCommand::Ultraplan {
                task: Some("ship both features".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/teleport conversation.rs"),
            Some(SlashCommand::Teleport {
                target: Some("conversation.rs".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/debug-tool-call"),
            Some(SlashCommand::DebugToolCall)
        );
        assert_eq!(
            SlashCommand::parse("/model simcoe-opus"),
            Some(SlashCommand::Model {
                model: Some("simcoe-opus".to_string()),
            })
        );
        assert_eq!(
            SlashCommand::parse("/model"),
            Some(SlashCommand::Model { model: None })
        );
        assert_eq!(
            SlashCommand::parse("/permissions read-only"),
            Some(SlashCommand::Permissions {
                mode: Some("read-only".to_string()),
            })
        );
        assert_eq!(
            SlashCommand::parse("/clear"),
            Some(SlashCommand::Clear { confirm: false })
        );
        assert_eq!(
            SlashCommand::parse("/clear --confirm"),
            Some(SlashCommand::Clear { confirm: true })
        );
        assert_eq!(SlashCommand::parse("/cost"), Some(SlashCommand::Cost));
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
            SlashCommand::parse("/resume session.json"),
            Some(SlashCommand::Resume {
                session_path: Some("session.json".to_string()),
            })
        );
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
            SlashCommand::parse("/agents explore"),
            Some(SlashCommand::Agents {
                agent: Some("explore".to_string())
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
            SlashCommand::parse("/skills"),
            Some(SlashCommand::Skills { skill: None })
        );
        assert_eq!(
            SlashCommand::parse("/skills help"),
            Some(SlashCommand::Skills {
                skill: Some("help".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/tasks agent-123"),
            Some(SlashCommand::Tasks {
                task: Some("agent-123".to_string())
            })
        );
        assert_eq!(SlashCommand::parse("/init"), Some(SlashCommand::Init));
        assert_eq!(SlashCommand::parse("/diff"), Some(SlashCommand::Diff));
        assert_eq!(SlashCommand::parse("/version"), Some(SlashCommand::Version));
        assert_eq!(
            SlashCommand::parse("/export notes.txt"),
            Some(SlashCommand::Export {
                path: Some("notes.txt".to_string())
            })
        );
        assert_eq!(
            SlashCommand::parse("/session switch abc123"),
            Some(SlashCommand::Session {
                action: Some("switch".to_string()),
                target: Some("abc123".to_string())
            })
        );
    }

    #[test]
    fn renders_help_from_shared_specs() {
        let help = render_slash_command_help();
        assert!(help.contains("works with --resume SESSION.json"));
        assert!(help.contains("/help"));
        assert!(help.contains("/status"));
        assert!(help.contains("/compact"));
        assert!(help.contains("/bughunter [scope]"));
        assert!(help.contains("/commit"));
        assert!(help.contains("/pr [context]"));
        assert!(help.contains("/issue [context]"));
        assert!(help.contains("/ultraplan [task]"));
        assert!(help.contains("/teleport <symbol-or-path>"));
        assert!(help.contains("/debug-tool-call"));
        assert!(help.contains("/model [model]"));
        assert!(help.contains("/permissions [read-only|workspace-write|danger-full-access]"));
        assert!(help.contains("/clear [--confirm]"));
        assert!(help.contains("/cost"));
        assert!(help.contains("/dump-manifests"));
        assert!(help.contains("/bootstrap-plan"));
        assert!(help.contains("/resume <session-path>"));
        assert!(help.contains("/login"));
        assert!(help.contains("/logout"));
        assert!(help.contains("/system-prompt [--cwd PATH] [--date YYYY-MM-DD]"));
        assert!(help.contains("/config [env|hooks|model]"));
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
        assert!(help.contains("/init"));
        assert!(help.contains("/diff"));
        assert!(help.contains("/version"));
        assert!(help.contains("/review [context]"));
        assert!(help.contains("/plan [task]"));
        assert!(help.contains("/export [file]"));
        assert!(help.contains("/session [list|switch <session-id>]"));
        assert_eq!(slash_command_specs().len(), 40);
        assert_eq!(resume_supported_slash_commands().len(), 26);
    }

    #[test]
    fn renders_resume_help_from_resume_supported_specs() {
        let help = render_resume_command_help();

        assert!(help.contains("Resume-compatible slash commands"));
        assert!(help.contains("/help"));
        assert!(help.contains("/config [env|hooks|model]"));
        assert!(help.contains("/export [file]"));
        assert!(help.contains("/session [list|switch <session-id>]"));
        assert!(!help.contains("/review [context]"));
        assert!(!help.contains("/login"));
    }

    #[test]
    fn compacts_sessions_via_slash_command() {
        let session = Session {
            version: 1,
            messages: vec![
                ConversationMessage::user_text("a ".repeat(200)),
                ConversationMessage::assistant(vec![ContentBlock::Text {
                    text: "b ".repeat(200),
                }]),
                ConversationMessage::tool_result("1", "bash", "ok ".repeat(200), false),
                ConversationMessage::assistant(vec![ContentBlock::Text {
                    text: "recent".to_string(),
                }]),
            ],
        };

        let result = handle_slash_command(
            "/compact",
            &session,
            CompactionConfig {
                preserve_recent_messages: 2,
                max_estimated_tokens: 1,
            },
        )
        .expect("slash command should be handled");

        assert!(result.message.contains("Compacted 2 messages"));
        assert_eq!(result.session.messages[0].role, MessageRole::System);
    }

    #[test]
    fn help_command_is_non_mutating() {
        let session = Session::new();
        let result = handle_slash_command("/help", &session, CompactionConfig::default())
            .expect("help command should be handled");
        assert_eq!(result.session, session);
        assert!(result.message.contains("Slash commands"));
    }

    #[test]
    fn ignores_unknown_or_runtime_bound_slash_commands() {
        let session = Session::new();
        assert!(handle_slash_command("/unknown", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/status", &session, CompactionConfig::default()).is_none());
        assert!(
            handle_slash_command("/bughunter", &session, CompactionConfig::default()).is_none()
        );
        assert!(handle_slash_command("/review", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/plan", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/commit", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/pr", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/issue", &session, CompactionConfig::default()).is_none());
        assert!(
            handle_slash_command("/ultraplan", &session, CompactionConfig::default()).is_none()
        );
        assert!(
            handle_slash_command("/teleport foo", &session, CompactionConfig::default()).is_none()
        );
        assert!(
            handle_slash_command("/debug-tool-call", &session, CompactionConfig::default())
                .is_none()
        );
        assert!(
            handle_slash_command("/model simcoe", &session, CompactionConfig::default()).is_none()
        );
        assert!(handle_slash_command(
            "/permissions read-only",
            &session,
            CompactionConfig::default()
        )
        .is_none());
        assert!(handle_slash_command("/clear", &session, CompactionConfig::default()).is_none());
        assert!(
            handle_slash_command("/clear --confirm", &session, CompactionConfig::default())
                .is_none()
        );
        assert!(handle_slash_command("/cost", &session, CompactionConfig::default()).is_none());
        assert!(
            handle_slash_command("/dump-manifests", &session, CompactionConfig::default())
                .is_none()
        );
        assert!(
            handle_slash_command("/bootstrap-plan", &session, CompactionConfig::default())
                .is_none()
        );
        assert!(handle_slash_command("/login", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/logout", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command(
            "/resume session.json",
            &session,
            CompactionConfig::default()
        )
        .is_none());
        assert!(
            handle_slash_command("/system-prompt", &session, CompactionConfig::default()).is_none()
        );
        assert!(handle_slash_command("/config", &session, CompactionConfig::default()).is_none());
        assert!(
            handle_slash_command("/config env", &session, CompactionConfig::default()).is_none()
        );
        assert!(handle_slash_command("/hooks", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/mcp", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/agents", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/plugin", &session, CompactionConfig::default()).is_none());
        assert!(
            handle_slash_command("/reload-plugins", &session, CompactionConfig::default())
                .is_none()
        );
        assert!(
            handle_slash_command("/remote-env", &session, CompactionConfig::default()).is_none()
        );
        assert!(
            handle_slash_command("/remote-setup", &session, CompactionConfig::default()).is_none()
        );
        assert!(handle_slash_command("/tools", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/doctor", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/skills", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/tasks", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/diff", &session, CompactionConfig::default()).is_none());
        assert!(handle_slash_command("/version", &session, CompactionConfig::default()).is_none());
        assert!(
            handle_slash_command("/export note.txt", &session, CompactionConfig::default())
                .is_none()
        );
        assert!(
            handle_slash_command("/session list", &session, CompactionConfig::default()).is_none()
        );
    }
}
