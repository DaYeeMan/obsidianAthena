---
type: daily-quant-research-review
date: 2026-07-15
created: 2026-07-15 0802 EDT
tags: [quant-research, daily-review, arxiv, ml-validation, intraday-futures, portfolio-optimization]
---

# 2026-07-15 0802 Daily Quant Research Review

## Run Inputs

- Primary feed state: blogwatcher-cli pre-run context from `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Feed scan status: 5 of 7 blogs succeeded; Quantocracy returned 302 and Quantpedia returned 429. No stdlib RSS fallback was used.
- New high-signal arXiv/feed leads validated directly through the arXiv API before saving.
- Existing context checked: candidate registry, source index, framework registry excerpts, open questions excerpt, and coding queue.

## Saved / Updated Source Notes

1. [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]
2. [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]]
3. [[Learning Predictive Ambiguity Sets for Decision-Focused DRO]]

## High-Signal Candidates

### 1. Base-rate-honest directional ML forecasting benchmark

- Source: [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]] — arXiv:2607.12248v1.
- Classification: **Evidence-backed at abstract level as negative-result / validation methodology**.
- Practicality: **foundational / retail-adaptable**.
- Why it matters: the authors report that a headline roughly 80% directional-accuracy result for LoRA-adapted TimesFM was a rising-market base-rate artifact. Always-up/base-rate comparisons, held-out-ticker splits, expanding walk-forward folds, paired tests, and FDR control are exactly the validation discipline needed before trusting equity or crypto directional ML.
- Decay / failure mode addressed: prevents false ML alpha from class imbalance, benchmark omission, universe leakage, and raw-hit-rate reporting.
- Next action: add always-up/base-rate, random-walk, persistence, AR(1), held-out-asset, paired-test, and net-utility baselines to any directional ML backtest.

### 2. Intraday OHLCV signal falsification and deployment gates

- Source: [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]] — arXiv:2605.04004v2.
- Classification: **Evidence-backed at abstract level as validation/falsification methodology**.
- Practicality: **retail-adaptable / foundational**.
- Why it matters: common five-minute MNQ OHLCV momentum signal families did not meet joint deployment gates once realistic friction, sample-size, walk-forward, and year-consistency criteria were applied; positive controls make it a useful falsification template rather than just a negative rant.
- Decay / failure mode addressed: downgrades generic intraday OHLCV pattern claims that live below fees/slippage or survive only through tuning.
- Next action: add a deployment-gate table to intraday futures/ETF/crypto notebooks: walk-forward OOS, minimum trades, cost stress, year consistency, positive controls, and negative-result logging.

### 3. Adaptive ambiguity-set DRO for portfolio decisions

- Source: [[Learning Predictive Ambiguity Sets for Decision-Focused DRO]] — arXiv:2607.09820v1.
- Classification: **Plausible but untested at abstract level**.
- Practicality: **foundational / retail-adaptable as methodology**.
- Why it matters: learned state-dependent Wasserstein radii and scenario distributions are a clean connection between forecast uncertainty and downstream portfolio decisions.
- Main caution: the headline result is only a 20-stock S&P 500 experiment from 2018–2026 at abstract level; it may be universe/regime/cost sensitive and should not be promoted before full-paper/code review.
- Next action: compare against equal weight, inverse-vol, Ledoit-Wolf GMVP, volatility targeting, fixed-radius DRO, partial adjustment, and simple state-dependent shrinkage before any deep LPAS implementation.

## Screened But Not Saved

- **EVOQUANT: Self-Evolving Verifier-Guided Strategy Optimization for Robust Quantitative Trading** — **Speculative / low-priority**. Interesting agentic-research automation lead, but abstract-level Sharpe improvements across seven strategies are not enough without detailed leakage controls, cost realism, benchmark transparency, and overfitting safeguards. Keep as watch-only; do not add to registry today.
- **Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring** — **foundational but outside immediate asset-focus**. Useful monitoring methodology for distributional shift, but less directly actionable than the ML/base-rate and intraday falsification items; not saved today.
- **Multidimensional stochastic liquidity in Kyle's model of informed trading** — high-quality theory lead but institutional/foundational and not immediately connected beyond existing liquidity-tail/impact framework; screened but not saved today.
- **A Noise-Aware Quantum Algorithm for Credit Valuation Adjustments on Real Quantum Hardware** — rejected for this library run as outside scope and not useful for equities/options/crypto strategy validation.

## Literature Connections / Framework Leads

### Reinforces

- [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]] reinforces [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]], [[Forecasting Realized Volatility with Time Series Foundation Models]], and [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]: model claims need simple baselines, time-gated data, and downstream net-utility tests.
- [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]] reinforces [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]], [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]], and [[Liquidity-Based Audit of Algorithmic Trading Strategies]].
- [[Learning Predictive Ambiguity Sets for Decision-Focused DRO]] reinforces [[Forecast-uncertainty-aware ML asset pricing]] and [[Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization]].

### Contradicts / Weakens

- Weakens any directional ML claim that reports raw accuracy without always-up/base-rate comparisons.
- Weakens generic intraday OHLCV pattern claims that lack cost gates, minimum trade counts, year splits, and positive/negative controls.
- Does not yet weaken fixed-radius DRO or standard portfolio baselines; the LPAS evidence needs fuller validation.

### Transfers Across Asset Classes

- Base-rate-honest directional scoring transfers from equity TimesFM evaluation to crypto return classifiers and options/equity event classifiers.
- Intraday deployment gates transfer from MNQ futures to crypto perpetuals and ETF intraday strategies, with funding/fee/spread adjustments.
- Adaptive ambiguity radii may transfer to volatility-risk-premium sizing or ML allocation, but only as a risk-control method after simple baselines.

### Framework Updates Made

- Updated `Framework Candidate Registry.md`:
  - Added the TimesFM base-rate paper and LPAS paper to Distributional-forecast-first ML strategy evaluation.
  - Added the MNQ OHLCV falsification paper to Cost-aware decision-process diagnostics.
  - Added TimesFM and LPAS to Simple-rule benchmark-first AI portfolio-policy evaluation.
- Updated `Open Research Questions.md` with a new question on whether directional ML/foundation-model forecasts beat base-rate/always-up benchmarks across held-out assets, regimes, and costs.

## Registry / Queue Updates

- Updated [[01 Research Candidate Registry]] with three new tracked candidates:
  1. Base-rate-honest directional ML forecasting benchmark.
  2. Intraday OHLCV signal falsification and deployment gates.
  3. Adaptive ambiguity-set DRO for portfolio decisions.
- Updated [[01 Sources/Source Index]] with the three new source notes.
- Coding queue reviewed but unchanged. None of today's items are coding-ready as standalone strategy specs; two are validation/audit modules and one is a method lead needing full-paper/code review.

## Validation Priority

1. Add base-rate-honest directional scoring to any ML return classifier before model expansion.
2. Add intraday deployment gates to short-horizon bar strategies before further tuning.
3. Treat LPAS as a medium-priority method lead only after simple uncertainty/sizing baselines exist.

## Hygiene Notes

- New wikilinks were limited to existing or newly created notes.
- New source titles were added to Source Index.
- No unresolved concept-only framework labels were wikilinked.
- Feed failures were recorded as source-collection warnings only; arXiv validation succeeded for saved items.
