  ├── simcoe-ai-cli/      # Main CLI binary (`claw`)
# Simcoe AI — Rust Implementation

A high-performance Rust implementation of the Simcoe AI CLI harness. Built for speed, safety, and native tool execution.

## Quick Start

```bash
# Build
cd rust/
cargo build --release

# Run interactive REPL
./target/release/claw

# One-shot prompt
./target/release/claw prompt "explain this codebase"

# With specific model
./target/release/claw --model simcoe-sonnet prompt "fix the bug in main.rs"
```

## Configuration

Set your API credentials:

```bash
export SIMCOE_AI_API_KEY="your-key"
# Or use a proxy / alternate upstream
export SIMCOE_AI_BASE_URL="https://your-proxy.com"
```

Or authenticate via OAuth:

```bash
# requires an `oauth` block in your resolved runtime config, e.g. `.simcoe.json`
claw login
```

## Features

| Feature | Status |
|---------|--------|
| Simcoe AI API + streaming | ✅ |
| OAuth login/logout | ✅ |
| Interactive REPL (rustyline) | ✅ |
| Tool system (bash, read, write, edit, grep, glob) | ✅ |
| Web tools (search, fetch) | ✅ |
| Sub-agent orchestration | ✅ |
| Todo tracking | ✅ |
| Notebook editing | ✅ |
| SIMCOE.md / project memory | ✅ |
| Config file hierarchy (.simcoe.json) | ✅ |
| Permission system | ✅ |
| MCP server lifecycle | ✅ |
| Session persistence + resume | ✅ |
| Extended thinking (thinking blocks) | ✅ |
| Cost tracking + usage display | ✅ |
| Git integration | ✅ |
| Markdown terminal rendering (ANSI) | ✅ |
| Model aliases (opus/sonnet/haiku) | ✅ |
| Slash commands (/status, /compact, /clear, etc.) | ✅ |
| Hooks (PreToolUse/PostToolUse) | 🔧 Config only |
| Plugin system | 📋 Planned |
| Skills registry | 📋 Planned |

## Model Aliases

Short names resolve to the latest model versions:

| Alias | Resolves To |
|-------|------------|
| `simcoe-opus` | upstream Opus profile |
| `simcoe-sonnet` | upstream Sonnet profile |
| `simcoe-haiku` | upstream Haiku profile |

## CLI Flags

```
claw [OPTIONS] [COMMAND]

Options:
  --model MODEL                    Set the model (alias or full name)
  --dangerously-skip-permissions   Skip all permission checks
  --permission-mode MODE           Set read-only, workspace-write, or danger-full-access
  --allowedTools TOOLS             Restrict enabled tools
  --output-format FORMAT           Output format (text or json)
  --version, -V                    Print version info

Commands:
  prompt <text>      One-shot prompt (non-interactive)
  login              Authenticate via OAuth
  logout             Clear stored credentials
  init               Initialize project config
  doctor             Check environment health
  self-update        Update to latest version
```

## Slash Commands (REPL)

| Command | Description |
|---------|-------------|
| `/help` | Show help |
| `/status` | Show session status (model, tokens, cost) |
| `/cost` | Show cost breakdown |
| `/compact` | Compact conversation history |
| `/clear` | Clear conversation |
| `/model [name]` | Show or switch model |
| `/permissions` | Show or switch permission mode |
| `/config [section]` | Show config (env, hooks, model) |
| `/memory` | Show SIMCOE.md contents |
| `/diff` | Show git diff |
| `/export [path]` | Export conversation |
| `/session [id]` | Resume a previous session |
| `/version` | Show version |

## Workspace Layout

```
rust/
├── Cargo.toml              # Workspace root
├── Cargo.lock
└── crates/
    ├── api/                # Simcoe API client + SSE streaming
    ├── commands/           # Shared slash-command registry
    ├── compat-harness/     # TS manifest extraction harness
    ├── runtime/            # Session, config, permissions, MCP, prompts
    ├── simcoe-ai-cli/      # Main CLI binary (`claw`)
    └── tools/              # Built-in tool implementations
```

### Crate Responsibilities

- **api** — HTTP client, SSE stream parser, request/response types, auth (API key + OAuth bearer)
- **commands** — Slash command definitions and help text generation
- **compat-harness** — Extracts tool/prompt manifests from upstream TS source
- **runtime** — `ConversationRuntime` agentic loop, `ConfigLoader` hierarchy, `Session` persistence, permission policy, MCP client, system prompt assembly, usage tracking
- **simcoe-ai-cli** — REPL, one-shot prompt, streaming display, tool call rendering, CLI argument parsing
- **tools** — Tool specs + execution: Bash, ReadFile, WriteFile, EditFile, GlobSearch, GrepSearch, WebSearch, WebFetch, Agent, TodoWrite, NotebookEdit, Skill, ToolSearch, REPL runtimes

## Stats

- **~20K lines** of Rust
- **6 crates** in workspace
- **Binary name:** `claw`
- **Default model:** `simcoe-opus`
- **Default permissions:** `danger-full-access`

## License

See repository root.
