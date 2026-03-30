"""
Extract short, attributed reference notes from a local PDF.

This script is intended for local manuals, estimator books, and other
reference-only material that should not be ingested as raw page dumps. It reads
PDF text, groups pages into small chunks, and writes concise JSONL reference
records that the existing build_catalog_data.py reference path can reuse.

Usage:
    python scripts/extract_reference_pdf.py \
        --source sources/2026_national_electrical_estimator_ebook.pdf \
        --out data/raw/estimator_ebook_notes.jsonl

Then, if the source is approved for example generation:
    python scripts/build_catalog_data.py \
        --source data/raw/estimator_ebook_notes.jsonl \
        --out data/raw/estimator_ebook_examples.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pypdf import PdfReader


MAX_SUMMARY_CHARS = 700
MAX_POINT_CHARS = 220


def _clean_line(value: str | None) -> str | None:
    if not value:
        return None
    cleaned = value.replace("\x00", " ")
    cleaned = cleaned.replace("\u2019", "'")
    cleaned = cleaned.replace("\u2013", "-")
    cleaned = cleaned.replace("\u2014", "-")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned or None


def _clean_block(value: str | None) -> str | None:
    if not value:
        return None
    raw_lines = []
    for raw_line in value.splitlines():
        cleaned = _clean_line(raw_line)
        if cleaned:
            raw_lines.append(cleaned)

    lines = []
    for line in raw_lines:
        if not lines:
            lines.append(line)
            continue

        previous = lines[-1]
        if previous.endswith("-") and line[:1].islower():
            lines[-1] = previous[:-1] + line
            continue

        if (
            len(previous) >= 35
            and previous[-1] not in ".:;!?"
            and line[:1].islower()
        ):
            lines[-1] = previous + " " + line
            continue

        lines.append(line)

    return "\n".join(lines) or None


def _page_lines(text: str) -> list[str]:
    lines = []
    for raw_line in text.splitlines():
        cleaned = _clean_line(raw_line)
        if cleaned:
            lines.append(cleaned)
    return lines


def _looks_like_heading(line: str) -> bool:
    if len(line) > 120:
        return False
    if sum(ch.isalpha() for ch in line) < 4:
        return False
    if line.lower().startswith(("page ", "copyright", "isbn ")):
        return False
    if re.fullmatch(r"[0-9 .:-]+", line):
        return False
    return True


def _pick_title(lines: list[str], fallback: str) -> str:
    for line in lines[:12]:
        if _looks_like_heading(line):
            return line
    return fallback


def _split_sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def _build_summary(text: str) -> str | None:
    normalized_text = " ".join(_page_lines(text))
    sentences = _split_sentences(normalized_text)
    if not sentences:
        cleaned = _clean_line(normalized_text)
        if not cleaned:
            return None
        return cleaned[:MAX_SUMMARY_CHARS].rstrip()

    summary_parts = []
    current_length = 0
    for sentence in sentences:
        if len(summary_parts) >= 4:
            break
        extra = len(sentence) + (1 if summary_parts else 0)
        if current_length + extra > MAX_SUMMARY_CHARS:
            break
        summary_parts.append(sentence)
        current_length += extra

    if not summary_parts:
        return sentences[0][:MAX_SUMMARY_CHARS].rstrip()
    return " ".join(summary_parts)


def _build_key_points(lines: list[str], title: str) -> list[str]:
    points = []
    seen = {title}
    for line in lines:
        if line in seen:
            continue
        if len(line) < 35 or len(line) > MAX_POINT_CHARS:
            continue
        if line.lower().startswith(("page ", "section ", "chapter ")):
            continue
        seen.add(line)
        points.append(line)
        if len(points) >= 5:
            break
    return points


def _iter_page_text(reader: PdfReader):
    for page_number, page in enumerate(reader.pages, start=1):
        text = _clean_block(page.extract_text() or "")
        if text:
            yield page_number, text


def _looks_like_table_of_contents(lines: list[str]) -> bool:
    if len(lines) < 8:
        return False
    dot_leader_lines = sum("..." in line for line in lines[:20])
    numbered_entry_lines = sum(bool(re.search(r"\b\d{1,3}$", line)) for line in lines[:20])
    return dot_leader_lines >= 5 or numbered_entry_lines >= 8


def _build_records(
    source_path: Path,
    source_name: str,
    pages: list[tuple[int, str]],
    chunk_size: int,
    min_chars: int,
) -> list[dict]:
    records = []
    for index in range(0, len(pages), chunk_size):
        chunk = pages[index:index + chunk_size]
        if not chunk:
            continue

        page_numbers = [page_number for page_number, _ in chunk]
        chunk_text = "\n".join(text for _, text in chunk)
        if len(chunk_text) < min_chars:
            continue

        lines = _page_lines(chunk_text)
        if not lines:
            continue
        if _looks_like_table_of_contents(lines):
            continue

        fallback = f"{source_name} pages {page_numbers[0]}-{page_numbers[-1]}"
        title = _pick_title(lines, fallback)
        summary = _build_summary(chunk_text)
        key_points = _build_key_points(lines, title)
        if not summary and not key_points:
            continue

        record = {
            "kind": "reference",
            "source_name": source_name,
            "page_title": title,
            "summary": summary,
            "key_points": key_points,
            "source_path": str(source_path),
            "page_start": page_numbers[0],
            "page_end": page_numbers[-1],
        }
        records.append({key: value for key, value in record.items() if value not in (None, [], "")})
    return records


def extract_pdf_records(
    source: str,
    *,
    source_name: str | None = None,
    chunk_size: int = 2,
    min_chars: int = 250,
    start_page: int = 1,
    end_page: int | None = None,
) -> tuple[list[dict], int, int]:
    source_path = Path(source)
    if not source_path.exists():
        raise FileNotFoundError(f"PDF not found: {source_path}")
    if source_path.suffix.lower() != ".pdf":
        raise ValueError("source must point to a .pdf file")
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")
    if start_page < 1:
        raise ValueError("start_page must be at least 1")

    reader = PdfReader(str(source_path))
    page_count = len(reader.pages)
    final_end_page = end_page or page_count
    if final_end_page < start_page:
        raise ValueError("end_page must be greater than or equal to start_page")

    selected_pages = [
        (page_number, text)
        for page_number, text in _iter_page_text(reader)
        if start_page <= page_number <= final_end_page
    ]
    final_source_name = source_name or source_path.stem.replace("_", " ")
    records = _build_records(
        source_path=source_path,
        source_name=final_source_name,
        pages=selected_pages,
        chunk_size=chunk_size,
        min_chars=min_chars,
    )
    return records, start_page, final_end_page


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract structured reference notes from a PDF")
    parser.add_argument("--source", required=True, help="Path to the local PDF")
    parser.add_argument("--out", required=True, help="Output JSONL path")
    parser.add_argument(
        "--source-name",
        help="Optional display name for the source; defaults to the PDF filename stem",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=2,
        help="Number of pages to group into each note record (default: 2)",
    )
    parser.add_argument(
        "--min-chars",
        type=int,
        default=250,
        help="Minimum extracted characters required for a note record (default: 250)",
    )
    parser.add_argument(
        "--start-page",
        type=int,
        default=1,
        help="First page to include, 1-based inclusive (default: 1)",
    )
    parser.add_argument(
        "--end-page",
        type=int,
        help="Last page to include, 1-based inclusive (default: end of document)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_path = Path(args.source)
    try:
        records, start_page, end_page = extract_pdf_records(
            args.source,
            source_name=args.source_name,
            chunk_size=args.chunk_size,
            min_chars=args.min_chars,
            start_page=args.start_page,
            end_page=args.end_page,
        )
    except (FileNotFoundError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc
    if not records:
        raise SystemExit("No reference note records were generated from the selected page range")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(
        f"Wrote {len(records)} reference note records from {source_path} "
        f"({start_page}-{end_page}) to {out_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())