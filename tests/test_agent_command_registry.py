from __future__ import annotations

import agent_command_registry
import json
from pathlib import Path

import pytest

from agent_command_registry import (
    describe_agent_command,
    execute_agent_command,
    list_agent_commands,
    normalize_agent_command_name,
    render_agent_command_help,
)


def _write_skill(path: Path, *, skill_id: str, title: str, summary: str, trigger: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "---",
                f"id: {skill_id}",
                f"title: {title}",
                f"summary: {summary}",
                "aliases:",
                f"  - {trigger}",
                "tags:",
                f"  - {trigger}",
                "route_fit:",
                "  - text",
                "triggers:",
                f"  - {trigger}",
                "use_when: []",
                "avoid_when: []",
                "---",
                f"Use this skill when the prompt mentions {trigger}.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def test_list_agent_commands_reports_registry_order_and_aliases() -> None:
    commands = list_agent_commands()

    assert [command["name"] for command in commands] == [
        "help",
        "exit",
        "session",
        "commands",
        "skills",
        "tools",
        "providers",
        "route",
        "workflow",
        "tasks",
    ]
    assert commands[1]["aliases"] == ["quit"]


def test_normalize_agent_command_name_accepts_aliases() -> None:
    assert normalize_agent_command_name("/quit") == "exit"
    assert normalize_agent_command_name("commands") == "commands"


def test_describe_agent_command_returns_usage_examples() -> None:
    payload = describe_agent_command("workflow")

    assert payload["name"] == "workflow"
    assert payload["kind"] == "shell_command"
    assert "/workflow show <name>" in payload["usage_examples"]


def test_execute_agent_command_lists_and_shows_commands() -> None:
    result = execute_agent_command(
        {},
        {},
        {"session_id": "agent-shell-123"},
        "/commands",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    detail = execute_agent_command(
        {},
        {},
        {"session_id": "agent-shell-123"},
        "/commands show quit",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )

    payload = json.loads(result["response"])
    detail_payload = json.loads(detail["response"])
    assert payload["command_count"] == 10
    assert detail_payload["name"] == "exit"
    assert detail_payload["aliases"] == ["quit"]


def test_execute_agent_command_handles_quit_alias() -> None:
    result = execute_agent_command(
        {},
        {},
        {"session_id": "agent-shell-123"},
        "/quit",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )

    assert result == {"exit": True, "response": "Exiting agent shell."}


def test_render_agent_command_help_mentions_commands_surface() -> None:
    help_text = render_agent_command_help()

    assert "/commands" in help_text
    assert "/commands show <name>" in help_text
    assert "/skills" in help_text
    assert "/tasks" in help_text


def test_execute_agent_command_lists_and_shows_skills(tmp_path: Path) -> None:
    skills_dir = tmp_path / "skills"
    _write_skill(
        skills_dir / "electrical-estimating.md",
        skill_id="electrical-estimating",
        title="Electrical Estimating",
        summary="Structure estimate answers around labor and material assumptions.",
        trigger="estimate",
    )
    cfg = {
        "skill_registry": {
            "enabled": True,
            "root_dir": str(skills_dir),
            "max_active_skills": 2,
            "max_instruction_chars": 1200,
        }
    }

    result = execute_agent_command(
        cfg,
        {},
        {"session_id": "agent-shell-123"},
        "/skills",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    detail = execute_agent_command(
        cfg,
        {},
        {"session_id": "agent-shell-123"},
        "/skills show estimate",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )

    payload = json.loads(result["response"])
    detail_payload = json.loads(detail["response"])
    assert payload["skill_count"] == 1
    assert payload["skills"][0]["name"] == "electrical-estimating"
    assert detail_payload["name"] == "electrical-estimating"
    assert "Use this skill" in detail_payload["instructions"]


def test_execute_agent_command_can_pin_use_and_clear_skills(tmp_path: Path) -> None:
    skills_dir = tmp_path / "skills"
    _write_skill(
        skills_dir / "electrical-estimating.md",
        skill_id="electrical-estimating",
        title="Electrical Estimating",
        summary="Structure estimate answers around labor and material assumptions.",
        trigger="estimate",
    )
    cfg = {
        "skill_registry": {
            "enabled": True,
            "root_dir": str(skills_dir),
            "max_active_skills": 2,
            "max_instruction_chars": 1200,
        }
    }

    def update_session_skills(
        settings: dict,
        session_summary: dict,
        pinned_skill_names: list[str] | None,
        next_turn_skill_names: list[str] | None,
    ) -> dict:
        updated_summary = dict(session_summary)
        if pinned_skill_names is not None:
            updated_summary["pinned_skills"] = list(pinned_skill_names)
        if next_turn_skill_names is not None:
            updated_summary["next_turn_skills"] = list(next_turn_skill_names)
        return updated_summary

    session_summary = {
        "session_id": "agent-shell-123",
        "pinned_skills": [],
        "next_turn_skills": [],
    }
    pinned = execute_agent_command(
        cfg,
        {},
        session_summary,
        "/skills pin estimate",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
        update_session_skills_fn=update_session_skills,
    )
    active = execute_agent_command(
        cfg,
        {},
        pinned["session_summary"],
        "/skills active",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
        update_session_skills_fn=update_session_skills,
    )
    queued = execute_agent_command(
        cfg,
        {},
        pinned["session_summary"],
        "/skills use estimate",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
        update_session_skills_fn=update_session_skills,
    )
    cleared = execute_agent_command(
        cfg,
        {},
        queued["session_summary"],
        "/skills clear",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
        update_session_skills_fn=update_session_skills,
    )

    pinned_payload = json.loads(pinned["response"])
    active_payload = json.loads(active["response"])
    queued_payload = json.loads(queued["response"])
    cleared_payload = json.loads(cleared["response"])

    assert pinned_payload["pinned_skill_names"] == ["electrical-estimating"]
    assert active_payload["pinned_skills"][0]["name"] == "electrical-estimating"
    assert queued_payload["next_turn_skill_names"] == ["electrical-estimating"]
    assert cleared_payload["pinned_skill_names"] == []
    assert cleared_payload["next_turn_skill_names"] == []


def test_execute_agent_command_lists_statuses_starts_cancels_and_resumes_tasks(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}
    list_payload = {
        "task_count": 1,
        "active_task_count": 1,
        "restartable_task_count": 0,
        "tasks": [
            {
                "task_id": "agent-task-123",
                "kind": "workflow",
                "name": "demo",
                "status": "running",
                "active": True,
                "restartable": False,
            }
        ],
    }
    status_payload = {
        "task_count": 1,
        "active_task_count": 1,
        "restartable_task_count": 0,
        "recent_limit": 5,
        "recent_tasks": [
            {
                "task_id": "agent-task-123",
                "kind": "workflow",
                "name": "demo",
                "status": "running",
                "active": True,
                "restartable": False,
            }
        ],
        "active_tasks": [
            {
                "task_id": "agent-task-123",
                "kind": "workflow",
                "name": "demo",
                "status": "running",
                "active": True,
                "restartable": False,
            }
        ],
        "restartable_tasks": [],
        "filters": {"kind": None, "status": "running", "source": None},
        "by_status": {"running": 1},
        "by_kind": {"workflow": 1},
    }
    detail_payload = {
        "task": {
            "task_id": "agent-task-123",
            "kind": "workflow",
            "name": "demo",
            "status": "running",
            "restartable": False,
        },
        "log_tail": ["▶ step"],
    }
    attach_payload = {
        "task": {
            "task_id": "agent-task-123",
            "kind": "workflow",
            "name": "demo",
            "status": "running",
            "process_running": True,
        },
        "cursor": 1,
        "next_cursor": 2,
        "attached_lines": ["▶ step"],
        "stream_complete": False,
    }
    started_payload = {
        "task_id": "agent-task-456",
        "kind": "workflow",
        "name": "demo",
        "status": "running",
        "metadata": {"variables": {"output_path": "/tmp/out"}},
    }
    subagent_payload = {
        "task_id": "agent-task-sub",
        "kind": "subagent",
        "name": "worker",
        "status": "running",
        "metadata": {"parent_task_id": "agent-task-parent"},
    }
    dream_payload = {
        "task_id": "agent-task-789",
        "kind": "dream",
        "name": "dream",
        "status": "running",
    }
    cancelled_payload = {
        "task_id": "agent-task-456",
        "kind": "workflow",
        "name": "demo",
        "status": "running",
        "cancel_requested_at": "2026-04-01T12:00:00Z",
    }
    resumed_payload = {
        "task_id": "agent-task-999",
        "kind": "workflow",
        "name": "demo",
        "status": "running",
        "metadata": {"resumed_from_task_id": "agent-task-456"},
    }

    def _fake_list_agent_tasks(
        cfg: dict,
        task_kind: str | None = None,
        task_status: str | None = None,
        task_source: str | None = None,
    ) -> dict:
        captured["list_args"] = {
            "kind": task_kind,
            "status": task_status,
            "source": task_source,
        }
        return list_payload

    monkeypatch.setattr(agent_command_registry, "list_agent_tasks", _fake_list_agent_tasks)
    monkeypatch.setattr(
        agent_command_registry,
        "describe_agent_task",
        lambda cfg, task_id: detail_payload,
    )
    monkeypatch.setattr(
        agent_command_registry,
        "attach_agent_task",
        lambda cfg, task_id, cursor=0, limit=20: attach_payload,
    )
    monkeypatch.setattr(
        agent_command_registry,
        "summarize_agent_tasks",
        lambda cfg,
        task_kind=None,
        task_status=None,
        task_source=None,
        recent_limit=5: status_payload,
    )
    monkeypatch.setattr(
        agent_command_registry,
        "start_workflow_task",
        lambda cfg, config_path, workflow_name, extra_vars, source: started_payload,
    )
    monkeypatch.setattr(
        agent_command_registry,
        "start_dream_task",
        lambda cfg, config_path, source: dream_payload,
    )

    def _fake_start_subagent_task(
        cfg: dict,
        config_path: str,
        prompt: str,
        *,
        source: str = "operator",
        section: str | None = None,
        attachments: list[str] | None = None,
        explicit_skill_names: list[str] | tuple[str, ...] | None = None,
        explicit_tool_name: str | None = None,
        parent_task_id: str | None = None,
        agent_name: str | None = None,
        allowed_routes: list[str] | tuple[str, ...] | None = None,
    ) -> dict:
        captured["subagent_args"] = {
            "prompt": prompt,
            "source": source,
            "section": section,
            "attachments": list(attachments or []),
            "explicit_skill_names": list(explicit_skill_names or []),
            "explicit_tool_name": explicit_tool_name,
            "parent_task_id": parent_task_id,
            "agent_name": agent_name,
            "allowed_routes": list(allowed_routes or []),
        }
        return subagent_payload

    monkeypatch.setattr(
        agent_command_registry,
        "start_subagent_task",
        _fake_start_subagent_task,
    )
    monkeypatch.setattr(
        agent_command_registry,
        "cancel_agent_task",
        lambda cfg, task_id: cancelled_payload,
    )
    monkeypatch.setattr(
        agent_command_registry,
        "resume_agent_task",
        lambda cfg, task_id, source: resumed_payload,
    )

    session_summary = {"session_id": "agent-shell-123", "config_path": "config.yaml"}
    listed = execute_agent_command(
        {},
        {},
        session_summary,
        "/tasks list --status running --source agent_shell",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    status = execute_agent_command(
        {},
        {},
        session_summary,
        "/tasks status --status running",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    shown = execute_agent_command(
        {},
        {},
        session_summary,
        "/tasks show agent-task-123",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    attached = execute_agent_command(
        {},
        {},
        session_summary,
        "/tasks attach agent-task-123 --cursor 1 --limit 1",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    started = execute_agent_command(
        {},
        {},
        session_summary,
        "/tasks start workflow demo --var output_path=/tmp/out",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    dreamed = execute_agent_command(
        {},
        {},
        session_summary,
        "/tasks start dream",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    subagent_started = execute_agent_command(
        {},
        {},
        session_summary,
        '/tasks start subagent --prompt "Summarize the source section." --section module-1 --attachment source.pdf --skill estimate --tool-name estimate_lookup --parent-task-id agent-task-parent --agent-name worker --allow-route deterministic_tool',
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    cancelled = execute_agent_command(
        {},
        {},
        session_summary,
        "/tasks cancel agent-task-456",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )
    resumed = execute_agent_command(
        {},
        {},
        session_summary,
        "/tasks resume agent-task-456",
        describe_session_fn=lambda settings, session_id: {"session_id": session_id},
        describe_context_providers_fn=lambda cfg: {"active": []},
    )

    assert json.loads(listed["response"])["task_count"] == 1
    assert captured["list_args"] == {"kind": None, "status": "running", "source": "agent_shell"}
    assert json.loads(status["response"])["active_task_count"] == 1
    assert json.loads(shown["response"])["task"]["task_id"] == "agent-task-123"
    assert json.loads(attached["response"])["next_cursor"] == 2
    assert json.loads(started["response"])["task_id"] == "agent-task-456"
    assert json.loads(dreamed["response"])["kind"] == "dream"
    assert json.loads(subagent_started["response"])["kind"] == "subagent"
    assert captured["subagent_args"] == {
        "prompt": "Summarize the source section.",
        "source": "agent_shell_subagent",
        "section": "module-1",
        "attachments": ["source.pdf"],
        "explicit_skill_names": ["estimate"],
        "explicit_tool_name": "estimate_lookup",
        "parent_task_id": "agent-task-parent",
        "agent_name": "worker",
        "allowed_routes": ["deterministic_tool"],
    }
    assert json.loads(cancelled["response"])["cancel_requested_at"] == "2026-04-01T12:00:00Z"
    assert json.loads(resumed["response"])["metadata"]["resumed_from_task_id"] == "agent-task-456"
