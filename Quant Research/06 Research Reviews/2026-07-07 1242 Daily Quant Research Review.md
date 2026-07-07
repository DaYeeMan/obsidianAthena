---
type: daily-quant-research-review
date: 2026-07-07 1242
created: 2026-07-07
tags: [quant-research, daily-review, arxiv, backtest-governance, volatility, market-impact]
---

# 2026-07-07 1242 Daily Quant Research Review

## Run Context

- Primary feed state: `blogwatcher-cli` with persistent DB `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Feed scan status: 5/7 feeds succeeded; Quantocracy returned HTTP 302 and Quantpedia timed out. No fallback RSS scanner was used.
- Inputs were treated as discovery leads only. The saved items below were validated with the arXiv `id_list` API before writing notes.
- Scope focus: equities, options/risk, crypto/microstructure, backtest validation, and cross-paper framework synthesis.

## High-Signal Items Saved

### 1. [[Look-Ahead-Freedom as Temporal Non-Interference]]

- Source: Xavier Fonseca, arXiv:2607.04958v1, 2026-07-06.
- Classification: **Evidence-backed as verification methodology at abstract level**.
- Practicality: **foundational**.
- Why kept: This is directly useful to the local backtest/research-agent stack. It formalizes look-ahead freedom as temporal non-interference and separates data availability time from reference time.
- Local implication: add `available_at`, `reference_time`, and `decision_time` assertions to the standard backtest audit block, plus planted-leak negative controls where possible.
- Decay / failure modes: a checker verifies only modeled pipeline steps; value-dependent availability remains undecidable/hard; cached files, manual steps, and agent summaries can still leak.

### 2. [[Forecasting Realized Volatility with Time Series Foundation Models]]

- Source: Alessio Brini, arXiv:2607.05291v1, 2026-07-06.
- Classification: **Evidence-backed at abstract level as model-evaluation evidence**.
- Practicality: **foundational / retail-adaptable**.
- Why kept: Useful for options-risk-premia sizing, volatility targeting, and ETF/futures risk forecasting. The paper is especially valuable because it benchmarks TSFMs against Log-HAR/econometric models rather than weak baselines.
- Key result from abstract: foundation models do not deliver uniform gains; only Tiny Time Mixers narrowly beats Log-HAR across horizons after asset-normalized comparison, and recalibration explains much of the short-horizon advantage.
- Local implication: do not use a TSFM volatility forecast in SPX/SPXW put-writing or allocation tests until EWMA/GARCH/Log-HAR, recalibration, per-asset loss ratios, and downstream cost-aware utility are implemented.

### 3. [[Order Splitting and Liquidity Replenishment for Square-Root Market Impact]]

- Source: Yang Zhou, Jianwen Chen, Ruipeng Wei, arXiv:2607.04280v1, 2026-07-05.
- Classification: **Plausible-to-evidence-backed as execution-cost methodology at abstract level**.
- Practicality: **foundational**.
- Why kept: strengthens the cost/capacity layer by making square-root impact mechanism-sensitive: the abstract identifies order splitting and liquidity replenishment as jointly necessary in the model.
- Local implication: square-root impact should be a stress scenario, not a fixed truth. Cost stress should vary by participation, volatility, spread/liquidity, execution horizon, and likely replenishment state.
- Decay / failure modes: simulation and calibration may not transfer to all venues; retail daily data cannot observe replenishment directly.

## Screened but Not Promoted

### Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles in Learning-Agent Markets

- Source: arXiv:2607.05141v1.
- Classification: **Speculative / foundational watch only**.
- Reason: interesting agent-based market-dynamics result, but the abstract's single optimized institutional agent plus herding retail simulation is not yet a retail-testable strategy or robust validation artifact. It reinforces market-impact/manipulation-risk concerns but was not added as a separate source note.

### Outcome-Classified Precision Auditing of Filter Rules in Algorithmic DEX Trading

- Source: arXiv:2607.02830v1.
- Classification: **Plausible but untested / retail-adaptable watch**.
- Reason: useful crypto filter-audit pattern with data/code claims, but the 13-day Solana DEX window is narrow and platform-specific. The conservative save-to-miss result is worth remembering for future crypto DEX research, but not enough today to create a standing candidate.

### Coordinated Sniper Cohorts on Pump.fun

- Source: arXiv:2607.02795v1.
- Classification: **Evidence-backed as cautionary causal-inference warning at abstract level / watch**.
- Reason: the paper itself refutes a strong cohort-specific causal interpretation after activity-matched placebo comparison. Useful warning against naive first-hour buyer-flow causality, but not a trading candidate without launch-quality covariates and fee/liquidity modeling.

### Causal Separation, Conditional Risk, and Projected Markowitz Portfolios

- Source: arXiv:2607.05320v1.
- Classification: **Plausible but untested / foundational watch**.
- Reason: potentially useful portfolio-covariance theory, but today it overlaps existing decision-aware covariance and conditional-risk questions. Deferred until the weekly synthesis layer can compare it against [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]].

### A Spectral Generalisation of the Variance Ratio

- Source: arXiv:2607.03858v1.
- Classification: **Plausible but untested / foundational watch**.
- Reason: interesting long-horizon covariance/memory decomposition, but less immediately actionable than the saved leakage, volatility, and impact items. Could be revisited for regime-conditional portfolio risk synthesis.

## Literature Connections / Framework Leads

### Reinforces

- [[Look-Ahead-Freedom as Temporal Non-Interference]] reinforces [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]] and [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]] by turning TimeGate/point-in-time discipline into a formal pipeline property.
- [[Forecasting Realized Volatility with Time Series Foundation Models]] reinforces [[Risk-Sensitive Specialist Routing for Volatility Forecasting]] but adds a stricter baseline requirement: specialist pools must include Log-HAR/econometric models and recalibration.
- [[Order Splitting and Liquidity Replenishment for Square-Root Market Impact]] reinforces [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]], [[Liquidity-Based Audit of Algorithmic Trading Strategies]], and [[Signature-Based Optimal Execution for Statistical Arbitrage]].

### Contradicts / Weakens

- Broad “foundation models replace econometric volatility models” claims are weakened; gains appear architecture-, asset-, horizon-, and calibration-dependent.
- Naive crypto first-hour buyer-flow causal interpretations are weakened by the Pump.fun cohort paper's placebo result.

### Framework Potential

- Cost-aware decision-process diagnostics: upgraded with formal look-ahead-freedom / temporal non-interference.
- Distributional-forecast-first ML strategy evaluation: upgraded with TSFM-vs-Log-HAR realized-volatility benchmark evidence.
- Microstructure-conditioned decay and liquidity-state validation: upgraded with replenishment-sensitive square-root impact mechanisms.

## Registry / Queue Updates

- Candidate registry updated:
  - added formal look-ahead-freedom checks,
  - added TSFM versus econometric realized-volatility forecasting,
  - updated the square-root market-impact row to link the new replenishment/order-splitting note.
- Framework registry updated:
  - added new source links to Cost-aware decision-process diagnostics,
  - Distributional-forecast-first ML strategy evaluation,
  - and Microstructure-conditioned decay and liquidity-state validation.
- Open research questions updated with two new questions on formal leakage checks and TSFM volatility utility.
- Coding-ready queue reviewed but unchanged: the new items improve the standard audit block and volatility-risk module design, but do not yet define a standalone coding-ready strategy.

## Hygiene Check Notes

- New source-note titles were created under `01 Sources/` and added to `01 Sources/Source Index.md`.
- Wikilinks in this review intentionally point only to existing or newly created notes.
- No root-level notes were intentionally created.
