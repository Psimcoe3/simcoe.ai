# PARITY GAP ANALYSIS

Scope: read-only comparison between the original TypeScript source at `/home/bellman/Workspace/claude-code/src/` and the Rust port under `rust/crates/`.

Method: compared feature surfaces, registries, entrypoints, and runtime plumbing only. No TypeScript source was copied.

## Executive summary

The Rust port has a good foundation for:
- Anthropic API/OAuth basics
- local conversation/session state
- a core tool loop
- MCP stdio/bootstrap support
- CLAUDE.md discovery
- a small but usable built-in tool set

It is **not feature-parity** with the TypeScript CLI.

Largest gaps:
- **plugins** are effectively absent in Rust
- **hook support** is narrower than TS
- **CLI breadth** is much narrower in Rust
- **skills** are local-file only in Rust, without the TS registry/bundled pipeline
- **assistant orchestration** lacks TS hook-aware orchestration and remote/structured transports
- **services** beyond core API/OAuth/MCP are mostly missing in Rust

---

## tools/

### TS exists
Evidence:
- `src/tools/` contains broad tool families including `AgentTool`, `AskUserQuestionTool`, `BashTool`, `ConfigTool`, `FileReadTool`, `FileWriteTool`, `GlobTool`, `GrepTool`, `LSPTool`, `ListMcpResourcesTool`, `MCPTool`, `McpAuthTool`, `ReadMcpResourceTool`, `RemoteTriggerTool`, `ScheduleCronTool`, `SkillTool`, `Task*`, `Team*`, `TodoWriteTool`, `ToolSearchTool`, `WebFetchTool`, `WebSearchTool`.
- Tool execution/orchestration is split across `src/services/tools/StreamingToolExecutor.ts`, `src/services/tools/toolExecution.ts`, `src/services/tools/toolHooks.ts`, and `src/services/tools/toolOrchestration.ts`.

