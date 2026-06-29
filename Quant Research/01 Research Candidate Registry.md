---
type: research-candidate-registry
created: 2026-06-28
last_updated: 2026-06-29
tags: [quant-research, candidate-registry, phase-2]
---

# Research Candidate Registry

This is the cross-library sorting/filtering table for research ideas. Daily reviews should update this registry when a candidate is added, materially reclassified, rejected, or flagged as outdated.

## Status Legend

- **Evidence-backed**: credible empirical/statistical evidence, but still requires implementation-specific validation.
- **Plausible but untested**: credible rationale or early evidence; not yet independently replicated here.
- **Speculative**: possible research lead with high uncertainty or fragile evidence.
- **Low quality**: weak methodology, unclear rules, or insufficient evidence.
- **Rejected**: not worth pursuing unless new evidence appears.

## Practicality Legend

- **retail-practical**: feasible with common data/tools and realistic retail execution.
- **retail-adaptable**: original version may be complex/institutional, but a simpler proxy is testable.
- **institutional-only**: requires privileged data, execution, scale, or infrastructure.
- **foundational**: important for methods/baselines even if not directly tradable.
- **outdated-watch**: may be decayed, crowded, obsolete, or superseded.

## Candidate Table

| Candidate | Asset Class | Strategy / Method Family | Status | Practicality | Coding Priority | Decay Risk | Last Reviewed | Primary Note | Next Action |
|---|---|---|---|---|---|---|---|---|---|
| SPX/SPXW short-dated put-writing with VIX and fractional-Kelly sizing | Options / equities | Volatility risk premium; position sizing | Plausible but untested | retail-adaptable | High | High: crowded short-vol, 0DTE market-structure shift, crash risk, bid/ask realism | 2026-06-28 | [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] | Replicate fixed-risk baseline first; require bid/ask fills, regime splits, margin/cash treatment. |
| Decision-aware covariance estimation for GMVP under heavy tails | Portfolio/risk | Covariance estimation; portfolio construction | Evidence-backed as methodology | foundational / retail-adaptable | Medium | Low as concept; turnover/cost risk in application | 2026-06-28 | [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]] | Add decision-regret metrics to portfolio backtests; compare against equal-weight/inverse-vol/Ledoit-Wolf. |
| Forecast-uncertainty-aware ML asset pricing | Equities / ML | Forecast uncertainty; sizing/shrinkage | Evidence-backed as methodology | foundational / retail-adaptable | Medium | Medium: ML forecasts unstable; confidence intervals can be miscalibrated under regime shift | 2026-06-28 | [[2026-06-28 Daily Quant Research Review]] | Create source note if reused; apply uncertainty shrinkage to ML alpha forecasts. |
| CryptoGAT / price-only crypto sequence-model skepticism | Crypto / ML | Forecasting baseline / model warning | Plausible but untested | retail-adaptable / outdated-watch | Medium | High: crypto regimes change quickly; price-only DL often fails after fees | 2026-06-29 | [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]] | Replicate only against strong simple baselines and fee-aware crypto cross-sectional rules; treat as warning first, not production alpha. |
| Continuous heavy-tail HMMs for equity return simulation and regime-conditional VaR | Equities / portfolio / risk | Regime models; synthetic data; risk modeling | Plausible but untested | foundational / retail-adaptable | Medium | Medium: predictive value may be limited even if stylized-fact fit is strong; risk of complexity without downstream decision gain | 2026-06-29 | [[Continuous Hidden Markov Models for Equity Returns]] | Use as simulation/risk baseline first; compare against EWMA vol and simple regime filters before any strategy deployment. |
| Crypto Granger-causality interaction networks | Crypto | Lead-lag / network features | Speculative | retail-adaptable only at slower horizons | Low/Medium | High: multiple testing, latency, fees, delistings, nonstationarity | 2026-06-28 | [[2026-06-28 Daily Quant Research Review]] | Only test with false-discovery controls and slow-horizon proxy; otherwise deprioritize. |
| Square-root law of market impact in U.S. large-cap equity | Equities / microstructure | Slippage/capacity model | Evidence-backed as execution-cost reference | institutional-only / foundational | Medium | Low as concept; direct ITCH/metaorder inference not retail-practical | 2026-06-28 | [[2026-06-28 Daily Quant Research Review]] | Use as cost-model reference, not alpha. Consider square-root participation penalty when scaling strategies. |

## Sorting Views

### Highest Coding Priority

1. [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] — High priority, but only if option-chain data with bid/ask are available.
2. Decision-aware covariance metrics — Medium priority, useful across portfolio/risk backtests.
3. Forecast-uncertainty-aware ML sizing — Medium priority, useful when ML scores are introduced.

### Outdated / Decay Watch

- Pure price-only deep learning for crypto forecasting.
- Crowded short-dated option-selling strategies, especially 0DTE-era variants.
- High-frequency crypto lead-lag/network claims without fee/latency/multiple-testing controls.

### Foundational References to Keep

- Decision-aware covariance estimation.
- Forecast uncertainty in ML asset pricing.
- Square-root market impact / capacity modeling.

## Maintenance Rules

- Update this note after each daily review when a new candidate is worth tracking.
- Do not add every screened paper; only add items that are useful as a strategy candidate, warning, foundational method, or rejection reference.
- If a candidate appears in multiple daily reviews, update the existing row rather than duplicating it.
- If evidence improves or worsens, update `Status`, `Practicality`, `Decay Risk`, and `Next Action`.
- If a candidate becomes coding-ready, create or link a backtest spec under [[Quant Research/04 Backtest Specs/Backtest Spec Index|Backtest Spec Index]].
