---
type: source-note
source_kind: paper / AMM dynamic-fee control theory
asset_classes: [crypto, DeFi, automated-market-makers, market-microstructure]
implementation_class: foundational / retail-adaptable as simulator and cost-model input
importance: medium
last_reviewed: "2026-08-01"
tags: [quant-source, crypto, defi, amm, dynamic-fees, market-microstructure]
concepts: [dynamic-amm-fees, inventory-sensitive-fees, arbitrage-deterrence, noise-trader-attraction]
---

# Optimal Dynamic Fees in Automated Market Makers

## Citation / Link

Leonardo Baggiani, Martin Herdegen, Leandro Sánchez-Betancourt, “Optimal Dynamic Fees in Automated Market Makers,” arXiv:2506.02869v3, updated 2026-07-30. https://arxiv.org/abs/2506.02869v3

Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper studies optimal dynamic trader-facing fees in a constant-function automated market maker. The abstract reports approximate closed-form solutions to the control problem and identifies two fee regimes: raising fees to deter arbitrageurs, and lowering fees to increase volatility/noise-trader participation. A practical approximation is a fee rule that is linear in AMM inventory and sensitive to changes in the external price.

For this library, the paper is not direct LP or trading alpha. It is a mechanism reference for DeFi execution and AMM market-design simulations: quoted pool states and constant-fee assumptions can be materially wrong when fees react to inventory and external-price moves.

## Core Contribution

- Formalizes trader-facing dynamic fees as an optimal-control problem for AMMs.
- Separates arbitrage-deterrence and noise-liquidity-attraction fee regimes.
- Suggests an implementable approximation: inventory-sensitive and external-price-sensitive linear dynamic fees.
- Supplies a theoretical complement to empirical AMM protocol-fee and DEX-routing source notes already in the library.

## Practical Relevance

- Classification: **Plausible-to-evidence-backed at abstract level as AMM market-design theory; foundational / retail-adaptable as simulator and cost-model input**.
- Retail adaptation is not “trade the fee rule.” The useful adaptation is to stress-test DeFi strategies under dynamic trader-facing fee schedules, not only fixed pool fees.
- Candidate implementation object: add a dynamic-fee scenario to AMM execution simulations and LP backtests, with inventory, external-price move, gas, stale-state, route-support, failed-transaction, and MEV/sandwich cost fields.

## Methods and Data

The abstract is theoretical/analytical. It does not validate a tradable live strategy in the library’s scope. A local test would need historical pool state, external reference prices, gas, pool fee settings, swaps, liquidity changes, and simulated execution paths under fixed-fee versus dynamic-fee counterfactuals.

## Leakage / Bias / Overfitting Concerns

- Control-model assumptions can dominate the optimal fee shape.
- External-price signals can be stale, manipulable, or unavailable at the same time as the AMM transaction decision.
- Simulated noise-trader/arbitrageur decomposition may not transfer across AMM designs, chains, or regimes.
- Dynamic fee tuning can overfit a period’s volatility/liquidity mix.

## Transaction Cost / Capacity Treatment

Dynamic fees are themselves a transaction-cost channel. Any DeFi backtest using this idea must include gas, priority fees, failed transactions, slippage, MEV/sandwich risk, route splitting, stale block state, and liquidity depth. LP/capacity analysis should include impermanent loss/LVR and inventory exposure, not only fee revenue.

## Strategy Ideas Extracted

1. **Execution-cost audit:** compare fixed-fee AMM execution assumptions against inventory/external-price-sensitive dynamic-fee stress.
2. **LP simulator upgrade:** evaluate whether dynamic-fee regimes change LP PnL distribution after LVR, inventory risk, and gas.
3. **No-trade gate:** skip DeFi trades when dynamic-fee and stale-state stress turns quoted edge negative.

## Connections to Existing Research

### Reinforces

- [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]]: complements LP take-rate event studies by addressing trader-facing dynamic fees that protocol-fee designs do not identify.
- [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]]: strengthens the requirement to model route-specific fees, gas, stale-state, and execution-time pool conditions.
- [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]]: reinforces the broader market-design lesson that AMM spread/fee capture is mechanism-dependent rather than a generic premium.

### Contradicts / Weakens

- Weakens any DeFi strategy backtest that assumes a static fixed fee, instantaneous external-price alignment, or costless arbitrage correction.

### Transfers Across Asset Classes or Domains

- Transfers an optimal-control fee-design lens into execution-cost stress testing. The trading analogue is not alpha; it is a better fill/cost model.

### Missing Validation or Method Supplied

- Supplies a candidate dynamic-fee scenario for AMM/DEX backtest audit modules.

## Framework Potential

- Candidate framework: microstructure-conditioned decay and liquidity-state validation.
- Linked notes: [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]], [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]], [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]].
- Testable composite hypothesis: DeFi strategy PnL rankings are unstable when AMM fees respond to inventory and external-price moves, especially during volatile/gas-congested states.
- Minimum viable validation: replay historical swaps or simulated trades under fixed fee, dynamic inventory-sensitive fee, dynamic external-price-sensitive fee, and stressed gas/MEV assumptions.
- What would falsify this connection? Dynamic-fee stress does not change execution cost, trade selection, LP PnL, or strategy ranking relative to fixed-fee assumptions across realistic regimes.

## Keep / Reject Decision

Keep as a foundational DeFi market-structure and execution-cost reference. Do not promote to the coding-ready queue until the DEX/AMM execution-audit module has data and fixed-fee baselines.

## Related Notes

- [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]]
- [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]]
- [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]]
