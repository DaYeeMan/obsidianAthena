---
type: daily-quant-research-review
date: 2026-07-18 0802
source_status: partial-rss-success
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review]
---

# 2026-07-18 0802 Daily Quant Research Review

## Run Status

- Pre-run collector used persistent blogwatcher-cli state from `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Blogwatcher scan completed with partial RSS failures: Alpha Architect, Robot Wealth, and arXiv feeds succeeded; Quantocracy returned HTTP 302 and Quantpedia returned HTTP 429. Practitioner/RSS coverage is therefore partial, but not degraded enough to block academic triage.
- Feed entries and query leads were treated as discovery input only. Kept items below were validated against directly inspectable Alpha Architect article text and/or arXiv API metadata.

## Screened Leads

| Lead | Source | Decision | Evidence Quality | Practicality | Reason |
|---|---|---|---|---|---|
| [[Two Accounting Anomalies - Accruals May Be Risk, PEAD May Be Mispricing]] | Alpha Architect summary of Penman & Zhu June 2026 paper | Keep source note + registry row | Evidence-backed as practitioner-reviewed paper summary | retail-adaptable / foundational | Strong anomaly-triage implication: accruals may be risk compensation under an intertemporal accounting hedge factor, while PEAD remains more consistent with delayed-information mispricing. Useful for deciding what accounting anomalies deserve coding time. |
| Existence and convergence of discrete-time Kyle models with multiple insiders | arXiv:2607.15057v1 | Watch / do not save | Low quality for this library today | foundational theory only | arXiv API metadata showed a title about discrete-time Kyle models but an abstract about extending Basak and Cuoco limited participation with heterogeneous time preferences. Because the metadata/title-abstract mismatch makes the lead ambiguous and it has no direct retail backtest path, it was not promoted. |
| Subjective Risk Decomposition: A New View for Uncertainty Quantification | arXiv:2607.15196v1 | Mention only | Plausible adjacent-domain method | foundational | Useful conceptually for choosing uncertainty measures from a strictly proper loss, but no finance-specific validation or immediate strategy/backtest implication. Could inform future forecast-uncertainty evaluation but not worth a source note today. |
| Augmenting goodness-of-fit tests with sequentially calibrated secondary statistics | arXiv:2607.15015v1 | Mention only | Plausible adjacent-domain method | foundational / retail-adaptable | Potentially useful for model-monitoring chains that preserve Type I error while decomposing power by first rejection. Connects to drift/power monitoring, but not yet finance-specific evidence. |
| Decoding Market Emotion from Blockchain Activity | arXiv:2607.15258v1 | Watch / no save | Speculative for trading | foundational only | Bitcoin sentiment classifier reports F1 around 0.84 for classifying sentiment from on-chain/price/social data; it is explicitly not price prediction and does not establish net trading utility. Keep below crypto microstructure/data-quality leads. |

## High-Signal Item: Accounting-Anomaly Reclassification

### Hypothesis

Old accounting anomalies should be split into at least two buckets before coding:

1. **risk-reclassified anomalies** whose spreads are compensation for multiperiod future-earnings risk or omitted benchmark exposure; and
2. **delayed-information anomalies** that remain more plausibly mispricing after suitable benchmark, liquidity, and post-publication tests.

The Alpha Architect/Penman-Zhu lead suggests accruals may fall more into bucket 1, while PEAD may remain closer to bucket 2.

### Economic Rationale

Accounting information is forward-looking. Accruals link current earnings to future earnings/cash-flow risk, so a one-period factor model can misclassify priced intertemporal risk as abnormal return. PEAD is event-driven and more naturally tied to slow information diffusion, investor underreaction, analyst/revision frictions, and earnings-announcement processing delays.

### Asset Class / Universe

- U.S. equities.
- Retail-adaptable universe: liquid common stocks or larger-cap U.S. equities with survivorship-free price/accounting data.
- Avoid microcap-heavy long-short construction unless costs, delistings, and borrow are explicitly modeled.

### Signal Definition for Future Backtest

- **Accrual leg:** portfolio sorts on accrual measure from point-in-time accounting statements; exact construction deferred until original paper is inspected.
- **PEAD leg:** sort by standardized unexpected earnings or earnings surprise after announcement-time availability; test 1/5/20/60-trading-day holding windows.
- **Benchmark block:** standard factors, sector/industry controls, cap/liquidity buckets, post-publication split, and an accounting/fundamental hedge-factor proxy if the original Penman-Zhu construction can be reproduced.

### Data Requirements

- CRSP/Compustat-like survivorship-free equity returns/accounting data, delisting returns, shares/market cap, and liquidity/spread proxies.
- Earnings announcement timestamps, filing/publication availability timestamps, and analyst/revision data if testing revenue surprises or forecast revisions.
- Transaction-cost estimates by liquidity/cap bucket and borrow/shortability assumptions for long-short variants.

### Backtest Design

1. Replicate accrual and PEAD portfolios separately.
2. Separate pre- and post-publication windows; also run modern-only windows.
3. Use point-in-time joins with explicit `available_at`, `reference_time`, and `decision_time` fields.
4. Compare raw long-short returns, factor-adjusted alphas, accounting-hedge-factor adjusted alphas, cap-axis residual diagnostics, and net-of-cost results.
5. Include simple baselines: momentum, earnings-surprise buy-and-hold, size/value/quality sorts, and equal-risk exposure constraints.

### Transaction-Cost Concerns

- Accrual sorts may be annual/lower turnover but can concentrate in small/illiquid/short-constrained stocks.
- PEAD is event-driven and may require quick post-announcement entry; slippage around announcements and borrow availability can dominate.
- Short legs require borrow feasibility, recall risk, and hard-to-borrow cost stress.

### Risks / Failure Modes

- Original paper details not yet inspected; source note is based on validated practitioner article text, not a full paper replication.
- Accrual/PEAD construction can leak if accounting or announcement availability timestamps are mishandled.
- Post-publication decay and crowding are high because both anomalies are old and widely known.
- Factor/benchmark expansion can become p-hacking if used to explain away any inconvenient alpha; predefine benchmark blocks.

### Validation Priority

Medium. PEAD-first replication is more promising than accrual-first alpha hunting, but neither is coding-ready until the exact paper rules and data source are specified.

## Literature Connections / Framework Leads

### Reinforces

- [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]]: anomaly backtests need survivorship-free data, post-publication splits, implementation review, and error traps.
- [[A Cap-Axis Integral Diagnostic of Factor Models]]: omitted dimensions such as cap/liquidity/benchmark risk can explain apparent residual alpha.

### Contradicts / Weakens

- Weakens naive accrual-mispricing interpretations if the accounting hedge factor explains the spread.
- Does not reject PEAD; it upgrades PEAD as the accounting anomaly more worth a careful event-study replication.

### Transfers Across Asset Classes

The benchmark-first anomaly reclassification lens transfers to crypto and options: a published return pattern should be tested against mechanism-relevant risk/cost state before being treated as alpha.

### Framework Potential

Potential framework lead: benchmark-first anomaly reclassification and decay audit. It has enough linked sources for the open question list, but I did not add a new framework row yet because the original Penman-Zhu paper details and hedge-factor construction need full inspection first.

## Registry / Queue Actions

- Candidate registry: updated with a new accounting-anomaly reclassification row.
- Source index: updated with the new source note.
- Open questions: updated with a question on accrual/PEAD risk-vs-mispricing separation under post-publication and cost controls.
- Framework registry: not changed; framework lead is watch-only until full paper inspection.
- Coding-ready queue: reviewed but unchanged. The PEAD/accrual item is not coding-ready because exact original-paper rules, data availability, costs, and go/no-go thresholds are not yet pinned down.

## Rejections / Downgrades

- Discrete-time Kyle model lead: not saved due to arXiv title/abstract mismatch and no immediate implementable retail link.
- Bitcoin sentiment classifier lead: not saved because classification of sentiment is not trading evidence and there is no cost-aware return-prediction or portfolio-utility result.
- Quantum basket option pricing lead and NeuralChaos lead from arXiv query output were screened as lower priority for this library today: mathematically interesting, but institutional/specialized and not connected to a near-term retail strategy or validation framework better than existing notes.

## Hygiene Notes

- New source-note title created and used consistently: [[Two Accounting Anomalies - Accruals May Be Risk, PEAD May Be Mispricing]].
- No intentional unresolved wikilinks were introduced beyond existing library links.
