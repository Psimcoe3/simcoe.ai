from __future__ import annotations

import copy
import os

from data_contracts import stable_identifier
from hook_runtime import apply_hook_stage
from indexed_memory import format_memory_context, query_memory
from retrieval_utils import format_retrieved_context, load_jsonl, retrieve_documents
from runtime_contracts import (
    CONTEXT_PROVIDER_MEMORY,
    CONTEXT_PROVIDER_RETRIEVAL,
    EXECUTION_STATUS_DENIED,
    EXECUTION_STATUS_SKIPPED,
    EXECUTION_STATUS_SUCCEEDED,
    EXECUTION_SUBJECT_CONTEXT_PROVIDER,
    HOOK_STAGE_POST_CONTEXT_PROVIDER,
    HOOK_STAGE_PRE_CONTEXT_PROVIDER,
    build_execution_envelope,
    normalize_context_provider,
)


DEFAULT_CONTEXT_PROVIDER_ORDER = [
    CONTEXT_PROVIDER_MEMORY,
    CONTEXT_PROVIDER_RETRIEVAL,
]


def resolve_context_provider_settings(cfg: dict) -> dict:
    provider_cfg = (
        cfg.get("context_providers") if isinstance(cfg.get("context_providers"), dict) else {}
    )
    configured_order = provider_cfg.get("order")
    if isinstance(configured_order, list) and configured_order:
        order = [
            normalize_context_provider(item, "context_providers.order") for item in configured_order
        ]
    else:
        order = list(DEFAULT_CONTEXT_PROVIDER_ORDER)

    max_workers = provider_cfg.get("max_workers", 8)
    if isinstance(max_workers, bool) or not isinstance(max_workers, int) or max_workers < 1:
        max_workers = 8

    return {
        "order": order,
        "max_workers": max_workers,
    }


def active_context_provider_names(cfg: dict, order: list[str] | None = None) -> list[str]:
    resolved_order = list(order or resolve_context_provider_settings(cfg)["order"])
    retrieval_cfg = cfg.get("retrieval") if isinstance(cfg.get("retrieval"), dict) else {}
    memory_cfg = cfg.get("memory") if isinstance(cfg.get("memory"), dict) else {}

    active: list[str] = []
    for provider_name in resolved_order:
        if provider_name == CONTEXT_PROVIDER_MEMORY and bool(memory_cfg.get("enabled", False)):
            active.append(provider_name)
        if provider_name == CONTEXT_PROVIDER_RETRIEVAL and bool(
            retrieval_cfg.get("enabled", False)
        ):
            active.append(provider_name)
    return active


def _memory_request_id(example: dict, index: int, query: str) -> str:
    return stable_identifier(
        "evaluation_memory_query",
        example.get("benchmark_id") or f"example_{index}",
        query,
        example.get("source") or "",
        example.get("section") or "",
    )


