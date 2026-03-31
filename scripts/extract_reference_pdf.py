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

from managed_source_defaults import load_managed_source_settings, resolve_managed_source_path
from pypdf import PdfReader


MAX_SUMMARY_CHARS = 700
MAX_POINT_CHARS = 220

SKIP_TITLE_PATTERNS = (
    "acknowledg",
    "preface",
    "copyright",
    "contents",
    "table of contents",
    "glossary",
    "index",
    "appendix",
    "review questions",
    "supplemental exercises",
    "practice problems",
    "section review",
    "answer key",
    "instructor resource",
    "case history",
)

SKIP_TEXT_PATTERNS = (
    "all rights reserved",
    "printed in the united states",
    "published by",
    "isbn",
    "technical editors",
    "this material is for the exclusive use",
    "possession and/or use by others is strictly prohibited",
    "pearson education",
    "user update",
    "powerpoint",
    "lesson plans",
    "answer the following questions",
    "use figure",
    "review questions",
    "supplemental exercises",
    "practice problems",
)

NORMALIZED_SKIP_TITLES = tuple(
    pattern.replace(" ", "")
    for pattern in (
        "acknowledgments",
        "preface",
        "copyright",
        "contents",
        "tableofcontents",
        "glossary",
        "index",
        "appendix",
        "reviewquestions",
        "supplementalexercises",
        "practiceproblems",
        "sectionreview",
        "sectionreviewcalculations",
        "sectionreviewanswerkey",
        "answerkey",
        "instructorresource",
        "casehistory",
    )
)

NORMALIZED_SKIP_TEXT_PATTERNS = tuple(
    re.sub(r"[^a-z]", "", pattern.lower())
    for pattern in (
        *SKIP_TEXT_PATTERNS,
        "curriculum@nccer.org",
        "feedback is welcome",
        "power points",
        "true or false",
        "which of the following",
        "fill in the blank",
        "review questions",
        "practice exercises",
        "practice problems",
        "supplemental exercises",
        "answer key",
        "use figure",
        "refer to figure",
        "answer the following questions",
    )
)


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
        if _ocr_noise_ratio(line.lower()) >= 0.20:
            continue
        seen.add(line)
        points.append(line)
        if len(points) >= 5:
            break
    return points


def _normalise_title_for_matching(value: str) -> str:
    lowered = value.lower().replace("vv", "w")
    return re.sub(r"[^a-z]", "", lowered)


def _looks_like_low_value_title(title: str) -> bool:
    lowered = title.lower().strip()
    normalized = _normalise_title_for_matching(title)
    if lowered in {"electrical", "njatc", "nccer"}:
        return True
    if lowered.startswith(("figure ", "review questions", "supplemental exercises", "practice problems")):
        return True
    if any(pattern in lowered for pattern in SKIP_TITLE_PATTERNS):
        return True
    return any(pattern in normalized for pattern in NORMALIZED_SKIP_TITLES)


def _ocr_noise_ratio(text: str) -> float:
    tokens = re.findall(r"\S+", text)
    if not tokens:
        return 1.0

    noisy = 0
    for token in tokens:
        punctuation_count = sum(not ch.isalnum() for ch in token)
        digit_count = sum(ch.isdigit() for ch in token)
        alpha_count = sum(ch.isalpha() for ch in token)
        if "�" in token:
            noisy += 1
            continue
        if punctuation_count >= max(3, len(token) // 2):
            noisy += 1
            continue
        if digit_count >= 3 and alpha_count >= 2:
            noisy += 1
            continue
        if re.search(r"[\"'`~^*_]{2,}", token):
            noisy += 1
            continue
    return noisy / len(tokens)


def _numbered_prompt_count(lines: list[str]) -> int:
    return sum(bool(re.match(r"^(?:[0-9]+|[A-Z])(?:[.)]|\s+-)", line.strip())) for line in lines)


def _looks_like_exercise_record(title: str, summary: str | None, key_points: list[str]) -> bool:
    joined = " ".join(part for part in [title, summary or "", *key_points] if part)
    lowered = joined.lower()
    normalized = re.sub(r"[^a-z]", "", _normalise_title_for_matching(joined))

    if any(pattern in normalized for pattern in NORMALIZED_SKIP_TEXT_PATTERNS):
        return True
    if title.lower().startswith("figure "):
        return True
    if _numbered_prompt_count(key_points) >= 2:
        return True
    if lowered.count("review questions") >= 1 and lowered.count("?") >= 2:
        return True
    if lowered.count("what ") + lowered.count("which ") + lowered.count("true or false") >= 3:
        return True
    return False


def _is_low_quality_record(title: str, summary: str | None, key_points: list[str], page_start: int, page_end: int) -> bool:
    joined = " ".join(part for part in [title, summary or "", *key_points] if part).lower()
    normalized_joined = re.sub(r"[^a-z]", "", _normalise_title_for_matching(joined))

    if _looks_like_low_value_title(title):
        return True
    if any(pattern in joined for pattern in SKIP_TEXT_PATTERNS):
        return True
    if any(pattern in normalized_joined for pattern in NORMALIZED_SKIP_TEXT_PATTERNS):
        return True
    if _looks_like_exercise_record(title, summary, key_points):
        return True
    if page_end <= 12 and any(pattern in joined for pattern in ("pearson", "edition", "published", "president", "vice president")):
        return True
    if _ocr_noise_ratio(joined) >= 0.18:
        return True
    return False


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
        if _is_low_quality_record(title, summary, key_points, page_numbers[0], page_numbers[-1]):
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
    parser.add_argument("--config", default="config.yaml", help="Config file with managed source defaults")
    parser.add_argument("--source", help="Path to the local PDF")
    parser.add_argument(
        "--managed-key",
        help="Optional managed_sources config key to use when --source is omitted (default: estimating_pdf)",
    )
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
    managed_sources = load_managed_source_settings(args.config)
    source = args.source or resolve_managed_source_path(
        managed_sources,
        args.managed_key or "estimating_pdf",
    )
    if not source:
        raise SystemExit(
            "Provide --source or configure the requested managed_sources path in the selected config"
        )

    source_path = Path(source)
    try:
        records, start_page, end_page = extract_pdf_records(
            str(source_path),
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