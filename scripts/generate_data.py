"""
scripts/generate_data.py
────────────────────────
Generate synthetic training examples using a local Ollama model or
OpenAI-compatible API.

Reads topic descriptions from a YAML file and produces JSONL rows that match
the pipeline's expected schema: {"instruction", "input" (optional), "response"}.

Usage (local, fully private):
    python scripts/generate_data.py --topics topics.yaml --out data/raw/generated.jsonl
    python scripts/generate_data.py --topics topics.yaml --out data/raw/generated.jsonl --count 20

Using OpenAI instead:
    python scripts/generate_data.py --topics topics.yaml --out data/raw/generated.jsonl --model openai/gpt-4o
    python scripts/generate_data.py --config config.yaml --topics topics.yaml --out data/raw/generated.jsonl --count 20

Then merge into your main dataset:
    cat data/raw/generated.jsonl >> data/raw/dataset.jsonl

Prerequisites:
    • For local generation: Ollama must be running (ollama serve).
    • For OpenAI: OPENAI_API_KEY must be set in the environment.
    • A topics YAML file describing the domains and example styles.
"""

import argparse
import json
import os
import sys
import time

import yaml
from dotenv import load_dotenv

from config_validation import load_config, validate_system_prompts_config
from prompt_templates import (
    SYSTEM_PROMPT_SURFACE_GENERATE_DATA,
    resolve_configured_system_prompt,
)

load_dotenv()

_SYSTEM_PROMPT = """\
You are a training-data generator for a domain-specific language model.

Given a topic description, produce a JSON array of instruction-tuning examples.
Each example must be a JSON object with these keys:
  - "instruction": a clear, specific question or task (string)
  - "input": optional additional context (string or omit the key)
  - "response": a thorough, accurate answer (string, 100-400 words)

Rules:
  1. Vary question types: definitional, procedural, scenario-based, comparative.
  2. Responses must be factually accurate and cite specific standards/codes/sections when applicable.
  3. Do NOT repeat the same question with minor rewording.
  4. Return ONLY the JSON array, no markdown fences or commentary.
"""


def resolve_generation_system_prompt(cfg: dict | None = None) -> tuple[str, dict]:
    default_prompt = _SYSTEM_PROMPT.rstrip("\n")
    if not isinstance(cfg, dict):
        return default_prompt, {
            "surface": SYSTEM_PROMPT_SURFACE_GENERATE_DATA,
            "configured": False,
            "source": "default",
            "template_id": None,
            "variables": {},
            "library_path": None,
        }

    return resolve_configured_system_prompt(
        cfg,
        SYSTEM_PROMPT_SURFACE_GENERATE_DATA,
        default_prompt,
    )


