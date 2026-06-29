---
type: source-note
source_kind: paper
asset_classes: [options, equities]
implementation_class: retail-adaptable
importance: high
last_reviewed: "2026-06-28"
tags: [quant-source, options, volatility-risk-premium, put-writing, position-sizing]
---

# Sizing the Risk - Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options

## Citation / Link

Maciej Wysocki, “Sizing the Risk: Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options,” arXiv:2508.16598v1, 2025-08-09. https://arxiv.org/abs/2508.16598v1

Semantic Scholar retrieval during 2026-06-28 cron run returned 0 citations, 50 references, and venue metadata that should be manually verified.

## Summary

The paper studies systematic S&P 500 index-option put-writing using short expirations from 0 to 5 days, with the main research question focused on position sizing rather than simply whether the volatility risk premium exists. It compares fixed-style implementations against Kelly, VIX-regime, and hybrid sizing approaches.

## Core Contribution

A directly testable design space for short-dated index-option premium selling:

- option tenor: 0–5 DTE SPX/SPXW puts,
- moneyness/delta selection,
- volatility estimators,
- sizing methods: Kelly, VIX scaling, and hybrid Kelly+VIX scaling.

## Practical Relevance

- Classification: **retail-adaptable**.
- Retail traders can access SPX/SPXW options, but robust replication needs good option-chain data and conservative fills.
- The research is more useful as a backtest template than as deployment evidence.

## Methods and Data

Required for replication:

- SPX/SPXW historical option chain with bid/ask, volume, open interest, greeks if available,
- SPX index levels,
- VIX and risk-free rates,
- margin/cash treatment,
- event/regime segmentation: 2018 vol event, 2020 crash, 2022 bear, 2023–2026 0DTE era.

## Leakage / Bias / Overfitting Concerns

- Avoid using same-sample Kelly fraction estimates without walk-forward estimation.
- Avoid midpoint fills, stale option quotes, and survivorship-filtered chains.
- Separate 0DTE results from 1–5 DTE; intraday path risk is qualitatively different.
- Report parameter sensitivity across deltas, expirations, stop/roll rules, and VIX regimes.

## Transaction Cost / Capacity Treatment

Critical. Strategy returns can be dominated by:

- bid/ask spreads,
- intraday gap risk,
- commissions and exchange fees,
- margin/cash drag,
- settlement and exercise mechanics,
- liquidity differences across strikes and expiries.

Backtests should use bid or conservative bid/ask assumptions, not mid-price fills.

## Strategy Ideas Extracted

- [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]]

## Keep / Reject Decision

**Keep** as a high-priority source for replication. Classification remains **Plausible but untested** until independently reproduced with realistic costs and regime splits.

## Related Notes

- [[2026-06-28 Daily Quant Research Review]]
