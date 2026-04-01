from __future__ import annotations

from build_golden_benchmark import _direct_tool_row_from_spec


def test_direct_tool_row_preserves_attachment_paths() -> None:
    row = _direct_tool_row_from_spec(
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
