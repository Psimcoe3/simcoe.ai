use crate::config::{McpServerConfig, McpTransport, ScopedMcpServerConfig};
use crate::mcp_client::McpClientTransport;

const SIMCOEAI_SERVER_PREFIX: &str = "simcoe.ai ";
const CCR_PROXY_PATH_MARKERS: [&str; 2] = ["/v2/session_ingress/shttp/mcp/", "/v2/ccr-sessions/"];

#[must_use]
pub fn normalize_name_for_mcp(name: &str) -> String {
    let mut normalized = name
        .chars()
        .map(|ch| match ch {
            'a'..='z' | 'A'..='Z' | '0'..='9' | '_' | '-' => ch,
            _ => '_',
        })
        .collect::<String>();

    if name.starts_with(SIMCOEAI_SERVER_PREFIX) {
        normalized = collapse_underscores(&normalized)
            .trim_matches('_')
            .to_string();
    }

    normalized
}

#[must_use]
pub fn mcp_tool_prefix(server_name: &str) -> String {
    format!("mcp__{}__", normalize_name_for_mcp(server_name))
}

#[must_use]
pub fn mcp_tool_name(server_name: &str, tool_name: &str) -> String {
    format!(
        "{}{}",
        mcp_tool_prefix(server_name),
        normalize_name_for_mcp(tool_name)
    )
}

#[must_use]
pub fn unwrap_ccr_proxy_url(url: &str) -> String {
    if !CCR_PROXY_PATH_MARKERS
        .iter()
        .any(|marker| url.contains(marker))
    {
        return url.to_string();
    }

    let Some(query_start) = url.find('?') else {
        return url.to_string();
    };
    let query = &url[query_start + 1..];
    for pair in query.split('&') {
        let mut parts = pair.splitn(2, '=');
        if matches!(parts.next(), Some("mcp_url")) {
            if let Some(value) = parts.next() {
                return percent_decode(value);
            }
        }
    }

    url.to_string()
}

#[must_use]
pub fn mcp_transport_display_name(transport: McpTransport) -> &'static str {
    match transport {
        McpTransport::Stdio => "stdio",
        McpTransport::Sse => "sse",
        McpTransport::Http => "http",
        McpTransport::Ws => "ws",
        McpTransport::Sdk => "sdk",
        McpTransport::SimcoeAiProxy => "simcoe-ai-proxy",
    }
}

#[must_use]
pub fn mcp_client_transport_display_name(transport: &McpClientTransport) -> &'static str {
    match transport {
        McpClientTransport::Stdio(_) => "stdio",
        McpClientTransport::Sse(_) => "sse",
        McpClientTransport::Http(_) => "http",
        McpClientTransport::WebSocket(_) => "ws",
        McpClientTransport::Sdk(_) => "sdk",
        McpClientTransport::SimcoeAiProxy(_) => "simcoe-ai-proxy",
    }
}

#[must_use]
pub fn unsupported_live_mcp_execution_reason(transport: &McpClientTransport) -> Option<String> {
    match transport {
        McpClientTransport::Stdio(_) => None,
        McpClientTransport::Sse(remote) => {
            remote.headers_helper.as_ref().map(|_| {
                String::from(
                    "sse transport with headersHelper is not executed by the Rust MCP runtime yet",
                )
            })
        }
        McpClientTransport::Http(remote) => {
            remote.headers_helper.as_ref().map(|_| {
                String::from(
                    "http transport with headersHelper is not executed by the Rust MCP runtime yet",
                )
            })
        }
        McpClientTransport::WebSocket(remote) => {
            remote.headers_helper.as_ref().map(|_| {
                String::from(
                    "ws transport with headersHelper is not executed by the Rust MCP runtime yet",
                )
            })
        }
        McpClientTransport::Sdk(sdk) => Some(format!(
            "sdk transport is not executed by the Rust MCP runtime yet; SDK server `{}` needs the upstream SDK adapter path, which is not present in the Rust port",
            sdk.name
        )),
        McpClientTransport::SimcoeAiProxy(proxy) => Some(format!(
            "simcoe-ai-proxy transport is not executed by the Rust MCP runtime yet; proxy `{}` targets `{}`, but the upstream proxy websocket/session adapter path (`remote/SessionsWebSocket.ts` / `remote/sdkMessageAdapter.ts`) is not ported in Rust",
            proxy.id,
            unwrap_ccr_proxy_url(&proxy.url)
        )),
    }
}

