use std::collections::BTreeMap;
use std::env;

use runtime::{
    inherited_upstream_proxy_env, upstream_proxy_live_transport_status,
    upstream_proxy_websocket_probe_from_env_map, AssistantEvent, TokenUsage, TurnSummary,
    UpstreamProxyBootstrap,
};
use serde_json::{json, Value};

pub(crate) fn build_turn_transport(summary: &TurnSummary, provider: &str) -> Value {
    let metadata = build_turn_transport_metadata(provider);
    json!({
        "kind": metadata["kind"].clone(),
        "active_transport_kind": metadata["active_transport_kind"].clone(),
        "provider_runtime": metadata["provider_runtime"].clone(),
        "capabilities": metadata["capabilities"].clone(),
        "bootstrap": metadata["bootstrap"].clone(),
        "events": build_turn_transport_events(summary),
    })
}

pub(crate) fn build_turn_transport_metadata(provider: &str) -> Value {
    let env_map = env::vars().collect::<BTreeMap<String, String>>();
    build_turn_transport_metadata_from_env_map(&env_map, provider)
}

pub(crate) fn build_turn_transport_events(summary: &TurnSummary) -> Vec<Value> {
    structured_turn_events(summary)
}

fn build_turn_transport_from_env_map(
    summary: &TurnSummary,
    env_map: &BTreeMap<String, String>,
    provider: &str,
) -> Value {
    let metadata = build_turn_transport_metadata_from_env_map(env_map, provider);
    json!({
        "kind": metadata["kind"].clone(),
        "active_transport_kind": metadata["active_transport_kind"].clone(),
        "provider_runtime": metadata["provider_runtime"].clone(),
        "capabilities": metadata["capabilities"].clone(),
        "bootstrap": metadata["bootstrap"].clone(),
        "events": build_turn_transport_events(summary),
    })
}

pub(crate) fn build_provider_runtime_metadata(provider: &str) -> Value {
    let (family, request_format) = match provider {
        "simcoe" | "anthropic" => ("anthropic-compatible", "messages-v1"),
        "openai" | "ollama" => ("openai-compatible", "chat-completions"),
        _ => ("custom", "unknown"),
    };

    json!({
        "provider": provider,
        "family": family,
        "request_format": request_format,
        "streaming_protocol": "sse",
        "buffered_fallback_supported": true,
    })
}

fn build_turn_transport_metadata_from_env_map(
    env_map: &BTreeMap<String, String>,
    provider: &str,
) -> Value {
    let bootstrap = UpstreamProxyBootstrap::from_env_map(env_map);
    let websocket_probe = upstream_proxy_websocket_probe_from_env_map(env_map);
    let ready = bootstrap.should_enable();
    let live_remote_transport = upstream_proxy_live_transport_status(&bootstrap, &websocket_probe);
    let inherited = inherited_upstream_proxy_env(env_map);
    let inherited_keys = inherited.keys().cloned().collect::<Vec<_>>();
    let missing = bootstrap.missing_requirements();
    let ws_url = (!bootstrap.remote.base_url.is_empty()).then(|| bootstrap.ws_url());

    json!({
        "kind": "provider-direct",
        "active_transport_kind": "api-stream",
        "provider_runtime": build_provider_runtime_metadata(provider),
        "capabilities": {
            "structured_local_events": true,
            "live_remote_transport": false,
            "live_remote_transport_kind": "upstream-proxy-websocket",
            "live_remote_transport_ready": live_remote_transport.ready,
            "live_remote_transport_path_ready": live_remote_transport.path_ready,
            "live_remote_transport_selected": false,
            "live_remote_transport_blocker_kind": live_remote_transport.blocker_kind,
            "live_remote_transport_blocker_detail": live_remote_transport.blocker_detail,
        },
        "bootstrap": {
            "remote_enabled": bootstrap.remote.enabled,
            "session_id": bootstrap.remote.session_id.clone(),
            "base_url": non_empty_string(&bootstrap.remote.base_url),
            "upstream_proxy_enabled": bootstrap.upstream_proxy_enabled,
            "ready": ready,
            "ws_url": ws_url,
            "websocket_probe": {
                "requested": websocket_probe.requested,
                "attempted": websocket_probe.attempted,
                "reachable": websocket_probe.reachable,
                "status": websocket_probe.status,
                "detail": websocket_probe.detail,
            },
            "token_path": bootstrap.token_path.display().to_string(),
            "token_present": bootstrap.token.is_some(),
            "ca_bundle_path": bootstrap.ca_bundle_path.display().to_string(),
            "system_ca_path": bootstrap.system_ca_path.display().to_string(),
            "inherited_proxy_env_count": inherited.len(),
            "inherited_proxy_env_keys": inherited_keys,
            "missing": missing,
        },
    })
}

