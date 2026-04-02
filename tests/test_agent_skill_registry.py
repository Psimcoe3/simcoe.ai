from __future__ import annotations

from pathlib import Path

from agent_skill_registry import (
    describe_agent_skill,
    list_agent_skills,
    match_agent_skills,
    render_agent_skill_prompt,
    select_agent_skills,
)


def _write_skill(
    path: Path,
    *,
    skill_id: str,
    title: str,
    summary: str,
    aliases: list[str],
    tags: list[str],
    route_fit: list[str],
    triggers: list[str],
    instructions: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "---",
                f"id: {skill_id}",
                f"title: {title}",
                f"summary: {summary}",
                "aliases:",
                *[f"  - {entry}" for entry in aliases],
                "tags:",
                *[f"  - {entry}" for entry in tags],
                "route_fit:",
                *[f"  - {entry}" for entry in route_fit],
                "triggers:",
                *[f"  - {entry}" for entry in triggers],
                "use_when: []",
                "avoid_when: []",
                "---",
                instructions,
                "",
            ]
        ),
        encoding="utf-8",
    )


def _cfg(skills_dir: Path) -> dict:
    return {
        "skill_registry": {
            "enabled": True,
            "root_dir": str(skills_dir),
            "max_active_skills": 2,
            "max_instruction_chars": 1200,
        }
    }


def test_list_and_describe_agent_skills_load_markdown_frontmatter(tmp_path: Path) -> None:
    skills_dir = tmp_path / "skills"
    _write_skill(
        skills_dir / "electrical-estimating.md",
        skill_id="electrical-estimating",
        title="Electrical Estimating",
        summary="Structure estimates around scope and assumptions.",
        aliases=["estimate", "quote"],
        tags=["labor", "material"],
        route_fit=["text", "retrieval"],
        triggers=["estimate", "labor"],
        instructions="Keep labor and material assumptions explicit.",
    )

    skills = list_agent_skills(_cfg(skills_dir))
    detail = describe_agent_skill(_cfg(skills_dir), "quote")

    assert len(skills) == 1
    assert skills[0]["name"] == "electrical-estimating"
    assert detail["name"] == "electrical-estimating"
    assert detail["route_fit"] == ["text", "retrieval"]
    assert detail["instructions"] == "Keep labor and material assumptions explicit."


def test_match_agent_skills_prefers_trigger_and_route_fit(tmp_path: Path) -> None:
    skills_dir = tmp_path / "skills"
    _write_skill(
        skills_dir / "electrical-estimating.md",
        skill_id="electrical-estimating",
        title="Electrical Estimating",
        summary="Estimate guidance",
        aliases=["estimate"],
        tags=["material"],
        route_fit=["text"],
        triggers=["estimate", "labor"],
        instructions="Separate labor and material assumptions.",
    )
    _write_skill(
        skills_dir / "revit-family-reference.md",
        skill_id="revit-family-reference",
        title="Revit Family Reference",
        summary="Revit guidance",
        aliases=["revit"],
        tags=["family"],
        route_fit=["deterministic_tool"],
        triggers=["revit", "family type"],
        instructions="Preserve exact family and type labels.",
    )

    matches = match_agent_skills(
        _cfg(skills_dir),
        "Explain how to structure an estimate with labor and material assumptions.",
        route_name="text",
    )
    prompt = render_agent_skill_prompt(_cfg(skills_dir), matches)

    assert [match["name"] for match in matches] == ["electrical-estimating"]
    assert matches[0]["match_score"] >= 4
    assert "Electrical Estimating" in prompt
    assert "Separate labor and material assumptions." in prompt


def test_select_agent_skills_prioritizes_explicit_then_pinned_then_matches(tmp_path: Path) -> None:
    skills_dir = tmp_path / "skills"
    _write_skill(
        skills_dir / "electrical-estimating.md",
        skill_id="electrical-estimating",
        title="Electrical Estimating",
        summary="Estimate guidance",
        aliases=["estimate"],
        tags=["material"],
        route_fit=["text"],
        triggers=["estimate", "labor"],
        instructions="Separate labor and material assumptions.",
    )
    _write_skill(
        skills_dir / "revit-family-reference.md",
        skill_id="revit-family-reference",
        title="Revit Family Reference",
        summary="Revit guidance",
        aliases=["revit"],
        tags=["family"],
        route_fit=["deterministic_tool"],
        triggers=["revit", "family type"],
        instructions="Preserve exact family and type labels.",
    )

    selected = select_agent_skills(
        _cfg(skills_dir),
        "Explain how to structure an estimate with labor and material assumptions.",
        route_name="text",
        explicit_skill_names=["revit"],
        pinned_skill_names=["estimate"],
    )

    assert [skill["name"] for skill in selected] == [
        "revit-family-reference",
        "electrical-estimating",
    ]
    assert selected[0]["selection_sources"] == ["explicit"]
    assert selected[1]["selection_sources"] == ["pinned", "matched"]
