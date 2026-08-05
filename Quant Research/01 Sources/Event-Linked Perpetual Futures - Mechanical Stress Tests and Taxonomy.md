---
type: source-note
source_kind: paper series / event-linked perpetual futures design and stress-test methodology
asset_classes: [prediction-markets, crypto, derivatives, market-microstructure, risk-management]
implementation_class: foundational
importance: medium
last_reviewed: "2026-07-30"
tags: [quant-source, prediction-markets, event-linked-perpetuals, leverage, market-design, stress-testing]
concepts: [event-linked-perps, binary-settlement-shortfall, funding-trilemma, event-market-manipulation, contract-taxonomy]
---

# Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy

## Citation / Link

Maksym Nechepurenko, “Resolution-Aware Perpetual Futures on Binary Prediction Markets: Failure Modes and Mechanical Stress Tests Using Polymarket Data,” arXiv:2605.10400v2, updated 2026-07-29. https://arxiv.org/abs/2605.10400v2

Maksym Nechepurenko, “A Taxonomy of Event-Linked Perpetual Futures: Design Axes, Failure Modes, and Empirical Evaluability,” arXiv:2605.10428v2, updated 2026-07-29. https://arxiv.org/abs/2605.10428v2

Maksym Nechepurenko, “Manipulation, Informed Trading, and Regulation in Leveraged Event-Linked Markets,” arXiv:2605.10486v2, updated 2026-07-29. https://arxiv.org/abs/2605.10486v2

Comments note major r2.1.0 revisions and code at https://github.com/ForesightFlow/event-linked-perps for the taxonomy/manipulation papers. Semantic Scholar lookup during this run returned 0 citations for arXiv:2605.10486; other lookups were rate-limited.

## Summary

This revised paper series studies whether perpetual-futures mechanics port cleanly to binary or event-linked claims. The resolution-aware paper derives a terminal shortfall for leveraged longs when a binary claim resolves adversely and identifies a funding trilemma near probability boundaries; its Polymarket mechanical stress tests produce mostly negative/non-portability evidence rather than a trading edge. The taxonomy paper formalizes event-linked perpetual design axes — underlying geometry, temporal structure, settlement structure, and venue-oracle composition — and proves narrow failure-mode results. The manipulation paper separates market-price manipulation, real-world outcome manipulation, resolution-process manipulation, and informed trading, arguing that leverage can amplify fixed-cost influence opportunities but that price impact, detection, and position limits can reverse the economics.

For this library, the series is a market-design and risk-control reference for prediction-market derivatives. It should prevent naive extrapolation from crypto perpetuals to bounded event claims.

## Core Contribution

- Shows that binary/event-linked settlement creates mechanical shortfall and funding problems not present in ordinary perpetuals.
- Provides a contract taxonomy that can be used as metadata before pooling prediction-market instruments.
- Separates manipulation and informed-trading channels instead of treating all event-market abnormal behavior as one effect.
- Supplies mechanical stress-test code/design, but no new empirical alpha claim in the revised abstracts.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as market-design/stress-test methodology; foundational**.
- Institutional/venue relevance is high; retail trading relevance is indirect.
- Use to define no-trade filters and metadata, not to trade event-linked leverage products.

## Methods and Data

- Analytical terminal-equity and funding-mechanism derivations for binary/event-linked claims.
- Mechanical stress tests on observed Polymarket paths from 21-27 April 2026 in arXiv:2605.10400v2.
- Contract taxonomy by payoff geometry, temporal structure, settlement, and venue/oracle composition.
- Manipulation/informed-trading channel model with fixed and variable cost components.

## Leakage / Bias / Overfitting Concerns

- Mechanical stress tests are path- and design-specific; they should not be overgeneralized to all prediction markets.
- Revisions explicitly state no new empirical run for the updated versions.
- Venue rules, collateralization, oracle/resolution process, and regulation can change quickly.
- Any empirical test must freeze contract metadata before analysis.

## Transaction Cost / Capacity Treatment

The series is about contract mechanics, not execution alpha. For any strategy, include spreads, fees, collateral/margin, liquidation/top-up rules, resolution disputes, oracle delays, and platform-specific constraints.

## Strategy Ideas Extracted

No positive strategy. Add a no-trade/design gate: avoid or separately bucket event-linked leverage products near boundaries, conditional ratios near zero denominators, final-leg spreads, and contracts with weak resolution/oracle safeguards. Use taxonomy labels before studying volatility, settlement manipulation, or market-making.

## Connections to Existing Research

### Reinforces

- [[SoK - Market Microstructure for Decentralized Prediction Markets]] — adds contract-level taxonomy and leverage-specific failure modes.
- [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]] — extends market-making design risk to leveraged/event-linked derivatives.
- [[Settlement Manipulation in Prediction Markets]] — separates resolution-process manipulation from market-price manipulation and informed trading.
- [[OpenMarket Synchronized Polymarket-Binance Dataset]] — potential dataset context for testing some event-linked design metadata, where applicable.

### Contradicts / Weakens

Weakens any assumption that perpetual-futures funding mechanics transfer directly to binary event claims.

### Transfers Across Asset Classes or Domains

Transfers to options and crypto derivatives as a reminder that payoff support, settlement, and collateralization define feasible leverage and failure modes.

### Missing Validation or Method Supplied

Supplies contract metadata fields and mechanical stress-test gates for prediction-market and event-linked derivative datasets.

## Framework Potential

- Candidate framework: event-linked market design and leverage-risk taxonomy.
- Linked notes: [[SoK - Market Microstructure for Decentralized Prediction Markets]], [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]], [[Settlement Manipulation in Prediction Markets]], [[OpenMarket Synchronized Polymarket-Binance Dataset]].
- Testable composite hypothesis: prediction-market volatility/settlement/manipulation findings are conditional on payoff geometry, settlement/oracle design, leverage/collateral rules, and probability-boundary state.
- Minimum viable validation: build contract metadata and mechanical feasibility labels before fitting return/volatility/manipulation models.
- What would falsify this connection? Similar empirical behavior across design buckets after controlling for liquidity and event category, or no incremental explanatory value from taxonomy labels.

## Keep / Reject Decision

Keep as foundational market-design and no-trade-filter research. Do not add to coding queue except as metadata for future prediction-market dataset work.

## Related Notes

- [[SoK - Market Microstructure for Decentralized Prediction Markets]]
- [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]]
- [[Settlement Manipulation in Prediction Markets]]
- [[OpenMarket Synchronized Polymarket-Binance Dataset]]
