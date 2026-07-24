---
type: source-note
source_kind: paper
asset_classes: [equities, futures, crypto, market-microstructure, liquidity]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-21"
tags: [quant-source, market-microstructure, liquidity-stress, herding, fundamental-anchoring, market-resilience]
concepts: [fundamental-anchoring, liquidity-resilience, one-sided-book-stress, fire-sale, liquidity-transmission]
---

# Herding and Liquidity in Order-Book Markets II - Fundamental Anchoring and Liquidity Resilience

## Citation / Link

Jan Novotny, “Herding and Liquidity in Order-Book Markets. II. Fundamental Anchoring and the Resilience of Liquidity,” arXiv:2607.16970v1, 2026-07-18. https://arxiv.org/abs/2607.16970v1

## Summary

This paper extends the order-book herding/liquidity-stress model by emphasizing fundamental anchoring. In the model, liquidity provision anchored to a fundamental value creates a restoring force: price mean-reverts toward value and the book refills after shocks. Removing the anchor eliminates mean reversion and allows leverage-driven fire sales to self-sustain. The abstract also reports that stress in one coupled market does not automatically transmit to a calmer market across several channels; market-maker withdrawal can thin the receiving book but does not by itself ignite a liquidity crisis.

The paper’s order parameter is one-sidedness of the book rather than directional price crashes. A liquidity crisis is framed as persistent one-sided book stress caused by failed anchoring, not merely a lack of market-making activity.

## Core Contribution

- Adds a mechanism to the prior liquidity-stress crossover note: failure of anchoring, not just herding intensity, determines whether liquidity shocks become persistent.
- Suggests that backtest stress states should track one-sided book pressure and anchor quality separately from ordinary volatility.
- Warns against assuming liquidity stress transmits mechanically across related markets; cross-market stress requires state conditioning, not blanket contagion assumptions.
- Helps interpret market-maker withdrawal as a liquidity-thinning variable that may raise costs without necessarily producing a self-sustaining crisis.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as market-microstructure simulation/theory; foundational**.
- Practicality: **foundational / retail-adaptable** only through proxies such as spread, depth imbalance, return-to-anchor distance, volatility bursts, ETF/futures basis, funding/basis, or deviations from reference/fundamental prices.
- Not direct alpha evidence.
- Useful as a cost and regime-conditioning input for short-horizon trend/reversal, crypto futures order-flow, and event-window strategies.

## Methods and Data

Abstract-level details:

- Order-book market model with liquidity provision anchored to a fundamental value.
- Causal intervention by dialing down anchor strength.
- Coupled-market stress transmission tests across herding, arbitrage flow, market-maker withdrawal, funding constraints, fire sales, and leverage spirals.
- Liquidity-stress order parameter: sustained one-sidedness of the book.

## Leakage / Bias / Overfitting Concerns

- Simulation thresholds may not transfer to real venues.
- Retail proxies for fundamental anchor strength are noisy and can be endogenous.
- Cross-market “non-transmission” in the model does not prove real markets avoid contagion; funding, margin, and correlated positioning can dominate.
- Stress filters must be evaluated by action attribution, because over-conservative filters can miss profitable rebounds.

## Transaction Cost / Capacity Treatment

Primary use is transaction-cost/risk conditioning: raise spread/slippage/fill-risk stress when book one-sidedness, depth depletion, basis/funding dislocation, or anchor deviation is elevated. Do not treat simulated resilience as permission to ignore costs.

## Strategy Ideas Extracted

Add an anchor-quality / one-sided-liquidity-state panel to backtests:

1. Define accessible anchor proxies: ETF NAV/futures fair value, index futures basis, crypto spot-perp basis/funding, VWAP/reference-price deviation, or slow moving fair-value models.
2. Define one-sided liquidity proxies: order-book imbalance when available, spread/depth deterioration, signed-volume imbalance, volatility burst, and rebound failure.
3. Stress costs/sizing when anchor deviation and one-sidedness jointly rise.
4. Compare against simple volatility/drawdown filters and liquidity-tail proxies.

## Connections to Existing Research

### Reinforces

- [[Herding and Liquidity in Order-Book Markets - A Robust Liquidity-Stress Crossover]]: adds the anchoring/resilience mechanism behind the earlier liquidity-stress crossover.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]: large order-flow shocks are not always information; state-dependent liquidity tails matter.
- [[When Does Order Flow Matter - State-Dependent L2 Liquidity-State Transitions in Crypto Futures]]: order-flow usefulness depends on pre-event liquidity state.
- [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]]: clock-phase order-flow signals should be tested conditional on anchor/liquidity resilience.

### Framework Potential

- Candidate framework: Microstructure-conditioned decay and liquidity-state validation.
- Testable composite hypothesis: short-horizon signals survive only when liquidity state is resilient or when cost stress does not absorb the signal.
- Minimum viable backtest: compare signal PnL and costs by anchor-deviation and one-sided-liquidity buckets.
- What would falsify this framework? No incremental explanatory value beyond volatility/drawdown/spread filters, or filters that reduce drawdown only by skipping most profitable trades.

## Validation Priority

Medium/high as an audit feature for crypto futures and intraday strategies; reference-only as standalone theory.
