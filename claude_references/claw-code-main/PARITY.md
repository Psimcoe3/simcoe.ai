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
- `McpAuthTool` now also exposes shared MCP blocker/auth categories as camelCase `reasonKind` fields on `unsupportedServers`, `attentionServers`, and non-ready per-server `servers` entries, and `/tools McpAuthTool` advertises that field in its live Rust output schema.
- Runtime execution is wired through `rust/crates/tools/src/lib.rs` and `rust/crates/runtime/src/conversation.rs`.
- Rust now exposes `/tools [name]` via `rust/crates/compat-harness/src/lib.rs`, `rust/crates/tools/src/lib.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` to inspect both the live Rust tool registry and archived TypeScript tool families from `src/reference_data/tools_snapshot.json`.
- Selected live Rust tool inspection now also includes explicit output-schema metadata when the Rust implementation defines one, so `/tools` can advertise native result contracts for the MCP tool family plus core shell/file/search built-ins (`bash`, `read_file`, `write_file`, `edit_file`, `glob_search`, `grep_search`, `PowerShell`) and local structured tools such as `NotebookEdit`, `Config`, `Agent`, `TodoWrite`, `Skill`, `SessionExportTool`, `WebFetch`, `WebSearch`, `StructuredOutput`, `REPL`, `Sleep`, `SyntheticOutputTool`, `SendUserMessage`, and `BriefTool` instead of only their input schemas. `/tools` now also includes live-discovered dynamic `mcp__server__tool` entries from configured MCP servers, along with pending discovery state, per-server failure detail, and a coarse `reason_kind` classifier when a server cannot currently enumerate its tools.
- Rust `ToolSearch` still returns the legacy `matches` name list, but it now also returns structured `match_details` for registry and dynamic MCP results plus `pending_mcp_server_details` with `reason_kind`, so agent consumers can explain dynamic MCP hits and bucket discovery failures without re-deriving them from tool names or raw blocker text alone.
- MCP reason classification is now shared in `rust/crates/runtime/src/mcp.rs` as a typed `McpReasonKind` enum, and the Rust CLI now threads that same category through `/tools`, `/mcp`, and `doctor` payloads/reporting instead of re-classifying MCP blockers from ad hoc status/detail strings in each surface.
- The interactive Rust CLI no longer collapses successful `ToolSearch` results to truncated raw JSON in tool-result rendering: it now summarizes `match_details` plus pending MCP discovery `reason_kind` entries in the higher-level agent-facing tool output path.
- The interactive Rust CLI now also gives `McpAuthTool` a dedicated agent-facing result summary in `simcoe-ai-cli/src/main.rs`: successful auth/status/save/logout results now render aggregate executable/blocker counts, status buckets, and attention-server `reasonKind` details instead of falling through the generic truncated JSON path.
- The interactive Rust CLI now also gives `MCPTool` a dedicated agent-facing result summary in `simcoe-ai-cli/src/main.rs`: successful `list_tools` and `call_tool` results render server/transport context, tool descriptors, content snippets, and `structuredContent` summaries instead of falling through the generic truncated JSON path.
- The interactive Rust CLI now also gives `ListMcpResourcesTool` and `ReadMcpResourceTool` dedicated agent-facing result summaries in `simcoe-ai-cli/src/main.rs`: successful resource list/read results render server/transport context, resource URIs/descriptors, and content snippets instead of falling through the generic truncated JSON path.
- The interactive Rust CLI now also gives dynamic `mcp__server__tool` calls the same dedicated agent-facing call summary as `MCPTool` in `simcoe-ai-cli/src/main.rs`, so direct dynamic MCP tool results no longer fall through the generic truncated JSON path.
- Rust now exposes the archived `BriefTool` name as a compatibility alias for the existing `SendUserMessage` implementation in `tools/src/lib.rs`, and both names now advertise the same structured output schema (`message`, optional resolved `attachments`, `sentAt`) while `simcoe-ai-cli/src/main.rs` renders dedicated start/result summaries instead of falling through generic truncated JSON.
- `bash`, `read_file`, `write_file`, `edit_file`, `glob_search`, `grep_search`, `PowerShell`, `NotebookEdit`, `Config`, `Agent`, `TodoWrite`, `Skill`, `SessionExportTool`, `WebFetch`, `WebSearch`, `StructuredOutput`, `REPL`, `Sleep`, and `SyntheticOutputTool` in `tools/src/lib.rs` now also advertise their structured local result payloads via `tool_output_schema()`, and `simcoe-ai-cli/src/main.rs` renders dedicated start/result summaries for those tools instead of falling through the generic truncated JSON path.
- Rust now also exposes an honest local `SessionExportTool`: it uses the shared managed-session store to export the active session transcript to a workspace file, returns structured `sessionId` / `sessionPath` / `exportPath` / `messageCount` output, and reuses the same transcript rendering path as the direct `/export` CLI command. This is a Rust-local workflow helper, not an upstream TS tool family.
- Rust execution now also accepts archived TypeScript-style tool family names for the overlapping local tool surface instead of only the Rust-native spellings. Calls such as `AgentTool`, `BashTool`, `ConfigTool`, `FileReadTool`, `FileWriteTool`, `FileEditTool`, `GlobTool`, `GrepTool`, `NotebookEditTool`, `PowerShellTool`, `REPLTool`, `SendMessageTool`, `SkillTool`, `SleepTool`, `TodoWriteTool`, `ToolSearchTool`, `WebFetchTool`, `WebSearchTool`, and `ExitPlanModeTool` now normalize to the native Rust implementations and shared output schemas in `tools/src/lib.rs`; `ToolSearch` indexes and now returns that same alias set in structured `match_details.aliases`; `/tools` uses the shared matcher plus alias metadata in `simcoe-ai-cli/src/format.rs` and `simcoe-ai-cli/src/main.rs`, so archived names resolve in discovery/inspection and are visible in both the default Rust registry listing and selected-tool detail/payloads; and the shared allowlist path (`tool_name_is_allowed`, runtime tool-definition filtering, `filter_tool_specs`, and `--allowedTools`) now canonicalizes the same alias set so archived spellings stay enabled through filtering and execution instead of only parsing successfully.
- Direct MCP tool-family regression coverage now explicitly asserts that blocked remote `headersHelper` transports fail as `unsupported-runtime` before any OAuth credential prompt across tool list, tool call, resource list, and resource read paths.
- The interactive Rust CLI now also gives the MCP tool family dedicated error summaries in `simcoe-ai-cli/src/main.rs`: blocked/auth-required failures for `MCPTool`, dynamic `mcp__server__tool` calls, and MCP resource tools now render the server plus shared `reason_kind` classification instead of falling through the generic truncated error path.
- The shared runtime `classify_mcp_reason_kind(...)` classifier now recognizes the real execution-time auth error wording `requires stored OAuth credentials`, so MCP error rendering and blocker reports stay aligned on `auth-required` categorization.
- MCP error summaries in `simcoe-ai-cli/src/main.rs` now also surface structured execution context extracted from the error string itself, including JSON-RPC method names and HTTP status codes for remote request, JSON-RPC, OAuth refresh, and OAuth metadata failures.
- Shared MCP reason classification now treats OAuth refresh failures containing `invalid_grant` as `expired-credentials` instead of generic `discovery-error`, so agent-facing MCP error summaries point at re-authentication rather than an undifferentiated transport failure.
- Shared MCP remediation hints now live next to the runtime classifier in `rust/crates/runtime/src/mcp.rs` and are reused by `simcoe-ai-cli/src/main.rs`, so blocked/auth-required/expired/discovery MCP failures now include actionable next-step guidance instead of only labels and truncated error text.
- Shared remediation hints are now also surfaced in `/mcp <server>` selected-server text output and `doctor` issue lines via `format.rs`: the `/mcp` Runtime section appends a `Hint` line when the runtime detail maps to a known hint, and `doctor` issues include a `; hint: …` suffix so agent consumers see next-step guidance in both sub-commands.
- `mcp_attention_payload` and `mcp_blocked_server_payload` in `simcoe-ai-cli/src/main.rs` now include a `remediation_hint` field alongside `detail`, so `/mcp` and `doctor` JSON payloads expose actionable next-step guidance for blocked and auth-attention servers without requiring callers to re-derive hints from the raw detail string.
- `McpAuthUnsupportedServer` and `McpAuthAttentionServer` in `tools/src/lib.rs` now also carry a camelCase `remediationHint` field populated from the shared `mcp_reason_remediation_hint` helper, so `McpAuthTool` tool output aligns with the CLI JSON payload contract: agent consumers see next-step guidance for blocked and auth-required servers without re-classifying the raw detail string.
- `PendingMcpServerDiscovery` in `tools/src/lib.rs` now carries a camelCase `remediationHint` field too, so `ToolSearch` `pending_mcp_server_details` entries advertise the same actionable guidance as every other MCP blocked/attention surface; `pending_mcp_server_discovery_output_schema()` and the `render_pending_mcp_discovery_items` text renderer were updated in parallel.
- A fresh repo search still found only reference-data pointers for the blocked proxy/helper adapter files (`src/reference_data/subsystems/remote.json` mentions `remote/SessionsWebSocket.ts` and `remote/sdkMessageAdapter.ts`) rather than live implementation or helper-output contracts, so `headersHelper`, `sdk`, and `simcoe-ai-proxy` execution remain genuinely blocked in this Rust snapshot.

