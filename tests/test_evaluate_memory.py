from __future__ import annotations

import json

from evaluate import prepare_prompts_with_retrieval
from indexed_memory import record_memory_entry


def _cfg(tmp_path) -> dict:
    corpus_path = tmp_path / "retrieval.jsonl"
    corpus_path.write_text(
        json.dumps(
            {
                "id": "doc-1",
                "source": "NCCER",
                "section": "Grounding and Bonding",
                "content": "Grounding and bonding protect people and equipment.",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    memory_root = tmp_path / "memory"
    return {
        "retrieval": {
            "enabled": True,
            "corpus_path": str(corpus_path),
            "top_k": 3,
            "max_context_chars": 1600,
            "min_score": 1,
        },
        "context_providers": {
            "order": ["memory", "retrieval"],
            "max_workers": 4,
        },
        "memory": {
            "enabled": True,
            "provider": "file",
            "root_dir": str(memory_root),
            "index_path": str(memory_root / "MEMORY.json"),
            "topics_dir": str(memory_root / "topics"),
            "events_path": str(memory_root / "events.jsonl"),
            "default_top_k": 3,
            "topic_candidate_limit": 8,
            "max_context_chars": 1000,
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
        },
        "hooks": {
            "enabled": True,
            "rules": [
                {
                    "name": "annotate_retrieval_provider",
                    "stage": "post_context_provider",
                    "action": "annotate",
                    "match": {"provider": "retrieval"},
                    "fields": {"policy": "grounded"},
                }
            ],
        },
    }


def test_prepare_prompts_with_retrieval_merges_memory_hints(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    record_memory_entry(
        cfg,
        topic="Grounding guidance",
        summary="Prefer verified grounding notes",
        content="Use verified NCCER grounding guidance before falling back to generic notes.",
        kind="verified_fact",
        verification_status="verified",
        tags=["grounding"],
    )

    prompts, metadata = prepare_prompts_with_retrieval(
        [
            {
                "prompt": "### Instruction:\nSummarize grounding guidance\n\n### Response:",
                "route": "retrieval",
                "source": "NCCER",
                "section": "Grounding and Bonding",
            }
        ],
        cfg,
        {"use_retrieval": True},
    )

    assert "### Memory Hints:" in prompts[0]
    assert "### Retrieved Context:" in prompts[0]
    assert metadata["context_prefetch_workers"] >= 1
    assert metadata["memory"]["used"] is True
    assert metadata["per_example"][0]["memory_used"] is True
    assert metadata["per_example"][0]["memory_request_id"]
    assert metadata["per_example"][0]["memory_results"]
    assert metadata["context_providers"]["order"] == ["memory", "retrieval"]
    assert [
        provider["provider"]
        for provider in metadata["context_providers"]["per_example"][0]["providers"]
    ] == ["memory", "retrieval"]
    assert (
        metadata["per_example"][0]["context_providers"][1]["hook_annotations"]["policy"]
        == "grounded"
    )
    assert (
        metadata["memory"]["per_example"][0]["request_id"]
        == metadata["per_example"][0]["memory_request_id"]
    )
