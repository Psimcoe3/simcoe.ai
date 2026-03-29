"""
Scrape publicly accessible electrical product/spec pages and public labor-rate pages.

This script is intentionally limited to openly published web pages. It is useful
for collecting manufacturer product information, specification summaries,
category pages, and public labor-rate or prevailing-wage reference pages. It is
not a substitute for licensed labor-unit databases.

Source configuration is provided via YAML.

Usage:
    python scripts/scrape_public_data.py \
        --sources sources/public_sources.yaml \
        --out data/raw/public_scrape.jsonl

Then:
    python scripts/build_catalog_data.py \
        --source data/raw/public_scrape.jsonl \
        --out data/raw/public_catalog_examples.jsonl
"""

import argparse
import json
import time
from dataclasses import dataclass
from typing import Iterable
from urllib.parse import urljoin, urlparse

import requests
import yaml
from bs4 import BeautifulSoup


USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/135.0 Safari/537.36"
)

LABOR_LINK_TOKENS = (
    "wage",
    "prevailing",
    "determination",
    "classification",
    "electric",
    "electrician",
    "apprentice",
    "rate",
    "fringe",
    "dataset",
    "download",
    ".xls",
    ".xlsx",
    ".pdf",
)


@dataclass
class Source:
    kind: str
    manufacturer: str | None
    source_name: str | None
    start_urls: list[str]
    allowed_domains: list[str]
    include_patterns: list[str]
    max_pages: int
    request_timeout: int


def _same_domain(hostname: str, allowed_domains: list[str]) -> bool:
    return any(hostname == domain or hostname.endswith("." + domain) for domain in allowed_domains)