### Rust exists
Evidence:
- Tool registry is centralized in `rust/crates/tools/src/lib.rs` via `mvp_tool_specs()`.
- Current built-ins include shell/file/search/web/todo/skill/agent/config/notebook/repl/powershell primitives plus MCP inspection/auth/resource helpers such as `ListMcpResourcesTool`, `ReadMcpResourceTool`, and `McpAuthTool`.
- Rust agent tooling now also exposes built-in sub-agent profile inspection via `list_agent_profiles()` and `load_agent_profile()`, alongside persisted task inspection.
- Rust MCP tooling now supports dynamic per-server MCP tool families and direct list/read/auth flows across `stdio`, `http`, `sse`, and `ws` transports, while surfacing explicit blocker reasons for unsupported `sdk`, `simcoe-ai-proxy`, and remote `headersHelper` execution paths.
- `McpAuthTool` now returns aggregate MCP runtime summaries beyond the raw per-server `servers` array, including `transportCounts`, `statusCounts`, `supportedExecutionCount`, `unsupportedExecutionCount`, `unsupportedServers`, and `attentionServers` for agent-facing MCP inspection.
- Runtime execution is wired through `rust/crates/tools/src/lib.rs` and `rust/crates/runtime/src/conversation.rs`.
- Rust now exposes `/tools [name]` via `rust/crates/compat-harness/src/lib.rs`, `rust/crates/tools/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect both the live Rust tool registry and archived TypeScript tool families from `src/reference_data/tools_snapshot.json`.
- Selected live Rust tool inspection now also includes explicit output-schema metadata when the Rust implementation defines one, so `/tools McpAuthTool` can advertise the aggregate MCP fields it returns instead of only its input contract.

### Missing or broken in Rust
- No Rust equivalents for major TS tools such as `AskUserQuestionTool`, `LSPTool`, `RemoteTriggerTool`, `ScheduleCronTool`, `Task*`, `Team*`, and several workflow/system tools.
- Some MCP parity gaps remain: `sdk`, `simcoe-ai-proxy`, and remote `headersHelper` execution are still inspection-only in Rust because the upstream adapter/runtime contract is not present in this port.
- Rust tool surface is still explicitly an MVP registry, not a parity registry, even though it is now inspectable through `/tools`.
- Rust lacks TS’s layered tool orchestration split.

**Status:** partial core with inspection parity.

---

## hooks/

### TS exists
Evidence:
- Hook command surface under `src/commands/hooks/`.
- Runtime hook machinery in `src/services/tools/toolHooks.ts` and `src/services/tools/toolExecution.ts`.
- TS supports `PreToolUse`, `PostToolUse`, and broader hook-driven behaviors configured through settings and documented in `src/skills/bundled/updateConfig.ts`.

### Rust exists
Evidence:
- Hook config is parsed and merged in `rust/crates/runtime/src/config.rs`.
- Hook execution lives in `rust/crates/runtime/src/hooks.rs` and is wired into `rust/crates/runtime/src/conversation.rs` for `PreToolUse` and `PostToolUse` handling.
- Hook config can be inspected via Rust config reporting in `rust/crates/commands/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs`.
- Rust now exposes `/hooks [pre|post]` in the CLI to inspect configured hook commands.
- Prompt guidance mentions hooks in `rust/crates/runtime/src/prompt.rs`.

### Missing or broken in Rust
- No TS-style hook mutation/rewrite pipeline or broader hook event families beyond pre/post tool use.
- No dedicated hook management workflow beyond config-backed inspection.

**Status:** pre/post shell hooks execute and can deny or warn, and the CLI can now inspect them, but parity remains narrower than TS.

---

## plugins/

### TS exists
Evidence:
- Built-in plugin scaffolding in `src/plugins/builtinPlugins.ts` and `src/plugins/bundled/index.ts`.
- Plugin lifecycle/services in `src/services/plugins/PluginInstallationManager.ts` and `src/services/plugins/pluginOperations.ts`.
- CLI/plugin command surface under `src/commands/plugin/` and `src/commands/reload-plugins/`.

### Rust exists
Evidence:
- No dedicated plugin subsystem appears under `rust/crates/`.
- Rust now exposes `/plugin [name]` and `/reload-plugins` via `rust/crates/compat-harness/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect archived plugin command/module surfaces from the TypeScript snapshot data.

### Missing or broken in Rust
- No plugin loader.
- No marketplace install/update/enable/disable flow.
- No actual `/plugin` management flow or live `/reload-plugins` execution parity.
- No plugin-provided hook/tool/command/MCP extension path.

**Status:** archived-surface inspection exists, but runtime/plugin-management parity is still missing.

---

## skills/ and CLAUDE.md discovery

### TS exists
Evidence:
- Skill loading/registry pipeline in `src/skills/loadSkillsDir.ts`, `src/skills/bundledSkills.ts`, and `src/skills/mcpSkillBuilders.ts`.
- Bundled skills under `src/skills/bundled/`.
- Skills command surface under `src/commands/skills/`.

### Rust exists
Evidence:
- `Skill` tool in `rust/crates/tools/src/lib.rs` resolves and reads local `SKILL.md` files and repo-local frontmatter skills under ancestor `skills/*.md` catalogs.
- Rust now has a `/skills` command in `rust/crates/simcoe-ai-cli/src/main.rs` with shared rendering in `rust/crates/simcoe-ai-cli/src/format.rs`, and JSON/NDJSON now emit dedicated skill list/detail fields instead of only wrapped text content.
- CLAUDE.md discovery is implemented in `rust/crates/runtime/src/prompt.rs`.
- Rust supports `/memory` and `/init` via `rust/crates/commands/src/lib.rs` and `rust/crates/simcoe-ai-cli/src/main.rs`; `/memory` JSON/NDJSON now emit dedicated project-context fields instead of only wrapped text content.

### Missing or broken in Rust
- No bundled skill registry equivalent.
- No MCP skill-builder pipeline.
- No TS-style live skill discovery/reload/change handling.
- No comparable session-memory / team-memory integration around skills.

