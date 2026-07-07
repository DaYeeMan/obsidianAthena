---
type: source-note
source_kind: paper
asset_classes: [equities, futures, fx, volatility, options, risk-management]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-07"
tags: [quant-source, volatility-forecasting, foundation-models, har, econometric-baselines, model-comparison]
concepts: [realized-volatility, time-series-foundation-models, log-har, mincer-zarnowitz, model-confidence-set]
---

# Forecasting Realized Volatility with Time Series Foundation Models

## Citation / Link

Alessio Brini, “Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks,” arXiv:2607.05291v1, 2026-07-06. https://arxiv.org/abs/2607.05291v1

## Summary

The paper compares nine zero-shot time-series foundation models against eight econometric realized-volatility benchmarks, including HAR-family models, on the VOLARE dataset across 50 assets in equities, FX, and futures and three forecast horizons. The abstract reports no uniform foundation-model advantage. Pooled losses can favor foundation models, but the gain is concentrated in outlier assets. When each asset's loss ratio is averaged against a well-specified Log-HAR benchmark, only Tiny Time Mixers beats the benchmark at every horizon, and only narrowly. Mincer-Zarnowitz recalibration suggests much of the short-horizon advantage comes from level/scale calibration rather than superior volatility-dynamics information.

## Core Contribution

- Provides a benchmark-first comparison for realized-volatility forecasting rather than assuming foundation models dominate classical econometrics.
- Shows that pooled average gains can be driven by a few assets; asset-normalized evaluation materially changes the conclusion.
- Separates scale/calibration improvement from genuine informational gain via recalibration.
- Finds that a simple equal-weight average of Tiny Time Mixers and Log-HAR is often more robust than choosing one best model in advance.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as model-evaluation evidence / foundational-retail-adaptable**.
- Not an alpha signal by itself; useful for risk forecasts, volatility targeting, options-risk-premia sizing, and drawdown control.
- Strong practical warning: do not add foundation models to volatility-risk systems until Log-HAR, EWMA/GARCH-style, and simple ensemble baselines are implemented and evaluated per asset.
- Retail adaptation is plausible with daily/intraday realized-volatility data; model complexity must be justified by downstream utility, not only forecast loss.

## Methods and Data

Abstract-level details:

- VOLARE dataset,
- 50 assets across equities, FX, and futures,
- three forecast horizons,
- nine zero-shot time-series foundation models,
- eight econometric benchmarks including HAR-family models,
- pairwise and multi-model forecast-comparison tests,
- Mincer-Zarnowitz recalibration,
- Model Confidence Set analysis.

## Leakage / Bias / Overfitting Concerns

- Zero-shot models may still embed training data overlap or market-regime priors; time coverage should be checked before production use.
- Pooled loss metrics can hide concentration in a small number of assets.
- Forecast-loss improvement may not improve a trading decision after turnover, option spreads, volatility-target rebalance costs, or crash convexity.
- Recalibrated forecasts may be more useful than complex raw models.

## Local Use / Backtest Translation

Minimum viable volatility-forecast test:

1. Start with rolling realized volatility, EWMA, GARCH if available, and Log-HAR.
2. Add TTM or another TSFM only after baseline metrics are stable.
3. Evaluate loss ratios per asset and horizon, not only pooled average loss.
4. Include Mincer-Zarnowitz recalibration for every model.
5. Test downstream use in volatility targeting or SPX/SPXW put-writing sizing with bid/ask, turnover, and drawdown metrics.

## Connections to Existing Research

### Reinforces

- [[Risk-Sensitive Specialist Routing for Volatility Forecasting]]: state-dependent routing may be useful, but the candidate specialist pool must include strong classical models.
- [[Forecast-uncertainty-aware ML asset pricing]]: calibration and uncertainty matter more than raw architecture novelty.
- [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]]: model comparison must be benchmark-first and cost-aware.

### Contradicts / Weakens

- Weakens broad claims that generic time-series foundation models can replace econometric volatility models without asset-by-asset validation.

### Framework Potential

- Candidate framework: Distributional-forecast-first ML strategy evaluation.
- Testable composite hypothesis: a simple Log-HAR + small-TSFM ensemble improves risk-control utility more robustly than any single architecture in options and ETF allocation backtests.
- Minimum viable backtest: compare EWMA/Log-HAR/TTM/ensemble forecasts for SPY or liquid futures realized volatility, then feed them into fixed-risk versus volatility-targeted allocation rules.
- Falsification: TSFM/ensemble forecast gains disappear after recalibration, costs, and downstream utility evaluation.
