from __future__ import annotations

import json
from pathlib import Path

from orchestration_inspect import (
    describe_agent_shell_session,
    describe_agent_shell_sessions,
    describe_context_providers,
    describe_execution_results,
    describe_hooks,
    summarize_execution_results,
)
from runtime_contracts import (
    EXECUTION_STATUS_SUCCEEDED,
    EXECUTION_SUBJECT_CONTEXT_PROVIDER,
    EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
    EXECUTION_SUBJECT_ROUTE,
    build_execution_envelope,
)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def _agent_shell_cfg(tmp_path) -> dict:
    root_dir = tmp_path / "agent_shell"
    return {
        "agent_shell": {
            "enabled": True,
            "root_dir": str(root_dir),
            "sessions_dir": str(root_dir / "sessions"),
            "transcripts_dir": str(root_dir / "transcripts"),
        }
    }


def test_describe_hooks_summarizes_rules() -> None:
    cfg = {
        "hooks": {
            "enabled": True,
            "rules": [
                {
                    "name": "annotate_route",
                    "stage": "post_route",
                    "action": "annotate",
                    "fields": {"policy": "grounded"},
                }
            ],
        }
    }

    summary = describe_hooks(cfg)

    assert summary["enabled"] is True
    assert summary["rule_count"] == 1
    assert summary["by_stage"]["post_route"] == 1
    assert summary["by_action"]["annotate"] == 1


def test_describe_context_providers_reports_order_and_active() -> None:
    cfg = {
        "retrieval": {"enabled": True},
        "memory": {"enabled": True},
        "context_providers": {"order": ["memory", "retrieval"], "max_workers": 4},
    }

    summary = describe_context_providers(cfg)

    assert summary["order"] == ["memory", "retrieval"]
    assert summary["active"] == ["memory", "retrieval"]
    assert summary["max_workers"] == 4


def test_summarize_execution_results_prefers_top_level_summary() -> None:
    summary = summarize_execution_results(
        {
            "execution": {
                "schema_version": 1,
                "summary": {"total": 3, "by_status": {"succeeded": 3}},
            }
        }
    )

    assert summary["source"] == "top_level_execution_summary"
    assert summary["summary"]["total"] == 3


def test_describe_execution_results_reads_saved_results(tmp_path) -> None:
    results_path = tmp_path / "results.json"
    results_path.write_text(
        json.dumps(
            {
                "execution": {
                    "schema_version": 1,
                    "summary": {"total": 2, "by_subject_type": {"route": 2}},
                }
            }
        ),
        encoding="utf-8",
    )

    summary = describe_execution_results(
        {"evaluation": {"results_path": str(results_path)}},
    )

    assert summary["results_path"] == str(results_path.resolve())
    assert summary["summary"]["by_subject_type"]["route"] == 2


def test_describe_agent_shell_sessions_lists_saved_summaries(tmp_path) -> None:
    cfg = _agent_shell_cfg(tmp_path)
    sessions_dir = tmp_path / "agent_shell" / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)

    (sessions_dir / "agent-shell-a.json").write_text(
        json.dumps(
            {
                "session_id": "agent-shell-a",
                "created_at": "2026-04-01T09:00:00Z",
                "updated_at": "2026-04-01T09:10:00Z",
                "provider": "ollama",
                "model": "simcoe",
                "turn_count": 1,
                "last_route": "text",
                "last_runtime_owner": "text",
                "route_counts": {"text": 1},
            }
        ),
        encoding="utf-8",
    )
    (sessions_dir / "agent-shell-b.json").write_text(
        json.dumps(
            {
                "session_id": "agent-shell-b",
                "created_at": "2026-04-01T10:00:00Z",
                "updated_at": "2026-04-01T10:20:00Z",
                "provider": "ollama",
                "model": "simcoe",
                "turn_count": 2,
                "last_route": "deterministic_tool",
                "last_runtime_owner": "geometry_rules",
                "route_counts": {"text": 1, "deterministic_tool": 1},
            }
        ),
        encoding="utf-8",
    )

    payload = describe_agent_shell_sessions(cfg)

    assert payload["session_count"] == 2
    assert [session["session_id"] for session in payload["sessions"]] == [
        "agent-shell-b",
        "agent-shell-a",
    ]
    assert payload["sessions"][0]["route_counts"]["deterministic_tool"] == 1


