---
type: source-note
source_kind: paper / passive execution and limit-order impact model
asset_classes: [equities, fx, market-microstructure, execution]
implementation_class: foundational / institutional-only as written / retail-adaptable as cost model
importance: high
last_reviewed: "2026-07-31"
tags: [quant-source, execution, passive-impact, limit-orders, adverse-selection, market-impact]
concepts: [passive-market-impact, fill-probability-decay, order-flow-imbalance-response, limit-order-execution]
---

# Optimal Execution with Passive Market Impact

## Citation / Link

Alexander Barzykin, Robert Boyce, Eyal Neuman, Sturmius Tuschmann, “Optimal Execution with Passive Market Impact,” arXiv:2607.28323v1, submitted 2026-07-30. https://arxiv.org/abs/2607.28323v1

Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper derives a mesoscopic optimal-execution model for limit orders that explicitly includes passive price impact. It uses two empirical observables: fill probabilities decay approximately exponentially with quote distance from the midprice, and short-term price changes respond linearly to order-flow imbalance. Combining these assumptions yields a reduced-form passive impact rate that decays exponentially with quote distance.

The model frames passive execution as a tactical trade-off: quoting more aggressively raises fill probability but increases accumulated impact/adverse selection; quoting less aggressively lowers impact but increases non-execution risk. The abstract reports empirical support from NASDAQ equities and public FX, plus extensions for heterogeneous decay, transient impact, and target schedules.

For this library, the useful object is a cost/fill realism upgrade for short-horizon and stat-arb backtests. Limit-order fills should not be treated as free midprice executions; passive quotes carry adverse-selection and opportunity-cost terms that depend on quote distance and order-flow state.

## Core Contribution

- Formalizes passive impact for limit-order execution, not only aggressive market-order impact.
- Links fill probability, adverse selection, quote aggressiveness, and opportunity cost in one execution model.
- Provides an empirically motivated bridge between simple spread/slippage assumptions and full limit-order-book simulation.
- Strengthens execution-cost audits for strategies that assume passive fills or maker rebates.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as execution-cost methodology; foundational / institutional-only as written / retail-adaptable as stress model**.
- Institutional as written because calibration needs order-book/fill data and tactical execution infrastructure.
- Retail adaptation: use a conservative passive-fill stress model in backtests — fill probability falls with quote distance, expected adverse selection rises with order-flow imbalance, and unfilled orders incur opportunity cost.

## Methods and Data

- Limit-order fill probability decay with distance from mid.
- Short-term price response to order-flow imbalance.
- Optimal liquidation with controlled passive quote aggressiveness.
- Empirical calibration using NASDAQ equities and public FX.

## Leakage / Bias / Overfitting Concerns

- Fill-probability and order-flow response parameters are venue-, asset-, time-, and volatility-state dependent.
- Public data may not capture queue position, hidden liquidity, maker/taker rebates, or partial fills.
- A calibrated passive-fill model can still overfit if it is tuned on the same strategy trades it evaluates.
- Tactical execution improvements may not matter for daily/slow strategies but can dominate intraday/stat-arb claims.

## Transaction Cost / Capacity Treatment

This is directly a transaction-cost/execution paper. The library implication is to replace optimistic maker-fill assumptions with state-dependent fill probability, adverse-selection, opportunity-cost, and non-fill penalties, especially for high-turnover strategies.

## Strategy Ideas Extracted

Execution audit module for passive-order backtests:

1. Estimate or stress fill probability as an exponential function of quote distance.
2. Penalize expected adverse selection using order-flow imbalance or a proxy such as short-horizon signed volume / queue imbalance when available.
3. Add opportunity cost for non-execution and delayed execution.
4. Compare passive-fill strategy results against marketable-order, midpoint-no-fill, and conservative no-fill baselines.
5. Report sensitivity to quote distance, volatility, spread, and liquidity state.

## Connections to Existing Research

### Reinforces

- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]
- [[Signature-Based Optimal Execution for Statistical Arbitrage]]
- [[Order Splitting and Liquidity Replenishment for Square-Root Market Impact]]
- [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]]

### Contradicts / Weakens

Weakens backtests that assume passive limit orders fill at favorable prices without adverse selection, queue risk, or opportunity cost.

### Transfers Across Asset Classes or Domains

The execution lens transfers to equities, FX, futures, and crypto, but calibration must be venue-specific. For crypto, exchange API latency, maker rebates, and queue opacity should be added.

### Missing Validation or Method Supplied

Supplies a passive-execution cost model that can sit between flat spread assumptions and full L2 replay.

## Framework Potential

- Candidate framework: microstructure-conditioned execution realism.
- Linked notes: [[Liquidity-Based Audit of Algorithmic Trading Strategies]], [[Signature-Based Optimal Execution for Statistical Arbitrage]], [[Order Splitting and Liquidity Replenishment for Square-Root Market Impact]].
- Testable composite hypothesis: passive-fill assumptions explain a meaningful share of the gap between gross intraday alpha and deployable net returns.
- Minimum viable validation: add fill-distance/adverse-selection/opportunity-cost stress to a short-horizon backtest and compare against spread-only costs.
- What would falsify this connection? Conservative passive-fill stress does not change rankings or net utility versus simpler spread/slippage models for the strategy horizon being tested.

## Keep / Reject Decision

Keep as a foundational execution-cost note. It should update the standard backtest audit block but does not create a standalone alpha strategy.

## Related Notes

- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]
- [[Signature-Based Optimal Execution for Statistical Arbitrage]]
- [[Order Splitting and Liquidity Replenishment for Square-Root Market Impact]]
