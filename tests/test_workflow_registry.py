from __future__ import annotations

import json
from pathlib import Path

import yaml

from workflow_registry import (
    get_workflow,
    list_workflows,
    render_workflow_steps,
    run_workflow,
    validate_workflow_manifest,
)


def _write_manifest(path: Path) -> None:
    payload = {
        "schema_version": 1,
        "workflows": {
            "demo": {
                "description": "Demo workflow",
                "required_vars": ["output_path"],
                "defaults": {"greeting": "hello"},
                "tags": ["demo"],
                "steps": [
                    {
                        "name": "write output",
                        "argv": [
                            "{python}",
                            "-c",
                            "from pathlib import Path; import sys; Path(sys.argv[1]).write_text(sys.argv[2], encoding='utf-8')",
                            "{output_path}",
                            "{greeting}",
                        ],
                    }
                ],
            }
        },
    }
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _dream_cfg(manifest_path: Path, memory_root: Path) -> dict:
    return {
        "workflow_registry": {
            "enabled": True,
            "manifest_path": str(manifest_path),
        },
        "memory": {
            "enabled": True,
            "provider": "file",
            "root_dir": str(memory_root),
            "index_path": str(memory_root / "MEMORY.json"),
            "topics_dir": str(memory_root / "topics"),
            "events_path": str(memory_root / "events.jsonl"),
            "default_top_k": 3,
            "topic_candidate_limit": 8,
            "max_context_chars": 1200,
            "max_index_entries": 64,
            "max_summary_chars": 120,
            "max_supporting_observations": 3,
            "max_trace_results": 3,
            "max_trace_excluded": 3,
            "min_score": 1,
            "require_verification": True,
            "contradiction_policy": "mark_stale",
            "exclude_contradicted_topics": True,
            "import_max_records": 16,
            "allowed_kinds": ["operator_note", "verified_fact", "decision", "exception"],
            "exclude_statuses": ["stale", "retracted"],
            "consolidation_min_events": 2,
        },
        "dream": {
            "enabled": True,
            "root_dir": str(memory_root / "dream"),
            "state_path": str(memory_root / "dream" / "state.json"),
            "lock_path": str(memory_root / "dream" / "consolidation.lock"),
            "log_dir": str(memory_root / "dream" / "daily_logs"),
            "minimum_hours_between_runs": 0,
            "minimum_sessions_between_runs": 1,
            "lock_timeout_seconds": 900,
            "max_recent_logs": 32,
            "max_persistable_entries_per_run": 8,
            "brief_summary_chars": 120,
        },
    }


def test_validate_workflow_manifest_accepts_scaffold() -> None:
    manifest = validate_workflow_manifest(
        {
            "schema_version": 1,
            "workflows": {
                "demo": {
                    "description": "Demo workflow",
                    "steps": [{"name": "noop", "argv": ["python", "--version"]}],
                }
            },
        }
    )

    assert manifest["schema_version"] == 1
    assert "demo" in manifest["workflows"]


def test_list_and_render_workflows(tmp_path) -> None:
    manifest_path = tmp_path / "registry.yaml"
    _write_manifest(manifest_path)
    cfg = {
        "workflow_registry": {
            "enabled": True,
            "manifest_path": str(manifest_path),
        }
    }

    listed = list_workflows(cfg)
    shown = get_workflow(cfg, "demo")
    rendered = render_workflow_steps(
        cfg,
        "config.yaml",
        "demo",
        {"output_path": str(tmp_path / "result.txt")},
    )

    assert len(listed["workflows"]) == 1
    assert shown["name"] == "demo"
    assert rendered["steps"][0]["argv"][0].endswith("python") or rendered["steps"][0]["argv"][
        0
    ].endswith("python3")
    assert rendered["steps"][0]["argv"][-1] == "hello"


def test_run_workflow_executes_rendered_steps(tmp_path) -> None:
    manifest_path = tmp_path / "registry.yaml"
    _write_manifest(manifest_path)
    output_path = tmp_path / "workflow.txt"
    cfg = {
        "workflow_registry": {
            "enabled": True,
            "manifest_path": str(manifest_path),
        }
    }

    result = run_workflow(
        cfg,
        "config.yaml",
        "demo",
        {"output_path": str(output_path), "greeting": "done"},
    )

    assert result["executed_steps"] == 1
    assert output_path.read_text(encoding="utf-8") == "done"


def test_run_workflow_records_dream_session_and_runs_dream(tmp_path) -> None:
    manifest_path = tmp_path / "registry.yaml"
    _write_manifest(manifest_path)
    output_path = tmp_path / "workflow.txt"
    memory_root = tmp_path / "memory"
    cfg = _dream_cfg(manifest_path, memory_root)

    result = run_workflow(
        cfg,
        "config.yaml",
        "demo",
        {"output_path": str(output_path), "greeting": "done"},
    )

    state_path = memory_root / "dream" / "state.json"
    log_paths = sorted((memory_root / "dream" / "daily_logs").glob("*.jsonl"))
    state = json.loads(state_path.read_text(encoding="utf-8"))
    log_entries = [
        json.loads(line)
        for path in log_paths
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    assert output_path.read_text(encoding="utf-8") == "done"
    assert result["dream"]["enabled"] is True
    assert result["dream"]["status"] == "succeeded"
    assert state["session_count"] == 1
    assert state["dream_count"] == 1
    assert state["last_dream_session_count"] == 1
    assert {entry["category"] for entry in log_entries} == {"session", "workflow_result"}


def test_run_workflow_dry_run_skips_dream_side_effects(tmp_path) -> None:
    manifest_path = tmp_path / "registry.yaml"
    _write_manifest(manifest_path)
    memory_root = tmp_path / "memory"
    cfg = _dream_cfg(manifest_path, memory_root)

    result = run_workflow(
        cfg,
        "config.yaml",
        "demo",
        {"output_path": str(tmp_path / "workflow.txt")},
        dry_run=True,
    )

    assert result["dream"] == {"enabled": True, "status": "not_run"}
    assert not (memory_root / "dream" / "state.json").exists()


def test_checked_in_workflow_registry_includes_staged_reference_import() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    manifest_path = repo_root / "workflows" / "registry.yaml"
    manifest = validate_workflow_manifest(yaml.safe_load(manifest_path.read_text(encoding="utf-8")))

    assert "staged-reference-import" in manifest["workflows"]

    cfg = {
        "workflow_registry": {
            "enabled": True,
            "manifest_path": str(manifest_path),
        }
    }
    rendered = render_workflow_steps(
        cfg,
        "config.electrician.yaml",
        "staged-reference-import",
        {
            "batch_name": "downloads_reference_import_20260402_checked",
            "archive_list_file": "/tmp/downloads_reference_archives.txt",
        },
    )

    assert [step["name"] for step in rendered["steps"]] == [
        "stage selected archives",
        "organize staged references",
        "import staged references",
    ]
    assert rendered["steps"][0]["argv"][1] == "scripts/stage_reference_archives.py"
    assert rendered["steps"][1]["argv"][1] == "scripts/organize_staged_references.py"
    assert rendered["steps"][2]["argv"][1] == "scripts/import_staged_reference_batch.py"
