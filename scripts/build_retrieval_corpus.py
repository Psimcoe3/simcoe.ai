"""
Build a deduplicated retrieval corpus from electrician reference examples.
"""

import argparse
import hashlib
import json
import os
from collections import Counter

from manifest_utils import current_utc_timestamp, sha256_file, write_json_file
from retrieval_utils import parse_reference_response


def build_document_id(source: str | None, section: str | None, body: str) -> str:
    digest = hashlib.sha256()
    digest.update((source or "").encode("utf-8"))
    digest.update(b"\x00")
    digest.update((section or "").encode("utf-8"))
    digest.update(b"\x00")
    digest.update(body.encode("utf-8"))
    return digest.hexdigest()[:16]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a retrieval corpus from electrician examples.")
    parser.add_argument("--source", required=True, help="Path to the source example JSONL file.")
    parser.add_argument("--out", required=True, help="Path to the output retrieval corpus JSONL file.")
    parser.add_argument(
        "--manifest",
        required=True,
        help="Path to the output retrieval corpus manifest JSON file.",
    )
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    os.makedirs(os.path.dirname(args.manifest), exist_ok=True)

    documents_by_id: dict[str, dict] = {}
    source_counter = Counter()
    input_rows = 0

    with open(args.source, "r", encoding="utf-8") as handle:
        for raw_line in handle:
            stripped = raw_line.strip()
            if not stripped:
                continue

            input_rows += 1
            row = json.loads(stripped)
            response = row.get("response") or row.get("output") or ""
            parsed = parse_reference_response(response)

            doc_id = build_document_id(parsed.get("source"), parsed.get("section"), parsed["body"])
            source = parsed.get("source") or "UNKNOWN"
            source_counter[source] += 1

            if doc_id not in documents_by_id:
                documents_by_id[doc_id] = {
                    "id": doc_id,
                    "source": parsed.get("source"),
                    "section": parsed.get("section"),
                    "content": parsed["body"],
                    "key_points": parsed.get("key_points", []),
                    "sample_instructions": [],
                }

            sample_instructions = documents_by_id[doc_id]["sample_instructions"]
            instruction = row.get("instruction")
            if isinstance(instruction, str) and instruction.strip() and instruction not in sample_instructions:
                if len(sample_instructions) < 3:
                    sample_instructions.append(instruction.strip())

    documents = sorted(documents_by_id.values(), key=lambda item: (item.get("source") or "", item.get("section") or "", item["id"]))

    with open(args.out, "w", encoding="utf-8") as handle:
        for document in documents:
            handle.write(json.dumps(document, ensure_ascii=False))
            handle.write("\n")

    manifest = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "source": {
            "path": os.path.abspath(args.source),
            "sha256": sha256_file(args.source),
        },
        "output": {
            "path": os.path.abspath(args.out),
            "count": len(documents),
        },
        "input_rows": input_rows,
        "dedupe": {
            "unique_documents": len(documents),
            "duplicate_rows_removed": input_rows - len(documents),
        },
        "source_distribution": dict(source_counter.most_common()),
    }
    write_json_file(args.manifest, manifest)

    print(f"Built retrieval corpus with {len(documents)} documents → {args.out}")
    print(f"Manifest written to {args.manifest}")


if __name__ == "__main__":
    main()