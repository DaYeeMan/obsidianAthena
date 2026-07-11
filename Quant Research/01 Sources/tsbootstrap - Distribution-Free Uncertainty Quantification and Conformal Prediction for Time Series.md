---
type: source-note
source_kind: paper / software
asset_classes: [equities, crypto, portfolio, risk, ml]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-09"
tags: [quant-source, time-series-bootstrap, conformal-prediction, uncertainty-quantification, forecast-calibration, ml-validation]
concepts: [block-bootstrap, residual-bootstrap, sieve-bootstrap, wild-bootstrap, adaptive-conformal-prediction, dependent-data]
---

# tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series

## Citation / Link

Sankalp Gilda, “tsbootstrap: Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series,” arXiv:2607.06690v1, 2026-07-07. https://arxiv.org/abs/2607.06690v1

Code: https://github.com/astrogilda/tsbootstrap

## Summary

The paper/software note addresses a practical validation gap: financial and other time-series streams violate IID exchangeability, while many bootstrap and conformal workflows still assume IID observations. The abstract describes a typed API combining block, residual, sieve, and wild resampling; classical bootstrap confidence intervals; and adaptive conformal calibrators including EnbPI, ACI, NexCP, and AgACI. In a controlled coverage study, IID bootstrap undercovers sharply under dependence, while dependence-aware methods reduce the coverage deficit, with sieve bootstrap nearest nominal under short-memory linear dependence.

## Core Contribution

- Provides a unified software implementation for dependence-aware bootstrap and adaptive conformal prediction.
- Directly warns against IID bootstrap/conformal intervals for dependent financial time series.
- Offers practical calibration tools for forecast intervals, uncertainty bands, and validation diagnostics.
- Useful as a bridge between forecast-uncertainty ML asset-pricing work and implementation-grade validation.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as methodology / software; foundational / retail-adaptable**.
- Not a standalone trading signal.
- Strongly relevant to return/volatility forecast evaluation, uncertainty-aware sizing, regime/risk dashboards, and walk-forward strategy diagnostics.
- Retail adaptation is feasible: apply dependence-aware bootstrap or adaptive conformal intervals to daily ETF/equity/crypto forecasts and strategy fold metrics, then test whether intervals improve downstream sizing or go/no-go decisions versus simple volatility targeting and fixed thresholds.

## Methods and Data

Abstract-level details:

- block, residual, sieve, and wild bootstrap methods,
- classical bootstrap confidence intervals,
- adaptive conformal calibrators: EnbPI, ACI, NexCP, AgACI,
- controlled coverage study under dependent data,
- compiled backend and streaming reduce to reduce runtime/memory footprint.

## Strategy / Research Implication

Use this as a validation layer, not an alpha generator:

1. For ML return forecasts, compare point estimates with dependence-aware forecast intervals and conformal coverage.
2. For volatility/risk forecasts, measure interval coverage specifically in high-volatility states and after regime shifts.
3. For strategy backtests, bootstrap fold-level net performance with block/sieve methods before trusting a Sharpe or conditional edge.
4. For position sizing, only use uncertainty throttling if it improves turnover-adjusted net utility versus fixed-risk, inverse-vol, and volatility-targeting baselines.

## Risks and Failure Modes

- Valid intervals do not imply profitable forecasts.
- Block length / model choice can be data-mined.
- Coverage can still fail under abrupt regime breaks, changing liquidity, or structural market changes.
- Conformal/adaptive calibration may increase turnover if used directly for sizing without smoothing.
- Software maturity and API stability should be checked before production use.

## Connections to Existing Research

### Reinforces

- [[Forecast-uncertainty-aware ML asset pricing]]: supplies implementation-oriented uncertainty quantification for forecast intervals.
- [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]]: supports evaluating distributional outputs and calibrated intervals before adding complex backbones.
- [[Forecasting Realized Volatility with Time Series Foundation Models]]: reinforces benchmark-first, calibration-aware volatility forecasting.

### Supplies Missing Validation

- Gives practical dependence-aware resampling/conformal tools for the distributional-forecast-first ML strategy evaluation framework and for fold-level strategy diagnostics.

## Local Minimum Viable Adaptation

- Select a simple daily ETF/crypto forecast task with a strong baseline.
- Generate rolling forecasts and residuals using only time-gated data.
- Compare IID bootstrap, moving/block bootstrap, sieve bootstrap, and adaptive conformal intervals for empirical coverage.
- Evaluate downstream sizing utility net of turnover/costs, not only interval coverage.

## Classification

- Evidence quality: **Evidence-backed at abstract level as methodology / software**
- Practicality: **foundational / retail-adaptable**
- Coding priority: **Medium** once a forecast pipeline exists
