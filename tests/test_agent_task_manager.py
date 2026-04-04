from __future__ import annotations

import json
from pathlib import Path
import signal

import pytest

import agent_task_manager
from agent_task_manager import (
    TaskManagerError,
    attach_agent_task,
    cancel_agent_task,
    describe_agent_task,
    list_agent_tasks,
    parse_task_vars,
    resume_agent_task,
    run_task_worker,
    start_dream_task,
    start_subagent_task,
    start_workflow_task,
    summarize_agent_tasks,
)
from runtime_contracts import (
    TASK_STATUS_CANCELLED,
    TASK_KIND_DREAM,
    TASK_KIND_SUBAGENT,
    TASK_KIND_WORKFLOW,
    TASK_STATUS_COMPLETED,
    TASK_STATUS_FAILED,
    TASK_STATUS_PENDING,
    TASK_STATUS_RUNNING,
)


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


def _task_cfg_with_agent_registry(tmp_path: Path) -> dict:
    cfg = _task_cfg(tmp_path)
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)
    (skills_dir / "electrical-estimating.md").write_text(
        "\n".join(
            [
                "---",
                "id: electrical-estimating",
                "title: Electrical Estimating",
                "summary: Estimate guidance",
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
                "section: estimate-review",
                "---",
                "Review grounded estimate gaps.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    cfg["skill_registry"] = {
        "enabled": True,
        "root_dir": str(skills_dir),
        "max_active_skills": 2,
        "max_instruction_chars": 1200,
    }
    cfg["agent_registry"] = {
        "enabled": True,
        "root_dir": str(agents_dir),
    }
    return cfg


def _write_task_summary(
    tmp_path: Path,
    *,
    task_id: str,
    kind: str,
    status: str,
    pid: int | None = None,
    source: str = "operator",
    metadata: dict | None = None,
) -> tuple[Path, Path]:
    tasks_dir = tmp_path / "agent_tasks" / "tasks"
    logs_dir = tmp_path / "agent_tasks" / "logs"
    transcripts_dir = tmp_path / "agent_tasks" / "transcripts"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    summary_path = tasks_dir / f"{task_id}.json"
    log_path = logs_dir / f"{task_id}.log"
    transcript_path = transcripts_dir / f"{task_id}.jsonl"
    log_path.write_text("step 1\nstep 2\n", encoding="utf-8")
    summary_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "task_id": task_id,
                "kind": kind,
                "name": "demo" if kind == TASK_KIND_WORKFLOW else "dream",
                "status": status,
                "created_at": "2026-04-01T12:00:00Z",
                "updated_at": "2026-04-01T12:00:00Z",
                "config_path": str((tmp_path / "config.yaml").resolve()),
                "summary_path": str(summary_path.resolve()),
                "log_path": str(log_path.resolve()),
                "transcript_path": str(transcript_path.resolve()),
                "pid": pid,
                "source": source,
                "metadata": metadata or {},
                "result": None,
                "error": None,
                "exit_code": None,
                "started_at": None,
                "completed_at": None,
                "cancel_requested_at": None,
            }
        ),
        encoding="utf-8",
    )
    return summary_path, log_path


def test_parse_task_vars_parses_assignments() -> None:
    parsed = parse_task_vars(["output_path=/tmp/out", "greeting=hello"])

    assert parsed == {"output_path": "/tmp/out", "greeting": "hello"}


def test_parse_task_vars_rejects_invalid_assignments() -> None:
    with pytest.raises(TaskManagerError):
        parse_task_vars(["missing-separator"])


