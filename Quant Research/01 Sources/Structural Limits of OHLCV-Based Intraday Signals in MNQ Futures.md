---
type: source-note
source_kind: paper
asset_classes: [futures, market-microstructure, intraday, validation]
implementation_class: retail-adaptable / foundational
importance: high
last_reviewed: "2026-07-15"
tags: [quant-source, intraday-futures, ohlcv, negative-results, transaction-costs, mnq]
concepts: [ohlcv-signal-falsification, intraday-momentum-costs, negative-results, positive-controls, deployment-criteria]
---

# Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures

## Citation / Link

Mathias Mesfin, “Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures: A Systematic Falsification Study,” arXiv:2605.04004v2, updated 2026-07-13. https://arxiv.org/abs/2605.04004v2

## Summary

This paper tests whether common intraday momentum signals based on five-minute OHLCV data produce a tradable edge in Micro E-mini Nasdaq 100 (MNQ) futures after realistic execution costs. Across 947 trading days from 2021–2025 and fourteen signal families, the abstract reports that none met all deployment criteria: out-of-sample walk-forward validation, t-statistic above 2.0, at least 30 trades, positive net returns after a fixed two-point round-trip friction cost, and year-to-year consistency. The study includes positive controls that pass the same framework, which strengthens its value as a falsification template rather than a blanket claim that intraday futures alpha is impossible.

## Core Contribution

- Preserves a negative result with explicit deployment criteria, rather than only reporting surviving strategies.
- Shows that many gross OHLCV intraday edges can be below plausible round-trip friction.
- Uses positive controls to verify that the evaluation framework can detect edge when present.
- Provides a practical anti-overfitting template for retail intraday futures research.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as a negative-result / validation methodology; retail-adaptable / foundational**.
- Directly relevant to intraday OHLCV strategies in futures, ETFs, and crypto.
- Most useful as a rejection screen: if a signal cannot survive simple costs, minimum sample size, and year splits, do not tune it further.
- Should not be overgeneralized to all intraday strategies because the result is MNQ-specific and uses a specific friction assumption.

## Methods and Data

Abstract-level details:

- MNQ five-minute OHLCV bars,
- 947 trading days from 2021–2025,
- fourteen common intraday momentum signal families,
- out-of-sample walk-forward validation,
- deployment filters: t-statistic, minimum trades, net returns after costs, year consistency,
- positive-control signals to test framework sensitivity.

## Leakage / Bias / Overfitting Concerns

The main value is disciplined falsification, but local replication should check session definitions, contract rolls, timestamp alignment, overlapping trades, holiday/half-day handling, and whether signal families were selected after exploratory inspection.

## Transaction Cost / Capacity Treatment

The paper uses a fixed two-point round-trip friction cost. Local tests should stress a range of costs, include commissions and slippage, distinguish market/limit execution assumptions, and evaluate how fills change during high-volatility or low-liquidity periods.

## Strategy Ideas Extracted

No immediate strategy. Extract a deployment gate for intraday bar strategies: require out-of-sample walk-forward validation, minimum trade count, net-of-cost profitability, year consistency, and positive/negative controls before feature expansion.

## Connections to Existing Research

### Reinforces

- [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]] — reinforces that short-speed trend/momentum must be evaluated under modern market structure and costs.
- [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]] — reinforces that apparent short-horizon predictability may not translate into directional tradable alpha.
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]] — reinforces cost and liquidity-state auditing before accepting a backtest edge.

### Contradicts / Weakens

Weakens generic retail claims that simple OHLCV intraday momentum patterns are deployable without cost, sample-size, and regime/year-split evidence.

### Transfers Across Asset Classes or Domains

The falsification template transfers to crypto perpetual futures and ETF intraday strategies, especially where fees/funding/spread drag dominate small gross edges.

### Missing Validation or Method Supplied

Supplies a negative-result reporting discipline and explicit deployment gates for short-horizon systematic strategies.

## Framework Potential

- Candidate framework: Microstructure-conditioned decay and liquidity-state validation; cost-aware decision-process diagnostics.
- Linked notes: [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]], [[Liquidity-Based Audit of Algorithmic Trading Strategies]], [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]].
- Testable composite hypothesis: many short-horizon OHLCV effects fail once deployment gates and modern frictions are applied, but positive controls can preserve the ability to detect robust edges.
- Minimum viable validation: add a negative-control/positive-control and deployment-gate table to any intraday strategy notebook.
- What would falsify this connection? A simple OHLCV signal that passes the same gates across contracts, years, costs, and roll/session definitions.

## Keep / Reject Decision

**Keep as a foundational retail-adaptable negative-result and validation reference.** It should downgrade generic intraday OHLCV strategies but not eliminate carefully validated event/liquidity-state designs.

## Related Notes

- [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]]
- [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]]
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]
- [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]]
