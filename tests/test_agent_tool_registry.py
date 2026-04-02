from __future__ import annotations

from agent_tool_registry import (
    describe_agent_tool,
    execute_agent_tool,
    infer_agent_tool_name,
    list_agent_tools,
)
from deterministic_tool_utils import build_tool_request


def _cfg() -> dict:
    return {
        "deterministic_tools": {
            "estimate_lookup": {
                "enabled": True,
                "index_path": "data/raw/estimate_index.jsonl",
                "default_top_k": 7,
                "max_results": 9,
                "min_score": 3.5,
                "default_quantity": 2.0,
            },
            "revit_entity_lookup": {
                "enabled": False,
                "index_path": "data/raw/revit_family_index.jsonl",
                "default_top_k": 4,
                "max_results": 6,
                "min_score": 2.5,
            },
        }
    }


def test_list_agent_tools_reports_resolved_metadata() -> None:
    tools = list_agent_tools(_cfg())

    assert [tool["name"] for tool in tools] == [
        "estimate_lookup",
        "revit_entity_lookup",
    ]
    assert tools[0]["access_mode"] == "read_only"
    assert tools[0]["resolved_settings"]["default_top_k"] == 7
    assert tools[0]["resolved_settings"]["default_quantity"] == 2.0
    assert tools[1]["enabled"] is False


def test_infer_agent_tool_name_supports_aliases_and_revit_markers() -> None:
    assert infer_agent_tool_name("Show the revit family and type metadata") == "revit_entity_lookup"
    assert infer_agent_tool_name("Find the cost for EMT conduit") == "estimate_lookup"
    assert infer_agent_tool_name("anything", explicit_tool_name="estimate") == "estimate_lookup"


def test_execute_agent_tool_returns_disabled_error_for_disabled_tool() -> None:
    cfg = _cfg()
    request = build_tool_request("revit_entity_lookup", query="panelboard")

    result = execute_agent_tool(
        cfg,
        "revit",
        request,
        route_name="deterministic_tool",
    )

    assert result["tool_name"] == "revit_entity_lookup"
    assert result["response"]["response_type"] == "error"
    assert result["response"]["error"]["code"] == "disabled"
    assert "disabled" in result["assistant_response"]
    assert result["execution_envelope"]["status"] == "failed"


def test_describe_agent_tool_normalizes_aliases() -> None:
    payload = describe_agent_tool(_cfg(), "revit-lookup")

    assert payload["name"] == "revit_entity_lookup"
    assert payload["enabled"] is False
    assert payload["resolved_settings"]["default_top_k"] == 4
