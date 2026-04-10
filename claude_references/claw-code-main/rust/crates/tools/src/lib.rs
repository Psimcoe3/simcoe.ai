use std::collections::{BTreeMap, BTreeSet};
use std::io::Read;
use std::path::{Path, PathBuf};
use std::process::Command;
use std::time::{Duration, Instant};

use api::{
    ContentBlockDelta, InputContentBlock, InputMessage, MessageRequest, MessageResponse,
    OutputContentBlock, SimcoeApiClient, StreamEvent as ApiStreamEvent, ToolChoice, ToolDefinition,
    ToolResultContentBlock,
};
use reqwest::blocking::Client;
use runtime::{
    clear_mcp_oauth_credentials, edit_file, execute_bash, glob_search, grep_search,
    load_mcp_oauth_credentials, load_system_prompt, read_file, save_mcp_oauth_credentials,
    write_file, ApiClient, ApiRequest, AssistantEvent, BashCommandInput, ConfigLoader,
    ContentBlock, ConversationMessage, ConversationRuntime, GrepSearchInput, McpClientTransport,
    McpRemoteServerConfig, McpServerConfig, McpServerManager, McpWebSocketServerConfig,
    MessageRole, OAuthRefreshRequest, OAuthTokenSet, PermissionMode, PermissionPolicy,
    RuntimeConfig, RuntimeError, Session, TokenUsage, ToolError, ToolExecutor,
};
use serde::{de::DeserializeOwned, Deserialize, Serialize};
use serde_json::{json, Value};
use serde_yaml::{Mapping as YamlMapping, Value as YamlValue};
use tungstenite::client::IntoClientRequest;
use tungstenite::{connect as connect_websocket, Message as WebSocketMessage};

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ToolManifestEntry {
    pub name: String,
    pub source: ToolSource,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ToolSource {
    Base,
    Conditional,
}

#[derive(Debug, Clone, Default, PartialEq, Eq)]
pub struct ToolRegistry {
    entries: Vec<ToolManifestEntry>,
}

impl ToolRegistry {
    #[must_use]
    pub fn new(entries: Vec<ToolManifestEntry>) -> Self {
        Self { entries }
    }

    #[must_use]
    pub fn entries(&self) -> &[ToolManifestEntry] {
        &self.entries
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ToolSpec {
    pub name: &'static str,
    pub description: &'static str,
    pub input_schema: Value,
    pub required_permission: PermissionMode,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct SkillSummary {
    pub name: String,
    pub path: String,
    pub description: Option<String>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct LoadedSkill {
    pub skill: String,
    pub path: String,
    pub args: Option<String>,
    pub description: Option<String>,
    pub prompt: String,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct AgentTaskSummary {
    #[serde(rename = "agentId")]
    pub agent_id: String,
    pub name: String,
    pub description: String,
    #[serde(rename = "subagentType")]
    pub subagent_type: Option<String>,
    pub model: Option<String>,
    pub status: String,
    #[serde(rename = "outputFile")]
    pub output_file: String,
    #[serde(rename = "manifestFile")]
    pub manifest_file: String,
    #[serde(rename = "createdAt")]
    pub created_at: String,
    #[serde(rename = "startedAt", skip_serializing_if = "Option::is_none")]
    pub started_at: Option<String>,
    #[serde(rename = "completedAt", skip_serializing_if = "Option::is_none")]
    pub completed_at: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub error: Option<String>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct LoadedAgentTask {
    pub task: AgentTaskSummary,
    pub output: Option<String>,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct AgentProfileSummary {
    pub name: String,
    pub description: String,
    pub aliases: Vec<String>,
    pub tool_count: usize,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct LoadedAgentProfile {
    pub name: String,
    pub description: String,
    pub aliases: Vec<String>,
    pub tools: Vec<String>,
}

#[derive(Debug, Clone, PartialEq, Eq)]
struct RepoSkillRecord {
    name: String,
    path: PathBuf,
    description: Option<String>,
    aliases: Vec<String>,
    prompt: String,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct AgentProfileSpec {
    name: &'static str,
    description: &'static str,
    aliases: &'static [&'static str],
}

const AGENT_PROFILE_SPECS: &[AgentProfileSpec] = &[
    AgentProfileSpec {
        name: "general-purpose",
        description: "Default broad-access coding sub-agent.",
        aliases: &["general", "generalpurpose", "generalpurposeagent"],
    },
    AgentProfileSpec {
        name: "Explore",
        description: "Read-heavy repo exploration and research sub-agent.",
        aliases: &["explore", "explorer", "exploreagent"],
    },
    AgentProfileSpec {
        name: "Plan",
        description: "Planning-oriented sub-agent with todo and structured output tools.",
        aliases: &["plan", "planagent"],
    },
    AgentProfileSpec {
        name: "Verification",
        description: "Validation-oriented sub-agent with shell access.",
        aliases: &["verification", "verificationagent", "verify", "verifier"],
    },
    AgentProfileSpec {
        name: "simcoe-ai-guide",
        description: "Read-heavy guide sub-agent for Simcoe AI usage and conventions.",
        aliases: &[
            "simcoeaiguide",
            "simcoeaiguideagent",
            "claudecodeguide",
            "claudecodeguideagent",
            "guide",
        ],
    },
    AgentProfileSpec {
        name: "statusline-setup",
        description: "Narrow workspace-editing sub-agent for statusline setup tasks.",
        aliases: &["statusline", "statuslinesetup", "statuslinesetupagent"],
    },
];

#[must_use]
#[allow(clippy::too_many_lines)]
pub fn mvp_tool_specs() -> Vec<ToolSpec> {
    vec![
        ToolSpec {
            name: "bash",
            description: "Execute a shell command in the current workspace.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "command": { "type": "string" },
                    "timeout": { "type": "integer", "minimum": 1 },
                    "description": { "type": "string" },
                    "run_in_background": { "type": "boolean" },
                    "dangerouslyDisableSandbox": { "type": "boolean" }
                },
                "required": ["command"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::DangerFullAccess,
        },
        ToolSpec {
            name: "read_file",
            description: "Read a text file from the workspace.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "path": { "type": "string" },
                    "offset": { "type": "integer", "minimum": 0 },
                    "limit": { "type": "integer", "minimum": 1 }
                },
                "required": ["path"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "write_file",
            description: "Write a text file in the workspace.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "path": { "type": "string" },
                    "content": { "type": "string" }
                },
                "required": ["path", "content"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::WorkspaceWrite,
        },
        ToolSpec {
            name: "edit_file",
            description: "Replace text in a workspace file.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "path": { "type": "string" },
                    "old_string": { "type": "string" },
                    "new_string": { "type": "string" },
                    "replace_all": { "type": "boolean" }
                },
                "required": ["path", "old_string", "new_string"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::WorkspaceWrite,
        },
        ToolSpec {
            name: "glob_search",
            description: "Find files by glob pattern.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "pattern": { "type": "string" },
                    "path": { "type": "string" }
                },
                "required": ["pattern"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "grep_search",
            description: "Search file contents with a regex pattern.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "pattern": { "type": "string" },
                    "path": { "type": "string" },
                    "glob": { "type": "string" },
                    "output_mode": { "type": "string" },
                    "-B": { "type": "integer", "minimum": 0 },
                    "-A": { "type": "integer", "minimum": 0 },
                    "-C": { "type": "integer", "minimum": 0 },
                    "context": { "type": "integer", "minimum": 0 },
                    "-n": { "type": "boolean" },
                    "-i": { "type": "boolean" },
                    "type": { "type": "string" },
                    "head_limit": { "type": "integer", "minimum": 1 },
                    "offset": { "type": "integer", "minimum": 0 },
                    "multiline": { "type": "boolean" }
                },
                "required": ["pattern"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "ListMcpResourcesTool",
            description: "List resources exposed by a configured MCP server when its transport is supported by the Rust runtime.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "server": { "type": "string" },
                    "cursor": { "type": "string" }
                },
                "required": ["server"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "ReadMcpResourceTool",
            description: "Read a resource from a configured MCP server when its transport is supported by the Rust runtime.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "server": { "type": "string" },
                    "uri": { "type": "string" }
                },
                "required": ["server", "uri"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "MCPTool",
            description: "List tools from or call a tool on a configured MCP server when its transport is supported by the Rust runtime.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "server": { "type": "string" },
                    "tool": { "type": "string" },
                    "arguments": {
                        "type": "object",
                        "additionalProperties": true
                    },
                    "cursor": { "type": "string" }
                },
                "required": ["server"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::DangerFullAccess,
        },
        ToolSpec {
            name: "McpAuthTool",
            description: "Inspect or manage configured MCP server auth requirements, stored credentials, and execution support.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "server": { "type": "string" },
                    "action": {
                        "type": "string",
                        "enum": ["status", "save", "logout"]
                    },
                    "accessToken": { "type": "string" },
                    "refreshToken": { "type": "string" },
                    "expiresAt": { "type": "integer", "minimum": 0 },
                    "scopes": {
                        "type": "array",
                        "items": { "type": "string" }
                    }
                },
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "WebFetch",
            description:
                "Fetch a URL, convert it into readable text, and answer a prompt about it.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "url": { "type": "string", "format": "uri" },
                    "prompt": { "type": "string" }
                },
                "required": ["url", "prompt"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "WebSearch",
            description: "Search the web for current information and return cited results.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "query": { "type": "string", "minLength": 2 },
                    "allowed_domains": {
                        "type": "array",
                        "items": { "type": "string" }
                    },
                    "blocked_domains": {
                        "type": "array",
                        "items": { "type": "string" }
                    }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "TodoWrite",
            description: "Update the structured task list for the current session.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "todos": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "content": { "type": "string" },
                                "activeForm": { "type": "string" },
                                "status": {
                                    "type": "string",
                                    "enum": ["pending", "in_progress", "completed"]
                                }
                            },
                            "required": ["content", "activeForm", "status"],
                            "additionalProperties": false
                        }
                    }
                },
                "required": ["todos"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::WorkspaceWrite,
        },
        ToolSpec {
            name: "Skill",
            description: "Load a local skill definition and its instructions.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "skill": { "type": "string" },
                    "args": { "type": "string" }
                },
                "required": ["skill"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "Agent",
            description: "Launch a specialized agent task and persist its handoff metadata.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "description": { "type": "string" },
                    "prompt": { "type": "string" },
                    "subagent_type": { "type": "string" },
                    "name": { "type": "string" },
                    "model": { "type": "string" }
                },
                "required": ["description", "prompt"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::DangerFullAccess,
        },
        ToolSpec {
            name: "ToolSearch",
            description: "Search for deferred or specialized tools by exact name or keywords.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "query": { "type": "string" },
                    "max_results": { "type": "integer", "minimum": 1 }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "NotebookEdit",
            description: "Replace, insert, or delete a cell in a Jupyter notebook.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "notebook_path": { "type": "string" },
                    "cell_id": { "type": "string" },
                    "new_source": { "type": "string" },
                    "cell_type": { "type": "string", "enum": ["code", "markdown"] },
                    "edit_mode": { "type": "string", "enum": ["replace", "insert", "delete"] }
                },
                "required": ["notebook_path"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::WorkspaceWrite,
        },
        ToolSpec {
            name: "Sleep",
            description: "Wait for a specified duration without holding a shell process.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "duration_ms": { "type": "integer", "minimum": 0 }
                },
                "required": ["duration_ms"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "SendUserMessage",
            description: "Send a message to the user.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "message": { "type": "string" },
                    "attachments": {
                        "type": "array",
                        "items": { "type": "string" }
                    },
                    "status": {
                        "type": "string",
                        "enum": ["normal", "proactive"]
                    }
                },
                "required": ["message", "status"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "Config",
            description: "Get or set Claw Code settings.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "setting": { "type": "string" },
                    "value": {
                        "type": ["string", "boolean", "number"]
                    }
                },
                "required": ["setting"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::WorkspaceWrite,
        },
        ToolSpec {
            name: "StructuredOutput",
            description: "Return structured output in the requested format.",
            input_schema: json!({
                "type": "object",
                "additionalProperties": true
            }),
            required_permission: PermissionMode::ReadOnly,
        },
        ToolSpec {
            name: "REPL",
            description: "Execute code in a REPL-like subprocess.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "code": { "type": "string" },
                    "language": { "type": "string" },
                    "timeout_ms": { "type": "integer", "minimum": 1 }
                },
                "required": ["code", "language"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::DangerFullAccess,
        },
        ToolSpec {
            name: "PowerShell",
            description: "Execute a PowerShell command with optional timeout.",
            input_schema: json!({
                "type": "object",
                "properties": {
                    "command": { "type": "string" },
                    "timeout": { "type": "integer", "minimum": 1 },
                    "description": { "type": "string" },
                    "run_in_background": { "type": "boolean" }
                },
                "required": ["command"],
                "additionalProperties": false
            }),
            required_permission: PermissionMode::DangerFullAccess,
        },
    ]
}

pub fn execute_tool(name: &str, input: &Value) -> Result<String, String> {
    match name {
        "bash" => from_value::<BashCommandInput>(input).and_then(run_bash),
        "read_file" => from_value::<ReadFileInput>(input).and_then(run_read_file),
        "write_file" => from_value::<WriteFileInput>(input).and_then(run_write_file),
        "edit_file" => from_value::<EditFileInput>(input).and_then(run_edit_file),
        "glob_search" => from_value::<GlobSearchInputValue>(input).and_then(run_glob_search),
        "grep_search" => from_value::<GrepSearchInput>(input).and_then(run_grep_search),
        "ListMcpResourcesTool" => {
            from_value::<ListMcpResourcesInput>(input).and_then(run_list_mcp_resources)
        }
        "ReadMcpResourceTool" => {
            from_value::<ReadMcpResourceInput>(input).and_then(run_read_mcp_resource)
        }
        "MCPTool" => from_value::<McpToolInput>(input).and_then(run_mcp_tool),
        "McpAuthTool" => from_value::<McpAuthInput>(input).and_then(run_mcp_auth),
        "WebFetch" => from_value::<WebFetchInput>(input).and_then(run_web_fetch),
        "WebSearch" => from_value::<WebSearchInput>(input).and_then(run_web_search),
        "TodoWrite" => from_value::<TodoWriteInput>(input).and_then(run_todo_write),
        "Skill" => from_value::<SkillInput>(input).and_then(run_skill),
        "Agent" => from_value::<AgentInput>(input).and_then(run_agent),
        "ToolSearch" => from_value::<ToolSearchInput>(input).and_then(run_tool_search),
        "NotebookEdit" => from_value::<NotebookEditInput>(input).and_then(run_notebook_edit),
        "Sleep" => from_value::<SleepInput>(input).and_then(run_sleep),
        "SendUserMessage" | "Brief" => from_value::<BriefInput>(input).and_then(run_brief),
        "Config" => from_value::<ConfigInput>(input).and_then(run_config),
        "StructuredOutput" => {
            from_value::<StructuredOutputInput>(input).and_then(run_structured_output)
        }
        "REPL" => from_value::<ReplInput>(input).and_then(run_repl),
        "PowerShell" => from_value::<PowerShellInput>(input).and_then(run_powershell),
        _ if is_dynamic_mcp_tool_name(name) => execute_dynamic_mcp_tool(name, input),
        _ => Err(format!("unsupported tool: {name}")),
    }
}

fn from_value<T: for<'de> Deserialize<'de>>(input: &Value) -> Result<T, String> {
    serde_json::from_value(input.clone()).map_err(|error| error.to_string())
}

fn run_bash(input: BashCommandInput) -> Result<String, String> {
    serde_json::to_string_pretty(&execute_bash(input).map_err(|error| error.to_string())?)
        .map_err(|error| error.to_string())
}

#[allow(clippy::needless_pass_by_value)]
fn run_read_file(input: ReadFileInput) -> Result<String, String> {
    to_pretty_json(read_file(&input.path, input.offset, input.limit).map_err(io_to_string)?)
}

#[allow(clippy::needless_pass_by_value)]
fn run_write_file(input: WriteFileInput) -> Result<String, String> {
    to_pretty_json(write_file(&input.path, &input.content).map_err(io_to_string)?)
}

#[allow(clippy::needless_pass_by_value)]
fn run_edit_file(input: EditFileInput) -> Result<String, String> {
    to_pretty_json(
        edit_file(
            &input.path,
            &input.old_string,
            &input.new_string,
            input.replace_all.unwrap_or(false),
        )
        .map_err(io_to_string)?,
    )
}

#[allow(clippy::needless_pass_by_value)]
fn run_glob_search(input: GlobSearchInputValue) -> Result<String, String> {
    to_pretty_json(glob_search(&input.pattern, input.path.as_deref()).map_err(io_to_string)?)
}

#[allow(clippy::needless_pass_by_value)]
fn run_grep_search(input: GrepSearchInput) -> Result<String, String> {
    to_pretty_json(grep_search(&input).map_err(io_to_string)?)
}

fn run_list_mcp_resources(input: ListMcpResourcesInput) -> Result<String, String> {
    to_pretty_json(execute_list_mcp_resources(input)?)
}

fn run_read_mcp_resource(input: ReadMcpResourceInput) -> Result<String, String> {
    to_pretty_json(execute_read_mcp_resource(input)?)
}

fn run_mcp_tool(input: McpToolInput) -> Result<String, String> {
    to_pretty_json(execute_mcp_tool(input)?)
}

fn run_mcp_auth(input: McpAuthInput) -> Result<String, String> {
    to_pretty_json(execute_mcp_auth(input)?)
}

#[allow(clippy::needless_pass_by_value)]
fn run_web_fetch(input: WebFetchInput) -> Result<String, String> {
    to_pretty_json(execute_web_fetch(&input)?)
}

#[allow(clippy::needless_pass_by_value)]
fn run_web_search(input: WebSearchInput) -> Result<String, String> {
    to_pretty_json(execute_web_search(&input)?)
}

fn run_todo_write(input: TodoWriteInput) -> Result<String, String> {
    to_pretty_json(execute_todo_write(input)?)
}

fn run_skill(input: SkillInput) -> Result<String, String> {
    to_pretty_json(execute_skill(input)?)
}

fn run_agent(input: AgentInput) -> Result<String, String> {
    to_pretty_json(execute_agent(input)?)
}

fn run_tool_search(input: ToolSearchInput) -> Result<String, String> {
    to_pretty_json(execute_tool_search(input))
}

fn run_notebook_edit(input: NotebookEditInput) -> Result<String, String> {
    to_pretty_json(execute_notebook_edit(input)?)
}

fn run_sleep(input: SleepInput) -> Result<String, String> {
    to_pretty_json(execute_sleep(input))
}

fn run_brief(input: BriefInput) -> Result<String, String> {
    to_pretty_json(execute_brief(input)?)
}

fn run_config(input: ConfigInput) -> Result<String, String> {
    to_pretty_json(execute_config(input)?)
}

fn run_structured_output(input: StructuredOutputInput) -> Result<String, String> {
    to_pretty_json(execute_structured_output(input))
}

fn run_repl(input: ReplInput) -> Result<String, String> {
    to_pretty_json(execute_repl(input)?)
}

fn run_powershell(input: PowerShellInput) -> Result<String, String> {
    to_pretty_json(execute_powershell(input).map_err(|error| error.to_string())?)
}

fn to_pretty_json<T: serde::Serialize>(value: T) -> Result<String, String> {
    serde_json::to_string_pretty(&value).map_err(|error| error.to_string())
}

#[allow(clippy::needless_pass_by_value)]
fn io_to_string(error: std::io::Error) -> String {
    error.to_string()
}

#[derive(Debug, Deserialize)]
struct ReadFileInput {
    path: String,
    offset: Option<usize>,
    limit: Option<usize>,
}

#[derive(Debug, Deserialize)]
struct WriteFileInput {
    path: String,
    content: String,
}

#[derive(Debug, Deserialize)]
struct EditFileInput {
    path: String,
    old_string: String,
    new_string: String,
    replace_all: Option<bool>,
}

#[derive(Debug, Deserialize)]
struct GlobSearchInputValue {
    pattern: String,
    path: Option<String>,
}

#[derive(Debug, Deserialize)]
struct ListMcpResourcesInput {
    server: String,
    cursor: Option<String>,
}

#[derive(Debug, Deserialize)]
struct ReadMcpResourceInput {
    server: String,
    uri: String,
}

#[derive(Debug, Deserialize)]
struct McpToolInput {
    server: String,
    tool: Option<String>,
    arguments: Option<Value>,
    cursor: Option<String>,
}

#[derive(Debug, Deserialize)]
#[serde(rename_all = "camelCase")]
struct McpAuthInput {
    server: Option<String>,
    action: Option<String>,
    access_token: Option<String>,
    refresh_token: Option<String>,
    expires_at: Option<u64>,
    scopes: Option<Vec<String>>,
}

#[derive(Debug, Deserialize)]
struct WebFetchInput {
    url: String,
    prompt: String,
}

#[derive(Debug, Deserialize)]
struct WebSearchInput {
    query: String,
    allowed_domains: Option<Vec<String>>,
    blocked_domains: Option<Vec<String>>,
}

#[derive(Debug, Deserialize)]
struct TodoWriteInput {
    todos: Vec<TodoItem>,
}

#[derive(Debug, Deserialize, Serialize, Clone, PartialEq, Eq)]
struct TodoItem {
    content: String,
    #[serde(rename = "activeForm")]
    active_form: String,
    status: TodoStatus,
}

#[derive(Debug, Deserialize, Serialize, Clone, PartialEq, Eq)]
#[serde(rename_all = "snake_case")]
enum TodoStatus {
    Pending,
    InProgress,
    Completed,
}

#[derive(Debug, Deserialize)]
struct SkillInput {
    skill: String,
    args: Option<String>,
}

#[derive(Debug, Deserialize)]
struct AgentInput {
    description: String,
    prompt: String,
    subagent_type: Option<String>,
    name: Option<String>,
    model: Option<String>,
}

#[derive(Debug, Deserialize)]
struct ToolSearchInput {
    query: String,
    max_results: Option<usize>,
}

#[derive(Debug, Deserialize)]
struct NotebookEditInput {
    notebook_path: String,
    cell_id: Option<String>,
    new_source: Option<String>,
    cell_type: Option<NotebookCellType>,
    edit_mode: Option<NotebookEditMode>,
}

#[derive(Debug, Deserialize, Serialize, Clone, Copy, PartialEq, Eq)]
#[serde(rename_all = "lowercase")]
enum NotebookCellType {
    Code,
    Markdown,
}

#[derive(Debug, Deserialize, Serialize, Clone, Copy, PartialEq, Eq)]
#[serde(rename_all = "lowercase")]
enum NotebookEditMode {
    Replace,
    Insert,
    Delete,
}

#[derive(Debug, Deserialize)]
struct SleepInput {
    duration_ms: u64,
}

#[derive(Debug, Deserialize)]
struct BriefInput {
    message: String,
    attachments: Option<Vec<String>>,
    status: BriefStatus,
}

#[derive(Debug, Deserialize)]
#[serde(rename_all = "lowercase")]
enum BriefStatus {
    Normal,
    Proactive,
}

#[derive(Debug, Deserialize)]
struct ConfigInput {
    setting: String,
    value: Option<ConfigValue>,
}

#[derive(Debug, Deserialize)]
#[serde(untagged)]
enum ConfigValue {
    String(String),
    Bool(bool),
    Number(f64),
}

#[derive(Debug, Deserialize)]
#[serde(transparent)]
struct StructuredOutputInput(BTreeMap<String, Value>);

#[derive(Debug, Deserialize)]
struct ReplInput {
    code: String,
    language: String,
    timeout_ms: Option<u64>,
}

#[derive(Debug, Deserialize)]
struct PowerShellInput {
    command: String,
    timeout: Option<u64>,
    description: Option<String>,
    run_in_background: Option<bool>,
}

#[derive(Debug, Serialize)]
struct WebFetchOutput {
    bytes: usize,
    code: u16,
    #[serde(rename = "codeText")]
    code_text: String,
    result: String,
    #[serde(rename = "durationMs")]
    duration_ms: u128,
    url: String,
}

#[derive(Debug, Serialize)]
struct WebSearchOutput {
    query: String,
    results: Vec<WebSearchResultItem>,
    #[serde(rename = "durationSeconds")]
    duration_seconds: f64,
}

#[derive(Debug, Serialize)]
struct TodoWriteOutput {
    #[serde(rename = "oldTodos")]
    old_todos: Vec<TodoItem>,
    #[serde(rename = "newTodos")]
    new_todos: Vec<TodoItem>,
    #[serde(rename = "verificationNudgeNeeded")]
    verification_nudge_needed: Option<bool>,
}

#[derive(Debug, Serialize)]
struct SkillOutput {
    skill: String,
    path: String,
    args: Option<String>,
    description: Option<String>,
    prompt: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct AgentOutput {
    #[serde(rename = "agentId")]
    agent_id: String,
    name: String,
    description: String,
    #[serde(rename = "subagentType")]
    subagent_type: Option<String>,
    model: Option<String>,
    status: String,
    #[serde(rename = "outputFile")]
    output_file: String,
    #[serde(rename = "manifestFile")]
    manifest_file: String,
    #[serde(rename = "createdAt")]
    created_at: String,
    #[serde(rename = "startedAt", skip_serializing_if = "Option::is_none")]
    started_at: Option<String>,
    #[serde(rename = "completedAt", skip_serializing_if = "Option::is_none")]
    completed_at: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    error: Option<String>,
}

#[derive(Debug, Clone)]
struct AgentJob {
    manifest: AgentOutput,
    prompt: String,
    system_prompt: Vec<String>,
    allowed_tools: BTreeSet<String>,
}

#[derive(Debug, Serialize)]
struct ToolSearchOutput {
    matches: Vec<String>,
    query: String,
    normalized_query: String,
    #[serde(rename = "total_deferred_tools")]
    total_deferred_tools: usize,
    #[serde(rename = "pending_mcp_servers")]
    pending_mcp_servers: Option<Vec<String>>,
}

#[derive(Debug, Serialize)]
struct NotebookEditOutput {
    new_source: String,
    cell_id: Option<String>,
    cell_type: Option<NotebookCellType>,
    language: String,
    edit_mode: String,
    error: Option<String>,
    notebook_path: String,
    original_file: String,
    updated_file: String,
}

#[derive(Debug, Serialize)]
struct SleepOutput {
    duration_ms: u64,
    message: String,
}

#[derive(Debug, Serialize)]
struct BriefOutput {
    message: String,
    attachments: Option<Vec<ResolvedAttachment>>,
    #[serde(rename = "sentAt")]
    sent_at: String,
}

#[derive(Debug, Serialize)]
struct ResolvedAttachment {
    path: String,
    size: u64,
    #[serde(rename = "isImage")]
    is_image: bool,
}

#[derive(Debug, Serialize)]
struct ConfigOutput {
    success: bool,
    operation: Option<String>,
    setting: Option<String>,
    value: Option<Value>,
    #[serde(rename = "previousValue")]
    previous_value: Option<Value>,
    #[serde(rename = "newValue")]
    new_value: Option<Value>,
    error: Option<String>,
}

#[derive(Debug, Serialize)]
struct StructuredOutputResult {
    data: String,
    structured_output: BTreeMap<String, Value>,
}

#[derive(Debug, Serialize)]
struct ReplOutput {
    language: String,
    stdout: String,
    stderr: String,
    #[serde(rename = "exitCode")]
    exit_code: i32,
    #[serde(rename = "durationMs")]
    duration_ms: u128,
}

#[derive(Debug, Serialize)]
#[serde(untagged)]
enum WebSearchResultItem {
    SearchResult {
        tool_use_id: String,
        content: Vec<SearchHit>,
    },
    Commentary(String),
}

#[derive(Debug, Serialize)]
struct SearchHit {
    title: String,
    url: String,
}

#[derive(Debug, Serialize)]
struct ListMcpResourcesOutput {
    server: String,
    transport: String,
    #[serde(rename = "resourceCount")]
    resource_count: usize,
    resources: Vec<runtime::McpResource>,
    #[serde(rename = "nextCursor", skip_serializing_if = "Option::is_none")]
    next_cursor: Option<String>,
}

#[derive(Debug, Serialize)]
struct ReadMcpResourceOutput {
    server: String,
    transport: String,
    uri: String,
    #[serde(rename = "contentCount")]
    content_count: usize,
    contents: Vec<runtime::McpResourceContents>,
}

#[derive(Debug, Serialize)]
struct McpToolCatalogOutput {
    server: String,
    transport: String,
    action: String,
    #[serde(rename = "toolCount")]
    tool_count: usize,
    tools: Vec<runtime::McpTool>,
    #[serde(rename = "nextCursor", skip_serializing_if = "Option::is_none")]
    next_cursor: Option<String>,
}

#[derive(Debug, Serialize)]
struct McpToolCallOutput {
    server: String,
    transport: String,
    action: String,
    tool: String,
    #[serde(rename = "qualifiedToolName")]
    qualified_tool_name: String,
    content: Vec<runtime::McpToolCallContent>,
    #[serde(rename = "structuredContent", skip_serializing_if = "Option::is_none")]
    structured_content: Option<Value>,
    #[serde(rename = "isError", skip_serializing_if = "Option::is_none")]
    is_error: Option<bool>,
    #[serde(rename = "_meta", skip_serializing_if = "Option::is_none")]
    meta: Option<Value>,
}

#[derive(Debug, Serialize)]
struct McpAuthOutput {
    action: String,
    #[serde(rename = "serverCount")]
    server_count: usize,
    #[serde(rename = "transportCounts")]
    transport_counts: BTreeMap<String, usize>,
    #[serde(rename = "supportedExecutionCount")]
    supported_execution_count: usize,
    #[serde(rename = "unsupportedExecutionCount")]
    unsupported_execution_count: usize,
    #[serde(rename = "statusCounts")]
    status_counts: BTreeMap<String, usize>,
    #[serde(rename = "unsupportedServers")]
    unsupported_servers: Vec<McpAuthUnsupportedServer>,
    #[serde(rename = "attentionServers")]
    attention_servers: Vec<McpAuthAttentionServer>,
    servers: Vec<McpServerAuthStatus>,
}

#[derive(Debug, Serialize)]
struct McpAuthUnsupportedServer {
    server: String,
    transport: String,
    detail: String,
}

#[derive(Debug, Serialize)]
struct McpAuthAttentionServer {
    server: String,
    transport: String,
    status: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    detail: Option<String>,
}

#[derive(Debug, Serialize)]
struct McpServerAuthStatus {
    server: String,
    scope: String,
    transport: String,
    #[serde(rename = "authKind")]
    auth_kind: String,
    #[serde(rename = "requiresUserAuth")]
    requires_user_auth: bool,
    #[serde(rename = "supportedExecution")]
    supported_execution: bool,
    #[serde(rename = "interactiveSupported")]
    interactive_supported: bool,
    status: String,
    #[serde(rename = "storedCredentials")]
    stored_credentials: bool,
    #[serde(rename = "refreshTokenPresent")]
    refresh_token_present: bool,
    #[serde(rename = "expiresAt", skip_serializing_if = "Option::is_none")]
    expires_at: Option<u64>,
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    scopes: Vec<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    detail: Option<String>,
    #[serde(rename = "clientId", skip_serializing_if = "Option::is_none")]
    client_id: Option<String>,
    #[serde(rename = "callbackPort", skip_serializing_if = "Option::is_none")]
    callback_port: Option<u16>,
    #[serde(
        rename = "authServerMetadataUrl",
        skip_serializing_if = "Option::is_none"
    )]
    auth_server_metadata_url: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    xaa: Option<bool>,
}

fn load_runtime_config_for_tools() -> Result<RuntimeConfig, String> {
    let cwd = std::env::current_dir().map_err(|error| error.to_string())?;
    ConfigLoader::default_for(cwd)
        .load()
        .map_err(|error| error.to_string())
}

fn configured_mcp_server_names(config: &RuntimeConfig) -> Vec<String> {
    config.mcp().servers().keys().cloned().collect()
}

fn mcp_auth_status_counts(servers: &[McpServerAuthStatus]) -> BTreeMap<String, usize> {
    let mut counts = BTreeMap::new();
    for server in servers {
        *counts.entry(server.status.clone()).or_default() += 1;
    }
    counts
}

fn mcp_auth_transport_counts(servers: &[McpServerAuthStatus]) -> BTreeMap<String, usize> {
    let mut counts = BTreeMap::new();
    for server in servers {
        *counts.entry(server.transport.clone()).or_default() += 1;
    }
    counts
}

fn mcp_auth_attention_servers(servers: &[McpServerAuthStatus]) -> Vec<McpAuthAttentionServer> {
    servers
        .iter()
        .filter(|server| server.status != "ready")
        .map(|server| McpAuthAttentionServer {
            server: server.server.clone(),
            transport: server.transport.clone(),
            status: server.status.clone(),
            detail: server.detail.clone(),
        })
        .collect()
}

fn mcp_auth_unsupported_servers(
    attention_servers: &[McpAuthAttentionServer],
) -> Vec<McpAuthUnsupportedServer> {
    attention_servers
        .iter()
        .filter(|server| server.status == "unsupported-transport")
        .map(|server| McpAuthUnsupportedServer {
            server: server.server.clone(),
            transport: server.transport.clone(),
            detail: server
                .detail
                .clone()
                .unwrap_or_else(|| String::from("<unknown>")),
        })
        .collect()
}

fn resolve_mcp_server_name(config: &RuntimeConfig, requested: &str) -> Result<String, String> {
    let requested = requested.trim();
    if requested.is_empty() {
        return Err(String::from("MCP server name must not be empty"));
    }

    let exact = config
        .mcp()
        .servers()
        .keys()
        .filter(|name| name.eq_ignore_ascii_case(requested))
        .cloned()
        .collect::<Vec<_>>();
    if let [matched] = exact.as_slice() {
        return Ok(matched.clone());
    }
    if exact.len() > 1 {
        return Err(format!(
            "multiple MCP servers matched `{requested}`; use an exact server name"
        ));
    }

    let normalized = runtime::normalize_name_for_mcp(requested);
    let fuzzy = config
        .mcp()
        .servers()
        .keys()
        .filter(|name| runtime::normalize_name_for_mcp(name) == normalized)
        .cloned()
        .collect::<Vec<_>>();
    match fuzzy.as_slice() {
        [matched] => Ok(matched.clone()),
        [] => {
            let configured = configured_mcp_server_names(config);
            if configured.is_empty() {
                Err(String::from("no MCP servers are configured"))
            } else {
                Err(format!(
                    "unknown MCP server `{requested}`; configured servers: {}",
                    configured.join(", ")
                ))
            }
        }
        _ => Err(format!(
            "multiple MCP servers matched `{requested}`; use an exact server name"
        )),
    }
}

#[derive(Debug, Default)]
struct DynamicMcpCatalog {
    tools: Vec<runtime::ManagedMcpTool>,
    pending_servers: Vec<String>,
}

#[derive(Debug, Deserialize)]
struct OAuthServerMetadata {
    authorization_endpoint: String,
    token_endpoint: String,
}

#[derive(Debug, Clone, PartialEq, Eq)]
struct SseFrame {
    event: Option<String>,
    data: String,
}

#[derive(Debug, Default)]
struct SseFrameParser {
    buffer: Vec<u8>,
}

impl SseFrameParser {
    fn push(&mut self, chunk: &[u8]) -> Result<Vec<SseFrame>, String> {
        self.buffer.extend_from_slice(chunk);
        let mut frames = Vec::new();
        while let Some(frame) = self.next_frame() {
            if let Some(frame) = parse_sse_frame(&frame)? {
                frames.push(frame);
            }
        }
        Ok(frames)
    }

    fn finish(&mut self) -> Result<Vec<SseFrame>, String> {
        if self.buffer.is_empty() {
            return Ok(Vec::new());
        }
        let trailing = std::mem::take(&mut self.buffer);
        match parse_sse_frame(&String::from_utf8_lossy(&trailing))? {
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

fn parse_sse_frame(frame: &str) -> Result<Option<SseFrame>, String> {
    let trimmed = frame.trim();
    if trimmed.is_empty() {
        return Ok(None);
    }

    let mut event_name = None;
    let mut data_lines = Vec::new();
    for line in trimmed.lines() {
        if line.starts_with(':') {
            continue;
        }
        if let Some(name) = line.strip_prefix("event:") {
            event_name = Some(name.trim().to_string());
            continue;
        }
        if let Some(data) = line.strip_prefix("data:") {
            data_lines.push(data.trim_start().to_string());
        }
    }

    if data_lines.is_empty() {
        return Ok(None);
    }
    let data = data_lines.join("\n");
    if data == "[DONE]" {
        return Ok(None);
    }

    Ok(Some(SseFrame {
        event: event_name,
        data,
    }))
}

fn load_stored_mcp_credentials(
    server_name: &str,
    server_config: &runtime::ScopedMcpServerConfig,
) -> Result<Option<OAuthTokenSet>, String> {
    load_mcp_oauth_credentials(&runtime::mcp_credentials_key(server_name, server_config))
        .map_err(io_to_string)
}

fn ensure_live_mcp_execution_supported(
    server_name: &str,
    server_config: &runtime::ScopedMcpServerConfig,
) -> Result<(), String> {
    let transport = McpClientTransport::from_config(&server_config.config);
    if let Some(reason) = runtime::unsupported_live_mcp_execution_reason(&transport) {
        return Err(format!(
            "MCP server `{server_name}` uses {} transport; {reason}",
            mcp_transport_label(server_config)
        ));
    }
    Ok(())
}

fn resolve_mcp_server_config<'a>(
    config: &'a RuntimeConfig,
    requested: &str,
) -> Result<(String, &'a runtime::ScopedMcpServerConfig), String> {
    let server_name = resolve_mcp_server_name(config, requested)?;
    let server_config = config
        .mcp()
        .get(&server_name)
        .ok_or_else(|| format!("unknown MCP server `{server_name}`"))?;
    Ok((server_name, server_config))
}

fn mcp_transport_name(transport: runtime::McpTransport) -> &'static str {
    runtime::mcp_transport_display_name(transport)
}

fn mcp_transport_label(config: &runtime::ScopedMcpServerConfig) -> &'static str {
    mcp_transport_name(config.transport())
}

fn config_source_label(source: runtime::ConfigSource) -> &'static str {
    match source {
        runtime::ConfigSource::User => "user",
        runtime::ConfigSource::Project => "project",
        runtime::ConfigSource::Local => "local",
    }
}

fn build_tool_async_runtime() -> Result<tokio::runtime::Runtime, String> {
    tokio::runtime::Builder::new_current_thread()
        .enable_all()
        .build()
        .map_err(|error| error.to_string())
}

fn run_mcp_manager<T>(
    config: &RuntimeConfig,
    operation: impl FnOnce(&mut McpServerManager, &tokio::runtime::Runtime) -> Result<T, String>,
) -> Result<T, String> {
    let mut manager = McpServerManager::from_runtime_config(config);
    let async_runtime = build_tool_async_runtime()?;
    let result = operation(&mut manager, &async_runtime);
    let shutdown = async_runtime
        .block_on(async { manager.shutdown().await.map_err(|error| error.to_string()) });
    match (result, shutdown) {
        (Ok(value), Ok(())) => Ok(value),
        (Err(error), Ok(())) | (Err(error), Err(_)) => Err(error),
        (Ok(_), Err(error)) => Err(error),
    }
}

fn run_mcp_jsonrpc_operation<TResult>(
    config: &RuntimeConfig,
    server_name: &str,
    method: &'static str,
    operation: impl FnOnce(
        &mut McpServerManager,
        &tokio::runtime::Runtime,
    ) -> Result<runtime::JsonRpcResponse<TResult>, String>,
) -> Result<TResult, String> {
    let response = run_mcp_manager(config, operation)?;
    if let Some(error) = response.error {
        return Err(format!(
            "MCP server `{server_name}` returned JSON-RPC error for {method}: {} ({})",
            error.message, error.code
        ));
    }
    response
        .result
        .ok_or_else(|| format!("MCP server `{server_name}` returned no result for {method}"))
}

fn trim_remote_mcp_response_body(body: &str) -> String {
    let trimmed = body.trim();
    let total_chars = trimmed.chars().count();
    if total_chars <= 240 {
        return trimmed.to_string();
    }
    let mut snippet = trimmed.chars().take(240).collect::<String>();
    snippet.push_str("...");
    snippet
}

fn apply_remote_mcp_request_headers(
    mut request: reqwest::blocking::RequestBuilder,
    headers: &BTreeMap<String, String>,
    bearer_token: Option<&str>,
    accept: &str,
) -> reqwest::blocking::RequestBuilder {
    request = request.header(reqwest::header::ACCEPT, accept);
    for (name, value) in headers {
        request = request.header(name, value);
    }
    if let Some(token) = bearer_token {
        request = request.bearer_auth(token);
    }
    request
}

fn response_is_sse(response: &reqwest::blocking::Response) -> bool {
    response
        .headers()
        .get(reqwest::header::CONTENT_TYPE)
        .and_then(|value| value.to_str().ok())
        .is_some_and(|value| value.to_ascii_lowercase().starts_with("text/event-stream"))
}

fn extract_matching_jsonrpc_response_from_value<TResult: DeserializeOwned>(
    server_name: &str,
    method: &'static str,
    value: Value,
    expected_id: &runtime::JsonRpcId,
) -> Result<Option<runtime::JsonRpcResponse<TResult>>, String> {
    match value {
        Value::Array(items) => {
            for item in items {
                if let Some(response) = extract_matching_jsonrpc_response_from_value(
                    server_name,
                    method,
                    item,
                    expected_id,
                )? {
                    return Ok(Some(response));
                }
            }
            Ok(None)
        }
        Value::Object(object) => {
            let is_response = object.contains_key("result") || object.contains_key("error");
            if !is_response {
                return Ok(None);
            }
            let Some(id_value) = object.get("id") else {
                return Ok(None);
            };
            let parsed_id = serde_json::from_value::<runtime::JsonRpcId>(id_value.clone())
                .map_err(|error| {
                    format!(
                        "invalid JSON-RPC id from MCP server `{server_name}` for {method}: {error}"
                    )
                })?;
            if parsed_id != *expected_id {
                return Ok(None);
            }
            serde_json::from_value::<runtime::JsonRpcResponse<TResult>>(Value::Object(object))
                .map(Some)
                .map_err(|error| {
                    format!(
                        "invalid JSON-RPC response from MCP server `{server_name}` for {method}: {error}"
                    )
                })
        }
        _ => Ok(None),
    }
}

fn resolve_remote_jsonrpc_response<TResult>(
    server_name: &str,
    method: &'static str,
    response: runtime::JsonRpcResponse<TResult>,
) -> Result<TResult, String> {
    if let Some(error) = response.error {
        return Err(format!(
            "MCP server `{server_name}` returned JSON-RPC error for {method}: {} ({})",
            error.message, error.code
        ));
    }
    response
        .result
        .ok_or_else(|| format!("MCP server `{server_name}` returned no result for {method}"))
}

fn parse_http_jsonrpc_response_body<TResult: DeserializeOwned>(
    server_name: &str,
    method: &'static str,
    body: &str,
    expected_id: &runtime::JsonRpcId,
) -> Result<TResult, String> {
    let value: Value = serde_json::from_str(body).map_err(|error| {
        format!("invalid JSON-RPC response from MCP server `{server_name}` for {method}: {error}")
    })?;
    let response =
        extract_matching_jsonrpc_response_from_value(server_name, method, value, expected_id)?
            .ok_or_else(|| {
                format!(
            "MCP server `{server_name}` returned no matching JSON-RPC response for {method}"
        )
            })?;
    resolve_remote_jsonrpc_response(server_name, method, response)
}

fn resolve_sse_endpoint_url(base_url: &str, endpoint: &str) -> Result<String, String> {
    let trimmed = endpoint.trim();
    let base_url = reqwest::Url::parse(base_url).map_err(|error| error.to_string())?;
    if let Ok(absolute) = reqwest::Url::parse(trimmed) {
        return Ok(absolute.to_string());
    }
    base_url
        .join(trimmed)
        .map(|url| url.to_string())
        .map_err(|error| error.to_string())
}

fn maybe_extract_jsonrpc_response_from_sse_frame<TResult: DeserializeOwned>(
    server_name: &str,
    method: &'static str,
    frame: SseFrame,
    expected_id: &runtime::JsonRpcId,
) -> Result<Option<TResult>, String> {
    let Ok(value) = serde_json::from_str::<Value>(&frame.data) else {
        return Ok(None);
    };
    let Some(response) =
        extract_matching_jsonrpc_response_from_value(server_name, method, value, expected_id)?
    else {
        return Ok(None);
    };
    resolve_remote_jsonrpc_response(server_name, method, response).map(Some)
}

fn maybe_extract_jsonrpc_response_from_websocket_payload<TResult: DeserializeOwned>(
    server_name: &str,
    method: &'static str,
    payload: &str,
    expected_id: &runtime::JsonRpcId,
) -> Result<Option<TResult>, String> {
    let Ok(value) = serde_json::from_str::<Value>(payload) else {
        return Ok(None);
    };
    let Some(response) =
        extract_matching_jsonrpc_response_from_value(server_name, method, value, expected_id)?
    else {
        return Ok(None);
    };
    resolve_remote_jsonrpc_response(server_name, method, response).map(Some)
}

fn read_matching_jsonrpc_response_from_sse_stream<TResult: DeserializeOwned>(
    server_name: &str,
    method: &'static str,
    expected_id: &runtime::JsonRpcId,
    mut response: reqwest::blocking::Response,
) -> Result<TResult, String> {
    let mut parser = SseFrameParser::default();
    let mut buffer = [0_u8; 4096];

    loop {
        let read = response.read(&mut buffer).map_err(|error| {
            format!(
                "failed to read SSE response from MCP server `{server_name}` for {method}: {error}"
            )
        })?;
        if read == 0 {
            break;
        }
        for frame in parser.push(&buffer[..read])? {
            if let Some(result) = maybe_extract_jsonrpc_response_from_sse_frame(
                server_name,
                method,
                frame,
                expected_id,
            )? {
                return Ok(result);
            }
        }
    }

    for frame in parser.finish()? {
        if let Some(result) =
            maybe_extract_jsonrpc_response_from_sse_frame(server_name, method, frame, expected_id)?
        {
            return Ok(result);
        }
    }

    Err(format!(
        "MCP server `{server_name}` returned no matching JSON-RPC response for {method} on SSE stream"
    ))
}

fn read_legacy_sse_endpoint(
    server_name: &str,
    sse_url: &str,
    mut response: reqwest::blocking::Response,
) -> Result<(String, reqwest::blocking::Response), String> {
    let mut parser = SseFrameParser::default();
    let mut buffer = [0_u8; 4096];

    loop {
        let read = response.read(&mut buffer).map_err(|error| {
            format!(
                "failed to read SSE endpoint bootstrap from MCP server `{server_name}`: {error}"
            )
        })?;
        if read == 0 {
            break;
        }
        for frame in parser.push(&buffer[..read])? {
            if frame.event.as_deref() == Some("endpoint") {
                let endpoint = resolve_sse_endpoint_url(sse_url, &frame.data).map_err(|error| {
                    format!("invalid SSE endpoint from MCP server `{server_name}`: {error}")
                })?;
                return Ok((endpoint, response));
            }
        }
    }

    Err(format!(
        "MCP server `{server_name}` did not provide an SSE endpoint event"
    ))
}

fn fetch_mcp_oauth_metadata(
    server_name: &str,
    metadata_url: &str,
) -> Result<OAuthServerMetadata, String> {
    let client = build_http_client()?;
    let response = client.get(metadata_url).send().map_err(|error| {
        format!("failed to fetch OAuth metadata for MCP server `{server_name}`: {error}")
    })?;
    let status = response.status();
    let body = response.text().map_err(|error| {
        format!("failed to read OAuth metadata response for MCP server `{server_name}`: {error}")
    })?;
    if !status.is_success() {
        return Err(format!(
            "OAuth metadata request for MCP server `{server_name}` failed with HTTP {}: {}",
            status.as_u16(),
            trim_remote_mcp_response_body(&body)
        ));
    }
    serde_json::from_str(&body).map_err(|error| {
        format!("invalid OAuth metadata response for MCP server `{server_name}`: {error}")
    })
}

fn build_mcp_oauth_config(
    server_name: &str,
    oauth: &runtime::McpOAuthConfig,
) -> Result<runtime::OAuthConfig, String> {
    let client_id = oauth
        .client_id
        .clone()
        .ok_or_else(|| format!("MCP server `{server_name}` is missing an OAuth client_id"))?;
    let metadata_url = oauth.auth_server_metadata_url.clone().ok_or_else(|| {
        format!("MCP server `{server_name}` is missing an OAuth authServerMetadataUrl")
    })?;
    let metadata = fetch_mcp_oauth_metadata(server_name, &metadata_url)?;
    Ok(runtime::OAuthConfig {
        client_id,
        authorize_url: metadata.authorization_endpoint,
        token_url: metadata.token_endpoint,
        callback_port: oauth.callback_port,
        manual_redirect_url: None,
        scopes: Vec::new(),
    })
}

fn refresh_stored_mcp_credentials(
    server_name: &str,
    server_config: &runtime::ScopedMcpServerConfig,
    oauth: &runtime::McpOAuthConfig,
    existing: &OAuthTokenSet,
) -> Result<OAuthTokenSet, String> {
    let refresh_token = existing.refresh_token.clone().ok_or_else(|| {
        format!(
            "stored OAuth credentials for MCP server `{server_name}` are expired and do not include a refresh token"
        )
    })?;
    let oauth_config = build_mcp_oauth_config(server_name, oauth)?;
    let refresh_request = OAuthRefreshRequest::from_config(
        &oauth_config,
        refresh_token,
        Some(existing.scopes.clone()),
    );
    let client = build_http_client()?;
    let response = client
        .post(&oauth_config.token_url)
        .header(
            reqwest::header::CONTENT_TYPE,
            "application/x-www-form-urlencoded",
        )
        .form(&refresh_request.form_params())
        .send()
        .map_err(|error| {
            format!("failed to refresh OAuth credentials for MCP server `{server_name}`: {error}")
        })?;
    let status = response.status();
    let body = response.text().map_err(|error| {
        format!("failed to read OAuth refresh response for MCP server `{server_name}`: {error}")
    })?;
    if !status.is_success() {
        return Err(format!(
            "OAuth refresh for MCP server `{server_name}` failed with HTTP {}: {}",
            status.as_u16(),
            trim_remote_mcp_response_body(&body)
        ));
    }
    let mut refreshed: OAuthTokenSet = serde_json::from_str(&body).map_err(|error| {
        format!("invalid OAuth refresh response for MCP server `{server_name}`: {error}")
    })?;
    if refreshed.refresh_token.is_none() {
        refreshed.refresh_token = existing.refresh_token.clone();
    }
    if refreshed.scopes.is_empty() {
        refreshed.scopes = existing.scopes.clone();
    }
    save_mcp_oauth_credentials(
        &runtime::mcp_credentials_key(server_name, server_config),
        &refreshed,
    )
    .map_err(io_to_string)?;
    Ok(refreshed)
}

fn resolve_remote_mcp_bearer_token(
    server_name: &str,
    server_config: &runtime::ScopedMcpServerConfig,
    remote: &McpRemoteServerConfig,
) -> Result<Option<String>, String> {
    match remote.oauth.as_ref() {
        None => Ok(None),
        Some(oauth) => {
            let stored = load_stored_mcp_credentials(server_name, server_config)?.ok_or_else(|| {
                format!(
                    "MCP server `{server_name}` requires stored OAuth credentials; save them with McpAuthTool action `save`"
                )
            })?;
            let token_set = if runtime::mcp_oauth_token_is_expired(&stored) {
                refresh_stored_mcp_credentials(server_name, server_config, oauth, &stored)?
            } else {
                stored
            };
            Ok(Some(token_set.access_token))
        }
    }
}

fn run_remote_mcp_jsonrpc_operation<TResult: DeserializeOwned>(
    server_name: &str,
    server_config: &runtime::ScopedMcpServerConfig,
    remote: &McpRemoteServerConfig,
    method: &'static str,
    params: Option<Value>,
) -> Result<TResult, String> {
    ensure_live_mcp_execution_supported(server_name, server_config)?;
    let client = build_http_client()?;
    let bearer_token = resolve_remote_mcp_bearer_token(server_name, server_config, remote)?;
    let request_id = runtime::JsonRpcId::String(format!("mcp:{method}"));
    let payload = runtime::JsonRpcRequest::new(request_id.clone(), method, params);
    let response = apply_remote_mcp_request_headers(
        client.post(&remote.url),
        &remote.headers,
        bearer_token.as_deref(),
        "application/json, text/event-stream",
    )
    .json(&payload)
    .send()
    .map_err(|error| format!("MCP server `{server_name}` {method} request failed: {error}"))?;
    let status = response.status();
    if !status.is_success() {
        let body = response.text().map_err(|error| {
            format!("failed to read {method} response from MCP server `{server_name}`: {error}")
        })?;
        return Err(format!(
            "MCP server `{server_name}` returned HTTP {} for {method}: {}",
            status.as_u16(),
            trim_remote_mcp_response_body(&body)
        ));
    }

    if response_is_sse(&response) {
        return read_matching_jsonrpc_response_from_sse_stream(
            server_name,
            method,
            &request_id,
            response,
        );
    }

    let body = response.text().map_err(|error| {
        format!("failed to read {method} response from MCP server `{server_name}`: {error}")
    })?;
    parse_http_jsonrpc_response_body(server_name, method, &body, &request_id)
}

fn run_websocket_mcp_jsonrpc_operation<TResult: DeserializeOwned>(
    server_name: &str,
    server_config: &runtime::ScopedMcpServerConfig,
    remote: &McpWebSocketServerConfig,
    method: &'static str,
    params: Option<Value>,
) -> Result<TResult, String> {
    ensure_live_mcp_execution_supported(server_name, server_config)?;
    let mut request = remote.url.clone().into_client_request().map_err(|error| {
        format!("failed to build websocket request for MCP server `{server_name}`: {error}")
    })?;
    for (name, value) in &remote.headers {
        let header_name =
            tungstenite::http::HeaderName::try_from(name.as_str()).map_err(|error| {
                format!("invalid websocket header name for MCP server `{server_name}`: {error}")
            })?;
        let header_value = tungstenite::http::HeaderValue::from_str(value).map_err(|error| {
            format!("invalid websocket header value for MCP server `{server_name}`: {error}")
        })?;
        request.headers_mut().insert(header_name, header_value);
    }
    let (mut websocket, _) = connect_websocket(request).map_err(|error| {
        format!("failed to connect to MCP server `{server_name}` over websocket: {error}")
    })?;

    let request_id = runtime::JsonRpcId::String(format!("mcp:{method}"));
    let payload = runtime::JsonRpcRequest::new(request_id.clone(), method, params);
    let payload = serde_json::to_string(&payload).map_err(|error| {
        format!("failed to encode JSON-RPC payload for MCP server `{server_name}`: {error}")
    })?;
    websocket
        .send(WebSocketMessage::Text(payload.into()))
        .map_err(|error| {
            format!(
                "failed to send {method} websocket request to MCP server `{server_name}`: {error}"
            )
        })?;

    loop {
        let message = websocket.read().map_err(|error| {
            format!(
                "failed to read {method} websocket response from MCP server `{server_name}`: {error}"
            )
        })?;
        match message {
            WebSocketMessage::Text(text) => {
                if let Some(result) = maybe_extract_jsonrpc_response_from_websocket_payload(
                    server_name,
                    method,
                    text.as_ref(),
                    &request_id,
                )? {
                    return Ok(result);
                }
            }
            WebSocketMessage::Binary(data) => {
                let Ok(payload) = String::from_utf8(data.to_vec()) else {
                    continue;
                };
                if let Some(result) = maybe_extract_jsonrpc_response_from_websocket_payload(
                    server_name,
                    method,
                    &payload,
                    &request_id,
                )? {
                    return Ok(result);
                }
            }
            WebSocketMessage::Ping(payload) => {
                websocket.send(WebSocketMessage::Pong(payload)).map_err(|error| {
                    format!(
                        "failed to respond to websocket ping from MCP server `{server_name}`: {error}"
                    )
                })?;
            }
            WebSocketMessage::Pong(_) => {}
            WebSocketMessage::Close(_) => break,
            _ => {}
        }
    }

    Err(format!(
        "MCP server `{server_name}` returned no matching JSON-RPC response for {method} on websocket transport"
    ))
}

fn run_legacy_sse_mcp_jsonrpc_operation<TResult: DeserializeOwned>(
    server_name: &str,
    server_config: &runtime::ScopedMcpServerConfig,
    remote: &McpRemoteServerConfig,
    method: &'static str,
    params: Option<Value>,
) -> Result<TResult, String> {
    ensure_live_mcp_execution_supported(server_name, server_config)?;
    let client = build_http_client()?;
    let bearer_token = resolve_remote_mcp_bearer_token(server_name, server_config, remote)?;
    let sse_response = apply_remote_mcp_request_headers(
        client.get(&remote.url),
        &remote.headers,
        bearer_token.as_deref(),
        "text/event-stream",
    )
    .send()
    .map_err(|error| {
        format!("failed to open SSE stream for MCP server `{server_name}`: {error}")
    })?;
    let status = sse_response.status();
    if !status.is_success() {
        let body = sse_response.text().map_err(|error| {
            format!("failed to read SSE bootstrap error from MCP server `{server_name}`: {error}")
        })?;
        return Err(format!(
            "MCP server `{server_name}` returned HTTP {} while opening SSE stream: {}",
            status.as_u16(),
            trim_remote_mcp_response_body(&body)
        ));
    }
    if !response_is_sse(&sse_response) {
        return Err(format!(
            "MCP server `{server_name}` did not return an SSE stream for the configured sse transport"
        ));
    }

    let (endpoint_url, sse_response) =
        read_legacy_sse_endpoint(server_name, &remote.url, sse_response)?;
    let request_id = runtime::JsonRpcId::String(format!("mcp:{method}"));
    let payload = runtime::JsonRpcRequest::new(request_id.clone(), method, params);
    let post_response = apply_remote_mcp_request_headers(
        client.post(endpoint_url),
        &remote.headers,
        bearer_token.as_deref(),
        "application/json, text/event-stream",
    )
    .json(&payload)
    .send()
    .map_err(|error| {
        format!(
            "MCP server `{server_name}` {method} POST request failed over SSE transport: {error}"
        )
    })?;
    let post_status = post_response.status();
    if !post_status.is_success() {
        let body = post_response.text().map_err(|error| {
            format!(
                "failed to read {method} POST response from MCP server `{server_name}`: {error}"
            )
        })?;
        return Err(format!(
            "MCP server `{server_name}` returned HTTP {} for {method} over SSE transport: {}",
            post_status.as_u16(),
            trim_remote_mcp_response_body(&body)
        ));
    }

    if response_is_sse(&post_response) {
        return read_matching_jsonrpc_response_from_sse_stream(
            server_name,
            method,
            &request_id,
            post_response,
        );
    }

    let body = post_response.text().map_err(|error| {
        format!("failed to read {method} POST response from MCP server `{server_name}`: {error}")
    })?;
    if !body.trim().is_empty() {
        if let Ok(result) =
            parse_http_jsonrpc_response_body(server_name, method, &body, &request_id)
        {
            return Ok(result);
        }
    }

    read_matching_jsonrpc_response_from_sse_stream(server_name, method, &request_id, sse_response)
}

fn list_mcp_tools_for_server(
    config: &RuntimeConfig,
    server_name: &str,
    cursor: Option<String>,
) -> Result<(String, runtime::McpListToolsResult), String> {
    let server_config = config
        .mcp()
        .get(server_name)
        .ok_or_else(|| format!("unknown MCP server `{server_name}`"))?;
    let transport = mcp_transport_label(server_config).to_string();
    match &server_config.config {
        McpServerConfig::Stdio(_) => {
            let request_server = server_name.to_string();
            let request_cursor = cursor.clone();
            let result = run_mcp_jsonrpc_operation(
                config,
                server_name,
                "tools/list",
                move |manager, async_runtime| {
                    async_runtime.block_on(async {
                        manager
                            .list_tools_for_server(&request_server, request_cursor.clone())
                            .await
                            .map_err(|error| error.to_string())
                    })
                },
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Http(remote) => {
            let params = cursor.map(|cursor| json!({ "cursor": cursor }));
            let result = run_remote_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "tools/list",
                params,
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Sse(remote) => {
            let params = cursor.map(|cursor| json!({ "cursor": cursor }));
            let result = run_legacy_sse_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "tools/list",
                params,
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Ws(remote) => {
            let params = cursor.map(|cursor| json!({ "cursor": cursor }));
            let result = run_websocket_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "tools/list",
                params,
            )?;
            Ok((transport, result))
        }
        _ => {
            ensure_live_mcp_execution_supported(server_name, server_config)?;
            unreachable!("unsupported transport was not rejected")
        }
    }
}

fn call_mcp_tool_for_server(
    config: &RuntimeConfig,
    server_name: &str,
    tool_name: &str,
    arguments: Option<Value>,
) -> Result<(String, runtime::McpToolCallResult), String> {
    let server_config = config
        .mcp()
        .get(server_name)
        .ok_or_else(|| format!("unknown MCP server `{server_name}`"))?;
    let transport = mcp_transport_label(server_config).to_string();
    match &server_config.config {
        McpServerConfig::Stdio(_) => {
            let request_server = server_name.to_string();
            let request_tool = tool_name.to_string();
            let request_arguments = arguments.clone();
            let result = run_mcp_jsonrpc_operation(
                config,
                server_name,
                "tools/call",
                move |manager, async_runtime| {
                    async_runtime.block_on(async {
                        manager
                            .call_named_tool(
                                &request_server,
                                &request_tool,
                                request_arguments.clone(),
                            )
                            .await
                            .map_err(|error| error.to_string())
                    })
                },
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Http(remote) => {
            let params = serde_json::to_value(runtime::McpToolCallParams {
                name: tool_name.to_string(),
                arguments,
                meta: None,
            })
            .map_err(|error| error.to_string())?;
            let result = run_remote_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "tools/call",
                Some(params),
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Sse(remote) => {
            let params = serde_json::to_value(runtime::McpToolCallParams {
                name: tool_name.to_string(),
                arguments,
                meta: None,
            })
            .map_err(|error| error.to_string())?;
            let result = run_legacy_sse_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "tools/call",
                Some(params),
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Ws(remote) => {
            let params = serde_json::to_value(runtime::McpToolCallParams {
                name: tool_name.to_string(),
                arguments,
                meta: None,
            })
            .map_err(|error| error.to_string())?;
            let result = run_websocket_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "tools/call",
                Some(params),
            )?;
            Ok((transport, result))
        }
        _ => {
            ensure_live_mcp_execution_supported(server_name, server_config)?;
            unreachable!("unsupported transport was not rejected")
        }
    }
}

fn list_mcp_resources_for_server(
    config: &RuntimeConfig,
    server_name: &str,
    cursor: Option<String>,
) -> Result<(String, runtime::McpListResourcesResult), String> {
    let server_config = config
        .mcp()
        .get(server_name)
        .ok_or_else(|| format!("unknown MCP server `{server_name}`"))?;
    let transport = mcp_transport_label(server_config).to_string();
    match &server_config.config {
        McpServerConfig::Stdio(_) => {
            let request_server = server_name.to_string();
            let request_cursor = cursor.clone();
            let result = run_mcp_jsonrpc_operation(
                config,
                server_name,
                "resources/list",
                move |manager, async_runtime| {
                    async_runtime.block_on(async {
                        manager
                            .list_resources(&request_server, request_cursor.clone())
                            .await
                            .map_err(|error| error.to_string())
                    })
                },
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Http(remote) => {
            let params = cursor.map(|cursor| json!({ "cursor": cursor }));
            let result = run_remote_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "resources/list",
                params,
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Sse(remote) => {
            let params = cursor.map(|cursor| json!({ "cursor": cursor }));
            let result = run_legacy_sse_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "resources/list",
                params,
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Ws(remote) => {
            let params = cursor.map(|cursor| json!({ "cursor": cursor }));
            let result = run_websocket_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "resources/list",
                params,
            )?;
            Ok((transport, result))
        }
        _ => {
            ensure_live_mcp_execution_supported(server_name, server_config)?;
            unreachable!("unsupported transport was not rejected")
        }
    }
}

fn read_mcp_resource_for_server(
    config: &RuntimeConfig,
    server_name: &str,
    uri: &str,
) -> Result<(String, runtime::McpReadResourceResult), String> {
    let server_config = config
        .mcp()
        .get(server_name)
        .ok_or_else(|| format!("unknown MCP server `{server_name}`"))?;
    let transport = mcp_transport_label(server_config).to_string();
    match &server_config.config {
        McpServerConfig::Stdio(_) => {
            let request_server = server_name.to_string();
            let request_uri = uri.to_string();
            let result = run_mcp_jsonrpc_operation(
                config,
                server_name,
                "resources/read",
                move |manager, async_runtime| {
                    async_runtime.block_on(async {
                        manager
                            .read_resource(&request_server, &request_uri)
                            .await
                            .map_err(|error| error.to_string())
                    })
                },
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Http(remote) => {
            let params = serde_json::to_value(runtime::McpReadResourceParams {
                uri: uri.to_string(),
            })
            .map_err(|error| error.to_string())?;
            let result = run_remote_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "resources/read",
                Some(params),
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Sse(remote) => {
            let params = serde_json::to_value(runtime::McpReadResourceParams {
                uri: uri.to_string(),
            })
            .map_err(|error| error.to_string())?;
            let result = run_legacy_sse_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "resources/read",
                Some(params),
            )?;
            Ok((transport, result))
        }
        McpServerConfig::Ws(remote) => {
            let params = serde_json::to_value(runtime::McpReadResourceParams {
                uri: uri.to_string(),
            })
            .map_err(|error| error.to_string())?;
            let result = run_websocket_mcp_jsonrpc_operation(
                server_name,
                server_config,
                remote,
                "resources/read",
                Some(params),
            )?;
            Ok((transport, result))
        }
        _ => {
            ensure_live_mcp_execution_supported(server_name, server_config)?;
            unreachable!("unsupported transport was not rejected")
        }
    }
}

fn discover_mcp_tools_for_server(
    config: &RuntimeConfig,
    server_name: &str,
) -> Result<Vec<runtime::ManagedMcpTool>, String> {
    let mut cursor = None;
    let mut discovered = Vec::new();
    loop {
        let (_, result) = list_mcp_tools_for_server(config, server_name, cursor.clone())?;
        discovered.extend(
            result
                .tools
                .into_iter()
                .map(|tool| runtime::ManagedMcpTool {
                    server_name: server_name.to_string(),
                    qualified_name: runtime::mcp_tool_name(server_name, &tool.name),
                    raw_name: tool.name.clone(),
                    tool,
                }),
        );
        if result.next_cursor.is_none() || result.next_cursor == cursor {
            break;
        }
        cursor = result.next_cursor;
    }
    Ok(discovered)
}

fn dynamic_mcp_catalog(allowed_tools: Option<&BTreeSet<String>>) -> DynamicMcpCatalog {
    if allowed_tools.is_some_and(|allowed| !allowed.contains("MCPTool")) {
        return DynamicMcpCatalog::default();
    }
    let Ok(config) = load_runtime_config_for_tools() else {
        return DynamicMcpCatalog::default();
    };
    let mut catalog = DynamicMcpCatalog::default();
    for server_name in configured_mcp_server_names(&config) {
        match discover_mcp_tools_for_server(&config, &server_name) {
            Ok(tools) => catalog.tools.extend(tools),
            Err(_) => catalog.pending_servers.push(server_name),
        }
    }
    catalog.pending_servers.sort();
    catalog.pending_servers.dedup();
    catalog
}

fn dynamic_mcp_tool_definitions(allowed_tools: Option<&BTreeSet<String>>) -> Vec<ToolDefinition> {
    dynamic_mcp_catalog(allowed_tools)
        .tools
        .into_iter()
        .map(|tool| ToolDefinition {
            name: tool.qualified_name,
            description: Some(tool.tool.description.unwrap_or_else(|| {
                format!(
                    "Invoke MCP tool `{}` on configured server `{}`.",
                    tool.raw_name, tool.server_name
                )
            })),
            input_schema: tool
                .tool
                .input_schema
                .unwrap_or_else(|| json!({ "type": "object", "additionalProperties": true })),
        })
        .collect()
}

fn resolve_dynamic_mcp_tool(
    config: &RuntimeConfig,
    qualified_tool_name: &str,
) -> Result<runtime::ManagedMcpTool, String> {
    let server_name = configured_mcp_server_names(config)
        .into_iter()
        .find(|server_name| qualified_tool_name.starts_with(&runtime::mcp_tool_prefix(server_name)))
        .ok_or_else(|| format!("unknown MCP tool `{qualified_tool_name}`"))?;
    discover_mcp_tools_for_server(config, &server_name)?
        .into_iter()
        .find(|tool| tool.qualified_name == qualified_tool_name)
        .ok_or_else(|| {
            format!(
                "MCP tool `{qualified_tool_name}` is not currently exposed by server `{server_name}`"
            )
        })
}

fn execute_dynamic_mcp_tool(name: &str, input: &Value) -> Result<String, String> {
    let config = load_runtime_config_for_tools()?;
    let tool = resolve_dynamic_mcp_tool(&config, name)?;
    let arguments = (!input.is_null()).then(|| input.clone());
    let (transport, result) =
        call_mcp_tool_for_server(&config, &tool.server_name, &tool.raw_name, arguments)?;
    let output = serde_json::to_value(McpToolCallOutput {
        server: tool.server_name.clone(),
        transport,
        action: String::from("call_tool"),
        tool: tool.raw_name.clone(),
        qualified_tool_name: tool.qualified_name,
        content: result.content,
        structured_content: result.structured_content,
        is_error: result.is_error,
        meta: result.meta,
    })
    .map_err(|error| error.to_string())?;
    to_pretty_json(output)
}

fn execute_list_mcp_resources(
    input: ListMcpResourcesInput,
) -> Result<ListMcpResourcesOutput, String> {
    let config = load_runtime_config_for_tools()?;
    let (server_name, _) = resolve_mcp_server_config(&config, &input.server)?;
    let (transport, result) = list_mcp_resources_for_server(&config, &server_name, input.cursor)?;
    let resource_count = result.resources.len();
    Ok(ListMcpResourcesOutput {
        server: server_name,
        transport,
        resource_count,
        resources: result.resources,
        next_cursor: result.next_cursor,
    })
}

fn execute_read_mcp_resource(input: ReadMcpResourceInput) -> Result<ReadMcpResourceOutput, String> {
    let config = load_runtime_config_for_tools()?;
    let (server_name, _) = resolve_mcp_server_config(&config, &input.server)?;
    let (transport, result) = read_mcp_resource_for_server(&config, &server_name, &input.uri)?;
    let content_count = result.contents.len();
    Ok(ReadMcpResourceOutput {
        server: server_name,
        transport,
        uri: input.uri,
        content_count,
        contents: result.contents,
    })
}

fn execute_mcp_tool(input: McpToolInput) -> Result<Value, String> {
    if input.tool.is_none() && input.arguments.is_some() {
        return Err(String::from("MCPTool arguments require a tool name"));
    }
    if input.tool.is_some() && input.cursor.is_some() {
        return Err(String::from(
            "MCPTool cursor is only valid when listing tools",
        ));
    }

    let config = load_runtime_config_for_tools()?;
    let (server_name, _) = resolve_mcp_server_config(&config, &input.server)?;

    match input.tool {
        Some(tool_name) => {
            let tool_name = tool_name.trim().to_string();
            if tool_name.is_empty() {
                return Err(String::from("MCPTool tool name must not be empty"));
            }
            let (transport, result) =
                call_mcp_tool_for_server(&config, &server_name, &tool_name, input.arguments)?;
            serde_json::to_value(McpToolCallOutput {
                server: server_name.clone(),
                transport,
                action: String::from("call_tool"),
                tool: tool_name.clone(),
                qualified_tool_name: runtime::mcp_tool_name(&server_name, &tool_name),
                content: result.content,
                structured_content: result.structured_content,
                is_error: result.is_error,
                meta: result.meta,
            })
            .map_err(|error| error.to_string())
        }
        None => {
            let (transport, result) =
                list_mcp_tools_for_server(&config, &server_name, input.cursor)?;
            let tool_count = result.tools.len();
            serde_json::to_value(McpToolCatalogOutput {
                server: server_name,
                transport,
                action: String::from("list_tools"),
                tool_count,
                tools: result.tools,
                next_cursor: result.next_cursor,
            })
            .map_err(|error| error.to_string())
        }
    }
}

fn mcp_status_for_server(
    server_name: &str,
    server_config: &runtime::ScopedMcpServerConfig,
) -> Result<McpServerAuthStatus, String> {
    let scope = config_source_label(server_config.scope).to_string();
    let status =
        runtime::mcp_server_auth_status(server_name, server_config).map_err(io_to_string)?;
    Ok(McpServerAuthStatus {
        server: server_name.to_string(),
        scope,
        transport: status.transport,
        auth_kind: status.auth_kind,
        requires_user_auth: status.requires_user_auth,
        supported_execution: status.supported_execution,
        interactive_supported: status.interactive_supported,
        status: status.status,
        stored_credentials: status.stored_credentials,
        refresh_token_present: status.refresh_token_present,
        expires_at: status.expires_at,
        scopes: status.scopes,
        detail: status.detail,
        client_id: status.client_id,
        callback_port: status.callback_port,
        auth_server_metadata_url: status.auth_server_metadata_url,
        xaa: status.xaa,
    })
}

fn mcp_oauth_config_for_server<'a>(
    server_name: &str,
    server_config: &'a runtime::ScopedMcpServerConfig,
) -> Result<&'a runtime::McpOAuthConfig, String> {
    match &server_config.config {
        McpServerConfig::Http(remote) | McpServerConfig::Sse(remote) => remote
            .oauth
            .as_ref()
            .ok_or_else(|| format!("MCP server `{server_name}` does not use OAuth credentials")),
        _ => Err(format!(
            "MCP server `{server_name}` does not expose per-server OAuth credentials"
        )),
    }
}

fn execute_mcp_auth(input: McpAuthInput) -> Result<McpAuthOutput, String> {
    let config = load_runtime_config_for_tools()?;
    let action = input.action.as_deref().unwrap_or("status");
    let server_names = match (action, input.server.as_deref()) {
        ("save" | "logout", Some(server)) => vec![resolve_mcp_server_name(&config, server)?],
        ("save" | "logout", None) => {
            return Err(format!(
                "McpAuthTool action `{action}` requires a server name"
            ));
        }
        (_, Some(server)) => vec![resolve_mcp_server_name(&config, server)?],
        (_, None) => configured_mcp_server_names(&config),
    };

    match action {
        "status" => {}
        "save" => {
            let server_name = server_names
                .first()
                .expect("save action resolves one server");
            let server_config = config
                .mcp()
                .get(server_name)
                .expect("resolved MCP server must exist");
            let _oauth = mcp_oauth_config_for_server(server_name, server_config)?;
            let access_token = input
                .access_token
                .as_deref()
                .map(str::trim)
                .filter(|value| !value.is_empty())
                .ok_or_else(|| {
                    String::from("McpAuthTool action `save` requires a non-empty accessToken")
                })?;
            let refresh_token = input
                .refresh_token
                .as_deref()
                .map(str::trim)
                .filter(|value| !value.is_empty())
                .map(ToOwned::to_owned);
            let scopes = input
                .scopes
                .unwrap_or_default()
                .into_iter()
                .map(|scope| scope.trim().to_string())
                .filter(|scope| !scope.is_empty())
                .collect::<Vec<_>>();
            let token_set = OAuthTokenSet {
                access_token: access_token.to_string(),
                refresh_token,
                expires_at: input.expires_at,
                scopes,
            };
            save_mcp_oauth_credentials(
                &runtime::mcp_credentials_key(server_name, server_config),
                &token_set,
            )
            .map_err(io_to_string)?;
        }
        "logout" => {
            let server_name = server_names
                .first()
                .expect("logout action resolves one server");
            let server_config = config
                .mcp()
                .get(server_name)
                .expect("resolved MCP server must exist");
            let _oauth = mcp_oauth_config_for_server(server_name, server_config)?;
            clear_mcp_oauth_credentials(&runtime::mcp_credentials_key(server_name, server_config))
                .map_err(io_to_string)?;
        }
        other => {
            return Err(format!("unknown McpAuthTool action `{other}`"));
        }
    }

    let servers = server_names
        .iter()
        .map(|server_name| {
            let server_config = config
                .mcp()
                .get(server_name)
                .expect("resolved MCP server must exist");
            mcp_status_for_server(server_name, server_config)
        })
        .collect::<Result<Vec<_>, _>>()?;

    let supported_execution_count = servers
        .iter()
        .filter(|server| server.supported_execution)
        .count();
    let unsupported_execution_count = servers.len().saturating_sub(supported_execution_count);
    let transport_counts = mcp_auth_transport_counts(&servers);
    let status_counts = mcp_auth_status_counts(&servers);
    let attention_servers = mcp_auth_attention_servers(&servers);
    let unsupported_servers = mcp_auth_unsupported_servers(&attention_servers);

    Ok(McpAuthOutput {
        action: action.to_string(),
        server_count: servers.len(),
        transport_counts,
        supported_execution_count,
        unsupported_execution_count,
        status_counts,
        unsupported_servers,
        attention_servers,
        servers,
    })
}

fn execute_web_fetch(input: &WebFetchInput) -> Result<WebFetchOutput, String> {
    let started = Instant::now();
    let client = build_http_client()?;
    let request_url = normalize_fetch_url(&input.url)?;
    let response = client
        .get(request_url.clone())
        .send()
        .map_err(|error| error.to_string())?;

    let status = response.status();
    let final_url = response.url().to_string();
    let code = status.as_u16();
    let code_text = status.canonical_reason().unwrap_or("Unknown").to_string();
    let content_type = response
        .headers()
        .get(reqwest::header::CONTENT_TYPE)
        .and_then(|value| value.to_str().ok())
        .unwrap_or_default()
        .to_string();
    let body = response.text().map_err(|error| error.to_string())?;
    let bytes = body.len();
    let normalized = normalize_fetched_content(&body, &content_type);
    let result = summarize_web_fetch(&final_url, &input.prompt, &normalized, &body, &content_type);

    Ok(WebFetchOutput {
        bytes,
        code,
        code_text,
        result,
        duration_ms: started.elapsed().as_millis(),
        url: final_url,
    })
}

fn execute_web_search(input: &WebSearchInput) -> Result<WebSearchOutput, String> {
    let started = Instant::now();
    let client = build_http_client()?;
    let search_url = build_search_url(&input.query)?;
    let response = client
        .get(search_url)
        .send()
        .map_err(|error| error.to_string())?;

    let final_url = response.url().clone();
    let html = response.text().map_err(|error| error.to_string())?;
    let mut hits = extract_search_hits(&html);

    if hits.is_empty() && final_url.host_str().is_some() {
        hits = extract_search_hits_from_generic_links(&html);
    }

    if let Some(allowed) = input.allowed_domains.as_ref() {
        hits.retain(|hit| host_matches_list(&hit.url, allowed));
    }
    if let Some(blocked) = input.blocked_domains.as_ref() {
        hits.retain(|hit| !host_matches_list(&hit.url, blocked));
    }

    dedupe_hits(&mut hits);
    hits.truncate(8);

    let summary = if hits.is_empty() {
        format!("No web search results matched the query {:?}.", input.query)
    } else {
        let rendered_hits = hits
            .iter()
            .map(|hit| format!("- [{}]({})", hit.title, hit.url))
            .collect::<Vec<_>>()
            .join("\n");
        format!(
            "Search results for {:?}. Include a Sources section in the final answer.\n{}",
            input.query, rendered_hits
        )
    };

    Ok(WebSearchOutput {
        query: input.query.clone(),
        results: vec![
            WebSearchResultItem::Commentary(summary),
            WebSearchResultItem::SearchResult {
                tool_use_id: String::from("web_search_1"),
                content: hits,
            },
        ],
        duration_seconds: started.elapsed().as_secs_f64(),
    })
}

fn build_http_client() -> Result<Client, String> {
    Client::builder()
        .timeout(Duration::from_secs(20))
        .redirect(reqwest::redirect::Policy::limited(10))
        .user_agent("clawd-rust-tools/0.1")
        .build()
        .map_err(|error| error.to_string())
}

fn normalize_fetch_url(url: &str) -> Result<String, String> {
    let parsed = reqwest::Url::parse(url).map_err(|error| error.to_string())?;
    if parsed.scheme() == "http" {
        let host = parsed.host_str().unwrap_or_default();
        if host != "localhost" && host != "127.0.0.1" && host != "::1" {
            let mut upgraded = parsed;
            upgraded
                .set_scheme("https")
                .map_err(|()| String::from("failed to upgrade URL to https"))?;
            return Ok(upgraded.to_string());
        }
    }
    Ok(parsed.to_string())
}

fn build_search_url(query: &str) -> Result<reqwest::Url, String> {
    if let Ok(base) = std::env::var("CLAWD_WEB_SEARCH_BASE_URL") {
        let mut url = reqwest::Url::parse(&base).map_err(|error| error.to_string())?;
        url.query_pairs_mut().append_pair("q", query);
        return Ok(url);
    }

    let mut url = reqwest::Url::parse("https://html.duckduckgo.com/html/")
        .map_err(|error| error.to_string())?;
    url.query_pairs_mut().append_pair("q", query);
    Ok(url)
}

fn normalize_fetched_content(body: &str, content_type: &str) -> String {
    if content_type.contains("html") {
        html_to_text(body)
    } else {
        body.trim().to_string()
    }
}

fn summarize_web_fetch(
    url: &str,
    prompt: &str,
    content: &str,
    raw_body: &str,
    content_type: &str,
) -> String {
    let lower_prompt = prompt.to_lowercase();
    let compact = collapse_whitespace(content);

    let detail = if lower_prompt.contains("title") {
        extract_title(content, raw_body, content_type).map_or_else(
            || preview_text(&compact, 600),
            |title| format!("Title: {title}"),
        )
    } else if lower_prompt.contains("summary") || lower_prompt.contains("summarize") {
        preview_text(&compact, 900)
    } else {
        let preview = preview_text(&compact, 900);
        format!("Prompt: {prompt}\nContent preview:\n{preview}")
    };

    format!("Fetched {url}\n{detail}")
}

fn extract_title(content: &str, raw_body: &str, content_type: &str) -> Option<String> {
    if content_type.contains("html") {
        let lowered = raw_body.to_lowercase();
        if let Some(start) = lowered.find("<title>") {
            let after = start + "<title>".len();
            if let Some(end_rel) = lowered[after..].find("</title>") {
                let title =
                    collapse_whitespace(&decode_html_entities(&raw_body[after..after + end_rel]));
                if !title.is_empty() {
                    return Some(title);
                }
            }
        }
    }

    for line in content.lines() {
        let trimmed = line.trim();
        if !trimmed.is_empty() {
            return Some(trimmed.to_string());
        }
    }
    None
}

fn html_to_text(html: &str) -> String {
    let mut text = String::with_capacity(html.len());
    let mut in_tag = false;
    let mut previous_was_space = false;

    for ch in html.chars() {
        match ch {
            '<' => in_tag = true,
            '>' => in_tag = false,
            _ if in_tag => {}
            '&' => {
                text.push('&');
                previous_was_space = false;
            }
            ch if ch.is_whitespace() => {
                if !previous_was_space {
                    text.push(' ');
                    previous_was_space = true;
                }
            }
            _ => {
                text.push(ch);
                previous_was_space = false;
            }
        }
    }

    collapse_whitespace(&decode_html_entities(&text))
}

fn decode_html_entities(input: &str) -> String {
    input
        .replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", "\"")
        .replace("&#39;", "'")
        .replace("&nbsp;", " ")
}

fn collapse_whitespace(input: &str) -> String {
    input.split_whitespace().collect::<Vec<_>>().join(" ")
}

fn preview_text(input: &str, max_chars: usize) -> String {
    if input.chars().count() <= max_chars {
        return input.to_string();
    }
    let shortened = input.chars().take(max_chars).collect::<String>();
    format!("{}…", shortened.trim_end())
}

fn extract_search_hits(html: &str) -> Vec<SearchHit> {
    let mut hits = Vec::new();
    let mut remaining = html;

    while let Some(anchor_start) = remaining.find("result__a") {
        let after_class = &remaining[anchor_start..];
        let Some(href_idx) = after_class.find("href=") else {
            remaining = &after_class[1..];
            continue;
        };
        let href_slice = &after_class[href_idx + 5..];
        let Some((url, rest)) = extract_quoted_value(href_slice) else {
            remaining = &after_class[1..];
            continue;
        };
        let Some(close_tag_idx) = rest.find('>') else {
            remaining = &after_class[1..];
            continue;
        };
        let after_tag = &rest[close_tag_idx + 1..];
        let Some(end_anchor_idx) = after_tag.find("</a>") else {
            remaining = &after_tag[1..];
            continue;
        };
        let title = html_to_text(&after_tag[..end_anchor_idx]);
        if let Some(decoded_url) = decode_duckduckgo_redirect(&url) {
            hits.push(SearchHit {
                title: title.trim().to_string(),
                url: decoded_url,
            });
        }
        remaining = &after_tag[end_anchor_idx + 4..];
    }

    hits
}

fn extract_search_hits_from_generic_links(html: &str) -> Vec<SearchHit> {
    let mut hits = Vec::new();
    let mut remaining = html;

    while let Some(anchor_start) = remaining.find("<a") {
        let after_anchor = &remaining[anchor_start..];
        let Some(href_idx) = after_anchor.find("href=") else {
            remaining = &after_anchor[2..];
            continue;
        };
        let href_slice = &after_anchor[href_idx + 5..];
        let Some((url, rest)) = extract_quoted_value(href_slice) else {
            remaining = &after_anchor[2..];
            continue;
        };
        let Some(close_tag_idx) = rest.find('>') else {
            remaining = &after_anchor[2..];
            continue;
        };
        let after_tag = &rest[close_tag_idx + 1..];
        let Some(end_anchor_idx) = after_tag.find("</a>") else {
            remaining = &after_anchor[2..];
            continue;
        };
        let title = html_to_text(&after_tag[..end_anchor_idx]);
        if title.trim().is_empty() {
            remaining = &after_tag[end_anchor_idx + 4..];
            continue;
        }
        let decoded_url = decode_duckduckgo_redirect(&url).unwrap_or(url);
        if decoded_url.starts_with("http://") || decoded_url.starts_with("https://") {
            hits.push(SearchHit {
                title: title.trim().to_string(),
                url: decoded_url,
            });
        }
        remaining = &after_tag[end_anchor_idx + 4..];
    }

    hits
}

fn extract_quoted_value(input: &str) -> Option<(String, &str)> {
    let quote = input.chars().next()?;
    if quote != '"' && quote != '\'' {
        return None;
    }
    let rest = &input[quote.len_utf8()..];
    let end = rest.find(quote)?;
    Some((rest[..end].to_string(), &rest[end + quote.len_utf8()..]))
}

fn decode_duckduckgo_redirect(url: &str) -> Option<String> {
    if url.starts_with("http://") || url.starts_with("https://") {
        return Some(html_entity_decode_url(url));
    }

    let joined = if url.starts_with("//") {
        format!("https:{url}")
    } else if url.starts_with('/') {
        format!("https://duckduckgo.com{url}")
    } else {
        return None;
    };

    let parsed = reqwest::Url::parse(&joined).ok()?;
    if parsed.path() == "/l/" || parsed.path() == "/l" {
        for (key, value) in parsed.query_pairs() {
            if key == "uddg" {
                return Some(html_entity_decode_url(value.as_ref()));
            }
        }
    }
    Some(joined)
}

fn html_entity_decode_url(url: &str) -> String {
    decode_html_entities(url)
}

fn host_matches_list(url: &str, domains: &[String]) -> bool {
    let Ok(parsed) = reqwest::Url::parse(url) else {
        return false;
    };
    let Some(host) = parsed.host_str() else {
        return false;
    };
    let host = host.to_ascii_lowercase();
    domains.iter().any(|domain| {
        let normalized = normalize_domain_filter(domain);
        !normalized.is_empty() && (host == normalized || host.ends_with(&format!(".{normalized}")))
    })
}

fn normalize_domain_filter(domain: &str) -> String {
    let trimmed = domain.trim();
    let candidate = reqwest::Url::parse(trimmed)
        .ok()
        .and_then(|url| url.host_str().map(str::to_string))
        .unwrap_or_else(|| trimmed.to_string());
    candidate
        .trim()
        .trim_start_matches('.')
        .trim_end_matches('/')
        .to_ascii_lowercase()
}

fn dedupe_hits(hits: &mut Vec<SearchHit>) {
    let mut seen = BTreeSet::new();
    hits.retain(|hit| seen.insert(hit.url.clone()));
}

fn execute_todo_write(input: TodoWriteInput) -> Result<TodoWriteOutput, String> {
    validate_todos(&input.todos)?;
    let store_path = todo_store_path()?;
    let old_todos = if store_path.exists() {
        serde_json::from_str::<Vec<TodoItem>>(
            &std::fs::read_to_string(&store_path).map_err(|error| error.to_string())?,
        )
        .map_err(|error| error.to_string())?
    } else {
        Vec::new()
    };

    let all_done = input
        .todos
        .iter()
        .all(|todo| matches!(todo.status, TodoStatus::Completed));
    let persisted = if all_done {
        Vec::new()
    } else {
        input.todos.clone()
    };

    if let Some(parent) = store_path.parent() {
        std::fs::create_dir_all(parent).map_err(|error| error.to_string())?;
    }
    std::fs::write(
        &store_path,
        serde_json::to_string_pretty(&persisted).map_err(|error| error.to_string())?,
    )
    .map_err(|error| error.to_string())?;

    let verification_nudge_needed = (all_done
        && input.todos.len() >= 3
        && !input
            .todos
            .iter()
            .any(|todo| todo.content.to_lowercase().contains("verif")))
    .then_some(true);

    Ok(TodoWriteOutput {
        old_todos,
        new_todos: input.todos,
        verification_nudge_needed,
    })
}

pub fn list_skills() -> Vec<SkillSummary> {
    let mut skills = BTreeMap::<String, SkillSummary>::new();

    for skill in list_repo_skill_records() {
        let key = skill.name.to_ascii_lowercase();
        if skills.contains_key(&key) {
            continue;
        }

        skills.insert(
            key,
            SkillSummary {
                name: skill.name,
                path: skill.path.display().to_string(),
                description: skill.description,
            },
        );
    }

    for root in skill_roots() {
        let Ok(entries) = std::fs::read_dir(&root) else {
            continue;
        };

        for entry in entries.flatten() {
            let path = entry.path().join("SKILL.md");
            if !path.exists() {
                continue;
            }

            let name = entry.file_name().to_string_lossy().to_string();
            let key = name.to_ascii_lowercase();
            if skills.contains_key(&key) {
                continue;
            }

            let description = std::fs::read_to_string(&path)
                .ok()
                .and_then(|prompt| parse_skill_description(&prompt));

            skills.insert(
                key,
                SkillSummary {
                    name,
                    path: path.display().to_string(),
                    description,
                },
            );
        }
    }

    skills.into_values().collect()
}

pub fn load_skill(skill: &str, args: Option<String>) -> Result<LoadedSkill, String> {
    if let Some(skill) = find_repo_skill(skill) {
        return Ok(LoadedSkill {
            skill: skill.name,
            path: skill.path.display().to_string(),
            args,
            description: skill.description,
            prompt: skill.prompt,
        });
    }

    let skill_path = resolve_skill_path(skill)?;
    let prompt = std::fs::read_to_string(&skill_path).map_err(|error| error.to_string())?;
    let description = parse_skill_description(&prompt);

    Ok(LoadedSkill {
        skill: skill.to_string(),
        path: skill_path.display().to_string(),
        args,
        description,
        prompt,
    })
}

pub fn list_agent_tasks() -> Result<Vec<AgentTaskSummary>, String> {
    let store_dir = agent_store_dir()?;
    if !store_dir.exists() {
        return Ok(Vec::new());
    }

    let mut tasks = std::fs::read_dir(&store_dir)
        .map_err(|error| error.to_string())?
        .filter_map(Result::ok)
        .map(|entry| entry.path())
        .filter(|path| path.extension().and_then(|ext| ext.to_str()) == Some("json"))
        .filter_map(|path| {
            let contents = std::fs::read_to_string(&path).ok()?;
            serde_json::from_str::<AgentTaskSummary>(&contents).ok()
        })
        .collect::<Vec<_>>();

    tasks.sort_by(|left, right| {
        right
            .created_at
            .cmp(&left.created_at)
            .then_with(|| left.agent_id.cmp(&right.agent_id))
    });
    Ok(tasks)
}

pub fn load_agent_task(task: &str) -> Result<LoadedAgentTask, String> {
    let requested = task.trim();
    if requested.is_empty() {
        return Err(String::from("task id must not be empty"));
    }

    let tasks = list_agent_tasks()?;
    let exact = tasks
        .iter()
        .filter(|entry| {
            entry.agent_id.eq_ignore_ascii_case(requested)
                || entry.name.eq_ignore_ascii_case(requested)
        })
        .cloned()
        .collect::<Vec<_>>();

    let task = if let [task] = exact.as_slice() {
        task.clone()
    } else if exact.len() > 1 {
        return Err(format!(
            "multiple tasks matched '{requested}'; use a full agent id"
        ));
    } else {
        let partial = tasks
            .iter()
            .filter(|entry| entry.agent_id.starts_with(requested))
            .cloned()
            .collect::<Vec<_>>();
        match partial.as_slice() {
            [task] => task.clone(),
            [] => return Err(format!("unknown task: {requested}")),
            _ => {
                return Err(format!(
                    "multiple tasks matched '{requested}'; use a longer agent id"
                ))
            }
        }
    };

    let output = std::fs::read_to_string(&task.output_file).ok();
    Ok(LoadedAgentTask { task, output })
}

pub fn list_agent_profiles() -> Vec<AgentProfileSummary> {
    AGENT_PROFILE_SPECS
        .iter()
        .map(|spec| AgentProfileSummary {
            name: spec.name.to_string(),
            description: spec.description.to_string(),
            aliases: spec
                .aliases
                .iter()
                .map(|alias| (*alias).to_string())
                .collect(),
            tool_count: allowed_tools_for_subagent(spec.name).len(),
        })
        .collect()
}

pub fn load_agent_profile(agent: &str) -> Result<LoadedAgentProfile, String> {
    let spec = resolve_agent_profile_spec(agent)
        .ok_or_else(|| format!("unknown agent profile: {}", agent.trim()))?;
    let mut tools = allowed_tools_for_subagent(spec.name)
        .into_iter()
        .collect::<Vec<_>>();
    tools.sort();

    Ok(LoadedAgentProfile {
        name: spec.name.to_string(),
        description: spec.description.to_string(),
        aliases: spec
            .aliases
            .iter()
            .map(|alias| (*alias).to_string())
            .collect(),
        tools,
    })
}

fn resolve_agent_profile_spec(agent: &str) -> Option<&'static AgentProfileSpec> {
    let requested = agent.trim();
    if requested.is_empty() {
        return None;
    }

    let canonical = canonical_tool_token(requested);
    AGENT_PROFILE_SPECS.iter().find(|spec| {
        canonical_tool_token(spec.name) == canonical
            || spec
                .aliases
                .iter()
                .any(|alias| canonical_tool_token(alias) == canonical)
    })
}

fn execute_skill(input: SkillInput) -> Result<SkillOutput, String> {
    let skill = load_skill(&input.skill, input.args)?;

    Ok(SkillOutput {
        skill: skill.skill,
        path: skill.path,
        args: skill.args,
        description: skill.description,
        prompt: skill.prompt,
    })
}

fn validate_todos(todos: &[TodoItem]) -> Result<(), String> {
    if todos.is_empty() {
        return Err(String::from("todos must not be empty"));
    }
    // Allow multiple in_progress items for parallel workflows
    if todos.iter().any(|todo| todo.content.trim().is_empty()) {
        return Err(String::from("todo content must not be empty"));
    }
    if todos.iter().any(|todo| todo.active_form.trim().is_empty()) {
        return Err(String::from("todo activeForm must not be empty"));
    }
    Ok(())
}

fn todo_store_path() -> Result<std::path::PathBuf, String> {
    if let Ok(path) = std::env::var("CLAWD_TODO_STORE") {
        return Ok(std::path::PathBuf::from(path));
    }
    let cwd = std::env::current_dir().map_err(|error| error.to_string())?;
    Ok(cwd.join(".clawd-todos.json"))
}

fn list_repo_skill_records() -> Vec<RepoSkillRecord> {
    let mut skills = BTreeMap::<String, RepoSkillRecord>::new();

    for root in repo_skill_roots() {
        let mut files = Vec::new();
        collect_markdown_files(&root, &mut files);
        files.sort();

        for path in files {
            let Ok(skill) = parse_repo_skill_file(&path) else {
                continue;
            };

            let key = skill.name.to_ascii_lowercase();
            skills.entry(key).or_insert(skill);
        }
    }

    skills.into_values().collect()
}

fn find_repo_skill(skill: &str) -> Option<RepoSkillRecord> {
    let requested = requested_skill_name(skill).ok()?;
    let normalized = normalize_skill_lookup_token(&requested);

    list_repo_skill_records().into_iter().find(|entry| {
        normalize_skill_lookup_token(&entry.name) == normalized
            || entry
                .aliases
                .iter()
                .any(|alias| normalize_skill_lookup_token(alias) == normalized)
    })
}

fn repo_skill_roots() -> Vec<PathBuf> {
    let Ok(cwd) = std::env::current_dir() else {
        return Vec::new();
    };

    let mut roots = Vec::new();
    for ancestor in cwd.ancestors() {
        let candidate = ancestor.join("skills");
        if candidate.is_dir() && !roots.iter().any(|root| root == &candidate) {
            roots.push(candidate);
        }
    }

    roots
}

fn collect_markdown_files(root: &Path, files: &mut Vec<PathBuf>) {
    let Ok(entries) = std::fs::read_dir(root) else {
        return;
    };

    let mut children = entries
        .flatten()
        .map(|entry| entry.path())
        .collect::<Vec<_>>();
    children.sort();

    for child in children {
        let name = child
            .file_name()
            .and_then(|value| value.to_str())
            .unwrap_or("");
        if name.starts_with('.') {
            continue;
        }

        if child.is_dir() {
            collect_markdown_files(&child, files);
            continue;
        }

        if child
            .extension()
            .and_then(|value| value.to_str())
            .is_some_and(|value| value.eq_ignore_ascii_case("md"))
        {
            files.push(child);
        }
    }
}

fn parse_repo_skill_file(path: &Path) -> Result<RepoSkillRecord, String> {
    let contents = std::fs::read_to_string(path).map_err(|error| error.to_string())?;
    let Some((frontmatter, prompt)) = split_yaml_frontmatter(&contents) else {
        return Err(format!(
            "repo skill file must use YAML frontmatter: {}",
            path.display()
        ));
    };

    let yaml = serde_yaml::from_str::<YamlValue>(&frontmatter).map_err(|error| {
        format!(
            "could not parse repo skill frontmatter '{}': {error}",
            path.display()
        )
    })?;
    let mapping = yaml.as_mapping().ok_or_else(|| {
        format!(
            "repo skill frontmatter must be a mapping: {}",
            path.display()
        )
    })?;

    let name = yaml_required_string(mapping, "id", path)?;
    let aliases = yaml_string_list(mapping, "aliases");
    let description = yaml_optional_string(mapping, "summary");

    Ok(RepoSkillRecord {
        name: name.to_ascii_lowercase(),
        path: path.to_path_buf(),
        description,
        aliases,
        prompt,
    })
}

fn split_yaml_frontmatter(contents: &str) -> Option<(String, String)> {
    let lines = contents.lines().collect::<Vec<_>>();
    if lines.first().is_none_or(|line| line.trim() != "---") {
        return None;
    }

    let closing_index = lines
        .iter()
        .enumerate()
        .skip(1)
        .find_map(|(index, line)| (line.trim() == "---").then_some(index))?;

    let prompt = lines[closing_index + 1..].join("\n").trim().to_string();
    if prompt.is_empty() {
        return None;
    }

    Some((lines[1..closing_index].join("\n"), prompt))
}

fn yaml_optional_string(mapping: &YamlMapping, key: &str) -> Option<String> {
    mapping
        .get(&YamlValue::String(key.to_string()))
        .and_then(YamlValue::as_str)
        .map(str::trim)
        .filter(|value| !value.is_empty())
        .map(ToOwned::to_owned)
}

fn yaml_required_string(mapping: &YamlMapping, key: &str, path: &Path) -> Result<String, String> {
    yaml_optional_string(mapping, key).ok_or_else(|| {
        format!(
            "repo skill frontmatter '{}' must contain a non-empty {}",
            path.display(),
            key
        )
    })
}

fn yaml_string_list(mapping: &YamlMapping, key: &str) -> Vec<String> {
    mapping
        .get(&YamlValue::String(key.to_string()))
        .and_then(YamlValue::as_sequence)
        .into_iter()
        .flatten()
        .filter_map(YamlValue::as_str)
        .map(str::trim)
        .filter(|value| !value.is_empty())
        .map(ToOwned::to_owned)
        .collect()
}

fn normalize_skill_lookup_token(value: &str) -> String {
    value
        .trim()
        .to_ascii_lowercase()
        .replace(['_', '-'], " ")
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ")
}

fn requested_skill_name(skill: &str) -> Result<String, String> {
    let requested = skill
        .trim()
        .trim_start_matches('/')
        .trim_start_matches('$')
        .trim();
    if requested.is_empty() {
        return Err(String::from("skill must not be empty"));
    }
    Ok(requested.to_string())
}

fn skill_roots() -> Vec<std::path::PathBuf> {
    let mut roots = Vec::new();
    if let Ok(codex_home) = std::env::var("CODEX_HOME") {
        roots.push(std::path::PathBuf::from(codex_home).join("skills"));
    }

    let fallback = std::path::PathBuf::from("/home/bellman/.codex/skills");
    if !roots.iter().any(|root| root == &fallback) {
        roots.push(fallback);
    }

    roots
}

fn resolve_skill_path(skill: &str) -> Result<std::path::PathBuf, String> {
    let requested = requested_skill_name(skill)?;

    for root in skill_roots() {
        let direct = root.join(&requested).join("SKILL.md");
        if direct.exists() {
            return Ok(direct);
        }

        if let Ok(entries) = std::fs::read_dir(&root) {
            for entry in entries.flatten() {
                let path = entry.path().join("SKILL.md");
                if !path.exists() {
                    continue;
                }
                if entry
                    .file_name()
                    .to_string_lossy()
                    .eq_ignore_ascii_case(&requested)
                {
                    return Ok(path);
                }
            }
        }
    }

    Err(format!("unknown skill: {requested}"))
}

const DEFAULT_AGENT_MODEL: &str = "simcoe-opus-4-6";
const DEFAULT_AGENT_SYSTEM_DATE: &str = "2026-03-31";
const DEFAULT_AGENT_MAX_ITERATIONS: usize = 32;

fn execute_agent(input: AgentInput) -> Result<AgentOutput, String> {
    execute_agent_with_spawn(input, spawn_agent_job)
}

fn execute_agent_with_spawn<F>(input: AgentInput, spawn_fn: F) -> Result<AgentOutput, String>
where
    F: FnOnce(AgentJob) -> Result<(), String>,
{
    if input.description.trim().is_empty() {
        return Err(String::from("description must not be empty"));
    }
    if input.prompt.trim().is_empty() {
        return Err(String::from("prompt must not be empty"));
    }

    let agent_id = make_agent_id();
    let output_dir = agent_store_dir()?;
    std::fs::create_dir_all(&output_dir).map_err(|error| error.to_string())?;
    let output_file = output_dir.join(format!("{agent_id}.md"));
    let manifest_file = output_dir.join(format!("{agent_id}.json"));
    let normalized_subagent_type = normalize_subagent_type(input.subagent_type.as_deref());
    let model = resolve_agent_model(input.model.as_deref());
    let agent_name = input
        .name
        .as_deref()
        .map(slugify_agent_name)
        .filter(|name| !name.is_empty())
        .unwrap_or_else(|| slugify_agent_name(&input.description));
    let created_at = iso8601_now();
    let system_prompt = build_agent_system_prompt(&normalized_subagent_type)?;
    let allowed_tools = allowed_tools_for_subagent(&normalized_subagent_type);

    let output_contents = format!(
        "# Agent Task

- id: {}
- name: {}
- description: {}
- subagent_type: {}
- created_at: {}

## Prompt

{}
",
        agent_id, agent_name, input.description, normalized_subagent_type, created_at, input.prompt
    );
    std::fs::write(&output_file, output_contents).map_err(|error| error.to_string())?;

    let manifest = AgentOutput {
        agent_id,
        name: agent_name,
        description: input.description,
        subagent_type: Some(normalized_subagent_type),
        model: Some(model),
        status: String::from("running"),
        output_file: output_file.display().to_string(),
        manifest_file: manifest_file.display().to_string(),
        created_at: created_at.clone(),
        started_at: Some(created_at),
        completed_at: None,
        error: None,
    };
    write_agent_manifest(&manifest)?;

    let manifest_for_spawn = manifest.clone();
    let job = AgentJob {
        manifest: manifest_for_spawn,
        prompt: input.prompt,
        system_prompt,
        allowed_tools,
    };
    if let Err(error) = spawn_fn(job) {
        let error = format!("failed to spawn sub-agent: {error}");
        persist_agent_terminal_state(&manifest, "failed", None, Some(error.clone()))?;
        return Err(error);
    }

    Ok(manifest)
}

fn spawn_agent_job(job: AgentJob) -> Result<(), String> {
    let thread_name = format!("clawd-agent-{}", job.manifest.agent_id);
    std::thread::Builder::new()
        .name(thread_name)
        .spawn(move || {
            let result =
                std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| run_agent_job(&job)));
            match result {
                Ok(Ok(())) => {}
                Ok(Err(error)) => {
                    let _ =
                        persist_agent_terminal_state(&job.manifest, "failed", None, Some(error));
                }
                Err(_) => {
                    let _ = persist_agent_terminal_state(
                        &job.manifest,
                        "failed",
                        None,
                        Some(String::from("sub-agent thread panicked")),
                    );
                }
            }
        })
        .map(|_| ())
        .map_err(|error| error.to_string())
}

fn run_agent_job(job: &AgentJob) -> Result<(), String> {
    let mut runtime = build_agent_runtime(job)?.with_max_iterations(DEFAULT_AGENT_MAX_ITERATIONS);
    let summary = runtime
        .run_turn(job.prompt.clone(), None)
        .map_err(|error| error.to_string())?;
    let final_text = final_assistant_text(&summary);
    persist_agent_terminal_state(&job.manifest, "completed", Some(final_text.as_str()), None)
}

fn build_agent_runtime(
    job: &AgentJob,
) -> Result<ConversationRuntime<SimcoeRuntimeClient, SubagentToolExecutor>, String> {
    let model = job
        .manifest
        .model
        .clone()
        .unwrap_or_else(|| DEFAULT_AGENT_MODEL.to_string());
    let allowed_tools = job.allowed_tools.clone();
    let api_client = SimcoeRuntimeClient::new(model, allowed_tools.clone())?;
    let tool_executor = SubagentToolExecutor::new(allowed_tools);
    Ok(ConversationRuntime::new(
        Session::new(),
        api_client,
        tool_executor,
        agent_permission_policy(),
        job.system_prompt.clone(),
    ))
}

fn build_agent_system_prompt(subagent_type: &str) -> Result<Vec<String>, String> {
    let cwd = std::env::current_dir().map_err(|error| error.to_string())?;
    let mut prompt = load_system_prompt(
        cwd,
        DEFAULT_AGENT_SYSTEM_DATE.to_string(),
        std::env::consts::OS,
        "unknown",
    )
    .map_err(|error| error.to_string())?;
    prompt.push(format!(
        "You are a background sub-agent of type `{subagent_type}`. Work only on the delegated task, use only the tools available to you, do not ask the user questions, and finish with a concise result."
    ));
    Ok(prompt)
}

fn resolve_agent_model(model: Option<&str>) -> String {
    model
        .map(str::trim)
        .filter(|model| !model.is_empty())
        .unwrap_or(DEFAULT_AGENT_MODEL)
        .to_string()
}

fn allowed_tools_for_subagent(subagent_type: &str) -> BTreeSet<String> {
    let tools = match subagent_type {
        "Explore" => vec![
            "read_file",
            "glob_search",
            "grep_search",
            "ListMcpResourcesTool",
            "ReadMcpResourceTool",
            "McpAuthTool",
            "WebFetch",
            "WebSearch",
            "ToolSearch",
            "Skill",
            "StructuredOutput",
        ],
        "Plan" => vec![
            "read_file",
            "glob_search",
            "grep_search",
            "ListMcpResourcesTool",
            "ReadMcpResourceTool",
            "McpAuthTool",
            "WebFetch",
            "WebSearch",
            "ToolSearch",
            "Skill",
            "TodoWrite",
            "StructuredOutput",
            "SendUserMessage",
        ],
        "Verification" => vec![
            "bash",
            "read_file",
            "glob_search",
            "grep_search",
            "ListMcpResourcesTool",
            "ReadMcpResourceTool",
            "MCPTool",
            "McpAuthTool",
            "WebFetch",
            "WebSearch",
            "ToolSearch",
            "TodoWrite",
            "StructuredOutput",
            "SendUserMessage",
            "PowerShell",
        ],
        "simcoe-ai-guide" => vec![
            "read_file",
            "glob_search",
            "grep_search",
            "WebFetch",
            "WebSearch",
            "ToolSearch",
            "Skill",
            "StructuredOutput",
            "SendUserMessage",
        ],
        "statusline-setup" => vec![
            "bash",
            "read_file",
            "write_file",
            "edit_file",
            "glob_search",
            "grep_search",
            "ToolSearch",
        ],
        _ => vec![
            "bash",
            "read_file",
            "write_file",
            "edit_file",
            "glob_search",
            "grep_search",
            "ListMcpResourcesTool",
            "ReadMcpResourceTool",
            "MCPTool",
            "McpAuthTool",
            "WebFetch",
            "WebSearch",
            "TodoWrite",
            "Skill",
            "ToolSearch",
            "NotebookEdit",
            "Sleep",
            "SendUserMessage",
            "Config",
            "StructuredOutput",
            "REPL",
            "PowerShell",
        ],
    };
    tools.into_iter().map(str::to_string).collect()
}

fn agent_permission_policy() -> PermissionPolicy {
    mvp_tool_specs().into_iter().fold(
        PermissionPolicy::new(PermissionMode::DangerFullAccess),
        |policy, spec| policy.with_tool_requirement(spec.name, spec.required_permission),
    )
}

fn write_agent_manifest(manifest: &AgentOutput) -> Result<(), String> {
    std::fs::write(
        &manifest.manifest_file,
        serde_json::to_string_pretty(manifest).map_err(|error| error.to_string())?,
    )
    .map_err(|error| error.to_string())
}

fn persist_agent_terminal_state(
    manifest: &AgentOutput,
    status: &str,
    result: Option<&str>,
    error: Option<String>,
) -> Result<(), String> {
    append_agent_output(
        &manifest.output_file,
        &format_agent_terminal_output(status, result, error.as_deref()),
    )?;
    let mut next_manifest = manifest.clone();
    next_manifest.status = status.to_string();
    next_manifest.completed_at = Some(iso8601_now());
    next_manifest.error = error;
    write_agent_manifest(&next_manifest)
}

fn append_agent_output(path: &str, suffix: &str) -> Result<(), String> {
    use std::io::Write as _;

    let mut file = std::fs::OpenOptions::new()
        .append(true)
        .open(path)
        .map_err(|error| error.to_string())?;
    file.write_all(suffix.as_bytes())
        .map_err(|error| error.to_string())
}

fn format_agent_terminal_output(status: &str, result: Option<&str>, error: Option<&str>) -> String {
    let mut sections = vec![format!("\n## Result\n\n- status: {status}\n")];
    if let Some(result) = result.filter(|value| !value.trim().is_empty()) {
        sections.push(format!("\n### Final response\n\n{}\n", result.trim()));
    }
    if let Some(error) = error.filter(|value| !value.trim().is_empty()) {
        sections.push(format!("\n### Error\n\n{}\n", error.trim()));
    }
    sections.join("")
}

struct SimcoeRuntimeClient {
    runtime: tokio::runtime::Runtime,
    client: SimcoeApiClient,
    model: String,
    allowed_tools: BTreeSet<String>,
}

impl SimcoeRuntimeClient {
    fn new(model: String, allowed_tools: BTreeSet<String>) -> Result<Self, String> {
        let client = SimcoeApiClient::from_env().map_err(|error| error.to_string())?;
        Ok(Self {
            runtime: tokio::runtime::Runtime::new().map_err(|error| error.to_string())?,
            client,
            model,
            allowed_tools,
        })
    }
}

impl ApiClient for SimcoeRuntimeClient {
    fn stream(&mut self, request: ApiRequest) -> Result<Vec<AssistantEvent>, RuntimeError> {
        let tools = runtime_tool_definitions(Some(&self.allowed_tools));
        let message_request = MessageRequest {
            model: self.model.clone(),
            max_tokens: 32_000,
            messages: convert_messages(&request.messages),
            system: (!request.system_prompt.is_empty()).then(|| request.system_prompt.join("\n\n")),
            tools: (!tools.is_empty()).then_some(tools),
            tool_choice: (!self.allowed_tools.is_empty()).then_some(ToolChoice::Auto),
            stream: true,
        };

        self.runtime.block_on(async {
            let mut stream = self
                .client
                .stream_message(&message_request)
                .await
                .map_err(|error| RuntimeError::new(error.to_string()))?;
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
                            push_output_block(block, &mut events, &mut pending_tool, true);
                        }
                    }
                    ApiStreamEvent::ContentBlockStart(start) => {
                        push_output_block(
                            start.content_block,
                            &mut events,
                            &mut pending_tool,
                            true,
                        );
                    }
                    ApiStreamEvent::ContentBlockDelta(delta) => match delta.delta {
                        ContentBlockDelta::TextDelta { text } => {
                            if !text.is_empty() {
                                events.push(AssistantEvent::TextDelta(text));
                            }
                        }
                        ContentBlockDelta::InputJsonDelta { partial_json } => {
                            if let Some((_, _, input)) = &mut pending_tool {
                                input.push_str(&partial_json);
                            }
                        }
                    },
                    ApiStreamEvent::ContentBlockStop(_) => {
                        if let Some((id, name, input)) = pending_tool.take() {
                            events.push(AssistantEvent::ToolUse { id, name, input });
                        }
                    }
                    ApiStreamEvent::MessageDelta(delta) => {
                        events.push(AssistantEvent::Usage(TokenUsage {
                            input_tokens: delta.usage.input_tokens,
                            output_tokens: delta.usage.output_tokens,
                            cache_creation_input_tokens: 0,
                            cache_read_input_tokens: 0,
                        }));
                    }
                    ApiStreamEvent::MessageStop(_) => {
                        saw_stop = true;
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
                return Ok(events);
            }

            let response = self
                .client
                .send_message(&MessageRequest {
                    stream: false,
                    ..message_request.clone()
                })
                .await
                .map_err(|error| RuntimeError::new(error.to_string()))?;
            Ok(response_to_events(response))
        })
    }
}

struct SubagentToolExecutor {
    allowed_tools: BTreeSet<String>,
}

impl SubagentToolExecutor {
    fn new(allowed_tools: BTreeSet<String>) -> Self {
        Self { allowed_tools }
    }
}

impl ToolExecutor for SubagentToolExecutor {
    fn execute(&mut self, tool_name: &str, input: &str) -> Result<String, ToolError> {
        if !tool_name_is_allowed(&self.allowed_tools, tool_name) {
            return Err(ToolError::new(format!(
                "tool `{tool_name}` is not enabled for this sub-agent"
            )));
        }
        let value = serde_json::from_str(input)
            .map_err(|error| ToolError::new(format!("invalid tool input JSON: {error}")))?;
        execute_tool(tool_name, &value).map_err(ToolError::new)
    }
}

fn is_dynamic_mcp_tool_name(name: &str) -> bool {
    name.starts_with("mcp__")
}

pub fn tool_name_is_allowed(allowed_tools: &BTreeSet<String>, tool_name: &str) -> bool {
    allowed_tools.contains(tool_name)
        || (is_dynamic_mcp_tool_name(tool_name) && allowed_tools.contains("MCPTool"))
}

fn tool_specs_for_allowed_tools(allowed_tools: Option<&BTreeSet<String>>) -> Vec<ToolSpec> {
    mvp_tool_specs()
        .into_iter()
        .filter(|spec| allowed_tools.is_none_or(|allowed| allowed.contains(spec.name)))
        .collect()
}

pub fn runtime_tool_definitions(allowed_tools: Option<&BTreeSet<String>>) -> Vec<ToolDefinition> {
    let mut definitions = tool_specs_for_allowed_tools(allowed_tools)
        .into_iter()
        .map(|spec| ToolDefinition {
            name: spec.name.to_string(),
            description: Some(spec.description.to_string()),
            input_schema: spec.input_schema,
        })
        .collect::<Vec<_>>();
    definitions.extend(dynamic_mcp_tool_definitions(allowed_tools));
    definitions
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

fn push_output_block(
    block: OutputContentBlock,
    events: &mut Vec<AssistantEvent>,
    pending_tool: &mut Option<(String, String, String)>,
    streaming_tool_input: bool,
) {
    match block {
        OutputContentBlock::Text { text } => {
            if !text.is_empty() {
                events.push(AssistantEvent::TextDelta(text));
            }
        }
        OutputContentBlock::ToolUse { id, name, input } => {
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
}

fn response_to_events(response: MessageResponse) -> Vec<AssistantEvent> {
    let mut events = Vec::new();
    let mut pending_tool = None;

    for block in response.content {
        push_output_block(block, &mut events, &mut pending_tool, false);
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
    events
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

#[allow(clippy::needless_pass_by_value)]
fn execute_tool_search(input: ToolSearchInput) -> ToolSearchOutput {
    let deferred = deferred_tool_specs();
    let max_results = input.max_results.unwrap_or(5).max(1);
    let query = input.query.trim().to_string();
    let normalized_query = normalize_tool_search_query(&query);
    let catalog = dynamic_mcp_catalog(None);
    let mut matches = search_tool_specs(&query, max_results, &deferred);
    for name in search_dynamic_mcp_tools(&query, max_results, &catalog) {
        if matches.len() >= max_results {
            break;
        }
        if !matches.contains(&name) {
            matches.push(name);
        }
    }

    ToolSearchOutput {
        matches,
        query,
        normalized_query,
        total_deferred_tools: deferred.len() + catalog.tools.len(),
        pending_mcp_servers: (!catalog.pending_servers.is_empty())
            .then_some(catalog.pending_servers),
    }
}

fn deferred_tool_specs() -> Vec<ToolSpec> {
    mvp_tool_specs()
        .into_iter()
        .filter(|spec| {
            !matches!(
                spec.name,
                "bash" | "read_file" | "write_file" | "edit_file" | "glob_search" | "grep_search"
            )
        })
        .collect()
}

fn search_tool_specs(query: &str, max_results: usize, specs: &[ToolSpec]) -> Vec<String> {
    let lowered = query.to_lowercase();
    if let Some(selection) = lowered.strip_prefix("select:") {
        return selection
            .split(',')
            .map(str::trim)
            .filter(|part| !part.is_empty())
            .filter_map(|wanted| {
                let wanted = canonical_tool_token(wanted);
                specs
                    .iter()
                    .find(|spec| canonical_tool_token(spec.name) == wanted)
                    .map(|spec| spec.name.to_string())
            })
            .take(max_results)
            .collect();
    }

    let mut required = Vec::new();
    let mut optional = Vec::new();
    for term in lowered.split_whitespace() {
        if let Some(rest) = term.strip_prefix('+') {
            if !rest.is_empty() {
                required.push(rest);
            }
        } else {
            optional.push(term);
        }
    }
    let terms = if required.is_empty() {
        optional.clone()
    } else {
        required.iter().chain(optional.iter()).copied().collect()
    };

    let mut scored = specs
        .iter()
        .filter_map(|spec| {
            let name = spec.name.to_lowercase();
            let canonical_name = canonical_tool_token(spec.name);
            let normalized_description = normalize_tool_search_query(spec.description);
            let haystack = format!(
                "{name} {} {canonical_name}",
                spec.description.to_lowercase()
            );
            let normalized_haystack = format!("{canonical_name} {normalized_description}");
            if required.iter().any(|term| !haystack.contains(term)) {
                return None;
            }

            let mut score = 0_i32;
            for term in &terms {
                let canonical_term = canonical_tool_token(term);
                if haystack.contains(term) {
                    score += 2;
                }
                if name == *term {
                    score += 8;
                }
                if name.contains(term) {
                    score += 4;
                }
                if canonical_name == canonical_term {
                    score += 12;
                }
                if normalized_haystack.contains(&canonical_term) {
                    score += 3;
                }
            }

            if score == 0 && !lowered.is_empty() {
                return None;
            }
            Some((score, spec.name.to_string()))
        })
        .collect::<Vec<_>>();

    scored.sort_by(|left, right| right.0.cmp(&left.0).then_with(|| left.1.cmp(&right.1)));
    scored
        .into_iter()
        .map(|(_, name)| name)
        .take(max_results)
        .collect()
}

fn search_dynamic_mcp_tools(
    query: &str,
    max_results: usize,
    catalog: &DynamicMcpCatalog,
) -> Vec<String> {
    let lowered = query.to_lowercase();
    if let Some(selection) = lowered.strip_prefix("select:") {
        return selection
            .split(',')
            .map(str::trim)
            .filter(|part| !part.is_empty())
            .filter_map(|wanted| {
                let wanted = canonical_tool_token(wanted);
                catalog
                    .tools
                    .iter()
                    .find(|tool| canonical_tool_token(&tool.qualified_name) == wanted)
                    .map(|tool| tool.qualified_name.clone())
            })
            .take(max_results)
            .collect();
    }

    let mut required = Vec::new();
    let mut optional = Vec::new();
    for term in lowered.split_whitespace() {
        if let Some(rest) = term.strip_prefix('+') {
            if !rest.is_empty() {
                required.push(rest);
            }
        } else {
            optional.push(term);
        }
    }
    let terms = if required.is_empty() {
        optional.clone()
    } else {
        required.iter().chain(optional.iter()).copied().collect()
    };

    let mut scored = catalog
        .tools
        .iter()
        .filter_map(|tool| {
            let name = tool.qualified_name.to_lowercase();
            let raw_name = tool.raw_name.to_lowercase();
            let server_name = tool.server_name.to_lowercase();
            let description = tool
                .tool
                .description
                .as_deref()
                .unwrap_or_default()
                .to_lowercase();
            let canonical_name = canonical_tool_token(&tool.qualified_name);
            let normalized_description =
                normalize_tool_search_query(tool.tool.description.as_deref().unwrap_or_default());
            let haystack =
                format!("{name} {raw_name} {server_name} {description} {canonical_name}");
            let normalized_haystack = format!(
                "{canonical_name} {} {}",
                canonical_tool_token(&tool.raw_name),
                normalized_description
            );
            if required.iter().any(|term| !haystack.contains(term)) {
                return None;
            }

            let mut score = 0_i32;
            for term in &terms {
                let canonical_term = canonical_tool_token(term);
                if haystack.contains(term) {
                    score += 2;
                }
                if name == *term {
                    score += 8;
                }
                if name.contains(term) || raw_name.contains(term) || server_name.contains(term) {
                    score += 4;
                }
                if canonical_name == canonical_term {
                    score += 12;
                }
                if normalized_haystack.contains(&canonical_term) {
                    score += 3;
                }
            }

            if score == 0 && !lowered.is_empty() {
                return None;
            }
            Some((score, tool.qualified_name.clone()))
        })
        .collect::<Vec<_>>();

    scored.sort_by(|left, right| right.0.cmp(&left.0).then_with(|| left.1.cmp(&right.1)));
    scored
        .into_iter()
        .map(|(_, name)| name)
        .take(max_results)
        .collect()
}

fn normalize_tool_search_query(query: &str) -> String {
    query
        .trim()
        .split(|ch: char| ch.is_whitespace() || ch == ',')
        .filter(|term| !term.is_empty())
        .map(canonical_tool_token)
        .collect::<Vec<_>>()
        .join(" ")
}

fn canonical_tool_token(value: &str) -> String {
    let mut canonical = value
        .chars()
        .filter(char::is_ascii_alphanumeric)
        .flat_map(char::to_lowercase)
        .collect::<String>();
    if let Some(stripped) = canonical.strip_suffix("tool") {
        canonical = stripped.to_string();
    }
    canonical
}

fn agent_store_dir() -> Result<std::path::PathBuf, String> {
    if let Ok(path) = std::env::var("CLAWD_AGENT_STORE") {
        return Ok(std::path::PathBuf::from(path));
    }
    let cwd = std::env::current_dir().map_err(|error| error.to_string())?;
    if let Some(workspace_root) = cwd.ancestors().nth(2) {
        return Ok(workspace_root.join(".clawd-agents"));
    }
    Ok(cwd.join(".clawd-agents"))
}

fn make_agent_id() -> String {
    let nanos = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap_or_default()
        .as_nanos();
    format!("agent-{nanos}")
}

fn slugify_agent_name(description: &str) -> String {
    let mut out = description
        .chars()
        .map(|ch| {
            if ch.is_ascii_alphanumeric() {
                ch.to_ascii_lowercase()
            } else {
                '-'
            }
        })
        .collect::<String>();
    while out.contains("--") {
        out = out.replace("--", "-");
    }
    out.trim_matches('-').chars().take(32).collect()
}

fn normalize_subagent_type(subagent_type: Option<&str>) -> String {
    let trimmed = subagent_type.map(str::trim).unwrap_or_default();
    if trimmed.is_empty() {
        return String::from("general-purpose");
    }

    match canonical_tool_token(trimmed).as_str() {
        "general" | "generalpurpose" | "generalpurposeagent" => String::from("general-purpose"),
        "explore" | "explorer" | "exploreagent" => String::from("Explore"),
        "plan" | "planagent" => String::from("Plan"),
        "verification" | "verificationagent" | "verify" | "verifier" => {
            String::from("Verification")
        }
        "simcoeaiguide"
        | "simcoeaiguideagent"
        | "claudecodeguide"
        | "claudecodeguideagent"
        | "guide" => String::from("simcoe-ai-guide"),
        "statusline" | "statuslinesetup" | "statuslinesetupagent" => {
            String::from("statusline-setup")
        }
        _ => trimmed.to_string(),
    }
}

fn iso8601_now() -> String {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap_or_default()
        .as_secs()
        .to_string()
}

#[allow(clippy::too_many_lines)]
fn execute_notebook_edit(input: NotebookEditInput) -> Result<NotebookEditOutput, String> {
    let path = std::path::PathBuf::from(&input.notebook_path);
    if path.extension().and_then(|ext| ext.to_str()) != Some("ipynb") {
        return Err(String::from(
            "File must be a Jupyter notebook (.ipynb file).",
        ));
    }

    let original_file = std::fs::read_to_string(&path).map_err(|error| error.to_string())?;
    let mut notebook: serde_json::Value =
        serde_json::from_str(&original_file).map_err(|error| error.to_string())?;
    let language = notebook
        .get("metadata")
        .and_then(|metadata| metadata.get("kernelspec"))
        .and_then(|kernelspec| kernelspec.get("language"))
        .and_then(serde_json::Value::as_str)
        .unwrap_or("python")
        .to_string();
    let cells = notebook
        .get_mut("cells")
        .and_then(serde_json::Value::as_array_mut)
        .ok_or_else(|| String::from("Notebook cells array not found"))?;

    let edit_mode = input.edit_mode.unwrap_or(NotebookEditMode::Replace);
    let target_index = match input.cell_id.as_deref() {
        Some(cell_id) => Some(resolve_cell_index(cells, Some(cell_id), edit_mode)?),
        None if matches!(
            edit_mode,
            NotebookEditMode::Replace | NotebookEditMode::Delete
        ) =>
        {
            Some(resolve_cell_index(cells, None, edit_mode)?)
        }
        None => None,
    };
    let resolved_cell_type = match edit_mode {
        NotebookEditMode::Delete => None,
        NotebookEditMode::Insert => Some(input.cell_type.unwrap_or(NotebookCellType::Code)),
        NotebookEditMode::Replace => Some(input.cell_type.unwrap_or_else(|| {
            target_index
                .and_then(|index| cells.get(index))
                .and_then(cell_kind)
                .unwrap_or(NotebookCellType::Code)
        })),
    };
    let new_source = require_notebook_source(input.new_source, edit_mode)?;

    let cell_id = match edit_mode {
        NotebookEditMode::Insert => {
            let resolved_cell_type = resolved_cell_type.expect("insert cell type");
            let new_id = make_cell_id(cells.len());
            let new_cell = build_notebook_cell(&new_id, resolved_cell_type, &new_source);
            let insert_at = target_index.map_or(cells.len(), |index| index + 1);
            cells.insert(insert_at, new_cell);
            cells
                .get(insert_at)
                .and_then(|cell| cell.get("id"))
                .and_then(serde_json::Value::as_str)
                .map(ToString::to_string)
        }
        NotebookEditMode::Delete => {
            let removed = cells.remove(target_index.expect("delete target index"));
            removed
                .get("id")
                .and_then(serde_json::Value::as_str)
                .map(ToString::to_string)
        }
        NotebookEditMode::Replace => {
            let resolved_cell_type = resolved_cell_type.expect("replace cell type");
            let cell = cells
                .get_mut(target_index.expect("replace target index"))
                .ok_or_else(|| String::from("Cell index out of range"))?;
            cell["source"] = serde_json::Value::Array(source_lines(&new_source));
            cell["cell_type"] = serde_json::Value::String(match resolved_cell_type {
                NotebookCellType::Code => String::from("code"),
                NotebookCellType::Markdown => String::from("markdown"),
            });
            match resolved_cell_type {
                NotebookCellType::Code => {
                    if !cell.get("outputs").is_some_and(serde_json::Value::is_array) {
                        cell["outputs"] = json!([]);
                    }
                    if cell.get("execution_count").is_none() {
                        cell["execution_count"] = serde_json::Value::Null;
                    }
                }
                NotebookCellType::Markdown => {
                    if let Some(object) = cell.as_object_mut() {
                        object.remove("outputs");
                        object.remove("execution_count");
                    }
                }
            }
            cell.get("id")
                .and_then(serde_json::Value::as_str)
                .map(ToString::to_string)
        }
    };

    let updated_file =
        serde_json::to_string_pretty(&notebook).map_err(|error| error.to_string())?;
    std::fs::write(&path, &updated_file).map_err(|error| error.to_string())?;

    Ok(NotebookEditOutput {
        new_source,
        cell_id,
        cell_type: resolved_cell_type,
        language,
        edit_mode: format_notebook_edit_mode(edit_mode),
        error: None,
        notebook_path: path.display().to_string(),
        original_file,
        updated_file,
    })
}

fn require_notebook_source(
    source: Option<String>,
    edit_mode: NotebookEditMode,
) -> Result<String, String> {
    match edit_mode {
        NotebookEditMode::Delete => Ok(source.unwrap_or_default()),
        NotebookEditMode::Insert | NotebookEditMode::Replace => source
            .ok_or_else(|| String::from("new_source is required for insert and replace edits")),
    }
}

fn build_notebook_cell(cell_id: &str, cell_type: NotebookCellType, source: &str) -> Value {
    let mut cell = json!({
        "cell_type": match cell_type {
            NotebookCellType::Code => "code",
            NotebookCellType::Markdown => "markdown",
        },
        "id": cell_id,
        "metadata": {},
        "source": source_lines(source),
    });
    if let Some(object) = cell.as_object_mut() {
        match cell_type {
            NotebookCellType::Code => {
                object.insert(String::from("outputs"), json!([]));
                object.insert(String::from("execution_count"), Value::Null);
            }
            NotebookCellType::Markdown => {}
        }
    }
    cell
}

fn cell_kind(cell: &serde_json::Value) -> Option<NotebookCellType> {
    cell.get("cell_type")
        .and_then(serde_json::Value::as_str)
        .map(|kind| {
            if kind == "markdown" {
                NotebookCellType::Markdown
            } else {
                NotebookCellType::Code
            }
        })
}

#[allow(clippy::needless_pass_by_value)]
fn execute_sleep(input: SleepInput) -> SleepOutput {
    std::thread::sleep(Duration::from_millis(input.duration_ms));
    SleepOutput {
        duration_ms: input.duration_ms,
        message: format!("Slept for {}ms", input.duration_ms),
    }
}

fn execute_brief(input: BriefInput) -> Result<BriefOutput, String> {
    if input.message.trim().is_empty() {
        return Err(String::from("message must not be empty"));
    }

    let attachments = input
        .attachments
        .as_ref()
        .map(|paths| {
            paths
                .iter()
                .map(|path| resolve_attachment(path))
                .collect::<Result<Vec<_>, String>>()
        })
        .transpose()?;

    let message = match input.status {
        BriefStatus::Normal | BriefStatus::Proactive => input.message,
    };

    Ok(BriefOutput {
        message,
        attachments,
        sent_at: iso8601_timestamp(),
    })
}

fn resolve_attachment(path: &str) -> Result<ResolvedAttachment, String> {
    let resolved = std::fs::canonicalize(path).map_err(|error| error.to_string())?;
    let metadata = std::fs::metadata(&resolved).map_err(|error| error.to_string())?;
    Ok(ResolvedAttachment {
        path: resolved.display().to_string(),
        size: metadata.len(),
        is_image: is_image_path(&resolved),
    })
}

fn is_image_path(path: &Path) -> bool {
    matches!(
        path.extension()
            .and_then(|ext| ext.to_str())
            .map(str::to_ascii_lowercase)
            .as_deref(),
        Some("png" | "jpg" | "jpeg" | "gif" | "webp" | "bmp" | "svg")
    )
}

fn execute_config(input: ConfigInput) -> Result<ConfigOutput, String> {
    let setting = input.setting.trim();
    if setting.is_empty() {
        return Err(String::from("setting must not be empty"));
    }
    let Some(spec) = supported_config_setting(setting) else {
        return Ok(ConfigOutput {
            success: false,
            operation: None,
            setting: None,
            value: None,
            previous_value: None,
            new_value: None,
            error: Some(format!("Unknown setting: \"{setting}\"")),
        });
    };

    let path = config_file_for_scope(spec.scope)?;
    let mut document = read_json_object(&path)?;

    if let Some(value) = input.value {
        let normalized = normalize_config_value(spec, value)?;
        let previous_value = get_nested_value(&document, spec.path).cloned();
        set_nested_value(&mut document, spec.path, normalized.clone());
        write_json_object(&path, &document)?;
        Ok(ConfigOutput {
            success: true,
            operation: Some(String::from("set")),
            setting: Some(setting.to_string()),
            value: Some(normalized.clone()),
            previous_value,
            new_value: Some(normalized),
            error: None,
        })
    } else {
        Ok(ConfigOutput {
            success: true,
            operation: Some(String::from("get")),
            setting: Some(setting.to_string()),
            value: get_nested_value(&document, spec.path).cloned(),
            previous_value: None,
            new_value: None,
            error: None,
        })
    }
}

fn execute_structured_output(input: StructuredOutputInput) -> StructuredOutputResult {
    StructuredOutputResult {
        data: String::from("Structured output provided successfully"),
        structured_output: input.0,
    }
}

fn execute_repl(input: ReplInput) -> Result<ReplOutput, String> {
    if input.code.trim().is_empty() {
        return Err(String::from("code must not be empty"));
    }
    let _ = input.timeout_ms;
    let runtime = resolve_repl_runtime(&input.language)?;
    let started = Instant::now();
    let output = Command::new(runtime.program)
        .args(runtime.args)
        .arg(&input.code)
        .output()
        .map_err(|error| error.to_string())?;

    Ok(ReplOutput {
        language: input.language,
        stdout: String::from_utf8_lossy(&output.stdout).into_owned(),
        stderr: String::from_utf8_lossy(&output.stderr).into_owned(),
        exit_code: output.status.code().unwrap_or(1),
        duration_ms: started.elapsed().as_millis(),
    })
}

struct ReplRuntime {
    program: &'static str,
    args: &'static [&'static str],
}

fn resolve_repl_runtime(language: &str) -> Result<ReplRuntime, String> {
    match language.trim().to_ascii_lowercase().as_str() {
        "python" | "py" => Ok(ReplRuntime {
            program: detect_first_command(&["python3", "python"])
                .ok_or_else(|| String::from("python runtime not found"))?,
            args: &["-c"],
        }),
        "javascript" | "js" | "node" => Ok(ReplRuntime {
            program: detect_first_command(&["node"])
                .ok_or_else(|| String::from("node runtime not found"))?,
            args: &["-e"],
        }),
        "sh" | "shell" | "bash" => Ok(ReplRuntime {
            program: detect_first_command(&["bash", "sh"])
                .ok_or_else(|| String::from("shell runtime not found"))?,
            args: &["-lc"],
        }),
        other => Err(format!("unsupported REPL language: {other}")),
    }
}

fn detect_first_command(commands: &[&'static str]) -> Option<&'static str> {
    commands
        .iter()
        .copied()
        .find(|command| command_exists(command))
}

#[derive(Clone, Copy)]
enum ConfigScope {
    Global,
    Settings,
}

#[derive(Clone, Copy)]
struct ConfigSettingSpec {
    scope: ConfigScope,
    kind: ConfigKind,
    path: &'static [&'static str],
    options: Option<&'static [&'static str]>,
}

#[derive(Clone, Copy)]
enum ConfigKind {
    Boolean,
    String,
}

fn supported_config_setting(setting: &str) -> Option<ConfigSettingSpec> {
    Some(match setting {
        "theme" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::String,
            path: &["theme"],
            options: None,
        },
        "editorMode" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::String,
            path: &["editorMode"],
            options: Some(&["default", "vim", "emacs"]),
        },
        "verbose" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::Boolean,
            path: &["verbose"],
            options: None,
        },
        "preferredNotifChannel" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::String,
            path: &["preferredNotifChannel"],
            options: None,
        },
        "autoCompactEnabled" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::Boolean,
            path: &["autoCompactEnabled"],
            options: None,
        },
        "autoMemoryEnabled" => ConfigSettingSpec {
            scope: ConfigScope::Settings,
            kind: ConfigKind::Boolean,
            path: &["autoMemoryEnabled"],
            options: None,
        },
        "autoDreamEnabled" => ConfigSettingSpec {
            scope: ConfigScope::Settings,
            kind: ConfigKind::Boolean,
            path: &["autoDreamEnabled"],
            options: None,
        },
        "fileCheckpointingEnabled" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::Boolean,
            path: &["fileCheckpointingEnabled"],
            options: None,
        },
        "showTurnDuration" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::Boolean,
            path: &["showTurnDuration"],
            options: None,
        },
        "terminalProgressBarEnabled" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::Boolean,
            path: &["terminalProgressBarEnabled"],
            options: None,
        },
        "todoFeatureEnabled" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::Boolean,
            path: &["todoFeatureEnabled"],
            options: None,
        },
        "model" => ConfigSettingSpec {
            scope: ConfigScope::Settings,
            kind: ConfigKind::String,
            path: &["model"],
            options: None,
        },
        "alwaysThinkingEnabled" => ConfigSettingSpec {
            scope: ConfigScope::Settings,
            kind: ConfigKind::Boolean,
            path: &["alwaysThinkingEnabled"],
            options: None,
        },
        "permissions.defaultMode" => ConfigSettingSpec {
            scope: ConfigScope::Settings,
            kind: ConfigKind::String,
            path: &["permissions", "defaultMode"],
            options: Some(&["default", "plan", "acceptEdits", "dontAsk", "auto"]),
        },
        "language" => ConfigSettingSpec {
            scope: ConfigScope::Settings,
            kind: ConfigKind::String,
            path: &["language"],
            options: None,
        },
        "teammateMode" => ConfigSettingSpec {
            scope: ConfigScope::Global,
            kind: ConfigKind::String,
            path: &["teammateMode"],
            options: Some(&["tmux", "in-process", "auto"]),
        },
        _ => return None,
    })
}

fn normalize_config_value(spec: ConfigSettingSpec, value: ConfigValue) -> Result<Value, String> {
    let normalized = match (spec.kind, value) {
        (ConfigKind::Boolean, ConfigValue::Bool(value)) => Value::Bool(value),
        (ConfigKind::Boolean, ConfigValue::String(value)) => {
            match value.trim().to_ascii_lowercase().as_str() {
                "true" => Value::Bool(true),
                "false" => Value::Bool(false),
                _ => return Err(String::from("setting requires true or false")),
            }
        }
        (ConfigKind::Boolean, ConfigValue::Number(_)) => {
            return Err(String::from("setting requires true or false"))
        }
        (ConfigKind::String, ConfigValue::String(value)) => Value::String(value),
        (ConfigKind::String, ConfigValue::Bool(value)) => Value::String(value.to_string()),
        (ConfigKind::String, ConfigValue::Number(value)) => json!(value),
    };

    if let Some(options) = spec.options {
        let Some(as_str) = normalized.as_str() else {
            return Err(String::from("setting requires a string value"));
        };
        if !options.iter().any(|option| option == &as_str) {
            return Err(format!(
                "Invalid value \"{as_str}\". Options: {}",
                options.join(", ")
            ));
        }
    }

    Ok(normalized)
}

fn config_file_for_scope(scope: ConfigScope) -> Result<PathBuf, String> {
    let cwd = std::env::current_dir().map_err(|error| error.to_string())?;
    Ok(match scope {
        ConfigScope::Global => config_home_dir()?.join("settings.json"),
        ConfigScope::Settings => cwd.join(".simcoe").join("settings.local.json"),
    })
}

fn config_home_dir() -> Result<PathBuf, String> {
    if let Ok(path) = std::env::var("SIMCOE_CONFIG_HOME") {
        return Ok(PathBuf::from(path));
    }
    let home = std::env::var("HOME").map_err(|_| String::from("HOME is not set"))?;
    Ok(PathBuf::from(home).join(".simcoe"))
}

fn read_json_object(path: &Path) -> Result<serde_json::Map<String, Value>, String> {
    match std::fs::read_to_string(path) {
        Ok(contents) => {
            if contents.trim().is_empty() {
                return Ok(serde_json::Map::new());
            }
            serde_json::from_str::<Value>(&contents)
                .map_err(|error| error.to_string())?
                .as_object()
                .cloned()
                .ok_or_else(|| String::from("config file must contain a JSON object"))
        }
        Err(error) if error.kind() == std::io::ErrorKind::NotFound => Ok(serde_json::Map::new()),
        Err(error) => Err(error.to_string()),
    }
}

fn write_json_object(path: &Path, value: &serde_json::Map<String, Value>) -> Result<(), String> {
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).map_err(|error| error.to_string())?;
    }
    std::fs::write(
        path,
        serde_json::to_string_pretty(value).map_err(|error| error.to_string())?,
    )
    .map_err(|error| error.to_string())
}

