from __future__ import annotations

import json
from pathlib import Path

from agent_shell import (
    handle_shell_command,
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
    skills_dir = tmp_path / "skills"

    (skills_dir / "electrical-estimating.md").parent.mkdir(parents=True, exist_ok=True)
    (skills_dir / "electrical-estimating.md").write_text(
        "\n".join(
            [
                "---",
                "id: electrical-estimating",
                "title: Electrical Estimating",
                "summary: Structure estimate answers around labor and material assumptions.",
                "aliases:",
                "  - estimate",
                "  - quote",
                "tags:",
                "  - labor",
                "  - material",
                "route_fit:",
                "  - text",
                "  - retrieval",
                "triggers:",
                "  - estimate",
                "  - labor",
                "  - material",
                "use_when: []",
                "avoid_when: []",
                "---",
                "Separate labor, material, and assumptions when discussing an estimate.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (skills_dir / "revit-family-reference.md").write_text(
        "\n".join(
            [
                "---",
                "id: revit-family-reference",
                "title: Revit Family Reference",
                "summary: Present exact Revit family and type labels from grounded records.",
                "aliases:",
                "  - revit",
                "tags:",
                "  - family",
                "  - type",
                "route_fit:",
                "  - text",
                "  - deterministic_tool",
                "triggers:",
                "  - revit",
                "  - family type",
                "use_when: []",
                "avoid_when: []",
                "---",
                "Prefer exact family and type labels and say when grounded data is missing.",
                "",
            ]
        ),
        encoding="utf-8",
    )

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
        "agent_task_manager": {
            "enabled": True,
            "root_dir": str(tmp_path / "agent_tasks"),
            "tasks_dir": str(tmp_path / "agent_tasks" / "tasks"),
            "logs_dir": str(tmp_path / "agent_tasks" / "logs"),
        },
        "skill_registry": {
            "enabled": True,
            "root_dir": str(skills_dir),
            "max_active_skills": 2,
            "max_instruction_chars": 1200,
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
    assert payload["session"]["last_skill_names"] == []


def test_run_agent_turn_attaches_matching_skill_guidance(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, _ = resolve_agent_shell_system_prompt(cfg)
    captured_messages: dict[str, list[dict]] = {}

    def fake_completion(messages: list[dict]) -> str:
        captured_messages["messages"] = messages
        return "Structured estimate answer"

    turn = run_agent_turn(
        cfg,
        settings,
        "Explain how to structure an electrical estimate with labor and material assumptions.",
        system_prompt=system_prompt,
        history_messages=[],
        completion_fn=fake_completion,
    )

    assert turn["route"] == "text"
    assert turn["skills"][0]["name"] == "electrical-estimating"
    assert turn["skills"][0]["selection_sources"] == ["matched"]
    assert turn["skill_prompt"] is not None
    assert "### Active Skills:" in captured_messages["messages"][-1]["content"]
    assert "Electrical Estimating" in captured_messages["messages"][-1]["content"]


def test_run_agent_turn_applies_explicit_and_pinned_skill_selection(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, _ = resolve_agent_shell_system_prompt(cfg)
    captured_messages: dict[str, list[dict]] = {}

    def fake_completion(messages: list[dict]) -> str:
        captured_messages["messages"] = messages
        return "Structured answer"

    turn = run_agent_turn(
        cfg,
        settings,
        "Explain how to structure an estimate with labor and material assumptions.",
        system_prompt=system_prompt,
        history_messages=[],
        explicit_skill_names=["revit"],
        pinned_skill_names=["estimate"],
        completion_fn=fake_completion,
    )

    assert [skill["name"] for skill in turn["skills"]] == [
        "revit-family-reference",
        "electrical-estimating",
    ]
    assert turn["skills"][0]["selection_sources"] == ["explicit"]
    assert turn["skills"][1]["selection_sources"] == ["pinned", "matched"]
    assert "Revit Family Reference" in captured_messages["messages"][-1]["content"]


def test_handle_shell_command_lists_and_shows_tools(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, metadata = resolve_agent_shell_system_prompt(cfg)
    session = initialize_session(
        settings,
        config_path="config.yaml",
        system_prompt_metadata=metadata,
    )

    list_result = handle_shell_command(cfg, settings, session, "/tools")
    list_payload = json.loads(list_result["response"])
    show_result = handle_shell_command(cfg, settings, session, "/tools show estimate")
    show_payload = json.loads(show_result["response"])

    assert list_result["exit"] is False
    assert list_payload["tool_count"] == 2
    assert list_payload["enabled_count"] == 2
    assert [tool["name"] for tool in list_payload["tools"]] == [
        "estimate_lookup",
        "revit_entity_lookup",
    ]
    assert show_payload["name"] == "estimate_lookup"
    assert show_payload["kind"] == "deterministic_tool"
    assert show_payload["enabled"] is True


def test_handle_shell_command_lists_and_shows_skills(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, metadata = resolve_agent_shell_system_prompt(cfg)
    session = initialize_session(
        settings,
        config_path="config.yaml",
        system_prompt_metadata=metadata,
    )

    list_result = handle_shell_command(cfg, settings, session, "/skills")
    list_payload = json.loads(list_result["response"])
    show_result = handle_shell_command(cfg, settings, session, "/skills show estimate")
    show_payload = json.loads(show_result["response"])

    assert list_result["exit"] is False
    assert list_payload["skill_count"] == 2
    assert [skill["name"] for skill in list_payload["skills"]] == [
        "electrical-estimating",
        "revit-family-reference",
    ]
    assert show_payload["name"] == "electrical-estimating"
    assert "Separate labor, material, and assumptions" in show_payload["instructions"]


def test_handle_shell_command_can_pin_and_queue_skills(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    _, metadata = resolve_agent_shell_system_prompt(cfg)
    session = initialize_session(
        settings,
        config_path="config.yaml",
        system_prompt_metadata=metadata,
    )

    pinned = handle_shell_command(cfg, settings, session, "/skills pin estimate")
    pinned_payload = json.loads(pinned["response"])
    queued = handle_shell_command(
        cfg,
        settings,
        pinned["session_summary"],
        "/skills use revit",
    )
    queued_payload = json.loads(queued["response"])
    cleared = handle_shell_command(
        cfg,
        settings,
        queued["session_summary"],
        "/skills clear",
    )
    cleared_payload = json.loads(cleared["response"])

    assert pinned_payload["pinned_skill_names"] == ["electrical-estimating"]
    assert queued_payload["next_turn_skill_names"] == ["revit-family-reference"]
    assert cleared_payload["pinned_skill_names"] == []
    assert cleared_payload["next_turn_skill_names"] == []


def test_handle_shell_command_lists_and_shows_commands(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, metadata = resolve_agent_shell_system_prompt(cfg)
    session = initialize_session(
        settings,
        config_path="config.yaml",
        system_prompt_metadata=metadata,
    )

    list_result = handle_shell_command(cfg, settings, session, "/commands")
    list_payload = json.loads(list_result["response"])
    show_result = handle_shell_command(cfg, settings, session, "/commands show route")
    show_payload = json.loads(show_result["response"])

    assert list_result["exit"] is False
    assert list_payload["command_count"] == 10
    assert [command["name"] for command in list_payload["commands"]] == [
        "help",
        "exit",
        "session",
        "commands",
        "skills",
        "tools",
        "providers",
        "route",
        "workflow",
        "tasks",
    ]
    assert show_payload["name"] == "route"
    assert show_payload["kind"] == "shell_command"
    assert "/route <instruction>" in show_payload["usage_examples"]


def test_handle_shell_command_lists_and_shows_tasks(tmp_path: Path) -> None:
    cfg = _base_cfg(tmp_path)
    settings = resolve_agent_shell_settings(cfg)
    system_prompt, metadata = resolve_agent_shell_system_prompt(cfg)
    session = initialize_session(
        settings,
        config_path="config.yaml",
        system_prompt_metadata=metadata,
    )

    tasks_dir = tmp_path / "agent_tasks" / "tasks"
    logs_dir = tmp_path / "agent_tasks" / "logs"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    (logs_dir / "agent-task-123.log").write_text("started\nfinished\n", encoding="utf-8")
    (tasks_dir / "agent-task-123.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "task_id": "agent-task-123",
                "kind": "workflow",
                "name": "demo",
                "status": "completed",
                "created_at": "2026-04-01T12:00:00Z",
                "updated_at": "2026-04-01T12:01:00Z",
                "started_at": "2026-04-01T12:00:05Z",
                "completed_at": "2026-04-01T12:01:00Z",
                "summary_path": str((tasks_dir / "agent-task-123.json").resolve()),
                "log_path": str((logs_dir / "agent-task-123.log").resolve()),
                "config_path": str((tmp_path / "config.yaml").resolve()),
                "pid": 12345,
                "source": "operator",
                "metadata": {"workflow": "demo"},
                "result": {"executed_steps": 1},
                "error": None,
                "exit_code": 0,
                "cancel_requested_at": None,
            }
        ),
        encoding="utf-8",
    )

    list_result = handle_shell_command(cfg, settings, session, "/tasks")
    status_result = handle_shell_command(cfg, settings, session, "/tasks status")
    show_result = handle_shell_command(cfg, settings, session, "/tasks show agent-task-123")
    attach_result = handle_shell_command(
        cfg,
        settings,
        session,
        "/tasks attach agent-task-123 --cursor 1 --limit 1",
    )
    list_payload = json.loads(list_result["response"])
    status_payload = json.loads(status_result["response"])
    show_payload = json.loads(show_result["response"])
    attach_payload = json.loads(attach_result["response"])

    assert list_result["exit"] is False
    assert list_payload["task_count"] == 1
    assert list_payload["tasks"][0]["task_id"] == "agent-task-123"
    assert status_payload["task_count"] == 1
    assert status_payload["recent_tasks"][0]["task_id"] == "agent-task-123"
    assert status_payload["restartable_task_count"] == 0
    assert show_payload["task"]["task_id"] == "agent-task-123"
    assert show_payload["log_tail"] == ["started", "finished"]
    assert attach_payload["attached_lines"] == ["finished"]
    assert attach_payload["next_cursor"] == 2
