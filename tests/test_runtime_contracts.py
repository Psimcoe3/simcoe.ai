from __future__ import annotations

import pytest

from runtime_contracts import (
    EXECUTION_STATUS_SUCCEEDED,
    EXECUTION_SUBJECT_ROUTE,
    HOOK_ACTION_ANNOTATE,
    HOOK_STAGE_POST_CONTEXT_PROVIDER,
    FAIL_ROUTE_FALLBACK,
    TASK_KIND_SUBAGENT,
    TASK_KIND_WORKFLOW,
    TASK_STATUS_RUNNING,
    build_execution_envelope,
    normalize_context_provider,
    normalize_execution_status,
    normalize_execution_subject,
    normalize_hook_action,
    normalize_hook_stage,
    normalize_task_kind,
    normalize_task_status,
    ROUTE_RETRIEVAL,
    normalize_route_fallback,
    summarize_execution_envelopes,
    validate_route_contract,
)


def test_validate_route_contract_defaults_runtime_owner_for_retrieval() -> None:
    route, runtime_owner = validate_route_contract(
        ROUTE_RETRIEVAL,
        None,
        multimodal_enabled=False,
    )

    assert route == ROUTE_RETRIEVAL
    assert runtime_owner == "retrieval"


def test_validate_route_contract_rejects_multimodal_route_when_disabled() -> None:
    with pytest.raises(ValueError, match="requires architecture.multimodal_runtime_enabled=true"):
        validate_route_contract("drawing_sheet", None, multimodal_enabled=False)


def test_validate_route_contract_rejects_incompatible_runtime_owner() -> None:
    with pytest.raises(ValueError, match="invalid for"):
        validate_route_contract("deterministic_tool", "text", multimodal_enabled=False)


def test_normalize_route_fallback_accepts_fail_marker() -> None:
    assert normalize_route_fallback("fail", "routing.route_fallbacks.text") == FAIL_ROUTE_FALLBACK


def test_normalize_context_provider_accepts_memory() -> None:
    assert normalize_context_provider("memory") == "memory"


def test_normalize_hook_stage_and_action_accept_known_values() -> None:
    assert normalize_hook_stage("post_context_provider") == HOOK_STAGE_POST_CONTEXT_PROVIDER
    assert normalize_hook_action("annotate") == HOOK_ACTION_ANNOTATE


def test_normalize_execution_subject_and_status_accept_known_values() -> None:
    assert normalize_execution_subject("route") == EXECUTION_SUBJECT_ROUTE
    assert normalize_execution_status("succeeded") == EXECUTION_STATUS_SUCCEEDED


def test_normalize_task_kind_and_status_accept_known_values() -> None:
    assert normalize_task_kind("workflow") == TASK_KIND_WORKFLOW
    assert normalize_task_kind("subagent") == TASK_KIND_SUBAGENT
    assert normalize_task_status("running") == TASK_STATUS_RUNNING


def test_build_execution_envelope_and_summary_are_stable() -> None:
    envelope = build_execution_envelope(
        "route",
        "retrieval",
        "succeeded",
        owner="retrieval",
        details={"resolved_route": "retrieval"},
    )

    summary = summarize_execution_envelopes([envelope, None])

    assert envelope["schema_version"] == 1
    assert envelope["subject_type"] == "route"
    assert envelope["subject_name"] == "retrieval"
    assert envelope["status"] == "succeeded"
    assert summary["total"] == 1
    assert summary["by_subject_type"]["route"] == 1
    assert summary["by_subject"]["route:retrieval"] == 1
    assert summary["by_owner"]["retrieval"] == 1
