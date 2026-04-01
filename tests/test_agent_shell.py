from __future__ import annotations

import json
from pathlib import Path

from agent_shell import (
    describe_agent_shell_session,
    initialize_session,
    read_session_turns,
    record_turn,
    resolve_agent_shell_settings,
    resolve_agent_shell_system_prompt,
    run_agent_turn,
)


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")


def _base_cfg(tmp_path: Path) -> dict:
    retrieval_corpus = tmp_path / "retrieval.jsonl"
    estimate_index = tmp_path / "estimate_index.jsonl"
    revit_index = tmp_path / "revit_index.jsonl"

    _write_jsonl(
        retrieval_corpus,
        [
            {
                "id": "doc-1",
                "source": "NCCER Electrical Guides / NCCER Level 1 Trainee Guide",
                "section": "Module Nine",
                "content": "Grounding and bonding create a low-impedance fault path and reduce shock risk.",
            }
        ],
    )
    _write_jsonl(
        estimate_index,
        [
            {
                "record_type": "estimate_lookup",
                "record_id": "estimate_lookup:emt_conduit",
                "lookup_key": "emt-conduit-34",
                "lookup_tokens": ["emt", "conduit"],
                "family_name": "Conduit",
                "category": "Raceway",
                "manufacturer": "Generic",
                "part_number": "EMT-34",
                "description": "EMT conduit",
                "unit": "LF",
                "crew": "electrician",
                "installed_total": 12.5,
                "bare_total": 8.0,
                "source_name": "estimate_fixture",
                "source_row": 1,
                "data_contract": {"runtime_owner": "geometry_rules"},
            }
        ],
    )
    _write_jsonl(
        revit_index,
        [
            {
                "record_type": "revit_family_reference",
                "record_id": "revit_family_reference:panelboard",
                "lookup_key": "panelboard-type-a",
                "lookup_tokens": ["panelboard", "type", "a"],
                "family_name": "Panelboard",
                "type_name": "Type A",
                "family_and_type": "Panelboard : Type A",
            }
        ],
    )

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
        "retrieval": {
            "enabled": True,
            "corpus_path": str(retrieval_corpus),
            "top_k": 3,
            "max_context_chars": 1200,
            "min_score": 1,
        },
        "context_providers": {
            "order": ["memory", "retrieval"],
            "max_workers": 2,
        },
        "hooks": {
            "enabled": False,
            "rules": [],
        },
        "deterministic_tools": {
            "estimate_lookup": {
                "enabled": True,
                "index_path": str(estimate_index),
                "default_top_k": 3,
                "max_results": 3,
                "min_score": 1,
                "default_quantity": 1.0,
            },
            "revit_entity_lookup": {
                "enabled": True,
                "index_path": str(revit_index),
                "default_top_k": 3,
                "max_results": 3,
                "min_score": 1,
            },
        },
        "agent_shell": {
            "enabled": True,
            "provider": "ollama",
            "model": "simcoe",
            "root_dir": str(tmp_path / "agent_shell"),
            "sessions_dir": str(tmp_path / "agent_shell" / "sessions"),
            "transcripts_dir": str(tmp_path / "agent_shell" / "transcripts"),
            "max_turns": 10,
            "temperature": 0.2,
            "max_output_tokens": 256,
            "ollama_base_url": "http://localhost:11434/v1",
            "openai_api_key_env": "OPENAI_API_KEY",
            "include_memory_in_text_routes": False,
            "include_retrieval_in_text_routes": False,
            "persist_context_sections": True,
        },
        "system_prompts": {
            "library_path": "prompts/system_prompt_templates.yaml",
            "agent_shell": {"template_id": "interactive-grounded-operator"},
        },
    }


def test_run_agent_turn_injects_retrieval_context(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, _ = resolve_agent_shell_system_prompt(cfg)
    captured_messages: dict[str, list[dict]] = {}

    def fake_completion(messages: list[dict]) -> str:
        captured_messages["messages"] = messages
        return "Grounded answer"

    turn = run_agent_turn(
        cfg,
        settings,
        "Summarize the electrical construction reference source Module Nine.",
        system_prompt=system_prompt,
        history_messages=[],
        source="NCCER Electrical Guides / NCCER Level 1 Trainee Guide",
        completion_fn=fake_completion,
    )

    assert turn["route"] == "retrieval"
    assert turn["assistant"]["response"] == "Grounded answer"
    assert "### Retrieved Context:" in captured_messages["messages"][-1]["content"]
    assert turn["execution"]["summary"]["by_subject_type"]["route"] == 1
    assert turn["execution"]["summary"]["by_subject_type"]["context_provider"] == 1


def test_run_agent_turn_executes_estimate_lookup(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, _ = resolve_agent_shell_system_prompt(cfg)

    turn = run_agent_turn(
        cfg,
        settings,
        "Find the estimate lookup for EMT conduit.",
        system_prompt=system_prompt,
        history_messages=[],
    )

    assert turn["route"] == "deterministic_tool"
    assert turn["tool"]["name"] == "estimate_lookup"
    assert "estimate_lookup returned 1 result" in turn["assistant"]["response"]
    assert "EMT conduit" in turn["assistant"]["response"]
    assert turn["execution"]["deterministic_tool"]["subject_name"] == "estimate_lookup"


def test_agent_shell_session_persists_and_reloads_turns(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, metadata = resolve_agent_shell_system_prompt(cfg)
    session = initialize_session(
        settings,
        config_path="config.yaml",
        system_prompt_metadata=metadata,
    )

    turn = run_agent_turn(
        cfg,
        settings,
        "Explain grounding and bonding.",
        system_prompt=system_prompt,
        history_messages=[],
        completion_fn=lambda messages: "Stored answer",
        turn_index=int(session["turn_count"]),
    )
    updated_session = record_turn(
        settings,
        session,
        turn,
        system_prompt_metadata=metadata,
    )

    payload = describe_agent_shell_session(settings, updated_session["session_id"], tail=1)
    turns = read_session_turns(settings, updated_session["session_id"])

    assert payload["session"]["turn_count"] == 1
    assert payload["recent_turns"][0]["assistant_response"] == "Stored answer"
    assert turns[0]["assistant"]["response"] == "Stored answer"
    assert turns[0]["route"] == "text"
