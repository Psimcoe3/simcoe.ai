"""
Stable request and response envelopes for deterministic lookup runtimes.
"""

from __future__ import annotations

import json
import os

from data_contracts import stable_identifier
from manifest_utils import current_utc_timestamp


TOOL_SCHEMA_VERSION = 1


def _clean_filters(filters: dict | None) -> dict:
    cleaned: dict[str, object] = {}
    if not isinstance(filters, dict):
        return cleaned

    for key, value in sorted(filters.items()):
        if value is None:
            continue
        if isinstance(value, str):
            stripped = value.strip()
            if stripped:
                cleaned[key] = stripped
            continue
        cleaned[key] = value
    return cleaned


def build_tool_request(
    tool_name: str,
    *,
    query: str | None = None,
    record_id: str | None = None,
    lookup_key: str | None = None,
    filters: dict | None = None,
    top_k: int | None = None,
    quantity: float | None = None,
) -> dict:
    cleaned_filters = _clean_filters(filters)
    cleaned_query = query.strip() if isinstance(query, str) and query.strip() else None
    cleaned_record_id = (
        record_id.strip() if isinstance(record_id, str) and record_id.strip() else None
    )
    cleaned_lookup_key = (
        lookup_key.strip() if isinstance(lookup_key, str) and lookup_key.strip() else None
    )

    request_id = stable_identifier(
        "deterministic_tool_request",
        tool_name,
        cleaned_query,
        cleaned_record_id,
        cleaned_lookup_key,
        json.dumps(cleaned_filters, sort_keys=True),
        top_k if top_k is not None else "",
        quantity if quantity is not None else "",
    )

    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "request_id": request_id,
        "tool_name": tool_name,
        "query": cleaned_query,
        "record_id": cleaned_record_id,
        "lookup_key": cleaned_lookup_key,
        "filters": cleaned_filters,
        "top_k": top_k,
        "quantity": quantity,
    }


def build_tool_response(
    tool_name: str,
    *,
    request: dict,
    results: list[dict],
    index_path: str,
    warnings: list[str] | None = None,
    provenance: dict | None = None,
    runtime_owner: str = "geometry_rules",
) -> dict:
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool_name": tool_name,
        "runtime_owner": runtime_owner,
        "response_type": "lookup_result",
        "generated_at": current_utc_timestamp(),
        "request": request,
        "result_count": len(results),
        "results": results,
        "warnings": warnings or [],
        "provenance": {
            "index_path": os.path.abspath(index_path),
            **(provenance or {}),
        },
    }


def build_tool_error(
    tool_name: str,
    *,
    request: dict,
    message: str,
    code: str = "tool_error",
    runtime_owner: str = "geometry_rules",
) -> dict:
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool_name": tool_name,
        "runtime_owner": runtime_owner,
        "response_type": "error",
        "generated_at": current_utc_timestamp(),
        "request": request,
        "error": {
            "code": code,
            "message": message,
        },
    }