fn structured_turn_events(summary: &TurnSummary) -> Vec<Value> {
    let mut events = Vec::new();

    for (assistant_index, turn) in summary.transport_trace.iter().enumerate() {
        events.push(json!({
            "type": "message_start",
            "assistant_index": assistant_index,
            "role": "assistant",
        }));

        for event in &turn.events {
            match event {
                AssistantEvent::TextDelta(text) => {
                    if !text.is_empty() {
                        events.push(json!({
                            "type": "text",
                            "assistant_index": assistant_index,
                            "text": text,
                        }));
                    }
                }
                AssistantEvent::ToolUse { id, name, input } => {
                    events.push(json!({
                        "type": "tool_use",
                        "assistant_index": assistant_index,
                        "id": id,
                        "name": name,
                        "input": parse_json_value(input),
                    }));
                }
                AssistantEvent::Usage(usage) => {
                    events.push(usage_event(assistant_index, *usage));
                }
                AssistantEvent::MessageStop => {
                    events.push(json!({
                        "type": "message_stop",
                        "assistant_index": assistant_index,
                    }));
                }
            }
        }

        for result in &turn.tool_results {
            events.push(json!({
                "type": "tool_result",
                "assistant_index": assistant_index,
                "tool_use_id": result.tool_use_id,
                "tool_name": result.tool_name,
                "output": parse_json_value(&result.output),
                "is_error": result.is_error,
            }));
        }
    }

    events
}

fn usage_event(assistant_index: usize, usage: TokenUsage) -> Value {
    json!({
        "type": "usage",
        "assistant_index": assistant_index,
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "cache_creation_input_tokens": usage.cache_creation_input_tokens,
        "cache_read_input_tokens": usage.cache_read_input_tokens,
    })
}

fn parse_json_value(value: &str) -> Value {
    serde_json::from_str(value).unwrap_or_else(|_| Value::String(value.to_string()))
}

fn non_empty_string(value: &str) -> Option<String> {
    (!value.is_empty()).then(|| value.to_string())
}

#[cfg(test)]
mod tests {
    use super::{
        build_turn_transport_events, build_turn_transport_from_env_map,
        build_turn_transport_metadata_from_env_map, structured_turn_events,
    };
    use runtime::{
        AssistantEvent, AssistantTurnTrace, ContentBlock, ConversationMessage, TokenUsage,
        ToolResultTrace, TurnSummary,
    };
    use serde_json::json;
    use std::collections::BTreeMap;
    use std::fs;

