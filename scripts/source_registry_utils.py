"""
Helpers for repo-managed source registry organization.
"""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath


DEFAULT_REPO_SYNC_DIR = "sources/managed"
DEFAULT_MATERIALIZED_MANIFEST_PATH = "data/registry/materialized_sources.json"


def _slugify_segment(value: object, fallback: str) -> str:
    cleaned = str(value or "").strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "_", cleaned).strip("_")
    return slug or fallback


def source_registry_namespace(source_registry_cfg: dict | None = None, root: str | None = None) -> str:
    if isinstance(source_registry_cfg, dict):
        explicit = source_registry_cfg.get("repo_namespace")
        if isinstance(explicit, str) and explicit.strip():
            return _slugify_segment(explicit, "external_sources")
        if root is None:
            root = source_registry_cfg.get("root")

    if root:
        return _slugify_segment(Path(str(root)).name, "external_sources")
    return "external_sources"


def repo_sync_dir(source_registry_cfg: dict | None = None) -> str:
    if isinstance(source_registry_cfg, dict):
        configured = source_registry_cfg.get("repo_sync_dir")
        if isinstance(configured, str) and configured.strip():
            return configured.strip()
    return DEFAULT_REPO_SYNC_DIR


def materialized_manifest_path(source_registry_cfg: dict | None = None) -> str:
    if isinstance(source_registry_cfg, dict):
        configured = source_registry_cfg.get("materialized_manifest_path")
        if isinstance(configured, str) and configured.strip():
            return configured.strip()
    return DEFAULT_MATERIALIZED_MANIFEST_PATH


def managed_relative_path(
    relative_path: str,
    asset_kind: str,
    runtime_owner: str | None,
    namespace: str,
) -> str:
    owner_segment = _slugify_segment(runtime_owner or "manual_review", "manual_review")
    kind_segment = _slugify_segment(asset_kind or "other", "other")
    normalized_relative_path = Path(str(relative_path).replace("\\", "/")).as_posix().lstrip("/")
    return str(Path(namespace) / owner_segment / kind_segment / normalized_relative_path)


def _normalized_relative_path(relative_path: str) -> str:
    return PurePosixPath(str(relative_path).replace("\\", "/")).as_posix().lstrip("/")


def _relative_path_within_managed_root(relative_path: str, managed_root: str) -> str:
    normalized_relative_path = _normalized_relative_path(relative_path)
    path_parts = PurePosixPath(normalized_relative_path).parts
    managed_root_name = Path(managed_root).name.strip().lower()
    if path_parts and managed_root_name and path_parts[0].strip().lower() == managed_root_name:
        trimmed = PurePosixPath(*path_parts[1:]).as_posix()
        if trimmed and trimmed != ".":
            return trimmed
    return normalized_relative_path


def resolve_repo_managed_path(
    *,
    relative_path: str,
    asset_kind: str,
    suggested_ingestion: dict | None,
    namespace: str,
    repo_sync_root: str,
    managed_sources_cfg: dict | None = None,
) -> str:
    suggested = suggested_ingestion if isinstance(suggested_ingestion, dict) else {}
    managed_source_key = suggested.get("managed_source_key")
    if isinstance(managed_sources_cfg, dict) and isinstance(managed_source_key, str) and managed_source_key.strip():
        managed_root = managed_sources_cfg.get(managed_source_key)
        if isinstance(managed_root, str) and managed_root.strip():
            relative_suffix = _relative_path_within_managed_root(relative_path, managed_root)
            return str(Path(managed_root.strip()) / relative_suffix)

    return str(
        Path(repo_sync_root)
        / managed_relative_path(
            relative_path,
            asset_kind,
            suggested.get("runtime_owner") if isinstance(suggested, dict) else None,
            namespace,
        )
    )