def _coerce_optional_string(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    return cleaned or None


def _finalize_provider_result(
    provider_name: str,
    section_title: str,
    payload: dict,
    *,
    events: list[dict],
    annotations: dict,
    denied: bool = False,
    deny_reason: str | None = None,
) -> dict:
    trace = copy.deepcopy(payload)
    context = str(trace.pop("context", "") or "")
    trace.pop("section_title", None)
    trace.pop("benchmark_id", None)
    trace.pop("example_index", None)
    trace["provider"] = provider_name

    if denied:
        context = ""
        trace["used"] = False
        trace["denied"] = True
        trace["deny_reason"] = deny_reason

    if annotations:
        trace["hook_annotations"] = copy.deepcopy(annotations)
    if events:
        trace["hook_events"] = copy.deepcopy(events)
    if denied:
        execution_status = EXECUTION_STATUS_DENIED
    elif trace.get("queried") is False and not trace.get("used", False):
        execution_status = EXECUTION_STATUS_SKIPPED
    else:
        execution_status = EXECUTION_STATUS_SUCCEEDED

    envelope_details = {
        key: copy.deepcopy(value)
        for key, value in trace.items()
        if key not in {"provider", "hook_annotations", "hook_events", "execution_envelope"}
    }
    trace["execution_envelope"] = build_execution_envelope(
        EXECUTION_SUBJECT_CONTEXT_PROVIDER,
        provider_name,
        execution_status,
        owner=provider_name,
        details=envelope_details,
        hook_annotations=annotations,
        hook_events=events,
    )

    return {
        "provider": provider_name,
        "section_title": section_title,
        "context": context,
        "trace": trace,
    }


def _run_memory_provider(
    cfg: dict, memory_cfg: dict, example: dict, query: str, index: int
) -> dict:
    provider_name = CONTEXT_PROVIDER_MEMORY
    section_title = "Memory Hints"
    request_id = _memory_request_id(example, index, query)
    pre_payload = {
        "provider": provider_name,
        "query": query,
        "request_id": request_id,
        "benchmark_id": example.get("benchmark_id"),
        "example_index": index,
    }
    pre_hook = apply_hook_stage(cfg, HOOK_STAGE_PRE_CONTEXT_PROVIDER, pre_payload)
    hook_events = list(pre_hook["events"])
    annotations = dict(pre_hook["annotations"])
    if pre_hook["denied"]:
        return _finalize_provider_result(
            provider_name,
            section_title,
            {
                "query": query,
                "request_id": request_id,
                "used": False,
                "queried": False,
                "results": [],
                "excluded": [],
                "context": "",
            },
            events=hook_events,
            annotations=annotations,
            denied=True,
            deny_reason=pre_hook["deny_reason"],
        )

    hook_payload = pre_hook["payload"]
    effective_query = _coerce_optional_string(hook_payload.get("query")) or query
    effective_request_id = _coerce_optional_string(hook_payload.get("request_id")) or request_id
    memory_query = query_memory(
        cfg,
        effective_query,
        request_id=effective_request_id,
        trace_result_limit=int(memory_cfg.get("max_trace_results", 3) or 3),
        trace_excluded_limit=int(memory_cfg.get("max_trace_excluded", 3) or 3),
        supporting_observation_limit=int(memory_cfg.get("max_supporting_observations", 3) or 3),
    )
    context = format_memory_context(
        memory_query.get("results", []),
        int(memory_cfg.get("max_context_chars", 1200) or 1200),
    )
    post_payload = {
        "provider": provider_name,
        "query": effective_query,
        "request_id": memory_query.get("request_id", effective_request_id),
        "used": bool(memory_query.get("used")),
        "queried": True,
        "results": copy.deepcopy(
            memory_query.get("trace_results", memory_query.get("results", []))
        ),
        "excluded": copy.deepcopy(memory_query.get("excluded", [])),
        "context": context,
        "section_title": section_title,
        "benchmark_id": example.get("benchmark_id"),
        "example_index": index,
    }
    post_hook = apply_hook_stage(cfg, HOOK_STAGE_POST_CONTEXT_PROVIDER, post_payload)
    hook_events.extend(post_hook["events"])
    annotations = dict(post_hook["annotations"])
    return _finalize_provider_result(
        provider_name,
        section_title,
        post_hook["payload"],
        events=hook_events,
        annotations=annotations,
        denied=bool(post_hook["denied"]),
        deny_reason=post_hook["deny_reason"],
    )


def _run_retrieval_provider(
    cfg: dict,
    retrieval_cfg: dict,
    corpus: list[dict],
    example: dict,
    query: str,
    index: int,
) -> dict:
    provider_name = CONTEXT_PROVIDER_RETRIEVAL
    section_title = "Retrieved Context"
    preferred_source = example.get("source")
    preferred_section = example.get("section")
    pre_payload = {
        "provider": provider_name,
        "query": query,
        "preferred_source": preferred_source,
        "preferred_section": preferred_section,
        "benchmark_id": example.get("benchmark_id"),
        "example_index": index,
    }
    pre_hook = apply_hook_stage(cfg, HOOK_STAGE_PRE_CONTEXT_PROVIDER, pre_payload)
    hook_events = list(pre_hook["events"])
    annotations = dict(pre_hook["annotations"])
    if pre_hook["denied"]:
        return _finalize_provider_result(
            provider_name,
            section_title,
            {
                "query": query,
                "preferred_source": preferred_source,
                "preferred_section": preferred_section,
                "used": False,
                "context_included": False,
                "results": [],
                "context": "",
            },
            events=hook_events,
            annotations=annotations,
            denied=True,
            deny_reason=pre_hook["deny_reason"],
        )

    hook_payload = pre_hook["payload"]
    effective_query = _coerce_optional_string(hook_payload.get("query")) or query
    effective_source = _coerce_optional_string(
        hook_payload.get("preferred_source")
    ) or _coerce_optional_string(preferred_source)
    effective_section = _coerce_optional_string(
        hook_payload.get("preferred_section")
    ) or _coerce_optional_string(preferred_section)
    retrieved = retrieve_documents(
        effective_query,
        corpus,
        top_k=int(retrieval_cfg.get("top_k", 3)),
        min_score=float(retrieval_cfg.get("min_score", 1.0)),
        preferred_source=effective_source,
        preferred_section=effective_section,
    )
    context = format_retrieved_context(
        retrieved,
        max_context_chars=int(retrieval_cfg.get("max_context_chars", 1600) or 1600),
    )
    post_payload = {
        "provider": provider_name,
        "query": effective_query,
        "preferred_source": effective_source,
        "preferred_section": effective_section,
        "used": True,
        "context_included": bool(context.strip()),
        "results": [
            {
                "id": item.get("id"),
                "source": item.get("source"),
                "section": item.get("section"),
                "score": item.get("score"),
            }
            for item in retrieved
        ],
        "context": context,
        "section_title": section_title,
        "benchmark_id": example.get("benchmark_id"),
        "example_index": index,
    }
    post_hook = apply_hook_stage(cfg, HOOK_STAGE_POST_CONTEXT_PROVIDER, post_payload)
    hook_events.extend(post_hook["events"])
    annotations = dict(post_hook["annotations"])
    return _finalize_provider_result(
        provider_name,
        section_title,
        post_hook["payload"],
        events=hook_events,
        annotations=annotations,
        denied=bool(post_hook["denied"]),
        deny_reason=post_hook["deny_reason"],
    )


def build_context_provider_registry(cfg: dict) -> tuple[list[dict], dict]:
    settings = resolve_context_provider_settings(cfg)
    retrieval_cfg = cfg.get("retrieval") if isinstance(cfg.get("retrieval"), dict) else {}
    memory_cfg = cfg.get("memory") if isinstance(cfg.get("memory"), dict) else {}

    providers: list[dict] = []
    metadata = {
        "order": list(settings["order"]),
        "max_workers": settings["max_workers"],
        "active": [],
    }

    corpus: list[dict] | None = None
    corpus_path = _coerce_optional_string(retrieval_cfg.get("corpus_path"))
    for provider_name in settings["order"]:
        if provider_name == CONTEXT_PROVIDER_MEMORY and bool(memory_cfg.get("enabled", False)):
            providers.append(
                {
                    "name": provider_name,
                    "section_title": "Memory Hints",
                    "query_fn": lambda example,
                    query,
                    index,
                    cfg=cfg,
                    memory_cfg=memory_cfg: _run_memory_provider(
                        cfg,
                        memory_cfg,
                        example,
                        query,
                        index,
                    ),
                }
            )
            metadata["active"].append(provider_name)
        if provider_name == CONTEXT_PROVIDER_RETRIEVAL and bool(
            retrieval_cfg.get("enabled", False)
        ):
            if corpus is None and corpus_path is not None:
                corpus = load_jsonl(corpus_path)
            providers.append(
                {
                    "name": provider_name,
                    "section_title": "Retrieved Context",
                    "query_fn": lambda example,
                    query,
                    index,
                    cfg=cfg,
                    retrieval_cfg=retrieval_cfg,
                    corpus=corpus or []: _run_retrieval_provider(
                        cfg,
                        retrieval_cfg,
                        corpus,
                        example,
                        query,
                        index,
                    ),
                }
            )
            metadata["active"].append(provider_name)

    if corpus_path is not None and corpus is not None:
        metadata["corpus_path"] = os.path.abspath(corpus_path)
        metadata["corpus_size"] = len(corpus)
        metadata["top_k"] = int(retrieval_cfg.get("top_k", 3))
        metadata["max_context_chars"] = int(retrieval_cfg.get("max_context_chars", 1600))
        metadata["min_score"] = float(retrieval_cfg.get("min_score", 1.0))

    return providers, metadata