def _load_sources(path: str) -> list[Source]:
    with open(path, "r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}

    sources = []
    for item in config.get("sources", []):
        sources.append(
            Source(
                kind=item["kind"],
                manufacturer=item.get("manufacturer"),
                source_name=item.get("source_name") or item.get("manufacturer"),
                start_urls=item.get("start_urls", []),
                allowed_domains=item.get("allowed_domains", []),
                include_patterns=item.get("include_patterns", []),
                max_pages=int(item.get("max_pages", 10)),
                request_timeout=int(item.get("request_timeout", 12)),
            )
        )
    return sources


def _fetch(session: requests.Session, url: str, timeout: int) -> str:
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def _collect_links(url: str, soup: BeautifulSoup, source: Source) -> list[str]:
    discovered = []
    for tag in soup.select("a[href]"):
        href = tag.get("href", "").strip()
        if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("javascript:"):
            continue
        absolute = urljoin(url, href)
        parsed = urlparse(absolute)
        if parsed.scheme not in {"http", "https"}:
            continue
        if not _same_domain(parsed.hostname or "", source.allowed_domains):
            continue
        if source.include_patterns and not any(pattern in absolute for pattern in source.include_patterns):
            continue
        discovered.append(absolute)
    return discovered


def _text_or_none(node) -> str | None:
    if node is None:
        return None
    text = " ".join(node.get_text(" ", strip=True).split())
    return text or None


def _meta_content(soup: BeautifulSoup, *names: str) -> str | None:
    for name in names:
        tag = soup.find("meta", attrs={"property": name}) or soup.find("meta", attrs={"name": name})
        if tag and tag.get("content"):
            return " ".join(tag["content"].split())
    return None


def _extract_spec_pairs(soup: BeautifulSoup) -> dict[str, str]:
    specs = {}

    for row in soup.select("table tr"):
        cells = row.find_all(["th", "td"])
        if len(cells) >= 2:
            key = _text_or_none(cells[0])
            value = _text_or_none(cells[1])
            if key and value and len(key) < 80 and len(value) < 300:
                specs[key.lower()] = value

    for node in soup.select("dt"):
        key = _text_or_none(node)
        sibling = node.find_next_sibling("dd")
        value = _text_or_none(sibling)
        if key and value and len(key) < 80 and len(value) < 300:
            specs[key.lower()] = value

    return specs


def _extract_reference_links(
    url: str,
    soup: BeautifulSoup,
    source: Source,
    *,
    require_tokens: bool,
) -> list[dict[str, str]]:
    links = []
    seen = set()
    for tag in soup.select("a[href]"):
        href = tag.get("href", "").strip()
        text = _text_or_none(tag)
        if not href or not text:
            continue

        absolute = urljoin(url, href)
        parsed = urlparse(absolute)
        if parsed.scheme not in {"http", "https"}:
            continue
        if not _same_domain(parsed.hostname or "", source.allowed_domains):
            continue
        if source.include_patterns and not any(pattern in absolute for pattern in source.include_patterns):
            continue

        combined = f"{text} {absolute}".lower()
        if require_tokens and not any(token in combined for token in LABOR_LINK_TOKENS):
            continue

        key = (text, absolute)
        if key in seen:
            continue
        seen.add(key)
        links.append({"title": text, "url": absolute})
        if len(links) >= 12:
            break

    return links


def _collect_reference_points(soup: BeautifulSoup) -> list[str]:
    points = []
    for node in soup.select("main li, article li, .content li, #content li"):
        text = _text_or_none(node)
        if text and 20 <= len(text) <= 240:
            points.append(text)
        if len(points) >= 8:
            break

    if points:
        return points

    for node in soup.select("main p, article p, .content p, #content p"):
        text = _text_or_none(node)
        if text and 80 <= len(text) <= 320:
            points.append(text)
        if len(points) >= 4:
            break

    return points


def _extract_reference_record(url: str, soup: BeautifulSoup, source: Source, kind: str) -> dict | None:
    title = (
        _text_or_none(soup.find("h1"))
        or _meta_content(soup, "og:title", "twitter:title")
        or _text_or_none(soup.find("title"))
    )
    summary = _meta_content(soup, "description", "og:description", "twitter:description")
    key_points = _collect_reference_points(soup)
    reference_links = _extract_reference_links(
        url,
        soup,
        source,
        require_tokens=(kind == "labor_reference"),
    )

    if not title:
        return None

    path = urlparse(url).path.lower()
    lowered_title = title.lower()
    if any(token in path for token in ("/privacy", "/terms", "/contact", "/about", "/login", "/subscribe")):
        return None
    if any(token in lowered_title for token in ("privacy", "terms", "cookie", "login", "subscribe")):
        return None
    if not summary and not key_points and not reference_links:
        return None

    record = {
        "kind": kind,
        "source_name": source.source_name,
        "manufacturer": source.manufacturer,
        "page_title": title,
        "summary": summary,
        "key_points": key_points,
        "reference_links": reference_links,
        "source_url": url,
    }
    return {key: value for key, value in record.items() if value}


def _extract_catalog_record(url: str, soup: BeautifulSoup, source: Source) -> dict | None:
    title = (
        _text_or_none(soup.find("h1"))
        or _meta_content(soup, "og:title", "twitter:title")
        or _text_or_none(soup.find("title"))
    )
    description = _meta_content(soup, "description", "og:description", "twitter:description")
    specs = _extract_spec_pairs(soup)

    if not title and not description:
        return None

    pdf_links = []
    for tag in soup.select("a[href]"):
        href = tag.get("href", "")
        absolute = urljoin(url, href)
        if absolute.lower().endswith(".pdf"):
            pdf_links.append(absolute)

    signal_count = 0
    if description:
        signal_count += 1
    if specs:
        signal_count += 1
    if pdf_links:
        signal_count += 1

    path = urlparse(url).path.lower()
    lowered_title = (title or "").lower()
    if any(token in path for token in ("/patents", "/privacy", "/terms", "/contact", "/about")):
        return None
    if any(token in lowered_title for token in ("patent", "privacy", "terms", "intellectual property")):
        return None
    if signal_count == 0:
        return None
    if "/categories/" in path and signal_count < 2:
        return None

    record = {
        "manufacturer": source.manufacturer,
        "product_name": title,
        "description": description,
        "source_url": url,
    }

    field_map = {
        "part number": "part_number",
        "catalog number": "part_number",
        "model": "part_number",
        "category": "category",
        "type": "subcategory",
        "trade size": "trade_size",
        "material": "materials",
        "finish": "finish",
        "voltage": "voltage",
        "amperage": "amperage",
        "current rating": "amperage",
        "standards": "standards",
        "listings": "standards",
        "environment": "environment_rating",
        "mounting": "mounting",
        "application": "applications",
        "applications": "applications",
        "dimensions": "dimensions",
    }

    for source_key, target_key in field_map.items():
        if source_key in specs:
            record[target_key] = specs[source_key]

    if pdf_links:
        record["spec_sheet_url"] = pdf_links[0]

    return {key: value for key, value in record.items() if value}


def _extract_labor_records(url: str, soup: BeautifulSoup, source: Source) -> list[dict]:
    heading = _text_or_none(soup.find("h1")) or _meta_content(soup, "og:title") or "Public labor rate page"
    rows = []
    for table in soup.select("table"):
        headers = [_text_or_none(cell) for cell in table.select("tr th")]
        normalized_headers = [header.lower() for header in headers if header]
        if not headers or not any("wage" in header or "rate" in header or "fringe" in header for header in normalized_headers):
            continue

        for tr in table.select("tr"):
            cells = [_text_or_none(cell) for cell in tr.find_all("td")]
            if len(cells) != len(headers) or not any(cells):
                continue
            item = {
                "kind": "labor_rate",
                "source_name": source.source_name or source.manufacturer or heading,
                "page_title": heading,
                "source_url": url,
            }
            for header, value in zip(headers, cells):
                if header and value:
                    item[header.lower().replace(" ", "_")] = value
            rows.append(item)

    if rows:
        return rows

    reference_record = _extract_reference_record(url, soup, source, kind="labor_reference")
    return [reference_record] if reference_record else []


def scrape_source(session: requests.Session, source: Source) -> Iterable[dict]:
    queue = list(source.start_urls)
    seen = set()
    crawled = 0

    while queue and crawled < source.max_pages:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        crawled += 1

        try:
            html = _fetch(session, url, timeout=source.request_timeout)
        except Exception as exc:
            print(f"⚠️   Skipping {url}: {exc}")
            continue

        soup = BeautifulSoup(html, "html.parser")

        if source.kind == "catalog":
            record = _extract_catalog_record(url, soup, source)
            if record:
                yield record
        elif source.kind == "labor":
            yield from _extract_labor_records(url, soup, source)
        elif source.kind == "reference":
            record = _extract_reference_record(url, soup, source, kind="industry_reference")
            if record:
                yield record

        for discovered in _collect_links(url, soup, source):
            if discovered not in seen and discovered not in queue:
                queue.append(discovered)

        time.sleep(0.5)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape public electrical product/spec and labor-rate pages.")
    parser.add_argument("--sources", required=True, help="YAML file describing public web sources")
    parser.add_argument("--out", required=True, help="Output JSONL path")
    parser.add_argument(
        "--source-name",
        action="append",
        dest="source_names",
        help="Limit scraping to one or more configured source_name/manufacturer labels",
    )
    args = parser.parse_args()

    sources = _load_sources(args.sources)
    if not sources:
        raise SystemExit("❌  No sources found in configuration")

    if args.source_names:
        selected = set(args.source_names)
        sources = [
            source
            for source in sources
            if (source.source_name or source.manufacturer) in selected
        ]
        if not sources:
            raise SystemExit("❌  No configured sources matched --source-name")

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    count = 0
    with open(args.out, "w", encoding="utf-8") as handle:
        for source in sources:
            label = source.source_name or source.manufacturer or "public data"
            print(f"\n🔎  Scraping {source.kind} sources for {label}")
            for record in scrape_source(session, source):
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                count += 1

    print(f"\n✅  Wrote {count} public records to {args.out}")


if __name__ == "__main__":
    main()