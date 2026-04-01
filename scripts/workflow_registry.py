from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path
import subprocess
import sys

import yaml

from config_validation import load_config, validate_workflow_registry_config
from indexed_memory import append_dream_log_entry, record_dream_session, run_memory_dream


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_REGISTRY_SCHEMA_VERSION = 1


class WorkflowRegistryError(ValueError):
    pass


def resolve_workflow_registry_settings(cfg: dict) -> dict:
    workflow_registry = (
        cfg.get("workflow_registry") if isinstance(cfg.get("workflow_registry"), dict) else {}
    )
    manifest_path = workflow_registry.get("manifest_path") or "workflows/registry.yaml"
    return {
        "enabled": bool(workflow_registry.get("enabled", False)),
        "manifest_path": str(manifest_path),
    }


def _resolve_repo_path(path: str) -> str:
    candidate = Path(path).expanduser()
    if candidate.is_absolute():
        return str(candidate.resolve())
    return str((REPO_ROOT / candidate).resolve())


def _require_non_empty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise WorkflowRegistryError(f"{label} must be a non-empty string")
    return value


def _require_string_list(value: object, label: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list):
        raise WorkflowRegistryError(f"{label} must be a list of strings")
    if not value and not allow_empty:
        raise WorkflowRegistryError(f"{label} must not be empty")
    return [_require_non_empty_string(item, label) for item in value]


