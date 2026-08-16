---
type: source-note
source_kind: paper / constrained-investor-base event study and classification-risk state
asset_classes: [equities, event-studies, asset-pricing, market-frictions]
implementation_class: retail-adaptable / foundational
importance: medium
last_reviewed: "2026-08-14"
tags: [quant-source, equities, event-study, constrained-investors, classification-risk, Shariah-screening]
concepts: [classification-uncertainty, investor-base-fragmentation, permission-premium, index-inclusion-event-study]
---

# The Price of Permission - Classification Uncertainty in Constrained Capital Markets

## Citation / Link

Abdulrahman Qadi, Akash Sharma, Francesca Medda, “The Price of Permission: Classification Uncertainty in Constrained Capital Markets,” arXiv:2608.12634v1, submitted 2026-08-12. https://arxiv.org/abs/2608.12634v1

Semantic Scholar lookup returned HTTP 429 during the 2026-08-14 run, so citation counts were not recorded.

## Summary

The paper studies Shariah-compliant equity screening as a transparent case where institutional rules determine who may own a stock. The abstract distinguishes the binary eligibility label from classification uncertainty: rulebook disagreement and proximity to active screening boundaries determine how fragmented or unstable the permitted investor base is. In a 1999–2024 CRSP-Compustat panel of 13,188 securities across seven researcher-emulated Shariah rulebooks, screening disagreement and boundary proximity rank next-month screen-implied transitions. The U.S. evidence does not support an unconditional equal-weighted permission premium, and a 2023 DJIM/S&P methodology change produces no robust matched repricing.

The stronger event evidence comes from 25 official Securities Commission Malaysia lists. Among sufficiently tradable pre-existing inclusions, matched returns are reportedly 1.76 percentage points over [0,10] trading days and 2.25 percentage points over [0,20], with supportive leave-one-date-out, first-inclusion-only, and placebo checks. However, a joint 20-day pre-event test rejects and ownership/demand-pressure diagnostics do not identify a unique marginal buyer.

For this library, the useful idea is not a generic “Shariah premium.” It is an event-study and monitoring framework: formal eligibility may matter when it changes a constrained investor base in a recognized local market, but classification risk alone is not enough for a broad U.S. anomaly.

## Core Contribution

- Defines classification uncertainty from rulebook disagreement and proximity to screening boundaries.
- Tests whether constrained-investor permission states predict transitions and repricing.
- Finds no robust unconditional U.S. permission premium.
- Finds more supportive official Malaysian inclusion-event evidence among sufficiently tradable securities.
- Flags pre-event and buyer-identification caveats.

## Practical Relevance

- Classification: **Plausible but untested for tradable use; retail-adaptable / foundational as an event-study template**.
- Could inform constrained-investor-base event screens: official Shariah inclusions, index eligibility, mandate eligibility, collateral/rating inclusion, ETF/index methodology changes, or borrow/short-sale permission states.
- Not coding-ready for the core queue because tradable universes, event calendars, liquidity filters, tax/foreign-access constraints, and implementation costs are unresolved.

## Implementation / Backtest Translation

Minimum viable event-study proxy:

1. Build an official inclusion/exclusion calendar for a constrained investor rule, not an inferred label alone.
2. Require pre-event tradability and investability filters.
3. Measure matched or factor-adjusted returns over [0,10] and [0,20] windows, with pre-event placebo windows and leave-one-date-out checks.
4. Add turnover/volume, ownership, ETF/index flow, or fund-holding diagnostics where obtainable.
5. Score after-cost tradability: spread, foreign access, borrow/shortability, taxes, and event-timing availability.

## Costs / Frictions

- Foreign-market access, currency conversion, taxes, and local-market spreads may dominate a 10–20 day event effect.
- Official list publication timing and pre-announcement leakage must be timestamped precisely.
- Classification proximity variables require clean accounting data, rulebook implementation, and point-in-time fundamentals.

## Risks / Failure Modes

- U.S. null evidence warns against broad permission-premium overgeneralization.
- Pre-event return rejection suggests leakage, anticipation, or confounding.
- Demand-pressure mechanism is not cleanly identified.
- The effect may be market-specific and crowded once official lists are easily scraped.

## Connections to Existing Research

### Reinforces

- [[Bias-Robust Causal Inference for Panel Data]]: event studies with constrained donor pools need counterfactual-error and placebo discipline.
- [[Robustness or Crowding - Experimental Design for Trading Strategy Capacity]]: official eligibility effects may decay as capital crowds the same predictable windows.

### Framework Potential

- Candidate framework: investor-base constraint events as tradable only when the official event timestamp, marginal-buyer mechanism, liquidity, and post-cost capacity are all validated.
- What would falsify it: effects vanish after precise announcement timestamps, investability filters, costs, and date-cluster/bootstrap inference.
