---
type: source-note
source_kind: paper / AMM portfolio-product and band-rebalancing methodology
asset_classes: [crypto, DeFi, automated-market-makers, portfolio, market-microstructure]
implementation_class: foundational / retail-adaptable as simulator and cost-model input
importance: medium
last_reviewed: "2026-08-05"
tags: [quant-source, crypto, defi, amm, portfolio-construction, rebalancing]
concepts: [amm-portfolio-products, verifiable-mandates, band-rebalancing, arbitrage-only-rebalancing]
---

# AMM Mandate Portfolios - Verifiable Band Rebalancing

## Citation / Link

Zachary Feinstein, Ionut Florescu, Sean O'Leary, “Mandate without Managers: Automated Market Makers as Verifiable Portfolio Products,” arXiv:2608.02917v1, submitted 2026-08-03. https://arxiv.org/abs/2608.02917v1

Semantic Scholar lookup returned HTTP 429 during this run, so citation counts were not recorded.

## Summary

The paper reframes geometric-mean automated market makers (G3Ms), such as Balancer-style pools, as verifiable portfolio products rather than only decentralized exchanges. A multi-asset fee structure lets competitive arbitrage implement a band-rebalancing strategy with ex ante bounded mis-weighting, so mandate compliance can be checked from observable pool holdings. The abstract reports historical simulations against VBIAX, EQL, and EDOW in which G3M portfolios outperform incumbent funds on annualized return and tracking error for some fee ranges, using arbitrage-only order flow.

For this library, the source is not direct LP alpha. Its useful contribution is a portfolio/rebalancing simulator design: AMM fee bands, arbitrage flow, gas/MEV, and external-price latency can change whether an apparent rebalance or LP edge is real.

## Core Contribution

- Treats AMM invariants as programmatic portfolio mandates with observable compliance.
- Links multi-asset fees to arbitrage-driven band rebalancing and bounded mis-weighting.
- Compares simulated AMM portfolio products against realized fund benchmarks.
- Supplies a DeFi-specific bridge between portfolio rebalancing, execution cost, and verifiable holdings.

## Practical Relevance

- Classification: **Plausible-to-evidence-backed at abstract level as AMM portfolio/rebalancing methodology; foundational / retail-adaptable as simulator and cost-model input**.
- Retail adaptation is a simulation/audit object, not “buy AMM LP shares blindly.”
- Useful for DeFi/AMM execution and portfolio research where fixed rebalancing schedules, fixed fees, or frictionless arbitrage are unrealistic.

## Strategy / Backtest Translation

- Hypothesis: AMM/G3M band-rebalancing policies can replicate target-weight portfolio mandates with lower explicit manager intervention, but net investor utility depends on fee range, arbitrage latency, gas, MEV/sandwich risk, LP inventory exposure, and tracking-error objective.
- Minimum viable test: simulate a two- to multi-asset constant-function pool on liquid assets with external reference prices; compare against calendar rebalancing, threshold rebalancing, equal weight/risk parity, and buy-and-hold after gas, pool fees, adverse selection, and stale-state assumptions.
- Data needed: historical asset prices at daily/intraday frequency, fee schedule, pool invariant/weights, gas/MEV assumptions, arbitrage latency, trade-size constraints, and benchmark fund/index weights.
- Baselines: buy-and-hold, calendar monthly/quarterly rebalance, fixed threshold rebalance, CEX execution with explicit spread/slippage, and fixed-fee AMM simulation.

## Leakage / Bias / Overfitting Concerns

- Fee ranges that outperform historical benchmarks can be selected ex post.
- Arbitrage-only order flow omits noise flow, LP entry/exit timing, real gas, MEV, and failed transactions.
- Historical fund comparisons may not match mandate, tax, leverage, or investability constraints.
- Pool holdings are observable, but external reference prices and arbitrage latency remain implementation assumptions.

## Transaction Cost / Capacity Treatment

AMM portfolio results must include gas, failed transactions, MEV/sandwich exposure, stale block state, route support, pool depth, arbitrage latency, and LP impermanent-loss/inventory transfer. For retail, the main question is whether an AMM-style rebalance rule improves net portfolio outcomes versus transparent threshold rebalancing, not whether the protocol can prove mandate compliance.

## Connections to Existing Research

### Reinforces

- [[Optimal Dynamic Fees in Automated Market Makers]] — both sources make AMM fee policy an endogenous state variable, not a fixed cost.
- [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]] — AMM portfolio simulations need route/gas/stale-state realism before claiming edge.

### Contradicts / Weakens

Weakens any DeFi backtest that assumes frictionless, instantaneous arbitrage or fixed rebalance costs inside AMM pools.

### Transfers Across Asset Classes or Domains

Transfers threshold/band rebalancing logic from classical portfolio construction into AMM/G3M design, but only as a simulation benchmark until live execution costs are modeled.

### Missing Validation or Method Supplied

Supplies a verifiable-holdings and bounded-misweight diagnostic for AMM portfolio products.

## Framework Potential

- Candidate framework: AMM execution and portfolio-mandate validation.
- Linked notes: [[Optimal Dynamic Fees in Automated Market Makers]], [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]].
- Testable composite hypothesis: AMM/G3M portfolio products should be judged against simple threshold rebalancing after gas, MEV, stale-state, route, and arbitrage-latency costs, not only against gross fund returns.
- Minimum viable validation: historical simulation with fixed-fee and dynamic-fee cases, arbitrage latency buckets, gas/MEV stress, and mandate-tracking-error versus net-return tradeoff.
- What would falsify this connection? If simple threshold/calendar rebalancing dominates after realistic costs, or if fee bands only work in ex post selected ranges.

## Keep / Reject Decision

Keep as a foundational DeFi/portfolio-source note. Add a registry row as a simulation/audit candidate; do not promote to coding queue until a specific AMM dataset and cost model are chosen.

## Related Notes

- [[Optimal Dynamic Fees in Automated Market Makers]]
- [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]]
