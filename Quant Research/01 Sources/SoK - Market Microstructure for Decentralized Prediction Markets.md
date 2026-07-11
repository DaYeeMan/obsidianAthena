---
type: source-note
source_kind: paper / survey
asset_classes: [prediction-markets, crypto, market-microstructure]
implementation_class: foundational
importance: medium
last_reviewed: "2026-07-10"
tags: [quant-source, prediction-markets, decentralized-markets, market-microstructure, crypto, manipulation-resistance]
concepts: [decentralized-prediction-markets, polymarket, market-resolution, settlement, manipulation-resistance, market-design]
---

# SoK - Market Microstructure for Decentralized Prediction Markets

## Citation / Link

Nahid Rahman, Joseph Al-Chami, Jeremy Clark, “SoK: Market Microstructure for Decentralized Prediction Markets (DePMs),” arXiv:2510.15612v4, updated 2026-07-08. https://arxiv.org/abs/2510.15612v4

## Summary

This systematization-of-knowledge paper surveys decentralized prediction markets from early designs through modern markets such as Polymarket. It organizes DePMs into an eight-stage workflow: infrastructure, market topic, share structure/pricing, initialization, trading, resolution, settlement, and archiving. It emphasizes trade-offs among decentralization, expressiveness, and manipulation resistance and identifies open research problems.

## Core Contribution

- Provides a market-design map for decentralized prediction markets rather than a single empirical alpha claim.
- Highlights that modern DePMs differ materially from early designs such as Truthcoin and Augur v1.
- Makes resolution and settlement design explicit, which is crucial for event-window manipulation and volatility research.
- Gives a taxonomy for deciding which prediction-market datasets are comparable and which are structurally different.

## Practical Relevance

- Classification: **Evidence-backed as a survey / foundational**.
- Not a trading signal and not directly retail-practical as alpha.
- Useful for data selection, venue-risk classification, manipulation-risk screening, and transferability checks between Kalshi, Polymarket, and other event-market datasets.

## Methods and Data

Abstract-level details:

- review of hundreds of DePM proposals since 2011,
- modular eight-stage market workflow,
- analysis of design variants and trade-offs,
- open problems for DePM research.

Minimum local adaptation:

1. Before testing prediction-market signals, classify the venue/contract by resolution mechanism, settlement process, trading mechanism, and manipulation defenses.
2. Avoid pooling contracts across designs unless the design variables are modeled.
3. Use taxonomy fields as covariates in settlement-manipulation and volatility studies.

## Leakage / Bias / Overfitting Concerns

- Survey evidence is not empirical alpha evidence.
- DePM designs and regulatory constraints change quickly; historical findings may not transfer to current markets.
- Archival data can be incomplete or altered by indexing choices.

## Transaction Cost / Capacity Treatment

- DePM trading requires venue-specific fees, liquidity, spread, oracle/resolution risk, and on-chain settlement costs.
- The survey is most useful for identifying which frictions must be modeled, not estimating their magnitude.

## Strategy Ideas Extracted

No direct strategy extracted. Use as a **foundational taxonomy** for prediction-market research:

- **Hypothesis:** prediction-market strategy performance and manipulation risk are conditional on venue design, resolution process, and settlement architecture.
- **Validation:** add market-design fields before pooling event contracts or comparing Kalshi and Polymarket-style datasets.

## Connections to Existing Research

### Reinforces

- [[Settlement Manipulation in Prediction Markets]]: settlement rules and resolution mechanisms are first-order variables.
- [[Volatility in Prediction Markets - A Structural Approach]]: structural volatility models should account for venue and contract design.

### Contradicts / Weakens

- Weakens broad claims about “prediction markets” that ignore centralized/decentralized venue design differences.

### Transfers Across Asset Classes or Domains

- The modular workflow resembles exchange microstructure taxonomies in crypto spot/derivatives venues.

### Missing Validation or Method Supplied

- Supplies a classification layer for DePM datasets before event-study or volatility-model comparisons.

## Framework Potential

- Candidate framework: structural event-contract risk modeling.
- Linked notes: [[Settlement Manipulation in Prediction Markets]], [[Volatility in Prediction Markets - A Structural Approach]].
- Testable composite hypothesis: event-market signal robustness depends on contract design, venue mechanics, time-to-resolution, liquidity, and resolution/settlement rules.
- Minimum viable validation: tag contracts by design variables and test whether settlement-window effects or volatility forecasts survive design-conditioned splits.
- What would falsify this connection? design tags do not explain any variation in volatility, manipulation risk, liquidity, or strategy performance after simple controls.

## Keep / Reject Decision

Keep as foundational for prediction-market research design; not a coding-queue item.

## Related Notes

- [[Settlement Manipulation in Prediction Markets]]
- [[Volatility in Prediction Markets - A Structural Approach]]
