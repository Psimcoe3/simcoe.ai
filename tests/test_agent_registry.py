from __future__ import annotations

from pathlib import Path

import pytest

from agent_registry import (
    describe_agent_definition,
    list_agent_definitions,
    resolve_agent_definition_task_defaults,
)


def _write_skill(path: Path, *, skill_id: str, title: str, summary: str, alias: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "---",
                f"id: {skill_id}",
                f"title: {title}",
                f"summary: {summary}",
                "aliases:",
                f"  - {alias}",
                "tags: []",
                "route_fit:",
                "  - text",
                "triggers:",
                f"  - {alias}",
                "use_when: []",
                "avoid_when: []",
                "---",
                "Keep the answer grounded.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def _write_agent(
    path: Path,
    *,
    agent_id: str,
    title: str,
    summary: str,
    aliases: list[str],
    skill_names: list[str],
    allowed_routes: list[str],
    tool_name: str | None,
    section: str | None,
    instructions: str,
) -> None:
    lines = [
        "---",
        f"id: {agent_id}",
        f"title: {title}",
        f"summary: {summary}",
        "aliases:",
        *[f"  - {entry}" for entry in aliases],
        "skill_names:",
        *[f"  - {entry}" for entry in skill_names],
        "allowed_routes:",
        *[f"  - {entry}" for entry in allowed_routes],
        "use_when: []",
        "avoid_when: []",
    ]
    if tool_name is not None:
        lines.append(f"tool_name: {tool_name}")
    if section is not None:
        lines.append(f"section: {section}")
    lines.extend(["---", instructions, ""])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _cfg(tmp_path: Path) -> dict:
    skills_dir = tmp_path / "skills"
    agents_dir = tmp_path / "agents"
    _write_skill(
        skills_dir / "electrical-estimating.md",
        skill_id="electrical-estimating",
        title="Electrical Estimating",
        summary="Estimate guidance",
        alias="estimate",
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


def test_list_and_describe_agent_definitions_load_markdown_frontmatter(tmp_path: Path) -> None:
    cfg = _cfg(tmp_path)
    _write_agent(
        Path(cfg["agent_registry"]["root_dir"]) / "estimate-reviewer.md",
        agent_id="estimate-reviewer",
        title="Estimate Reviewer",
        summary="Review estimate gaps",
        aliases=["estimate-review"],
        skill_names=["estimate"],
        allowed_routes=["text", "retrieval"],
        tool_name=None,
        section="estimate-section",
        instructions="Review grounded estimate gaps.",
    )

    agents = list_agent_definitions(cfg)
    detail = describe_agent_definition(cfg, "estimate-review")

    assert len(agents) == 1
    assert agents[0]["name"] == "estimate-reviewer"
    assert agents[0]["skill_names"] == ["electrical-estimating"]
    assert detail["name"] == "estimate-reviewer"
    assert detail["allowed_routes"] == ["text", "retrieval"]
    assert detail["section"] == "estimate-section"
    assert detail["instructions"] == "Review grounded estimate gaps."


def test_resolve_agent_definition_task_defaults_returns_task_ready_defaults(
    tmp_path: Path,
) -> None:
    cfg = _cfg(tmp_path)
    _write_agent(
        Path(cfg["agent_registry"]["root_dir"]) / "estimate-reviewer.md",
        agent_id="estimate-reviewer",
        title="Estimate Reviewer",
        summary="Review estimate gaps",
        aliases=["estimate-review"],
        skill_names=["estimate"],
        allowed_routes=["deterministic_tool"],
        tool_name="estimate_lookup",
        section="estimate-section",
        instructions="Review grounded estimate gaps.",
    )

    defaults = resolve_agent_definition_task_defaults(cfg, "estimate-review")

    assert defaults == {
        "agent_definition_name": "estimate-reviewer",
        "title": "Estimate Reviewer",
        "instructions": "Review grounded estimate gaps.",
        "section": "estimate-section",
        "explicit_skill_names": ["electrical-estimating"],
        "explicit_tool_name": "estimate_lookup",
        "allowed_routes": ["deterministic_tool"],
    }


def test_list_agent_definitions_rejects_deterministic_route_without_tool(tmp_path: Path) -> None:
    cfg = _cfg(tmp_path)
    _write_agent(
        Path(cfg["agent_registry"]["root_dir"]) / "broken-agent.md",
        agent_id="broken-agent",
        title="Broken Agent",
        summary="Invalid deterministic route",
        aliases=[],
        skill_names=[],
        allowed_routes=["deterministic_tool"],
        tool_name=None,
        section=None,
        instructions="Do the invalid thing.",
    )

    with pytest.raises(ValueError, match="cannot include deterministic_tool without tool_name"):
        list_agent_definitions(cfg)
