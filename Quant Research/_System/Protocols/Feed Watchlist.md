---
type: feed-watchlist
tags: [quant-research, rss, sources]
---

# Feed Watchlist

The primary feed scanner uses `blogwatcher-cli` with database `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`. The stdlib `_System/Scripts/feed_scan.py` remains only as a degraded fallback if blogwatcher-cli is unavailable or failing.

The configured feed set currently checks:

- Quantocracy — practitioner aggregator
- Alpha Architect — practitioner / factor research
- Robot Wealth — practitioner research and backtesting
- Quantpedia — strategy research lead source
- arXiv q-fin trading / statistical finance / portfolio management query

Feed results are leads only. They should not be added to the research library unless they pass the evidence, practicality, cost, and reproducibility filters.

## Maintenance

Add feeds only if they are likely to surface systematic, reproducible, testable research. Avoid feeds dominated by guru-style signals, unsupported win-rate claims, or discretionary chart commentary.
