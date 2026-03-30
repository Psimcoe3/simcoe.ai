"""
Helpers for stable record IDs and review-safe data contracts.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


REVIEW_STATES = {"review_required", "reviewed", "approved"}
RUNTIME_OWNERS = {"text", "retrieval", "multimodal", "geometry_rules"}

DOCUMENT_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".md",
    ".rst",
    ".yaml",
    ".yml",
    ".json",
    ".jsonl",
    ".doc",
    ".docx",
}
CODE_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".cs",
    ".java",
    ".go",
    ".rs",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".sql",
    ".sh",
    ".ps1",
}
IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".bmp",
    ".tif",
    ".tiff",
}
TABULAR_EXTENSIONS = {
    ".csv",
    ".tsv",
    ".xlsx",
    ".xls",
}
CAD_BIM_EXTENSIONS = {
    ".rfa",
    ".rvt",
    ".ifc",
    ".dwg",
    ".dxf",
}


def stable_identifier(namespace: str, *parts: object) -> str:
    digest = hashlib.sha256()
    for part in parts:
        digest.update(str(part or "").strip().encode("utf-8"))
        digest.update(b"\x1f")
    return f"{namespace}:{digest.hexdigest()[:16]}"


def build_data_contract(
    *,
    data_family: str,
    runtime_owner: str,
    routing_hint: str,
    review_state: str = "review_required",
    sft_candidate: bool = False,
) -> dict:
    if review_state not in REVIEW_STATES:
        raise ValueError(f"Unsupported review_state: {review_state}")
    if runtime_owner not in RUNTIME_OWNERS:
        raise ValueError(f"Unsupported runtime_owner: {runtime_owner}")

    return {
        "schema_version": 1,
        "data_family": data_family,
        "runtime_owner": runtime_owner,
        "routing_hint": routing_hint,
        "review_state": review_state,
        "sft_candidate": bool(sft_candidate),
    }


def infer_asset_kind(path: str) -> str:
    extension = Path(path).suffix.lower()
    if extension in DOCUMENT_EXTENSIONS:
        return "document"
    if extension in CODE_EXTENSIONS:
        return "code"
    if extension in IMAGE_EXTENSIONS:
        return "image"
    if extension in TABULAR_EXTENSIONS:
        return "tabular"
    if extension in CAD_BIM_EXTENSIONS:
        return "cad_bim"
    return "other"


def suggested_ingestion_contract(asset_kind: str) -> dict:
    suggestions = {
        "document": {
            "runtime_owner": "retrieval",
            "data_family": "reference_unassigned",
            "pipeline": "ingest_reference_folder",
        },
        "code": {
            "runtime_owner": "retrieval",
            "data_family": "code_reference_unassigned",
            "pipeline": "ingest_reference_folder",
        },
        "image": {
            "runtime_owner": "multimodal",
            "data_family": "multimodal_unassigned",
            "pipeline": "manual_review",
        },
        "tabular": {
            "runtime_owner": "manual_review",
            "data_family": "structured_unassigned",
            "pipeline": "manual_review",
        },
        "cad_bim": {
            "runtime_owner": "geometry_rules",
            "data_family": "spatial_grounding_unassigned",
            "pipeline": "revit_ingestion",
        },
        "other": {
            "runtime_owner": "manual_review",
            "data_family": "unassigned",
            "pipeline": "manual_review",
        },
    }
    return suggestions.get(asset_kind, suggestions["other"])