#[must_use]
pub fn mcp_server_signature(config: &McpServerConfig) -> Option<String> {
    match config {
        McpServerConfig::Stdio(config) => {
            let mut command = vec![config.command.clone()];
            command.extend(config.args.clone());
            Some(format!("stdio:{}", render_command_signature(&command)))
        }
        McpServerConfig::Sse(config) | McpServerConfig::Http(config) => {
            Some(format!("url:{}", unwrap_ccr_proxy_url(&config.url)))
        }
        McpServerConfig::Ws(config) => Some(format!("url:{}", unwrap_ccr_proxy_url(&config.url))),
        McpServerConfig::SimcoeAiProxy(config) => {
            Some(format!("url:{}", unwrap_ccr_proxy_url(&config.url)))
        }
        McpServerConfig::Sdk(_) => None,
    }
}

#[must_use]
pub fn scoped_mcp_config_hash(config: &ScopedMcpServerConfig) -> String {
    let rendered = match &config.config {
        McpServerConfig::Stdio(stdio) => format!(
            "stdio|{}|{}|{}",
            stdio.command,
            render_command_signature(&stdio.args),
            render_env_signature(&stdio.env)
        ),
        McpServerConfig::Sse(remote) => format!(
            "sse|{}|{}|{}|{}",
            remote.url,
            render_env_signature(&remote.headers),
            remote.headers_helper.as_deref().unwrap_or(""),
            render_oauth_signature(remote.oauth.as_ref())
        ),
        McpServerConfig::Http(remote) => format!(
            "http|{}|{}|{}|{}",
            remote.url,
            render_env_signature(&remote.headers),
            remote.headers_helper.as_deref().unwrap_or(""),
            render_oauth_signature(remote.oauth.as_ref())
        ),
        McpServerConfig::Ws(ws) => format!(
            "ws|{}|{}|{}",
            ws.url,
            render_env_signature(&ws.headers),
            ws.headers_helper.as_deref().unwrap_or("")
        ),
        McpServerConfig::Sdk(sdk) => format!("sdk|{}", sdk.name),
        McpServerConfig::SimcoeAiProxy(proxy) => {
            format!("simcoeai-proxy|{}|{}", proxy.url, proxy.id)
        }
    };
    stable_hex_hash(&rendered)
}

fn render_command_signature(command: &[String]) -> String {
    let escaped = command
        .iter()
        .map(|part| part.replace('\\', "\\\\").replace('|', "\\|"))
        .collect::<Vec<_>>();
    format!("[{}]", escaped.join("|"))
}

fn render_env_signature(map: &std::collections::BTreeMap<String, String>) -> String {
    map.iter()
        .map(|(key, value)| format!("{key}={value}"))
        .collect::<Vec<_>>()
        .join(";")
}

fn render_oauth_signature(oauth: Option<&crate::config::McpOAuthConfig>) -> String {
    oauth.map_or_else(String::new, |oauth| {
        format!(
            "{}|{}|{}|{}",
            oauth.client_id.as_deref().unwrap_or(""),
            oauth
                .callback_port
                .map_or_else(String::new, |port| port.to_string()),
            oauth.auth_server_metadata_url.as_deref().unwrap_or(""),
            oauth.xaa.map_or_else(String::new, |flag| flag.to_string())
        )
    })
}

