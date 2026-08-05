---
type: source-note
source_kind: paper / prediction-market public-fill attribution limits
asset_classes: [prediction-markets, crypto, polymarket, market-microstructure]
implementation_class: foundational / retail-adaptable with public records
importance: medium
last_reviewed: "2026-07-31"
tags: [quant-source, prediction-markets, polymarket, attribution-limits, public-records, market-microstructure]
concepts: [polymarket-fill-attribution, public-fill-identification-limits, maker-taker-attribution, behavioral-concentration]
---

# Fill-Side Behavioral Concentration on Polymarket - Attribution Limits

## Citation / Link

Maksym Nechepurenko, “Fill-Side Behavioral Concentration on Polymarket: Identification Limits under Record-Level Attribution,” arXiv:2605.11640v2, updated 2026-07-30. https://arxiv.org/abs/2605.11640v2

Comment: major pre-publication correction; the archived sample is a 2.285-day legacy-CTF-only block range, not a seven-day venue sample; no new empirical run. Semantic Scholar lookup during this run returned 1 citation, 0 influential citations, and 12 references.

## Summary

The paper studies what Polymarket public executed-fill records can and cannot identify. The updated abstract explicitly narrows the empirical scope: the archived extraction covers only legacy CTF Exchange Polygon blocks 86,008,447–86,107,178, roughly 25 April 2026 17:09 UTC to 28 April 2026 00:00 UTC. It contains 13,356,931 OrderFilled records, 77,204 addresses with at least five attributed records, and 43,116 token identifiers; negative-risk markets are absent.

The revision is valuable as a data-identification warning. The archived feature construction credits both maker and taker addresses on each fill, but this convention is not invariant to match fragmentation, and mint/burn executions do not admit a universal buyer/seller interpretation. The originally reported one-cluster result is retained only as a null under the original record-level representation, not as evidence of a truly unimodal participant population.

For this library, the actionable lesson is conservative: public prediction-market fill records are useful for descriptive diagnostics, but buyer/seller behavior, concentration, and informed-flow claims require venue-specific attribution rules, maker/taker side handling, mint/burn logic, and sample-scope disclosure before becoming strategy evidence.

## Core Contribution

- Documents identification limits in Polymarket public executed-fill data.
- Corrects sample scope and makes legacy-CTF-only coverage explicit.
- Shows that maker/taker record attribution can alter concentration and clustering interpretations.
- Reinforces that public fills do not fully identify quote lifecycle or economically invariant buyer/seller behavior.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as data-identification warning; foundational / retail-adaptable with public records**.
- Retail adaptation is feasible as a data-quality gate for public Polymarket studies.
- Not alpha evidence; it is a no-trade / no-overclaim filter before settlement-window or participant-behavior strategies.

## Methods and Data

- Public OrderFilled records from a corrected legacy CTF Exchange Polygon block range.
- Address-level attribution with at least five attributed records.
- Concentration and clustering claims under record-level representation.
- Revision explicitly narrows scope and emphasizes attribution limits.

## Leakage / Bias / Overfitting Concerns

- Sample is short and legacy-CTF-only, so cross-period or whole-venue conclusions are unsafe.
- Maker/taker and mint/burn attribution rules can change the economic interpretation.
- Negative-risk markets are absent, limiting generalization.
- Record-level clustering can be representation-dependent rather than behaviorally fundamental.

## Transaction Cost / Capacity Treatment

No strategy cost model. Use this as a data-quality and identification screen before building prediction-market execution or settlement-window backtests. If fill-side identity is ambiguous, do not infer informed-flow, manipulation, or concentration alpha without additional data.

## Strategy Ideas Extracted

Prediction-market public-record audit checklist:

1. Record exact contract type, venue subsystem, block/time window, and market inclusions/exclusions.
2. Separate maker, taker, mint, burn, and match-fragmentation effects where possible.
3. Report whether concentration is address-, fill-, dollar-, or side-weighted.
4. Avoid buyer/seller/informed-flow claims unless the side convention is economically invariant.
5. Treat unresolved attribution as a validation blocker for behavioral alpha claims.

## Connections to Existing Research

### Reinforces

- [[OpenMarket Synchronized Polymarket-Binance Dataset]]
- [[Settlement Manipulation in Prediction Markets]]
- [[SoK - Market Microstructure for Decentralized Prediction Markets]]
- [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]]

### Contradicts / Weakens

Weakens prediction-market studies that infer participant behavior or manipulative flow from public fill records without side-attribution and sample-scope caveats.

### Transfers Across Asset Classes or Domains

Transfers mainly to prediction markets and DeFi/public-chain market microstructure. The same lesson applies to AMM swaps and DEX fills where public records may not directly identify economic intent.

### Missing Validation or Method Supplied

Supplies a public-record attribution gate for Polymarket and decentralized prediction-market research.

## Framework Potential

- Candidate framework: prediction-market and public-chain data-identification gates.
- Linked notes: [[OpenMarket Synchronized Polymarket-Binance Dataset]], [[Settlement Manipulation in Prediction Markets]], [[SoK - Market Microstructure for Decentralized Prediction Markets]], [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]].
- Testable composite hypothesis: public prediction-market data can support robust settlement/venue-design tests only after side attribution, sample scope, and contract-type metadata are made explicit.
- Minimum viable validation: add attribution-scope metadata and side-convention sensitivity panels to any Polymarket event study.
- What would falsify this connection? A future data source provides invariant side, quote-lifecycle, and account-role identification, making these public-record caveats less binding.

## Keep / Reject Decision

Keep as a medium-importance foundational data-quality warning. It should prevent overclaiming from public Polymarket fills and improve future settlement/manipulation backtest specs.

## Related Notes

- [[OpenMarket Synchronized Polymarket-Binance Dataset]]
- [[Settlement Manipulation in Prediction Markets]]
- [[SoK - Market Microstructure for Decentralized Prediction Markets]]
- [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]]
