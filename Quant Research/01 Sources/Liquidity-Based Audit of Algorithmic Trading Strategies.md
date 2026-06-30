---
type: source-note
source_kind: paper
asset_classes: [equities, execution, risk]
implementation_class: foundational
importance: medium
last_reviewed: "2026-06-30"
tags: [quant-source, liquidity, transaction-costs, execution, audit, market-impact]
concepts: [liquidity-demand, roll-spread, adverse-selection, fire-sale-externality]
---

# Liquidity-Based Audit of Algorithmic Trading Strategies

## Citation / Link

Irene Aldridge, “Liquidity-Based Audit of Algorithmic Trading Strategies,” arXiv:2606.29018v1, 2026-06-27. https://arxiv.org/abs/2606.29018v1

## Summary

The paper proposes an observable statistic for classifying an algorithmic strategy as a net liquidity consumer or liquidity provider from its trade and price history, without knowing the underlying signal or optimization problem. The abstract links this statistic to multi-period regret decomposition, Kyle/Roll microstructure intuition, and CRSP equity calibration across 2016–2025.

## Core Contribution

- Converts liquidity consumption into a strategy audit diagnostic rather than a vague execution label.
- Connects strategy-level trading history to implied illiquidity and regret.
- Highlights a portfolio-of-strategies externality: correlated liquidity demand can scale welfare loss nonlinearly.

## Practical Relevance

- Classification: **foundational / retail-adaptable as a diagnostic**.
- Not alpha. Useful for backtest quality control and strategy portfolio construction.
- Retail adaptation: compute simplified liquidity-demand proxies from signed turnover, return impact, spread proxies, and execution timing.

## Methods and Data

Abstract mentions CRSP equities from 2016–2025, AR(1) cost process, Roll-implied spread, and an estimator computable in O(Tnd). Local use can start simpler:

- daily strategy trades/weights,
- asset returns and spread proxies,
- turnover and participation estimates,
- correlation of liquidity demand across strategies.

## Leakage / Bias / Overfitting Concerns

- A diagnostic based on realized trade/price history should be applied out-of-sample and not optimized directly without a holdout.
- Signed trade reconstruction can be noisy for backtests with assumed fills.
- Daily proxies may miss intraday liquidity demand, especially for options and crypto.

## Transaction Cost / Capacity Treatment

This is primarily a transaction-cost/capacity reference. Use it to flag strategies that look profitable only because they implicitly demand liquidity during favorable backtest marks but would pay spread/impact in live execution.

## Strategy Ideas Extracted

No direct trading strategy. Add a liquidity-audit layer to future backtests: classify each strategy as liquidity consumer/provider, estimate spread/impact penalty, and measure whether multiple strategies crowd into the same liquidity-demand episodes.

## Connections to Existing Research

### Reinforces

- Square-root market-impact reference in [[2026-06-28 Daily Quant Research Review]].
- [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]]: evaluate models by downstream portfolio consequences, including liquidity and turnover.

### Contradicts / Weakens

- Weakens high-turnover strategies reported without explicit liquidity-demand and impact diagnostics.

### Transfers Across Asset Classes or Domains

- Applies to crypto and options backtests via spread/impact proxies, though direct adaptation needs asset-specific microstructure treatment.

### Missing Validation or Method Supplied

- Supplies a candidate audit metric for the research library’s backtest-review checklist.

## Framework Potential

- Candidate framework: cost-aware strategy diagnostics.
- Linked notes: [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]], square-root impact reference, [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]].
- Testable composite hypothesis: a strategy’s apparent edge should be discounted by observable liquidity-demand intensity and correlation with other strategies.
- Minimum viable validation: compute liquidity-consumption proxies for existing backtests and check whether net returns survive higher costs in crowded liquidity-demand states.
- What would falsify this connection? Liquidity-demand classification is unstable or uninformative once realistic spread/impact models are already included.

## Keep / Reject Decision

**Keep** as a foundational execution-cost and backtest-audit method.

## Related Notes

- [[2026-06-30 0044 Daily Quant Research Review]]