**Status:** local skills are usable in both tool and CLI flows, but bundled/MCP skill parity is still missing.

---

## cli/

### TS exists
Evidence:
- Large command surface under `src/commands/` including `agents`, `hooks`, `mcp`, `memory`, `model`, `permissions`, `plan`, `plugin`, `resume`, `review`, `skills`, `tasks`, and many more.
- Structured/remote transport stack in `src/cli/structuredIO.ts`, `src/cli/remoteIO.ts`, and `src/cli/transports/*`.
- CLI handler split in `src/cli/handlers/*`.

### Rust exists
Evidence:
- Shared slash command registry in `rust/crates/commands/src/lib.rs`.
- Rust slash commands currently cover `help`, `status`, `compact`, `model`, `permissions`, `clear`, `cost`, `dump-manifests`, `bootstrap-plan`, `login`, `logout`, `resume`, `system-prompt`, `config`, `hooks`, `mcp`, `memory`, `agents`, `plugin`, `reload-plugins`, `remote-env`, `remote-setup`, `tools`, `doctor`, `skills`, `tasks`, `init`, `diff`, `version`, `bughunter`, `review`, `plan`, `commit`, `pr`, `issue`, `ultraplan`, `teleport`, `debug-tool-call`, `export`, `session`.
- Rust now exposes `/config [env|hooks|model]` via `rust/crates/runtime/src/config.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect discovered config files, merged config JSON, and supported section views, and JSON/NDJSON now emit dedicated discovered-file, merged-config, and selected-section fields instead of only wrapped text content.
- Rust now exposes `/hooks [pre|post]` via `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect configured pre/post hook commands, and JSON/NDJSON now emit dedicated event, count, and command-list fields instead of only wrapped text content.
- Rust now exposes `/mcp [server]` via `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect configured MCP servers, derived bootstrap transport details, and shared runtime auth/status state; text output now summarizes executable/blocked/status counts plus per-server runtime state, and JSON/NDJSON emit dedicated server, runtime-status, aggregate status-count, and attention-server fields instead of only wrapped text content.
- Rust now exposes `/agents [name]` via `rust/crates/tools/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect built-in sub-agent profiles, aliases, allowed-tool subsets, and recent persisted tasks, and JSON/NDJSON now emit dedicated profile, task-count, and recent-task fields instead of only wrapped text content.
- Rust now exposes `/plugin [name]` via `rust/crates/compat-harness/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect archived plugin command/module surfaces from the upstream snapshot data, and JSON/NDJSON now emit dedicated snapshot or selected-surface fields instead of only wrapped text content.
- Rust now exposes `/reload-plugins` via `rust/crates/compat-harness/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` as an inspection-only report over the archived reload flow metadata, and JSON/NDJSON now emit dedicated archived snapshot and selected-surface fields instead of only wrapped text content.
- Rust now exposes `/remote-env` via `rust/crates/runtime/src/remote.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect the current remote-session environment plus derived upstream-proxy bootstrap state.
- Rust now exposes `/remote-setup` via `rust/crates/compat-harness/src/lib.rs`, `rust/crates/runtime/src/remote.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` as a read-only report over archived remote setup command surfaces and CLI transport modules, combined with current bootstrap readiness.
- Rust now exposes `/tools [name]` via `rust/crates/compat-harness/src/lib.rs`, `rust/crates/tools/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect the live Rust tool registry and archived TypeScript tool-family snapshots, and JSON/NDJSON now emit dedicated live-registry and archived-family fields instead of only wrapped text content.
- Rust now exposes `/doctor` via `rust/crates/runtime/src/config.rs`, `rust/crates/runtime/src/oauth.rs`, `rust/crates/runtime/src/prompt.rs`, `rust/crates/runtime/src/sandbox.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` as a read-only runtime diagnostic that summarizes config load state, workspace context, sandbox activation, OAuth credentials, hooks, MCP transports, shared MCP auth/status state, and remote bootstrap readiness; JSON/NDJSON emit dedicated config/auth/hooks/MCP/remote issue fields including MCP status counts and non-ready attention servers instead of only wrapped text content.
- Rust now exposes `/login` and `/logout` in the REPL via the shared slash-command registry plus the existing live OAuth helpers in `rust/crates/simcoe-ai-cli/src/main.rs`; they reuse the direct CLI auth flow, remain intentionally unsupported with `--resume` because they mutate account-level credentials rather than session files, and now bound direct non-interactive auth output honestly: `logout` honors `text|json|ndjson`, while `login` supports `text` plus NDJSON progress records and rejects single-shot JSON because the OAuth browser fallback may need manual continuation.
- Rust now also exposes direct read-only CLI inspection subcommands `config [env|hooks|model]`, `hooks [pre|post]`, `mcp [server]`, `memory`, `agents [name]`, `plugin [name]`, `reload-plugins`, `remote-env`, `remote-setup`, `tools [name]`, `doctor`, `skills [skill]`, and `tasks [id]` via `rust/crates/simcoe-ai-cli/src/format.rs` and `rust/crates/simcoe-ai-cli/src/main.rs`; like the earlier direct inspection commands, they honor `text|json|ndjson` and reuse the same report helpers as the REPL and `--resume` paths, while `config`, `hooks`, `mcp`, `agents`, `memory`, `plugin`, `reload-plugins`, `remote-env`, `remote-setup`, `tools`, `doctor`, `skills`, and `tasks` JSON/NDJSON now expose dedicated structured fields instead of only wrapped text content.
- Rust now exposes `/dump-manifests`, `/bootstrap-plan`, and `/system-prompt [--cwd PATH] [--date YYYY-MM-DD]` via the shared slash-command registry plus reusable helpers in `rust/crates/simcoe-ai-cli/src/main.rs`; these commands mirror the remaining direct local CLI actions and are available in both the REPL and `--resume` because they are read-only workspace/runtime inspection paths.
- Rust now exposes `/tasks [id]` via `rust/crates/tools/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect persisted sub-agent task manifests and outputs, and JSON/NDJSON now emit dedicated task summary/detail fields instead of only wrapped text content.
- Main CLI/repl/prompt handling lives in `rust/crates/simcoe-ai-cli/src/main.rs`.

