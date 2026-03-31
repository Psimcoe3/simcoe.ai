from __future__ import annotations

from deterministic_tool_utils import build_tool_request, build_tool_response


def test_build_tool_request_normalizes_inputs_and_stabilizes_request_id() -> None:
    request_a = build_tool_request(
        "estimate_lookup",
        query="  EMT conduit  ",
        filters={
            "family_name": "  Raceway  ",
            "category": "  ",
            "unit": None,
        },
        top_k=3,
        quantity=2.0,
    )
    request_b = build_tool_request(
        "estimate_lookup",
        query="EMT conduit",
        filters={"family_name": "Raceway"},
        top_k=3,
        quantity=2.0,
    )

    assert request_a["query"] == "EMT conduit"
    assert request_a["filters"] == {"family_name": "Raceway"}
    assert request_a["request_id"] == request_b["request_id"]
    assert request_a["request_id"].startswith("deterministic_tool_request:")


def test_build_tool_response_uses_absolute_index_path(tmp_path) -> None:
    index_path = tmp_path / "estimate_index.jsonl"
    index_path.write_text("", encoding="utf-8")

    request = build_tool_request("estimate_lookup", query="emt")
    response = build_tool_response(
        "estimate_lookup",
        request=request,
        results=[{"record_id": "estimate_lookup:abc123"}],
        index_path=str(index_path),
    )

    assert response["tool_name"] == "estimate_lookup"
    assert response["result_count"] == 1
    assert response["provenance"]["index_path"] == str(index_path.resolve())
