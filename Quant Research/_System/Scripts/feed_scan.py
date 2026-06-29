#!/usr/bin/env python
"""
Stdlib-only RSS/Atom feed scanner for the quant-research Obsidian library.
Prints recent entries as JSON. Feed failures are reported per-feed but do not fail the run.
"""
from __future__ import annotations

import email.utils
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

FEEDS = [
    {
        "name": "Quantocracy",
        "url": "https://quantocracy.com/feed/",
        "kind": "practitioner-aggregator",
        "caution": "aggregator; triage for reproducibility and costs",
    },
    {
        "name": "Alpha Architect",
        "url": "https://alphaarchitect.com/feed/",
        "kind": "practitioner-research",
        "caution": "often useful but verify paper/source and implementation assumptions",
    },
    {
        "name": "Robot Wealth",
        "url": "https://robotwealth.com/feed/",
        "kind": "practitioner-research",
        "caution": "prioritize posts with code/data and realistic costs",
    },
    {
        "name": "Quantpedia",
        "url": "https://quantpedia.com/feed/",
        "kind": "strategy-research",
        "caution": "often summary/paywalled; use as lead, not evidence",
    },
    {
        "name": "arXiv q-fin trading and market microstructure",
        "url": "https://export.arxiv.org/api/query?search_query=cat:q-fin.TR+OR+cat:q-fin.ST+OR+cat:q-fin.PM&sortBy=submittedDate&sortOrder=descending&max_results=10",
        "kind": "academic",
        "caution": "paper feed; still check methods, costs, leakage, and practicality",
    },
]

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
}


def text(el):
    if el is None or el.text is None:
        return ""
    return " ".join(el.text.split())


def parse_date(raw: str) -> str:
    raw = (raw or "").strip()
    if not raw:
        return ""
    try:
        dt = email.utils.parsedate_to_datetime(raw)
        if dt:
            return dt.astimezone(timezone.utc).date().isoformat()
    except Exception:
        pass
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return raw[:10]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "HermesQuantResearch/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read()


def parse_feed(blob: bytes, limit: int):
    root = ET.fromstring(blob)
    tag = root.tag.lower()
    entries = []

    if tag.endswith("feed"):
        for e in root.findall("atom:entry", NS)[:limit]:
            link = ""
            link_el = e.find("atom:link", NS)
            if link_el is not None:
                link = link_el.attrib.get("href", "")
            entries.append({
                "title": text(e.find("atom:title", NS)),
                "url": link or text(e.find("atom:id", NS)),
                "published": parse_date(text(e.find("atom:published", NS)) or text(e.find("atom:updated", NS))),
                "summary": text(e.find("atom:summary", NS))[:500],
            })
    else:
        channel = root.find("channel")
        items = channel.findall("item") if channel is not None else root.findall(".//item")
        for item in items[:limit]:
            entries.append({
                "title": text(item.find("title")),
                "url": text(item.find("link")),
                "published": parse_date(text(item.find("pubDate")) or text(item.find("{http://purl.org/dc/elements/1.1/}date"))),
                "summary": text(item.find("description"))[:500],
            })
    return entries


def main() -> int:
    per_feed_limit = 5
    out = {"generated_at_utc": datetime.now(timezone.utc).isoformat(), "feeds": []}
    for feed in FEEDS:
        rec = {k: feed[k] for k in ("name", "url", "kind", "caution")}
        try:
            rec["entries"] = parse_feed(fetch(feed["url"]), per_feed_limit)
            rec["ok"] = True
        except Exception as exc:
            rec["ok"] = False
            rec["error"] = f"{type(exc).__name__}: {exc}"
            rec["entries"] = []
        out["feeds"].append(rec)
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
