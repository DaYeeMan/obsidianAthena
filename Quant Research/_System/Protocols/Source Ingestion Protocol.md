---
type: source-ingestion-protocol
tags: [quant-research, sources, ingestion]
---

# Source Ingestion Protocol

Use this protocol to improve source discovery beyond ad hoc paper search.

## Daily Collection Inputs

The daily collector should combine:

1. arXiv / Semantic Scholar paper discovery,
2. direct RSS/feed scan using `_System/Scripts/feed_scan.py`,
3. credible practitioner research blogs when available,
4. existing registry gaps and coding queue needs.

## Feed Scan Script

Script path:

`C:/Users/enson/Documents/Obsidian Vault/Quant Research/_System/Scripts/feed_scan.py`

The script is intentionally stdlib-only and can run even though `blogwatcher-cli` is not installed. It prints recent feed entries as JSON. The collector should treat feed entries as leads, not evidence.

## Quality Filter

Do not add a feed item to the library unless it provides one of:

- a testable strategy hypothesis,
- reproducible methodology,
- useful data/backtest warning,
- foundational method,
- credible decay/outdatedness evidence.

## Feed Lead Treatment

Practitioner posts are lower evidentiary weight than papers unless they include transparent methodology, code, data, and realistic costs. When in doubt, classify as `Plausible but untested` or `Speculative`, not `Evidence-backed`.
