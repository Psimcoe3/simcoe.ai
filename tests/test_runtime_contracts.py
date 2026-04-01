from __future__ import annotations

import pytest

from runtime_contracts import (
    HOOK_ACTION_ANNOTATE,
    HOOK_STAGE_POST_CONTEXT_PROVIDER,
    FAIL_ROUTE_FALLBACK,
    normalize_context_provider,
    normalize_hook_action,
    normalize_hook_stage,
    ROUTE_RETRIEVAL,
    normalize_route_fallback,
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