    fn sample_summary() -> TurnSummary {
        TurnSummary {
            assistant_messages: vec![
                ConversationMessage::assistant_with_usage(
                    vec![
                        ContentBlock::Text {
                            text: "Inspecting Cargo.toml".to_string(),
                        },
                        ContentBlock::ToolUse {
                            id: "toolu_1".to_string(),
                            name: "read_file".to_string(),
                            input: "{\"path\":\"Cargo.toml\"}".to_string(),
                        },
                    ],
                    Some(TokenUsage {
                        input_tokens: 3,
                        output_tokens: 1,
                        cache_creation_input_tokens: 0,
                        cache_read_input_tokens: 0,
                    }),
                ),
                ConversationMessage::assistant_with_usage(
                    vec![ContentBlock::Text {
                        text: "Done".to_string(),
                    }],
                    Some(TokenUsage {
                        input_tokens: 3,
                        output_tokens: 4,
                        cache_creation_input_tokens: 0,
                        cache_read_input_tokens: 0,
                    }),
                ),
            ],
            tool_results: vec![ConversationMessage::tool_result(
                "toolu_1",
                "read_file",
                "{\"content\":\"[package]\"}",
                false,
            )],
            transport_trace: vec![
                AssistantTurnTrace {
                    events: vec![
                        AssistantEvent::TextDelta("Inspect".to_string()),
                        AssistantEvent::TextDelta("ing Cargo.toml".to_string()),
                        AssistantEvent::ToolUse {
                            id: "toolu_1".to_string(),
                            name: "read_file".to_string(),
                            input: "{\"path\":\"Cargo.toml\"}".to_string(),
                        },
                        AssistantEvent::Usage(TokenUsage {
                            input_tokens: 3,
                            output_tokens: 1,
                            cache_creation_input_tokens: 0,
                            cache_read_input_tokens: 0,
                        }),
                        AssistantEvent::MessageStop,
                    ],
                    tool_results: vec![ToolResultTrace {
                        tool_use_id: "toolu_1".to_string(),
                        tool_name: "read_file".to_string(),
                        output: "{\"content\":\"[package]\"}".to_string(),
                        is_error: false,
                    }],
                },
                AssistantTurnTrace {
                    events: vec![
                        AssistantEvent::TextDelta("Done".to_string()),
                        AssistantEvent::Usage(TokenUsage {
                            input_tokens: 3,
                            output_tokens: 4,
                            cache_creation_input_tokens: 0,
                            cache_read_input_tokens: 0,
                        }),
                        AssistantEvent::MessageStop,
                    ],
                    tool_results: Vec::new(),
                },
            ],
            iterations: 2,
            usage: TokenUsage {
                input_tokens: 6,
                output_tokens: 5,
                cache_creation_input_tokens: 0,
                cache_read_input_tokens: 0,
            },
            auto_compaction: None,
        }
    }

    #[test]
    fn structured_turn_events_preserve_assistant_and_tool_order() {
        let events = structured_turn_events(&sample_summary());
        let event_types = events
            .iter()
            .map(|event| event["type"].as_str().expect("event type"))
            .collect::<Vec<_>>();

        assert_eq!(
            event_types,
            vec![
                "message_start",
                "text",
                "text",
                "tool_use",
                "usage",
                "message_stop",
                "tool_result",
                "message_start",
                "text",
                "usage",
                "message_stop",
            ]
        );
        assert_eq!(events[1]["text"], json!("Inspect"));
        assert_eq!(events[2]["text"], json!("ing Cargo.toml"));
        assert_eq!(events[3]["input"], json!({"path": "Cargo.toml"}));
        assert_eq!(events[6]["tool_use_id"], json!("toolu_1"));
        assert_eq!(events[6]["output"], json!({"content": "[package]"}));
        assert_eq!(events[6]["assistant_index"], json!(0));
    }

