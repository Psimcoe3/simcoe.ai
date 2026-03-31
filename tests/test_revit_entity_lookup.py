from __future__ import annotations

import json

from deterministic_tool_utils import build_tool_request
from revit_entity_lookup import resolve_tool_settings, run_revit_entity_lookup_request


def _write_index(path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row))
            handle.write("\n")


def test_resolve_tool_settings_caps_top_k() -> None:
    cfg = {
        "deterministic_tools": {
            "revit_entity_lookup": {
                "enabled": True,
                "index_path": "data/raw/revit_family_index.jsonl",
                "default_top_k": 5,
                "max_results": 2,
                "min_score": 2,
            }
        }
    }

    settings = resolve_tool_settings(cfg, top_k=9)

    assert settings["top_k"] == 2
    assert settings["min_score"] == 2.0


def test_run_revit_entity_lookup_request_ranks_best_match(tmp_path) -> None:
    index_path = tmp_path / "revit_family_index.jsonl"
    _write_index(
        index_path,
        [
            {
                "record_id": "revit_family_reference:bestmatch",
                "record_type": "revit_family_reference",
                "lookup_key": "assemblies-junction-box-nema-1-galvanized-screw-cover",
                "category": "Assemblies",
                "subcategory": "Junction Box",
                "family_name": "eE_ASM_Pullbox_Supported_v3",
                "type_name": "Nema 1 Galvanized",
                "description": "12in x 48in x 48in Nema 1 Galvanized Screw Cover",
                "unit": "ASM",
                "lookup_tokens": [
                    "assemblies",
                    "junction",
                    "box",
                    "nema",
                    "galvanized",
                    "screw",
                    "cover",
                    "12in",
                    "48in",
                ],
                "data_contract": {"schema_version": 1},
            },
            {
                "record_id": "revit_family_reference:runnerup",
                "record_type": "revit_family_reference",
                "lookup_key": "assemblies-junction-box-painted-cover",
                "category": "Assemblies",
                "subcategory": "Junction Box",
                "family_name": "Different_Family",
                "type_name": "Painted",
                "description": "12in x 48in x 48in Painted Cover",
                "unit": "ASM",
                "lookup_tokens": [
                    "assemblies",
                    "junction",
                    "box",
                    "painted",
                    "cover",
                    "12in",
                    "48in",
                ],
                "data_contract": {"schema_version": 1},
            },
        ],
    )

    cfg = {
        "deterministic_tools": {
            "revit_entity_lookup": {
                "enabled": True,
                "index_path": str(index_path),
                "default_top_k": 5,
                "max_results": 10,
                "min_score": 2,
            }
        }
    }
    request = build_tool_request(
        "revit_entity_lookup",
        query="12in x 48in x 48in Nema 1 Galvanized Screw Cover",
        top_k=1,
    )

    response = run_revit_entity_lookup_request(cfg, request)

    assert response["result_count"] == 1
    assert response["results"][0]["record_id"] == "revit_family_reference:bestmatch"
    assert response["results"][0]["type_name"] == "Nema 1 Galvanized"
    assert response["results"][0]["match_score"] > 0


def test_run_revit_entity_lookup_request_supports_exact_lookup_key(tmp_path) -> None:
    index_path = tmp_path / "revit_family_index.jsonl"
    _write_index(
        index_path,
        [
            {
                "record_id": "revit_family_reference:exact",
                "record_type": "revit_family_reference",
                "lookup_key": "assemblies-aluminum-rack-ee-asm-aluminum-rack",
                "category": "Assemblies",
                "subcategory": "Aluminum Rack",
                "family_name": "eE_ASM_Aluminum_Rack",
                "type_name": "eE_ASM_Aluminum_Rack",
                "description": "Aluminum Rack Assembly",
                "unit": "ASM",
                "lookup_tokens": ["assemblies", "aluminum", "rack", "assembly"],
                "data_contract": {"schema_version": 1},
            }
        ],
    )

    cfg = {
        "deterministic_tools": {
            "revit_entity_lookup": {
                "enabled": True,
                "index_path": str(index_path),
                "default_top_k": 5,
                "max_results": 10,
                "min_score": 2,
            }
        }
    }
    request = build_tool_request(
        "revit_entity_lookup",
        lookup_key="assemblies-aluminum-rack-ee-asm-aluminum-rack",
        top_k=1,
    )

    response = run_revit_entity_lookup_request(cfg, request)

    assert response["result_count"] == 1
    assert response["results"][0]["record_id"] == "revit_family_reference:exact"
    assert response["results"][0]["match_reasons"][0]["type"] == "lookup_key_match"
