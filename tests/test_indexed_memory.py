from __future__ import annotations

import json

from indexed_memory import (
    consolidate_memory,
    import_memory_entries,
    query_memory,
    record_memory_entry,
)
from manifest_utils import read_json_file


def _cfg(tmp_path) -> dict:
    root_dir = tmp_path / "memory"
    return {
        "memory": {
            "enabled": True,
            "provider": "file",
            "root_dir": str(root_dir),
            "index_path": str(root_dir / "MEMORY.json"),
            "topics_dir": str(root_dir / "topics"),
            "events_path": str(root_dir / "events.jsonl"),
            "default_top_k": 3,
            "topic_candidate_limit": 8,
            "max_context_chars": 1200,
            "max_index_entries": 64,
            "max_summary_chars": 120,
            "max_supporting_observations": 3,
            "max_trace_results": 3,
            "max_trace_excluded": 3,
            "min_score": 1,
            "require_verification": True,
            "contradiction_policy": "mark_stale",
            "exclude_contradicted_topics": True,
            "import_max_records": 16,
            "allowed_kinds": ["operator_note", "verified_fact", "decision", "exception"],
            "exclude_statuses": ["stale", "retracted"],
            "consolidation_min_events": 2,
        }
    }


def test_record_memory_entry_materializes_event_topic_and_index(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    event = record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="Prefer verified grounding notes",
        content="Use verified NCCER grounding guidance before falling back to generic notes.",
        kind="verified_fact",
        verification_status="verified",
        tags=["grounding", "nccer"],
    )

    events_path = tmp_path / "memory" / "events.jsonl"
    index_path = tmp_path / "memory" / "MEMORY.json"
    topic_path = tmp_path / "memory" / "topics" / f"{event['topic_id']}.json"

    assert events_path.exists()
    assert index_path.exists()
    assert topic_path.exists()

    topic = read_json_file(str(topic_path))
    index = read_json_file(str(index_path))

    assert topic["topic"] == "Grounding guidance"
    assert topic["observation_count"] == 1
    assert index["topics"][0]["topic_id"] == event["topic_id"]
    assert "observations" not in index["topics"][0]
    assert index["topics"][0]["summary"] == "Prefer verified grounding notes"


def test_query_memory_excludes_unverified_topic_by_default(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    record_memory_entry(
        cfg,
        topic="Generic note",
        summary="Unverified generic guidance",
        content="Someone mentioned grounding this way but it was never checked.",
        kind="operator_note",
        verification_status="unverified",
        tags=["grounding"],
    )

    result = query_memory(cfg, "grounding guidance")

    assert result["results"] == []
    assert result["excluded"]
    assert "unverified" in result["excluded"][0]["exclusion_reasons"]


def test_consolidate_memory_deduplicates_exact_duplicate_observations(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="Prefer verified grounding notes",
        content="Use verified NCCER grounding guidance before falling back to generic notes.",
        kind="verified_fact",
        verification_status="verified",
    )
    record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="Prefer verified grounding notes",
        content="Use verified NCCER grounding guidance before falling back to generic notes.",
        kind="verified_fact",
        verification_status="verified",
    )

    stats = consolidate_memory(cfg)
    topic_files = list((tmp_path / "memory" / "topics").glob("*.json"))
    topic = read_json_file(str(topic_files[0]))

    assert stats["duplicates_removed"] >= 1
    assert topic["observation_count"] == 1
    assert topic["observations"][0]["duplicate_count"] == 2


def test_query_memory_returns_stale_topic_as_excluded(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    event = record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="Temporary grounding note",
        content="Old guidance that should no longer be used.",
        kind="operator_note",
        verification_status="verified",
    )
    record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="This note is stale",
        content="The previous grounding note is obsolete.",
        kind="decision",
        status="stale",
        verification_status="verified",
        supersedes=event["event_id"],
    )

    result = query_memory(cfg, "temporary grounding note", require_verification=False)

    assert result["results"] == []
    assert result["excluded"]
    assert "stale" in result["excluded"][0]["exclusion_reasons"]


def test_query_memory_preserves_request_lineage_for_returned_topic(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="Prefer verified grounding notes",
        content="Use verified NCCER grounding guidance before falling back to generic notes.",
        kind="verified_fact",
        verification_status="verified",
    )

    result = query_memory(cfg, "grounding guidance", request_id="req-123")

    assert result["provider"] == "file"
    assert result["request_id"] == "req-123"
    assert result["results"]
    assert result["results"][0]["lineage"]["request_id"] == "req-123"


def test_contradicting_entry_marks_prior_observation_stale(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    original = record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="Legacy grounding note",
        content="Use the old grounding method.",
        kind="verified_fact",
        verification_status="verified",
    )
    corrected = record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="Updated grounding note",
        content="Use the corrected NCCER grounding method.",
        kind="verified_fact",
        verification_status="verified",
        contradicts=[original["event_id"]],
    )

    topic_path = tmp_path / "memory" / "topics" / f"{original['topic_id']}.json"
    topic = read_json_file(str(topic_path))
    original_observation = next(
        observation
        for observation in topic["observations"]
        if observation["event_id"] == original["event_id"]
    )

    assert original_observation["status"] == "stale"
    assert corrected["event_id"] in original_observation["contradicted_by"]
    assert topic["summary"] == "Updated grounding note"


def test_import_memory_entries_loads_curated_rows(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    import_path = tmp_path / "memory_import.json"
    import_path.write_text(
        json.dumps(
            {
                "entries": [
                    {
                        "topic": "Bonding guidance",
                        "summary": "Use verified bonding notes",
                        "content": "Prefer verified bonding notes before generic guidance.",
                        "kind": "verified_fact",
                        "verification_status": "verified",
                        "tags": ["bonding"],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    payload = import_memory_entries(cfg, str(import_path), source_label="operator_seed")
    result = query_memory(cfg, "bonding guidance")

    assert payload["imported_count"] == 1
    assert result["results"]
    assert result["results"][0]["topic"] == "Bonding guidance"
