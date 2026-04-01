from __future__ import annotations

import pytest

from request_router import route_request


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
            "revit_entity_lookup": {"enabled": True},
        },
    }


def test_route_request_uses_retrieval_for_grounded_reference_queries() -> None:
    decision = route_request(
        _base_cfg(),
        "Summarize the electrical construction reference source Module Nine.",
        source="NCCER Electrical Guides / NCCER Level 1 Trainee Guide",
    )

    assert decision["requested_route"] == "retrieval"
    assert decision["resolved_route"] == "retrieval"
    assert decision["runtime_owner"] == "retrieval"


def test_route_request_uses_deterministic_tool_for_lookup_queries() -> None:
    decision = route_request(
        _base_cfg(),
        "Find the estimate lookup for EMT conduit.",
    )

    assert decision["requested_route"] == "deterministic_tool"
    assert decision["resolved_route"] == "deterministic_tool"
    assert decision["runtime_owner"] == "geometry_rules"


def test_route_request_blocks_drawing_sheet_when_multimodal_is_disabled() -> None:
    with pytest.raises(ValueError, match="fallback policy is 'fail'"):
        route_request(
            _base_cfg(),
            "Review this drawing sheet and tell me what panel schedule it shows.",
            attachments=["Drawings/Plan Set/A101.pdf"],
        )


def test_route_request_allows_drawing_sheet_when_multimodal_is_enabled() -> None:
    cfg = _base_cfg()
    cfg["architecture"]["multimodal_runtime_enabled"] = True

    decision = route_request(
        cfg,
        "Review this drawing sheet and tell me what panel schedule it shows.",
        attachments=["Drawings/Plan Set/A101.pdf"],
    )

    assert decision["requested_route"] == "drawing_sheet"
    assert decision["resolved_route"] == "drawing_sheet"
    assert decision["runtime_owner"] == "multimodal"
