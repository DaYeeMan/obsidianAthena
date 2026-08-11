---
type: source-note
source_kind: paper / decentralized-exchange trader-identity return-predictability evidence
asset_classes: [crypto, decentralized-exchange, market-microstructure, return-prediction]
implementation_class: foundational / institutional-only as written / retail-adaptable as public-wallet-flow diagnostic
importance: high
last_reviewed: "2026-08-07"
tags: [quant-source, crypto, dex, wallet-identity, adverse-selection, return-predictability, market-microstructure]
concepts: [public-trader-identity, wallet-informedness, pseudonymous-counterparty-history, adverse-selection-state]
---

# Public Trader Identity - Adverse Selection and Return Predictability

## Citation / Link

Daojing Zhai, “Public Trader Identity: Adverse Selection and Return Predictability,” arXiv:2608.04373v2, submitted 2026-08-05 and updated 2026-08-06. https://arxiv.org/abs/2608.04373v2

Comment from arXiv metadata: 40 pages, 8 figures, 15 tables. Semantic Scholar lookup returned HTTP 429 during the 2026-08-06 run and again for this ID during the 2026-08-07 run, so citation counts were not recorded.

## 2026-08-07 Version Maintenance

The 2026-08-07 arXiv validation surfaced v2. The directly validated abstract preserves the same core claims and metrics: 17.1 billion messages, 14.3 million aggressive orders, 147,113 wallets, $84.3 billion taker notional, adjacent ten-day wallet-informativeness rank correlation of 0.52, one-second return R2 of 12.31%, 13.2% gain with t = 9.2, and 1.6x the largest activity-matched placebo cohort. No new coding-ready rule, data access path, or cost model was supplied by the abstract, so the registry and coding queue remain conservative.

## Summary

The paper studies a decentralized exchange where each order, cancellation, rejection, and fill carries a persistent pseudonymous wallet address. It reconstructs a full-depth limit order book from 17.1 billion messages and 14.3 million aggressive orders across 147,113 wallets and $84.3 billion in taker notional. The abstract reports that post-trade informativeness is persistent at the wallet level: ranking wallets by subsequent price movement over ten days carries into the next ten days with rank correlation of 0.52. Adding identity information to prices, quotes, and anonymous order-flow features improves one-second out-of-sample return R2 to 12.31%, a 13.2% gain with t = 9.2, and the identity increment is larger at realized trades than at regularly sampled moments.

For this library, the useful claim is not “copy top wallets blindly.” It is that public identity can be a microstructure state variable when wallet histories are observable, but implementation must confront latency, venue rules, adverse selection, fees, and severe crowding/decay if identifiers become widely used.

## Core Contribution

- Converts public pseudonymous trader identity into a measurable adverse-selection / informed-flow variable.
- Shows persistence of wallet-level post-trade informativeness across adjacent windows at abstract level.
- Compares identity features against anonymous price, quote, and order-flow benchmarks.
- Reinforces the broader lesson that participant identity and attribution conventions can dominate short-horizon predictability in transparent crypto venues.

## Practical Relevance

- Classification: **Evidence-backed at abstract level; foundational / institutional-only as written / retail-adaptable as diagnostic**.
- Institutional-only as written because full-depth message reconstruction at scale, one-second response, venue-specific matching semantics, and reliable wallet attribution are demanding.
- Retail-adaptable proxy: for public DEX or prediction-market datasets, bucket aggressive flow by historically positive/negative wallet post-trade impact, then test as a state variable rather than a standalone signal.

## Methods and Data

- Full-depth LOB reconstruction from a decentralized exchange.
- Persistent wallet identifiers linked to orders, cancellations, rejections, and fills.
- Ten-day ranking and next-ten-day persistence tests.
- One-second return prediction compared with anonymous benchmark features and activity-matched placebo cohorts.

## Leakage / Bias / Overfitting Concerns

- Wallet rankings must be formed strictly before the prediction window.
- Wallet identities can be split, rotated, or sybil-manipulated after publication.
- One venue’s transparency and matching engine may not transfer to CEXs, AMMs, or prediction markets.
- Pooled R2 can hide tails, adverse fills, or profitability concentration in inaccessible latency regimes.

## Transaction Cost / Capacity Treatment

The abstract is predictive, not a post-cost trading rule. Any backtest must include taker fees, maker/taker side, spread, queue/fill assumptions, latency, order-size capacity, wallet-ranking update delay, and market-impact/crowding stress.

## Strategy Ideas Extracted

- Hypothesis: historically informative aggressive wallets forecast short-horizon returns on transparent venues after controlling for anonymous order flow.
- Minimum viable validation: reconstruct or use a public trade/order dataset with stable identifiers; rank wallets only on prior windows; compare identity-flow features against price/quote/order-flow baselines; evaluate net utility after fees and latency; include placebo wallet cohorts.
- Practical use: venue-state/adverse-selection feature or no-trade filter for DEX/prediction-market strategies, not a first coding target.

## Connections to Existing Research

### Reinforces

- [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]]: side and participant attribution are first-order identification issues in public prediction-market records.
- [[OpenMarket Synchronized Polymarket-Binance Dataset]]: public cross-venue datasets should test whether participant identity adds beyond book-implied probability and underlying-market order flow.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]: large/aggressive flow interpretation depends on liquidity/informedness state, not only order size.

### Contradicts / Weakens

Weakens anonymous-order-flow-only microstructure models for transparent venues where public trader histories are persistent and predictive.

### Transfers Across Asset Classes or Domains

Potentially transfers to public-wallet DeFi, on-chain perps, and prediction markets; less transferable to equities or centralized crypto venues without public identity.

### Missing Validation or Method Supplied

Supplies a participant-identity feature-admission test: identity must beat anonymous flow, placebo wallet cohorts, and strict time-gated ranking before being considered signal evidence.

## Framework Potential

- Candidate framework: Microstructure-conditioned decay and liquidity-state validation.
- Linked notes: [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]], [[OpenMarket Synchronized Polymarket-Binance Dataset]], [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]].
- Testable composite hypothesis: public participant identity improves state-dependent adverse-selection measurement only on venues where identifiers are stable and execution latency/costs are low enough.
- Minimum viable validation: time-gated wallet ranking, identity-feature ablation, placebo cohorts, fee/latency stress, and sybil/identifier-turnover diagnostics.
- What would falsify this connection? Identity features fail to beat anonymous order-flow baselines out of sample after ranking delay, fees, and wallet-churn controls.

## Keep / Reject Decision

**Keep.** High-signal microstructure source and framework update, but do not promote to coding queue until an obtainable dataset and execution-cost model are specified.

## Related Notes

- [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]]
- [[OpenMarket Synchronized Polymarket-Binance Dataset]]
- Microstructure-conditioned decay and liquidity-state validation framework