def generate_batch(
    client,
    model: str,
    topic: dict,
    count: int,
    system_prompt: str,
) -> list[dict]:
    """Ask the LLM to produce `count` examples for a single topic."""
    topic_name = topic["name"]
    topic_description = topic["description"]
    example_styles = topic.get("example_styles", "questions, procedures, scenarios")

    user_prompt = (
        f"Topic: {topic_name}\n"
        f"Description: {topic_description}\n"
        f"Example styles to include: {example_styles}\n\n"
        f"Generate exactly {count} diverse instruction-tuning examples for this topic.\n"
        f"Return ONLY a valid JSON array. No extra text before or after."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.8,
        max_tokens=4096,
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
    if raw.endswith("```"):
        raw = raw.rsplit("```", 1)[0]
    raw = raw.strip()

    # Try to extract JSON array from the response
    examples = _parse_json_array(raw)

    # Validate each example
    validated = []
    for ex in examples:
        if not isinstance(ex, dict):
            continue
        instruction = ex.get("instruction", "").strip()
        response_text = ex.get("response", "").strip()
        if not instruction or not response_text:
            continue
        record = {"instruction": instruction, "response": response_text}
        input_text = (ex.get("input") or "").strip()
        if input_text:
            record["input"] = input_text
        validated.append(record)

    return validated


def _parse_json_array(raw: str) -> list:
    """Robustly parse a JSON array from LLM output, handling common issues."""
    import re as _re

    # First try direct parse
    try:
        result = json.loads(raw)
        if isinstance(result, list):
            return result
        if isinstance(result, dict):
            return [result]
    except json.JSONDecodeError:
        pass

    # Try to find the outermost [...] bracket pair
    start = raw.find("[")
    if start != -1:
        depth = 0
        end = start
        for i in range(start, len(raw)):
            if raw[i] == "[":
                depth += 1
            elif raw[i] == "]":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        try:
            return json.loads(raw[start:end])
        except json.JSONDecodeError:
            pass

    # Try to fix common issues: control characters inside strings
    cleaned = raw
    # Remove control characters except \n \r \t within the text
    cleaned = _re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', ' ', cleaned)
    try:
        result = json.loads(cleaned)
        if isinstance(result, list):
            return result
    except json.JSONDecodeError:
        pass

    # Try extracting individual JSON objects with regex
    objects = []
    for m in _re.finditer(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', raw):
        try:
            obj = json.loads(m.group())
            if "instruction" in obj and "response" in obj:
                objects.append(obj)
        except json.JSONDecodeError:
            continue
    if objects:
        return objects

    raise ValueError(f"Could not parse JSON from model output ({len(raw)} chars)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate synthetic training examples from topic descriptions."
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Optional config file used for runtime system prompt template selection.",
    )
    parser.add_argument(
        "--topics",
        required=True,
        help="Path to a YAML file describing topics to generate examples for.",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output JSONL file path (appends if it already exists).",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of examples to generate per topic (default: 10).",
    )
    parser.add_argument(
        "--model",
        default="simcoe",
        help="Model to use: Ollama model name (default: simcoe) or 'openai/<model>' for OpenAI API.",
    )
    args = parser.parse_args()

    system_prompt = _SYSTEM_PROMPT.rstrip("\n")
    system_prompt_info = {
        "surface": SYSTEM_PROMPT_SURFACE_GENERATE_DATA,
        "configured": False,
        "source": "default",
        "template_id": None,
        "variables": {},
        "library_path": None,
    }
    if args.config:
        cfg = load_config(args.config)
        validate_system_prompts_config(cfg)
        system_prompt, system_prompt_info = resolve_generation_system_prompt(cfg)
        if system_prompt_info["configured"]:
            print(
                "Using generation system prompt template "
                f"'{system_prompt_info['template_id']}'"
            )

    use_openai = args.model.startswith("openai/")

    try:
        from openai import OpenAI
    except ImportError:
        print("❌  openai package not installed. Run: pip install openai")
        sys.exit(1)

    if use_openai:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("❌  OPENAI_API_KEY not set. Add it to .env or export it.")
            sys.exit(1)
        client = OpenAI(api_key=api_key)
        model_name = args.model.removeprefix("openai/")
    else:
        # Use Ollama's OpenAI-compatible API
        client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        model_name = args.model

    with open(args.topics, "r", encoding="utf-8") as f:
        topics_cfg = yaml.safe_load(f)

    topics = topics_cfg.get("topics", [])
    if not topics:
        print("❌  No topics found in the YAML file.")
        sys.exit(1)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)

    total_generated = 0
    max_retries = 3

    with open(args.out, "a", encoding="utf-8") as out_file:
        for topic in topics:
            name = topic.get("name", "unknown")
            print(f"\n📝  Generating {args.count} examples for: {name}")

            for attempt in range(1, max_retries + 1):
                try:
                    examples = generate_batch(
                        client,
                        model_name,
                        topic,
                        args.count,
                        system_prompt,
                    )
                    for ex in examples:
                        out_file.write(json.dumps(ex, ensure_ascii=False) + "\n")
                    total_generated += len(examples)
                    print(f"    ✅  Wrote {len(examples)} examples")
                    break
                except Exception as exc:
                    if attempt < max_retries:
                        print(f"    ⚠️   Attempt {attempt} failed: {exc}. Retrying …")
                        time.sleep(1)
                    else:
                        print(f"    ❌  Failed after {max_retries} attempts for '{name}': {exc}")

            # Rate-limit courtesy
            time.sleep(1)

    print(f"\n✅  Total: {total_generated} examples written to {args.out}")


if __name__ == "__main__":
    main()
