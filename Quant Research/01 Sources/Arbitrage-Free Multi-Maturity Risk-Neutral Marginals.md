---
type: source-note
source_kind: paper
asset_classes: [options, volatility, derivatives, risk-management]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: "2026-07-08"
tags: [quant-source, options, risk-neutral-density, arbitrage-free, volatility-surface, tail-risk]
concepts: [risk-neutral-marginals, butterfly-arbitrage, calendar-arbitrage, option-implied-distributions, power-law-tails]
---

# Arbitrage-Free Multi-Maturity Risk-Neutral Marginals

## Citation / Link

Hao Qin, Ruozhong Yang, Charlie Che, Liming Feng, “Arbitrage-Free Multi-Maturity Risk-Neutral Marginals,” arXiv:2607.06204v1, 2026-07-07. https://arxiv.org/abs/2607.06204v1

## Summary

The paper proposes an explicit construction of risk-neutral marginal distributions from discrete arbitrage-free option prices across maturities. The abstract emphasizes downstream applications that work with option-implied distributions rather than raw option prices: martingale optimal transport, Bass local-volatility calibration, scenario analysis, and option-implied tail-risk measurement. The proposed construction assigns probability mass interval-by-interval over observed strikes to reproduce input option prices, then completes tails using closed-form power-law tails satisfying price and slope boundary conditions while preserving butterfly- and calendar-arbitrage-freeness.

## Core Contribution

- Bridges arbitrage-free option price data and usable risk-neutral marginal distributions.
- Guarantees butterfly and calendar arbitrage freedom by construction, rather than relying on post-hoc smoothing.
- Provides closed-form density, distribution, quantile, and Monte Carlo sampling objects.
- Useful for option-implied tail-risk analytics and stress scenarios where raw option-chain interpolation can introduce arbitrage artifacts.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as derivatives methodology; foundational / retail-adaptable**.
- Not a standalone options strategy; it improves option-chain preprocessing, implied distribution estimation, and tail-risk diagnostics.
- Retail adaptation is possible if historical option chains with bid/ask are available, but production use needs careful cleaning and no-arbitrage filtering before marginal construction.
- Strong relevance to SPX/SPXW short-vol research: implied tail and skew diagnostics should be built from arbitrage-consistent distributions, not ad hoc interpolated IV points.

## Methods and Data

Abstract-level details:

- input: discrete arbitrage-free option prices across strikes and maturities,
- interval-by-interval mass assignment on observed strike range,
- closed-form power-law tail completion outside observed strikes,
- exact reproduction of input prices,
- butterfly/calendar arbitrage-freeness,
- closed-form CDF/density/quantiles and Monte Carlo sampling,
- numerical experiments reported in abstract but not yet inspected in full.

## Leakage / Bias / Overfitting Concerns

- The method assumes input prices are already arbitrage-free; raw retail option data often violate this due to stale quotes, crossed markets, and bid/ask noise.
- Tail completion can dominate tail-risk signals; power-law tail assumptions should be stress-tested.
- Option strategy backtests must use quote-time availability and executable bid/ask, not retrospectively smoothed surfaces.
- Implied distributions are risk-neutral, not physical forecasts; carry/risk-premium interpretation requires realized-distribution comparison.

## Connections to Existing Research

### Reinforces

- [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]]: improves tail/skew diagnostics and stress testing for short-dated option-selling ideas.
- [[Forecasting Realized Volatility with Time Series Foundation Models]] and [[Risk-Sensitive Specialist Routing for Volatility Forecasting]]: risk-neutral tails can be compared against realized-volatility forecasts to evaluate volatility-risk-premium assumptions.

### Transfers Across Asset Classes

- Most practical in index options and liquid ETF options where multi-maturity chains are available; less reliable in illiquid single-name options with wide spreads and stale quotes.

## Framework Potential

- Candidate framework: arbitrage-consistent option-implied tail diagnostics.
- Linked notes: [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]], [[Forecasting Realized Volatility with Time Series Foundation Models]], [[Risk-Sensitive Specialist Routing for Volatility Forecasting]].
- Testable composite hypothesis: short-volatility sizing and drawdown control improve when implied tail/skew state is estimated from arbitrage-consistent marginals and compared with realized-volatility forecasts.
- Minimum viable backtest: compute no-arbitrage risk-neutral tail metrics for SPX/SPXW chains, compare against VIX/IV percentile/skew baselines, and evaluate whether they improve fixed-risk put-writing drawdown control net of bid/ask.
- What would falsify this framework? If arbitrage-consistent tail metrics fail to improve over simple VIX/skew/IV-rank filters after quote cleaning, costs, and crash-period tests.

## Classification

- Evidence quality: **Evidence-backed at abstract level as options methodology**.
- Practicality: **foundational / retail-adaptable with option-chain data**.
- Coding priority: **Low/Medium** until option-chain data access is resolved.
