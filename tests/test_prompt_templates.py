from __future__ import annotations

import agent_shell
import evaluate
import export
import generate_data
from prompt_templates import render_system_prompt_template, resolve_configured_system_prompt


def test_render_system_prompt_template_applies_required_variables() -> None:
    rendered = render_system_prompt_template(
        "grounded-domain-baseline",
        variables={"domain": "NEC code interpretation"},
        library_path="prompts/system_prompt_templates.yaml",
    )

    assert "You are a domain-focused assistant for NEC code interpretation." in rendered


def test_resolve_generation_system_prompt_uses_behavior_equivalent_template() -> None:
    prompt, metadata = generate_data.resolve_generation_system_prompt(
        {
            "system_prompts": {
                "library_path": "prompts/system_prompt_templates.yaml",
                "generate_data": {"template_id": "synthetic-data-generator"},
            }
        }
    )

    assert prompt == generate_data._SYSTEM_PROMPT.rstrip("\n")
    assert metadata["template_id"] == "synthetic-data-generator"


def test_resolve_judge_system_prompt_uses_behavior_equivalent_template() -> None:
    prompt, metadata = evaluate.resolve_judge_system_prompt(
        {
            "system_prompts": {
                "library_path": "prompts/system_prompt_templates.yaml",
                "evaluation_judge": {"template_id": "evaluation-rubric-judge"},
            }
        }
    )

    assert prompt == evaluate._JUDGE_SYSTEM_PROMPT
    assert metadata["template_id"] == "evaluation-rubric-judge"


def test_resolve_modelfile_system_prompt_uses_behavior_equivalent_template() -> None:
    prompt, metadata = export.resolve_modelfile_system_prompt(
        {
            "system_prompts": {
                "library_path": "prompts/system_prompt_templates.yaml",
                "export_modelfile": {"template_id": "runtime-helpful-assistant"},
            }
        }
    )

    assert prompt == "You are a helpful AI assistant fine-tuned on domain-specific data.\n"
    assert metadata["template_id"] == "runtime-helpful-assistant"


def test_resolve_agent_shell_system_prompt_uses_behavior_equivalent_template() -> None:
    prompt, metadata = agent_shell.resolve_agent_shell_system_prompt(
        {
            "system_prompts": {
                "library_path": "prompts/system_prompt_templates.yaml",
                "agent_shell": {"template_id": "interactive-grounded-operator"},
            }
        }
    )

    assert prompt == agent_shell._SYSTEM_PROMPT.rstrip("\n")
    assert metadata["template_id"] == "interactive-grounded-operator"


def test_resolve_configured_system_prompt_falls_back_without_surface_config() -> None:
    prompt, metadata = resolve_configured_system_prompt(
        {"system_prompts": {"library_path": "prompts/system_prompt_templates.yaml"}},
        "export_modelfile",
        "fallback",
    )

    assert prompt == "fallback"
    assert metadata["configured"] is False
