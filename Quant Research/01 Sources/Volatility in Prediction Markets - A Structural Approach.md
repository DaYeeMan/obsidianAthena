---
type: source-note
source_kind: paper
asset_classes: [prediction-markets, crypto, market-microstructure, volatility]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-10"
tags: [quant-source, prediction-markets, volatility-forecasting, market-microstructure, order-flow, kalshi]
concepts: [prediction-market-volatility, wright-fisher-deadline-resolution, glosten-milgrom, binary-contracts, structural-volatility]
---

# Volatility in Prediction Markets - A Structural Approach

## Citation / Link

Weiye Xi, Ciamac C. Moallemi, Mallesh Pai, Shouqiao Want, “Volatility in Prediction Markets: A Structural Approach,” arXiv:2607.08199v1, 2026-07-09. https://arxiv.org/abs/2607.08199v1

## Summary

The paper argues that standard ARCH/GARCH volatility models are misspecified for prediction markets because prices are bounded probabilities, payoffs are binary, and resolution happens at known deadlines. It proposes a structural volatility model combining a Wright-Fisher deadline-resolution component with a Glosten-Milgrom order-flow component. In a large Kalshi contract panel, structural variables reportedly dominate plain ARCH/GARCH forecasts, while structural plus residual GARCH performs best.

## Core Contribution

- Treats prediction-market volatility as a function of bounded probability state, time-to-resolution, information arrival, spread, and volume rather than generic return clustering alone.
- Gives an interpretable framework for event-contract market making, risk management, and settlement-window diagnostics.
- Separates smooth deadline-resolution contracts from jump/event-concentrated categories such as sports.
- Extends this library's prediction-market settlement-manipulation work beyond price-level event windows into volatility and liquidity-state forecasting.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as market-microstructure / volatility methodology; foundational / retail-adaptable**.
- Retail adaptation is plausible for Kalshi/Polymarket-style datasets if historical trade, spread, volume, price, deadline, and category metadata are available.
- Not a direct alpha signal. It is more useful as a volatility/risk input, market-making risk model, event-window filter, and manipulation-risk context.

## Methods and Data

Abstract-level details:

- binary prediction-market contracts with known resolution deadlines,
- Wright-Fisher deadline-resolution component,
- Glosten-Milgrom order-flow/spread/volume component,
- large Kalshi panel,
- ARCH/GARCH and structural-plus-GARCH comparisons.

Minimum local adaptation:

1. Build contract-level panel with price, spread, volume, category, deadline, and resolution event time.
2. Forecast next-window absolute return or probability-price variance using structural variables and simple GARCH/rolling baselines.
3. Evaluate by contract category and by time-to-resolution bucket.
4. Use the model first as a risk filter for event windows, not as a standalone directional trade.

## Leakage / Bias / Overfitting Concerns

- Resolution metadata and final outcome timestamps must be available before the forecast decision, not backfilled in a way that leaks event timing.
- Category-specific fitting can overfit sparse categories; the paper's abstract says category-specific fitting does not systematically improve OOS performance.
- Bid/ask and volume fields can be stale or venue-specific; decentralized markets add indexing and wash-trade risks.

## Transaction Cost / Capacity Treatment

- Prediction-market spreads and fees are often large relative to expected short-horizon edge.
- Any market-making or volatility-linked trade must model fill probability, adverse selection, queue position, fee tiers, and contract resolution risk.
- Structural volatility forecasts may be most valuable for avoiding bad liquidity states rather than generating aggressive trades.

## Strategy Ideas Extracted

- **Hypothesis:** structural variables -- probability level, time-to-resolution, spread, volume, category, and residual volatility -- forecast prediction-market volatility better than generic GARCH and can improve risk sizing/avoidance around settlement/event windows.
- **Universe:** Kalshi/Polymarket binary contracts with enough history and clean timestamps.
- **Signal definition:** ex ante structural-vol forecast bucket; use as a no-trade/risk-limit filter and compare to rolling volatility/GARCH.
- **Backtest design:** event-time panel validation, contract-clustered OOS splits, fee/spread-aware simulated fills, and comparison against simply avoiding near-resolution windows.
- **Validation priority:** medium; useful if prediction-market data ingestion becomes available.

## Connections to Existing Research

### Reinforces

- [[Settlement Manipulation in Prediction Markets]]: settlement/event windows should be modeled structurally, not treated as generic time-series volatility.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]: order-flow and liquidity state can drive volatility without necessarily implying information.

### Contradicts / Weakens

- Weakens direct import of equity/FX GARCH models into bounded binary contracts without structural features.

### Transfers Across Asset Classes or Domains

- Similar state-space logic may apply to crypto event markets, sports/event contracts, and other bounded payoff markets where resolution time is known.

### Missing Validation or Method Supplied

- Supplies a volatility-forecasting layer for prediction-market manipulation and market-making diagnostics.

## Framework Potential

- Candidate framework: structural event-contract risk modeling.
- Linked notes: [[Settlement Manipulation in Prediction Markets]], [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]].
- Testable composite hypothesis: prediction-market risk should be conditioned on probability state, time-to-resolution, spread/volume, and event category before testing settlement or order-flow signals.
- Minimum viable validation: forecast realized probability-price volatility by time-to-resolution bucket and test whether risk filters improve net event-window strategy results.
- What would falsify this connection? structural variables fail to improve OOS forecasts after rolling volatility and time-to-resolution baselines, or costs erase any risk-filter improvement.

## Keep / Reject Decision

Keep as a high-signal foundational/retail-adaptable source for prediction-market microstructure and event-risk modeling.

## Related Notes

- [[Settlement Manipulation in Prediction Markets]]
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]