def _require_mapping(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        raise WorkflowRegistryError(f"{label} must be a mapping")
    return value


def _coerce_template_value(value: object, label: str) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return value
    raise WorkflowRegistryError(f"{label} must be a string, integer, float, or boolean")


def validate_workflow_manifest(manifest: dict) -> dict:
    if not isinstance(manifest, dict):
        raise WorkflowRegistryError("workflow registry manifest must be a mapping")

    schema_version = manifest.get("schema_version")
    if (
        isinstance(schema_version, bool)
        or not isinstance(schema_version, int)
        or schema_version < 1
    ):
        raise WorkflowRegistryError("workflow registry schema_version must be a positive integer")

    workflows = _require_mapping(manifest.get("workflows"), "workflow registry workflows")
    if not workflows:
        raise WorkflowRegistryError("workflow registry workflows must not be empty")

    normalized_workflows: dict[str, dict] = {}
    for workflow_name, raw_workflow in workflows.items():
        cleaned_name = _require_non_empty_string(workflow_name, "workflow name").strip().lower()
        workflow = _require_mapping(raw_workflow, f"workflow '{cleaned_name}'")
        description = _require_non_empty_string(
            workflow.get("description"),
            f"workflow '{cleaned_name}'.description",
        )
        steps = workflow.get("steps")
        if not isinstance(steps, list) or not steps:
            raise WorkflowRegistryError(f"workflow '{cleaned_name}'.steps must be a non-empty list")

        required_vars = _require_string_list(
            workflow.get("required_vars", []),
            f"workflow '{cleaned_name}'.required_vars",
            allow_empty=True,
        )
        if len(required_vars) != len(set(required_vars)):
            raise WorkflowRegistryError(
                f"workflow '{cleaned_name}'.required_vars must not contain duplicates"
            )

        defaults_raw = workflow.get("defaults", {})
        defaults = _require_mapping(defaults_raw, f"workflow '{cleaned_name}'.defaults")
        normalized_defaults = {
            _require_non_empty_string(
                key, f"workflow '{cleaned_name}'.defaults key"
            ): _coerce_template_value(
                value,
                f"workflow '{cleaned_name}'.defaults.{key}",
            )
            for key, value in defaults.items()
        }

        tags = _require_string_list(
            workflow.get("tags", []),
            f"workflow '{cleaned_name}'.tags",
            allow_empty=True,
        )

        normalized_steps: list[dict] = []
        for index, raw_step in enumerate(steps):
            step = _require_mapping(raw_step, f"workflow '{cleaned_name}'.steps[{index}]")
            step_name = _require_non_empty_string(
                step.get("name"),
                f"workflow '{cleaned_name}'.steps[{index}].name",
            )
            argv = _require_string_list(
                step.get("argv"),
                f"workflow '{cleaned_name}'.steps[{index}].argv",
            )
            cwd = step.get("cwd")
            if cwd is not None:
                cwd = _require_non_empty_string(
                    cwd,
                    f"workflow '{cleaned_name}'.steps[{index}].cwd",
                )

            env_raw = step.get("env", {})
            env = _require_mapping(env_raw, f"workflow '{cleaned_name}'.steps[{index}].env")
            normalized_env = {
                _require_non_empty_string(
                    key,
                    f"workflow '{cleaned_name}'.steps[{index}].env key",
                ): _coerce_template_value(
                    value,
                    f"workflow '{cleaned_name}'.steps[{index}].env.{key}",
                )
                for key, value in env.items()
            }

            normalized_steps.append(
                {
                    "name": step_name,
                    "argv": argv,
                    "cwd": cwd,
                    "env": normalized_env,
                }
            )

        normalized_workflows[cleaned_name] = {
            "description": description,
            "required_vars": required_vars,
            "defaults": normalized_defaults,
            "tags": tags,
            "steps": normalized_steps,
        }

    return {
        "schema_version": schema_version,
        "workflows": normalized_workflows,
    }


def load_workflow_registry(cfg: dict) -> dict:
    settings = resolve_workflow_registry_settings(cfg)
    manifest_path = _resolve_repo_path(settings["manifest_path"])
    if not os.path.isfile(manifest_path):
        raise WorkflowRegistryError(f"workflow registry manifest not found: {manifest_path}")

    try:
        with open(manifest_path, "r", encoding="utf-8") as handle:
            payload = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        raise WorkflowRegistryError(f"could not parse workflow registry manifest: {exc}") from exc

    manifest = validate_workflow_manifest(payload)
    return {
        "enabled": settings["enabled"],
        "manifest_path": manifest_path,
        **manifest,
    }


def list_workflows(cfg: dict) -> dict:
    registry = load_workflow_registry(cfg)
    workflows = []
    for workflow_name in sorted(registry["workflows"]):
        workflow = registry["workflows"][workflow_name]
        workflows.append(
            {
                "name": workflow_name,
                "description": workflow["description"],
                "step_count": len(workflow["steps"]),
                "required_vars": workflow["required_vars"],
                "defaults": copy.deepcopy(workflow["defaults"]),
                "tags": workflow["tags"],
            }
        )

    return {
        "enabled": registry["enabled"],
        "manifest_path": registry["manifest_path"],
        "schema_version": registry["schema_version"],
        "workflows": workflows,
    }


def get_workflow(cfg: dict, workflow_name: str) -> dict:
    cleaned_name = _require_non_empty_string(workflow_name, "workflow name").strip().lower()
    registry = load_workflow_registry(cfg)
    workflow = registry["workflows"].get(cleaned_name)
    if workflow is None:
        known = ", ".join(sorted(registry["workflows"]))
        raise WorkflowRegistryError(
            f"unknown workflow '{cleaned_name}'. Available workflows: {known}"
        )

    return {
        "enabled": registry["enabled"],
        "manifest_path": registry["manifest_path"],
        "schema_version": registry["schema_version"],
        "name": cleaned_name,
        **copy.deepcopy(workflow),
    }


def _render_template(value: str, variables: dict, label: str) -> str:
    try:
        return value.format(**variables)
    except KeyError as exc:
        missing_key = exc.args[0]
        raise WorkflowRegistryError(f"{label} requires missing variable '{missing_key}'") from exc


def _workflow_variables(
    config_path: str, workflow: dict, extra_vars: dict[str, str] | None = None
) -> dict:
    variables = {
        "python": sys.executable,
        "config": os.path.abspath(config_path),
        "repo_root": str(REPO_ROOT),
    }
    variables.update(copy.deepcopy(workflow.get("defaults", {})))
    if extra_vars:
        variables.update({key: str(value) for key, value in extra_vars.items()})

    missing = [key for key in workflow.get("required_vars", []) if not variables.get(key)]
    if missing:
        raise WorkflowRegistryError(
            f"workflow '{workflow['name']}' is missing required variables: {', '.join(sorted(missing))}"
        )

    return variables


def render_workflow_steps(
    cfg: dict,
    config_path: str,
    workflow_name: str,
    extra_vars: dict[str, str] | None = None,
) -> dict:
    workflow = get_workflow(cfg, workflow_name)
    variables = _workflow_variables(config_path, workflow, extra_vars)
    rendered_steps: list[dict] = []
    for index, step in enumerate(workflow["steps"]):
        rendered_argv = [
            _render_template(
                part, variables, f"workflow '{workflow['name']}' step {index + 1} argv"
            )
            for part in step["argv"]
        ]
        if step.get("cwd"):
            cwd = _render_template(
                step["cwd"],
                variables,
                f"workflow '{workflow['name']}' step {index + 1} cwd",
            )
        else:
            cwd = str(REPO_ROOT)
        rendered_env = {
            key: _render_template(
                value,
                variables,
                f"workflow '{workflow['name']}' step {index + 1} env.{key}",
            )
            for key, value in step["env"].items()
        }
        rendered_steps.append(
            {
                "name": step["name"],
                "argv": rendered_argv,
                "cwd": _resolve_repo_path(cwd),
                "env": rendered_env,
            }
        )

    return {
        "enabled": workflow["enabled"],
        "manifest_path": workflow["manifest_path"],
        "schema_version": workflow["schema_version"],
        "workflow": workflow["name"],
        "description": workflow["description"],
        "required_vars": workflow["required_vars"],
        "defaults": workflow["defaults"],
        "tags": workflow["tags"],
        "variables": variables,
        "steps": rendered_steps,
    }


def run_workflow(
    cfg: dict,
    config_path: str,
    workflow_name: str,
    extra_vars: dict[str, str] | None = None,
    *,
    dry_run: bool = False,
) -> dict:
    rendered = render_workflow_steps(cfg, config_path, workflow_name, extra_vars)
    dream_cfg = cfg.get("dream") if isinstance(cfg.get("dream"), dict) else {}
    dream_enabled = bool(dream_cfg.get("enabled", False))
    dream_result: dict = {
        "enabled": dream_enabled,
        "status": "disabled" if not dream_enabled else "not_run",
    }
    if dry_run:
        return {
            **rendered,
            "dry_run": True,
            "executed_steps": 0,
            "dream": dream_result,
        }

    executed_steps = 0
    dream_session = None
    current_step = None

    if dream_enabled:
        try:
            dream_session = record_dream_session(
                cfg,
                source="workflow_registry",
                summary=f"Workflow run started ({rendered['workflow']})",
                details=(f"workflow={rendered['workflow']} steps={len(rendered['steps'])}"),
                metadata={
                    "workflow": rendered["workflow"],
                    "step_count": len(rendered["steps"]),
                    "tags": list(rendered["tags"]),
                    "dry_run": False,
                },
            )
        except Exception as exc:
            dream_result = {
                "enabled": True,
                "status": "session_error",
                "error": str(exc),
            }

    try:
        for step in rendered["steps"]:
            current_step = step
            print(f"▶ {step['name']}")
            subprocess.run(
                step["argv"],
                cwd=step["cwd"],
                env={**os.environ, **step["env"]},
                check=True,
            )
            executed_steps += 1
    except subprocess.CalledProcessError:
        if dream_enabled:
            try:
                append_dream_log_entry(
                    cfg,
                    category="workflow_failure",
                    summary=f"Workflow failed ({rendered['workflow']})",
                    details=(
                        f"workflow={rendered['workflow']} "
                        f"step={current_step['name'] if isinstance(current_step, dict) else 'unknown'} "
                        f"executed_steps={executed_steps}"
                    ),
                    source="workflow_registry",
                    session_id=(
                        dream_session.get("session_id") if isinstance(dream_session, dict) else None
                    ),
                    metadata={
                        "workflow": rendered["workflow"],
                        "step_name": current_step["name"]
                        if isinstance(current_step, dict)
                        else None,
                        "executed_steps": executed_steps,
                    },
                )
            except Exception:
                pass
        raise

    if dream_enabled:
        try:
            append_dream_log_entry(
                cfg,
                category="workflow_result",
                summary=f"Workflow finished ({rendered['workflow']})",
                details=(f"workflow={rendered['workflow']} executed_steps={executed_steps}"),
                source="workflow_registry",
                session_id=(
                    dream_session.get("session_id") if isinstance(dream_session, dict) else None
                ),
                metadata={
                    "workflow": rendered["workflow"],
                    "executed_steps": executed_steps,
                    "tags": list(rendered["tags"]),
                },
            )
            dream_result = run_memory_dream(cfg)
        except Exception as exc:
            dream_result = {
                "enabled": True,
                "status": "failed",
                "error": str(exc),
            }

    return {
        **rendered,
        "dry_run": False,
        "executed_steps": executed_steps,
        "dream": dream_result,
    }


def _parse_vars(values: list[str]) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            raise WorkflowRegistryError(f"workflow variable '{item}' must use KEY=VALUE format")
        key, value = item.split("=", 1)
        cleaned_key = _require_non_empty_string(key, "workflow variable name").strip()
        parsed[cleaned_key] = value
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect and run checked-in operator workflows.")
    parser.add_argument(
        "--config", default="config.yaml", help="Config file with workflow registry settings"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List available workflows")
    show_parser = subparsers.add_parser("show", help="Show one workflow definition")
    show_parser.add_argument("workflow", help="Workflow name to show")
    subparsers.add_parser("validate", help="Validate the workflow registry manifest")
    run_parser = subparsers.add_parser("run", help="Run a workflow")
    run_parser.add_argument("workflow", help="Workflow name to run")
    run_parser.add_argument(
        "--var",
        action="append",
        default=[],
        help="Template variable assignment in KEY=VALUE form. Can be repeated.",
    )
    run_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Render the workflow without executing its steps.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)
    validate_workflow_registry_config(cfg)

    try:
        if args.command == "list":
            payload = list_workflows(cfg)
        elif args.command == "show":
            payload = get_workflow(cfg, args.workflow)
        elif args.command == "validate":
            registry = load_workflow_registry(cfg)
            payload = {
                "enabled": registry["enabled"],
                "manifest_path": registry["manifest_path"],
                "schema_version": registry["schema_version"],
                "valid": True,
                "workflow_count": len(registry["workflows"]),
            }
        elif args.command == "run":
            payload = run_workflow(
                cfg,
                args.config,
                args.workflow,
                _parse_vars(args.var),
                dry_run=bool(args.dry_run),
            )
        else:
            raise WorkflowRegistryError(f"unsupported command: {args.command}")
    except WorkflowRegistryError as exc:
        print(f"❌  {exc}")
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"❌  workflow step failed with exit code {exc.returncode}")
        return exc.returncode or 1

    print(json.dumps(payload, indent=2, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
