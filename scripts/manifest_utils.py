"""
Shared helpers for writing machine-readable pipeline manifests.
"""

import importlib.metadata
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone


def current_utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: str, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def summarise_numeric(values: list[int | float]) -> dict | None:
    if not values:
        return None

    total = sum(values)
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "mean": round(total / len(values), 4),
    }


def read_json_file(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def safe_git_commit(repository_dir: str) -> str | None:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repository_dir,
            capture_output=True,
            check=True,
            text=True,
        )
    except Exception:
        return None
    return completed.stdout.strip() or None


def package_version(name: str) -> str | None:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def runtime_manifest(package_names: list[str] | None = None) -> dict:
    packages = package_names or []
    return {
        "python": sys.version,
        "packages": {
            name: version
            for name in packages
            if (version := package_version(name)) is not None
        },
    }


def file_metadata(path: str, include_sha256: bool = True) -> dict:
    payload = {
        "path": os.path.abspath(path),
        "size_bytes": os.path.getsize(path),
    }
    if include_sha256:
        payload["sha256"] = sha256_file(path)
    return payload


def directory_artifact_manifest(directory: str, include_sha256: bool = True) -> list[dict]:
    artifacts: list[dict] = []
    if not os.path.isdir(directory):
        return artifacts

    root = os.path.abspath(directory)
    for current_root, _, filenames in os.walk(root):
        for filename in sorted(filenames):
            path = os.path.join(current_root, filename)
            artifact = file_metadata(path, include_sha256=include_sha256)
            artifact["relative_path"] = os.path.relpath(path, root)
            artifacts.append(artifact)

    return sorted(artifacts, key=lambda item: item["relative_path"])


def write_json_file(path: str, payload: dict) -> None:
    parent_dir = os.path.dirname(path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")