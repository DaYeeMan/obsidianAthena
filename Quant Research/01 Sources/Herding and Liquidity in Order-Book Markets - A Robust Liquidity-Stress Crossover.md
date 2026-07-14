---
type: source-note
source_kind: paper
asset_classes: [market-microstructure, liquidity, agent-based-models, execution-risk]
implementation_class: foundational
importance: medium
last_reviewed: "2026-07-13"
tags: [quant-source, market-microstructure, liquidity-stress, herding, order-book, agent-based-models]
concepts: [liquidity-stress-crossover, herding-layer, bouchaud-phase-diagram, one-sided-book]
---

# Herding and Liquidity in Order-Book Markets - A Robust Liquidity-Stress Crossover

## Citation / Link

Jan Novotny, “Herding and Liquidity in Order-Book Markets. I. A Robust Liquidity-Stress Crossover and its Reflexive Mechanism,” arXiv:2607.08907v1, 2026-07-09. https://arxiv.org/abs/2607.08907v1

## Summary

The paper uses Bouchaud's phase-diagram method on a continuous-double-auction order-book model with fundamental-anchored zero-intelligence liquidity and a mid-anchored chartist herding layer. The abstract reports a robust liquidity-stress crossover: the fraction of one-sided-book events rises under high herder fraction and herding strength, disappears in scrambled-sign null cells, and remains robust under order-flow-imbalance rules and momentum-window changes. The paper is simulation/model evidence, not a direct alpha test.

## Core Contribution

- Treats liquidity dry-ups as a robust phase-diagram feature rather than a one-parameter simulation artifact.
- Gives a microstructural mechanism for reflexive herding-driven liquidity stress.
- Provides a stress-test lens for strategies that consume liquidity during crowded momentum/order-flow states.
- Reinforces that volume/order-flow signals can be dangerous when they coincide with one-sided-book or liquidity-tail states.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as simulation methodology; foundational**.
- Not a tradable signal and not directly retail-practical as alpha.
- Useful for backtest stress design: when signal crowding/herding proxies are high, slippage and fill risk should be stressed more aggressively rather than treated as constant.
- Retail adaptation can use proxies such as spread widening, depth depletion, order-flow imbalance, volatility bursts, and failed fills if full order-book state is unavailable.

## Methods and Data

Abstract-level details:

- continuous-double-auction order-book model,
- fundamental-anchored zero-intelligence liquidity,
- mid-anchored chartist herding layer,
- herder fraction and herding strength grid,
- scrambled-sign nulls,
- one-sided-book order parameter,
- robustness checks across order-flow-imbalance rule and momentum-window horizon.

Minimum local adaptation:

1. Add a liquidity-stress flag to backtests using spread/depth/volume/volatility/order-flow proxies.
2. Test whether strategy PnL, turnover, and slippage estimates deteriorate in high-herding/high-imbalance states.
3. Stress fills and market impact more heavily during one-sided-book proxy states.
4. Avoid interpreting volume bursts as informed flow without checking liquidity-stress state.

## Risks / Failure Modes

- Agent-based simulation results may not identify a live-market threshold.
- Retail data may only approximate one-sided-book and herding states.
- Parameter grids can look robust while omitting key market-maker, latency, or venue-fragmentation mechanics.
- Stress diagnostics may become too conservative if not tied to realized slippage or opportunity cost.

## Connections to Existing Research

### Reinforces

- Microstructure-conditioned decay and liquidity-state validation by adding a liquidity-stress crossover mechanism.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]] because order-flow/volume bursts can reflect liquidity stress rather than information.
- [[Robustness in Sequential Decision Making under Evolving Uncertainty]] by warning that action robustness should be state-dependent in illiquid/herding regimes.

## Validation Priority

**Medium/Reference**. Add to the backtest audit framework as a stress-scenario source; do not code as standalone alpha.
