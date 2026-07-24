---
type: source-note
source_kind: paper / empirical DeFi microstructure audit
asset_classes: [crypto, defi, market-microstructure, automated-market-makers]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-24"
tags: [quant-source, defi, amm-routing, execution-quality, gas-costs, sandwich-attacks]
concepts: [dex-routing-suboptimality, information-timely-routing, gas-aware-routing, stale-state-execution, sandwich-loss-attribution]
---

# DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution

## Citation / Link

Weiye Xi, Ciamac C. Moallemi, “Quantifying Sub-Optimality in Routing for Automated Market Makers,” arXiv:2607.20762v1, 2026-07-22. https://arxiv.org/abs/2607.20762v1

Comment: 21 pages; accepted at the 5th Workshop on Decentralized Finance (DeFi 2026), held with Financial Cryptography and Data Security 2026.

## Summary

The paper is a large-scale empirical audit of DEX routing quality using 2.98 million WETH-USDC swaps on Ethereum. It compares realized routes with three reproducible optimized benchmarks: support-constrained optimum (split quality conditional on used pools), full-venue optimum (value of broader pool access), and gas-aware full-venue optimum (routing value net of gas trade-offs). The abstract reports an average realized shortfall of 2.02 bps per trade, about $24 million in aggregate. Inefficiency is heterogeneous and heavy-tailed: small trades suffer higher percentage losses, while a few outliers dominate dollar shortfall. Information timeliness is central: optimizing on one-block-lagged AMM state materially raises shortfall and additional stale delays degrade execution. Sandwich attacks explain a significant fraction of routing sub-optimality.

For this library, the paper is primarily an execution-quality and venue-friction source, not a standalone alpha signal.

## Core Contribution

- Provides reproducible benchmark definitions for DEX routing quality instead of comparing realized swaps to vague “best price” claims.
- Separates split-quality, venue-access, gas-cost, stale-state, and sandwich-attack components of AMM execution loss.
- Quantifies that small trades may have high percentage friction even when aggregate dollar losses are concentrated in tail outliers.
- Reinforces that on-chain execution quality depends on block-state timeliness, MEV exposure, gas, pool access, and route splitting.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as empirical DeFi execution-quality evidence; foundational / retail-adaptable**.
- Retail adaptation: use as a transaction-cost and route-quality audit for any DEX-based crypto backtest or cross-venue strategy. Do not assume quoted AMM mid/prices are executable.
- Not directly tradable unless the user has reliable mempool/block-state data, private routing, MEV protection, and venue-specific execution control.

## Data / Backtest Requirements

Minimum local adaptation for DEX strategy research:

1. Swap/trade records with timestamp/block, token pair, realized route, pool states, gas paid, and transaction outcome.
2. Point-in-time AMM pool reserves/liquidity and fee tiers at decision block, not post-trade state.
3. Route optimizer benchmark with support-constrained, full-venue, and gas-aware variants.
4. Sandwich/MEV flags or at least proxy labels using surrounding transactions, slippage, and price impact.
5. Strategy backtest report fields: intended price, quoted route, realized route, gas, failed/canceled transactions, stale-state delay, and adverse execution.

## Leakage / Bias / Overfitting Concerns

- A backtest that uses execution-time or post-block pool state for a pre-trade decision can lookahead route quality.
- Gas costs and reverted transactions can dominate small-trade economics.
- MEV protection, private relay usage, aggregator version, and routing API behavior change over time.
- Heavy-tailed outliers mean average bps may not describe execution risk; use distributional/cvar-style diagnostics.

## Transaction Cost / Capacity Treatment

Transaction cost is the research object. Any DEX alpha or arbitrage test should include pool fees, gas, slippage, price impact, sandwich loss, stale-state loss, failed transactions, and route-suboptimality stress. Backtests should include both percentage and dollar shortfall because small and large trades fail differently.

## Strategy Ideas Extracted

- **Hypothesis:** DEX strategy edges that survive naive pool-fee assumptions may disappear once information-timely, gas-aware routing shortfall and MEV exposure are charged.
- **Asset class/universe:** Ethereum AMM swaps, initially WETH-USDC or similarly liquid pairs.
- **Signal definition:** not an alpha signal; route-quality audit variables include stale-block delay, realized-vs-support-constrained shortfall, gas-aware full-venue shortfall, sandwich flag, trade size bucket, and pool-access breadth.
- **Backtest design:** descriptive audit first; then stress any DEX strategy by adding route-quality cost distributions conditioned on size, gas regime, venue, and MEV exposure.
- **Validation priority:** medium/high if coding crypto/DeFi execution; otherwise foundational reference.

## Connections to Existing Research

### Reinforces

- [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]]: AMM design choices are not just pricing details; they affect realized liquidity and execution quality.
- [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]]: venue-quality diagnostics should be part of crypto execution filters.
- [[Risk-Based Auto-Deleveraging]]: crypto venue mechanics can dominate realized PnL and tail risk.
- [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]]: AMM economics should be evaluated with mechanism-specific loss accounting rather than generic spread assumptions.

### Framework Potential

- Candidate framework: Microstructure-conditioned decay and liquidity-state validation.
- Testable composite hypothesis: crypto/DeFi strategies need venue-state and execution-route diagnostics because stale state, MEV, gas, and route sub-optimality can erase gross alpha even when signal logic is valid.
- Minimum viable validation: add route-quality and venue-quality cost fields to any DEX backtest before evaluating alpha.
- What would falsify this framework? Route sub-optimality and MEV proxies add no explanatory power for realized execution shortfall after simple fee/gas/size controls.

## Keep / Reject Decision

Keep as a high-value foundational execution-quality source. Do not promote to coding queue as a standalone strategy; fold into the standard cost/regime/liquidity/decision audit block when DeFi execution is in scope.
