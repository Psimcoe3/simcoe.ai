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
        }
    }


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
    tasks_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    summary_path = tasks_dir / f"{task_id}.json"
    log_path = logs_dir / f"{task_id}.log"
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
    assert listed["tasks"][0]["task_id"] == "agent-task-123"
    assert listed["tasks"][0]["restartable"] is False
    assert detail["task"]["task_id"] == "agent-task-123"
    assert detail["task"]["restartable"] is False
    assert detail["log_tail"] == ["step 2"]


def test_summarize_agent_tasks_reports_active_restartable_and_filtered_views(
    tmp_path: Path,
) -> None:
    cfg = _task_cfg(tmp_path)
    _write_task_summary(
        tmp_path,
        task_id="agent-task-200",
        kind=TASK_KIND_WORKFLOW,
        status=TASK_STATUS_RUNNING,
        pid=200,
        source="agent_shell",
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

    assert summary["task_count"] == 2
    assert summary["active_task_count"] == 1
    assert summary["restartable_task_count"] == 1
    assert len(summary["recent_tasks"]) == 1
    assert summary["active_tasks"][0]["task_id"] == "agent-task-200"
    assert summary["restartable_tasks"][0]["task_id"] == "agent-task-100"
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
    assert captured["command"][4] == "worker"
    assert captured["command"][-1] == TASK_KIND_SUBAGENT
    assert parent_summary["metadata"]["child_task_ids"] == [task_id]
    assert parent_summary["last_child_task_id"] == task_id


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
        source: str = "operator",
        request_source: str | None = None,
        section: str | None = None,
        attachments: list[str] | None = None,
        explicit_skill_names: list[str] | tuple[str, ...] | None = None,
        explicit_tool_name: str | None = None,
        parent_task_id: str | None = None,
        agent_name: str | None = None,
        allowed_routes: list[str] | tuple[str, ...] | None = None,
        task_metadata: dict | None = None,
    ) -> dict:
        captured["source"] = source
        captured["request_source"] = request_source
        captured["section"] = section
        captured["attachments"] = attachments
        captured["parent_task_id"] = parent_task_id
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
    assert captured["request_source"] == "NCCER source"
    assert captured["section"] == "Module 1"
    assert captured["attachments"] == ["manual.pdf"]
    assert captured["parent_task_id"] == "agent-task-parent"
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

    assert result["status"] == TASK_STATUS_COMPLETED
    assert result["exit_code"] == 0
    assert result["result"]["workflow"] == "demo"
    assert saved["status"] == TASK_STATUS_COMPLETED


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

    assert result["status"] == TASK_STATUS_COMPLETED
    assert result["exit_code"] == 0
    assert result["result"]["status"] == "succeeded"


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

    assert result["status"] == TASK_STATUS_COMPLETED
    assert result["result"]["assistant_response"] == "Grounded answer"
    assert result["result"]["route"] == "text"
    assert saved["status"] == TASK_STATUS_COMPLETED
