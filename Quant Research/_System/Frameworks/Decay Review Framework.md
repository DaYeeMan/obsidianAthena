---
type: decay-framework
tags: [quant-research, model-decay, outdatedness]
---

# Model and Strategy Decay Review Framework

Use this framework to sort, filter, and identify outdated models or strategies while preserving foundational work.

## Keep Even If Not Directly Tradable

Preserve as `foundational` when a paper/model supplies:
- a canonical baseline
- a durable economic mechanism
- a widely used methodology
- a useful null model or risk model
- a conceptual map for later strategy research

## Flag as Outdated-Watch

Flag as `outdated-watch` when there is evidence of:
- post-publication alpha decay
- severe crowding
- market structure changes that invalidate assumptions
- execution costs now overwhelming expected edge
- data no longer available or now too expensive
- method superseded by simpler, stronger, or more robust approaches

## Institutional-Only vs Retail-Adaptable

Classify as `institutional-only` if it requires:
- proprietary order flow or broker/dealer data
- latency-sensitive execution
- exchange membership/co-location
- massive options-chain storage/compute beyond reasonable retail setup
- balance-sheet/borrow access not available to retail
- OTC instruments or bespoke financing

Classify as `retail-adaptable` if the core idea can be approximated with:
- daily or intraday public data
- liquid equities/options/ETFs/crypto instruments
- simpler features
- slower holding periods
- robust cross-sectional or event-study design

## Practicality Questions

1. Can a retail trader obtain the necessary data legally and affordably?
2. Does the strategy survive realistic spreads, commissions, slippage, borrow, and option liquidity?
3. Does it require forecasting precision that is unlikely outside an institution?
4. Is the improvement over simple baselines economically meaningful?
5. Can the idea be expressed as a clean backtest hypothesis within days, not months?
6. Is the research useful as a building block even if not deployable directly?
