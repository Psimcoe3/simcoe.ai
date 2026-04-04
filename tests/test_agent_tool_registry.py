from __future__ import annotations

import agent_tool_registry
import pytest
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


def _cfg_with_delegate(tmp_path) -> dict:
    agents_dir = tmp_path / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    (agents_dir / "estimate-reviewer.md").write_text(
        "\n".join(
            [
                "---",
                "id: estimate-reviewer",
                "title: Estimate Reviewer",
                "summary: Review estimate gaps.",
                "aliases:",
                "  - estimate-review",
                "skill_names: []",
                "allowed_routes:",
                "  - text",
                "use_when: []",
                "avoid_when: []",
                "---",
                "Review grounded estimate gaps.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return {
        "deterministic_tools": {
            "delegate_to_subagent": {"enabled": True},
            "estimate_lookup": {"enabled": True},
            "revit_entity_lookup": {"enabled": False},
        },
        "agent_registry": {
            "enabled": True,
            "root_dir": str(agents_dir),
        },
        "agent_task_manager": {
            "enabled": True,
            "root_dir": str(tmp_path / "agent_tasks"),
            "tasks_dir": str(tmp_path / "agent_tasks" / "tasks"),
            "logs_dir": str(tmp_path / "agent_tasks" / "logs"),
        },
    }


def test_list_agent_tools_reports_resolved_metadata() -> None:
    tools = list_agent_tools(_cfg())

    assert [tool["name"] for tool in tools] == [
        "estimate_lookup",
        "revit_entity_lookup",
        "delegate_to_subagent",
    ]
    assert tools[0]["access_mode"] == "read_only"
    assert tools[0]["resolved_settings"]["default_top_k"] == 7
    assert tools[0]["resolved_settings"]["default_quantity"] == 2.0
    assert tools[1]["enabled"] is False
    assert tools[2]["enabled"] is False
    assert tools[2]["access_mode"] == "mutating"


def test_infer_agent_tool_name_supports_aliases_and_revit_markers() -> None:
    assert infer_agent_tool_name("Show the revit family and type metadata") == "revit_entity_lookup"
    assert infer_agent_tool_name("Find the cost for EMT conduit") == "estimate_lookup"
    assert (
        infer_agent_tool_name("Delegate to estimate-reviewer: review the latest estimate answer.")
        == "delegate_to_subagent"
    )
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


def test_execute_agent_tool_can_delegate_to_named_subagent(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path,
) -> None:
    cfg = _cfg_with_delegate(tmp_path)
    request = build_tool_request(
        "delegate_to_subagent",
        query=(
            "### Agent Instructions:\n"
            "Review grounded estimate gaps.\n\n"
            "### Assigned Task:\n"
            "Delegate to estimate-review: Review the latest estimate answer."
        ),
        filters={
            "source": "operator",
            "parent_task_id": "agent-task-parent",
            "delegation_briefing": "Check grounded conduit references before answering.",
        },
    )
    request["config_path"] = "config.yaml"
    captured: dict[str, object] = {}

    def _fake_start_subagent_task(
        cfg: dict,
        config_path: str,
        prompt: str,
        *,
        agent_definition_name: str | None = None,
        agent_instructions: str | None = None,
        source: str = "operator",
        request_source: str | None = None,
        section: str | None = None,
        attachments: list[str] | None = None,
        explicit_skill_names: list[str] | tuple[str, ...] | None = None,
        explicit_tool_name: str | None = None,
        parent_task_id: str | None = None,
        delegation_briefing: str | None = None,
        agent_name: str | None = None,
        allowed_routes: list[str] | tuple[str, ...] | None = None,
        task_metadata: dict | None = None,
    ) -> dict:
        captured["args"] = {
            "config_path": config_path,
            "prompt": prompt,
            "agent_definition_name": agent_definition_name,
            "source": source,
            "request_source": request_source,
            "section": section,
            "attachments": list(attachments or []),
            "parent_task_id": parent_task_id,
            "delegation_briefing": delegation_briefing,
        }
        return {
            "task_id": "agent-task-123",
            "kind": "subagent",
            "name": "Estimate Reviewer",
            "status": "running",
            "source": source,
            "config_path": config_path,
            "summary_path": str(tmp_path / "agent_tasks" / "tasks" / "agent-task-123.json"),
            "log_path": str(tmp_path / "agent_tasks" / "logs" / "agent-task-123.log"),
            "metadata": {
                "agent_definition_name": agent_definition_name,
                "parent_task_id": parent_task_id,
            },
        }

    monkeypatch.setattr(agent_tool_registry, "start_subagent_task", _fake_start_subagent_task)

    result = execute_agent_tool(
        cfg,
        "delegate",
        request,
        route_name="deterministic_tool",
    )

    assert result["tool_name"] == "delegate_to_subagent"
    assert result["response"]["response_type"] == "task_result"
    assert result["response"]["task"]["task_id"] == "agent-task-123"
    assert result["response"]["task"]["parent_task_id"] == "agent-task-parent"
    assert "agent-task-123" in result["assistant_response"]
    assert result["execution_envelope"]["status"] == "succeeded"
    assert captured["args"] == {
        "config_path": "config.yaml",
        "prompt": "Review the latest estimate answer.",
        "agent_definition_name": "estimate-reviewer",
        "source": "agent_shell_delegate",
        "request_source": "operator",
        "section": None,
        "attachments": [],
        "parent_task_id": "agent-task-parent",
        "delegation_briefing": "Check grounded conduit references before answering.",
    }
