from __future__ import annotations

import json
from pathlib import Path

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


def _write_skill(path: Path, *, skill_id: str, title: str, summary: str, instructions: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "---",
                f"id: {skill_id}",
                f"title: {title}",
                f"summary: {summary}",
                "aliases: []",
                "tags: []",
                "route_fit:",
                "  - text",
                "  - retrieval",
                "triggers:",
                f"  - {skill_id}",
                "use_when: []",
                "avoid_when: []",
                "---",
                instructions,
                "",
            ]
        ),
        encoding="utf-8",
    )


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
    assert (
        metadata["context_providers"]["execution_summary"]["by_subject_type"]["context_provider"]
        == 2
    )
    assert [
        provider["provider"]
        for provider in metadata["context_providers"]["per_example"][0]["providers"]
    ] == ["memory", "retrieval"]
    assert (
        metadata["per_example"][0]["context_providers"][0]["execution_envelope"]["subject_type"]
        == "context_provider"
    )
    assert (
        metadata["per_example"][0]["context_providers"][1]["hook_annotations"]["policy"]
        == "grounded"
    )
    assert (
        metadata["memory"]["per_example"][0]["request_id"]
        == metadata["per_example"][0]["memory_request_id"]
    )


def test_prepare_prompts_with_retrieval_applies_explicit_skills(tmp_path) -> None:
    cfg = _cfg(tmp_path)
    skills_dir = tmp_path / "skills"
    _write_skill(
        skills_dir / "electrical-estimating.md",
        skill_id="electrical-estimating",
        title="Electrical Estimating",
        summary="Estimate guidance",
        instructions="Keep labor and material assumptions explicit.",
    )
    cfg["skill_registry"] = {
        "enabled": True,
        "root_dir": str(skills_dir),
        "max_active_skills": 2,
        "max_instruction_chars": 1200,
    }

    prompts, metadata = prepare_prompts_with_retrieval(
        [
            {
                "prompt": "### Instruction:\nDraft a conduit estimate\n\n### Response:",
                "route": "text",
                "skill_names": ["electrical-estimating"],
            }
        ],
        cfg,
        {"use_retrieval": False, "skill_names": ["electrical-estimating"]},
    )

    assert prompts[0].startswith("### Active Skills:")
    assert "Electrical Estimating" in prompts[0]
    assert "Keep labor and material assumptions explicit." in prompts[0]
    assert metadata["skills"]["used"] is True
    assert metadata["skills"]["global_skill_names"] == ["electrical-estimating"]
    assert metadata["skills"]["per_example"][0]["requested_skill_names"] == [
        "electrical-estimating"
    ]
    assert metadata["skills"]["per_example"][0]["selected_skill_names"] == ["electrical-estimating"]
    assert metadata["skills"]["per_example"][0]["selected_skills"][0]["selection_sources"] == [
        "explicit"
    ]
