---
type: source-note
source_kind: paper
asset_classes: [equities, market-microstructure, execution, transaction-costs]
implementation_class: foundational
importance: medium
last_reviewed: "2026-07-07"
tags: [quant-source, market-impact, square-root-law, execution, order-splitting, liquidity-replenishment]
concepts: [square-root-impact, metaorders, liquidity-replenishment, capacity, slippage]
---

# Order Splitting and Liquidity Replenishment for Square-Root Market Impact

## Citation / Link

Yang Zhou, Jianwen Chen, Ruipeng Wei, “Order Splitting and Liquidity Replenishment Are Jointly Necessary for the Square-Root Law of Market Impact,” arXiv:2607.04280v1, 2026-07-05. https://arxiv.org/abs/2607.04280v1

## Summary

The paper uses a calibrated heterogeneous-agent limit-order-book simulation to test mechanisms proposed for the square-root law of market impact. The abstract reports that the model reproduces a square-root exponent near the Tokyo Stock Exchange benchmark, while several classic theoretical predictions fail to match per-stock exponents on the same simulated data. Counterfactual ablations identify order splitting and liquidity replenishment by market makers as jointly necessary in this model: removing either component materially changes the exponent, while perturbing momentum trading, price limits, splitting rules, or background liquidity has smaller effects.

## Core Contribution

- Moves the square-root law from a generic cost-model assumption toward a mechanism-sensitive execution hypothesis.
- Emphasizes the joint role of metaorder splitting and replenishing liquidity rather than the visible book shape or metaorder-size tail alone.
- Provides an ablation-style way to think about when square-root impact assumptions may fail.

## Practical Relevance

- Classification: **Plausible-to-evidence-backed as execution-cost methodology / foundational** at abstract level.
- Not an alpha signal; it improves slippage, capacity, and participation-rate stress testing.
- Retail use is indirect: most retail backtests cannot estimate metaorders, but can still stress slippage using participation, ADV, spread, volatility, and liquidity-state proxies.
- Helps avoid treating square-root impact as a universal constant independent of execution schedule and liquidity replenishment state.

## Methods and Data

Abstract-level details:

- minimal limit-order-book model with heterogeneous interacting agents,
- calibration against a Tokyo Stock Exchange benchmark,
- 2000 independently parameterized simulated stocks,
- comparison of GGPS, FGLW, and LOB-walking predictions,
- counterfactual ablations of order splitting and liquidity replenishment.

## Leakage / Bias / Overfitting Concerns

- Simulation results depend on the agent model and calibration target; live-market empirical validation is still required before using exact exponents.
- Retail daily data cannot observe replenishment directly; proxies are noisy.
- Capacity rules can be falsely precise if they ignore spread, volatility state, execution horizon, and venue fragmentation.

## Local Use / Backtest Translation

Minimum viable execution-cost stress:

1. Keep a square-root participation penalty as a capacity stress, not a precise point estimate.
2. Report sensitivity across impact exponent and coefficient assumptions.
3. Condition cost stress by liquidity state: ADV, spread proxy, volatility, turnover, and available execution horizon.
4. If a strategy trades predictably or in crowded windows, assume worse replenishment and higher slippage.
5. For crypto/DEX venues, use venue-specific depth and taker-fee stress rather than importing equity square-root parameters.

## Connections to Existing Research

### Reinforces

- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]: large trades and impact depend on liquidity-demand and replenishment states.
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]: backtests should report liquidity demand and cost stress, not just turnover.
- [[Signature-Based Optimal Execution for Statistical Arbitrage]]: execution path can dominate signal profitability.

### Framework Potential

- Candidate framework: Microstructure-conditioned decay and liquidity-state validation.
- Testable composite hypothesis: strategy profitability should be stress-tested under worse replenishment states, especially around crowded rebalances, settlement windows, and high-volatility periods.
- Minimum viable backtest: add square-root/linear/spread-based cost scenarios and liquidity-state buckets to the standard backtest audit block.
- Falsification: cost stress does not alter rankings or go/no-go decisions across realistic parameter ranges.
