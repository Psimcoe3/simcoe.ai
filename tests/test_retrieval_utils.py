from __future__ import annotations

from retrieval_utils import (
    build_context_augmented_prompt,
    parse_reference_response,
    retrieve_documents,
)


def test_parse_reference_response_extracts_source_section_and_key_points() -> None:
    parsed = parse_reference_response(
        "Source: NCCER Guide — Grounding and Bonding\n\nSummary line\n- Point one\n- Point two"
    )

    assert parsed["source"] == "NCCER Guide"
    assert parsed["section"] == "Grounding and Bonding"
    assert parsed["body"].startswith("Summary line")
    assert parsed["key_points"] == ["Point one", "Point two"]


def test_retrieve_documents_prefers_exact_source_and_section_hints() -> None:
    corpus = [
        {
            "id": "hinted",
            "source": "NCCER Electrical Guides / Level 2",
            "section": "Grounding and Bonding",
            "content": "Grounding and bonding protect people and equipment.",
        },
        {
            "id": "generic",
            "source": "Generic Reference",
            "section": "Grounding",
            "content": "Grounding and bonding are important in electrical systems.",
        },
    ]

    results = retrieve_documents(
        "grounding bonding",
        corpus,
        top_k=1,
        min_score=1,
        preferred_source="NCCER Electrical Guides / Level 2",
        preferred_section="Grounding and Bonding",
    )

    assert len(results) == 1
    assert results[0]["id"] == "hinted"
    assert results[0]["score"] >= 1


def test_build_context_augmented_prompt_inserts_memory_and_retrieval_sections() -> None:
    prompt = "### Instruction:\nSummarize grounding guidance\n\n### Response:"

    augmented = build_context_augmented_prompt(
        prompt,
        memory_context="[Memory 1] Topic: Grounding guidance",
        retrieved_context="[1] Source: NCCER",
    )

    assert "### Memory Hints:" in augmented
    assert "### Retrieved Context:" in augmented
    assert augmented.index("### Memory Hints:") < augmented.index("### Retrieved Context:")
