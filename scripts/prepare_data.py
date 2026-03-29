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

Output:
    data/processed/train/   — Arrow dataset shard
    data/processed/valid/   — Arrow dataset shard
"""

import argparse
import json
import os
import sys

import yaml
from datasets import Dataset, DatasetDict, load_dataset
from transformers import AutoTokenizer


# ── Chat template ──────────────────────────────────────────────────────────────

def format_example(example: dict) -> dict:
    """
    Convert a raw JSONL record into a single 'text' field using an
    Alpaca-style instruction template.  The 'input' field is optional.
    """
    instruction = example.get("instruction", "").strip()
    context = example.get("input", "").strip()
    response = example.get("response", example.get("output", "")).strip()

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

def validate_lengths(
    dataset: Dataset,
    tokenizer: AutoTokenizer,
    max_seq_length: int,
) -> Dataset:
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

    before = len(dataset)
    dataset = dataset.filter(
        lambda ex: ex["token_count"] <= max_seq_length,
        desc="Filtering over-length examples",
    )
    after = len(dataset)
    dropped = before - after

    if dropped:
        print(
            f"  ⚠️   Dropped {dropped} / {before} examples that exceeded "
            f"max_seq_length={max_seq_length} tokens."
        )
    else:
        print(f"  ✅  All {before} examples are within max_seq_length={max_seq_length}.")

    # Drop the temporary column — the training script doesn't need it.
    dataset = dataset.remove_columns(["token_count"])
    return dataset


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare JSONL data for fine-tuning.")
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to config.yaml (default: config.yaml)",
    )
    args = parser.parse_args()

    # Load config
    with open(args.config, "r") as f:
        cfg = yaml.safe_load(f)

    raw_path: str = cfg["data"]["raw_path"]
    processed_dir: str = cfg["data"]["processed_dir"]
    validation_split: float = cfg["data"]["validation_split"]
    random_state: int = cfg["data"]["random_state"]
    max_seq_length: int = cfg["model"]["max_seq_length"]
    model_name: str = cfg["model"]["name"]

    if not os.path.exists(raw_path):
        print(f"❌  Raw data file not found: {raw_path}")
        sys.exit(1)

    print(f"\n📂  Loading dataset from: {raw_path}")
    raw_dataset = load_dataset("json", data_files=raw_path, split="train")
    print(f"    Loaded {len(raw_dataset)} examples.")

    # Format into chat template
    print("\n📝  Formatting examples into instruction-response template …")
    formatted = raw_dataset.map(format_example, desc="Formatting")

    # Keep only the 'text' column
    columns_to_remove = [c for c in formatted.column_names if c != "text"]
    formatted = formatted.remove_columns(columns_to_remove)

    # Train / validation split (use random_state=3407 for reproducibility)
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

    # Length validation
    print(f"\n🔍  Loading tokeniser from '{model_name}' for length validation …")
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    except Exception as exc:
        print(f"  ⚠️   Could not load tokeniser ({exc}).  Skipping length validation.")
        tokenizer = None

    if tokenizer is not None:
        print("  Validating train set …")
        train_ds = validate_lengths(train_ds, tokenizer, max_seq_length)
        print("  Validating validation set …")
        valid_ds = validate_lengths(valid_ds, tokenizer, max_seq_length)

    # Save to disk
    os.makedirs(processed_dir, exist_ok=True)
    train_path = os.path.join(processed_dir, "train")
    valid_path = os.path.join(processed_dir, "valid")

    print(f"\n💾  Saving processed datasets …")
    train_ds.save_to_disk(train_path)
    valid_ds.save_to_disk(valid_path)

    print(f"    Train → {train_path}")
    print(f"    Valid → {valid_path}")
    print("\n✅  Data preparation complete.\n")


if __name__ == "__main__":
    main()