def test_describe_agent_shell_session_reconstructs_execution_summary(tmp_path) -> None:
    cfg = _agent_shell_cfg(tmp_path)
    sessions_dir = tmp_path / "agent_shell" / "sessions"
    transcripts_dir = tmp_path / "agent_shell" / "transcripts"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    session_id = "agent-shell-abc"
    transcript_path = transcripts_dir / f"{session_id}.jsonl"
    route_text = build_execution_envelope(
        EXECUTION_SUBJECT_ROUTE,
        "text",
        EXECUTION_STATUS_SUCCEEDED,
        owner="text",
    )
    provider_memory = build_execution_envelope(
        EXECUTION_SUBJECT_CONTEXT_PROVIDER,
        "memory",
        EXECUTION_STATUS_SUCCEEDED,
        owner="memory",
    )
    route_tool = build_execution_envelope(
        EXECUTION_SUBJECT_ROUTE,
        "deterministic_tool",
        EXECUTION_STATUS_SUCCEEDED,
        owner="geometry_rules",
    )
    deterministic_tool = build_execution_envelope(
        EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
        "estimate_lookup",
        EXECUTION_STATUS_SUCCEEDED,
        owner="geometry_rules",
    )

    _write_jsonl(
        transcript_path,
        [
            {
                "turn_id": "turn-1",
                "turn_index": 0,
                "route": "text",
                "runtime_owner": "text",
                "user": {"prompt": "Explain grounding and bonding."},
                "assistant": {"response": "Grounding answer"},
                "error": None,
                "execution": {
                    "schema_version": 1,
                    "route": route_text,
                    "context_providers": [provider_memory],
                    "deterministic_tool": None,
                },
            },
            {
                "turn_id": "turn-2",
                "turn_index": 1,
                "route": "deterministic_tool",
                "runtime_owner": "geometry_rules",
                "user": {"prompt": "Find the estimate lookup for EMT conduit."},
                "assistant": {"response": "estimate_lookup returned 1 result(s)."},
                "error": None,
                "execution": {
                    "schema_version": 1,
                    "route": route_tool,
                    "context_providers": [],
                    "deterministic_tool": deterministic_tool,
                },
            },
        ],
    )
    (sessions_dir / f"{session_id}.json").write_text(
        json.dumps(
            {
                "session_id": session_id,
                "created_at": "2026-04-01T09:00:00Z",
                "updated_at": "2026-04-01T09:10:00Z",
                "provider": "ollama",
                "model": "simcoe",
                "turn_count": 2,
                "route_counts": {"text": 1, "deterministic_tool": 1},
                "last_route": "deterministic_tool",
                "last_runtime_owner": "geometry_rules",
                "transcript_path": str(transcript_path.resolve()),
            }
        ),
        encoding="utf-8",
    )

    payload = describe_agent_shell_session(cfg, session_id, tail=1)

    assert payload["session"]["turn_count"] == 2
    assert payload["recent_turns"][0]["turn_id"] == "turn-2"
    assert payload["recent_turns"][0]["assistant_response"] == (
        "estimate_lookup returned 1 result(s)."
    )
    assert payload["execution"]["source"] == "reconstructed_from_agent_shell_transcript"
    assert payload["execution"]["summary"]["by_subject_type"]["route"] == 2
    assert payload["execution"]["summary"]["by_subject_type"]["context_provider"] == 1
    assert payload["execution"]["summary"]["by_subject_type"]["deterministic_tool"] == 1
