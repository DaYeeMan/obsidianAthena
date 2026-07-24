---
type: source-note
source_kind: paper
asset_classes: [futures, equities, crypto, trend-following, portfolio]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-23"
tags: [quant-source, trend-following, time-series-momentum, autocorrelation, trading-costs, skewness]
concepts: [trend-following-systems, volatility-normalized-returns, spectral-mass, cost-optimal-span, structural-skew]
---

# The Science and Practice of Trend-Following Systems

## Citation / Link

Artur Sepp, Vladimir Lucic, “The Science and Practice of Trend-Following Systems,” arXiv:2607.19497v1, 2026-07-21. https://arxiv.org/abs/2607.19497v1

## Summary

This paper gives an analytical framework for trend-following systems, classifying them into European, American, and time-series momentum variants. The abstract derives relationships between trend-following PnL, autocorrelation, drift, and volatility-normalized returns. A key mechanism is low-frequency spectral mass: trend-following alpha appears when kernel-weighted spectral mass in normalized returns exceeds the white-noise benchmark, and longer lookbacks gain additionally from squared drift. The paper also derives Sharpe, cost-optimal span under trading costs, and structural positive skewness of aggregated trend-following returns.

The useful library takeaway is not “trend always works.” It is a design and attribution language for comparing trend speeds, persistence, drift, costs, and skewness against microstructure-conditioned decay evidence.

## Core Contribution

- Provides a mechanism-level decomposition of trend-following returns into autocorrelation, drift, low-frequency spectrum, costs, and skewness.
- Offers a cost-optimal lookback/span lens instead of tuning trend speeds only by historical Sharpe.
- Reinforces the library’s distinction between slower trend/carry-style persistence and fragile short-speed trend affected by microstructure.
- Gives a way to evaluate whether trend performance comes from structural skew/drift or overfit autocorrelation at noisy frequencies.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as trend-following methodology; foundational / retail-adaptable**.
- Retail adaptation: use daily ETF/futures/crypto returns, volatility-normalized returns, simple moving-average/time-series-momentum rules, explicit turnover, and spread/slippage stress.
- Not a new standalone alpha claim until the target universe, lookback family, roll/margin/funding assumptions, and costs are specified.
- Particularly useful for deciding whether a trend signal’s lookback is economically cost-optimal rather than sample-fit.

## Data / Backtest Requirements

- Universe: liquid futures or ETF proxies; crypto perpetuals only with funding/fees and venue-risk controls.
- Fields: returns, realized volatility or volatility target, trade dates, contract rolls/funding where relevant, transaction costs, turnover.
- Baselines: buy-and-hold, equal-weight/inverse-vol, simple 12-month TSMOM, shorter lookback variants, and no-trade/white-noise simulations.
- Validation: walk-forward parameter selection, pre/post-publication and regime splits, market-structure buckets, non-overlapping inference for overlapping signals.

## Costs / Frictions

Trend strategies can lose if the gross persistence signal sits below turnover, spread, roll/funding, tax, and impact costs. Cost-optimal span should be treated as a constraint and robustness diagnostic, not only an optimization target.

## Failure Modes / Decay Risks

- Post-publication crowding and strategy commoditization.
- Short-speed trend decay after microstructure changes and HFT liquidity provision.
- Lookback/data-mining overfit, especially when selecting the best span ex post.
- Futures roll and cash/margin assumptions can dominate portfolio-level results.
- Crypto variants may be venue-specific and funding-sensitive.

## Connections to Existing Research

### Reinforces

- [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]] by giving a mechanism for separating slower persistence from microstructure-fragile short-speed trend.
- [[Regime-Conditional Distributional Comparison of Trading Strategies]] because trend evaluation should report conditional distributions, not only full-period Sharpe.

### Contradicts / Weakens

- Weakens naïve claims that any moving-average crossover is evidence of tradable alpha; persistence, costs, and structural skew must be identified separately.

### Framework Potential

- Candidate framework: trend-following decomposition and cost-optimal span audit.
- Minimum viable backtest: daily liquid futures/ETF trend rules with volatility normalization, lookback grid, turnover/cost stress, and comparison to spectral/autocorrelation diagnostics.
- Falsifier: no robust net performance or skew advantage after walk-forward lookback selection, realistic costs, and simple baselines.
