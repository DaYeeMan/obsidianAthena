---
type: daily-quant-research-review
date: 2026-07-23
time: "0803"
source_status: normal_with_feed_warnings
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review, arxiv, validation, model-decay]
---

# 2026-07-23 0803 Daily Quant Research Review

## Run Status

- Primary persistent feed collector: blogwatcher-cli via `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Feed scan status: usable but imperfect. Alpha Architect, Robot Wealth, and arXiv feeds scanned; Quantocracy returned HTTP 302 and Quantpedia timed out. I did not use the stdlib fallback RSS scanner.
- Evidence standard: feed/query entries were treated as discovery leads only. High-signal arXiv leads were validated through the arXiv API `id_list` metadata before saving notes.
- Coding queue reviewed: unchanged. Today’s items improve validation/framework discipline but do not yet provide complete falsifiable strategy rules, data source, costs, baselines, and go/no-go design for immediate queue promotion.

## Validated High-Signal Items Saved

### 1. [[The Science and Practice of Trend-Following Systems]]

- Source: Artur Sepp and Vladimir Lucic, arXiv:2607.19497v1, 2026-07-21.
- Classification: **Evidence-backed at abstract level as trend-following methodology; foundational / retail-adaptable**.
- Practical implication: use volatility-normalized autocorrelation/spectral diagnostics and cost-optimal lookback/span before coding trend variants. This is especially useful for separating slower trend persistence from microstructure-fragile short-speed trend.
- Decay/cost warning: trend is crowded; short lookbacks are vulnerable to turnover, roll/funding, spread, market-impact, and market-structure decay.

### 2. [[Retail Traders Ruin - Anatomy of Popular Signal Failure]]

- Source: Adam Darmanin, arXiv:2607.20093v1, 2026-07-22; initial non-peer-reviewed draft.
- Classification: **Evidence-backed at abstract level as validation design; specific empirical claims Plausible but untested**.
- Practical implication: preserve as a recurring rejection filter for candlestick, oscillator, volume, calendar, and overfit trend claims. A popular retail rule should pass statistical edge, net economic materiality, and leverage/survival gates before being entertained.
- Decay/cost warning: without point-in-time membership, delisting corrections, multiplicity control, exposure-matched benchmarks, and costs, retail-rule “edge” is likely false deployability.

### 3. [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]]

- Source: Ayoub Jadouli, arXiv:2607.19453v1, 2026-07-21; simulation-only negative empirical study with available code/artifacts.
- Classification: **Evidence-backed at abstract level as negative code-supported audit; foundational / retail-adaptable**.
- Practical implication: high AUC or extrema ranking is not enough; require purged splits, no same-close entries, average precision, net policy return, raw artifact retention, and no-trade/buy-hold/simple-rule baselines before any crypto OHLCV ML strategy is promoted.
- Decay/cost warning: price-only crypto candle models are especially exposed to fee drag, venue-specific structure, short samples, leakage, and post-publication adaptation.

### 4. [[Quantum Kernels and the Cross-Section of Stock Returns - Vanishing Advantage]]

- Source: Junchi Shen, arXiv:2607.20168v1, 2026-07-22.
- Classification: **Evidence-backed at abstract level as negative model-comparison evidence; foundational / outdated-watch**.
- Practical implication: any exotic/quantum/representation-learning alpha claim should first pass kernel-swap controls, equal tuning budgets, point-in-time universes, linear/classical baselines, multiplicity correction, and net portfolio utility.
- Decay/cost warning: apparent model novelty can be manufactured by full-sample screening, unequal budgets, and missing simple baselines.

## Screened but Not Saved as Source Notes

- `focus and focus-cpt: Fast Online Changepoint Detection in R and Python` was validated as a useful software-adjacent companion to [[ARp-Focus Online Changepoint Detection under Autocorrelation]], but I did not create a new source note because it primarily supplies implementation packaging rather than a new finance-specific mechanism. It should be considered when coding online drift/kill-switch modules.
- `Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients` was outside the library’s current equities/options/crypto strategy and validation priorities.
- Several adjacent-domain leads were screened as method leads only; none supplied a stronger direct connection than the four saved notes.

## Literature Connections / Framework Leads

### Reinforces

- Cost-aware decision-process diagnostics: today’s retail-signal and Binance timing audits add concrete negative-result gates for statistical evidence, economic materiality, survival, policy value, and artifact retention.
- Microstructure-conditioned decay and liquidity-state validation: the trend-following paper complements existing trend-decay notes by offering a theoretical decomposition of persistence, drift, costs, and skew rather than another raw Sharpe result.
- Simple-rule benchmark-first AI portfolio-policy evaluation: the quantum-kernel paper strengthens the “model novelty is not alpha” rule with equal-budget classical controls and point-in-time universe requirements.

### Contradicts / Weakens

- Weakens retail chart-rule folklore, candle-based crypto ML timing, and quantum/exotic model advantage claims that do not show leakage-clean, cost-aware, simple-baseline-beating results.
- Does not reject trend-following wholesale; the strongest validated distinction is between properly costed slower trend persistence and fragile short-speed or overfit trend rules.

### Transfers Across Asset Classes

- The three-gate retail-signal falsification pattern can be reused for equities, ETFs, crypto spot/perps, and futures rule libraries.
- The predictive-score-to-policy-value audit applies to crypto ML, equity directional ML, LLM/agent forecasts, and option-risk throttles whenever forecast metrics are separated from executable decisions.

### Missing Link Supplied

- Today’s new missing link is a reusable “negative evidence is useful evidence” layer: refuted or no-trade results should be preserved when they improve future screening and prevent repeated overfit strategy coding.

## Registry / Queue Changes

- Candidate registry updated with four rows:
  - Trend-following decomposition and cost-optimal span audit.
  - Retail-signal falsification gates for popular rule families.
  - Crypto candle-based ML timing no-trade gate.
  - Quantum/exotic model advantage falsification for asset pricing.
- Source index updated with all four new source notes.
- Framework registry not patched today; the new items reinforce existing frameworks rather than requiring a new framework row.
- Open questions unchanged; existing questions already cover base-rate/simple-rule benchmarks, crypto OHLCV/ML policy value, trend speed/cost survival, and model-complexity falsification.
- Coding-ready queue unchanged because no item supplied a fully specified immediate strategy implementation.

## Hygiene Notes

- New wikilinks were limited to source notes that already existed or were created in this run.
- No root-level vault notes were intentionally created.
- Post-write checks verified the four new source-note titles in the source index, registry, and this review note; a wikilink check across the five new/updated run artifacts reported `wikilinks_missing 0`, and the vault root zero-byte markdown check returned no files.
