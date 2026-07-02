---
type: daily-collection-protocol
tags: [quant-research, phase-2, cron]
---

# Daily Collection Protocol

The daily research collector runs as a triage process, not a content dump.

## Daily Steps

1. Search for credible new or newly relevant research across equities, options, and crypto.
2. Prefer academic, empirical, reproducible, or transparent practitioner work.
3. Extract only candidates that can become:
   - a testable strategy hypothesis,
   - a better backtest/risk/modeling method,
   - a foundational reference,
   - or a decay/outdatedness warning.
4. Classify evidence quality:
   - Evidence-backed
   - Plausible but untested
   - Speculative
   - Low quality
   - Rejected
5. Classify implementation practicality:
   - retail-practical
   - retail-adaptable
   - institutional-only
   - foundational
   - outdated-watch
6. Check for decay/outdatedness:
   - post-publication alpha decay
   - crowding/arbitrage
   - market-structure change
   - unrealistic costs/slippage/borrow/option spreads
   - inaccessible data/execution
   - unnecessary model complexity versus simple baselines
7. Write a distinct timestamped review note under `06 Research Reviews` for each collector run.
8. Create/update source or strategy notes only when the candidate is worth preserving.
9. Use Obsidian wikilinks only for notes that already exist or are created in the same run. If an item is only a concept, framework label, or watch-only method lead, use plain text instead of `[[wikilinks]]` unless you intentionally create the corresponding note in the correct Quant Research folder.
10. Update [[Quant Research/01 Research Candidate Registry|Research Candidate Registry]] for any candidate that is worth tracking, reclassified, rejected as a recurring bad idea, or newly flagged as outdated.
11. Before finalizing, run link/file hygiene checks: verify each new wikilink target exists or is intentionally unresolved, verify newly created source-note titles match links exactly, and check for zero-byte markdown files at the vault root caused by unresolved-link creation.
12. Send Discord summary only for high-signal items or to confirm the review was saved.

## Daily Note Naming

`YYYY-MM-DD HHMM Daily Quant Research Review.md`

Example: `2026-06-30 1435 Daily Quant Research Review.md`

Each collector run should create a distinct review note. Multiple same-day runs must not overwrite or merge into the first daily review unless the user explicitly asks for consolidation. If a timestamp collision occurs, append `-2`, `-3`, etc.

## Minimum Useful Daily Output

A useful daily review can be short. Quality beats volume. It should include:

- 3–5 screened candidates or fewer if quality is low
- explicit rejections when relevant
- at least one practical implication, research lead, or backtest idea when available
- links/citations for sources

## Coding-Time Support Requirement

This library is not only for market events. It should also help when the user is actively coding a strategy and asks for:

- relevant literature
- validation pitfalls
- feature ideas
- baseline models
- backtest design
- cost/slippage assumptions
- robustness checks
- ways to simplify institutional research into retail-testable proxies
