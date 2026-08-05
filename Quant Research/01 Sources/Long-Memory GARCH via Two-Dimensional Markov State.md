---
type: source-note
source_kind: paper / volatility-model methodology
asset_classes: [equities, options, crypto, volatility, risk-management]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: "2026-07-29"
tags: [quant-source, volatility-forecasting, garch, long-memory, markov-chain, risk-management]
concepts: [long-memory-garch, state-dependent-volatility-decay, two-dimensional-markov-state, qlike-baseline]
---

# Long-Memory GARCH via Two-Dimensional Markov State

## Citation / Link

Kyungsub Lee, Kennedy Titus Kayaki, “Long-memory GARCH via a two-dimensional Markov chain,” arXiv:2607.25189v1, submitted 2026-07-28. https://arxiv.org/abs/2607.25189v1

Semantic Scholar lookup was rate-limited during the 2026-07-29 daily run, so citation counts were not recorded.

## Summary

The paper proposes a GARCH-type volatility model where level-and-slope updates of a latent power-law kernel generate state-dependent decay of past shocks while keeping the volatility state two-dimensional and Markovian. The abstract reports a Foster-Lyapunov stability condition, positive Harris recurrence, a unique invariant distribution, simulations with substantial low-frequency persistence near the stability boundary, and competitive out-of-sample volatility forecasting.

For this library, the useful object is a compact long-memory volatility baseline. It can strengthen volatility-risk-premium, crypto volatility-throttle, and options-sizing research only if it beats simpler EWMA/GARCH/HAR/log-HAR models by QLIKE and by downstream net utility after turnover and missed-risk costs.

## Core Contribution

- Compresses long-memory volatility persistence into a two-dimensional Markov state.
- Provides theoretical stationarity/recurrence conditions rather than only empirical fitting.
- Offers a low-dimensional alternative to high-parameter neural volatility models.
- Reinforces the library rule that nonlinear or complex volatility models need strong simple anchors.

## Practical Relevance

- Classification: **Plausible but untested at abstract level as volatility-forecasting methodology; foundational / retail-adaptable**.
- Retail adaptation is feasible with daily or intraday returns for ETFs, SPX proxies, BTC/ETH, and liquid futures.
- Not a standalone alpha signal; test first as a risk/sizing input.

## Methods and Data

- Return series and log-squared innovation history.
- Two-dimensional latent Markov state governing power-law decay.
- Compare against EWMA, GARCH(1,1), HAR/log-HAR, realized-volatility, and existing distributional-output models.
- Use chronological splits; report QLIKE, calibration, tail-loss detection, and downstream sizing utility.

## Leakage / Bias / Overfitting Concerns

- Stability-boundary tuning may overfit persistent regimes.
- Forecast gains may be asset/sample-specific.
- Volatility forecast improvement does not guarantee tradable performance once rebalancing costs and missed rebound costs are included.

## Transaction Cost / Capacity Treatment

No trading costs in the abstract. Any use in strategy sizing must account for turnover induced by volatility changes, option spread costs, futures/ETF spread and slippage, and crypto venue frictions.

## Strategy Ideas Extracted

Use as a candidate volatility-state input for SPX short-volatility throttles, ETF/crypto volatility targeting, and regime-conditional backtest reports. Do not promote until it beats simple volatility baselines out of sample.

## Connections to Existing Research

### Reinforces

- [[Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting]]: both argue for anchored volatility models and incremental residual/structure tests.
- [[Pathwise Roughness of Bitcoin Realized Volatility]]: both address long-memory/roughness/persistence, but this paper proposes a forecast model rather than only measurement.

### Contradicts / Weakens

Weakens claims that high-dimensional neural volatility models are necessary before compact Markov/GARCH anchors are exhausted.

### Transfers Across Asset Classes or Domains

The same forecast discipline can transfer from equities/options to BTC/ETH volatility throttles if tested against venue-stress and realized-volatility baselines.

### Missing Validation or Method Supplied

Supplies a compact long-memory baseline for the distributional/regime volatility framework.

## Framework Potential

- Candidate framework: Regime-conditional distributional strategy evaluation / Distributional-forecast-first ML strategy evaluation.
- Linked notes: [[Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting]], [[Pathwise Roughness of Bitcoin Realized Volatility]], [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]].
- Testable composite hypothesis: compact long-memory volatility states improve risk sizing only when they add QLIKE and downstream net utility versus EWMA/GARCH/HAR.
- Minimum viable validation: per-asset walk-forward volatility forecast plus risk-sizing backtest.
- What would falsify this connection? No stable QLIKE improvement or net utility gain after turnover/costs versus simpler anchors.

## Keep / Reject Decision

Keep as a foundational volatility baseline candidate. Coding queue unchanged.

## Related Notes

- [[Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting]]
- [[Pathwise Roughness of Bitcoin Realized Volatility]]
- [[Forecasting Realized Volatility with Time Series Foundation Models]]
