from __future__ import annotations

from copy import deepcopy

import pytest

from config_validation import (
    validate_agent_task_manager_config,
    validate_agent_shell_config,
    validate_context_providers_config,
    validate_dream_config,
    validate_hooks_config,
    validate_memory_config,
    validate_multimodal_config,
    validate_routing_config,
    validate_skill_registry_config,
    validate_system_prompts_config,
    validate_workflow_registry_config,
)


def _base_cfg() -> dict:
    return {
        "architecture": {
            "system_type": "grounded_multi_runtime",
            "primary_runtime": "text",
            "multimodal_runtime_enabled": False,
            "retrieval_layer_enabled": True,
            "geometry_rules_enabled": False,
            "grounded_answers_require_retrieval": True,
        },
        "routing": {
            "default_route": "text",
            "route_fallbacks": {
                "text": "fail",
                "retrieval": "text",
                "deterministic_tool": "text",
                "drawing_sheet": "fail",
                "mixed": "fail",
            },
            "latency_budgets_ms": {
                "text": 1800,
                "retrieval": 2600,
                "deterministic_tool": 1200,
                "drawing_sheet": 5000,
                "mixed": 6500,
            },
        },
        "managed_sources": {
            "root": "sources/managed/electricalai_docs",
            "reference_root": "sources/managed/electricalai_docs/retrieval/document",
            "estimating_reference_root": "sources/managed/electricalai_docs/retrieval/document/estimating",
            "estimating_pdf": "sources/managed/electricalai_docs/retrieval/document/estimating/2026_national_electrical_estimator_ebook.pdf",
            "estimating_har_dir": "sources/managed/electricalai_docs/manual_review/other/estimating/RSmeans",
            "code_training_reference_root": "sources/managed/electricalai_docs/retrieval/document/Electrical Code_Training",
            "drawings_reference_root": "sources/managed/electricalai_docs/retrieval/document/Drawings",
            "drawings_multimodal_root": "sources/managed/electricalai_docs/multimodal/image/Drawings",
            "revit_reference_root": "sources/managed/electricalai_docs/retrieval/document/Revit",
            "revit_family_dir": "sources/managed/electricalai_docs/geometry_rules/cad_bim/Revit/Families",
            "structured_root": "sources/managed/electricalai_docs/manual_review/tabular",
        },
        "multimodal": {
            "enabled_routes": ["drawing_sheet", "mixed"],
            "drawing_asset_root": "sources/managed/electricalai_docs/multimodal/image/Drawings",
            "observation_mode": "ocr_plus_layout",
            "ocr_enabled": True,
            "max_pages_per_document": 6,
            "max_images_per_request": 12,
            "max_observation_chars": 6000,
            "model_name": None,
            "processor_name": None,
        },
    }


def test_validate_multimodal_config_accepts_disabled_scaffold() -> None:
    validate_multimodal_config(_base_cfg())


def test_validate_multimodal_config_requires_model_when_enabled(
    capsys: pytest.CaptureFixture[str],
) -> None:
    cfg = _base_cfg()
    cfg["architecture"]["multimodal_runtime_enabled"] = True

    with pytest.raises(SystemExit):
        validate_multimodal_config(cfg)

    captured = capsys.readouterr()
    assert "multimodal.model_name is required" in captured.out


def test_validate_multimodal_config_rejects_overlapping_drawing_roots(
    capsys: pytest.CaptureFixture[str],
) -> None:
    cfg = _base_cfg()
    cfg["managed_sources"]["drawings_multimodal_root"] = (
        "sources/managed/electricalai_docs/retrieval/document/Drawings/sheets"
    )
    cfg["multimodal"]["drawing_asset_root"] = (
        "sources/managed/electricalai_docs/retrieval/document/Drawings/sheets"
    )

    with pytest.raises(SystemExit):
        validate_multimodal_config(cfg)

    captured = capsys.readouterr()
    assert "must be separate, non-overlapping paths" in captured.out


def test_validate_routing_config_rejects_multimodal_default_when_disabled(
    capsys: pytest.CaptureFixture[str],
) -> None:
    cfg = _base_cfg()
    cfg["routing"]["default_route"] = "drawing_sheet"

    with pytest.raises(SystemExit):
        validate_routing_config(cfg)

    captured = capsys.readouterr()
    assert "routing.default_route cannot require the multimodal runtime" in captured.out


def test_validate_routing_config_accepts_complete_route_map() -> None:
    cfg = deepcopy(_base_cfg())
    validate_routing_config(cfg)


