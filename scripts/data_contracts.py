"""
Helpers for stable record IDs and review-safe data contracts.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


REVIEW_STATES = {"review_required", "reviewed", "approved"}
RUNTIME_OWNERS = {"text", "retrieval", "multimodal", "geometry_rules", "manual_review"}

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

DRAWING_PATH_PHRASES = (
    "drawing",
    "drawings",
    "plan",
    "plans",
    "plan set",
    "plan sheet",
    "plan sheets",
    "blueprint",
    "blueprints",
    "sheet",
    "sheets",
    "single line",
    "one line",
    "schematic",
    "schematics",
    "elevation",
    "elevations",
)
ESTIMATING_PATH_PHRASES = ("estimating", "estimate", "estimator", "rsmeans")
REVIT_PATH_PHRASES = ("revit",)
CODE_TRAINING_PATH_PHRASES = ("electrical code training", "code training")


def _normalized_path_text(relative_path: str | None) -> str:
    if not isinstance(relative_path, str) or not relative_path.strip():
        return ""
    normalized = relative_path.replace("\\", "/").lower()
    normalized = normalized.replace("_", " ").replace("-", " ").replace("/", " ")
    return " ".join(normalized.split())


def _path_contains_phrase(relative_path: str | None, phrases: tuple[str, ...]) -> bool:
    normalized = _normalized_path_text(relative_path)
    if not normalized:
        return False
    return any(phrase in normalized for phrase in phrases)


def is_drawing_asset(asset_kind: str, relative_path: str | None = None) -> bool:
    if asset_kind not in {"document", "image"}:
        return False
    return _path_contains_phrase(relative_path, DRAWING_PATH_PHRASES)


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


def suggested_ingestion_contract(asset_kind: str, relative_path: str | None = None) -> dict:
    if is_drawing_asset(asset_kind, relative_path):
        return {
            "runtime_owner": "multimodal",
            "data_family": "drawing_sheet_unassigned",
            "pipeline": "manual_review",
            "routing_hint": "drawing_sheet_only",
            "route": "drawing_sheet",
            "managed_source_key": "drawings_multimodal_root",
        }

    suggestions = {
        "document": {
            "runtime_owner": "retrieval",
            "data_family": "reference_unassigned",
            "pipeline": "ingest_reference_folder",
            "routing_hint": "retrieval_only",
            "route": "retrieval",
            "managed_source_key": "reference_root",
        },
        "code": {
            "runtime_owner": "retrieval",
            "data_family": "code_reference_unassigned",
            "pipeline": "ingest_reference_folder",
            "routing_hint": "retrieval_only",
            "route": "retrieval",
            "managed_source_key": "code_training_reference_root",
        },
        "image": {
            "runtime_owner": "manual_review",
            "data_family": "visual_unassigned",
            "pipeline": "manual_review",
            "routing_hint": "manual_review_only",
            "route": None,
            "managed_source_key": None,
        },
        "tabular": {
            "runtime_owner": "manual_review",
            "data_family": "structured_unassigned",
            "pipeline": "manual_review",
            "routing_hint": "manual_review_only",
            "route": None,
            "managed_source_key": "structured_root",
        },
        "cad_bim": {
            "runtime_owner": "geometry_rules",
            "data_family": "spatial_grounding_unassigned",
            "pipeline": "revit_ingestion",
            "routing_hint": "deterministic_tool_input",
            "route": "deterministic_tool",
            "managed_source_key": "revit_family_dir",
        },
        "other": {
            "runtime_owner": "manual_review",
            "data_family": "unassigned",
            "pipeline": "manual_review",
            "routing_hint": "manual_review_only",
            "route": None,
            "managed_source_key": None,
        },
    }
    suggestion = dict(suggestions.get(asset_kind, suggestions["other"]))

    if asset_kind == "document" and _path_contains_phrase(relative_path, ESTIMATING_PATH_PHRASES):
        suggestion["managed_source_key"] = "estimating_reference_root"
    elif asset_kind == "document" and _path_contains_phrase(relative_path, REVIT_PATH_PHRASES):
        suggestion["managed_source_key"] = "revit_reference_root"
    elif asset_kind == "code" and _path_contains_phrase(relative_path, CODE_TRAINING_PATH_PHRASES):
        suggestion["managed_source_key"] = "code_training_reference_root"

    return suggestion