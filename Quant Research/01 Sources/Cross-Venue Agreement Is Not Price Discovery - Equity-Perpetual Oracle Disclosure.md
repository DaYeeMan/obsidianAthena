---
type: source-note
source_kind: paper / crypto equity-perpetual oracle market-design validation
asset_classes: [crypto, equity-perpetuals, market-microstructure, prediction-markets, oracles]
implementation_class: foundational / institutional-only as written / retail-adaptable as oracle-risk diagnostic
importance: high
last_reviewed: "2026-08-11"
tags: [quant-source, crypto, equity-perpetuals, oracle-design, price-discovery, market-microstructure]
concepts: [cross-venue-agreement, oracle-disclosure, closed-window-marks, cash-reopen-validation]
---

# Cross-Venue Agreement Is Not Price Discovery - Equity-Perpetual Oracle Disclosure

## Citation / Link

Donghwa Seo, Doohwi Cha, Seunghan Son, Juyeong Lee, Minjae Lee, Minsuk Sung, “When Cross-Venue Agreement Is Not Price Discovery: Disclosure Frontiers for 24/7 Equity-Perpetual Oracles,” arXiv:2608.09188v1, submitted 2026-08-10. https://arxiv.org/abs/2608.09188v1

arXiv comment: 16 pages, 2 figures. Semantic Scholar lookup returned HTTP 429 during the 2026-08-11 run, so citation counts were not recorded.

## Summary

The paper studies crypto-listed equity perpetuals that trade while the primary cash market is closed and still require a mark for margin, funding, and liquidation. The abstract models the closed-window mark as an oracle operator combining external anchoring and self/peer derivative reference. From marks and proxies alone these components are observationally equivalent: lead-lag and information-share estimators have power equal to size unless disclosure or cash-reopen validation breaks the equivalence class.

The empirical claim is conservative but useful: disclosed topology or support restrictions can identify, falsify, or leave a positive-dimensional class of possible oracle structures, while cross-venue agreement by itself does not prove price discovery.

For this library, this is a market-design and validation note, not a trading signal. It warns that 24/7 equity-perpetual, prediction-market, and oracle-driven crypto backtests need mark-construction metadata and cash-reopen validation before treating cross-venue agreement as information.

## Core Contribution

- Separates external anchoring from self/peer derivative reference in closed-window oracle marks.
- Shows observational equivalence from marks/proxies alone, limiting lead-lag and information-share inference.
- Identifies disclosure conditions that can break the equivalence class.
- Uses cash-reopen validation to bound live-external content in closed-window variance.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as market-design validation methodology; foundational / institutional-only as written / retail-adaptable as oracle-risk diagnostic**.
- Retail adaptation: for equity-perpetual or prediction-market studies, require contract/oracle metadata, primary-market open/closed flags, cash-reopen error, and venue-mark disclosure before using cross-venue agreement as price-discovery evidence.
- Strong no-trade/filter implication: avoid treating overnight or weekend equity-perpetual marks as independent information when the mark may be self-referential.

## Methods and Data

- Abstract-level validation only in this run.
- Requires closed-window mark data, venue disclosures, external anchor rules, self/peer reference structure, and cash-market reopen prices.
- Applicable proxy checks: compare closed-window mark changes to cash-reopen errors, mark dispersion, oracle-rule changes, funding/liquidation events, and forbidden-anchor tests where metadata exist.

## Leakage / Bias / Overfitting Concerns

- Lead-lag tests can be unidentified if mark topology is not disclosed.
- Cross-venue agreement can be circular reference, not information.
- Venue disclosures may be partial or change over time.
- Cash-reopen validation must avoid using reopen information in pre-open trading decisions.

## Transaction Cost / Capacity Treatment

Trading implications are secondary. Any strategy using equity-perp closed-window marks must include funding, liquidation, spread/depth, venue availability, oracle update timing, and execution latency. The paper mainly supplies a data-quality/oracle-risk gate.

## Strategy Ideas Extracted

- Add a closed-window oracle-risk label to equity-perpetual and prediction-market backtests.
- For 24/7 equity-perp signals, treat primary-market reopen error as an ex post validation metric rather than as decision-time data.
- Reject cross-venue agreement as a price-discovery signal unless venue disclosure or reopen validation supports independent external content.

## Connections to Existing Research

### Reinforces

- [[OpenMarket Synchronized Polymarket-Binance Dataset]]
- [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]]
- [[Settlement Manipulation in Prediction Markets]]
- [[Axient Leveraged Event Markets - Credit and Finality Design]]
- [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]]

### Contradicts / Weakens

Weakens naive lead-lag or information-share claims in oracle-linked 24/7 instruments when topology, anchors, and cash-reopen validation are unavailable.

### Transfers Across Asset Classes or Domains

Transfers to prediction markets, crypto derivatives, AMM oracles, index perpetuals, and any strategy using non-primary-market marks when the cash/reference market is closed.

### Missing Validation or Method Supplied

Supplies an oracle-disclosure and cash-reopen validation gate for market-design and venue-risk frameworks.

## Framework Potential

- Candidate framework: Prediction-market/event-linked derivative design-risk validation.
- Linked notes: [[OpenMarket Synchronized Polymarket-Binance Dataset]], [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]], [[Settlement Manipulation in Prediction Markets]], [[Axient Leveraged Event Markets - Credit and Finality Design]].
- Testable composite hypothesis: oracle-linked instruments with opaque self/peer reference should have higher closed-window mark error and liquidation/funding instability than instruments with disclosed external anchors.
- Minimum viable validation: closed-window mark-to-reopen error by venue, disclosure type, funding/liquidation state, and cross-venue agreement bucket.
- What would falsify this connection? Disclosed external-content tests show cross-venue agreement reliably predicts cash reopen beyond simple baselines and oracle metadata.

## Keep / Reject Decision

**Keep.** High-value foundational market-design and oracle-risk validation source; no direct alpha promotion.

## Related Notes

- [[2026-08-11 1402 Daily Quant Research Review]]
