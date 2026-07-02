---
type: source-note
source_kind: paper
asset_classes: [equities, strategy-evaluation, risk]
implementation_class: foundational
importance: high
last_reviewed: "2026-07-01"
tags: [quant-source, strategy-evaluation, regimes, distributional-methods, gamlss]
concepts: [regime-conditional-performance, distributional-comparison, walk-forward-validation, adjusted-information-ratio]
---

# Regime-Conditional Distributional Comparison of Trading Strategies

## Citation / Link

Krzysztof Ozimek, “Regime-Conditional Distributional Comparison of Trading Strategies: A GAMLSS/ZAGA Framework Applied to the S&P 500,” arXiv:2606.31251v1, 2026-06-30. https://arxiv.org/abs/2606.31251v1

## Summary

The paper argues that strategy comparison should not collapse performance into a single full-period metric. It models walk-forward out-of-sample fold performance as a conditional distribution whose location, scale, and shape vary with market-regime covariates. The application compares a polynomial SVM strategy against buy-and-hold on the S&P 500 from 2002–2025 using 146 out-of-sample folds and an adjusted information ratio metric.

## Core Contribution

- Treats strategy performance as regime-conditional and distributional rather than one scalar Sharpe/IR.
- Uses GAMLSS with a zero-adjusted gamma response to model fold-level adjusted information-ratio outcomes.
- Tests expected performance, variance, and risk-adjusted dominance at representative volatility/momentum regimes.
- Provides a validation lens that can be reused even if the specific SVM strategy is not compelling.

## Practical Relevance

- Classification: **Evidence-backed as a strategy-evaluation methodology / foundational-retail-adaptable**.
- Not a direct alpha source; the useful object is the comparison framework.
- Retail adaptation: any local backtest can store rolling/walk-forward fold metrics, condition them on simple regimes such as realized volatility, trend, VIX, liquidity, or funding, and test whether apparent edge exists only in fragile states.

## Methods and Data

Abstract-level details:

- S&P 500, 2002–2025,
- 146 out-of-sample walk-forward folds,
- polynomial SVM strategy versus buy-and-hold,
- adjusted information ratio per fold,
- realized volatility and cumulative momentum as regime covariates,
- GAMLSS/ZAGA distributional modeling and parametric bootstrap hypothesis tests.

Local minimum viable adaptation:

1. Preserve fold-level metrics from any backtest rather than only aggregate summary metrics.
2. Define ex ante regime covariates available at the start of each fold.
3. Compare strategy and baseline conditional distributions across regimes.
4. Reject strategies whose edge appears only in statistically weak or cost-unrealistic regimes.

## Leakage / Bias / Overfitting Concerns

- Regime covariates must be computed only from information available at the decision time.
- Flexible distributional models can overfit fold-level observations if too many regime features are included.
- A complex SVM example should not be interpreted as evidence that SVM trading is robust; compare against simple trend, volatility scaling, and buy-and-hold baselines.
- Multiple regime slices can invite data mining unless candidate regimes are pre-specified.

## Transaction Cost / Capacity Treatment

The abstract is about strategy comparison methodology, not detailed execution. Local use should condition net-of-cost fold metrics on regimes and explicitly stress spreads, slippage, turnover, financing, borrow, and option/crypto liquidity where applicable.

## Strategy Ideas Extracted

No direct strategy. Use as a validation layer for strategy families already in the library, especially short-volatility sizing, crypto momentum/funding models, ML forecasts, and portfolio-allocation rules.

## Keep / Reject Decision

**Keep** as a high-priority foundational validation method. It strengthens the library’s move from return-only comparisons toward regime-aware, distributional, cost-aware evaluation.

## Connections to Existing Research

### Reinforces

- [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]]: both prioritize distributions over point summaries.
- [[Continuous Hidden Markov Models for Equity Returns]]: supplies an evaluation counterpart to regime/risk modeling.
- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]] and [[Liquidity-Based Audit of Algorithmic Trading Strategies]]: complements process/cost diagnostics with regime-conditional performance diagnostics.

### Framework Potential

- Candidate framework: Regime-conditional distributional strategy evaluation.
- Minimum viable backtest: store out-of-sample fold metrics, condition them on volatility/trend/liquidity regimes, and compare strategy-vs-baseline distributions net of costs.
- Falsification: if regime-conditioned effects vanish under simple baselines, realistic costs, or post-publication splits, the strategy remains unpromoted.