def test_validate_memory_config_accepts_scaffold() -> None:
    validate_memory_config(
        {
            "memory": {
                "enabled": False,
                "provider": "file",
                "root_dir": "data/memory",
                "index_path": "data/memory/MEMORY.json",
                "topics_dir": "data/memory/topics",
                "events_path": "data/memory/events.jsonl",
                "default_top_k": 3,
                "topic_candidate_limit": 8,
                "max_context_chars": 1200,
                "max_index_entries": 64,
                "max_summary_chars": 160,
                "max_supporting_observations": 3,
                "max_trace_results": 3,
                "max_trace_excluded": 3,
                "min_score": 2,
                "require_verification": True,
                "contradiction_policy": "mark_stale",
                "exclude_contradicted_topics": True,
                "import_max_records": 32,
                "allowed_kinds": ["operator_note", "verified_fact", "decision", "exception"],
                "exclude_statuses": ["stale", "retracted"],
                "consolidation_min_events": 8,
            }
        }
    )


def test_validate_memory_config_rejects_unknown_kind(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit):
        validate_memory_config(
            {
                "memory": {
                    "enabled": False,
                    "provider": "file",
                    "root_dir": "data/memory",
                    "index_path": "data/memory/MEMORY.json",
                    "topics_dir": "data/memory/topics",
                    "events_path": "data/memory/events.jsonl",
                    "default_top_k": 3,
                    "topic_candidate_limit": 8,
                    "max_context_chars": 1200,
                    "max_index_entries": 64,
                    "max_summary_chars": 160,
                    "max_supporting_observations": 3,
                    "max_trace_results": 3,
                    "max_trace_excluded": 3,
                    "min_score": 2,
                    "require_verification": True,
                    "contradiction_policy": "mark_stale",
                    "exclude_contradicted_topics": True,
                    "import_max_records": 32,
                    "allowed_kinds": ["operator_note", "not_a_kind"],
                    "exclude_statuses": ["stale", "retracted"],
                    "consolidation_min_events": 8,
                }
            }
        )

    captured = capsys.readouterr()
    assert "memory.allowed_kinds contains unsupported values" in captured.out


