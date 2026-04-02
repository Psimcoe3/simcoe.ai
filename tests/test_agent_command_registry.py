from __future__ import annotations

import json
from pathlib import Path

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
    assert payload["command_count"] == 9
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