### Missing or broken in Rust
- Missing major TS command families beyond inspection-only parity and many others.
- Rust now emits structured non-interactive output across prompt, `--resume`, and read-only direct-command flows, and non-interactive JSON/NDJSON requests now surface machine-readable error payloads too: prompt JSON/NDJSON includes ordered assistant/tool transport events plus richer remote bootstrap diagnostics from a shared live per-turn trace in `rust/crates/runtime/src/conversation.rs` and `rust/crates/simcoe-ai-cli/src/transport.rs`, including the active transport kind (`api-stream`), explicit `live_remote_transport=false` capability flags, token/CA bundle paths, inherited proxy-env keys, and missing bootstrap prerequisites; `--resume` JSON/NDJSON emits per-command session-inspection records; direct commands like `dump-manifests`, `bootstrap-plan`, `system-prompt`, `init`, and `--version` honor JSON/NDJSON; `config`, `hooks`, `mcp`, `agents`, `memory`, `plugin`, `reload-plugins`, `remote-env`, `remote-setup`, `tools`, `doctor`, `skills`, and `tasks` now emit dedicated config/hook/mcp/profile/project-context/snapshot/transport/archive/health payloads; and structured error payloads now include operation metadata plus the failing resumed slash command when available; it still lacks the full TS live remote structured IO / websocket transport runtime.
- No TS-style handler decomposition for auth/plugins/MCP/agents.

**Status:** functional local CLI core, much narrower than TS.

---

## assistant/ (agentic loop, streaming, tool calling)

