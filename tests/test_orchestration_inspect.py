from __future__ import annotations

import json
from pathlib import Path

from orchestration_inspect import (
    describe_agent_agents,
    describe_agent_commands,
    describe_agent_skills,
    describe_agent_tasks,
    describe_agent_tools,
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
            "history_turn_window": 6,
        }
    }


def _skill_cfg(tmp_path: Path) -> dict:
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)
    (skills_dir / "electrical-estimating.md").write_text(
        "\n".join(
            [
                "---",
                "id: electrical-estimating",
                "title: Electrical Estimating",
                "summary: Structure estimate answers around assumptions.",
                "aliases:",
                "  - estimate",
                "tags:",
                "  - labor",
                "route_fit:",
                "  - text",
                "triggers:",
                "  - estimate",
                "use_when: []",
                "avoid_when: []",
                "---",
                "Separate labor and material assumptions.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return {
        "skill_registry": {
            "enabled": True,
            "root_dir": str(skills_dir),
            "max_active_skills": 2,
            "max_instruction_chars": 1200,
        }
    }


def _task_cfg(tmp_path: Path) -> dict:
    root_dir = tmp_path / "agent_tasks"
    return {
        "agent_task_manager": {
            "enabled": True,
            "root_dir": str(root_dir),
            "tasks_dir": str(root_dir / "tasks"),
            "logs_dir": str(root_dir / "logs"),
            "transcripts_dir": str(root_dir / "transcripts"),
        }
    }


def _agent_cfg(tmp_path: Path) -> dict:
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)
    (skills_dir / "electrical-estimating.md").write_text(
        "\n".join(
            [
                "---",
                "id: electrical-estimating",
                "title: Electrical Estimating",
                "summary: Estimate guidance.",
                "aliases:",
                "  - estimate",
                "tags: []",
                "route_fit:",
                "  - text",
                "triggers:",
                "  - estimate",
                "use_when: []",
                "avoid_when: []",
                "---",
                "Separate labor and material assumptions.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    agents_dir = tmp_path / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    (agents_dir / "estimate-reviewer.md").write_text(
        "\n".join(
            [
                "---",
                "id: estimate-reviewer",
                "title: Estimate Reviewer",
                "summary: Review estimate gaps.",
                "aliases:",
                "  - estimate-review",
                "skill_names:",
                "  - estimate",
                "allowed_routes:",
                "  - text",
                "  - retrieval",
                "use_when: []",
                "avoid_when: []",
                "---",
                "Review grounded estimate gaps.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return {
        "skill_registry": {
            "enabled": True,
            "root_dir": str(skills_dir),
            "max_active_skills": 2,
            "max_instruction_chars": 1200,
        },
        "agent_registry": {
            "enabled": True,
            "root_dir": str(agents_dir),
        },
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


def test_describe_agent_commands_reports_registry() -> None:
    summary = describe_agent_commands()
    detail = describe_agent_commands("quit")

    assert summary["command_count"] == 11
    assert summary["commands"][0]["name"] == "help"
    assert detail["name"] == "exit"
    assert detail["aliases"] == ["quit"]


def test_describe_agent_skills_reports_registry(tmp_path: Path) -> None:
    cfg = _skill_cfg(tmp_path)

    summary = describe_agent_skills(cfg)
    detail = describe_agent_skills(cfg, "estimate")

    assert summary["skill_count"] == 1
    assert summary["skills"][0]["name"] == "electrical-estimating"
    assert detail["name"] == "electrical-estimating"
    assert "Separate labor and material assumptions." in detail["instructions"]


def test_describe_agent_agents_reports_registry(tmp_path: Path) -> None:
    cfg = _agent_cfg(tmp_path)

    summary = describe_agent_agents(cfg)
    detail = describe_agent_agents(cfg, "estimate-review")

    assert summary["agent_count"] == 1
    assert summary["agents"][0]["name"] == "estimate-reviewer"
    assert detail["name"] == "estimate-reviewer"
    assert detail["skill_names"] == ["electrical-estimating"]
    assert "Review grounded estimate gaps." in detail["instructions"]


def test_describe_agent_tools_reports_registry() -> None:
    cfg = {
        "deterministic_tools": {
            "estimate_lookup": {"enabled": True, "default_top_k": 7},
            "revit_entity_lookup": {"enabled": False},
        }
    }

    summary = describe_agent_tools(cfg)
    detail = describe_agent_tools(cfg, "estimate")

    assert summary["tool_count"] == 3
    assert summary["enabled_count"] == 1
    assert summary["tools"][0]["name"] == "estimate_lookup"
    assert detail["name"] == "estimate_lookup"
    assert detail["resolved_settings"]["default_top_k"] == 7


def test_describe_agent_tasks_reports_saved_tasks(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    tasks_dir = tmp_path / "agent_tasks" / "tasks"
    logs_dir = tmp_path / "agent_tasks" / "logs"
    transcripts_dir = tmp_path / "agent_tasks" / "transcripts"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    log_path = logs_dir / "agent-task-123.log"
    log_path.write_text("step 1\nstep 2\n", encoding="utf-8")
    summary_path = tasks_dir / "agent-task-123.json"
    summary_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "task_id": "agent-task-123",
                "kind": "workflow",
                "name": "demo",
                "status": "completed",
                "created_at": "2026-04-01T12:00:00Z",
                "updated_at": "2026-04-01T12:01:00Z",
                "started_at": "2026-04-01T12:00:05Z",
                "completed_at": "2026-04-01T12:01:00Z",
                "summary_path": str(summary_path.resolve()),
                "log_path": str(log_path.resolve()),
                "transcript_path": str((transcripts_dir / "agent-task-123.jsonl").resolve()),
                "config_path": str((tmp_path / "config.yaml").resolve()),
                "pid": 12345,
                "source": "operator",
                "metadata": {
                    "workflow": "demo",
                    "child_task_ids": ["agent-task-456"],
                },
                "result": {"executed_steps": 1},
                "error": None,
                "exit_code": 0,
                "cancel_requested_at": None,
            }
        ),
        encoding="utf-8",
    )

    summary = describe_agent_tasks(cfg)
    detail = describe_agent_tasks(cfg, "agent-task-123", tail=1)

    assert summary["task_count"] == 1
    assert summary["active_task_count"] == 0
    assert summary["restartable_task_count"] == 0
    assert summary["lineage"] == {
        "root_task_count": 1,
        "child_task_count": 0,
        "parent_task_count": 1,
    }
    assert summary["tasks"][0]["task_id"] == "agent-task-123"
    assert summary["tasks"][0]["child_task_count"] == 1
    assert summary["tasks"][0]["last_child_task_id"] == "agent-task-456"
    assert detail["task"]["name"] == "demo"
    assert detail["task"]["child_task_count"] == 1
    assert detail["task"]["child_task_ids"] == ["agent-task-456"]
    assert detail["task"]["restartable"] is False
    assert detail["log_tail"] == ["step 2"]


def test_describe_agent_tasks_includes_subagent_transcript(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    tasks_dir = tmp_path / "agent_tasks" / "tasks"
    logs_dir = tmp_path / "agent_tasks" / "logs"
    transcripts_dir = tmp_path / "agent_tasks" / "transcripts"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    log_path = logs_dir / "agent-task-subagent.log"
    log_path.write_text("subagent task started\nsubagent task completed\n", encoding="utf-8")
    transcript_path = transcripts_dir / "agent-task-subagent.jsonl"
    transcript_path.write_text(
        json.dumps(
            {
                "turn_id": "turn-subagent",
                "turn_index": 0,
                "route": "text",
                "runtime_owner": "text",
                "user": {"prompt": "Summarize the source section."},
                "assistant": {"response": "Grounded answer", "source": "model"},
                "skills": [],
                "tool": None,
                "error": None,
                "execution": {
                    "schema_version": 1,
                    "route": {
                        "subject_type": "route",
                        "subject_name": "text",
                        "status": "succeeded",
                    },
                    "context_providers": [],
                    "deterministic_tool": None,
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )
    summary_path = tasks_dir / "agent-task-subagent.json"
    summary_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "task_id": "agent-task-subagent",
                "kind": "subagent",
                "name": "worker",
                "status": "completed",
                "created_at": "2026-04-01T12:00:00Z",
                "updated_at": "2026-04-01T12:01:00Z",
                "started_at": "2026-04-01T12:00:05Z",
                "completed_at": "2026-04-01T12:01:00Z",
                "summary_path": str(summary_path.resolve()),
                "log_path": str(log_path.resolve()),
                "transcript_path": str(transcript_path.resolve()),
                "config_path": str((tmp_path / "config.yaml").resolve()),
                "pid": 12345,
                "source": "agent_shell_subagent",
                "metadata": {
                    "prompt": "Summarize the source section.",
                    "allowed_routes": ["text", "retrieval"],
                },
                "result": {"assistant_response": "Grounded answer"},
                "error": None,
                "exit_code": 0,
                "cancel_requested_at": None,
            }
        ),
        encoding="utf-8",
    )

    detail = describe_agent_tasks(cfg, "agent-task-subagent", tail=1)

    assert detail["transcript"]["turn_count"] == 1
    assert detail["transcript"]["recent_turns"][0]["assistant_response"] == "Grounded answer"
    assert detail["transcript"]["execution"]["summary"]["by_subject_type"] == {"route": 1}


def test_describe_agent_tasks_includes_workflow_transcript_events(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    tasks_dir = tmp_path / "agent_tasks" / "tasks"
    logs_dir = tmp_path / "agent_tasks" / "logs"
    transcripts_dir = tmp_path / "agent_tasks" / "transcripts"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    log_path = logs_dir / "agent-task-workflow.log"
    log_path.write_text("step 1\nstep 2\n", encoding="utf-8")
    transcript_path = transcripts_dir / "agent-task-workflow.jsonl"
    transcript_path.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "record_type": "task_event",
                        "event_type": "task_started",
                        "recorded_at": "2026-04-01T12:00:01Z",
                        "task_id": "agent-task-workflow",
                        "task_kind": "workflow",
                        "task_status": "running",
                        "workflow": "demo",
                        "step_count": 1,
                    }
                ),
                json.dumps(
                    {
                        "record_type": "task_event",
                        "event_type": "task_completed",
                        "recorded_at": "2026-04-01T12:00:05Z",
                        "task_id": "agent-task-workflow",
                        "task_kind": "workflow",
                        "task_status": "completed",
                        "workflow": "demo",
                        "step_count": 1,
                        "executed_steps": 1,
                        "result": {
                            "workflow": "demo",
                            "description": "Demo workflow",
                            "executed_steps": 1,
                            "step_count": 1,
                            "tags": ["demo"],
                            "variables": {},
                            "dream": {"enabled": False, "status": "not_run"},
                        },
                    }
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    summary_path = tasks_dir / "agent-task-workflow.json"
    summary_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "task_id": "agent-task-workflow",
                "kind": "workflow",
                "name": "demo",
                "status": "completed",
                "created_at": "2026-04-01T12:00:00Z",
                "updated_at": "2026-04-01T12:01:00Z",
                "started_at": "2026-04-01T12:00:05Z",
                "completed_at": "2026-04-01T12:01:00Z",
                "summary_path": str(summary_path.resolve()),
                "log_path": str(log_path.resolve()),
                "transcript_path": str(transcript_path.resolve()),
                "config_path": str((tmp_path / "config.yaml").resolve()),
                "pid": 12345,
                "source": "operator",
                "metadata": {
                    "workflow": "demo",
                    "step_count": 1,
                },
                "result": {"executed_steps": 1},
                "error": None,
                "exit_code": 0,
                "cancel_requested_at": None,
            }
        ),
        encoding="utf-8",
    )

    detail = describe_agent_tasks(cfg, "agent-task-workflow", tail=1, transcript_tail=1)

    assert detail["transcript"]["event_count"] == 2
    assert detail["transcript"]["recent_events"][0]["event_type"] == "task_completed"
    assert detail["transcript"]["recent_events"][0]["dream_status"] == "not_run"


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
                "last_skill_names": [],
                "pinned_skills": ["electrical-estimating"],
                "next_turn_skills": [],
                "history_summary_text": "- [text] User: First question | Assistant: First answer",
                "history_summary_turn_count": 1,
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
                "last_skill_names": ["electrical-estimating"],
                "pinned_skills": ["electrical-estimating"],
                "next_turn_skills": ["revit-family-reference"],
                "history_summary_text": None,
                "history_summary_turn_count": 0,
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
    assert payload["sessions"][0]["pinned_skills"] == ["electrical-estimating"]
    assert payload["sessions"][0]["next_turn_skills"] == ["revit-family-reference"]
    assert payload["sessions"][0]["has_history_summary"] is False
    assert payload["sessions"][0]["history_recent_turn_window"] == 6
    assert payload["sessions"][0]["history_recent_turn_count"] == 2
    assert payload["sessions"][0]["history_omitted_turn_count"] == 0
    assert payload["sessions"][1]["has_history_summary"] is True
    assert payload["sessions"][1]["history_summary_turn_count"] == 1
    assert payload["sessions"][1]["history_recent_turn_window"] == 6
    assert payload["sessions"][1]["history_recent_turn_count"] == 1
    assert payload["sessions"][1]["history_omitted_turn_count"] == 0


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
    assert payload["history"] == {
        "recent_turn_window": 6,
        "recent_turn_count": 2,
        "summary_turn_count": 0,
        "omitted_turn_count": 0,
        "has_summary": False,
        "summary_char_count": 0,
        "message_count": 4,
    }
    assert payload["execution"]["source"] == "reconstructed_from_agent_shell_transcript"
    assert payload["execution"]["summary"]["by_subject_type"]["route"] == 2
    assert payload["execution"]["summary"]["by_subject_type"]["context_provider"] == 1
    assert payload["execution"]["summary"]["by_subject_type"]["deterministic_tool"] == 1


def test_describe_agent_shell_session_uses_configured_history_window(tmp_path) -> None:
    cfg = _agent_shell_cfg(tmp_path)
    cfg["agent_shell"]["history_turn_window"] = 4
    sessions_dir = tmp_path / "agent_shell" / "sessions"
    transcripts_dir = tmp_path / "agent_shell" / "transcripts"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    session_id = "agent-shell-configured-window"
    transcript_path = transcripts_dir / f"{session_id}.jsonl"
    _write_jsonl(
        transcript_path,
        [
            {
                "turn_id": f"turn-{index}",
                "turn_index": index,
                "route": "text",
                "runtime_owner": "text",
                "user": {"prompt": f"Question {index}"},
                "assistant": {"response": f"Answer {index}"},
                "error": None,
                "execution": {
                    "schema_version": 1,
                    "route": None,
                    "context_providers": [],
                    "deterministic_tool": None,
                },
            }
            for index in range(8)
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
                "turn_count": 8,
                "history_turn_window": 4,
                "history_summary_text": "- [text] User: Question 0 | Assistant: Answer 0\n- [text] User: Question 1 | Assistant: Answer 1\n- [text] User: Question 2 | Assistant: Answer 2\n- [text] User: Question 3 | Assistant: Answer 3",
                "history_summary_turn_count": 4,
                "route_counts": {"text": 8},
                "last_route": "text",
                "last_runtime_owner": "text",
                "transcript_path": str(transcript_path.resolve()),
            }
        ),
        encoding="utf-8",
    )

    payload = describe_agent_shell_session(cfg, session_id, tail=1)

    assert payload["history"] == {
        "recent_turn_window": 4,
        "recent_turn_count": 4,
        "summary_turn_count": 4,
        "omitted_turn_count": 0,
        "has_summary": True,
        "summary_char_count": len(payload["session"]["history_summary_text"]),
        "message_count": 9,
    }


def test_describe_agent_tasks_reports_subagent_prompt_context(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    tasks_dir = tmp_path / "agent_tasks" / "tasks"
    logs_dir = tmp_path / "agent_tasks" / "logs"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    log_path = logs_dir / "agent-task-subagent.log"
    log_path.write_text("subagent task started\nsubagent task completed\n", encoding="utf-8")
    summary_path = tasks_dir / "agent-task-subagent.json"
    summary_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "task_id": "agent-task-subagent",
                "kind": "subagent",
                "name": "Estimate Reviewer",
                "status": "completed",
                "created_at": "2026-04-01T12:00:00Z",
                "updated_at": "2026-04-01T12:01:00Z",
                "started_at": "2026-04-01T12:00:05Z",
                "completed_at": "2026-04-01T12:01:00Z",
                "summary_path": str(summary_path.resolve()),
                "log_path": str(log_path.resolve()),
                "config_path": str((tmp_path / "config.yaml").resolve()),
                "pid": 12345,
                "source": "agent_shell_subagent",
                "metadata": {
                    "prompt": "Review the latest estimate answer.",
                    "agent_instructions": "Review grounded estimate gaps.",
                    "delegation_briefing": "Check NEC grounding references first.",
                    "attachments": ["/tmp/source-a.txt"],
                    "explicit_skill_names": ["electrical-estimating"],
                    "allowed_routes": ["text", "retrieval"],
                },
                "result": {"assistant_response": "Looks grounded."},
                "error": None,
                "exit_code": 0,
                "cancel_requested_at": None,
            }
        ),
        encoding="utf-8",
    )

    detail = describe_agent_tasks(cfg, "agent-task-subagent", tail=1)

    assert detail["task"]["subagent_context"] == {
        "has_prior_history": False,
        "history_message_count": 0,
        "prompt_sections": [
            "agent_instructions",
            "delegation_briefing",
            "assigned_task",
        ],
        "prompt_section_count": 3,
        "prompt_char_count": len("Review the latest estimate answer."),
        "has_agent_instructions": True,
        "agent_instructions_char_count": len("Review grounded estimate gaps."),
        "has_delegation_briefing": True,
        "delegation_briefing_char_count": len("Check NEC grounding references first."),
        "attachment_count": 1,
        "explicit_skill_names": ["electrical-estimating"],
        "explicit_tool_name": None,
        "allowed_routes": ["text", "retrieval"],
    }
