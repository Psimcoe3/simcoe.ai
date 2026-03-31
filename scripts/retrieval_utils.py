"""
Helpers for building and querying a lightweight local retrieval corpus.
"""

import json
import re
from collections import Counter


_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "what",
    "when",
    "which",
    "with",
    "you",
    "your",
}


def normalise_text(value: str) -> str:
    value = value.lower()
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def tokenize(value: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9]+", normalise_text(value))
    return [token for token in tokens if token not in _STOPWORDS and len(token) > 1]


def parse_reference_response(response: str) -> dict:
    lines = [line.rstrip() for line in response.splitlines()]
    source = None
    section = None
    body_lines = lines[:]

    if lines:
        match = re.match(r"Source:\s*(.*?)\s+—\s+(.*)", lines[0])
        if match:
            source = match.group(1).strip()
            section = match.group(2).strip()
            body_lines = lines[1:]

    body = "\n".join(line for line in body_lines).strip()
    key_points: list[str] = []
    for line in body_lines:
        stripped = line.strip()
        if stripped.startswith("-"):
            key_points.append(stripped.lstrip("- ").strip())

    return {
        "source": source,
        "section": section,
        "body": body,
        "key_points": key_points,
    }


def extract_instruction_text(prompt: str) -> str:
    match = re.search(r"### Instruction:\s*(.*?)\s*(?:### Input:|### Response:)", prompt, re.DOTALL)
    if not match:
        return prompt.strip()
    return match.group(1).strip()


def score_document(
    query: str,
    document: dict,
    preferred_source: str | None = None,
    preferred_section: str | None = None,
) -> float:
    query_tokens = Counter(tokenize(query))
    if not query_tokens:
        return 0.0

    source_tokens = set(tokenize(document.get("source", "")))
    section_tokens = set(tokenize(document.get("section", "")))
    content_tokens = Counter(tokenize(document.get("content", "")))
    query_token_set = set(query_tokens)

    section_overlap = len(query_token_set & section_tokens)
    source_overlap = len(query_token_set & source_tokens)
    content_overlap = sum(
        min(query_tokens[token], content_tokens.get(token, 0)) for token in query_token_set
    )

    normalized_query = normalise_text(query)
    normalized_document_source = normalise_text(document.get("source", ""))
    normalized_document_section = normalise_text(document.get("section", ""))
    phrase_bonus = 0.0
    if document.get("section") and normalized_query in normalise_text(document["section"]):
        phrase_bonus += 2.0
    if normalized_query and normalized_query in normalise_text(document.get("content", "")):
        phrase_bonus += 1.0

    hint_bonus = 0.0
    normalized_preferred_source = normalise_text(preferred_source or "")
    if normalized_preferred_source:
        if normalized_preferred_source == normalized_document_source:
            hint_bonus += 16.0
        else:
            hint_source_overlap = len(set(tokenize(preferred_source or "")) & source_tokens)
            hint_bonus += hint_source_overlap * 3.0

    normalized_preferred_section = normalise_text(preferred_section or "")
    if normalized_preferred_section:
        if normalized_preferred_section == normalized_document_section:
            hint_bonus += 10.0
        elif normalized_preferred_section in normalized_document_section:
            hint_bonus += 6.0

    if normalized_preferred_source and normalized_preferred_section:
        if (
            normalized_preferred_source == normalized_document_source
            and normalized_preferred_section == normalized_document_section
        ):
            hint_bonus += 8.0

    return float(
        section_overlap * 4 + source_overlap * 2 + content_overlap + phrase_bonus + hint_bonus
    )


def retrieve_documents(
    query: str,
    corpus: list[dict],
    top_k: int,
    min_score: float,
    preferred_source: str | None = None,
    preferred_section: str | None = None,
) -> list[dict]:
    ranked: list[dict] = []
    for document in corpus:
        score = score_document(
            query,
            document,
            preferred_source=preferred_source,
            preferred_section=preferred_section,
        )
        if score < min_score:
            continue

        ranked.append(
            {
                **document,
                "score": round(score, 4),
            }
        )

    ranked.sort(key=lambda item: (-item["score"], item.get("id", "")))
    return ranked[:top_k]


def format_retrieved_context(results: list[dict], max_context_chars: int) -> str:
    chunks: list[str] = []
    current_length = 0
    for index, item in enumerate(results, start=1):
        chunk = (
            f"[{index}] Source: {item.get('source') or 'Unknown'}\n"
            f"Section: {item.get('section') or 'Unknown'}\n"
            f"Content: {item.get('content', '').strip()}"
        ).strip()
        proposed_length = current_length + len(chunk) + (2 if chunks else 0)
        if chunks and proposed_length > max_context_chars:
            break
        chunks.append(chunk)
        current_length = proposed_length

    return "\n\n".join(chunks)


def build_retrieval_augmented_prompt(prompt: str, retrieved_context: str) -> str:
    if not retrieved_context.strip():
        return prompt

    if "### Response:" not in prompt:
        return f"{prompt}\n\n### Retrieved Context:\n{retrieved_context}"

    return prompt.replace(
        "### Response:",
        f"### Retrieved Context:\n{retrieved_context}\n\n### Response:",
        1,
    )


def load_jsonl(path: str) -> list[dict]:
    rows: list[dict] = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                rows.append(json.loads(stripped))
    return rows
