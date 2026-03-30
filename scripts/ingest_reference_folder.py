"""
Ingest a local folder of manuals, notes, and code-like files into JSONL records.

This script is designed for mixed local reference trees. It recursively scans a
folder and emits structured JSONL records that can later be reviewed and, where
appropriate, converted into training examples with build_catalog_data.py.

Supported inputs:
    - PDFs: summarized into short attributed reference notes via extract_reference_pdf
    - Text/Markdown/YAML/JSON files: chunked into reference notes
    - Code files: chunked into code reference records for logic/code understanding

Usage:
    python scripts/ingest_reference_folder.py \
        --root "/mnt/c/Users/Paul/source/repos/Psimcoe3/Simcoe-Design/References/docs/Electrical Material" \
        --out data/raw/electrical_material_reference.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from data_contracts import build_data_contract, stable_identifier
from extract_reference_pdf import extract_pdf_records
from managed_source_defaults import load_managed_source_settings, resolve_managed_source_path


TEXT_EXTENSIONS = {".txt", ".md", ".rst", ".yaml", ".yml", ".json"}
CODE_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".cs", ".java", ".go", ".rs",
    ".c", ".cpp", ".h", ".hpp", ".sql", ".sh", ".ps1",
}


def _clean_line(value: str | None) -> str | None:
    if not value:
        return None
    cleaned = value.replace("\x00", " ")
    cleaned = re.sub(r"\s+", " ", value.replace("\x00", " ")).strip()
    return cleaned or None


def _read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            return None


def _title_from_lines(lines: list[str], fallback: str) -> str:
    for line in lines[:10]:
        if 5 <= len(line) <= 120 and not re.fullmatch(r"[=#*\-\s]+", line):
            return line
    return fallback


def _summary_from_lines(lines: list[str], max_chars: int = 700) -> str | None:
    if not lines:
        return None
    summary_parts = []
    current = 0
    for line in lines:
        if len(line) < 25:
            continue
        extra = len(line) + (1 if summary_parts else 0)
        if current + extra > max_chars:
            break
        summary_parts.append(line)
        current += extra
        if len(summary_parts) >= 4:
            break
    return " ".join(summary_parts) if summary_parts else None


def _chunk_lines(lines: list[str], chunk_size: int) -> list[list[str]]:
    chunks = []
    for index in range(0, len(lines), chunk_size):
        chunk = [line for line in lines[index:index + chunk_size] if line]
        if chunk:
            chunks.append(chunk)
    return chunks


def _text_records(path: Path, root: Path, source_name: str, chunk_lines: int) -> list[dict]:
    content = _read_text(path)
    if not content:
        return []
    lines = [_clean_line(line) for line in content.splitlines()]
    lines = [line for line in lines if line]
    if len(lines) < 3:
        return []

    records = []
    relative_source_path = str(path.relative_to(root))
    for index, chunk in enumerate(_chunk_lines(lines, chunk_lines), start=1):
        title = _title_from_lines(chunk, f"{path.stem} chunk {index}")
        summary = _summary_from_lines(chunk)
        key_points = [line for line in chunk[1:6] if 30 <= len(line) <= 220]
        if not summary and not key_points:
            continue
        records.append(
            {
                "kind": "reference",
                "source_name": source_name,
                "page_title": title,
                "summary": summary,
                "key_points": key_points,
                "record_id": stable_identifier(
                    "reference_note",
                    relative_source_path,
                    f"text_chunk_{index}",
                ),
                "source_path": str(path),
                "relative_source_path": relative_source_path,
                "record_group": f"text_chunk_{index}",
                "data_contract": build_data_contract(
                    data_family="reference_notes",
                    runtime_owner="retrieval",
                    routing_hint="retrieval_only",
                ),
            }
        )
    return records


def _language_for_path(path: Path) -> str:
    return path.suffix.lower().lstrip(".") or "text"


def _code_records(path: Path, root: Path, source_name: str, chunk_lines: int) -> list[dict]:
    content = _read_text(path)
    if not content:
        return []
    lines = content.splitlines()
    if len(lines) < 5:
        return []

    records = []
    relative_source_path = str(path.relative_to(root))
    for index, chunk in enumerate(_chunk_lines(lines, chunk_lines), start=1):
        normalized_chunk = [_clean_line(line) for line in chunk]
        normalized_chunk = [line for line in normalized_chunk if line]
        if len(normalized_chunk) < 3:
            continue
        title = _title_from_lines(normalized_chunk, f"{path.name} chunk {index}")
        summary = _summary_from_lines(normalized_chunk, max_chars=500)
        records.append(
            {
                "kind": "code_reference",
                "source_name": source_name,
                "page_title": title,
                "summary": summary,
                "key_points": normalized_chunk[:5],
                "record_id": stable_identifier(
                    "code_reference",
                    relative_source_path,
                    f"code_chunk_{index}",
                ),
                "source_path": str(path),
                "relative_source_path": relative_source_path,
                "language": _language_for_path(path),
                "record_group": f"code_chunk_{index}",
                "data_contract": build_data_contract(
                    data_family="code_reference_notes",
                    runtime_owner="retrieval",
                    routing_hint="retrieval_only",
                ),
            }
        )
    return records


def _collect_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ingest a local mixed reference folder into JSONL")
    parser.add_argument("--config", default="config.yaml", help="Config file with managed source defaults")
    parser.add_argument("--root", help="Root folder to scan recursively")
    parser.add_argument("--out", required=True, help="Output JSONL path")
    parser.add_argument("--source-name", help="Optional source label for all emitted records")
    parser.add_argument(
        "--text-chunk-lines",
        type=int,
        default=20,
        help="Number of lines per text/code chunk for non-PDF files (default: 20)",
    )
    parser.add_argument(
        "--pdf-chunk-size",
        type=int,
        default=2,
        help="Number of pages per PDF note record (default: 2)",
    )
    parser.add_argument(
        "--pdf-min-chars",
        type=int,
        default=250,
        help="Minimum extracted chars for each PDF note record (default: 250)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    managed_sources = load_managed_source_settings(args.config)
    root_value = args.root or resolve_managed_source_path(
        managed_sources,
        "estimating_reference_root",
        "reference_root",
    )
    if not root_value:
        raise SystemExit(
            "Provide --root or configure managed_sources.estimating_reference_root/reference_root"
        )

    root = Path(root_value)
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Folder not found: {root}")

    source_name = args.source_name or root.name
    records = []
    counts = {"pdf": 0, "text": 0, "code": 0}

    for path in _collect_files(root):
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            pdf_records, _, _ = extract_pdf_records(
                str(path),
                source_name=f"{source_name} / {path.stem}",
                chunk_size=args.pdf_chunk_size,
                min_chars=args.pdf_min_chars,
                start_page=1,
                end_page=None,
            )
            for record in pdf_records:
                relative_source_path = str(path.relative_to(root))
                record["relative_source_path"] = relative_source_path
                record["record_id"] = stable_identifier(
                    "reference_note",
                    relative_source_path,
                    record.get("page_start"),
                    record.get("page_end"),
                )
                record["data_contract"] = build_data_contract(
                    data_family="reference_notes",
                    runtime_owner="retrieval",
                    routing_hint="retrieval_only",
                )
            records.extend(pdf_records)
            counts["pdf"] += len(pdf_records)
            continue
        if suffix in TEXT_EXTENSIONS:
            chunk_records = _text_records(path, root, source_name, args.text_chunk_lines)
            records.extend(chunk_records)
            counts["text"] += len(chunk_records)
            continue
        if suffix in CODE_EXTENSIONS:
            chunk_records = _code_records(path, root, source_name, args.text_chunk_lines)
            records.extend(chunk_records)
            counts["code"] += len(chunk_records)

    if not records:
        raise SystemExit("No supported records were found in the folder")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(
        f"Wrote {len(records)} records from {root} to {out_path} "
        f"(pdf={counts['pdf']}, text={counts['text']}, code={counts['code']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())