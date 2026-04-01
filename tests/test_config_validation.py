from __future__ import annotations

from copy import deepcopy

import pytest

from config_validation import (
    validate_memory_config,
    validate_multimodal_config,
    validate_routing_config,
)


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
        "managed_sources": {
            "root": "sources/managed/electricalai_docs",
            "reference_root": "sources/managed/electricalai_docs/retrieval/document",
            "estimating_reference_root": "sources/managed/electricalai_docs/retrieval/document/estimating",
            "estimating_pdf": "sources/managed/electricalai_docs/retrieval/document/estimating/2026_national_electrical_estimator_ebook.pdf",
            "estimating_har_dir": "sources/managed/electricalai_docs/manual_review/other/estimating/RSmeans",
            "code_training_reference_root": "sources/managed/electricalai_docs/retrieval/document/Electrical Code_Training",
            "drawings_reference_root": "sources/managed/electricalai_docs/retrieval/document/Drawings",
            "drawings_multimodal_root": "sources/managed/electricalai_docs/multimodal/image/Drawings",
            "revit_reference_root": "sources/managed/electricalai_docs/retrieval/document/Revit",
            "revit_family_dir": "sources/managed/electricalai_docs/geometry_rules/cad_bim/Revit/Families",
            "structured_root": "sources/managed/electricalai_docs/manual_review/tabular",
        },
        "multimodal": {
            "enabled_routes": ["drawing_sheet", "mixed"],
            "drawing_asset_root": "sources/managed/electricalai_docs/multimodal/image/Drawings",
            "observation_mode": "ocr_plus_layout",
            "ocr_enabled": True,
            "max_pages_per_document": 6,
            "max_images_per_request": 12,
            "max_observation_chars": 6000,
            "model_name": None,
            "processor_name": None,
        },
    }


def test_validate_multimodal_config_accepts_disabled_scaffold() -> None:
    validate_multimodal_config(_base_cfg())


def test_validate_multimodal_config_requires_model_when_enabled(
    capsys: pytest.CaptureFixture[str],
) -> None:
    cfg = _base_cfg()
    cfg["architecture"]["multimodal_runtime_enabled"] = True

    with pytest.raises(SystemExit):
        validate_multimodal_config(cfg)

    captured = capsys.readouterr()
    assert "multimodal.model_name is required" in captured.out


def test_validate_multimodal_config_rejects_overlapping_drawing_roots(
    capsys: pytest.CaptureFixture[str],
) -> None:
    cfg = _base_cfg()
    cfg["managed_sources"]["drawings_multimodal_root"] = (
        "sources/managed/electricalai_docs/retrieval/document/Drawings/sheets"
    )
    cfg["multimodal"]["drawing_asset_root"] = (
        "sources/managed/electricalai_docs/retrieval/document/Drawings/sheets"
    )

    with pytest.raises(SystemExit):
        validate_multimodal_config(cfg)

    captured = capsys.readouterr()
    assert "must be separate, non-overlapping paths" in captured.out


def test_validate_routing_config_rejects_multimodal_default_when_disabled(
    capsys: pytest.CaptureFixture[str],
) -> None:
    cfg = _base_cfg()
    cfg["routing"]["default_route"] = "drawing_sheet"

    with pytest.raises(SystemExit):
        validate_routing_config(cfg)

    captured = capsys.readouterr()
    assert "routing.default_route cannot require the multimodal runtime" in captured.out


def test_validate_routing_config_accepts_complete_route_map() -> None:
    cfg = deepcopy(_base_cfg())
    validate_routing_config(cfg)


def test_validate_memory_config_accepts_scaffold() -> None:
    validate_memory_config(
        {
            "memory": {
                "enabled": False,
                "root_dir": "data/memory",
                "index_path": "data/memory/MEMORY.json",
                "topics_dir": "data/memory/topics",
                "events_path": "data/memory/events.jsonl",
                "default_top_k": 3,
                "topic_candidate_limit": 8,
                "max_context_chars": 1200,
                "max_index_entries": 64,
                "max_summary_chars": 160,
                "max_supporting_observations": 3,
                "max_trace_results": 3,
                "max_trace_excluded": 3,
                "min_score": 2,
                "require_verification": True,
                "contradiction_policy": "mark_stale",
                "exclude_contradicted_topics": True,
                "import_max_records": 32,
                "allowed_kinds": ["operator_note", "verified_fact", "decision", "exception"],
                "exclude_statuses": ["stale", "retracted"],
                "consolidation_min_events": 8,
            }
        }
    )


def test_validate_memory_config_rejects_unknown_kind(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        validate_memory_config(
            {
                "memory": {
                    "enabled": False,
                    "root_dir": "data/memory",
                    "index_path": "data/memory/MEMORY.json",
                    "topics_dir": "data/memory/topics",
                    "events_path": "data/memory/events.jsonl",
                    "default_top_k": 3,
                    "topic_candidate_limit": 8,
                    "max_context_chars": 1200,
                    "max_index_entries": 64,
                    "max_summary_chars": 160,
                    "max_supporting_observations": 3,
                    "max_trace_results": 3,
                    "max_trace_excluded": 3,
                    "min_score": 2,
                    "require_verification": True,
                    "contradiction_policy": "mark_stale",
                    "exclude_contradicted_topics": True,
                    "import_max_records": 32,
                    "allowed_kinds": ["operator_note", "not_a_kind"],
                    "exclude_statuses": ["stale", "retracted"],
                    "consolidation_min_events": 8,
                }
            }
        )

    captured = capsys.readouterr()
    assert "memory.allowed_kinds contains unsupported values" in captured.out


def test_validate_memory_config_rejects_track_only_without_exclusion(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_memory_config(
            {
                "memory": {
                    "enabled": False,
                    "root_dir": "data/memory",
                    "index_path": "data/memory/MEMORY.json",
                    "topics_dir": "data/memory/topics",
                    "events_path": "data/memory/events.jsonl",
                    "default_top_k": 3,
                    "topic_candidate_limit": 8,
                    "max_context_chars": 1200,
                    "max_index_entries": 64,
                    "max_summary_chars": 160,
                    "max_supporting_observations": 3,
                    "max_trace_results": 3,
                    "max_trace_excluded": 3,
                    "min_score": 2,
                    "require_verification": True,
                    "contradiction_policy": "track_only",
                    "exclude_contradicted_topics": False,
                    "import_max_records": 32,
                    "allowed_kinds": ["operator_note", "verified_fact", "decision", "exception"],
                    "exclude_statuses": ["stale", "retracted"],
                    "consolidation_min_events": 8,
                }
            }
        )

    captured = capsys.readouterr()
    assert "memory.exclude_contradicted_topics must be true" in captured.out
