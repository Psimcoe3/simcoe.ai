from __future__ import annotations

from pathlib import Path

import pytest

from generate_data import build_generation_user_prompt


def _write_skill(
    path: Path,
    *,
    skill_id: str,
    title: str,
    summary: str,
    aliases: list[str],
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
                "tags: []",
                "route_fit:",
                "  - text",
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


def _cfg(tmp_path: Path) -> dict:
    skills_dir = tmp_path / "skills"
    _write_skill(
        skills_dir / "electrical-estimating.md",
        skill_id="electrical-estimating",
        title="Electrical Estimating",
        summary="Estimate guidance",
        aliases=["estimate"],
        triggers=["estimate", "labor"],
        instructions="Separate labor and material assumptions.",
    )
    _write_skill(
        skills_dir / "revit-family-reference.md",
        skill_id="revit-family-reference",
        title="Revit Family Reference",
        summary="Revit guidance",
        aliases=["revit"],
        triggers=["revit", "family type"],
        instructions="Preserve exact family and type labels.",
    )
    return {
        "skill_registry": {
            "enabled": True,
            "root_dir": str(skills_dir),
            "max_active_skills": 2,
            "max_instruction_chars": 1200,
        }
    }


def test_build_generation_user_prompt_requires_config_for_explicit_skills() -> None:
    with pytest.raises(ValueError, match="requested local skills"):
        build_generation_user_prompt(
            {
                "name": "Electrical estimating",
                "description": "Estimate conduit runs.",
            },
            5,
            explicit_skill_names=["electrical-estimating"],
        )


def test_build_generation_user_prompt_applies_explicit_and_topic_skills(tmp_path: Path) -> None:
    prompt, metadata = build_generation_user_prompt(
        {
            "name": "Electrical estimating",
            "description": "Estimate conduit runs.",
            "example_styles": "pricing guidance",
            "skill_names": ["estimate"],
        },
        5,
        cfg=_cfg(tmp_path),
        explicit_skill_names=["revit"],
    )

    assert prompt.startswith("### Active Skills:")
    assert "Electrical Estimating" in prompt
    assert "Revit Family Reference" in prompt
    assert metadata["global_skill_names"] == ["revit"]
    assert metadata["topic_skill_names"] == ["estimate"]
    assert metadata["selected_skill_names"] == [
        "revit-family-reference",
        "electrical-estimating",
    ]
    assert metadata["selected_skills"][0]["selection_sources"] == ["explicit"]


def test_build_generation_user_prompt_auto_matches_topic_text(tmp_path: Path) -> None:
    prompt, metadata = build_generation_user_prompt(
        {
            "name": "Electrical estimating",
            "description": "Structure labor and material estimate guidance.",
            "example_styles": "scenario-based estimating",
        },
        5,
        cfg=_cfg(tmp_path),
    )

    assert "Electrical Estimating" in prompt
    assert metadata["used"] is True
    assert metadata["selected_skill_names"] == ["electrical-estimating"]
    assert metadata["selected_skills"][0]["selection_sources"] == ["matched"]
