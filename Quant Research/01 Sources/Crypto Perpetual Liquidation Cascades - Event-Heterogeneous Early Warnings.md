---
type: source-note
source_kind: paper / crypto perpetual liquidation-cascade early-warning diagnostics
asset_classes: [crypto, bitcoin, perpetual-futures, risk-management, market-microstructure]
implementation_class: foundational / retail-adaptable with exchange data
importance: medium
last_reviewed: "2026-07-30"
tags: [quant-source, crypto, perpetual-futures, liquidation-cascades, early-warning-signals, risk-management]
concepts: [critical-slowing-down, liquidation-cascade-warning, leverage-state-variable, endogenous-vs-exogenous-cascades]
---

# Crypto Perpetual Liquidation Cascades - Event-Heterogeneous Early Warnings

## Citation / Link

Ramon Marc Garcia Seuma, “Where does the criticality live? Early-warning signals are event-heterogeneous across seven crypto-perpetual liquidation cascades,” arXiv:2607.27070v1, submitted 2026-07-29. https://arxiv.org/abs/2607.27070v1

Comment: 13 pages, 7 figures. Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper tests whether crypto perpetual-futures crashes exhibit a reproducible early-warning signature of critical transitions and, if so, which variable carries it. It studies seven BTC liquidation cascades from 2022-2025 using minute-level price and 5-minute leverage/order-flow data. Rolling variance and lag-1 autocorrelation on detrended residuals are tested with Kendall-tau across 39 configurations per variable and event. The abstract reports no event-invariant variable: price carries a critical-slowing-down signature in five of seven events but not in two sudden-news tariff shocks; one major event appears to locate the signal in leverage rather than price.

For this library, the important point is regime heterogeneity. Liquidation-risk filters should not assume one universal early-warning variable; endogenous leverage buildup and exogenous news shocks require different validation buckets.

## Core Contribution

- Tests early-warning signals across multiple BTC liquidation cascades using price and leverage/order-flow state variables.
- Separates endogenous-buildup cascades from sudden exogenous-news shocks.
- Shows that criticality may live in different observables across events.
- Reinforces the need for event-clustered validation rather than pooled average crash metrics.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as crypto liquidation-risk methodology; foundational / retail-adaptable with exchange data**.
- Retail adaptation is possible with minute prices, open interest/leverage/liquidation/order-flow proxies, funding, and venue-stress data, but high-quality leverage data can be exchange-specific.
- Not a directional alpha claim. Use as a kill-switch/deleveraging or stress-label candidate for crypto futures strategies.

## Methods and Data

- Seven BTC liquidation cascades from 2022-2025.
- Minute-level price plus 5-minute leverage/order-flow data.
- Detrended residuals, rolling variance, lag-1 autocorrelation, Kendall-tau trend tests, and 39 configuration sweeps per variable/event.

## Leakage / Bias / Overfitting Concerns

- Event selection and detrending choices can create hindsight bias.
- Configuration sweeps require multiplicity control or predeclared validation.
- Cascades are rare, so confidence intervals and false-alarm rates matter.
- Public liquidation/open-interest proxies may lag or differ from exchange-internal risk states.

## Transaction Cost / Capacity Treatment

The paper is a risk diagnostic, not a trade signal. Any deleveraging rule must include funding, spreads, market impact during stress, exchange outages, ADL/insurance-fund mechanics, and the opportunity cost of false exits.

## Strategy Ideas Extracted

Candidate risk-control module: for crypto futures trend/funding/carry strategies, build event labels for liquidation cascades and compare early-warning variables — price variance/autocorrelation, leverage/open-interest stress, liquidation flow, funding dislocation, spread/depth, and exchange-quality flags — against simple realized-volatility, drawdown, and funding filters.

## Connections to Existing Research

### Reinforces

- [[Risk-Based Auto-Deleveraging]] — extends exchange-risk stress from ADL design toward pre-cascade warning variables.
- [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]] — reminds that clock/order-flow effects need liquidation-state controls.
- [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]] — exchange-quality flags may help separate endogenous buildup from data/venue artifacts.

### Contradicts / Weakens

Weakens any universal crypto crash-warning indicator; the signal can move from price to leverage or disappear in sudden news shocks.

### Transfers Across Asset Classes or Domains

Transfers to options and equity risk-throttle research as an event-heterogeneity rule: endogenous liquidity/positioning crises and exogenous jumps should be validated separately.

### Missing Validation or Method Supplied

Supplies an event-clustered early-warning design and a warning to evaluate false alarms and missed exogenous shocks separately.

## Framework Potential

- Candidate framework: microstructure-conditioned liquidation/venue-stress validation.
- Linked notes: [[Risk-Based Auto-Deleveraging]], [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]].
- Testable composite hypothesis: crypto futures strategies should reduce leverage only when predeclared price/leverage/order-flow stress variables improve net drawdown or tail loss versus simple vol/drawdown/funding filters after false-exit costs.
- Minimum viable validation: event-clustered BTC/ETH perp backtest with pre-cascade windows, matched non-events, blocked validation, and action-attribution.
- What would falsify this connection? Stress variables that only identify events in hindsight or underperform simple volatility/drawdown filters after opportunity costs.

## Keep / Reject Decision

Keep as a foundational crypto risk source. Add to registry as a risk-filter candidate, not a coding-queue item.

## Related Notes

- [[Risk-Based Auto-Deleveraging]]
- [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]]
- [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]]