fn get_nested_value<'a>(
    value: &'a serde_json::Map<String, Value>,
    path: &[&str],
) -> Option<&'a Value> {
    let (first, rest) = path.split_first()?;
    let mut current = value.get(*first)?;
    for key in rest {
        current = current.as_object()?.get(*key)?;
    }
    Some(current)
}

fn set_nested_value(root: &mut serde_json::Map<String, Value>, path: &[&str], new_value: Value) {
    let (first, rest) = path.split_first().expect("config path must not be empty");
    if rest.is_empty() {
        root.insert((*first).to_string(), new_value);
        return;
    }

    let entry = root
        .entry((*first).to_string())
        .or_insert_with(|| Value::Object(serde_json::Map::new()));
    if !entry.is_object() {
        *entry = Value::Object(serde_json::Map::new());
    }
    let map = entry.as_object_mut().expect("object inserted");
    set_nested_value(map, rest, new_value);
}

fn iso8601_timestamp() -> String {
    if let Ok(output) = Command::new("date")
        .args(["-u", "+%Y-%m-%dT%H:%M:%SZ"])
        .output()
    {
        if output.status.success() {
            return String::from_utf8_lossy(&output.stdout).trim().to_string();
        }
    }
    iso8601_now()
}

#[allow(clippy::needless_pass_by_value)]
fn execute_powershell(input: PowerShellInput) -> std::io::Result<runtime::BashCommandOutput> {
    let _ = &input.description;
    let shell = detect_powershell_shell()?;
    execute_shell_command(
        shell,
        &input.command,
        input.timeout,
        input.run_in_background,
    )
}

