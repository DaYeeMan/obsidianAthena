---
type: source-ingestion-protocol
tags: [quant-research, sources, ingestion]
---

# Source Ingestion Protocol

Use this protocol to improve source discovery beyond ad hoc paper search.

## Daily Collection Inputs

The daily collector should combine:

1. arXiv / Semantic Scholar paper discovery,
2. persistent RSS/feed state from `blogwatcher-cli`,
3. credible practitioner research blogs when available,
4. existing registry gaps and coding queue needs.

## Feed Collection Path

Primary feed collector:

`blogwatcher-cli` with database `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`

Hermes cron runs `C:/Users/enson/.hermes/quant-research/scripts/quant_research_collect_sources.py`, which initializes configured feeds in blogwatcher, scans them, and emits `blogwatcher_feed_leads` in the pre-run JSON. The collector should treat feed entries as leads, not evidence.

Fallback script:

`C:/Users/enson/Documents/Obsidian Vault/Quant Research/_System/Scripts/feed_scan.py`

The stdlib fallback script exists only for degraded operation if `blogwatcher-cli` is unavailable or failing. If fallback output is used, record that plainly in the review note instead of implying persistent feed-state coverage.

## Quality Filter

Do not add a feed item to the library unless it provides one of:

- a testable strategy hypothesis,
- reproducible methodology,
- useful data/backtest warning,
- foundational method,
- credible decay/outdatedness evidence.

## Feed Lead Treatment

Practitioner posts are lower evidentiary weight than papers unless they include transparent methodology, code, data, and realistic costs. When in doubt, classify as `Plausible but untested` or `Speculative`, not `Evidence-backed`.
