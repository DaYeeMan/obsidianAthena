---
type: source-note
source_kind: paper / volatility-forecast validation methodology
asset_classes: [crypto, equities, ETFs, volatility, risk-management]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-08-04"
tags: [quant-source, volatility-forecasting, regime-diagnostics, forecast-bias, crypto, etfs]
concepts: [latent-regime-bias-audit, tail-underprediction, regime-conditional-forecast-validation]
---

# Latent-Regime Bias Auditing for Volatility Forecasting

## Citation / Link

Arthur Chagas, Pedro Bento, Yan Aquino, Arthur Buzelin, Wagner Meira, Cristiano Arbex Valle, “Latent-Regime Bias Auditing for Volatility Forecasting,” arXiv:2608.01599v1, submitted 2026-08-03. https://arxiv.org/abs/2608.01599v1

Comment: accepted for publication at IEEE CIFEr 2026. Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper proposes a model-agnostic volatility forecast audit that asks where forecasts fail conditionally, not only which model has the lowest average RMSE or MAE. The method learns representations of market-state windows using only training information, clusters them into latent regimes, assigns regimes out of sample, and compares aggregate behavior with regime-conditional bias, tail underprediction, and underprediction-sensitive economic losses. The abstract reports applications to daily volatility forecasting across cryptocurrency and ETF assets, where models with competitive aggregate accuracy still show severe regime-specific bias and tail underprediction.

For this library, this is directly useful as a validation layer for volatility/risk-throttle research.

## Core Contribution

- Makes regime-conditional forecast bias explicit.
- Uses training-only regime discovery and out-of-sample assignment to reduce leakage.
- Separates average forecast accuracy from tail underprediction and economic loss.
- Applies to crypto and ETF volatility, matching the library’s asset focus.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as forecast-validation methodology; foundational / retail-adaptable**.
- Retail adaptation is feasible using daily ETF/crypto returns and realized-volatility targets.
- This is a diagnostic, not a standalone volatility alpha signal.

## Backtest Translation

- Hypothesis: volatility models with similar aggregate QLIKE/RMSE can differ materially in high-risk latent regimes; regime-bias diagnostics improve risk throttle selection.
- Data: daily prices for ETFs/crypto, realized volatility target, trailing market-state windows, forecast timestamps.
- Baselines: EWMA, GARCH(1,1), HAR/log-HAR, rolling realized volatility, simple VIX/drawdown filters where applicable.
- Validation: fit regimes only on training folds, freeze clustering/assignment per fold, score regime-conditional bias/tail underprediction and downstream sizing utility after turnover/costs.

## Risks / Failure Modes

- Latent clusters can become flexible data-mining labels; require frozen fold construction and simple regime baselines.
- Diagnostic improvement may not translate into better post-cost sizing or allocation.
- Daily-volatility diagnostics may miss intraday crash/liquidity dynamics relevant to 0DTE options or leveraged crypto.

## Connections to Existing Research

- Extends [[Emergent Latent-State Computation under Stochastic Volatility]] from synthetic latent-state interpretability into real-market forecast-bias auditing.
- Reinforces [[Regime-Conditional Distributional Comparison of Trading Strategies]] and [[Long-Memory GARCH via Two-Dimensional Markov State]].
- Supplies a concrete validation block for SPX/SPXW short-vol and crypto risk-throttle research before adding complex ML forecasters.