def test_list_and_describe_agent_tasks_read_saved_state(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    _write_task_summary(
        tmp_path,
        task_id="agent-task-123",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_COMPLETED,
        pid=12345,
    )

    listed = list_agent_tasks(cfg)
    detail = describe_agent_task(cfg, "agent-task-123", tail=1)

    assert listed["task_count"] == 1
    assert listed["active_task_count"] == 0
    assert listed["restartable_task_count"] == 0
    assert listed["by_status"] == {TASK_STATUS_COMPLETED: 1}
    assert listed["by_kind"] == {TASK_KIND_WORKFLOW: 1}
    assert listed["lineage"] == {
        "root_task_count": 1,
        "child_task_count": 0,
        "parent_task_count": 0,
    }
    assert listed["tasks"][0]["task_id"] == "agent-task-123"
    assert listed["tasks"][0]["child_task_count"] == 0
    assert listed["tasks"][0]["last_child_task_id"] is None
    assert listed["tasks"][0]["restartable"] is False
    assert detail["task"]["task_id"] == "agent-task-123"
    assert detail["task"]["child_task_count"] == 0
    assert detail["task"]["child_task_ids"] == []
    assert detail["task"]["restartable"] is False
    assert detail["log_tail"] == ["step 2"]


def test_summarize_agent_tasks_reports_active_restartable_and_filtered_views(
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    _write_task_summary(
        tmp_path,
        task_id="agent-task-300",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_RUNNING,
        pid=300,
        source="agent_shell",
        metadata={"child_task_ids": ["agent-task-200"]},
    )
    _write_task_summary(
        tmp_path,
        task_id="agent-task-200",
        kind=TASK_KIND_SUBAGENT,
        status=TASK_STATUS_COMPLETED,
        source="agent_shell",
        metadata={"parent_task_id": "agent-task-300"},
    )
    _write_task_summary(
        tmp_path,
        task_id="agent-task-100",
        kind=TASK_KIND_DREAM,
        status=TASK_STATUS_CANCELLED,
        source="operator",
    )

    summary = summarize_agent_tasks(cfg, recent_limit=1)
    filtered = list_agent_tasks(cfg, task_source="operator")

    assert summary["task_count"] == 3
    assert summary["active_task_count"] == 1
    assert summary["restartable_task_count"] == 1
    assert len(summary["recent_tasks"]) == 1
    assert summary["active_tasks"][0]["task_id"] == "agent-task-300"
    assert summary["restartable_tasks"][0]["task_id"] == "agent-task-100"
    assert summary["lineage"] == {
        "root_task_count": 2,
        "child_task_count": 1,
        "parent_task_count": 1,
        "tasks_with_children": [
            {
                "task_id": "agent-task-300",
                "kind": TASK_KIND_WORKFLOW,
                "name": "demo",
                "status": TASK_STATUS_RUNNING,
                "active": True,
                "restartable": False,
                "created_at": "2026-04-01T12:00:00Z",
                "updated_at": "2026-04-01T12:00:00Z",
                "started_at": None,
                "completed_at": None,
                "exit_code": None,
                "pid": 300,
                "source": "agent_shell",
                "parent_task_id": None,
                "child_task_count": 1,
                "last_child_task_id": "agent-task-200",
                "agent_definition_name": None,
                "cancel_requested_at": None,
                "resumed_by_task_id": None,
                "resumed_from_task_id": None,
            }
        ],
    }
    assert filtered["filters"]["source"] == "operator"
    assert filtered["task_count"] == 1
    assert filtered["tasks"][0]["task_id"] == "agent-task-100"


def test_attach_agent_task_reads_incremental_log_lines(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    _write_task_summary(
        tmp_path,
        task_id="agent-task-123",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_RUNNING,
        pid=None,
    )

    payload = attach_agent_task(cfg, "agent-task-123", cursor=1, limit=1)

    assert payload["cursor"] == 1
    assert payload["next_cursor"] == 2
    assert payload["attached_lines"] == ["step 2"]
    assert payload["process_running"] is False
    assert payload["stream_complete"] is True


def test_describe_agent_task_reports_subagent_prompt_context(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    _write_task_summary(
        tmp_path,
        task_id="agent-task-321",
        kind=TASK_KIND_SUBAGENT,
        status=TASK_STATUS_COMPLETED,
        source="agent_shell_subagent",
        metadata={
            "prompt": "Review the latest estimate answer.",
            "agent_instructions": "Review grounded estimate gaps.",
            "delegation_briefing": "Check NEC grounding references first.",
            "attachments": ["/tmp/source-a.txt"],
            "explicit_skill_names": ["electrical-estimating"],
            "allowed_routes": ["text", "retrieval"],
        },
    )

    detail = describe_agent_task(cfg, "agent-task-321", tail=1)

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


def test_describe_agent_task_reads_subagent_transcript(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    _, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-654",
        kind=TASK_KIND_SUBAGENT,
        status=TASK_STATUS_COMPLETED,
        source="agent_shell_subagent",
    )
    transcript_path = tmp_path / "agent_tasks" / "transcripts" / "agent-task-654.jsonl"
    transcript_path.write_text(
        json.dumps(
            {
                "turn_id": "turn-654",
                "turn_index": 0,
                "route": "deterministic_tool",
                "runtime_owner": "geometry_rules",
                "user": {"prompt": "Find the estimate lookup for EMT conduit."},
                "assistant": {
                    "response": "estimate_lookup returned 1 result(s).",
                    "source": "tool",
                },
                "skills": [],
                "tool": {
                    "name": "estimate_lookup",
                    "request": {"query": "EMT conduit"},
                    "response": {"result_count": 1},
                },
                "error": None,
                "execution": {
                    "schema_version": 1,
                    "route": {
                        "subject_type": "route",
                        "subject_name": "deterministic_tool",
                        "status": "succeeded",
                    },
                    "context_providers": [],
                    "deterministic_tool": {
                        "subject_type": "deterministic_tool",
                        "subject_name": "estimate_lookup",
                        "status": "succeeded",
                    },
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )

    detail = describe_agent_task(cfg, "agent-task-654", tail=1)

    assert detail["transcript"]["turn_count"] == 1
    assert detail["transcript"]["recent_turns"] == [
        {
            "turn_id": "turn-654",
            "turn_index": 0,
            "route": "deterministic_tool",
            "runtime_owner": "geometry_rules",
            "user_prompt": "Find the estimate lookup for EMT conduit.",
            "assistant_response": "estimate_lookup returned 1 result(s).",
            "skill_names": [],
            "tool_name": "estimate_lookup",
            "error": None,
        }
    ]
    assert detail["transcript"]["last_turn"]["tool"]["name"] == "estimate_lookup"
    assert detail["transcript"]["execution"]["summary"]["by_subject_type"] == {
        "route": 1,
        "deterministic_tool": 1,
    }


def test_describe_agent_task_reads_workflow_transcript_events(tmp_path: Path) -> None:
    cfg = _task_cfg(tmp_path)
    _, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-741",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_COMPLETED,
        metadata={
            "workflow": "demo",
            "description": "Demo workflow",
            "step_count": 2,
            "variables": {"output_path": "/tmp/out"},
            "tags": ["demo"],
        },
    )
    transcript_path = tmp_path / "agent_tasks" / "transcripts" / "agent-task-741.jsonl"
    transcript_path.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "record_type": "task_event",
                        "event_type": "task_started",
                        "recorded_at": "2026-04-01T12:00:01Z",
                        "task_id": "agent-task-741",
                        "task_kind": "workflow",
                        "task_status": "running",
                        "workflow": "demo",
                        "step_count": 2,
                        "variables": {"output_path": "/tmp/out"},
                    }
                ),
                json.dumps(
                    {
                        "record_type": "task_event",
                        "event_type": "task_completed",
                        "recorded_at": "2026-04-01T12:00:05Z",
                        "task_id": "agent-task-741",
                        "task_kind": "workflow",
                        "task_status": "completed",
                        "workflow": "demo",
                        "step_count": 2,
                        "executed_steps": 2,
                        "result": {
                            "workflow": "demo",
                            "description": "Demo workflow",
                            "executed_steps": 2,
                            "step_count": 2,
                            "tags": ["demo"],
                            "variables": {"output_path": "/tmp/out"},
                            "dream": {"enabled": False, "status": "not_run"},
                        },
                    }
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    detail = describe_agent_task(cfg, "agent-task-741", tail=1, transcript_tail=1)

    assert detail["log_tail"] == ["step 2"]
    assert detail["task"]["transcript_path"] == str(transcript_path.resolve())
    assert detail["transcript"]["record_count"] == 2
    assert detail["transcript"]["event_count"] == 2
    assert detail["transcript"]["recent_events"] == [
        {
            "event_type": "task_completed",
            "recorded_at": "2026-04-01T12:00:05Z",
            "task_kind": "workflow",
            "task_status": "completed",
            "workflow": "demo",
            "executed_steps": 2,
            "step_count": 2,
            "dream_status": "not_run",
            "error": None,
            "exit_code": None,
        }
    ]
    assert detail["transcript"]["last_event"]["result"]["workflow"] == "demo"


def test_start_workflow_task_persists_summary_and_builds_worker_command(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    captured: dict[str, object] = {}

    class _FakeUuid:
        hex = "abc123def4567890"

    monkeypatch.setattr(agent_task_manager.uuid, "uuid4", lambda: _FakeUuid())
    monkeypatch.setattr(
        agent_task_manager,
        "current_utc_timestamp",
        lambda: "2026-04-01T12:00:00Z",
    )
    monkeypatch.setattr(
        agent_task_manager,
        "render_workflow_steps",
        lambda cfg, config_path, workflow_name, extra_vars: {
            "workflow": workflow_name,
            "description": "Demo workflow",
            "required_vars": ["output_path"],
            "defaults": {"greeting": "hello"},
            "tags": ["demo"],
            "variables": {"output_path": "/tmp/out", "greeting": "hello"},
            "steps": [{"name": "write output", "argv": ["python", "-V"]}],
        },
    )

    def _fake_start_task_process(settings: dict, summary: dict, command: list[str]) -> dict:
        captured["settings"] = settings
        captured["summary"] = summary
        captured["command"] = command
        return {**summary, "status": TASK_STATUS_RUNNING, "command": command}

    monkeypatch.setattr(agent_task_manager, "_start_task_process", _fake_start_task_process)

    result = start_workflow_task(
        cfg,
        str(tmp_path / "config.yaml"),
        "demo",
        {"output_path": "/tmp/out"},
    )

    task_id = "agent-task-abc123def456"
    summary_path = tmp_path / "agent_tasks" / "tasks" / f"{task_id}.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert result["task_id"] == task_id
    assert result["status"] == TASK_STATUS_RUNNING
    assert summary["status"] == TASK_STATUS_PENDING
    assert summary["metadata"]["workflow"] == "demo"
    assert summary["metadata"]["step_count"] == 1
    assert captured["command"][4] == "worker"
    assert "--workflow" in captured["command"]
    assert "--var" in captured["command"]


def test_start_subagent_task_persists_parent_linkage_and_defaults(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    parent_summary_path, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-parent",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_RUNNING,
        pid=111,
    )

    captured: dict[str, object] = {}

    class _FakeUuid:
        hex = "1234567890abcdef"

    monkeypatch.setattr(agent_task_manager.uuid, "uuid4", lambda: _FakeUuid())
    monkeypatch.setattr(
        agent_task_manager,
        "current_utc_timestamp",
        lambda: "2026-04-02T10:00:00Z",
    )

    def _fake_start_task_process(settings: dict, summary: dict, command: list[str]) -> dict:
        captured["summary"] = summary
        captured["command"] = command
        return {**summary, "status": TASK_STATUS_RUNNING, "command": command}

    monkeypatch.setattr(agent_task_manager, "_start_task_process", _fake_start_task_process)

    result = start_subagent_task(
        cfg,
        str(tmp_path / "config.yaml"),
        "Summarize the reference section.",
        source="agent_shell_subagent",
        parent_task_id="agent-task-parent",
        delegation_briefing="Check conduit support references first.",
        agent_name="worker",
    )

    task_id = "agent-task-1234567890ab"
    summary_path = tmp_path / "agent_tasks" / "tasks" / f"{task_id}.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    parent_summary = json.loads(parent_summary_path.read_text(encoding="utf-8"))

    assert result["task_id"] == task_id
    assert summary["kind"] == TASK_KIND_SUBAGENT
    assert summary["name"] == "worker"
    assert summary["metadata"]["prompt"] == "Summarize the reference section."
    assert summary["metadata"]["request_source"] == "agent_shell_subagent"
    assert summary["metadata"]["allowed_routes"] == ["text", "retrieval"]
    assert summary["metadata"]["parent_task_id"] == "agent-task-parent"
    assert summary["metadata"]["delegation_briefing"] == "Check conduit support references first."
    assert captured["command"][4] == "worker"
    assert captured["command"][-1] == TASK_KIND_SUBAGENT
    assert parent_summary["metadata"]["child_task_ids"] == [task_id]
    assert parent_summary["last_child_task_id"] == task_id


def test_start_subagent_task_applies_agent_definition_defaults(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg_with_agent_registry(tmp_path)
    captured: dict[str, object] = {}

    class _FakeUuid:
        hex = "abcdef1234567890"

    monkeypatch.setattr(agent_task_manager.uuid, "uuid4", lambda: _FakeUuid())
    monkeypatch.setattr(
        agent_task_manager,
        "current_utc_timestamp",
        lambda: "2026-04-02T10:02:00Z",
    )

    def _fake_start_task_process(settings: dict, summary: dict, command: list[str]) -> dict:
        captured["summary"] = summary
        captured["command"] = command
        return {**summary, "status": TASK_STATUS_RUNNING, "command": command}

    monkeypatch.setattr(agent_task_manager, "_start_task_process", _fake_start_task_process)

    result = start_subagent_task(
        cfg,
        str(tmp_path / "config.yaml"),
        "Review the latest estimate answer.",
        agent_definition_name="estimate-review",
        source="agent_shell_subagent",
    )

    task_id = "agent-task-abcdef123456"
    summary_path = tmp_path / "agent_tasks" / "tasks" / f"{task_id}.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert result["task_id"] == task_id
    assert summary["name"] == "Estimate Reviewer"
    assert summary["metadata"]["agent_definition_name"] == "estimate-reviewer"
    assert summary["metadata"]["agent_instructions"] == "Review grounded estimate gaps."
    assert summary["metadata"]["section"] == "estimate-review"
    assert summary["metadata"]["explicit_skill_names"] == ["electrical-estimating"]
    assert summary["metadata"]["allowed_routes"] == ["text", "retrieval"]
    assert captured["command"][4] == "worker"


def test_start_dream_task_persists_summary_and_builds_worker_command(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    cfg["dream"] = {"enabled": True}
    captured: dict[str, object] = {}

    class _FakeUuid:
        hex = "f0e1d2c3b4a59687"

    monkeypatch.setattr(agent_task_manager.uuid, "uuid4", lambda: _FakeUuid())
    monkeypatch.setattr(
        agent_task_manager,
        "current_utc_timestamp",
        lambda: "2026-04-01T12:00:00Z",
    )

    def _fake_start_task_process(settings: dict, summary: dict, command: list[str]) -> dict:
        captured["command"] = command
        return {**summary, "status": TASK_STATUS_RUNNING, "command": command}

    monkeypatch.setattr(agent_task_manager, "_start_task_process", _fake_start_task_process)

    result = start_dream_task(cfg, str(tmp_path / "config.yaml"))

    task_id = "agent-task-f0e1d2c3b4a5"
    summary_path = tmp_path / "agent_tasks" / "tasks" / f"{task_id}.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert result["task_id"] == task_id
    assert summary["kind"] == TASK_KIND_DREAM
    assert summary["metadata"]["dream_enabled"] is True
    assert captured["command"][4] == "worker"
    assert captured["command"][-1] == TASK_KIND_DREAM


def test_cancel_agent_task_marks_cancel_requested(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    summary_path, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-123",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_RUNNING,
        pid=4242,
    )
    calls: list[tuple[int, int]] = []

    monkeypatch.setattr(agent_task_manager, "current_utc_timestamp", lambda: "2026-04-01T12:05:00Z")
    monkeypatch.setattr(agent_task_manager.os, "getpgid", lambda pid: pid)
    monkeypatch.setattr(agent_task_manager.os, "killpg", lambda pid, sig: calls.append((pid, sig)))

    result = cancel_agent_task(cfg, "agent-task-123")
    saved = json.loads(summary_path.read_text(encoding="utf-8"))

    assert calls == [(4242, signal.SIGTERM)]
    assert result["cancel_requested_at"] == "2026-04-01T12:05:00Z"
    assert saved["cancel_requested_at"] == "2026-04-01T12:05:00Z"


def test_resume_agent_task_restarts_workflow_and_links_original_summary(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    summary_path, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-123",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_CANCELLED,
        metadata={
            "workflow": "demo",
            "variables": {"output_path": "/tmp/out"},
            "resume_depth": 1,
        },
    )
    captured: dict[str, object] = {}

    monkeypatch.setattr(agent_task_manager, "current_utc_timestamp", lambda: "2026-04-01T12:20:00Z")
    monkeypatch.setattr(agent_task_manager, "validate_workflow_registry_config", lambda cfg: None)

    def _fake_start_workflow_task(
        cfg: dict,
        config_path: str,
        workflow_name: str,
        extra_vars: dict[str, str] | None = None,
        *,
        source: str = "operator",
        task_metadata: dict | None = None,
    ) -> dict:
        captured["config_path"] = config_path
        captured["workflow_name"] = workflow_name
        captured["extra_vars"] = extra_vars
        captured["source"] = source
        captured["task_metadata"] = dict(task_metadata or {})
        return {
            "task_id": "agent-task-999",
            "kind": TASK_KIND_WORKFLOW,
            "name": "demo",
            "status": TASK_STATUS_RUNNING,
            "metadata": dict(task_metadata or {}),
        }

    monkeypatch.setattr(agent_task_manager, "start_workflow_task", _fake_start_workflow_task)

    result = resume_agent_task(cfg, "agent-task-123", source="agent_shell_resume")
    saved = json.loads(summary_path.read_text(encoding="utf-8"))

    assert result["task_id"] == "agent-task-999"
    assert captured["workflow_name"] == "demo"
    assert captured["extra_vars"] == {"output_path": "/tmp/out"}
    assert captured["source"] == "agent_shell_resume"
    assert captured["task_metadata"] == {
        "resumed_from_task_id": "agent-task-123",
        "resumed_from_status": TASK_STATUS_CANCELLED,
        "resumed_from_kind": TASK_KIND_WORKFLOW,
        "resume_depth": 2,
    }
    assert saved["resumed_at"] == "2026-04-01T12:20:00Z"
    assert saved["resumed_by_task_id"] == "agent-task-999"
    assert saved["resume_count"] == 1


def test_resume_agent_task_restarts_subagent_and_preserves_request_source(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    summary_path, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-555",
        kind=TASK_KIND_SUBAGENT,
        status=TASK_STATUS_FAILED,
        metadata={
            "prompt": "Summarize the source section.",
            "request_source": "NCCER source",
            "section": "Module 1",
            "attachments": ["manual.pdf"],
            "explicit_skill_names": [],
            "explicit_tool_name": None,
            "parent_task_id": "agent-task-parent",
            "delegation_briefing": "Focus on grounded NEC examples.",
            "agent_name": "worker",
            "allowed_routes": ["text", "retrieval"],
        },
    )
    captured: dict[str, object] = {}

    monkeypatch.setattr(agent_task_manager, "current_utc_timestamp", lambda: "2026-04-02T10:05:00Z")

    def _fake_start_subagent_task(
        cfg: dict,
        config_path: str,
        prompt: str,
        *,
        agent_definition_name: str | None = None,
        agent_instructions: str | None = None,
        source: str = "operator",
        request_source: str | None = None,
        section: str | None = None,
        attachments: list[str] | None = None,
        explicit_skill_names: list[str] | tuple[str, ...] | None = None,
        explicit_tool_name: str | None = None,
        parent_task_id: str | None = None,
        delegation_briefing: str | None = None,
        agent_name: str | None = None,
        allowed_routes: list[str] | tuple[str, ...] | None = None,
        task_metadata: dict | None = None,
    ) -> dict:
        captured["source"] = source
        captured["agent_definition_name"] = agent_definition_name
        captured["agent_instructions"] = agent_instructions
        captured["request_source"] = request_source
        captured["section"] = section
        captured["attachments"] = attachments
        captured["parent_task_id"] = parent_task_id
        captured["delegation_briefing"] = delegation_briefing
        captured["agent_name"] = agent_name
        captured["allowed_routes"] = list(allowed_routes or [])
        captured["task_metadata"] = dict(task_metadata or {})
        return {
            "task_id": "agent-task-777",
            "kind": TASK_KIND_SUBAGENT,
            "name": "worker",
            "status": TASK_STATUS_RUNNING,
        }

    monkeypatch.setattr(agent_task_manager, "start_subagent_task", _fake_start_subagent_task)

    result = resume_agent_task(cfg, "agent-task-555", source="agent_shell_resume")
    saved = json.loads(summary_path.read_text(encoding="utf-8"))

    assert result["task_id"] == "agent-task-777"
    assert captured["source"] == "agent_shell_resume"
    assert captured["agent_definition_name"] is None
    assert captured["agent_instructions"] is None
    assert captured["request_source"] == "NCCER source"
    assert captured["section"] == "Module 1"
    assert captured["attachments"] == ["manual.pdf"]
    assert captured["parent_task_id"] == "agent-task-parent"
    assert captured["delegation_briefing"] == "Focus on grounded NEC examples."
    assert captured["agent_name"] == "worker"
    assert captured["allowed_routes"] == ["text", "retrieval"]
    assert captured["task_metadata"] == {
        "resumed_from_task_id": "agent-task-555",
        "resumed_from_status": TASK_STATUS_FAILED,
        "resumed_from_kind": TASK_KIND_SUBAGENT,
        "resume_depth": 1,
    }
    assert saved["resumed_by_task_id"] == "agent-task-777"


def test_run_task_worker_completes_workflow_task(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    summary_path, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-123",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_PENDING,
    )

    monkeypatch.setattr(agent_task_manager, "current_utc_timestamp", lambda: "2026-04-01T12:10:00Z")
    monkeypatch.setattr(
        agent_task_manager,
        "run_workflow",
        lambda cfg, config_path, workflow_name, extra_vars: {
            "workflow": workflow_name,
            "description": "Demo workflow",
            "executed_steps": 1,
            "steps": [{"name": "write output"}],
            "tags": ["demo"],
            "variables": {"output_path": "/tmp/out"},
            "dream": {"enabled": False, "status": "not_run"},
        },
    )

    result = run_task_worker(
        cfg,
        task_id="agent-task-123",
        kind=TASK_KIND_WORKFLOW,
        workflow_name="demo",
        extra_vars={"output_path": "/tmp/out"},
    )
    saved = json.loads(summary_path.read_text(encoding="utf-8"))
    transcript_path = tmp_path / "agent_tasks" / "transcripts" / "agent-task-123.jsonl"

    assert result["status"] == TASK_STATUS_COMPLETED
    assert result["exit_code"] == 0
    assert result["result"]["workflow"] == "demo"
    assert saved["status"] == TASK_STATUS_COMPLETED
    transcript_rows = [
        json.loads(line)
        for line in transcript_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert transcript_rows[0]["event_type"] == "task_started"
    assert transcript_rows[1]["event_type"] == "task_completed"
    assert transcript_rows[1]["result"]["executed_steps"] == 1


def test_run_task_worker_completes_dream_task(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    _write_task_summary(
        tmp_path,
        task_id="agent-task-456",
        kind=TASK_KIND_DREAM,
        status=TASK_STATUS_PENDING,
    )

    monkeypatch.setattr(agent_task_manager, "current_utc_timestamp", lambda: "2026-04-01T12:15:00Z")
    monkeypatch.setattr(
        agent_task_manager,
        "run_memory_dream",
        lambda cfg: {"enabled": True, "status": "succeeded", "session_count": 1},
    )

    result = run_task_worker(
        cfg,
        task_id="agent-task-456",
        kind=TASK_KIND_DREAM,
    )
    transcript_path = tmp_path / "agent_tasks" / "transcripts" / "agent-task-456.jsonl"

    assert result["status"] == TASK_STATUS_COMPLETED
    assert result["exit_code"] == 0
    assert result["result"]["status"] == "succeeded"
    transcript_rows = [
        json.loads(line)
        for line in transcript_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert transcript_rows[0]["event_type"] == "task_started"
    assert transcript_rows[1]["event_type"] == "task_completed"
    assert transcript_rows[1]["dream_status"] == "succeeded"


def test_run_task_worker_completes_subagent_task(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    summary_path, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-888",
        kind=TASK_KIND_SUBAGENT,
        status=TASK_STATUS_PENDING,
        metadata={
            "prompt": "Summarize the reference section.",
            "request_source": "source document",
            "allowed_routes": ["text", "retrieval"],
        },
    )

    monkeypatch.setattr(agent_task_manager, "current_utc_timestamp", lambda: "2026-04-02T10:10:00Z")
    monkeypatch.setattr(
        agent_task_manager,
        "_run_subagent_turn",
        lambda cfg, summary: {
            "turn_id": "turn-123",
            "route": "text",
            "runtime_owner": "text",
            "assistant": {"response": "Grounded answer", "source": "model"},
            "error": None,
            "skills": [],
            "tool": None,
            "execution": {"summary": {"total": 1}},
        },
    )

    result = run_task_worker(
        cfg,
        task_id="agent-task-888",
        kind=TASK_KIND_SUBAGENT,
    )
    saved = json.loads(summary_path.read_text(encoding="utf-8"))
    transcript_path = tmp_path / "agent_tasks" / "transcripts" / "agent-task-888.jsonl"

    assert result["status"] == TASK_STATUS_COMPLETED
    assert result["result"]["assistant_response"] == "Grounded answer"
    assert result["result"]["route"] == "text"
    assert saved["status"] == TASK_STATUS_COMPLETED
    assert transcript_path.is_file()
    transcript_row = json.loads(transcript_path.read_text(encoding="utf-8").strip())
    assert transcript_row["turn_id"] == "turn-123"
    assert transcript_row["assistant"]["response"] == "Grounded answer"


def test_run_subagent_turn_threads_current_task_id_into_nested_turn(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    summary_path, _ = _write_task_summary(
        tmp_path,
        task_id="agent-task-parent",
        kind=TASK_KIND_SUBAGENT,
        status=TASK_STATUS_PENDING,
        metadata={
            "prompt": "Review the latest estimate answer.",
            "request_source": "source document",
            "delegation_briefing": "Operator note: verify NEC grounding references.",
            "allowed_routes": ["text", "retrieval"],
        },
    )
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    captured: dict[str, object] = {}

    monkeypatch.setattr(
        agent_task_manager,
        "route_request",
        lambda cfg, prompt, source=None, section=None, attachments=None, tool_name=None: {
            "resolved_route": "text"
        },
    )

    import agent_shell

    monkeypatch.setattr(
        agent_shell,
        "resolve_agent_shell_settings",
        lambda cfg: {
            "enabled": True,
            "provider": "ollama",
            "model": "simcoe",
            "root_dir": str(tmp_path / "agent_shell"),
            "sessions_dir": str(tmp_path / "agent_shell" / "sessions"),
            "transcripts_dir": str(tmp_path / "agent_shell" / "transcripts"),
            "max_turns": 10,
            "temperature": 0.2,
            "max_output_tokens": 256,
            "ollama_base_url": "http://localhost:11434/v1",
            "openai_api_key_env": "OPENAI_API_KEY",
            "include_memory_in_text_routes": False,
            "include_retrieval_in_text_routes": False,
            "persist_context_sections": True,
        },
    )
    monkeypatch.setattr(
        agent_shell,
        "resolve_agent_shell_system_prompt",
        lambda cfg: ("system prompt", {}),
    )
    monkeypatch.setattr(
        agent_shell,
        "build_completion_fn",
        lambda settings: (lambda messages: "unused"),
    )

    def _fake_run_agent_turn(cfg: dict, settings: dict, prompt: str, **kwargs) -> dict:
        captured["prompt"] = prompt
        captured["source"] = kwargs.get("source")
        captured["parent_task_id"] = kwargs.get("parent_task_id")
        captured["delegation_briefing"] = kwargs.get("delegation_briefing")
        return {
            "turn_id": "turn-123",
            "route": "text",
            "runtime_owner": "text",
            "assistant": {"response": "Grounded answer", "source": "model"},
            "error": None,
            "skills": [],
            "tool": None,
            "execution": {"summary": {"total": 1}},
        }

    monkeypatch.setattr(agent_shell, "run_agent_turn", _fake_run_agent_turn)

    result = agent_task_manager._run_subagent_turn(cfg, summary)

    assert result["assistant"]["response"] == "Grounded answer"
    assert captured["prompt"] == (
        "### Delegation Briefing:\n"
        "Operator note: verify NEC grounding references.\n\n"
        "### Assigned Task:\n"
        "Review the latest estimate answer."
    )
    assert captured["source"] == "source document"
    assert captured["parent_task_id"] == "agent-task-parent"
    assert captured["delegation_briefing"] == (
        "Parent task id: agent-task-parent\n"
        "Parent worker: dream\n"
        "Parent request source: source document\n\n"
        "Inherited delegation context:\n"
        "Operator note: verify NEC grounding references.\n\n"
        "Parent assigned task:\n"
        "Review the latest estimate answer."
    )