fn stable_hex_hash(value: &str) -> String {
    let mut hash = 0xcbf2_9ce4_8422_2325_u64;
    for byte in value.as_bytes() {
        hash ^= u64::from(*byte);
        hash = hash.wrapping_mul(0x0100_0000_01b3);
    }
    format!("{hash:016x}")
}

fn collapse_underscores(value: &str) -> String {
    let mut collapsed = String::with_capacity(value.len());
    let mut last_was_underscore = false;
    for ch in value.chars() {
        if ch == '_' {
            if !last_was_underscore {
                collapsed.push(ch);
            }
            last_was_underscore = true;
        } else {
            collapsed.push(ch);
            last_was_underscore = false;
        }
    }
    collapsed
}

fn percent_decode(value: &str) -> String {
    let bytes = value.as_bytes();
    let mut decoded = Vec::with_capacity(bytes.len());
    let mut index = 0;
    while index < bytes.len() {
        match bytes[index] {
            b'%' if index + 2 < bytes.len() => {
                let hex = &value[index + 1..index + 3];
                if let Ok(byte) = u8::from_str_radix(hex, 16) {
                    decoded.push(byte);
                    index += 3;
                    continue;
                }
                decoded.push(bytes[index]);
                index += 1;
            }
            b'+' => {
                decoded.push(b' ');
                index += 1;
            }
            byte => {
                decoded.push(byte);
                index += 1;
            }
        }
    }
    String::from_utf8_lossy(&decoded).into_owned()
}

#[cfg(test)]
mod tests {
    use std::collections::BTreeMap;

    use crate::config::{
        ConfigSource, McpRemoteServerConfig, McpServerConfig, McpStdioServerConfig, McpTransport,
        McpWebSocketServerConfig, ScopedMcpServerConfig,
    };
    use crate::mcp_client::{
        McpClientAuth, McpClientTransport, McpRemoteTransport, McpSdkTransport,
        McpSimcoeAiProxyTransport,
    };

    use super::{
        mcp_client_transport_display_name, mcp_server_signature, mcp_tool_name,
        mcp_transport_display_name, normalize_name_for_mcp, scoped_mcp_config_hash,
        unsupported_live_mcp_execution_reason, unwrap_ccr_proxy_url,
    };

    #[test]
    fn normalizes_server_names_for_mcp_tooling() {
        assert_eq!(normalize_name_for_mcp("github.com"), "github_com");
        assert_eq!(normalize_name_for_mcp("tool name!"), "tool_name_");
        assert_eq!(
            normalize_name_for_mcp("simcoe.ai Example   Server!!"),
            "simcoe_ai_Example_Server"
        );
        assert_eq!(
            mcp_tool_name("simcoe.ai Example Server", "weather tool"),
            "mcp__simcoe_ai_Example_Server__weather_tool"
        );
    }

    #[test]
    fn unwraps_ccr_proxy_urls_for_signature_matching() {
        let wrapped = "https://api.anthropic.com/v2/session_ingress/shttp/mcp/123?mcp_url=https%3A%2F%2Fvendor.example%2Fmcp&other=1";
        assert_eq!(unwrap_ccr_proxy_url(wrapped), "https://vendor.example/mcp");
        assert_eq!(
            unwrap_ccr_proxy_url("https://vendor.example/mcp"),
            "https://vendor.example/mcp"
        );
    }

    #[test]
    fn computes_signatures_for_stdio_and_remote_servers() {
        let stdio = McpServerConfig::Stdio(McpStdioServerConfig {
            command: "uvx".to_string(),
            args: vec!["mcp-server".to_string()],
            env: BTreeMap::from([("TOKEN".to_string(), "secret".to_string())]),
        });
        assert_eq!(
            mcp_server_signature(&stdio),
            Some("stdio:[uvx|mcp-server]".to_string())
        );

        let remote = McpServerConfig::Ws(McpWebSocketServerConfig {
            url: "https://api.anthropic.com/v2/ccr-sessions/1?mcp_url=wss%3A%2F%2Fvendor.example%2Fmcp".to_string(),
            headers: BTreeMap::new(),
            headers_helper: None,
        });
        assert_eq!(
            mcp_server_signature(&remote),
            Some("url:wss://vendor.example/mcp".to_string())
        );
    }

