---
type: source-note
source_kind: paper
asset_classes: [equities, statistical-arbitrage, execution]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: "2026-07-01"
tags: [quant-source, statistical-arbitrage, optimal-execution, path-signatures, transaction-costs]
concepts: [path-dependent-signals, execution-policy, temporary-impact, dollar-neutrality, return-on-turnover]
---

# Signature-Based Optimal Execution for Statistical Arbitrage

## Citation / Link

Gianmarco Morbelli, Sven Karbach, Mike Derksen, “Signature-Based Optimal Execution for Statistical Arbitrage with Path-Dependent Trading Signals,” arXiv:2606.31387v1, 2026-06-30. https://arxiv.org/abs/2606.31387v1

## Summary

The paper proposes a signature-based optimal-execution framework for statistical arbitrage strategies with path-dependent predictive signals. The alpha process and trading speed are represented on the same truncated signature basis, reducing the restricted execution problem to a finite-dimensional concave quadratic program. The abstract reports synthetic mean-reverting spread experiments and a historical equity pairs-trading backtest where the fitted signature policy improves return on turnover versus a classical z-score threshold benchmark.

## Core Contribution

- Treats signal history and execution speed jointly rather than using a signal threshold followed by naive execution.
- Incorporates temporary impact, inventory exposure, terminal liquidation, and approximate dollar neutrality.
- Evaluates execution by return on turnover, which is closer to implementability than raw prediction accuracy.

## Practical Relevance

- Classification: **Plausible but untested / foundational-retail-adaptable**.
- The full signature/QP framework is more complex than most retail stat-arb needs, but the principle is useful: compare signal-triggered entry/exit rules against cost-aware execution policies.
- Retail adaptation should start with simple pairs/stat-arb baselines before path signatures: z-score spread, volatility-scaled position, turnover cap, spread/slippage model, and walk-forward thresholds.

## Methods and Data

Abstract-level details:

- truncated signatures of time-augmented market paths,
- signature-linear trading speeds,
- finite-dimensional concave quadratic program,
- synthetic mean-reverting log-spread model,
- historical equity pairs-trading backtest,
- benchmark: classical z-score threshold strategy.

## Leakage / Bias / Overfitting Concerns

- Pair selection can leak future cointegration/stability if not done walk-forward.
- Signature features can overfit path shapes in small samples.
- Reported accounting outperformance may not survive realistic borrow, financing, market-impact, and short-sale constraints.
- Need simple baselines: z-score, Kalman hedge ratio, vol-scaled mean reversion, and no-trade bands.

## Transaction Cost / Capacity Treatment

Execution and turnover are central. Any local use should include bid/ask spreads, commissions, slippage, borrow/short fees, turnover caps, participation limits, and robustness to wider spread assumptions.

## Strategy Ideas Extracted

No immediate coding promotion. Use as an execution-design reference for any future pairs/stat-arb strategy: optimize the path from signal to trade under costs, not just the signal.

## Keep / Reject Decision

**Keep** as a medium-priority foundational execution reference. It is not yet a coding target because local pairs universe/data/cost assumptions are unspecified.

## Connections to Existing Research

### Reinforces

- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]: execution quality and liquidity demand determine whether a statistical edge survives.
- Cost-aware decision-process diagnostics: improves the decision/process layer between alpha signal and realized PnL.

### Framework Potential

Adds a stat-arb example to the cost-aware diagnostics framework: signal quality must be judged jointly with turnover, inventory, liquidation, and temporary impact.