fn detect_powershell_shell() -> std::io::Result<&'static str> {
    if command_exists("pwsh") {
        Ok("pwsh")
    } else if command_exists("powershell") {
        Ok("powershell")
    } else {
        Err(std::io::Error::new(
            std::io::ErrorKind::NotFound,
            "PowerShell executable not found (expected `pwsh` or `powershell` in PATH)",
        ))
    }
}

fn command_exists(command: &str) -> bool {
    std::process::Command::new("sh")
        .arg("-lc")
        .arg(format!("command -v {command} >/dev/null 2>&1"))
        .status()
        .map(|status| status.success())
        .unwrap_or(false)
}

#[allow(clippy::too_many_lines)]
fn execute_shell_command(
    shell: &str,
    command: &str,
    timeout: Option<u64>,
    run_in_background: Option<bool>,
) -> std::io::Result<runtime::BashCommandOutput> {
    if run_in_background.unwrap_or(false) {
        let child = std::process::Command::new(shell)
            .arg("-NoProfile")
            .arg("-NonInteractive")
            .arg("-Command")
            .arg(command)
            .stdin(std::process::Stdio::null())
            .stdout(std::process::Stdio::null())
            .stderr(std::process::Stdio::null())
            .spawn()?;
        return Ok(runtime::BashCommandOutput {
            stdout: String::new(),
            stderr: String::new(),
            raw_output_path: None,
            interrupted: false,
            is_image: None,
            background_task_id: Some(child.id().to_string()),
            backgrounded_by_user: Some(true),
            assistant_auto_backgrounded: Some(false),
            dangerously_disable_sandbox: None,
            return_code_interpretation: None,
            no_output_expected: Some(true),
            structured_content: None,
            persisted_output_path: None,
            persisted_output_size: None,
            sandbox_status: None,
        });
    }

    let mut process = std::process::Command::new(shell);
    process
        .arg("-NoProfile")
        .arg("-NonInteractive")
        .arg("-Command")
        .arg(command);
    process
        .stdout(std::process::Stdio::piped())
        .stderr(std::process::Stdio::piped());

    if let Some(timeout_ms) = timeout {
        let mut child = process.spawn()?;
        let started = Instant::now();
        loop {
            if let Some(status) = child.try_wait()? {
                let output = child.wait_with_output()?;
                return Ok(runtime::BashCommandOutput {
                    stdout: String::from_utf8_lossy(&output.stdout).into_owned(),
                    stderr: String::from_utf8_lossy(&output.stderr).into_owned(),
                    raw_output_path: None,
                    interrupted: false,
                    is_image: None,
                    background_task_id: None,
                    backgrounded_by_user: None,
                    assistant_auto_backgrounded: None,
                    dangerously_disable_sandbox: None,
                    return_code_interpretation: status
                        .code()
                        .filter(|code| *code != 0)
                        .map(|code| format!("exit_code:{code}")),
                    no_output_expected: Some(output.stdout.is_empty() && output.stderr.is_empty()),
                    structured_content: None,
                    persisted_output_path: None,
                    persisted_output_size: None,
                    sandbox_status: None,
                });
            }
            if started.elapsed() >= Duration::from_millis(timeout_ms) {
                let _ = child.kill();
                let output = child.wait_with_output()?;
                let stderr = String::from_utf8_lossy(&output.stderr).into_owned();
                let stderr = if stderr.trim().is_empty() {
                    format!("Command exceeded timeout of {timeout_ms} ms")
                } else {
                    format!(
                        "{}
Command exceeded timeout of {timeout_ms} ms",
                        stderr.trim_end()
                    )
                };
                return Ok(runtime::BashCommandOutput {
                    stdout: String::from_utf8_lossy(&output.stdout).into_owned(),
                    stderr,
                    raw_output_path: None,
                    interrupted: true,
                    is_image: None,
                    background_task_id: None,
                    backgrounded_by_user: None,
                    assistant_auto_backgrounded: None,
                    dangerously_disable_sandbox: None,
                    return_code_interpretation: Some(String::from("timeout")),
                    no_output_expected: Some(false),
                    structured_content: None,
                    persisted_output_path: None,
                    persisted_output_size: None,
                    sandbox_status: None,
                });
            }
            std::thread::sleep(Duration::from_millis(10));
        }
    }

    let output = process.output()?;
    Ok(runtime::BashCommandOutput {
        stdout: String::from_utf8_lossy(&output.stdout).into_owned(),
        stderr: String::from_utf8_lossy(&output.stderr).into_owned(),
        raw_output_path: None,
        interrupted: false,
        is_image: None,
        background_task_id: None,
        backgrounded_by_user: None,
        assistant_auto_backgrounded: None,
        dangerously_disable_sandbox: None,
        return_code_interpretation: output
            .status
            .code()
            .filter(|code| *code != 0)
            .map(|code| format!("exit_code:{code}")),
        no_output_expected: Some(output.stdout.is_empty() && output.stderr.is_empty()),
        structured_content: None,
        persisted_output_path: None,
        persisted_output_size: None,
        sandbox_status: None,
    })
}

