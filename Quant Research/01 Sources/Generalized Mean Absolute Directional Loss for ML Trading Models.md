---
type: source-note
source_kind: paper / trading-objective ML loss-function proposal
asset_classes: [equities, crypto, futures, ML, strategy-evaluation]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: "2026-08-06"
tags: [quant-source, machine-learning, directional-loss, trading-objective, model-selection]
concepts: [GMADL, decision-aligned-loss, directional-forecasting, return-magnitude-weighting]
---

# Generalized Mean Absolute Directional Loss for ML Trading Models

## Citation / Link

Jakub Michańków, Paweł Sakowski, Robert Ślepaczuk, “Generalized Mean Absolute Directional Loss for Machine Learning Trading Models,” arXiv:2412.18405v2, originally submitted 2024-12-24; v2 comment says updated results. https://arxiv.org/abs/2412.18405v2

Semantic Scholar lookup returned HTTP 429 during the 2026-08-06 run, so citation counts were not recorded.

## Summary

The paper proposes Generalized Mean Absolute Directional Loss (GMADL), a custom loss for machine-learning trading models. The abstract claims GMADL has better numerical properties and produces superior risk-weighted returns than classic regression/classification losses across asset classes and model complexities by aligning optimization with buy/sell signal performance and return magnitude sensitivity.

For this library, the paper is useful but should be treated conservatively. A trading-aligned objective is directionally sensible, but broad “superior regardless of asset/model complexity” claims are high overfit risk unless tested against simple baselines, fixed costs, and held-out assets/regimes.

## Core Contribution

- Proposes a differentiable / optimizable loss that combines directional correctness and return-magnitude sensitivity.
- Shifts model training away from generic MSE/cross-entropy or raw directional accuracy toward trading-relevant objectives.
- Connects loss-function choice to risk-weighted strategy performance rather than prediction-score-only evaluation.

## Practical Relevance

- Classification: **Plausible but untested at abstract level; foundational / retail-adaptable**.
- Retail adaptation is feasible in local ML experiments if GMADL is treated as one candidate objective inside a benchmark suite.
- Do not accept broad performance claims without independent time-gated replication.

## Methods and Data

The abstract indicates robust ML tools and hyperparameter tuning, but does not by itself provide enough detail to treat the result as evidence of portable alpha. The source should be read in full before implementation.

## Leakage / Bias / Overfitting Concerns

- Custom losses can overfit the backtest objective, especially when repeatedly tuned.
- Return-magnitude weighting can chase tails, increase turnover, or load on unstable regimes.
- Asset-class-wide superiority claims need held-out assets, chronological folds, and simple baselines.
- Directional loss still needs base-rate/always-up comparisons in rising markets.

## Transaction Cost / Capacity Treatment

Any GMADL replication must include costs, slippage/spreads, turnover penalties, borrow/funding where applicable, and capacity constraints. A loss that improves gross direction/magnitude scores may worsen net utility through churn.

## Strategy Ideas Extracted

- Hypothesis: decision-aligned directional/magnitude losses improve net trading utility versus MSE, cross-entropy, Sharpe-like differentiable objectives, and simple directional baselines when costs and turnover are included.
- Minimum viable validation: use frozen chronological splits across multiple assets; compare GMADL-trained models against MSE/classification/Huber/quantile losses, always-up/base-rate, momentum/reversal simple rules, and no-trade; report net PnL, turnover, drawdown, calibration, and regime splits.
- Practical use: candidate objective in ML benchmark suite, not a standalone strategy.

## Connections to Existing Research

### Reinforces

- [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]: directional metrics must be base-rate honest.
- [[Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization]]: decision-aware objectives can inflate rankings and turnover if unconstrained.
- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]: evaluation should be cost-aware and strategy-consistent.

### Contradicts / Weakens

Weakens generic prediction-loss-first ML workflows, but also warns against replacing one proxy metric with another without net-utility validation.

### Transfers Across Asset Classes or Domains

Potentially transfers to equities, crypto, futures, and FX, but only as a model-selection objective under asset-specific frictions.

### Missing Validation or Method Supplied

Supplies a loss-function candidate for the decision-aligned ML evaluation framework.

## Framework Potential

- Candidate framework: Distributional-forecast-first ML strategy evaluation and Simple-rule benchmark-first AI portfolio-policy evaluation.
- Linked notes: [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]], [[Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization]], [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]].
- Testable composite hypothesis: trading-objective losses are useful only when they beat base-rate/simple-rule baselines net of costs and do not increase turnover fragility.
- Minimum viable validation: frozen multi-asset chronological benchmark with cost/turnover stress and held-out regimes.
- What would falsify this connection? GMADL gains disappear after costs, turnover controls, base-rate baselines, or held-out assets.

## Keep / Reject Decision

**Keep as method lead; conservative classification.** Useful for ML benchmark design, but not coding-ready as alpha.

## Related Notes

- [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]
- [[Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization]]
- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]
