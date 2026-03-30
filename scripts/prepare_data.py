"""
scripts/prepare_data.py
───────────────────────
Load a JSONL file, format every example into an instruction-response chat
template, split 90 / 10 into train / validation sets, validate that no example
exceeds max_seq_length, and save the processed dataset to disk.

Usage:
    python scripts/prepare_data.py [--config config.yaml]

Input JSONL format (each line is a JSON object):
    {"instruction": "...", "input": "...", "response": "..."}
    The "input" field is optional — it is appended to the instruction when
    present (Alpaca-style).

Schema rules:
    - instruction: required non-empty string
    - input: optional string
    - response or output: at least one required non-empty string
    - response and output may both be present only when they match
    - metadata: optional JSON object
    - tags: optional list of non-empty strings
    - chat-style rows such as messages/conversations must be converted first

Output:
    data/processed/train/   — Arrow dataset shard
    data/processed/valid/   — Arrow dataset shard
"""

import argparse
import json
import os
import sys

from datasets import Dataset, load_dataset
from config_validation import load_config, validate_prepare_data_config
from manifest_utils import current_utc_timestamp, sha256_file, summarise_numeric, write_json_file
from tokenizer_utils import load_tokenizer_with_compat


SUPPORTED_RESPONSE_KEYS = ("response", "output")


def _is_non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _normalise_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return value.strip()


def _validate_tags(tags: object, line_number: int, errors: list[str]) -> None:
    if not isinstance(tags, list):
        errors.append(f"line {line_number}: 'tags' must be a list of non-empty strings")
        return

    invalid_indexes = [
        index for index, item in enumerate(tags, start=1)
        if not isinstance(item, str) or not item.strip()
    ]
    if invalid_indexes:
        positions = ", ".join(str(index) for index in invalid_indexes[:5])
        if len(invalid_indexes) > 5:
            positions += ", ..."
        errors.append(
            f"line {line_number}: 'tags' contains invalid entries at positions {positions}"
        )


def _summarise_unique_texts(texts: list[str]) -> dict[str, int]:
    unique_text_count = len(set(texts))
    return {
        "unique_text_rows": unique_text_count,
        "duplicate_text_rows": len(texts) - unique_text_count,
    }


# ── Chat template ──────────────────────────────────────────────────────────────

def format_example(example: dict) -> dict:
    """
    Convert a raw JSONL record into a single 'text' field using an
    Alpaca-style instruction template.  The 'input' field is optional.
    """
    instruction = (example.get("instruction") or "").strip()
    context = (example.get("input") or "").strip()
    response = (example.get("response") or example.get("output") or "").strip()

    if context:
        text = (
            f"### Instruction:\n{instruction}\n\n"
            f"### Input:\n{context}\n\n"
            f"### Response:\n{response}"
        )
    else:
        text = (
            f"### Instruction:\n{instruction}\n\n"
            f"### Response:\n{response}"
        )

    return {"text": text}


# ── Validation ─────────────────────────────────────────────────────────────────


