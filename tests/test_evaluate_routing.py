from __future__ import annotations

import pytest

import evaluate
from evaluate import build_example_from_benchmark_row, build_execution_artifact
from runtime_contracts import build_execution_envelope


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
            "skill_names": ["electrical-estimating", "electrical-estimating"],
        },
        _base_cfg(),
        multimodal_enabled=False,
    )

    assert example["route"] == "retrieval"
    assert example["runtime_owner"] == "retrieval"
    assert example["routing_decision"]["resolved_route"] == "retrieval"
    assert example["skill_names"] == ["electrical-estimating"]


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


def test_execute_deterministic_tool_example_applies_hooks(monkeypatch: pytest.MonkeyPatch) -> None:
    cfg = _base_cfg()
    cfg["hooks"] = {
        "enabled": True,
        "rules": [
            {
                "name": "rewrite_tool_query",
                "stage": "pre_deterministic_tool",
                "action": "set_fields",
                "match": {"tool_name": "estimate_lookup"},
                "fields": {"request.query": "rewritten emt conduit"},
            },
            {
                "name": "annotate_tool_result",
                "stage": "post_deterministic_tool",
                "action": "annotate",
                "match": {"tool_name": "estimate_lookup"},
                "fields": {"policy": "audited"},
            },
        ],
    }

    captured: dict = {}

    def _fake_estimate_lookup(
        cfg: dict, request: dict, index_path: str | None = None, min_score: float | None = None
    ) -> dict:
        captured["request"] = request
        return {
            "tool_name": "estimate_lookup",
            "result_count": 1,
            "results": [{"description": request.get("query")}],
            "warnings": [],
        }

    monkeypatch.setattr(evaluate, "run_estimate_lookup_request", _fake_estimate_lookup)

    result = evaluate.execute_deterministic_tool_example(
        cfg,
        {
            "route": "deterministic_tool",
            "tool_name": "estimate_lookup",
            "tool_request": {"query": "emt conduit"},
            "tool_expectation": {"result_count_at_least": 1},
        },
    )

    assert captured["request"]["query"] == "rewritten emt conduit"
    assert result["passed"] is True
    assert result["hook_annotations"]["policy"] == "audited"
    assert result["execution_envelope"]["subject_type"] == "deterministic_tool"
    assert result["execution_envelope"]["status"] == "succeeded"


def test_build_execution_artifact_collects_structured_envelopes() -> None:
    examples = [
        {
            "route": "retrieval",
            "runtime_owner": "retrieval",
            "routing_decision": {
                "execution_envelope": build_execution_envelope(
                    "route",
                    "retrieval",
                    "succeeded",
                    owner="retrieval",
                    details={"resolved_route": "retrieval"},
                )
            },
        },
        {
            "route": "deterministic_tool",
            "runtime_owner": "geometry_rules",
            "tool_name": "estimate_lookup",
        },
    ]
    retrieval_traces = [
        {
            "context_providers": [
                {
                    "execution_envelope": build_execution_envelope(
                        "context_provider",
                        "memory",
                        "succeeded",
                        owner="memory",
                        details={"used": True},
                    )
                }
            ]
        },
        None,
    ]
    route_results = [
        None,
        {
            "execution_envelope": build_execution_envelope(
                "deterministic_tool",
                "estimate_lookup",
                "succeeded",
                owner="geometry_rules",
                details={"passed": True},
            )
        },
    ]

    artifact = build_execution_artifact(examples, retrieval_traces, route_results)

    assert artifact["schema_version"] == 1
    assert artifact["summary"]["total"] == 4
    assert artifact["summary"]["by_subject_type"]["route"] == 2
    assert artifact["summary"]["by_subject_type"]["context_provider"] == 1
    assert artifact["summary"]["by_subject_type"]["deterministic_tool"] == 1
    assert artifact["per_example"][1]["deterministic_tool"]["subject_name"] == "estimate_lookup"
