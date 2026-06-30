---
type: source-note
source_kind: paper
asset_classes: [equities, ml, risk]
implementation_class: foundational
importance: high
last_reviewed: "2026-06-30"
tags: [quant-source, ml, fat-tails, uncertainty, distributional-forecasting]
concepts: [density-forecasting, mixture-heads, crps, tail-risk]
---

# Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns

## Citation / Link

Sichao He, Yansong Zhang, “Heads, Not Backbones: Output Heads Dominate Architectures on Fat-Tailed Returns,” arXiv:2606.30037v1, 2026-06-29. https://arxiv.org/abs/2606.30037v1

## Summary

The paper compares modern forecasting backbones on fat-tailed financial returns and finds that the output head can matter more than the backbone architecture. In the abstract, moving from point forecasts to Gaussian density forecasts improves distributional metrics, and Gaussian mixture density heads improve further, especially in high-volatility regimes. Squared-error rankings do not separate models as clearly as distributional metrics such as CRPS, pinball loss, and coverage.

## Core Contribution

- Redirects model selection from “which deep architecture?” toward “what predictive distribution and loss are appropriate for fat-tailed returns?”
- Shows that distributional-output design can matter more than backbone selection for tail-sensitive evaluation.
- Supports evaluating forecasts with CRPS/coverage/pinball rather than only point-error metrics.

## Practical Relevance

- Classification: **Evidence-backed as methodology / foundational-retail-adaptable**.
- Not a standalone alpha signal; useful for any ML forecast pipeline where sizing/risk depends on uncertainty.
- Highly relevant to [[Forecast-uncertainty-aware ML asset pricing]] and heavy-tail regime/risk work.

## Methods and Data

Abstract reports S&P 500 monthly log returns from 1871–2023 with anchored walk-forward validation, four backbones, and three output heads: point, Gaussian density, and four-component Gaussian mixture density.

Local adaptation:

- evaluate return forecasts by distributional loss and calibration,
- compare point model vs Gaussian vs mixture/quantile/conformal outputs,
- include simple baselines before deep backbones.

## Leakage / Bias / Overfitting Concerns

- Monthly S&P 500 sample has limited independent tail episodes despite long history.
- Mixture heads add parameters; must test stability across regimes and assets.
- Better distributional scoring does not guarantee tradable alpha unless it improves sizing, drawdown control, or option/risk decisions net of costs.

## Transaction Cost / Capacity Treatment

Transaction costs are indirect: use distributional forecasts to throttle position size, not to justify more turnover. Any strategy using the forecasts must compare turnover-adjusted performance versus simpler volatility targeting and inverse-vol baselines.

## Strategy Ideas Extracted

Method test: in existing ML alpha experiments, replace point-forecast-only objectives with distributional heads or calibrated forecast intervals, then evaluate whether uncertainty-aware sizing improves drawdown/turnover-adjusted returns versus naive volatility targeting.

## Connections to Existing Research

### Reinforces

- [[Forecast-uncertainty-aware ML asset pricing]]: uncertainty quality and calibration may matter more than point forecast accuracy.
- [[Continuous Hidden Markov Models for Equity Returns]]: heavy tails should be modeled in the predictive distribution, not ignored.
- [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]]: evaluate models by downstream decision utility, not generic error alone.

### Contradicts / Weakens

- Weakens architecture-first ML claims where Transformers/GNNs are promoted without better distributional calibration or simple baselines.

### Transfers Across Asset Classes or Domains

- Crypto forecasting should test output distributions and fee-aware sizing before adding complex graph/sequence backbones.

### Missing Validation or Method Supplied

- Supplies a concrete validation layer: CRPS, pinball loss, coverage, and volatility-regime subsamples.

## Framework Potential

- Candidate framework: distributional-forecast-first ML strategy evaluation.
- Linked notes: [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]], [[Continuous Hidden Markov Models for Equity Returns]], [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]].
- Testable composite hypothesis: calibrated predictive distributions improve risk-adjusted allocation more robustly than architecture changes when returns are fat-tailed.
- Minimum viable validation: compare point vs Gaussian/mixture/quantile heads on the same features and backbones, then evaluate downstream sizing/regret.
- What would falsify this connection? Distributional metrics improve but downstream turnover-adjusted portfolio outcomes do not.

## Keep / Reject Decision

**Keep** as a foundational ML validation and sizing-method reference.

## Related Notes

- [[2026-06-30 0044 Daily Quant Research Review]]