    #[test]
    fn build_turn_transport_reports_upstream_proxy_bootstrap() {
        let token_dir = std::env::temp_dir().join(format!(
            "claw-transport-test-{}-{}",
            std::process::id(),
            std::thread::current().name().unwrap_or("main")
        ));
        let _ = fs::remove_dir_all(&token_dir);
        fs::create_dir_all(&token_dir).expect("create token dir");
        let token_path = token_dir.join("session_token");
        fs::write(&token_path, "token-value\n").expect("write session token");

        let env_map = BTreeMap::from([
            ("SIMCOE_AI_REMOTE".to_string(), "true".to_string()),
            (
                "SIMCOE_AI_REMOTE_SESSION_ID".to_string(),
                "session-123".to_string(),
            ),
            (
                "SIMCOE_AI_BASE_URL".to_string(),
                "https://remote.test".to_string(),
            ),
            ("CCR_UPSTREAM_PROXY_ENABLED".to_string(), "true".to_string()),
            (
                "CCR_SESSION_TOKEN_PATH".to_string(),
                token_path.display().to_string(),
            ),
        ]);

        let transport = build_turn_transport_from_env_map(&sample_summary(), &env_map, "openai");

        assert_eq!(transport["kind"], json!("provider-direct"));
        assert_eq!(transport["active_transport_kind"], json!("api-stream"));
        assert_eq!(transport["provider_runtime"]["provider"], json!("openai"));
        assert_eq!(
            transport["provider_runtime"]["family"],
            json!("openai-compatible")
        );
        assert_eq!(
            transport["provider_runtime"]["request_format"],
            json!("chat-completions")
        );
        assert_eq!(
            transport["capabilities"]["live_remote_transport"],
            json!(false)
        );
        assert_eq!(
            transport["capabilities"]["live_remote_transport_kind"],
            json!("upstream-proxy-websocket")
        );
        assert_eq!(
            transport["capabilities"]["live_remote_transport_ready"],
            json!(false)
        );
        assert_eq!(
            transport["capabilities"]["live_remote_transport_path_ready"],
            json!(true)
        );
        assert_eq!(
            transport["capabilities"]["live_remote_transport_selected"],
            json!(false)
        );
        assert_eq!(
            transport["capabilities"]["live_remote_transport_blocker_kind"],
            json!("adapter-not-ported")
        );
        assert!(
            transport["capabilities"]["live_remote_transport_blocker_detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("not ported in Rust"))
        );
        assert_eq!(transport["bootstrap"]["remote_enabled"], json!(true));
        assert_eq!(transport["bootstrap"]["ready"], json!(true));
        assert_eq!(
            transport["bootstrap"]["websocket_probe"]["status"],
            json!("skipped")
        );
        assert_eq!(transport["bootstrap"]["token_present"], json!(true));
        assert_eq!(transport["bootstrap"]["missing"], json!([]));
        assert_eq!(
            transport["bootstrap"]["ws_url"],
            json!("wss://remote.test/v1/code/upstreamproxy/ws")
        );

        let _ = fs::remove_dir_all(token_dir);
    }

    #[test]
    fn build_turn_transport_metadata_reports_local_when_remote_is_unavailable() {
        let metadata = build_turn_transport_metadata_from_env_map(&BTreeMap::new(), "simcoe");

        assert_eq!(metadata["kind"], json!("provider-direct"));
        assert_eq!(metadata["active_transport_kind"], json!("api-stream"));
        assert_eq!(metadata["provider_runtime"]["provider"], json!("simcoe"));
        assert_eq!(
            metadata["provider_runtime"]["family"],
            json!("anthropic-compatible")
        );
        assert_eq!(
            metadata["capabilities"]["live_remote_transport_kind"],
            json!("upstream-proxy-websocket")
        );
        assert_eq!(
            metadata["capabilities"]["live_remote_transport_ready"],
            json!(false)
        );
        assert_eq!(
            metadata["capabilities"]["live_remote_transport_path_ready"],
            json!(false)
        );
        assert_eq!(
            metadata["capabilities"]["live_remote_transport_selected"],
            json!(false)
        );
        assert_eq!(
            metadata["capabilities"]["live_remote_transport_blocker_kind"],
            json!("disabled")
        );
        assert!(
            metadata["capabilities"]["live_remote_transport_blocker_detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("SIMCOE_AI_REMOTE disabled"))
        );
        assert_eq!(metadata["bootstrap"]["remote_enabled"], json!(false));
        assert_eq!(metadata["bootstrap"]["ready"], json!(false));
        assert_eq!(
            metadata["bootstrap"]["websocket_probe"]["status"],
            json!("skipped")
        );
        assert_eq!(metadata["bootstrap"]["token_present"], json!(false));
        assert_eq!(metadata["bootstrap"]["inherited_proxy_env_count"], json!(0));
        assert_eq!(
            metadata["bootstrap"]["missing"],
            json!([
                "SIMCOE_AI_REMOTE disabled",
                "missing remote session id",
                "missing base URL",
                "CCR_UPSTREAM_PROXY_ENABLED disabled",
                "missing session token",
            ])
        );
    }

    #[test]
    fn build_turn_transport_metadata_reports_inherited_proxy_env() {
        let env_map = BTreeMap::from([
            (
                "HTTPS_PROXY".to_string(),
                "http://127.0.0.1:8080".to_string(),
            ),
            (
                "SSL_CERT_FILE".to_string(),
                "/tmp/ca-bundle.crt".to_string(),
            ),
            ("NO_PROXY".to_string(), "localhost".to_string()),
            (
                "SIMCOE_AI_BASE_URL".to_string(),
                "https://remote.test".to_string(),
            ),
        ]);

        let metadata = build_turn_transport_metadata_from_env_map(&env_map, "anthropic");

        assert_eq!(metadata["bootstrap"]["ready"], json!(false));
        assert_eq!(metadata["provider_runtime"]["provider"], json!("anthropic"));
        assert_eq!(
            metadata["bootstrap"]["ws_url"],
            json!("wss://remote.test/v1/code/upstreamproxy/ws")
        );
        assert_eq!(metadata["bootstrap"]["inherited_proxy_env_count"], json!(3));
        assert_eq!(
            metadata["bootstrap"]["inherited_proxy_env_keys"],
            json!(["HTTPS_PROXY", "NO_PROXY", "SSL_CERT_FILE"])
        );
    }

    #[test]
    fn build_turn_transport_metadata_downgrades_remote_readiness_when_probe_fails() {
        let token_dir = std::env::temp_dir().join("claw-transport-probe-failure");
        let token_path = token_dir.join("session_token");
        fs::create_dir_all(&token_dir).expect("create temp dir");
        fs::write(&token_path, "token-value\n").expect("write session token");
        let unused_port = std::net::TcpListener::bind("127.0.0.1:0")
            .expect("bind port")
            .local_addr()
            .expect("local addr")
            .port();

        let env_map = BTreeMap::from([
            ("SIMCOE_AI_REMOTE".to_string(), "1".to_string()),
            (
                "SIMCOE_AI_REMOTE_SESSION_ID".to_string(),
                "session-123".to_string(),
            ),
            (
                "SIMCOE_AI_BASE_URL".to_string(),
                format!("http://127.0.0.1:{unused_port}"),
            ),
            ("CCR_UPSTREAM_PROXY_ENABLED".to_string(), "true".to_string()),
            (
                "CCR_SESSION_TOKEN_PATH".to_string(),
                token_path.display().to_string(),
            ),
            ("CCR_UPSTREAM_PROXY_PROBE".to_string(), "1".to_string()),
        ]);

        let metadata = build_turn_transport_metadata_from_env_map(&env_map, "simcoe");

        assert_eq!(metadata["bootstrap"]["ready"], json!(true));
        assert_eq!(
            metadata["bootstrap"]["websocket_probe"]["status"],
            json!("failed")
        );
        assert_eq!(
            metadata["capabilities"]["live_remote_transport_ready"],
            json!(false)
        );
        assert_eq!(
            metadata["capabilities"]["live_remote_transport_path_ready"],
            json!(false)
        );
        assert_eq!(
            metadata["capabilities"]["live_remote_transport_blocker_kind"],
            json!("probe-failed")
        );
        assert!(
            metadata["capabilities"]["live_remote_transport_blocker_detail"]
                .as_str()
                .is_some_and(|detail| detail.contains("failed to connect"))
        );

        let _ = fs::remove_dir_all(token_dir);
    }

    #[test]
    fn build_turn_transport_events_matches_structured_event_list() {
        let expected = structured_turn_events(&sample_summary());
        let actual = build_turn_transport_events(&sample_summary());
        assert_eq!(actual, expected);
    }
}
