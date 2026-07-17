---
type: source-note
source_kind: paper
asset_classes: [risk-models, portfolio, credit]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: 2026-07-17
tags: [quant-source, model-monitoring, distribution-shift, risk-management]
concepts: [Jensen-Shannon divergence, KL divergence, PSI, model drift, power analysis]
---

# Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring

## Citation / Link

Abdullah Karasan and Alper Hekimoğlu, “Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring,” arXiv:2607.12407v1, 2026-07-14. https://arxiv.org/abs/2607.12407

## Summary

Studies divergence measures for detecting distributional shift in financial model monitoring. Extends prior work by deriving chi-square benchmark values for Jensen-Shannon Divergence and Kullback-Leibler Divergence and comparing their statistical power with Population Stability Index. Jensen-Shannon shows better Type I error control but lower small-sample power, while PSI/KL can be more sensitive but raise false-alarm risk.

## Core Contribution

Turns model-drift metrics into a power/type-I-error trade-off rather than treating PSI-style thresholds as generic heuristics.

## Practical Relevance

- Foundational / retail-adaptable.
- Useful for monitoring ML features, return forecast distributions, volatility model inputs, option-chain cleanliness, or crypto exchange-quality variables.
- Not trading evidence by itself.

## Methods and Data

Analytical distributional properties and simulations/application to credit default probabilities from Merton, jump, and stochastic-volatility-with-jump models.

## Leakage / Bias / Overfitting Concerns

- Drift thresholds can be tuned to past breaks or crisis windows.
- Bin choices and sample sizes materially affect power.
- Feature drift is not necessarily model failure unless linked to forecast calibration or decision utility.

## Transaction Cost / Capacity Treatment

No direct transaction-cost model. In trading systems, drift alarms should be evaluated by action attribution: do they reduce drawdown or prevent bad trades net of missed opportunity and turnover?

## Strategy Ideas Extracted

Use divergence metrics as a risk monitor/kill-switch component for ML and data-quality pipelines. Compare PSI, Jensen-Shannon, and KL alerts against rolling coverage/calibration errors and downstream net utility.

## Connections to Existing Research

### Reinforces

- [[Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters]]
- [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]]
- [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]]

### Contradicts / Weakens

Weakens fixed-threshold drift-monitoring rules that do not specify sample size, power, Type I error, or action consequences.

### Transfers Across Asset Classes or Domains

Transfers credit-risk model-monitoring diagnostics to equity/crypto/option-feature drift monitoring, especially for exchange-quality and forecast-input surveillance.

### Missing Validation or Method Supplied

Supplies a more explicit false-alarm versus detection-power framing for model-drift alarms.

## Framework Potential

- Candidate framework: model-monitoring and kill-switch calibration.
- Linked notes: [[Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters]], [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]].
- Testable composite hypothesis: drift alarms improve strategy governance only when they are calibrated for power/type-I-error and tied to action-attribution metrics.
- Minimum viable validation: compute PSI/JSD/KL on rolling model features and forecast residuals; test alarm precision, missed breaks, and strategy decisions versus simple volatility/drawdown filters.
- What would falsify this connection? Alarms fire mostly during benign regimes, duplicate simple volatility filters, or reduce net utility through missed trades/over-de-risking.

## Keep / Reject Decision

Keep as Evidence-backed at abstract level for monitoring methodology and foundational for validation design. Practicality: foundational / retail-adaptable.

## Related Notes

- [[Framework Candidate Registry]]
- [[2026-07-17 0802 Daily Quant Research Review]]
