from __future__ import annotations

from data_contracts import suggested_ingestion_contract
from source_registry_utils import resolve_repo_managed_path


def test_suggested_ingestion_contract_routes_drawing_document_to_multimodal() -> None:
    suggested = suggested_ingestion_contract("document", "Drawings/Plan Sets/A101.pdf")

    assert suggested["runtime_owner"] == "multimodal"
    assert suggested["route"] == "drawing_sheet"
    assert suggested["managed_source_key"] == "drawings_multimodal_root"


def test_resolve_repo_managed_path_uses_drawings_multimodal_root() -> None:
    path = resolve_repo_managed_path(
        relative_path="Drawings/Plan Sets/A101.pdf",
        asset_kind="document",
        suggested_ingestion=suggested_ingestion_contract("document", "Drawings/Plan Sets/A101.pdf"),
        namespace="electricalai_docs",
        repo_sync_root="sources/managed",
        managed_sources_cfg={
            "drawings_multimodal_root": "sources/managed/electricalai_docs/multimodal/image/Drawings",
        },
    )

    assert path == "sources/managed/electricalai_docs/multimodal/image/Drawings/Plan Sets/A101.pdf"


def test_resolve_repo_managed_path_falls_back_to_generic_namespace_layout() -> None:
    path = resolve_repo_managed_path(
        relative_path="estimating/notes/example.txt",
        asset_kind="document",
        suggested_ingestion={"runtime_owner": "retrieval"},
        namespace="electricalai_docs",
        repo_sync_root="sources/managed",
        managed_sources_cfg={},
    )

    assert (
        path == "sources/managed/electricalai_docs/retrieval/document/estimating/notes/example.txt"
    )
