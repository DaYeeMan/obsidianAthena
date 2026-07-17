---
type: source-note
source_kind: paper
asset_classes: [ml, forecasting, risk, validation]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-14"
tags: [quant-source, conformal-prediction, quantile-forecasting, calibration, online-monitoring, model-risk]
concepts: [feature-aware-calibration, anytime-valid-audit, conditional-quantile-forecasters, evidence-process, non-iid-losses]
---

# Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters

## Citation / Link

Ivane Antonov, Sohom Mukherjee, Richard Pibernik, Yo Joong Choe, “Bet on Features: Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters,” arXiv:2607.11653v1, 2026-07-13. https://arxiv.org/abs/2607.11653v1

## Summary

This adjacent-domain ML/statistics paper develops a distribution-free game-theoretic testing framework for continuously auditing black-box conditional quantile forecasters. The abstract emphasizes that calibration depends on the auditor's information set: a quantile model can appear calibrated under coarse information but fail when richer features are considered. The method produces anytime-valid evidence processes for non-IID losses and feature-specific evidence of miscalibration, and finds a popular time-series forecaster miscalibrated with respect to several relevant features.

## Core Contribution

- Turns quantile forecast calibration into a continuously monitored, feature-aware process rather than a one-time fixed-horizon backtest.
- Does not require IID losses, which is crucial for financial time series.
- Produces interpretable feature-level evidence for where calibration fails.
- Supplies a method lead for online risk monitors and kill-switches in forecast-driven trading systems.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as adjacent-domain validation methodology; foundational / retail-adaptable**.
- Not trading evidence and not a standalone alpha source.
- Useful for volatility forecasts, VaR/ES proxies, quantile return forecasts, ML risk throttles, and any strategy that sizes positions from conditional quantiles.
- Strongly complements dependence-aware bootstrap/conformal validation already in the library.

## Methods and Data

Abstract-level details:

- conditional quantile calibration under different auditor feature sets,
- distribution-free game-theoretic testing,
- anytime-valid evidence processes,
- non-IID losses,
- contextual bets linear in auditor features,
- finite-time detection guarantees,
- empirical validation on simulated and real data including Chronos-2 miscalibration.

Minimum local adaptation:

1. Choose a forecasting target such as next-day realized volatility, drawdown quantile, or return lower-tail quantile.
2. Define auditor features available at decision time: volatility regime, liquidity state, trend state, asset, time-of-day/expiry bucket, sentiment extreme, or option-skew bucket.
3. Run online feature-aware calibration monitoring on out-of-sample forecasts.
4. Trigger review/throttling only when evidence is persistent and improves downstream net utility versus simple thresholds.

## Backtest / Validation Design

- Use rolling-origin forecasts with strict availability timestamps.
- Compare model quantiles against EWMA/GARCH/Log-HAR or simple historical quantiles.
- Report feature-specific miscalibration evidence, coverage, interval width, action changes, turnover, and net utility.
- Test whether an anytime-valid monitor detects regime failure earlier than fixed-window coverage checks without excessive false alarms.

## Risks / Failure Modes

- Feature-aware audits can become multiple-testing/data-mining exercises if auditor features are chosen post hoc.
- Evidence of miscalibration does not automatically imply a profitable trading adjustment.
- Online alarms can cause over-trading or overly conservative de-risking if not tied to action-attribution.
- Financial structural breaks may invalidate previously learned calibration relationships.

## Connections to Existing Research

### Reinforces

- [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]] by adding online, feature-aware quantile-calibration auditing.
- [[Forecast-uncertainty-aware ML asset pricing]] and [[Forecasting Realized Volatility with Time Series Foundation Models]] by requiring forecast intervals to be checked conditional on regimes/features.
- [[Robustness in Sequential Decision Making under Evolving Uncertainty]] by separating uncertainty detection from the action response.

### Framework Potential

- Candidate framework: online feature-aware forecast-risk monitoring.
- Minimum viable test: add feature-aware quantile-audit outputs to the standard ML/volatility forecast validation block.
- Falsifier: feature-aware alarms fail to improve calibration, drawdown control, or net utility versus simple rolling coverage and volatility thresholds.
