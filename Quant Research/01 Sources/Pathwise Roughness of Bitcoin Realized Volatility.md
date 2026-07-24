---
type: source-note
source_kind: paper / empirical volatility-methodology study
asset_classes: [crypto, bitcoin, volatility, risk-management]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: "2026-07-24"
tags: [quant-source, bitcoin, realized-volatility, rough-volatility, p-variation, volatility-measurement]
concepts: [bitcoin-realized-volatility-roughness, pathwise-roughness, normalized-p-variation, measurement-stability, rough-volatility-risk-filter]
---

# Pathwise Roughness of Bitcoin Realized Volatility

## Citation / Link

Milan Pontiggia, “Pathwise Roughness of Bitcoin Realized Volatility: Stability Across Time, Sampling, and Volatility Measures,” arXiv:2507.00575v4, updated 2026-07-23. https://arxiv.org/abs/2507.00575v4

Comment: 32 pages, 5 figures, 14 tables; code available upon request.

## Summary

The paper examines whether Bitcoin realized volatility has a measurable pathwise roughness index and whether that estimate is stable across time, sampling frequencies, and volatility measures. Using one-minute BTC/USD Bitstamp close prices from 2017–2024, it constructs realized-volatility paths at 1-, 5-, 10-, and 15-minute frequencies and applies the model-free normalized p-variation estimator of Cont and Das. A unique root is obtained in 341 of 380 rolling 90-day window/frequency configurations and 113 of 128 non-overlapping configurations. Conditional rolling median roughness estimates are low — 0.054, 0.065, 0.086, and 0.080 across the four frequencies — and finite estimates are below 1/2. However, root availability and estimate magnitude vary by period and measurement design, and the paper explicitly cautions that observed realized-volatility roughness does not directly identify latent spot-volatility roughness.

For this library, the value is a volatility-measurement and risk-modeling warning: Bitcoin volatility may look rough, but the estimate is measurement-sensitive and should not become an overfit trading feature without simple realized-volatility baselines.

## Core Contribution

- Supplies a model-free roughness measurement approach for BTC realized volatility.
- Shows low roughness estimates across many windows while documenting instability across time, frequency, truncation, and volatility measure.
- Distinguishes observed realized-volatility path roughness from latent spot-volatility roughness.
- Adds crypto-specific evidence to the library’s realized-volatility/risk-throttle and distributional validation themes.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as volatility-measurement evidence; foundational / retail-adaptable**.
- Retail adaptation: feasible with minute BTC data, but first use as a risk-model diagnostic rather than an alpha signal.
- Not coding-ready as a standalone trading strategy; roughness features must beat EWMA, HAR/Log-HAR, GARCH-style, realized-vol, funding, and drawdown baselines in downstream net utility.

## Data / Backtest Requirements

- Minute-level BTC/USD or BTC perpetual futures prices, with exchange-quality checks, outages, and timestamp normalization.
- Realized volatility at multiple sampling frequencies and window lengths.
- Jump-robust alternatives such as bipower variation or truncation variants.
- Strictly lagged feature construction: roughness estimated only from data available before the sizing/trading decision.
- Downstream evaluation as risk sizing/throttle, not just forecast loss.

## Leakage / Bias / Overfitting Concerns

- Frequency/window selection can be tuned after seeing performance.
- Exchange-specific data quality, outages, API changes, and 24/7 calendar effects can change estimates.
- Roughness estimates may duplicate ordinary realized volatility, volatility-of-volatility, or jump-intensity information.
- Feature instability can create false regime labels; require fold-level stability and action attribution.

## Transaction Cost / Capacity Treatment

Roughness is most plausible as a risk-throttle or sizing feature. Any strategy consuming it must include crypto fees, spread/slippage, funding for perpetuals, liquidation/ADL stress if leveraged, and missed-opportunity cost from risk-off filters.

## Strategy Ideas Extracted

- **Hypothesis:** BTC volatility roughness may identify regimes where volatility forecasts or leverage sizing should be de-risked, but only if it improves downstream net utility beyond simple realized-volatility and funding/drawdown filters.
- **Asset class/universe:** BTC spot or perpetual futures; possible later extension to ETH and liquid crypto futures.
- **Signal definition:** lagged rolling pathwise roughness estimate and root-availability/stability indicators, bucketed by sampling frequency/window; use as throttle, not directional signal.
- **Backtest design:** compare EWMA/HAR/GARCH-style volatility sizing with and without roughness features across exchange/date regimes; evaluate turnover, realized drawdown, tail loss, and missed rebound.
- **Validation priority:** medium as a framework/risk-model feature; low as standalone alpha.

## Connections to Existing Research

### Reinforces

- [[Forecasting Realized Volatility with Time Series Foundation Models]]: complex volatility features should be judged against simple realized-volatility baselines and downstream sizing utility.
- [[Regime-Conditional Distributional Comparison of Trading Strategies]]: roughness can be an ex ante regime covariate, but must be tested for conditional net utility.
- [[Risk-Based Auto-Deleveraging]]: volatility-state signals should interact with crypto leverage and venue-stress controls before production use.
- [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]]: price-derived crypto features require fee-aware baselines and no-trade gates.

### Framework Potential

- Candidate framework: regime-conditional distributional strategy evaluation.
- Testable composite hypothesis: pathwise volatility roughness adds incremental risk-control value beyond realized volatility, drawdown, funding, and venue-stress filters.
- Minimum viable backtest: BTC volatility-targeting/risk-throttle experiment with lagged roughness features and simple baselines.
- What would falsify this framework? roughness buckets are unstable across exchanges/frequencies or fail to improve tail risk/downstream utility net of turnover and missed-rebound costs.

## Keep / Reject Decision

Keep as a foundational/retail-adaptable volatility measurement source. Do not add to the coding-ready queue until a baseline BTC volatility-sizing backtest exists.