### Missing or broken in Rust
- `AskUserQuestionTool` is now implemented in Rust (`tools/src/lib.rs`): accepts `question` (string) + optional `options` array, checks `std::io::IsTerminal` to reject non-interactive contexts, prints the question/options to stdout, and reads the user's answer via `read_line`. CLI display includes a `? …` prompt in `format_tool_call_start` and a Q/A summary in `format_ask_user_question_result`. Tool spec registered in `mvp_tool_specs()`, output schema in `tool_output_schema()`, and `parity_manifest.json` updated.
- `TestingPermissionTool` is now implemented in Rust (`tools/src/lib.rs`): it resolves common action aliases or canonical tool names to the Rust tool registry, evaluates the shared `PermissionPolicy`, and returns structured `allow` / `prompt` / `deny` diagnostics with current-mode, required-mode, and reason fields. `simcoe-ai-cli/src/main.rs` now renders that structured result directly instead of treating it as a stub error.
- Rust also has local file-backed task tooling in `tools/src/lib.rs` for the current archived TS task family: `TaskCreateTool`, `TaskGetTool`, `TaskListTool`, `TaskOutputTool`, `TaskStopTool`, and `TaskUpdateTool`. That gives Rust practical local task-tool parity for persisted sub-agent manifests, even though the backing implementation is still a local file store rather than the upstream service stack.
- Rust now has local file-backed cron tooling in `tools/src/lib.rs`: `CronCreateTool`, `CronDeleteTool`, and `CronListTool` manage persisted schedule manifests under a local cron store and return structured results that `simcoe-ai-cli/src/main.rs` renders directly. This is still manifest-only parity, not a live scheduler service.
- Rust now has honest local `EnterPlanModeTool` / `ExitPlanModeV2Tool` support in `tools/src/lib.rs`: plan mode flips shared runtime state and blocks non-read-only built-in tools plus dynamic MCP tools until exited, and `simcoe-ai-cli/src/main.rs` renders the structured enter/exit result directly.
- Rust now has honest local `EnterWorktreeTool` / `ExitWorktreeTool` support in `tools/src/lib.rs`: they switch a shared runtime worktree root that `runtime` bash and file tools resolve relative paths against, and `simcoe-ai-cli/src/main.rs` renders the active/inactive worktree context directly.
- Rust now has honest local `TeamCreateTool` / `TeamDeleteTool` support in `tools/src/lib.rs`: they manage a local file-backed team registry with structured create/delete results, and `simcoe-ai-cli/src/main.rs` renders those registry operations directly. This is workspace-local parity, not a connected multi-user backend.
- Rust now has honest diagnostic `RemoteTriggerTool` support in `tools/src/lib.rs`: it reports structured remote bootstrap, websocket probe, and live transport blocker state using the existing remote runtime foundation, and `simcoe-ai-cli/src/main.rs` renders those blocker diagnostics directly. Actual remote event execution is still blocked because the upstream websocket/session adapter is not ported in Rust.
- Rust now has honest diagnostic `LSPTool` support in `tools/src/lib.rs`: it returns structured unsupported-runtime output that lists the requested LSP command, supported command set, and the missing attached language-server/runtime condition, and `simcoe-ai-cli/src/main.rs` renders that diagnostic directly. Actual LSP execution is still blocked because this Rust port has no attached editor-driven language-server runtime.
- `SyntheticOutputTool` still returns a structured local-only placeholder rather than a real upstream integration.
- Some MCP parity gaps remain: `sdk`, `simcoe-ai-proxy`, and remote `headersHelper` execution are still inspection-only in Rust because the upstream adapter/runtime contract is not present in this port.
- Rust tool surface is a stub-parity registry (all TS tool names registered with schemas and dispatch), not a full-execution registry.
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
- Repo-local skill aliases are now surfaced as first-class inspection metadata too: `crates/tools/src/lib.rs` carries alias lists through `SkillSummary` and `LoadedSkill`, `/skills` text output in `crates/simcoe-ai-cli/src/format.rs` shows aliases in both the default local listing and selected-skill detail, and the structured payload in `crates/simcoe-ai-cli/src/main.rs` now exposes those same aliases instead of only silently accepting them during lookup.
- `/skills` now also inspects archived bundled skill samples from `src/reference_data/subsystems/skills.json` via `rust/crates/compat-harness/src/lib.rs`, so the Rust CLI can list inspection-only bundled skill surfaces and render a selected archived bundled skill module even though it still cannot execute TS bundled or MCP-built skills.
- CLAUDE.md discovery is implemented in `rust/crates/runtime/src/prompt.rs`.
- Rust supports `/memory` and `/init` via `rust/crates/commands/src/lib.rs` and `rust/crates/simcoe-ai-cli/src/main.rs`; `/memory` JSON/NDJSON now emit dedicated project-context fields instead of only wrapped text content.

### Missing or broken in Rust
- No bundled skill runtime or prompt-loading equivalent beyond archived inspection snapshots.
- No MCP skill-builder pipeline.
- No TS-style live skill discovery/reload/change handling.
- No comparable session-memory / team-memory integration around skills.

**Status:** local skills are usable in both tool and CLI flows, and archived bundled skills are now inspectable, but bundled/MCP execution parity is still missing.

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
- Rust now exposes `/remote-setup` via `rust/crates/compat-harness/src/lib.rs`, `rust/crates/runtime/src/remote.rs`, `rust/crates/simcoe-ai-cli/src/format.rs`, `rust/crates/simcoe-ai-cli/src/app.rs`, and `rust/crates/simcoe-ai-cli/src/main.rs` as a read-only report over archived remote setup command surfaces, CLI transport modules, and the archived `upstreamproxy` relay sample files, combined with current bootstrap readiness.
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