### TS exists
Evidence:
- Assistant/session surface at `src/assistant/sessionHistory.ts`.
- Tool orchestration in `src/services/tools/StreamingToolExecutor.ts`, `src/services/tools/toolExecution.ts`, `src/services/tools/toolOrchestration.ts`.
- Remote/structured streaming layers in `src/cli/structuredIO.ts` and `src/cli/remoteIO.ts`.

### Rust exists
Evidence:
- Core loop in `rust/crates/runtime/src/conversation.rs`.
- Stream/tool event translation in `rust/crates/rusty-claude-cli/src/main.rs`.
- Structured JSON turn-transport output in `rust/crates/runtime/src/conversation.rs`, `rust/crates/simcoe-ai-cli/src/transport.rs`, and `rust/crates/simcoe-ai-cli/src/app.rs`.
- Session persistence in `rust/crates/runtime/src/session.rs`.

### Missing or broken in Rust
- Hook-aware orchestration exists for pre/post shell hooks, but remains narrower than TS.
- No TS structured/remote assistant transport stack.
- No richer TS assistant/session-history/background-task integration.

**Status:** strong core loop, missing orchestration layers.

---

## services/ (API client, auth, models, MCP)

### TS exists
Evidence:
- API services under `src/services/api/*`.
- OAuth services under `src/services/oauth/*`.
- MCP services under `src/services/mcp/*`.
- Additional service layers for analytics, prompt suggestion, session memory, plugin operations, settings sync, policy limits, team memory sync, notifier, voice, and more under `src/services/*`.

### Rust exists
Evidence:
- Core Anthropic API client in `rust/crates/api/src/{client,error,sse,types}.rs`.
- OAuth support in `rust/crates/runtime/src/oauth.rs`.
- MCP config/bootstrap/client support in `rust/crates/runtime/src/{config,mcp,mcp_client,mcp_stdio}.rs`, including websocket transport bootstrapping, shared transport/blocker labeling, and shared per-server auth/status evaluation.
- Usage accounting in `rust/crates/runtime/src/usage.rs`.
- Remote upstream-proxy support in `rust/crates/runtime/src/remote.rs`.

### Missing or broken in Rust
- Most TS service ecosystem beyond core messaging/auth/MCP is absent.
- No TS-equivalent plugin service layer.
- No TS-equivalent analytics/settings-sync/policy-limit/team-memory subsystems.
- No TS-style MCP connection-manager/UI layer.
- Model/provider ergonomics remain thinner than TS.

**Status:** core foundation exists; broader service ecosystem missing.

---

## Critical bug status in this worktree

### Fixed
- **Prompt mode tools enabled**
  - `rust/crates/simcoe-ai-cli/src/main.rs` now constructs prompt mode with `LiveCli::new(model, true, ...)`.
- **Default permission mode = DangerFullAccess**
  - Runtime default now resolves to `DangerFullAccess` in `rust/crates/simcoe-ai-cli/src/main.rs`.
  - Clap default also uses `DangerFullAccess` in `rust/crates/simcoe-ai-cli/src/args.rs`.
  - Init template writes `dontAsk` in `rust/crates/simcoe-ai-cli/src/init.rs`.
- **Streaming `{}` tool-input prefix bug**
  - `rust/crates/simcoe-ai-cli/src/main.rs` now strips the initial empty object only for streaming tool input, while preserving legitimate `{}` in non-stream responses.
- **Unlimited max_iterations**
  - Verified at `rust/crates/runtime/src/conversation.rs` with `usize::MAX`.
- **JSON prompt output cleanliness hardening**
  - `rust/crates/simcoe-ai-cli/src/main.rs` now routes streaming and tool rendering through suppressible writers, with regression tests covering hidden-output mode for both stream events and tool execution.

### Remaining notable parity issue
- **Structured/remote transport parity**
  - Rust now exposes structured local success and error output for prompt, `--resume`, and read-only direct-command flows, including ordered prompt transport events plus explicit remote-bootstrap diagnostics that distinguish the active `api-stream` path from the still-missing live remote websocket transport, but it still lacks the TS live remote structured IO / websocket transport path.
