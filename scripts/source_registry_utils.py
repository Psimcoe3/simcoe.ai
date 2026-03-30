"""
Helpers for repo-managed source registry organization.
"""

from __future__ import annotations

import re
from pathlib import Path


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
