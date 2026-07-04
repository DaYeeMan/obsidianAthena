---
type: source-note
source_kind: paper
asset_classes: [futures, trend-following, market-microstructure, portfolio]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-03"
tags: [quant-source, futures, trend-following, microstructure, transaction-costs, decay]
concepts: [short-term-trend-decay, tick-size, hft-market-making, market-impact-feedback, cta]
---

# Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following

## Citation / Link

Jutta G. Kurth, Zoltan Eisler, Adam Rej, Jean-Philippe Bouchaud, “Is Trend Still Your Friend?: A Microstructural Account of the Demise of Short-Term Trend-Following,” arXiv:2607.01550v1, 2026-07-02. https://arxiv.org/abs/2607.01550v1

## Summary

The paper studies why short-term trend-following has stopped reliably working since roughly 2009 even though longer-history trend following remains a major anomaly. Using about 100 liquid futures contracts from 1995–2025 and an industry-representative CTA proxy, the authors document that the short-term trend break depends strongly on signal speed and contract microstructure. Their central abstract-level result is that post-2008 trend PnL collapsed on small-tick contracts while remaining largely intact on large-tick contracts. The authors argue that HFT-dominated market making and liquidity withdrawal in front of predictable directional flow broke the self-reinforcing impact loop that historically sustained short-term trend in small-tick contracts.

## Core Contribution

- Converts trend-following decay from a generic crowding story into a microstructure-conditional hypothesis.
- Identifies volatility-normalized tick size as the cross-sectional variable separating degraded from surviving short-term trends.
- Treats trend profitability as partly endogenous to market impact from trend-followers, not only as passive return autocorrelation.
- Provides a concrete decay warning for short-speed trend systems and a possible survivorship filter for remaining implementations.

## Practical Relevance

- Classification: **Evidence-backed at abstract level / foundational-retail-adaptable**.
- Not enough for immediate live trading, but very useful for designing trend-following backtests and decay audits.
- Retail adaptation: test ETF/futures trend rules by speed bucket and tick-size/liquidity proxies; do not pool instruments without microstructure stratification.
- Strong implication: short-term trend backtests should explicitly include post-2009 and post-electronification regimes, turnover costs, and market-impact sensitivity.

## Methods and Data

Abstract-level details:

- roughly 100 liquid futures contracts,
- 1995–2025 sample,
- industry-representative CTA proxy,
- trend signal speed and asset-class dependence,
- cross-sectional split by volatility-normalized tick size,
- candidate explanations: capacity, electronification, CTA/order-flow interaction regime change, and microstructure mechanism.

Local minimum viable adaptation:

1. Build daily or intraday futures/ETF trend rules at multiple speeds.
2. Split instruments by tick-size/liquidity/spread proxies rather than only asset class.
3. Compare pre-2009, 2009–2019, and post-2020 performance net of realistic turnover costs.
4. Test whether surviving trend is concentrated in large-tick or high-friction instruments and whether it survives execution assumptions.

## Leakage / Bias / Overfitting Concerns

- Tick-size stratification must be defined ex ante or with lagged contract metadata.
- Futures roll, continuous-contract construction, and volatility normalization can change results.
- Short-speed trend is highly transaction-cost-sensitive; gross persistence is not sufficient.
- CTA proxy representativeness should be verified before using it as external validation.

## Transaction Cost / Capacity Treatment

This is mainly a transaction-cost and market-impact decay reference. Any local trend test should include commissions, bid/ask/spread proxies, turnover caps, and participation/impact stress. A rule that works only on small-tick contracts gross of costs should be treated as suspect.

## Strategy Ideas Extracted

### Microstructure-conditioned trend decay audit

- **Hypothesis:** Short-speed trend profitability is now conditional on market microstructure; large-tick/high-depth contracts retain more trend-following edge than small-tick contracts after costs.
- **Asset class / universe:** Liquid futures, ETF proxies where futures data are unavailable.
- **Signal:** Multi-speed time-series momentum/trend rules; evaluate by speed and tick-size/liquidity bucket.
- **Backtest design:** Rolling train/test or fixed-rule test across regimes, with turnover/cost stress and instrument-level clustering.
- **Validation priority:** Medium as a trend-filter and decay diagnostic, not as a standalone new alpha.

## Connections to Existing Research

### Reinforces

- Cost-aware decision-process diagnostics as a framework direction: strategy decay can be microstructure-driven and cost-state dependent.
- [[Regime-Conditional Distributional Comparison of Trading Strategies]]: performance should be conditioned on market-structure regimes, not averaged across eras.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]: order-flow interpretation and impact depend on liquidity state.

### Contradicts / Weakens

- Generic short-term trend-following claims that pool contracts and report pre-cost or pre-2009 performance without tick-size and market-structure splits.

### Framework Potential

- Candidate framework: microstructure-conditioned trend and reversal decay audit.
- Minimum viable backtest: add tick-size/liquidity buckets to trend and reversal tests and require post-2009 net-of-cost survival.
- What would falsify it locally: no relationship between tick-size/liquidity buckets and out-of-sample net trend performance after robust cost assumptions.