def validate_raw_jsonl(raw_path: str) -> None:
    """Validate JSONL formatting and the expected instruction-tuning schema."""
    errors: list[str] = []
    record_count = 0

    with open(raw_path, "r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            stripped_line = raw_line.strip()

            if not stripped_line:
                errors.append(f"line {line_number}: blank lines are not allowed")
                continue

            try:
                record = json.loads(stripped_line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_number}: invalid JSON ({exc.msg})")
                continue

            if not isinstance(record, dict):
                errors.append(f"line {line_number}: each row must be a JSON object")
                continue

            instruction = record.get("instruction")
            context = record.get("input")
            response = record.get("response")
            output = record.get("output")

            if not isinstance(instruction, str) or not instruction.strip():
                errors.append(
                    f"line {line_number}: 'instruction' must be a non-empty string"
                )

            if "input" in record and not isinstance(context, str):
                errors.append(f"line {line_number}: 'input' must be a string when present")

            if not _is_non_empty_string(response) and not _is_non_empty_string(output):
                errors.append(
                    f"line {line_number}: provide a non-empty '{SUPPORTED_RESPONSE_KEYS[0]}' or '{SUPPORTED_RESPONSE_KEYS[1]}' string"
                )

            if response is not None and not isinstance(response, str):
                errors.append(f"line {line_number}: 'response' must be a string when present")

            if output is not None and not isinstance(output, str):
                errors.append(f"line {line_number}: 'output' must be a string when present")

            if _is_non_empty_string(response) and _is_non_empty_string(output):
                if _normalise_text(response) != _normalise_text(output):
                    errors.append(
                        f"line {line_number}: 'response' and 'output' are both present but differ"
                    )

            if "metadata" in record and not isinstance(record["metadata"], dict):
                errors.append(f"line {line_number}: 'metadata' must be an object when present")

            if "tags" in record:
                _validate_tags(record["tags"], line_number, errors)

            if "messages" in record or "conversations" in record:
                errors.append(
                    f"line {line_number}: chat-style datasets are not supported directly; convert them to instruction/response rows first"
                )

            record_count += 1

    if record_count == 0:
        print(f"❌  Raw data file is empty: {raw_path}")
        sys.exit(1)

    if errors:
        print("❌  Dataset schema validation failed.")
        for error in errors[:10]:
            print(f"    - {error}")
        if len(errors) > 10:
            print(f"    - ... and {len(errors) - 10} more error(s)")
        sys.exit(1)

    print(f"  ✅  Validated {record_count} JSONL records against the expected schema.")


def validate_lengths(
    dataset: Dataset,
    tokenizer: AutoTokenizer,
    max_seq_length: int,
) -> tuple[Dataset, dict]:
    """
    Tokenise every example and remove any whose token count exceeds
    max_seq_length.  Prints a summary of how many examples were dropped.
    """

    def _tokenize(batch: dict) -> dict:
        tokens = tokenizer(
            batch["text"],
            truncation=False,
            padding=False,
            add_special_tokens=True,
        )
        batch["token_count"] = [len(ids) for ids in tokens["input_ids"]]
        return batch

    dataset = dataset.map(_tokenize, batched=True, desc="Tokenising for length check")

    token_counts = dataset["token_count"]
    before = len(dataset)
    dataset = dataset.filter(
        lambda ex: ex["token_count"] <= max_seq_length,
        desc="Filtering over-length examples",
    )
    kept_token_counts = dataset["token_count"]
    after = len(dataset)
    dropped = before - after
    dropped_token_counts = [count for count in token_counts if count > max_seq_length]

    if dropped:
        print(
            f"  ⚠️   Dropped {dropped} / {before} examples that exceeded "
            f"max_seq_length={max_seq_length} tokens."
        )
    else:
        print(f"  ✅  All {before} examples are within max_seq_length={max_seq_length}.")

    summary = {
        "before_rows": before,
        "after_rows": after,
        "dropped_rows": dropped,
        "max_seq_length": max_seq_length,
        "kept_token_count": summarise_numeric(kept_token_counts),
        "dropped_token_count": summarise_numeric(dropped_token_counts),
    }

    dataset = dataset.remove_columns(["token_count"])
    return dataset, summary


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare JSONL data for fine-tuning.")
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to config.yaml (default: config.yaml)",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)

    validate_prepare_data_config(cfg)

    raw_path: str = cfg["data"]["raw_path"]
    processed_dir: str = cfg["data"]["processed_dir"]
    validation_split: float = cfg["data"]["validation_split"]
    random_state: int = cfg["data"]["random_state"]
    max_seq_length: int = cfg["model"]["max_seq_length"]
    model_name: str = cfg["model"]["name"]

    if not os.path.exists(raw_path):
        print(f"❌  Raw data file not found: {raw_path}")
        sys.exit(1)

    print(f"\n🔎  Validating raw JSONL schema: {raw_path}")
    validate_raw_jsonl(raw_path)

    print(f"\n📂  Loading dataset from: {raw_path}")
    raw_dataset = load_dataset("json", data_files=raw_path, split="train")
    print(f"    Loaded {len(raw_dataset)} examples.")

    if len(raw_dataset) < 2:
        print("❌  Need at least 2 examples to create train and validation splits.")
        sys.exit(1)

    print("\n📝  Formatting examples into instruction-response template …")
    formatted = raw_dataset.map(format_example, desc="Formatting")

    columns_to_remove = [c for c in formatted.column_names if c != "text"]
    formatted = formatted.remove_columns(columns_to_remove)
    text_dedupe_summary = _summarise_unique_texts(formatted["text"])

    print(f"\n✂️   Splitting dataset: {100*(1-validation_split):.0f}% train / "
          f"{100*validation_split:.0f}% validation (seed={random_state}) …")
    split = formatted.train_test_split(
        test_size=validation_split,
        shuffle=True,
        seed=random_state,
    )
    train_ds = split["train"]
    valid_ds = split["test"]
    print(f"    Train: {len(train_ds)} examples")
    print(f"    Valid: {len(valid_ds)} examples")

    if len(train_ds) == 0 or len(valid_ds) == 0:
        print(
            "❌  The current validation split produced an empty train or validation set. "
            "Adjust data.validation_split or add more examples."
        )
        sys.exit(1)

    print(f"\n🔍  Loading tokeniser from '{model_name}' for length validation …")
    try:
        tokenizer = load_tokenizer_with_compat(model_name)
    except Exception as exc:
        print(f"  ⚠️   Could not load tokeniser ({exc}).  Skipping length validation.")
        tokenizer = None
        train_length_summary = {
            "skipped": True,
            "reason": str(exc),
        }
        valid_length_summary = {
            "skipped": True,
            "reason": str(exc),
        }

    if tokenizer is not None:
        print("  Validating train set …")
        train_ds, train_length_summary = validate_lengths(train_ds, tokenizer, max_seq_length)
        print("  Validating validation set …")
        valid_ds, valid_length_summary = validate_lengths(valid_ds, tokenizer, max_seq_length)

    if len(train_ds) == 0 or len(valid_ds) == 0:
        print(
            "❌  All examples in either the train or validation split were removed during "
            "length validation. Increase model.max_seq_length or shorten the dataset entries."
        )
        sys.exit(1)

    os.makedirs(processed_dir, exist_ok=True)
    train_path = os.path.join(processed_dir, "train")
    valid_path = os.path.join(processed_dir, "valid")
    manifest_path = os.path.join(processed_dir, "manifest.json")

    print(f"\n💾  Saving processed datasets …")
    train_ds.save_to_disk(train_path)
    valid_ds.save_to_disk(valid_path)

    manifest = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "config_path": os.path.abspath(args.config),
        "source": {
            "raw_path": os.path.abspath(raw_path),
            "sha256": sha256_file(raw_path),
            "size_bytes": os.path.getsize(raw_path),
        },
        "processing": {
            "model_name": model_name,
            "max_seq_length": max_seq_length,
            "validation_split": validation_split,
            "random_state": random_state,
        },
        "counts": {
            "raw_rows": len(raw_dataset),
            "formatted_rows": len(formatted),
            **text_dedupe_summary,
            "train_rows": len(train_ds),
            "valid_rows": len(valid_ds),
        },
        "length_validation": {
            "tokenizer_model": model_name if tokenizer is not None else None,
            "skipped": tokenizer is None,
            "train": train_length_summary,
            "valid": valid_length_summary,
        },
        "dataset_fingerprints": {
            "raw": getattr(raw_dataset, "_fingerprint", None),
            "formatted": getattr(formatted, "_fingerprint", None),
            "train": getattr(train_ds, "_fingerprint", None),
            "valid": getattr(valid_ds, "_fingerprint", None),
        },
        "outputs": {
            "processed_dir": os.path.abspath(processed_dir),
            "train_path": os.path.abspath(train_path),
            "valid_path": os.path.abspath(valid_path),
        },
    }
    write_json_file(manifest_path, manifest)

    print(f"    Train → {train_path}")
    print(f"    Valid → {valid_path}")
    print(f"    Manifest → {manifest_path}")
    print("\n✅  Data preparation complete.\n")


if __name__ == "__main__":
    main()
