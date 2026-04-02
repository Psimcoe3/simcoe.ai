from __future__ import annotations

from pathlib import Path

import pytest

from build_golden_benchmark import _direct_tool_row_from_spec, _validated_skill_names_from_spec


def _write_skill(
    path: Path,
    *,
    skill_id: str,
    title: str,
    summary: str,
    aliases: list[str],
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
                "  - retrieval",
                "triggers: []",
                "use_when: []",
                "avoid_when: []",
                "---",
                "Use this skill when it applies.",
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
    )
    return {
        "skill_registry": {
            "enabled": True,
            "root_dir": str(skills_dir),
            "max_active_skills": 2,
            "max_instruction_chars": 1200,
        }
    }


def test_direct_tool_row_preserves_attachment_paths(tmp_path: Path) -> None:
    row = _direct_tool_row_from_spec(
        _cfg(tmp_path),
        {
            "instruction": "Review this drawing sheet and find the panel schedule.",
            "tool_name": "estimate_lookup",
            "tool_request": {"query": "panel schedule"},
            "tool_expectation": {"result_count_at_least": 1},
            "attachment_paths": [" Drawings/Plan Set/A101.pdf ", ""],
        },
        1,
        "drawing-tool-001",
        "drawing_sheet",
        multimodal_enabled=True,
    )

    assert row["attachment_paths"] == ["Drawings/Plan Set/A101.pdf"]
    assert row["skill_names"] == []


def test_direct_tool_row_normalizes_skill_names(tmp_path: Path) -> None:
    row = _direct_tool_row_from_spec(
        _cfg(tmp_path),
        {
            "instruction": "Review this drawing sheet and find the panel schedule.",
            "tool_name": "estimate_lookup",
            "tool_request": {"query": "panel schedule"},
            "tool_expectation": {"result_count_at_least": 1},
            "skill_names": ["estimate", "electrical-estimating", "estimate"],
        },
        1,
        "drawing-tool-001",
        "drawing_sheet",
        multimodal_enabled=True,
    )

    assert row["skill_names"] == ["electrical-estimating"]


def test_validated_skill_names_from_spec_rejects_unknown_skill(tmp_path: Path) -> None:
    with pytest.raises(SystemExit, match="Spec entry 2 skill_names are invalid"):
        _validated_skill_names_from_spec(
            _cfg(tmp_path),
            {"skill_names": ["unknown-skill"]},
            index=2,
        )
