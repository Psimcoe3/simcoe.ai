mod bash;
mod bootstrap;
mod compact;
mod config;
mod conversation;
mod file_ops;
mod hooks;
mod json;
mod mcp;
mod mcp_client;
mod mcp_stdio;
mod oauth;
mod permissions;
mod prompt;
mod remote;
pub mod sandbox;
mod session;
mod usage;
mod workspace;

pub use bash::{execute_bash, BashCommandInput, BashCommandOutput};
pub use bootstrap::{BootstrapPhase, BootstrapPlan};
pub use compact::{
    compact_session, estimate_session_tokens, format_compact_summary,
    get_compact_continuation_message, should_compact, CompactionConfig, CompactionResult,
};
pub use config::{
    ConfigEntry, ConfigError, ConfigLoader, ConfigSource, McpConfigCollection, McpOAuthConfig,
    McpRemoteServerConfig, McpSdkServerConfig, McpServerConfig, McpSimcoeAiProxyServerConfig,
    McpStdioServerConfig, McpTransport, McpWebSocketServerConfig, OAuthConfig,
    ResolvedPermissionMode, RuntimeConfig, RuntimeFeatureConfig, RuntimeHookConfig,
    ScopedMcpServerConfig, SIMCOE_AI_SETTINGS_SCHEMA_NAME,
};
pub use conversation::{
    auto_compaction_threshold_from_env, ApiClient, ApiRequest, AssistantEvent, AssistantTurnTrace,
    AutoCompactionEvent, ConversationRuntime, RuntimeError, StaticToolExecutor, ToolError,
    ToolExecutor, ToolResultTrace, TurnSummary,
};
pub use file_ops::{
    edit_file, glob_search, grep_search, read_file, write_file, EditFileOutput, GlobSearchOutput,
    GrepSearchInput, GrepSearchOutput, ReadFileOutput, StructuredPatchHunk, TextFilePayload,
    WriteFileOutput,
};
pub use hooks::{HookEvent, HookRunResult, HookRunner};
pub use mcp::{
    classify_mcp_reason_kind, mcp_client_transport_display_name, mcp_credentials_key,
    mcp_oauth_token_is_expired, mcp_reason_remediation_hint, mcp_server_auth_status,
    mcp_server_signature, mcp_tool_name, mcp_tool_prefix, mcp_transport_display_name,
    normalize_name_for_mcp, scoped_mcp_config_hash, unsupported_live_mcp_execution_reason,
    unwrap_ccr_proxy_url, McpReasonKind, McpServerAuthStatusSnapshot,
};
pub use mcp_client::{
    McpClientAuth, McpClientBootstrap, McpClientTransport, McpRemoteTransport, McpSdkTransport,
    McpSimcoeAiProxyTransport, McpStdioTransport,
};
pub use mcp_stdio::{
    spawn_mcp_stdio_process, JsonRpcError, JsonRpcId, JsonRpcRequest, JsonRpcResponse,
    ManagedMcpTool, McpInitializeClientInfo, McpInitializeParams, McpInitializeResult,
    McpInitializeServerInfo, McpListResourcesParams, McpListResourcesResult, McpListToolsParams,
    McpListToolsResult, McpReadResourceParams, McpReadResourceResult, McpResource,
    McpResourceContents, McpServerManager, McpServerManagerError, McpStdioProcess, McpTool,
    McpToolCallContent, McpToolCallParams, McpToolCallResult, UnsupportedMcpServer,
};
pub use oauth::{
    clear_mcp_oauth_credentials, clear_oauth_credentials, code_challenge_s256, credentials_path,
    generate_pkce_pair, generate_state, load_mcp_oauth_credentials, load_oauth_credentials,
    loopback_redirect_uri, parse_oauth_callback_query, parse_oauth_callback_request_target,
    save_mcp_oauth_credentials, save_oauth_credentials, OAuthAuthorizationRequest,
    OAuthCallbackParams, OAuthRefreshRequest, OAuthTokenExchangeRequest, OAuthTokenSet,
    PkceChallengeMethod, PkceCodePair,
};
pub use permissions::{
    PermissionMode, PermissionOutcome, PermissionPolicy, PermissionPromptDecision,
    PermissionPrompter, PermissionRequest,
};
pub use prompt::{
    load_system_prompt, prepend_bullets, ContextFile, ProjectContext, PromptBuildError,
    SystemPromptBuilder, FRONTIER_MODEL_NAME, SYSTEM_PROMPT_DYNAMIC_BOUNDARY,
};
pub use remote::{
    inherited_upstream_proxy_env, no_proxy_list, read_token, upstream_proxy_live_transport_status,
    upstream_proxy_websocket_probe, upstream_proxy_websocket_probe_from_env_map,
    upstream_proxy_ws_url, RemoteSessionContext, UpstreamProxyBootstrap,
    UpstreamProxyLiveTransportStatus, UpstreamProxyState, UpstreamProxyWebSocketProbe,
    DEFAULT_SESSION_TOKEN_PATH, DEFAULT_SYSTEM_CA_BUNDLE, NO_PROXY_HOSTS, UPSTREAM_PROXY_ENV_KEYS,
    UPSTREAM_PROXY_PROBE_ENV_VAR,
};
pub use session::{ContentBlock, ConversationMessage, MessageRole, Session, SessionError};
pub use usage::{
    format_usd, pricing_for_model, ModelPricing, TokenUsage, UsageCostEstimate, UsageTracker,
};
pub use workspace::{
    active_worktree_root, clear_active_worktree_root, effective_current_dir,
    plan_mode_active, set_active_worktree_root, set_plan_mode_active,
};

#[cfg(test)]
pub(crate) fn test_env_lock() -> std::sync::MutexGuard<'static, ()> {
    static LOCK: std::sync::OnceLock<std::sync::Mutex<()>> = std::sync::OnceLock::new();
    LOCK.get_or_init(|| std::sync::Mutex::new(()))
        .lock()
        .unwrap_or_else(std::sync::PoisonError::into_inner)
}