fn resolve_cell_index(
    cells: &[serde_json::Value],
    cell_id: Option<&str>,
    edit_mode: NotebookEditMode,
) -> Result<usize, String> {
    if cells.is_empty()
        && matches!(
            edit_mode,
            NotebookEditMode::Replace | NotebookEditMode::Delete
        )
    {
        return Err(String::from("Notebook has no cells to edit"));
    }
    if let Some(cell_id) = cell_id {
        cells
            .iter()
            .position(|cell| cell.get("id").and_then(serde_json::Value::as_str) == Some(cell_id))
            .ok_or_else(|| format!("Cell id not found: {cell_id}"))
    } else {
        Ok(cells.len().saturating_sub(1))
    }
}

fn source_lines(source: &str) -> Vec<serde_json::Value> {
    if source.is_empty() {
        return vec![serde_json::Value::String(String::new())];
    }
    source
        .split_inclusive('\n')
        .map(|line| serde_json::Value::String(line.to_string()))
        .collect()
}

fn format_notebook_edit_mode(mode: NotebookEditMode) -> String {
    match mode {
        NotebookEditMode::Replace => String::from("replace"),
        NotebookEditMode::Insert => String::from("insert"),
        NotebookEditMode::Delete => String::from("delete"),
    }
}

fn make_cell_id(index: usize) -> String {
    format!("cell-{}", index + 1)
}