def test_validate_memory_config_rejects_track_only_without_exclusion(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_memory_config(
            {
                "memory": {
                    "enabled": False,
                    "provider": "file",
                    "root_dir": "data/memory",
                    "index_path": "data/memory/MEMORY.json",
                    "topics_dir": "data/memory/topics",
                    "events_path": "data/memory/events.jsonl",
                    "default_top_k": 3,
                    "topic_candidate_limit": 8,
                    "max_context_chars": 1200,
                    "max_index_entries": 64,
                    "max_summary_chars": 160,
                    "max_supporting_observations": 3,
                    "max_trace_results": 3,
                    "max_trace_excluded": 3,
                    "min_score": 2,
                    "require_verification": True,
                    "contradiction_policy": "track_only",
                    "exclude_contradicted_topics": False,
                    "import_max_records": 32,
                    "allowed_kinds": ["operator_note", "verified_fact", "decision", "exception"],
                    "exclude_statuses": ["stale", "retracted"],
                    "consolidation_min_events": 8,
                }
            }
        )

    captured = capsys.readouterr()
    assert "memory.exclude_contradicted_topics must be true" in captured.out


def test_validate_memory_config_rejects_unknown_provider(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_memory_config(
            {
                "memory": {
                    "enabled": False,
                    "provider": "sqlite",
                    "root_dir": "data/memory",
                    "index_path": "data/memory/MEMORY.json",
                    "topics_dir": "data/memory/topics",
                    "events_path": "data/memory/events.jsonl",
                    "default_top_k": 3,
                    "topic_candidate_limit": 8,
                    "max_context_chars": 1200,
                    "max_index_entries": 64,
                    "max_summary_chars": 160,
                    "max_supporting_observations": 3,
                    "max_trace_results": 3,
                    "max_trace_excluded": 3,
                    "min_score": 2,
                    "require_verification": True,
                    "contradiction_policy": "mark_stale",
                    "exclude_contradicted_topics": True,
                    "import_max_records": 32,
                    "allowed_kinds": ["operator_note", "verified_fact", "decision", "exception"],
                    "exclude_statuses": ["stale", "retracted"],
                    "consolidation_min_events": 8,
                }
            }
        )

    captured = capsys.readouterr()
    assert "memory.provider must be one of" in captured.out


def test_validate_dream_config_accepts_scaffold() -> None:
    validate_dream_config(
        {
            "memory": {
                "enabled": True,
            },
            "dream": {
                "enabled": True,
                "root_dir": "data/memory/dream",
                "state_path": "data/memory/dream/state.json",
                "lock_path": "data/memory/dream/consolidation.lock",
                "log_dir": "data/memory/dream/daily_logs",
                "minimum_hours_between_runs": 24,
                "minimum_sessions_between_runs": 5,
                "lock_timeout_seconds": 900,
                "max_recent_logs": 200,
                "max_persistable_entries_per_run": 32,
                "brief_summary_chars": 160,
            },
        }
    )


def test_validate_dream_config_requires_enabled_memory(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_dream_config(
            {
                "memory": {
                    "enabled": False,
                },
                "dream": {
                    "enabled": True,
                    "root_dir": "data/memory/dream",
                    "state_path": "data/memory/dream/state.json",
                    "lock_path": "data/memory/dream/consolidation.lock",
                    "log_dir": "data/memory/dream/daily_logs",
                    "minimum_hours_between_runs": 24,
                    "minimum_sessions_between_runs": 5,
                    "lock_timeout_seconds": 900,
                    "max_recent_logs": 200,
                    "max_persistable_entries_per_run": 32,
                    "brief_summary_chars": 160,
                },
            }
        )

    captured = capsys.readouterr()
    assert "dream.enabled requires memory.enabled to be true" in captured.out


def test_validate_dream_config_rejects_persist_limit_above_recent_logs(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_dream_config(
            {
                "memory": {
                    "enabled": True,
                },
                "dream": {
                    "enabled": False,
                    "root_dir": "data/memory/dream",
                    "state_path": "data/memory/dream/state.json",
                    "lock_path": "data/memory/dream/consolidation.lock",
                    "log_dir": "data/memory/dream/daily_logs",
                    "minimum_hours_between_runs": 24,
                    "minimum_sessions_between_runs": 5,
                    "lock_timeout_seconds": 900,
                    "max_recent_logs": 8,
                    "max_persistable_entries_per_run": 32,
                    "brief_summary_chars": 160,
                },
            }
        )

    captured = capsys.readouterr()
    assert (
        "dream.max_persistable_entries_per_run cannot exceed dream.max_recent_logs" in captured.out
    )


def test_validate_context_providers_config_accepts_scaffold() -> None:
    validate_context_providers_config(
        {
            "context_providers": {
                "order": ["memory", "retrieval"],
                "max_workers": 4,
            }
        }
    )


def test_validate_skill_registry_config_accepts_existing_dir(tmp_path) -> None:
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)

    validate_skill_registry_config(
        {
            "skill_registry": {
                "enabled": True,
                "root_dir": str(skills_dir),
                "max_active_skills": 2,
                "max_instruction_chars": 1200,
            }
        }
    )


def test_validate_skill_registry_config_rejects_missing_dir(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_skill_registry_config(
            {
                "skill_registry": {
                    "enabled": True,
                    "root_dir": "does/not/exist",
                    "max_active_skills": 2,
                    "max_instruction_chars": 1200,
                }
            }
        )

    captured = capsys.readouterr()
    assert "Skill registry directory not found" in captured.out


def test_validate_agent_task_manager_config_accepts_scaffold(tmp_path) -> None:
    root_dir = tmp_path / "agent_tasks"

    validate_agent_task_manager_config(
        {
            "agent_task_manager": {
                "enabled": True,
                "root_dir": str(root_dir),
                "tasks_dir": str(root_dir / "tasks"),
                "logs_dir": str(root_dir / "logs"),
            }
        }
    )


def test_validate_agent_task_manager_config_rejects_overlapping_dirs(
    capsys: pytest.CaptureFixture[str],
    tmp_path,
) -> None:
    root_dir = tmp_path / "agent_tasks"

    with pytest.raises(SystemExit):
        validate_agent_task_manager_config(
            {
                "agent_task_manager": {
                    "enabled": True,
                    "root_dir": str(root_dir),
                    "tasks_dir": str(root_dir / "tasks"),
                    "logs_dir": str(root_dir / "tasks"),
                }
            }
        )

    captured = capsys.readouterr()
    assert (
        "agent_task_manager.tasks_dir and agent_task_manager.logs_dir must be different"
        in captured.out
    )


def test_validate_context_providers_config_requires_retrieval(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_context_providers_config(
            {
                "context_providers": {
                    "order": ["memory"],
                    "max_workers": 4,
                }
            }
        )

    captured = capsys.readouterr()
    assert "context_providers.order must include 'retrieval'" in captured.out


def test_validate_hooks_config_accepts_scaffold() -> None:
    validate_hooks_config(
        {
            "hooks": {
                "enabled": True,
                "rules": [
                    {
                        "name": "annotate_retrieval_provider",
                        "stage": "post_context_provider",
                        "action": "annotate",
                        "match": {"provider": "retrieval"},
                        "fields": {"policy": "grounded"},
                    }
                ],
            }
        }
    )


def test_validate_hooks_config_rejects_unknown_stage(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_hooks_config(
            {
                "hooks": {
                    "enabled": True,
                    "rules": [
                        {
                            "name": "bad_stage",
                            "stage": "post_llm",
                            "action": "annotate",
                            "fields": {"policy": "grounded"},
                        }
                    ],
                }
            }
        )

    captured = capsys.readouterr()
    assert "hooks.rules[0].stage must be one of" in captured.out


def test_validate_workflow_registry_config_accepts_scaffold(tmp_path) -> None:
    manifest_path = tmp_path / "registry.yaml"
    manifest_path.write_text(
        "schema_version: 1\nworkflows: {demo: {description: Demo, steps: [{name: noop, argv: [python, --version]}]}}\n",
        encoding="utf-8",
    )

    validate_workflow_registry_config(
        {
            "workflow_registry": {
                "enabled": True,
                "manifest_path": str(manifest_path),
            }
        }
    )


def test_validate_workflow_registry_config_rejects_missing_manifest(
    capsys: pytest.CaptureFixture[str], tmp_path
) -> None:
    with pytest.raises(SystemExit):
        validate_workflow_registry_config(
            {
                "workflow_registry": {
                    "enabled": True,
                    "manifest_path": str(tmp_path / "missing.yaml"),
                }
            }
        )

    captured = capsys.readouterr()
    assert "Workflow registry manifest not found" in captured.out


def test_validate_agent_shell_config_accepts_scaffold() -> None:
    validate_agent_shell_config(
        {
            "memory": {"enabled": False},
            "retrieval": {"enabled": False},
            "agent_shell": {
                "enabled": True,
                "provider": "ollama",
                "model": "simcoe",
                "root_dir": "data/agent_shell",
                "sessions_dir": "data/agent_shell/sessions",
                "transcripts_dir": "data/agent_shell/transcripts",
                "max_turns": 40,
                "temperature": 0.2,
                "max_output_tokens": 512,
                "ollama_base_url": "http://localhost:11434/v1",
                "openai_api_key_env": "OPENAI_API_KEY",
                "include_memory_in_text_routes": False,
                "include_retrieval_in_text_routes": False,
                "persist_context_sections": True,
            },
        }
    )


def test_validate_agent_shell_config_rejects_unknown_provider(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_agent_shell_config(
            {
                "memory": {"enabled": False},
                "retrieval": {"enabled": False},
                "agent_shell": {
                    "enabled": True,
                    "provider": "vertex",
                    "model": "simcoe",
                    "root_dir": "data/agent_shell",
                    "sessions_dir": "data/agent_shell/sessions",
                    "transcripts_dir": "data/agent_shell/transcripts",
                    "max_turns": 40,
                    "temperature": 0.2,
                    "max_output_tokens": 512,
                    "ollama_base_url": "http://localhost:11434/v1",
                    "openai_api_key_env": "OPENAI_API_KEY",
                    "include_memory_in_text_routes": False,
                    "include_retrieval_in_text_routes": False,
                    "persist_context_sections": True,
                },
            }
        )

    captured = capsys.readouterr()
    assert "agent_shell.provider must be one of" in captured.out


def test_validate_agent_shell_config_requires_retrieval_for_text_route_injection(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_agent_shell_config(
            {
                "retrieval": {"enabled": False},
                "memory": {"enabled": False},
                "agent_shell": {
                    "enabled": True,
                    "provider": "ollama",
                    "model": "simcoe",
                    "root_dir": "data/agent_shell",
                    "sessions_dir": "data/agent_shell/sessions",
                    "transcripts_dir": "data/agent_shell/transcripts",
                    "max_turns": 40,
                    "temperature": 0.2,
                    "max_output_tokens": 512,
                    "ollama_base_url": "http://localhost:11434/v1",
                    "openai_api_key_env": "OPENAI_API_KEY",
                    "include_memory_in_text_routes": False,
                    "include_retrieval_in_text_routes": True,
                    "persist_context_sections": True,
                },
            }
        )

    captured = capsys.readouterr()
    assert "agent_shell.include_retrieval_in_text_routes requires retrieval.enabled" in captured.out


def test_validate_system_prompts_config_accepts_builtin_templates() -> None:
    validate_system_prompts_config(
        {
            "system_prompts": {
                "library_path": "prompts/system_prompt_templates.yaml",
                "agent_shell": {"template_id": "interactive-grounded-operator"},
                "generate_data": {"template_id": "synthetic-data-generator"},
                "evaluation_judge": {"template_id": "evaluation-rubric-judge"},
                "export_modelfile": {"template_id": "runtime-helpful-assistant"},
            }
        }
    )


def test_validate_system_prompts_config_rejects_missing_required_variables(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit):
        validate_system_prompts_config(
            {
                "system_prompts": {
                    "library_path": "prompts/system_prompt_templates.yaml",
                    "export_modelfile": {
                        "template_id": "grounded-domain-baseline",
                    },
                }
            }
        )

    captured = capsys.readouterr()
    assert "missing required variables: domain" in captured.out
