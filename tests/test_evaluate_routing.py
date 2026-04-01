from __future__ import annotations

import pytest

from evaluate import build_example_from_benchmark_row


def _base_cfg() -> dict:
    return {
        "architecture": {
            "system_type": "grounded_multi_runtime",
            "primary_runtime": "text",
            "multimodal_runtime_enabled": False,
            "retrieval_layer_enabled": True,
            "geometry_rules_enabled": False,
            "grounded_answers_require_retrieval": True,
        },
        "routing": {
            "default_route": "text",
            "route_fallbacks": {
                "text": "fail",
                "retrieval": "text",
                "deterministic_tool": "text",
                "drawing_sheet": "fail",
                "mixed": "fail",
            },
            "latency_budgets_ms": {
                "text": 1800,
                "retrieval": 2600,
                "deterministic_tool": 1200,
                "drawing_sheet": 5000,
                "mixed": 6500,
            },
        },
        "retrieval": {
            "enabled": True,
        },
        "deterministic_tools": {
            "estimate_lookup": {"enabled": True},
        },
    }


def test_build_example_from_benchmark_row_infers_retrieval_route() -> None:
    example = build_example_from_benchmark_row(
        {
            "benchmark_id": "nccer-001",
            "instruction": "Summarize the electrical construction reference source Module Nine.",
            "source": "NCCER Electrical Guides / NCCER Level 1 Trainee Guide",
            "response": "A summary",
        },
        _base_cfg(),
        multimodal_enabled=False,
    )

    assert example["route"] == "retrieval"
    assert example["runtime_owner"] == "retrieval"
    assert example["routing_decision"]["resolved_route"] == "retrieval"


def test_build_example_from_benchmark_row_blocks_drawing_sheet_without_runtime() -> None:
    with pytest.raises(SystemExit, match="routing failed"):
        build_example_from_benchmark_row(
            {
                "benchmark_id": "drawing-001",
                "instruction": "Review this drawing sheet and explain the panel schedule.",
                "attachment_paths": ["Drawings/Plan Set/A101.pdf"],
                "response": "Panel schedule details",
            },
            _base_cfg(),
            multimodal_enabled=False,
        )