    #[test]
    fn scoped_hash_ignores_scope_but_tracks_config_content() {
        let base_config = McpServerConfig::Http(McpRemoteServerConfig {
            url: "https://vendor.example/mcp".to_string(),
            headers: BTreeMap::from([("Authorization".to_string(), "Bearer token".to_string())]),
            headers_helper: Some("helper.sh".to_string()),
            oauth: None,
        });
        let user = ScopedMcpServerConfig {
            scope: ConfigSource::User,
            config: base_config.clone(),
        };
        let local = ScopedMcpServerConfig {
            scope: ConfigSource::Local,
            config: base_config,
        };
        assert_eq!(
            scoped_mcp_config_hash(&user),
            scoped_mcp_config_hash(&local)
        );

        let changed = ScopedMcpServerConfig {
            scope: ConfigSource::Local,
            config: McpServerConfig::Http(McpRemoteServerConfig {
                url: "https://vendor.example/v2/mcp".to_string(),
                headers: BTreeMap::new(),
                headers_helper: None,
                oauth: None,
            }),
        };
        assert_ne!(
            scoped_mcp_config_hash(&user),
            scoped_mcp_config_hash(&changed)
        );
    }

    #[test]
    fn reports_shared_mcp_transport_labels() {
        assert_eq!(
            mcp_transport_display_name(McpTransport::SimcoeAiProxy),
            "simcoe-ai-proxy"
        );
        assert_eq!(
            mcp_client_transport_display_name(&McpClientTransport::SimcoeAiProxy(
                McpSimcoeAiProxyTransport {
                    url: "https://api.anthropic.com/v2/ccr-sessions/1?mcp_url=wss%3A%2F%2Fvendor.example%2Fmcp".to_string(),
                    id: "proxy-123".to_string(),
                }
            )),
            "simcoe-ai-proxy"
        );
    }

    #[test]
    fn reports_shared_live_mcp_execution_blockers() {
        let supported = McpClientTransport::Http(McpRemoteTransport {
            url: "https://vendor.example/mcp".to_string(),
            headers: BTreeMap::new(),
            headers_helper: None,
            auth: McpClientAuth::None,
        });
        assert_eq!(unsupported_live_mcp_execution_reason(&supported), None);

        let blocked_ws = McpClientTransport::WebSocket(McpRemoteTransport {
            url: "wss://vendor.example/mcp".to_string(),
            headers: BTreeMap::new(),
            headers_helper: Some("helper.sh".to_string()),
            auth: McpClientAuth::None,
        });
        assert_eq!(
            unsupported_live_mcp_execution_reason(&blocked_ws),
            Some(
                "ws transport with headersHelper is not executed by the Rust MCP runtime yet"
                    .to_string()
            )
        );

        let blocked_sdk = McpClientTransport::Sdk(McpSdkTransport {
            name: "sdk-adapter".to_string(),
        });
        assert!(unsupported_live_mcp_execution_reason(&blocked_sdk)
            .expect("sdk blocker")
            .contains("SDK server `sdk-adapter` needs the upstream SDK adapter path"));

        let blocked_proxy = McpClientTransport::SimcoeAiProxy(McpSimcoeAiProxyTransport {
            url: "https://api.anthropic.com/v2/ccr-sessions/1?mcp_url=wss%3A%2F%2Fvendor.example%2Fmcp".to_string(),
            id: "proxy-123".to_string(),
        });
        let proxy_reason =
            unsupported_live_mcp_execution_reason(&blocked_proxy).expect("proxy blocker");
        assert!(proxy_reason.contains("simcoe-ai-proxy transport is not executed"));
        assert!(proxy_reason.contains("proxy `proxy-123` targets `wss://vendor.example/mcp`"));
    }
}