fn parse_skill_description(contents: &str) -> Option<String> {
    for line in contents.lines() {
        if let Some(value) = line.strip_prefix("description:") {
            let trimmed = value.trim();
            if !trimmed.is_empty() {
                return Some(trimmed.to_string());
            }
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use std::collections::{BTreeSet, VecDeque};
    use std::fs;
    use std::io::{Read, Write};
    use std::net::{SocketAddr, TcpListener};
    use std::path::{Path, PathBuf};
    use std::sync::{Arc, Mutex, OnceLock};
    use std::thread;
    use std::time::Duration;

    use super::{
        agent_permission_policy, allowed_tools_for_subagent, execute_agent_with_spawn,
        execute_tool, final_assistant_text, list_agent_profiles, list_agent_tasks, list_skills,
        load_agent_profile, load_agent_task, load_skill, mvp_tool_specs,
        persist_agent_terminal_state, runtime_tool_definitions, AgentInput, AgentJob,
        SubagentToolExecutor,
    };
    use runtime::{ApiRequest, AssistantEvent, ConversationRuntime, RuntimeError, Session};
    use serde_json::json;
    use tungstenite::{accept_hdr, Message as WebSocketMessage};

    fn env_lock() -> &'static Mutex<()> {
        static LOCK: OnceLock<Mutex<()>> = OnceLock::new();
        LOCK.get_or_init(|| Mutex::new(()))
    }

    fn temp_path(name: &str) -> PathBuf {
        let unique = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .expect("time")
            .as_nanos();
        std::env::temp_dir().join(format!("clawd-tools-{unique}-{name}"))
    }

    fn set_test_cwd(path: &Path) -> PathBuf {
        let original = std::env::current_dir().expect("current dir");
        std::env::set_current_dir(path).expect("set current dir");
        original
    }

    fn write_tools_mcp_server_script() -> PathBuf {
        let root = temp_path("mcp-server-script");
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

    #[test]
    fn exposes_mvp_tools() {
        let names = mvp_tool_specs()
            .into_iter()
            .map(|spec| spec.name)
            .collect::<Vec<_>>();
        assert!(names.contains(&"bash"));
        assert!(names.contains(&"read_file"));
        assert!(names.contains(&"WebFetch"));
        assert!(names.contains(&"WebSearch"));
        assert!(names.contains(&"ListMcpResourcesTool"));
        assert!(names.contains(&"ReadMcpResourceTool"));
        assert!(names.contains(&"MCPTool"));
        assert!(names.contains(&"McpAuthTool"));
        assert!(names.contains(&"TodoWrite"));
        assert!(names.contains(&"Skill"));
        assert!(names.contains(&"Agent"));
        assert!(names.contains(&"ToolSearch"));
        assert!(names.contains(&"NotebookEdit"));
        assert!(names.contains(&"Sleep"));
        assert!(names.contains(&"SendUserMessage"));
        assert!(names.contains(&"Config"));
        assert!(names.contains(&"StructuredOutput"));
        assert!(names.contains(&"REPL"));
        assert!(names.contains(&"PowerShell"));
    }

    #[test]
    fn rejects_unknown_tool_names() {
        let error = execute_tool("nope", &json!({})).expect_err("tool should be rejected");
        assert!(error.contains("unsupported tool"));
    }

    #[test]
    fn mcp_tool_family_operates_on_configured_servers() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("mcp-tools-cwd");
        let config_home = temp_path("mcp-tools-home");
        let script_path = write_tools_mcp_server_script();
        fs::create_dir_all(&cwd).expect("create cwd");
        fs::create_dir_all(&config_home).expect("create config home");
        fs::write(
            cwd.join(".simcoe.json"),
            serde_json::to_string_pretty(&json!({
                "mcpServers": {
                    "alpha": {
                        "type": "stdio",
                        "command": "python3",
                        "args": [script_path.to_string_lossy().into_owned()]
                    },
                    "remote": {
                        "type": "http",
                        "url": "https://vendor.example/mcp",
                        "oauth": {
                            "clientId": "client-id",
                            "callbackPort": 7777,
                            "authServerMetadataUrl": "https://issuer.example/.well-known/oauth-authorization-server",
                            "xaa": true
                        }
                    }
                }
            }))
            .expect("serialize settings"),
        )
        .expect("write project settings");

        let original_config_home = std::env::var("SIMCOE_CONFIG_HOME").ok();
        let original_cwd = set_test_cwd(&cwd);
        std::env::set_var("SIMCOE_CONFIG_HOME", &config_home);

        let listed_resources = execute_tool(
            "ListMcpResourcesTool",
            &json!({
                "server": "alpha"
            }),
        )
        .expect("list MCP resources");
        let listed_resources: serde_json::Value =
            serde_json::from_str(&listed_resources).expect("valid resource list json");
        assert_eq!(listed_resources["server"], json!("alpha"));
        assert_eq!(listed_resources["transport"], json!("stdio"));
        assert_eq!(listed_resources["resourceCount"], json!(1));
        assert_eq!(
            listed_resources["resources"][0]["uri"],
            json!("file://guide.txt")
        );

        let read_resource = execute_tool(
            "ReadMcpResourceTool",
            &json!({
                "server": "alpha",
                "uri": "file://guide.txt"
            }),
        )
        .expect("read MCP resource");
        let read_resource: serde_json::Value =
            serde_json::from_str(&read_resource).expect("valid resource read json");
        assert_eq!(read_resource["contentCount"], json!(1));
        assert_eq!(
            read_resource["contents"][0]["text"],
            json!("contents for file://guide.txt")
        );

        let listed_tools = execute_tool(
            "MCPTool",
            &json!({
                "server": "alpha"
            }),
        )
        .expect("list MCP tools");
        let listed_tools: serde_json::Value =
            serde_json::from_str(&listed_tools).expect("valid MCP tool list json");
        assert_eq!(listed_tools["action"], json!("list_tools"));
        assert_eq!(listed_tools["toolCount"], json!(1));
        assert_eq!(listed_tools["tools"][0]["name"], json!("echo"));

        let called_tool = execute_tool(
            "MCPTool",
            &json!({
                "server": "alpha",
                "tool": "echo",
                "arguments": {
                    "text": "hello"
                }
            }),
        )
        .expect("call MCP tool");
        let called_tool: serde_json::Value =
            serde_json::from_str(&called_tool).expect("valid MCP tool call json");
        assert_eq!(called_tool["action"], json!("call_tool"));
        assert_eq!(called_tool["tool"], json!("echo"));
        assert_eq!(called_tool["qualifiedToolName"], json!("mcp__alpha__echo"));
        assert_eq!(called_tool["structuredContent"]["server"], json!("alpha"));
        assert_eq!(called_tool["structuredContent"]["echoed"], json!("hello"));

        let auth = execute_tool("McpAuthTool", &json!({})).expect("inspect MCP auth");
        let auth: serde_json::Value = serde_json::from_str(&auth).expect("valid MCP auth json");
        assert_eq!(auth["serverCount"], json!(2));
        assert_eq!(auth["transportCounts"]["http"], json!(1));
        assert_eq!(auth["transportCounts"]["stdio"], json!(1));
        assert_eq!(auth["supportedExecutionCount"], json!(2));
        assert_eq!(auth["unsupportedExecutionCount"], json!(0));
        assert_eq!(auth["statusCounts"]["ready"], json!(1));
        assert_eq!(auth["statusCounts"]["user-auth-required"], json!(1));
        assert!(auth["unsupportedServers"]
            .as_array()
            .is_some_and(|servers| servers.is_empty()));
        assert!(auth["attentionServers"]
            .as_array()
            .is_some_and(|servers| servers.iter().any(|server| {
                server["server"] == json!("remote")
                    && server["status"] == json!("user-auth-required")
                    && server["transport"] == json!("http")
            })));
        let servers = auth["servers"].as_array().expect("auth server list");
        assert!(servers.iter().any(|server| {
            server["server"] == json!("alpha")
                && server["status"] == json!("ready")
                && server["supportedExecution"] == json!(true)
        }));
        assert!(servers.iter().any(|server| {
            server["server"] == json!("remote")
                && server["status"] == json!("user-auth-required")
                && server["supportedExecution"] == json!(true)
                && server["authKind"] == json!("oauth")
        }));

        let unsupported = execute_tool(
            "MCPTool",
            &json!({
                "server": "remote",
                "tool": "echo"
            }),
        )
        .expect_err("remote transport should be rejected honestly");
        assert!(unsupported.contains("requires stored OAuth credentials"));

        match original_config_home {
            Some(value) => std::env::set_var("SIMCOE_CONFIG_HOME", value),
            None => std::env::remove_var("SIMCOE_CONFIG_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(&cwd);
        let _ = fs::remove_dir_all(&config_home);
        let _ = fs::remove_dir_all(script_path.parent().expect("script parent"));
    }

    #[test]
    fn mcp_auth_reports_specific_details_for_sdk_and_proxy_transports() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("mcp-unsupported-cwd");
        let config_home = temp_path("mcp-unsupported-home");
        fs::create_dir_all(&cwd).expect("create cwd");
        fs::create_dir_all(&config_home).expect("create config home");

        fs::write(
            cwd.join(".simcoe.json"),
            serde_json::to_string_pretty(&json!({
                "mcpServers": {
                    "sdk-server": {
                        "type": "sdk",
                        "name": "sdk-adapter"
                    },
                    "proxy-server": {
                        "type": "simcoeai-proxy",
                        "url": "https://api.anthropic.com/v2/ccr-sessions/1?mcp_url=wss%3A%2F%2Fvendor.example%2Fmcp",
                        "id": "proxy-123"
                    }
                }
            }))
            .expect("serialize settings"),
        )
        .expect("write project settings");

        let original_config_home = std::env::var("SIMCOE_CONFIG_HOME").ok();
        let original_cwd = set_test_cwd(&cwd);
        std::env::set_var("SIMCOE_CONFIG_HOME", &config_home);

        let status =
            execute_tool("McpAuthTool", &json!({})).expect("inspect unsupported transports");
        let status: serde_json::Value = serde_json::from_str(&status).expect("valid status json");
        assert_eq!(status["serverCount"], json!(2));
        assert_eq!(status["transportCounts"]["sdk"], json!(1));
        assert_eq!(status["transportCounts"]["simcoe-ai-proxy"], json!(1));
        assert_eq!(status["supportedExecutionCount"], json!(0));
        assert_eq!(status["unsupportedExecutionCount"], json!(2));
        assert_eq!(status["statusCounts"]["unsupported-transport"], json!(2));
        assert!(status["unsupportedServers"]
            .as_array()
            .is_some_and(|servers| servers.iter().any(|server| {
                server["server"] == json!("sdk-server")
                    && server["transport"] == json!("sdk")
                    && server["detail"]
                        .as_str()
                        .is_some_and(|detail| detail.contains("SDK server `sdk-adapter`"))
            })));
        assert!(status["attentionServers"]
            .as_array()
            .is_some_and(|servers| servers.iter().any(|server| {
                server["server"] == json!("proxy-server")
                    && server["status"] == json!("unsupported-transport")
                    && server["transport"] == json!("simcoe-ai-proxy")
                    && server["detail"].as_str().is_some_and(|detail| {
                        detail.contains("proxy `proxy-123` targets `wss://vendor.example/mcp`")
                    })
            })));

        let servers = status["servers"].as_array().expect("server status array");
        let sdk = servers
            .iter()
            .find(|server| server["server"] == json!("sdk-server"))
            .expect("sdk server present");
        assert_eq!(sdk["status"], json!("unsupported-transport"));
        assert_eq!(sdk["supportedExecution"], json!(false));
        assert!(sdk["detail"]
            .as_str()
            .expect("sdk detail")
            .contains("SDK server `sdk-adapter` needs the upstream SDK adapter path"));

        let proxy = servers
            .iter()
            .find(|server| server["server"] == json!("proxy-server"))
            .expect("proxy server present");
        assert_eq!(proxy["status"], json!("unsupported-transport"));
        assert_eq!(proxy["supportedExecution"], json!(false));
        let proxy_detail = proxy["detail"].as_str().expect("proxy detail");
        assert!(proxy_detail.contains("proxy `proxy-123` targets `wss://vendor.example/mcp`"));
        assert!(proxy_detail.contains("SessionsWebSocket.ts"));
        assert!(proxy_detail.contains("sdkMessageAdapter.ts"));

        let proxy_error = execute_tool("MCPTool", &json!({ "server": "proxy-server" }))
            .expect_err("proxy transport should still be rejected honestly");
        assert!(proxy_error.contains("proxy `proxy-123` targets `wss://vendor.example/mcp`"));

        match original_config_home {
            Some(value) => std::env::set_var("SIMCOE_CONFIG_HOME", value),
            None => std::env::remove_var("SIMCOE_CONFIG_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(&cwd);
        let _ = fs::remove_dir_all(&config_home);
    }

    #[test]
    fn dynamic_http_mcp_tools_execute_with_saved_oauth_and_refresh() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("dynamic-http-mcp-cwd");
        let config_home = temp_path("dynamic-http-mcp-home");
        fs::create_dir_all(&cwd).expect("create cwd");
        fs::create_dir_all(&config_home).expect("create config home");

        let requests = Arc::new(Mutex::new(Vec::<HttpRequest>::new()));
        let base_url = Arc::new(Mutex::new(String::new()));
        let server = RequestAwareTestServer::spawn({
            let requests = Arc::clone(&requests);
            let base_url = Arc::clone(&base_url);
            Arc::new(move |request: &HttpRequest| {
                requests
                    .lock()
                    .unwrap_or_else(std::sync::PoisonError::into_inner)
                    .push(request.clone());
                match request.path.as_str() {
                    "/oauth-metadata" => {
                        let base_url = base_url
                            .lock()
                            .unwrap_or_else(std::sync::PoisonError::into_inner)
                            .clone();
                        HttpResponse::json(
                            200,
                            "OK",
                            &json!({
                                "authorization_endpoint": format!("{base_url}/oauth-authorize"),
                                "token_endpoint": format!("{base_url}/oauth-token"),
                            })
                            .to_string(),
                        )
                    }
                    "/oauth-token" => {
                        assert_eq!(
                            request.headers.get("content-type"),
                            Some(&String::from("application/x-www-form-urlencoded"))
                        );
                        assert!(request.body.contains("grant_type=refresh_token"));
                        assert!(request.body.contains("refresh_token=refresh-token"));
                        HttpResponse::json(
                            200,
                            "OK",
                            &json!({
                                "access_token": "refreshed-token",
                                "refresh_token": "fresh-refresh",
                                "expires_at": 9_999_999_999_u64,
                                "scopes": ["scope:a"],
                            })
                            .to_string(),
                        )
                    }
                    "/mcp" => {
                        let payload: serde_json::Value =
                            serde_json::from_str(&request.body).expect("valid JSON-RPC request");
                        assert_eq!(
                            request.headers.get("authorization"),
                            Some(&String::from("Bearer refreshed-token"))
                        );
                        let response = match payload["method"].as_str().expect("method") {
                            "tools/list" => json!({
                                "jsonrpc": "2.0",
                                "id": payload["id"].clone(),
                                "result": {
                                    "tools": [
                                        {
                                            "name": "echo",
                                            "description": "Echo over HTTP",
                                            "inputSchema": {
                                                "type": "object",
                                                "properties": {
                                                    "text": { "type": "string" }
                                                },
                                                "required": ["text"],
                                                "additionalProperties": false
                                            }
                                        }
                                    ]
                                }
                            }),
                            "tools/call" => {
                                assert_eq!(payload["params"]["name"], json!("echo"));
                                assert_eq!(payload["params"]["arguments"]["text"], json!("hello"));
                                json!({
                                    "jsonrpc": "2.0",
                                    "id": payload["id"].clone(),
                                    "result": {
                                        "content": [],
                                        "structuredContent": {
                                            "server": "vendor",
                                            "echoed": "hello"
                                        },
                                        "isError": false
                                    }
                                })
                            }
                            "resources/list" => json!({
                                "jsonrpc": "2.0",
                                "id": payload["id"].clone(),
                                "result": {
                                    "resources": [
                                        {
                                            "uri": "file://remote.txt",
                                            "name": "Remote Guide",
                                            "mimeType": "text/plain"
                                        }
                                    ]
                                }
                            }),
                            "resources/read" => {
                                assert_eq!(payload["params"]["uri"], json!("file://remote.txt"));
                                json!({
                                    "jsonrpc": "2.0",
                                    "id": payload["id"].clone(),
                                    "result": {
                                        "contents": [
                                            {
                                                "uri": "file://remote.txt",
                                                "mimeType": "text/plain",
                                                "text": "remote contents"
                                            }
                                        ]
                                    }
                                })
                            }
                            other => panic!("unexpected MCP method: {other}"),
                        };
                        HttpResponse::event_stream(200, "OK", &response.to_string())
                    }
                    other => panic!("unexpected request path: {other}"),
                }
            })
        });
        *base_url
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner) =
            format!("http://{}", server.addr());

        fs::write(
            cwd.join(".simcoe.json"),
            serde_json::to_string_pretty(&json!({
                "mcpServers": {
                    "vendor": {
                        "type": "http",
                        "url": format!("http://{}/mcp", server.addr()),
                        "oauth": {
                            "clientId": "client-id",
                            "authServerMetadataUrl": format!("http://{}/oauth-metadata", server.addr())
                        }
                    }
                }
            }))
            .expect("serialize settings"),
        )
        .expect("write project settings");

        let original_config_home = std::env::var("SIMCOE_CONFIG_HOME").ok();
        let original_cwd = set_test_cwd(&cwd);
        std::env::set_var("SIMCOE_CONFIG_HOME", &config_home);

        let saved = execute_tool(
            "McpAuthTool",
            &json!({
                "server": "vendor",
                "action": "save",
                "accessToken": "expired-token",
                "refreshToken": "refresh-token",
                "expiresAt": 1,
                "scopes": ["scope:a"]
            }),
        )
        .expect("save MCP OAuth credentials");
        let saved: serde_json::Value = serde_json::from_str(&saved).expect("valid save json");
        assert_eq!(saved["action"], json!("save"));
        assert_eq!(saved["servers"][0]["storedCredentials"], json!(true));

        let definitions = runtime_tool_definitions(None);
        assert!(definitions
            .iter()
            .any(|tool| tool.name == "mcp__vendor__echo"));

        let search = execute_tool("ToolSearch", &json!({ "query": "vendor echo" }))
            .expect("search dynamic MCP tools");
        let search: serde_json::Value = serde_json::from_str(&search).expect("valid search json");
        assert!(search["matches"]
            .as_array()
            .expect("search matches")
            .iter()
            .any(|value| value == "mcp__vendor__echo"));

        let called = execute_tool("mcp__vendor__echo", &json!({ "text": "hello" }))
            .expect("call dynamic MCP tool");
        let called: serde_json::Value = serde_json::from_str(&called).expect("valid call json");
        assert_eq!(called["qualifiedToolName"], json!("mcp__vendor__echo"));
        assert_eq!(called["structuredContent"]["server"], json!("vendor"));
        assert_eq!(called["structuredContent"]["echoed"], json!("hello"));

        let resources = execute_tool("ListMcpResourcesTool", &json!({ "server": "vendor" }))
            .expect("list remote MCP resources");
        let resources: serde_json::Value =
            serde_json::from_str(&resources).expect("valid resources json");
        assert_eq!(resources["transport"], json!("http"));
        assert_eq!(resources["resources"][0]["uri"], json!("file://remote.txt"));

        let read = execute_tool(
            "ReadMcpResourceTool",
            &json!({ "server": "vendor", "uri": "file://remote.txt" }),
        )
        .expect("read remote MCP resource");
        let read: serde_json::Value = serde_json::from_str(&read).expect("valid read json");
        assert_eq!(read["contents"][0]["text"], json!("remote contents"));

        let status = execute_tool("McpAuthTool", &json!({ "server": "vendor" }))
            .expect("inspect vendor auth");
        let status: serde_json::Value = serde_json::from_str(&status).expect("valid status json");
        assert_eq!(status["action"], json!("status"));
        assert_eq!(status["serverCount"], json!(1));
        assert_eq!(status["supportedExecutionCount"], json!(1));
        assert_eq!(status["unsupportedExecutionCount"], json!(0));
        assert_eq!(status["statusCounts"]["ready"], json!(1));
        assert_eq!(status["servers"][0]["status"], json!("ready"));
        assert_eq!(status["servers"][0]["storedCredentials"], json!(true));
        assert_eq!(status["servers"][0]["refreshTokenPresent"], json!(true));

        let logout = execute_tool(
            "McpAuthTool",
            &json!({ "server": "vendor", "action": "logout" }),
        )
        .expect("logout vendor auth");
        let logout: serde_json::Value = serde_json::from_str(&logout).expect("valid logout json");
        assert_eq!(logout["action"], json!("logout"));
        assert_eq!(logout["servers"][0]["storedCredentials"], json!(false));

        let missing_credentials = execute_tool("MCPTool", &json!({ "server": "vendor" }))
            .expect_err("remote MCP tool execution should require saved credentials after logout");
        assert!(missing_credentials.contains("requires stored OAuth credentials"));

        let requests = requests
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        assert!(
            requests
                .iter()
                .filter(|request| request.path == "/oauth-token")
                .count()
                >= 1
        );
        assert!(requests
            .iter()
            .any(|request| request.request_line.starts_with("POST /mcp ")));
        assert!(requests
            .iter()
            .filter(|request| request.path == "/mcp")
            .all(|request| request.headers.get("authorization")
                == Some(&String::from("Bearer refreshed-token"))));

        match original_config_home {
            Some(value) => std::env::set_var("SIMCOE_CONFIG_HOME", value),
            None => std::env::remove_var("SIMCOE_CONFIG_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(&cwd);
        let _ = fs::remove_dir_all(&config_home);
    }

    #[test]
    fn legacy_sse_mcp_tools_execute_with_saved_oauth_and_refresh() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("legacy-sse-mcp-cwd");
        let config_home = temp_path("legacy-sse-mcp-home");
        fs::create_dir_all(&cwd).expect("create cwd");
        fs::create_dir_all(&config_home).expect("create config home");

        let server = LegacySseTestServer::spawn();

        fs::write(
            cwd.join(".simcoe.json"),
            serde_json::to_string_pretty(&json!({
                "mcpServers": {
                    "vendor-sse": {
                        "type": "sse",
                        "url": format!("http://{}/sse", server.addr()),
                        "oauth": {
                            "clientId": "client-id",
                            "authServerMetadataUrl": format!("http://{}/oauth-metadata", server.addr())
                        }
                    }
                }
            }))
            .expect("serialize settings"),
        )
        .expect("write project settings");

        let original_config_home = std::env::var("SIMCOE_CONFIG_HOME").ok();
        let original_cwd = set_test_cwd(&cwd);
        std::env::set_var("SIMCOE_CONFIG_HOME", &config_home);

        let initial_status = execute_tool("McpAuthTool", &json!({ "server": "vendor-sse" }))
            .expect("inspect vendor-sse auth before save");
        let initial_status: serde_json::Value =
            serde_json::from_str(&initial_status).expect("valid initial status json");
        assert_eq!(initial_status["serverCount"], json!(1));
        assert_eq!(initial_status["supportedExecutionCount"], json!(1));
        assert_eq!(initial_status["unsupportedExecutionCount"], json!(0));
        assert_eq!(
            initial_status["statusCounts"]["user-auth-required"],
            json!(1)
        );
        assert_eq!(
            initial_status["servers"][0]["status"],
            json!("user-auth-required")
        );
        assert_eq!(
            initial_status["servers"][0]["supportedExecution"],
            json!(true)
        );

        let saved = execute_tool(
            "McpAuthTool",
            &json!({
                "server": "vendor-sse",
                "action": "save",
                "accessToken": "expired-token",
                "refreshToken": "refresh-token",
                "expiresAt": 1,
                "scopes": ["scope:a"]
            }),
        )
        .expect("save vendor-sse credentials");
        let saved: serde_json::Value = serde_json::from_str(&saved).expect("valid save json");
        assert_eq!(saved["action"], json!("save"));
        assert_eq!(saved["servers"][0]["storedCredentials"], json!(true));

        let definitions = runtime_tool_definitions(None);
        assert!(definitions
            .iter()
            .any(|tool| tool.name == "mcp__vendor-sse__echo"));

        let called = execute_tool("mcp__vendor-sse__echo", &json!({ "text": "hello" }))
            .expect("call dynamic legacy SSE MCP tool");
        let called: serde_json::Value = serde_json::from_str(&called).expect("valid call json");
        assert_eq!(called["transport"], json!("sse"));
        assert_eq!(called["structuredContent"]["server"], json!("vendor-sse"));
        assert_eq!(called["structuredContent"]["echoed"], json!("hello"));

        let listed = execute_tool("MCPTool", &json!({ "server": "vendor-sse" }))
            .expect("list legacy SSE MCP tools");
        let listed: serde_json::Value = serde_json::from_str(&listed).expect("valid list json");
        assert_eq!(listed["transport"], json!("sse"));
        assert_eq!(listed["tools"][0]["name"], json!("echo"));

        let resources = execute_tool("ListMcpResourcesTool", &json!({ "server": "vendor-sse" }))
            .expect("list legacy SSE resources");
        let resources: serde_json::Value =
            serde_json::from_str(&resources).expect("valid resource list json");
        assert_eq!(resources["transport"], json!("sse"));
        assert_eq!(resources["resources"][0]["uri"], json!("file://legacy.txt"));

        let read = execute_tool(
            "ReadMcpResourceTool",
            &json!({ "server": "vendor-sse", "uri": "file://legacy.txt" }),
        )
        .expect("read legacy SSE resource");
        let read: serde_json::Value = serde_json::from_str(&read).expect("valid read json");
        assert_eq!(read["contents"][0]["text"], json!("legacy contents"));

        let ready = execute_tool("McpAuthTool", &json!({ "server": "vendor-sse" }))
            .expect("inspect vendor-sse auth after save");
        let ready: serde_json::Value = serde_json::from_str(&ready).expect("valid ready json");
        assert_eq!(ready["supportedExecutionCount"], json!(1));
        assert_eq!(ready["unsupportedExecutionCount"], json!(0));
        assert_eq!(ready["statusCounts"]["ready"], json!(1));
        assert_eq!(ready["servers"][0]["status"], json!("ready"));
        assert_eq!(ready["servers"][0]["refreshTokenPresent"], json!(true));

        let logout = execute_tool(
            "McpAuthTool",
            &json!({ "server": "vendor-sse", "action": "logout" }),
        )
        .expect("logout vendor-sse auth");
        let logout: serde_json::Value = serde_json::from_str(&logout).expect("valid logout json");
        assert_eq!(logout["servers"][0]["storedCredentials"], json!(false));

        let missing_credentials = execute_tool("MCPTool", &json!({ "server": "vendor-sse" }))
            .expect_err("legacy SSE execution should require saved credentials after logout");
        assert!(missing_credentials.contains("requires stored OAuth credentials"));

        let requests = server.requests();
        assert!(
            requests
                .iter()
                .filter(|request| request.path == "/oauth-token")
                .count()
                >= 1
        );
        assert!(requests
            .iter()
            .any(|request| request.request_line.starts_with("GET /sse ")));
        assert!(requests
            .iter()
            .any(|request| request.request_line.starts_with("POST /messages ")));
        assert!(requests
            .iter()
            .filter(|request| request.path == "/sse" || request.path == "/messages")
            .all(|request| request.headers.get("authorization")
                == Some(&String::from("Bearer refreshed-token"))));

        match original_config_home {
            Some(value) => std::env::set_var("SIMCOE_CONFIG_HOME", value),
            None => std::env::remove_var("SIMCOE_CONFIG_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(&cwd);
        let _ = fs::remove_dir_all(&config_home);
    }

    #[test]
    fn websocket_mcp_tools_execute_with_static_headers() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("websocket-mcp-cwd");
        let config_home = temp_path("websocket-mcp-home");
        fs::create_dir_all(&cwd).expect("create cwd");
        fs::create_dir_all(&config_home).expect("create config home");

        let server = WebSocketTestServer::spawn();

        fs::write(
            cwd.join(".simcoe.json"),
            serde_json::to_string_pretty(&json!({
                "mcpServers": {
                    "vendor-ws": {
                        "type": "ws",
                        "url": format!("ws://{}/mcp", server.addr()),
                        "headers": {
                            "X-Test": "static-header"
                        }
                    }
                }
            }))
            .expect("serialize settings"),
        )
        .expect("write project settings");

        let original_config_home = std::env::var("SIMCOE_CONFIG_HOME").ok();
        let original_cwd = set_test_cwd(&cwd);
        std::env::set_var("SIMCOE_CONFIG_HOME", &config_home);

        let status = execute_tool("McpAuthTool", &json!({ "server": "vendor-ws" }))
            .expect("inspect websocket MCP auth");
        let status: serde_json::Value = serde_json::from_str(&status).expect("valid status json");
        assert_eq!(status["serverCount"], json!(1));
        assert_eq!(status["supportedExecutionCount"], json!(1));
        assert_eq!(status["unsupportedExecutionCount"], json!(0));
        assert_eq!(status["statusCounts"]["ready"], json!(1));
        assert_eq!(status["servers"][0]["status"], json!("ready"));
        assert_eq!(status["servers"][0]["supportedExecution"], json!(true));
        assert_eq!(status["servers"][0]["authKind"], json!("none"));

        let definitions = runtime_tool_definitions(None);
        assert!(definitions
            .iter()
            .any(|tool| tool.name == "mcp__vendor-ws__echo"));

        let called = execute_tool("mcp__vendor-ws__echo", &json!({ "text": "hello" }))
            .expect("call websocket MCP tool");
        let called: serde_json::Value = serde_json::from_str(&called).expect("valid call json");
        assert_eq!(called["transport"], json!("ws"));
        assert_eq!(called["structuredContent"]["server"], json!("vendor-ws"));
        assert_eq!(called["structuredContent"]["echoed"], json!("hello"));

        let listed = execute_tool("MCPTool", &json!({ "server": "vendor-ws" }))
            .expect("list websocket MCP tools");
        let listed: serde_json::Value = serde_json::from_str(&listed).expect("valid list json");
        assert_eq!(listed["transport"], json!("ws"));
        assert_eq!(listed["tools"][0]["name"], json!("echo"));

        let resources = execute_tool("ListMcpResourcesTool", &json!({ "server": "vendor-ws" }))
            .expect("list websocket MCP resources");
        let resources: serde_json::Value =
            serde_json::from_str(&resources).expect("valid resource list json");
        assert_eq!(resources["transport"], json!("ws"));
        assert_eq!(resources["resources"][0]["uri"], json!("file://ws.txt"));

        let read = execute_tool(
            "ReadMcpResourceTool",
            &json!({ "server": "vendor-ws", "uri": "file://ws.txt" }),
        )
        .expect("read websocket MCP resource");
        let read: serde_json::Value = serde_json::from_str(&read).expect("valid read json");
        assert_eq!(read["contents"][0]["text"], json!("websocket contents"));

        let requests = server.requests();
        assert!(requests.iter().all(|request| request.path == "/mcp"));
        assert!(requests.iter().all(|request| {
            request.headers.get("x-test") == Some(&String::from("static-header"))
        }));

        let messages = server.messages();
        assert!(messages
            .iter()
            .any(|message| message["method"] == json!("tools/list")));
        assert!(messages
            .iter()
            .any(|message| message["method"] == json!("tools/call")));
        assert!(messages
            .iter()
            .any(|message| message["method"] == json!("resources/list")));
        assert!(messages
            .iter()
            .any(|message| message["method"] == json!("resources/read")));

        match original_config_home {
            Some(value) => std::env::set_var("SIMCOE_CONFIG_HOME", value),
            None => std::env::remove_var("SIMCOE_CONFIG_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = fs::remove_dir_all(&cwd);
        let _ = fs::remove_dir_all(&config_home);
    }

    #[test]
    fn web_fetch_returns_prompt_aware_summary() {
        let server = TestServer::spawn(Arc::new(|request_line: &str| {
            assert!(request_line.starts_with("GET /page "));
            HttpResponse::html(
                200,
                "OK",
                "<html><head><title>Ignored</title></head><body><h1>Test Page</h1><p>Hello <b>world</b> from local server.</p></body></html>",
            )
        }));

        let result = execute_tool(
            "WebFetch",
            &json!({
                "url": format!("http://{}/page", server.addr()),
                "prompt": "Summarize this page"
            }),
        )
        .expect("WebFetch should succeed");

        let output: serde_json::Value = serde_json::from_str(&result).expect("valid json");
        assert_eq!(output["code"], 200);
        let summary = output["result"].as_str().expect("result string");
        assert!(summary.contains("Fetched"));
        assert!(summary.contains("Test Page"));
        assert!(summary.contains("Hello world from local server"));

        let titled = execute_tool(
            "WebFetch",
            &json!({
                "url": format!("http://{}/page", server.addr()),
                "prompt": "What is the page title?"
            }),
        )
        .expect("WebFetch title query should succeed");
        let titled_output: serde_json::Value = serde_json::from_str(&titled).expect("valid json");
        let titled_summary = titled_output["result"].as_str().expect("result string");
        assert!(titled_summary.contains("Title: Ignored"));
    }

    #[test]
    fn web_fetch_supports_plain_text_and_rejects_invalid_url() {
        let server = TestServer::spawn(Arc::new(|request_line: &str| {
            assert!(request_line.starts_with("GET /plain "));
            HttpResponse::text(200, "OK", "plain text response")
        }));

        let result = execute_tool(
            "WebFetch",
            &json!({
                "url": format!("http://{}/plain", server.addr()),
                "prompt": "Show me the content"
            }),
        )
        .expect("WebFetch should succeed for text content");

        let output: serde_json::Value = serde_json::from_str(&result).expect("valid json");
        assert_eq!(output["url"], format!("http://{}/plain", server.addr()));
        assert!(output["result"]
            .as_str()
            .expect("result")
            .contains("plain text response"));

        let error = execute_tool(
            "WebFetch",
            &json!({
                "url": "not a url",
                "prompt": "Summarize"
            }),
        )
        .expect_err("invalid URL should fail");
        assert!(error.contains("relative URL without a base") || error.contains("invalid"));
    }

    #[test]
    fn web_search_extracts_and_filters_results() {
        let server = TestServer::spawn(Arc::new(|request_line: &str| {
            assert!(request_line.contains("GET /search?q=rust+web+search "));
            HttpResponse::html(
                200,
                "OK",
                r#"
                <html><body>
                  <a class="result__a" href="https://docs.rs/reqwest">Reqwest docs</a>
                  <a class="result__a" href="https://example.com/blocked">Blocked result</a>
                </body></html>
                "#,
            )
        }));

        std::env::set_var(
            "CLAWD_WEB_SEARCH_BASE_URL",
            format!("http://{}/search", server.addr()),
        );
        let result = execute_tool(
            "WebSearch",
            &json!({
                "query": "rust web search",
                "allowed_domains": ["https://DOCS.rs/"],
                "blocked_domains": ["HTTPS://EXAMPLE.COM"]
            }),
        )
        .expect("WebSearch should succeed");
        std::env::remove_var("CLAWD_WEB_SEARCH_BASE_URL");

        let output: serde_json::Value = serde_json::from_str(&result).expect("valid json");
        assert_eq!(output["query"], "rust web search");
        let results = output["results"].as_array().expect("results array");
        let search_result = results
            .iter()
            .find(|item| item.get("content").is_some())
            .expect("search result block present");
        let content = search_result["content"].as_array().expect("content array");
        assert_eq!(content.len(), 1);
        assert_eq!(content[0]["title"], "Reqwest docs");
        assert_eq!(content[0]["url"], "https://docs.rs/reqwest");
    }

    #[test]
    fn web_search_handles_generic_links_and_invalid_base_url() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let server = TestServer::spawn(Arc::new(|request_line: &str| {
            assert!(request_line.contains("GET /fallback?q=generic+links "));
            HttpResponse::html(
                200,
                "OK",
                r#"
                <html><body>
                  <a href="https://example.com/one">Example One</a>
                  <a href="https://example.com/one">Duplicate Example One</a>
                  <a href="https://docs.rs/tokio">Tokio Docs</a>
                </body></html>
                "#,
            )
        }));

        std::env::set_var(
            "CLAWD_WEB_SEARCH_BASE_URL",
            format!("http://{}/fallback", server.addr()),
        );
        let result = execute_tool(
            "WebSearch",
            &json!({
                "query": "generic links"
            }),
        )
        .expect("WebSearch fallback parsing should succeed");
        std::env::remove_var("CLAWD_WEB_SEARCH_BASE_URL");

        let output: serde_json::Value = serde_json::from_str(&result).expect("valid json");
        let results = output["results"].as_array().expect("results array");
        let search_result = results
            .iter()
            .find(|item| item.get("content").is_some())
            .expect("search result block present");
        let content = search_result["content"].as_array().expect("content array");
        assert_eq!(content.len(), 2);
        assert_eq!(content[0]["url"], "https://example.com/one");
        assert_eq!(content[1]["url"], "https://docs.rs/tokio");

        std::env::set_var("CLAWD_WEB_SEARCH_BASE_URL", "://bad-base-url");
        let error = execute_tool("WebSearch", &json!({ "query": "generic links" }))
            .expect_err("invalid base URL should fail");
        std::env::remove_var("CLAWD_WEB_SEARCH_BASE_URL");
        assert!(error.contains("relative URL without a base") || error.contains("empty host"));
    }

    #[test]
    fn todo_write_persists_and_returns_previous_state() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let path = temp_path("todos.json");
        std::env::set_var("CLAWD_TODO_STORE", &path);

        let first = execute_tool(
            "TodoWrite",
            &json!({
                "todos": [
                    {"content": "Add tool", "activeForm": "Adding tool", "status": "in_progress"},
                    {"content": "Run tests", "activeForm": "Running tests", "status": "pending"}
                ]
            }),
        )
        .expect("TodoWrite should succeed");
        let first_output: serde_json::Value = serde_json::from_str(&first).expect("valid json");
        assert_eq!(first_output["oldTodos"].as_array().expect("array").len(), 0);

        let second = execute_tool(
            "TodoWrite",
            &json!({
                "todos": [
                    {"content": "Add tool", "activeForm": "Adding tool", "status": "completed"},
                    {"content": "Run tests", "activeForm": "Running tests", "status": "completed"},
                    {"content": "Verify", "activeForm": "Verifying", "status": "completed"}
                ]
            }),
        )
        .expect("TodoWrite should succeed");
        std::env::remove_var("CLAWD_TODO_STORE");
        let _ = std::fs::remove_file(path);

        let second_output: serde_json::Value = serde_json::from_str(&second).expect("valid json");
        assert_eq!(
            second_output["oldTodos"].as_array().expect("array").len(),
            2
        );
        assert_eq!(
            second_output["newTodos"].as_array().expect("array").len(),
            3
        );
        assert!(second_output["verificationNudgeNeeded"].is_null());
    }

    #[test]
    fn todo_write_rejects_invalid_payloads_and_sets_verification_nudge() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let path = temp_path("todos-errors.json");
        std::env::set_var("CLAWD_TODO_STORE", &path);

        let empty = execute_tool("TodoWrite", &json!({ "todos": [] }))
            .expect_err("empty todos should fail");
        assert!(empty.contains("todos must not be empty"));

        // Multiple in_progress items are now allowed for parallel workflows
        let _multi_active = execute_tool(
            "TodoWrite",
            &json!({
                "todos": [
                    {"content": "One", "activeForm": "Doing one", "status": "in_progress"},
                    {"content": "Two", "activeForm": "Doing two", "status": "in_progress"}
                ]
            }),
        )
        .expect("multiple in-progress todos should succeed");

        let blank_content = execute_tool(
            "TodoWrite",
            &json!({
                "todos": [
                    {"content": "   ", "activeForm": "Doing it", "status": "pending"}
                ]
            }),
        )
        .expect_err("blank content should fail");
        assert!(blank_content.contains("todo content must not be empty"));

        let nudge = execute_tool(
            "TodoWrite",
            &json!({
                "todos": [
                    {"content": "Write tests", "activeForm": "Writing tests", "status": "completed"},
                    {"content": "Fix errors", "activeForm": "Fixing errors", "status": "completed"},
                    {"content": "Ship branch", "activeForm": "Shipping branch", "status": "completed"}
                ]
            }),
        )
        .expect("completed todos should succeed");
        std::env::remove_var("CLAWD_TODO_STORE");
        let _ = fs::remove_file(path);

        let output: serde_json::Value = serde_json::from_str(&nudge).expect("valid json");
        assert_eq!(output["verificationNudgeNeeded"], true);
    }

    #[test]
    fn skill_loads_local_skill_prompt() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("skills-cwd");
        let codex_home = temp_path("skills-home");
        let skill_dir = codex_home.join("skills").join("help");
        std::fs::create_dir_all(&cwd).expect("create cwd");
        std::fs::create_dir_all(&skill_dir).expect("create skill dir");
        std::fs::write(
            skill_dir.join("SKILL.md"),
            "# Help\n\nGuide on using oh-my-codex plugin\n",
        )
        .expect("write skill prompt");

        let original_codex_home = std::env::var("CODEX_HOME").ok();
        let original_cwd = set_test_cwd(&cwd);
        std::env::set_var("CODEX_HOME", &codex_home);

        let result = execute_tool(
            "Skill",
            &json!({
                "skill": "help",
                "args": "overview"
            }),
        )
        .expect("Skill should succeed");

        let output: serde_json::Value = serde_json::from_str(&result).expect("valid json");
        assert_eq!(output["skill"], "help");
        assert!(output["path"]
            .as_str()
            .expect("path")
            .ends_with("/help/SKILL.md"));
        assert!(output["prompt"]
            .as_str()
            .expect("prompt")
            .contains("Guide on using oh-my-codex plugin"));

        let dollar_result = execute_tool(
            "Skill",
            &json!({
                "skill": "$help"
            }),
        )
        .expect("Skill should accept $skill invocation form");
        let dollar_output: serde_json::Value =
            serde_json::from_str(&dollar_result).expect("valid json");
        assert_eq!(dollar_output["skill"], "$help");
        assert!(dollar_output["path"]
            .as_str()
            .expect("path")
            .ends_with("/help/SKILL.md"));

        match original_codex_home {
            Some(value) => std::env::set_var("CODEX_HOME", value),
            None => std::env::remove_var("CODEX_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = std::fs::remove_dir_all(cwd);
        let _ = std::fs::remove_dir_all(codex_home);
    }

    #[test]
    fn skill_catalog_lists_discovered_local_skills() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("skills-catalog-cwd");
        let codex_home = temp_path("skills-catalog");
        let help_dir = codex_home.join("skills").join("help");
        let review_dir = codex_home.join("skills").join("review");
        std::fs::create_dir_all(&cwd).expect("create cwd");
        std::fs::create_dir_all(&help_dir).expect("create help skill dir");
        std::fs::create_dir_all(&review_dir).expect("create review skill dir");
        std::fs::write(
            help_dir.join("SKILL.md"),
            "description: Show REPL help\n\n# Help\n",
        )
        .expect("write help skill prompt");
        std::fs::write(
            review_dir.join("SKILL.md"),
            "description: Review the current change\n\n# Review\n",
        )
        .expect("write review skill prompt");

        let original_codex_home = std::env::var("CODEX_HOME").ok();
        let original_cwd = set_test_cwd(&cwd);
        std::env::set_var("CODEX_HOME", &codex_home);

        let skills = list_skills();
        assert_eq!(skills.len(), 2);
        assert_eq!(skills[0].name, "help");
        assert_eq!(skills[0].description.as_deref(), Some("Show REPL help"));
        assert_eq!(skills[1].name, "review");
        assert_eq!(
            skills[1].description.as_deref(),
            Some("Review the current change")
        );

        match original_codex_home {
            Some(value) => std::env::set_var("CODEX_HOME", value),
            None => std::env::remove_var("CODEX_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = std::fs::remove_dir_all(cwd);
        let _ = std::fs::remove_dir_all(codex_home);
    }

    #[test]
    fn load_skill_returns_prompt_metadata() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let cwd = temp_path("skills-load-cwd");
        let codex_home = temp_path("skills-load");
        let skill_dir = codex_home.join("skills").join("context-map");
        std::fs::create_dir_all(&cwd).expect("create cwd");
        std::fs::create_dir_all(&skill_dir).expect("create skill dir");
        std::fs::write(
            skill_dir.join("SKILL.md"),
            "description: Map relevant files\n\n# Context Map\nPrompt text\n",
        )
        .expect("write skill prompt");

        let original_codex_home = std::env::var("CODEX_HOME").ok();
        let original_cwd = set_test_cwd(&cwd);
        std::env::set_var("CODEX_HOME", &codex_home);

        let loaded =
            load_skill("context-map", Some("thorough".to_string())).expect("skill should load");
        assert_eq!(loaded.skill, "context-map");
        assert_eq!(loaded.args.as_deref(), Some("thorough"));
        assert_eq!(loaded.description.as_deref(), Some("Map relevant files"));
        assert!(loaded.prompt.contains("Prompt text"));
        assert!(loaded.path.ends_with("/context-map/SKILL.md"));

        match original_codex_home {
            Some(value) => std::env::set_var("CODEX_HOME", value),
            None => std::env::remove_var("CODEX_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = std::fs::remove_dir_all(cwd);
        let _ = std::fs::remove_dir_all(codex_home);
    }

    #[test]
    fn repo_local_skills_are_discovered_from_ancestor_catalog() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let repo_root = temp_path("repo-skills-root");
        let nested_cwd = repo_root
            .join("claude_references")
            .join("claw-code-main")
            .join("rust");
        let skill_dir = repo_root.join("skills");
        std::fs::create_dir_all(&nested_cwd).expect("create nested cwd");
        std::fs::create_dir_all(&skill_dir).expect("create skill dir");
        std::fs::write(
            skill_dir.join("electrical-estimating.md"),
            "---\nid: electrical-estimating\ntitle: Electrical Estimating\nsummary: Structure estimate answers around scope and uncertainty.\naliases:\n  - estimate\n  - quote\n---\nUse this skill for structured estimate answers.\n",
        )
        .expect("write repo skill");

        let original_codex_home = std::env::var("CODEX_HOME").ok();
        let original_cwd = set_test_cwd(&nested_cwd);
        std::env::remove_var("CODEX_HOME");

        let skills = list_skills();
        assert_eq!(skills.len(), 1);
        assert_eq!(skills[0].name, "electrical-estimating");
        assert_eq!(
            skills[0].description.as_deref(),
            Some("Structure estimate answers around scope and uncertainty.")
        );
        assert!(skills[0].path.ends_with("/skills/electrical-estimating.md"));

        let loaded = load_skill("estimate", Some("overview".to_string()))
            .expect("repo-local skill should load by alias");
        assert_eq!(loaded.skill, "electrical-estimating");
        assert_eq!(loaded.args.as_deref(), Some("overview"));
        assert_eq!(
            loaded.description.as_deref(),
            Some("Structure estimate answers around scope and uncertainty.")
        );
        assert!(loaded
            .prompt
            .contains("Use this skill for structured estimate answers."));

        match original_codex_home {
            Some(value) => std::env::set_var("CODEX_HOME", value),
            None => std::env::remove_var("CODEX_HOME"),
        }
        std::env::set_current_dir(original_cwd).expect("restore cwd");
        let _ = std::fs::remove_dir_all(repo_root);
    }

    #[test]
    fn tool_search_supports_keyword_and_select_queries() {
        let keyword = execute_tool(
            "ToolSearch",
            &json!({"query": "web current", "max_results": 3}),
        )
        .expect("ToolSearch should succeed");
        let keyword_output: serde_json::Value = serde_json::from_str(&keyword).expect("valid json");
        let matches = keyword_output["matches"].as_array().expect("matches");
        assert!(matches.iter().any(|value| value == "WebSearch"));

        let selected = execute_tool("ToolSearch", &json!({"query": "select:Agent,Skill"}))
            .expect("ToolSearch should succeed");
        let selected_output: serde_json::Value =
            serde_json::from_str(&selected).expect("valid json");
        assert_eq!(selected_output["matches"][0], "Agent");
        assert_eq!(selected_output["matches"][1], "Skill");

        let aliased = execute_tool("ToolSearch", &json!({"query": "AgentTool"}))
            .expect("ToolSearch should support tool aliases");
        let aliased_output: serde_json::Value = serde_json::from_str(&aliased).expect("valid json");
        assert_eq!(aliased_output["matches"][0], "Agent");
        assert_eq!(aliased_output["normalized_query"], "agent");

        let selected_with_alias =
            execute_tool("ToolSearch", &json!({"query": "select:AgentTool,Skill"}))
                .expect("ToolSearch alias select should succeed");
        let selected_with_alias_output: serde_json::Value =
            serde_json::from_str(&selected_with_alias).expect("valid json");
        assert_eq!(selected_with_alias_output["matches"][0], "Agent");
        assert_eq!(selected_with_alias_output["matches"][1], "Skill");
    }

    #[test]
    fn agent_persists_handoff_metadata() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let dir = temp_path("agent-store");
        std::env::set_var("CLAWD_AGENT_STORE", &dir);
        let captured = Arc::new(Mutex::new(None::<AgentJob>));
        let captured_for_spawn = Arc::clone(&captured);

        let manifest = execute_agent_with_spawn(
            AgentInput {
                description: "Audit the branch".to_string(),
                prompt: "Check tests and outstanding work.".to_string(),
                subagent_type: Some("Explore".to_string()),
                name: Some("ship-audit".to_string()),
                model: None,
            },
            move |job| {
                *captured_for_spawn
                    .lock()
                    .unwrap_or_else(std::sync::PoisonError::into_inner) = Some(job);
                Ok(())
            },
        )
        .expect("Agent should succeed");
        std::env::remove_var("CLAWD_AGENT_STORE");

        assert_eq!(manifest.name, "ship-audit");
        assert_eq!(manifest.subagent_type.as_deref(), Some("Explore"));
        assert_eq!(manifest.status, "running");
        assert!(!manifest.created_at.is_empty());
        assert!(manifest.started_at.is_some());
        assert!(manifest.completed_at.is_none());
        let contents = std::fs::read_to_string(&manifest.output_file).expect("agent file exists");
        let manifest_contents =
            std::fs::read_to_string(&manifest.manifest_file).expect("manifest file exists");
        assert!(contents.contains("Audit the branch"));
        assert!(contents.contains("Check tests and outstanding work."));
        assert!(manifest_contents.contains("\"subagentType\": \"Explore\""));
        assert!(manifest_contents.contains("\"status\": \"running\""));
        let captured_job = captured
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner)
            .clone()
            .expect("spawn job should be captured");
        assert_eq!(captured_job.prompt, "Check tests and outstanding work.");
        assert!(captured_job.allowed_tools.contains("read_file"));
        assert!(!captured_job.allowed_tools.contains("Agent"));

        let normalized = execute_tool(
            "Agent",
            &json!({
                "description": "Verify the branch",
                "prompt": "Check tests.",
                "subagent_type": "explorer"
            }),
        )
        .expect("Agent should normalize built-in aliases");
        let normalized_output: serde_json::Value =
            serde_json::from_str(&normalized).expect("valid json");
        assert_eq!(normalized_output["subagentType"], "Explore");

        let named = execute_tool(
            "Agent",
            &json!({
                "description": "Review the branch",
                "prompt": "Inspect diff.",
                "name": "Ship Audit!!!"
            }),
        )
        .expect("Agent should normalize explicit names");
        let named_output: serde_json::Value = serde_json::from_str(&named).expect("valid json");
        assert_eq!(named_output["name"], "ship-audit");
        let _ = std::fs::remove_dir_all(dir);
    }

    #[test]
    fn agent_fake_runner_can_persist_completion_and_failure() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let dir = temp_path("agent-runner");
        std::env::set_var("CLAWD_AGENT_STORE", &dir);

        let completed = execute_agent_with_spawn(
            AgentInput {
                description: "Complete the task".to_string(),
                prompt: "Do the work".to_string(),
                subagent_type: Some("Explore".to_string()),
                name: Some("complete-task".to_string()),
                model: Some("simcoe-sonnet-4-6".to_string()),
            },
            |job| {
                persist_agent_terminal_state(
                    &job.manifest,
                    "completed",
                    Some("Finished successfully"),
                    None,
                )
            },
        )
        .expect("completed agent should succeed");

        let completed_manifest = std::fs::read_to_string(&completed.manifest_file)
            .expect("completed manifest should exist");
        let completed_output =
            std::fs::read_to_string(&completed.output_file).expect("completed output should exist");
        assert!(completed_manifest.contains("\"status\": \"completed\""));
        assert!(completed_output.contains("Finished successfully"));

        let failed = execute_agent_with_spawn(
            AgentInput {
                description: "Fail the task".to_string(),
                prompt: "Do the failing work".to_string(),
                subagent_type: Some("Verification".to_string()),
                name: Some("fail-task".to_string()),
                model: None,
            },
            |job| {
                persist_agent_terminal_state(
                    &job.manifest,
                    "failed",
                    None,
                    Some(String::from("simulated failure")),
                )
            },
        )
        .expect("failed agent should still spawn");

        let failed_manifest =
            std::fs::read_to_string(&failed.manifest_file).expect("failed manifest should exist");
        let failed_output =
            std::fs::read_to_string(&failed.output_file).expect("failed output should exist");
        assert!(failed_manifest.contains("\"status\": \"failed\""));
        assert!(failed_manifest.contains("simulated failure"));
        assert!(failed_output.contains("simulated failure"));

        let spawn_error = execute_agent_with_spawn(
            AgentInput {
                description: "Spawn error task".to_string(),
                prompt: "Never starts".to_string(),
                subagent_type: None,
                name: Some("spawn-error".to_string()),
                model: None,
            },
            |_| Err(String::from("thread creation failed")),
        )
        .expect_err("spawn errors should surface");
        assert!(spawn_error.contains("failed to spawn sub-agent"));
        let spawn_error_manifest = std::fs::read_dir(&dir)
            .expect("agent dir should exist")
            .filter_map(Result::ok)
            .map(|entry| entry.path())
            .filter(|path| path.extension().and_then(|ext| ext.to_str()) == Some("json"))
            .find_map(|path| {
                let contents = std::fs::read_to_string(&path).ok()?;
                contents
                    .contains("\"name\": \"spawn-error\"")
                    .then_some(contents)
            })
            .expect("failed manifest should still be written");
        assert!(spawn_error_manifest.contains("\"status\": \"failed\""));
        assert!(spawn_error_manifest.contains("thread creation failed"));

        std::env::remove_var("CLAWD_AGENT_STORE");
        let _ = std::fs::remove_dir_all(dir);
    }

    #[test]
    fn agent_tasks_can_be_listed_and_loaded() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let dir = temp_path("agent-listing");
        std::env::set_var("CLAWD_AGENT_STORE", &dir);

        let first = execute_agent_with_spawn(
            AgentInput {
                description: "Audit the repo".to_string(),
                prompt: "Inspect the working tree".to_string(),
                subagent_type: Some("Explore".to_string()),
                name: Some("audit-repo".to_string()),
                model: None,
            },
            |job| {
                persist_agent_terminal_state(
                    &job.manifest,
                    "completed",
                    Some("Repo looks clean"),
                    None,
                )
            },
        )
        .expect("first agent should succeed");

        let second = execute_agent_with_spawn(
            AgentInput {
                description: "Verify release".to_string(),
                prompt: "Run verification".to_string(),
                subagent_type: Some("Verification".to_string()),
                name: Some("verify-release".to_string()),
                model: None,
            },
            |job| {
                persist_agent_terminal_state(
                    &job.manifest,
                    "failed",
                    None,
                    Some(String::from("tests failed")),
                )
            },
        )
        .expect("second agent should succeed");

        let tasks = list_agent_tasks().expect("tasks should load");
        assert_eq!(tasks.len(), 2);
        assert!(tasks.iter().any(|task| task.agent_id == first.agent_id));
        assert!(tasks.iter().any(|task| task.agent_id == second.agent_id));

        let loaded = load_agent_task(&first.agent_id).expect("exact id should load");
        assert_eq!(loaded.task.name, "audit-repo");
        assert_eq!(loaded.task.status, "completed");
        assert!(loaded
            .output
            .as_deref()
            .expect("output should exist")
            .contains("Repo looks clean"));

        let loaded_by_prefix =
            load_agent_task(&second.agent_id[..20]).expect("unique prefix should load");
        assert_eq!(loaded_by_prefix.task.name, "verify-release");
        assert_eq!(loaded_by_prefix.task.status, "failed");
        assert_eq!(loaded_by_prefix.task.error.as_deref(), Some("tests failed"));

        let missing = load_agent_task("missing-task").expect_err("unknown task should fail");
        assert!(missing.contains("unknown task"));

        std::env::remove_var("CLAWD_AGENT_STORE");
        let _ = std::fs::remove_dir_all(dir);
    }

    #[test]
    fn agent_tool_subset_mapping_is_expected() {
        let general = allowed_tools_for_subagent("general-purpose");
        assert!(general.contains("bash"));
        assert!(general.contains("write_file"));
        assert!(general.contains("MCPTool"));
        assert!(!general.contains("Agent"));

        let explore = allowed_tools_for_subagent("Explore");
        assert!(explore.contains("read_file"));
        assert!(explore.contains("grep_search"));
        assert!(explore.contains("ListMcpResourcesTool"));
        assert!(!explore.contains("bash"));

        let plan = allowed_tools_for_subagent("Plan");
        assert!(plan.contains("TodoWrite"));
        assert!(plan.contains("StructuredOutput"));
        assert!(plan.contains("McpAuthTool"));
        assert!(!plan.contains("Agent"));

        let verification = allowed_tools_for_subagent("Verification");
        assert!(verification.contains("bash"));
        assert!(verification.contains("PowerShell"));
        assert!(verification.contains("MCPTool"));
        assert!(!verification.contains("write_file"));
    }

    #[test]
    fn agent_profiles_list_and_resolve_aliases() {
        let profiles = list_agent_profiles();
        assert_eq!(profiles.len(), 6);
        assert!(profiles
            .iter()
            .any(|profile| profile.name == "general-purpose"));
        assert!(profiles.iter().any(|profile| profile.name == "Explore"));
        assert!(profiles.iter().any(|profile| profile.name == "Plan"));
        assert!(profiles
            .iter()
            .any(|profile| profile.name == "Verification"));

        let explore = load_agent_profile("explorer").expect("explore alias should resolve");
        assert_eq!(explore.name, "Explore");
        assert!(explore.tools.contains(&String::from("read_file")));
        assert!(!explore.tools.contains(&String::from("bash")));

        let guide = load_agent_profile("claudeCodeGuideAgent").expect("guide alias should resolve");
        assert_eq!(guide.name, "simcoe-ai-guide");
        assert!(guide.tools.contains(&String::from("SendUserMessage")));

        let missing =
            load_agent_profile("missing-profile").expect_err("unknown profile should fail");
        assert!(missing.contains("unknown agent profile"));
    }

    #[derive(Debug)]
    struct MockSubagentApiClient {
        calls: usize,
        input_path: String,
    }

    impl runtime::ApiClient for MockSubagentApiClient {
        fn stream(&mut self, request: ApiRequest) -> Result<Vec<AssistantEvent>, RuntimeError> {
            self.calls += 1;
            match self.calls {
                1 => {
                    assert_eq!(request.messages.len(), 1);
                    Ok(vec![
                        AssistantEvent::ToolUse {
                            id: "tool-1".to_string(),
                            name: "read_file".to_string(),
                            input: json!({ "path": self.input_path }).to_string(),
                        },
                        AssistantEvent::MessageStop,
                    ])
                }
                2 => {
                    assert!(request.messages.len() >= 3);
                    Ok(vec![
                        AssistantEvent::TextDelta("Scope: completed mock review".to_string()),
                        AssistantEvent::MessageStop,
                    ])
                }
                _ => panic!("unexpected mock stream call"),
            }
        }
    }

    #[test]
    fn subagent_runtime_executes_tool_loop_with_isolated_session() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let path = temp_path("subagent-input.txt");
        std::fs::write(&path, "hello from child").expect("write input file");

        let mut runtime = ConversationRuntime::new(
            Session::new(),
            MockSubagentApiClient {
                calls: 0,
                input_path: path.display().to_string(),
            },
            SubagentToolExecutor::new(BTreeSet::from([String::from("read_file")])),
            agent_permission_policy(),
            vec![String::from("system prompt")],
        );

        let summary = runtime
            .run_turn("Inspect the delegated file", None)
            .expect("subagent loop should succeed");

        assert_eq!(
            final_assistant_text(&summary),
            "Scope: completed mock review"
        );
        assert!(runtime
            .session()
            .messages
            .iter()
            .flat_map(|message| message.blocks.iter())
            .any(|block| matches!(
                block,
                runtime::ContentBlock::ToolResult { output, .. }
                    if output.contains("hello from child")
            )));

        let _ = std::fs::remove_file(path);
    }

    #[test]
    fn agent_rejects_blank_required_fields() {
        let missing_description = execute_tool(
            "Agent",
            &json!({
                "description": "  ",
                "prompt": "Inspect"
            }),
        )
        .expect_err("blank description should fail");
        assert!(missing_description.contains("description must not be empty"));

        let missing_prompt = execute_tool(
            "Agent",
            &json!({
                "description": "Inspect branch",
                "prompt": " "
            }),
        )
        .expect_err("blank prompt should fail");
        assert!(missing_prompt.contains("prompt must not be empty"));
    }

    #[test]
    fn notebook_edit_replaces_inserts_and_deletes_cells() {
        let path = temp_path("notebook.ipynb");
        std::fs::write(
            &path,
            r#"{
  "cells": [
    {"cell_type": "code", "id": "cell-a", "metadata": {}, "source": ["print(1)\n"], "outputs": [], "execution_count": null}
  ],
  "metadata": {"kernelspec": {"language": "python"}},
  "nbformat": 4,
  "nbformat_minor": 5
}"#,
        )
        .expect("write notebook");

        let replaced = execute_tool(
            "NotebookEdit",
            &json!({
                "notebook_path": path.display().to_string(),
                "cell_id": "cell-a",
                "new_source": "print(2)\n",
                "edit_mode": "replace"
            }),
        )
        .expect("NotebookEdit replace should succeed");
        let replaced_output: serde_json::Value = serde_json::from_str(&replaced).expect("json");
        assert_eq!(replaced_output["cell_id"], "cell-a");
        assert_eq!(replaced_output["cell_type"], "code");

        let inserted = execute_tool(
            "NotebookEdit",
            &json!({
                "notebook_path": path.display().to_string(),
                "cell_id": "cell-a",
                "new_source": "# heading\n",
                "cell_type": "markdown",
                "edit_mode": "insert"
            }),
        )
        .expect("NotebookEdit insert should succeed");
        let inserted_output: serde_json::Value = serde_json::from_str(&inserted).expect("json");
        assert_eq!(inserted_output["cell_type"], "markdown");
        let appended = execute_tool(
            "NotebookEdit",
            &json!({
                "notebook_path": path.display().to_string(),
                "new_source": "print(3)\n",
                "edit_mode": "insert"
            }),
        )
        .expect("NotebookEdit append should succeed");
        let appended_output: serde_json::Value = serde_json::from_str(&appended).expect("json");
        assert_eq!(appended_output["cell_type"], "code");

        let deleted = execute_tool(
            "NotebookEdit",
            &json!({
                "notebook_path": path.display().to_string(),
                "cell_id": "cell-a",
                "edit_mode": "delete"
            }),
        )
        .expect("NotebookEdit delete should succeed without new_source");
        let deleted_output: serde_json::Value = serde_json::from_str(&deleted).expect("json");
        assert!(deleted_output["cell_type"].is_null());
        assert_eq!(deleted_output["new_source"], "");

        let final_notebook: serde_json::Value =
            serde_json::from_str(&std::fs::read_to_string(&path).expect("read notebook"))
                .expect("valid notebook json");
        let cells = final_notebook["cells"].as_array().expect("cells array");
        assert_eq!(cells.len(), 2);
        assert_eq!(cells[0]["cell_type"], "markdown");
        assert!(cells[0].get("outputs").is_none());
        assert_eq!(cells[1]["cell_type"], "code");
        assert_eq!(cells[1]["source"][0], "print(3)\n");
        let _ = std::fs::remove_file(path);
    }

    #[test]
    fn notebook_edit_rejects_invalid_inputs() {
        let text_path = temp_path("notebook.txt");
        fs::write(&text_path, "not a notebook").expect("write text file");
        let wrong_extension = execute_tool(
            "NotebookEdit",
            &json!({
                "notebook_path": text_path.display().to_string(),
                "new_source": "print(1)\n"
            }),
        )
        .expect_err("non-ipynb file should fail");
        assert!(wrong_extension.contains("Jupyter notebook"));
        let _ = fs::remove_file(&text_path);

        let empty_notebook = temp_path("empty.ipynb");
        fs::write(
            &empty_notebook,
            r#"{"cells":[],"metadata":{"kernelspec":{"language":"python"}},"nbformat":4,"nbformat_minor":5}"#,
        )
        .expect("write empty notebook");

        let missing_source = execute_tool(
            "NotebookEdit",
            &json!({
                "notebook_path": empty_notebook.display().to_string(),
                "edit_mode": "insert"
            }),
        )
        .expect_err("insert without source should fail");
        assert!(missing_source.contains("new_source is required"));

        let missing_cell = execute_tool(
            "NotebookEdit",
            &json!({
                "notebook_path": empty_notebook.display().to_string(),
                "edit_mode": "delete"
            }),
        )
        .expect_err("delete on empty notebook should fail");
        assert!(missing_cell.contains("Notebook has no cells to edit"));
        let _ = fs::remove_file(empty_notebook);
    }

    #[test]
    fn bash_tool_reports_success_exit_failure_timeout_and_background() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let success = execute_tool("bash", &json!({ "command": "printf 'hello'" }))
            .expect("bash should succeed");
        let success_output: serde_json::Value = serde_json::from_str(&success).expect("json");
        assert_eq!(success_output["stdout"], "hello");
        assert_eq!(success_output["interrupted"], false);

        let failure = execute_tool("bash", &json!({ "command": "printf 'oops' >&2; exit 7" }))
            .expect("bash failure should still return structured output");
        let failure_output: serde_json::Value = serde_json::from_str(&failure).expect("json");
        assert_eq!(failure_output["returnCodeInterpretation"], "exit_code:7");
        assert!(failure_output["stderr"]
            .as_str()
            .expect("stderr")
            .contains("oops"));

        let timeout = execute_tool("bash", &json!({ "command": "sleep 1", "timeout": 10 }))
            .expect("bash timeout should return output");
        let timeout_output: serde_json::Value = serde_json::from_str(&timeout).expect("json");
        assert_eq!(timeout_output["interrupted"], true);
        assert_eq!(timeout_output["returnCodeInterpretation"], "timeout");
        assert!(timeout_output["stderr"]
            .as_str()
            .expect("stderr")
            .contains("Command exceeded timeout"));

        let background = execute_tool(
            "bash",
            &json!({ "command": "sleep 1", "run_in_background": true }),
        )
        .expect("bash background should succeed");
        let background_output: serde_json::Value = serde_json::from_str(&background).expect("json");
        assert!(background_output["backgroundTaskId"].as_str().is_some());
        assert_eq!(background_output["noOutputExpected"], true);
    }

    #[test]
    fn file_tools_cover_read_write_and_edit_behaviors() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let root = temp_path("fs-suite");
        fs::create_dir_all(&root).expect("create root");
        let original_dir = std::env::current_dir().expect("cwd");
        std::env::set_current_dir(&root).expect("set cwd");

        let write_create = execute_tool(
            "write_file",
            &json!({ "path": "nested/demo.txt", "content": "alpha\nbeta\nalpha\n" }),
        )
        .expect("write create should succeed");
        let write_create_output: serde_json::Value =
            serde_json::from_str(&write_create).expect("json");
        assert_eq!(write_create_output["type"], "create");
        assert!(root.join("nested/demo.txt").exists());

        let write_update = execute_tool(
            "write_file",
            &json!({ "path": "nested/demo.txt", "content": "alpha\nbeta\ngamma\n" }),
        )
        .expect("write update should succeed");
        let write_update_output: serde_json::Value =
            serde_json::from_str(&write_update).expect("json");
        assert_eq!(write_update_output["type"], "update");
        assert_eq!(write_update_output["originalFile"], "alpha\nbeta\nalpha\n");

        let read_full = execute_tool("read_file", &json!({ "path": "nested/demo.txt" }))
            .expect("read full should succeed");
        let read_full_output: serde_json::Value = serde_json::from_str(&read_full).expect("json");
        assert_eq!(read_full_output["file"]["content"], "alpha\nbeta\ngamma");
        assert_eq!(read_full_output["file"]["startLine"], 1);

        let read_slice = execute_tool(
            "read_file",
            &json!({ "path": "nested/demo.txt", "offset": 1, "limit": 1 }),
        )
        .expect("read slice should succeed");
        let read_slice_output: serde_json::Value = serde_json::from_str(&read_slice).expect("json");
        assert_eq!(read_slice_output["file"]["content"], "beta");
        assert_eq!(read_slice_output["file"]["startLine"], 2);

        let read_past_end = execute_tool(
            "read_file",
            &json!({ "path": "nested/demo.txt", "offset": 50 }),
        )
        .expect("read past EOF should succeed");
        let read_past_end_output: serde_json::Value =
            serde_json::from_str(&read_past_end).expect("json");
        assert_eq!(read_past_end_output["file"]["content"], "");
        assert_eq!(read_past_end_output["file"]["startLine"], 4);

        let read_error = execute_tool("read_file", &json!({ "path": "missing.txt" }))
            .expect_err("missing file should fail");
        assert!(!read_error.is_empty());

        let edit_once = execute_tool(
            "edit_file",
            &json!({ "path": "nested/demo.txt", "old_string": "alpha", "new_string": "omega" }),
        )
        .expect("single edit should succeed");
        let edit_once_output: serde_json::Value = serde_json::from_str(&edit_once).expect("json");
        assert_eq!(edit_once_output["replaceAll"], false);
        assert_eq!(
            fs::read_to_string(root.join("nested/demo.txt")).expect("read file"),
            "omega\nbeta\ngamma\n"
        );

        execute_tool(
            "write_file",
            &json!({ "path": "nested/demo.txt", "content": "alpha\nbeta\nalpha\n" }),
        )
        .expect("reset file");
        let edit_all = execute_tool(
            "edit_file",
            &json!({
                "path": "nested/demo.txt",
                "old_string": "alpha",
                "new_string": "omega",
                "replace_all": true
            }),
        )
        .expect("replace all should succeed");
        let edit_all_output: serde_json::Value = serde_json::from_str(&edit_all).expect("json");
        assert_eq!(edit_all_output["replaceAll"], true);
        assert_eq!(
            fs::read_to_string(root.join("nested/demo.txt")).expect("read file"),
            "omega\nbeta\nomega\n"
        );

        let edit_same = execute_tool(
            "edit_file",
            &json!({ "path": "nested/demo.txt", "old_string": "omega", "new_string": "omega" }),
        )
        .expect_err("identical old/new should fail");
        assert!(edit_same.contains("must differ"));

        let edit_missing = execute_tool(
            "edit_file",
            &json!({ "path": "nested/demo.txt", "old_string": "missing", "new_string": "omega" }),
        )
        .expect_err("missing substring should fail");
        assert!(edit_missing.contains("old_string not found"));

        std::env::set_current_dir(&original_dir).expect("restore cwd");
        let _ = fs::remove_dir_all(root);
    }

    #[test]
    fn glob_and_grep_tools_cover_success_and_errors() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let root = temp_path("search-suite");
        fs::create_dir_all(root.join("nested")).expect("create root");
        let original_dir = std::env::current_dir().expect("cwd");
        std::env::set_current_dir(&root).expect("set cwd");

        fs::write(
            root.join("nested/lib.rs"),
            "fn main() {}\nlet alpha = 1;\nlet alpha = 2;\n",
        )
        .expect("write rust file");
        fs::write(root.join("nested/notes.txt"), "alpha\nbeta\n").expect("write txt file");

        let globbed = execute_tool("glob_search", &json!({ "pattern": "nested/*.rs" }))
            .expect("glob should succeed");
        let globbed_output: serde_json::Value = serde_json::from_str(&globbed).expect("json");
        assert_eq!(globbed_output["numFiles"], 1);
        assert!(globbed_output["filenames"][0]
            .as_str()
            .expect("filename")
            .ends_with("nested/lib.rs"));

        let glob_error = execute_tool("glob_search", &json!({ "pattern": "[" }))
            .expect_err("invalid glob should fail");
        assert!(!glob_error.is_empty());

        let grep_content = execute_tool(
            "grep_search",
            &json!({
                "pattern": "alpha",
                "path": "nested",
                "glob": "*.rs",
                "output_mode": "content",
                "-n": true,
                "head_limit": 1,
                "offset": 1
            }),
        )
        .expect("grep content should succeed");
        let grep_content_output: serde_json::Value =
            serde_json::from_str(&grep_content).expect("json");
        assert_eq!(grep_content_output["numFiles"], 0);
        assert!(grep_content_output["appliedLimit"].is_null());
        assert_eq!(grep_content_output["appliedOffset"], 1);
        assert!(grep_content_output["content"]
            .as_str()
            .expect("content")
            .contains("let alpha = 2;"));

        let grep_count = execute_tool(
            "grep_search",
            &json!({ "pattern": "alpha", "path": "nested", "output_mode": "count" }),
        )
        .expect("grep count should succeed");
        let grep_count_output: serde_json::Value = serde_json::from_str(&grep_count).expect("json");
        assert_eq!(grep_count_output["numMatches"], 3);

        let grep_error = execute_tool(
            "grep_search",
            &json!({ "pattern": "(alpha", "path": "nested" }),
        )
        .expect_err("invalid regex should fail");
        assert!(!grep_error.is_empty());

        std::env::set_current_dir(&original_dir).expect("restore cwd");
        let _ = fs::remove_dir_all(root);
    }

    #[test]
    fn sleep_waits_and_reports_duration() {
        let started = std::time::Instant::now();
        let result =
            execute_tool("Sleep", &json!({"duration_ms": 20})).expect("Sleep should succeed");
        let elapsed = started.elapsed();
        let output: serde_json::Value = serde_json::from_str(&result).expect("json");
        assert_eq!(output["duration_ms"], 20);
        assert!(output["message"]
            .as_str()
            .expect("message")
            .contains("Slept for 20ms"));
        assert!(elapsed >= Duration::from_millis(15));
    }

    #[test]
    fn brief_returns_sent_message_and_attachment_metadata() {
        let attachment = std::env::temp_dir().join(format!(
            "clawd-brief-{}.png",
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .expect("time")
                .as_nanos()
        ));
        std::fs::write(&attachment, b"png-data").expect("write attachment");

        let result = execute_tool(
            "SendUserMessage",
            &json!({
                "message": "hello user",
                "attachments": [attachment.display().to_string()],
                "status": "normal"
            }),
        )
        .expect("SendUserMessage should succeed");

        let output: serde_json::Value = serde_json::from_str(&result).expect("json");
        assert_eq!(output["message"], "hello user");
        assert!(output["sentAt"].as_str().is_some());
        assert_eq!(output["attachments"][0]["isImage"], true);
        let _ = std::fs::remove_file(attachment);
    }

    #[test]
    fn config_reads_and_writes_supported_values() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let root = std::env::temp_dir().join(format!(
            "clawd-config-{}",
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .expect("time")
                .as_nanos()
        ));
        let home = root.join("home");
        let cwd = root.join("cwd");
        std::fs::create_dir_all(home.join(".simcoe")).expect("home dir");
        std::fs::create_dir_all(cwd.join(".simcoe")).expect("cwd dir");
        std::fs::write(
            home.join(".simcoe").join("settings.json"),
            r#"{"verbose":false}"#,
        )
        .expect("write global settings");

        let original_home = std::env::var("HOME").ok();
        let original_simcoe_home = std::env::var("SIMCOE_CONFIG_HOME").ok();
        let original_dir = std::env::current_dir().expect("cwd");
        std::env::set_var("HOME", &home);
        std::env::remove_var("SIMCOE_CONFIG_HOME");
        std::env::set_current_dir(&cwd).expect("set cwd");

        let get = execute_tool("Config", &json!({"setting": "verbose"})).expect("get config");
        let get_output: serde_json::Value = serde_json::from_str(&get).expect("json");
        assert_eq!(get_output["value"], false);

        let set = execute_tool(
            "Config",
            &json!({"setting": "permissions.defaultMode", "value": "plan"}),
        )
        .expect("set config");
        let set_output: serde_json::Value = serde_json::from_str(&set).expect("json");
        assert_eq!(set_output["operation"], "set");
        assert_eq!(set_output["newValue"], "plan");

        let invalid = execute_tool(
            "Config",
            &json!({"setting": "permissions.defaultMode", "value": "bogus"}),
        )
        .expect_err("invalid config value should error");
        assert!(invalid.contains("Invalid value"));

        let unknown =
            execute_tool("Config", &json!({"setting": "nope"})).expect("unknown setting result");
        let unknown_output: serde_json::Value = serde_json::from_str(&unknown).expect("json");
        assert_eq!(unknown_output["success"], false);

        std::env::set_current_dir(&original_dir).expect("restore cwd");
        match original_home {
            Some(value) => std::env::set_var("HOME", value),
            None => std::env::remove_var("HOME"),
        }
        match original_simcoe_home {
            Some(value) => std::env::set_var("SIMCOE_CONFIG_HOME", value),
            None => std::env::remove_var("SIMCOE_CONFIG_HOME"),
        }
        let _ = std::fs::remove_dir_all(root);
    }

    #[test]
    fn structured_output_echoes_input_payload() {
        let result = execute_tool("StructuredOutput", &json!({"ok": true, "items": [1, 2, 3]}))
            .expect("StructuredOutput should succeed");
        let output: serde_json::Value = serde_json::from_str(&result).expect("json");
        assert_eq!(output["data"], "Structured output provided successfully");
        assert_eq!(output["structured_output"]["ok"], true);
        assert_eq!(output["structured_output"]["items"][1], 2);
    }

    #[test]
    fn repl_executes_python_code() {
        let result = execute_tool(
            "REPL",
            &json!({"language": "python", "code": "print(1 + 1)", "timeout_ms": 500}),
        )
        .expect("REPL should succeed");
        let output: serde_json::Value = serde_json::from_str(&result).expect("json");
        assert_eq!(output["language"], "python");
        assert_eq!(output["exitCode"], 0);
        assert!(output["stdout"].as_str().expect("stdout").contains('2'));
    }

    #[test]
    fn powershell_runs_via_stub_shell() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let dir = std::env::temp_dir().join(format!(
            "clawd-pwsh-bin-{}",
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .expect("time")
                .as_nanos()
        ));
        std::fs::create_dir_all(&dir).expect("create dir");
        let script = dir.join("pwsh");
        std::fs::write(
            &script,
            r#"#!/bin/sh
while [ "$1" != "-Command" ] && [ $# -gt 0 ]; do shift; done
shift
printf 'pwsh:%s' "$1"
"#,
        )
        .expect("write script");
        std::process::Command::new("/bin/chmod")
            .arg("+x")
            .arg(&script)
            .status()
            .expect("chmod");
        let original_path = std::env::var("PATH").unwrap_or_default();
        std::env::set_var("PATH", format!("{}:{}", dir.display(), original_path));

        let result = execute_tool(
            "PowerShell",
            &json!({"command": "Write-Output hello", "timeout": 1000}),
        )
        .expect("PowerShell should succeed");

        let background = execute_tool(
            "PowerShell",
            &json!({"command": "Write-Output hello", "run_in_background": true}),
        )
        .expect("PowerShell background should succeed");

        std::env::set_var("PATH", original_path);
        let _ = std::fs::remove_dir_all(dir);

        let output: serde_json::Value = serde_json::from_str(&result).expect("json");
        assert_eq!(output["stdout"], "pwsh:Write-Output hello");
        assert!(output["stderr"].as_str().expect("stderr").is_empty());

        let background_output: serde_json::Value = serde_json::from_str(&background).expect("json");
        assert!(background_output["backgroundTaskId"].as_str().is_some());
        assert_eq!(background_output["backgroundedByUser"], true);
        assert_eq!(background_output["assistantAutoBackgrounded"], false);
    }

    #[test]
    fn powershell_errors_when_shell_is_missing() {
        let _guard = env_lock()
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner);
        let original_path = std::env::var("PATH").unwrap_or_default();
        let empty_dir = std::env::temp_dir().join(format!(
            "clawd-empty-bin-{}",
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .expect("time")
                .as_nanos()
        ));
        std::fs::create_dir_all(&empty_dir).expect("create empty dir");
        std::env::set_var("PATH", empty_dir.display().to_string());

        let err = execute_tool("PowerShell", &json!({"command": "Write-Output hello"}))
            .expect_err("PowerShell should fail when shell is missing");

        std::env::set_var("PATH", original_path);
        let _ = std::fs::remove_dir_all(empty_dir);

        assert!(err.contains("PowerShell executable not found"));
    }

    struct TestServer {
        addr: SocketAddr,
        shutdown: Option<std::sync::mpsc::Sender<()>>,
        handle: Option<thread::JoinHandle<()>>,
    }

    impl TestServer {
        fn spawn(handler: Arc<dyn Fn(&str) -> HttpResponse + Send + Sync + 'static>) -> Self {
            let listener = TcpListener::bind("127.0.0.1:0").expect("bind test server");
            listener
                .set_nonblocking(true)
                .expect("set nonblocking listener");
            let addr = listener.local_addr().expect("local addr");
            let (tx, rx) = std::sync::mpsc::channel::<()>();

            let handle = thread::spawn(move || loop {
                if rx.try_recv().is_ok() {
                    break;
                }

                match listener.accept() {
                    Ok((mut stream, _)) => {
                        let mut buffer = [0_u8; 4096];
                        let size = stream.read(&mut buffer).expect("read request");
                        let request = String::from_utf8_lossy(&buffer[..size]).into_owned();
                        let request_line = request.lines().next().unwrap_or_default().to_string();
                        let response = handler(&request_line);
                        stream
                            .write_all(response.to_bytes().as_slice())
                            .expect("write response");
                    }
                    Err(error) if error.kind() == std::io::ErrorKind::WouldBlock => {
                        thread::sleep(Duration::from_millis(10));
                    }
                    Err(error) => panic!("server accept failed: {error}"),
                }
            });

            Self {
                addr,
                shutdown: Some(tx),
                handle: Some(handle),
            }
        }

        fn addr(&self) -> SocketAddr {
            self.addr
        }
    }

    impl Drop for TestServer {
        fn drop(&mut self) {
            if let Some(tx) = self.shutdown.take() {
                let _ = tx.send(());
            }
            if let Some(handle) = self.handle.take() {
                handle.join().expect("join test server");
            }
        }
    }

    #[derive(Debug, Clone)]
    struct HttpRequest {
        request_line: String,
        path: String,
        headers: std::collections::BTreeMap<String, String>,
        body: String,
    }

    struct RequestAwareTestServer {
        addr: SocketAddr,
        shutdown: Option<std::sync::mpsc::Sender<()>>,
        handle: Option<thread::JoinHandle<()>>,
    }

    impl RequestAwareTestServer {
        fn spawn(
            handler: Arc<dyn Fn(&HttpRequest) -> HttpResponse + Send + Sync + 'static>,
        ) -> Self {
            let listener = TcpListener::bind("127.0.0.1:0").expect("bind test server");
            listener
                .set_nonblocking(true)
                .expect("set nonblocking listener");
            let addr = listener.local_addr().expect("local addr");
            let (tx, rx) = std::sync::mpsc::channel::<()>();

            let handle = thread::spawn(move || loop {
                if rx.try_recv().is_ok() {
                    break;
                }

                match listener.accept() {
                    Ok((mut stream, _)) => {
                        stream
                            .set_read_timeout(Some(Duration::from_secs(1)))
                            .expect("set read timeout");
                        let request = read_http_request(&mut stream);
                        let response = handler(&request);
                        stream
                            .write_all(response.to_bytes().as_slice())
                            .expect("write response");
                    }
                    Err(error) if error.kind() == std::io::ErrorKind::WouldBlock => {
                        thread::sleep(Duration::from_millis(10));
                    }
                    Err(error) => panic!("server accept failed: {error}"),
                }
            });

            Self {
                addr,
                shutdown: Some(tx),
                handle: Some(handle),
            }
        }

        fn addr(&self) -> SocketAddr {
            self.addr
        }
    }

    impl Drop for RequestAwareTestServer {
        fn drop(&mut self) {
            if let Some(tx) = self.shutdown.take() {
                let _ = tx.send(());
            }
            if let Some(handle) = self.handle.take() {
                handle.join().expect("join test server");
            }
        }
    }

    #[derive(Default)]
    struct LegacySseServerState {
        requests: Vec<HttpRequest>,
        pending_streams: VecDeque<std::sync::mpsc::Sender<String>>,
    }

    #[derive(Default)]
    struct WebSocketServerState {
        requests: Vec<HttpRequest>,
        messages: Vec<serde_json::Value>,
    }

    struct LegacySseTestServer {
        addr: SocketAddr,
        state: Arc<Mutex<LegacySseServerState>>,
        shutdown: Option<std::sync::mpsc::Sender<()>>,
        handle: Option<thread::JoinHandle<()>>,
    }

    impl LegacySseTestServer {
        fn spawn() -> Self {
            let listener = TcpListener::bind("127.0.0.1:0").expect("bind legacy SSE server");
            listener
                .set_nonblocking(true)
                .expect("set nonblocking listener");
            let addr = listener.local_addr().expect("local addr");
            let state = Arc::new(Mutex::new(LegacySseServerState::default()));
            let (tx, rx) = std::sync::mpsc::channel::<()>();
            let base_url = format!("http://{addr}");

            let handle = thread::spawn({
                let state = Arc::clone(&state);
                move || loop {
                    if rx.try_recv().is_ok() {
                        break;
                    }

                    match listener.accept() {
                        Ok((stream, _)) => {
                            let state = Arc::clone(&state);
                            let base_url = base_url.clone();
                            thread::spawn(move || {
                                handle_legacy_sse_connection(stream, state, &base_url)
                            });
                        }
                        Err(error) if error.kind() == std::io::ErrorKind::WouldBlock => {
                            thread::sleep(Duration::from_millis(10));
                        }
                        Err(error) => panic!("server accept failed: {error}"),
                    }
                }
            });

            Self {
                addr,
                state,
                shutdown: Some(tx),
                handle: Some(handle),
            }
        }

        fn addr(&self) -> SocketAddr {
            self.addr
        }

        fn requests(&self) -> Vec<HttpRequest> {
            self.state
                .lock()
                .unwrap_or_else(std::sync::PoisonError::into_inner)
                .requests
                .clone()
        }
    }

    impl Drop for LegacySseTestServer {
        fn drop(&mut self) {
            if let Some(tx) = self.shutdown.take() {
                let _ = tx.send(());
            }
            if let Some(handle) = self.handle.take() {
                handle.join().expect("join legacy SSE server");
            }
        }
    }

    struct WebSocketTestServer {
        addr: SocketAddr,
        state: Arc<Mutex<WebSocketServerState>>,
        shutdown: Option<std::sync::mpsc::Sender<()>>,
        handle: Option<thread::JoinHandle<()>>,
    }

    impl WebSocketTestServer {
        fn spawn() -> Self {
            let listener = TcpListener::bind("127.0.0.1:0").expect("bind websocket server");
            listener
                .set_nonblocking(true)
                .expect("set nonblocking listener");
            let addr = listener.local_addr().expect("local addr");
            let state = Arc::new(Mutex::new(WebSocketServerState::default()));
            let (tx, rx) = std::sync::mpsc::channel::<()>();

            let handle = thread::spawn({
                let state = Arc::clone(&state);
                move || loop {
                    if rx.try_recv().is_ok() {
                        break;
                    }

                    match listener.accept() {
                        Ok((stream, _)) => {
                            let state = Arc::clone(&state);
                            thread::spawn(move || handle_websocket_connection(stream, state));
                        }
                        Err(error) if error.kind() == std::io::ErrorKind::WouldBlock => {
                            thread::sleep(Duration::from_millis(10));
                        }
                        Err(error) => panic!("server accept failed: {error}"),
                    }
                }
            });

            Self {
                addr,
                state,
                shutdown: Some(tx),
                handle: Some(handle),
            }
        }

        fn addr(&self) -> SocketAddr {
            self.addr
        }

        fn requests(&self) -> Vec<HttpRequest> {
            self.state
                .lock()
                .unwrap_or_else(std::sync::PoisonError::into_inner)
                .requests
                .clone()
        }

        fn messages(&self) -> Vec<serde_json::Value> {
            self.state
                .lock()
                .unwrap_or_else(std::sync::PoisonError::into_inner)
                .messages
                .clone()
        }
    }

    impl Drop for WebSocketTestServer {
        fn drop(&mut self) {
            if let Some(tx) = self.shutdown.take() {
                let _ = tx.send(());
            }
            if let Some(handle) = self.handle.take() {
                handle.join().expect("join websocket server");
            }
        }
    }

    fn handle_legacy_sse_connection(
        mut stream: std::net::TcpStream,
        state: Arc<Mutex<LegacySseServerState>>,
        base_url: &str,
    ) {
        stream
            .set_read_timeout(Some(Duration::from_secs(1)))
            .expect("set read timeout");
        let request = read_http_request(&mut stream);
        state
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner)
            .requests
            .push(request.clone());

        match request.path.as_str() {
            "/oauth-metadata" => {
                let response = HttpResponse::json(
                    200,
                    "OK",
                    &json!({
                        "authorization_endpoint": format!("{base_url}/oauth-authorize"),
                        "token_endpoint": format!("{base_url}/oauth-token"),
                    })
                    .to_string(),
                );
                stream
                    .write_all(response.to_bytes().as_slice())
                    .expect("write oauth metadata response");
            }
            "/oauth-token" => {
                assert_eq!(
                    request.headers.get("content-type"),
                    Some(&String::from("application/x-www-form-urlencoded"))
                );
                assert!(request.body.contains("grant_type=refresh_token"));
                let response = HttpResponse::json(
                    200,
                    "OK",
                    &json!({
                        "access_token": "refreshed-token",
                        "refresh_token": "fresh-refresh",
                        "expires_at": 9_999_999_999_u64,
                        "scopes": ["scope:a"],
                    })
                    .to_string(),
                );
                stream
                    .write_all(response.to_bytes().as_slice())
                    .expect("write oauth token response");
            }
            "/sse" => {
                let (tx, rx) = std::sync::mpsc::channel::<String>();
                state
                    .lock()
                    .unwrap_or_else(std::sync::PoisonError::into_inner)
                    .pending_streams
                    .push_back(tx);
                let bootstrap = format!(
                    "HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nConnection: close\r\n\r\nevent: endpoint\ndata: /messages\n\n"
                );
                stream
                    .write_all(bootstrap.as_bytes())
                    .expect("write SSE bootstrap");
                if let Ok(message) = rx.recv_timeout(Duration::from_secs(1)) {
                    let event = format!("event: message\ndata: {message}\n\n");
                    stream
                        .write_all(event.as_bytes())
                        .expect("write SSE message event");
                }
            }
            "/messages" => {
                let payload: serde_json::Value =
                    serde_json::from_str(&request.body).expect("valid JSON-RPC request");
                let response = match payload["method"].as_str().expect("method") {
                    "tools/list" => json!({
                        "jsonrpc": "2.0",
                        "id": payload["id"].clone(),
                        "result": {
                            "tools": [
                                {
                                    "name": "echo",
                                    "description": "Echo over legacy SSE",
                                    "inputSchema": {
                                        "type": "object",
                                        "properties": {
                                            "text": { "type": "string" }
                                        },
                                        "required": ["text"],
                                        "additionalProperties": false
                                    }
                                }
                            ]
                        }
                    }),
                    "tools/call" => {
                        assert_eq!(payload["params"]["name"], json!("echo"));
                        json!({
                            "jsonrpc": "2.0",
                            "id": payload["id"].clone(),
                            "result": {
                                "content": [],
                                "structuredContent": {
                                    "server": "vendor-sse",
                                    "echoed": payload["params"]["arguments"]["text"].clone()
                                },
                                "isError": false
                            }
                        })
                    }
                    "resources/list" => json!({
                        "jsonrpc": "2.0",
                        "id": payload["id"].clone(),
                        "result": {
                            "resources": [
                                {
                                    "uri": "file://legacy.txt",
                                    "name": "Legacy Guide",
                                    "mimeType": "text/plain"
                                }
                            ]
                        }
                    }),
                    "resources/read" => json!({
                        "jsonrpc": "2.0",
                        "id": payload["id"].clone(),
                        "result": {
                            "contents": [
                                {
                                    "uri": payload["params"]["uri"].clone(),
                                    "mimeType": "text/plain",
                                    "text": "legacy contents"
                                }
                            ]
                        }
                    }),
                    other => panic!("unexpected MCP method: {other}"),
                };
                let sender = state
                    .lock()
                    .unwrap_or_else(std::sync::PoisonError::into_inner)
                    .pending_streams
                    .pop_front()
                    .expect("pending SSE stream for POST request");
                sender
                    .send(response.to_string())
                    .expect("send SSE response payload");
                let response = HttpResponse::text(202, "Accepted", "");
                stream
                    .write_all(response.to_bytes().as_slice())
                    .expect("write POST ack response");
            }
            other => panic!("unexpected request path: {other}"),
        }
    }

    fn handle_websocket_connection(
        stream: std::net::TcpStream,
        state: Arc<Mutex<WebSocketServerState>>,
    ) {
        stream
            .set_read_timeout(Some(Duration::from_secs(1)))
            .expect("set read timeout");
        stream
            .set_write_timeout(Some(Duration::from_secs(1)))
            .expect("set write timeout");

        let request_state = Arc::clone(&state);
        let mut websocket = accept_hdr(
            stream,
            move |request: &tungstenite::handshake::server::Request,
                  response: tungstenite::handshake::server::Response| {
                let headers = request
                    .headers()
                    .iter()
                    .filter_map(|(name, value)| {
                        value
                            .to_str()
                            .ok()
                            .map(|value| (name.as_str().to_ascii_lowercase(), value.to_string()))
                    })
                    .collect::<std::collections::BTreeMap<_, _>>();
                request_state
                    .lock()
                    .unwrap_or_else(std::sync::PoisonError::into_inner)
                    .requests
                    .push(HttpRequest {
                        request_line: format!("GET {} HTTP/1.1", request.uri()),
                        path: request.uri().path().to_string(),
                        headers,
                        body: String::new(),
                    });
                Ok(response)
            },
        )
        .expect("accept websocket");

        let payload = loop {
            match websocket.read().expect("read websocket message") {
                WebSocketMessage::Text(text) => break text.to_string(),
                WebSocketMessage::Binary(data) => {
                    break String::from_utf8(data.to_vec()).expect("utf-8 websocket payload")
                }
                WebSocketMessage::Ping(payload) => websocket
                    .send(WebSocketMessage::Pong(payload))
                    .expect("send websocket pong"),
                WebSocketMessage::Pong(_) => {}
                WebSocketMessage::Close(_) => return,
                _ => {}
            }
        };

        let payload: serde_json::Value =
            serde_json::from_str(&payload).expect("valid websocket JSON-RPC request");
        state
            .lock()
            .unwrap_or_else(std::sync::PoisonError::into_inner)
            .messages
            .push(payload.clone());

        let response = match payload["method"].as_str().expect("method") {
            "tools/list" => json!({
                "jsonrpc": "2.0",
                "id": payload["id"].clone(),
                "result": {
                    "tools": [
                        {
                            "name": "echo",
                            "description": "Echo over websocket",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "text": { "type": "string" }
                                },
                                "required": ["text"],
                                "additionalProperties": false
                            }
                        }
                    ]
                }
            }),
            "tools/call" => {
                assert_eq!(payload["params"]["name"], json!("echo"));
                json!({
                    "jsonrpc": "2.0",
                    "id": payload["id"].clone(),
                    "result": {
                        "content": [],
                        "structuredContent": {
                            "server": "vendor-ws",
                            "echoed": payload["params"]["arguments"]["text"].clone()
                        },
                        "isError": false
                    }
                })
            }
            "resources/list" => json!({
                "jsonrpc": "2.0",
                "id": payload["id"].clone(),
                "result": {
                    "resources": [
                        {
                            "uri": "file://ws.txt",
                            "name": "WebSocket Guide",
                            "mimeType": "text/plain"
                        }
                    ]
                }
            }),
            "resources/read" => json!({
                "jsonrpc": "2.0",
                "id": payload["id"].clone(),
                "result": {
                    "contents": [
                        {
                            "uri": payload["params"]["uri"].clone(),
                            "mimeType": "text/plain",
                            "text": "websocket contents"
                        }
                    ]
                }
            }),
            other => panic!("unexpected MCP method: {other}"),
        };

        websocket
            .send(WebSocketMessage::Text(response.to_string().into()))
            .expect("send websocket response");
    }

    fn read_http_request(stream: &mut impl Read) -> HttpRequest {
        let mut buffer = Vec::new();
        let mut chunk = [0_u8; 1024];
        let header_end = loop {
            let size = stream.read(&mut chunk).expect("read request chunk");
            assert_ne!(size, 0, "request terminated before headers were complete");
            buffer.extend_from_slice(&chunk[..size]);
            if let Some(index) = find_http_header_end(&buffer) {
                break index;
            }
        };

        let header_text = String::from_utf8_lossy(&buffer[..header_end]).into_owned();
        let content_length = header_text
            .lines()
            .skip(1)
            .find_map(|line| {
                let (name, value) = line.split_once(':')?;
                name.trim()
                    .eq_ignore_ascii_case("content-length")
                    .then(|| value.trim().parse::<usize>().expect("valid content length"))
            })
            .unwrap_or(0);
        let total_len = header_end + 4 + content_length;
        while buffer.len() < total_len {
            let size = stream.read(&mut chunk).expect("read request body chunk");
            assert_ne!(size, 0, "request terminated before body was complete");
            buffer.extend_from_slice(&chunk[..size]);
        }

        let mut lines = header_text.lines();
        let request_line = lines.next().unwrap_or_default().to_string();
        let path = request_line
            .split_whitespace()
            .nth(1)
            .unwrap_or_default()
            .to_string();
        let headers = lines
            .filter_map(|line| {
                let (name, value) = line.split_once(':')?;
                Some((name.trim().to_ascii_lowercase(), value.trim().to_string()))
            })
            .collect::<std::collections::BTreeMap<_, _>>();
        let body = String::from_utf8_lossy(&buffer[(header_end + 4)..total_len]).into_owned();

        HttpRequest {
            request_line,
            path,
            headers,
            body,
        }
    }

    fn find_http_header_end(buffer: &[u8]) -> Option<usize> {
        buffer.windows(4).position(|window| window == b"\r\n\r\n")
    }

    struct HttpResponse {
        status: u16,
        reason: &'static str,
        content_type: &'static str,
        body: String,
    }

    impl HttpResponse {
        fn html(status: u16, reason: &'static str, body: &str) -> Self {
            Self {
                status,
                reason,
                content_type: "text/html; charset=utf-8",
                body: body.to_string(),
            }
        }

        fn text(status: u16, reason: &'static str, body: &str) -> Self {
            Self {
                status,
                reason,
                content_type: "text/plain; charset=utf-8",
                body: body.to_string(),
            }
        }

        fn json(status: u16, reason: &'static str, body: &str) -> Self {
            Self {
                status,
                reason,
                content_type: "application/json",
                body: body.to_string(),
            }
        }

        fn event_stream(status: u16, reason: &'static str, body: &str) -> Self {
            Self {
                status,
                reason,
                content_type: "text/event-stream",
                body: format!("event: message\ndata: {body}\n\n"),
            }
        }

        fn to_bytes(&self) -> Vec<u8> {
            format!(
                "HTTP/1.1 {} {}\r\nContent-Type: {}\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{}",
                self.status,
                self.reason,
                self.content_type,
                self.body.len(),
                self.body
            )
            .into_bytes()
        }
    }
}
