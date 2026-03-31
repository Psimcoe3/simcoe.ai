from __future__ import annotations

from retrieval_utils import parse_reference_response, retrieve_documents


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
