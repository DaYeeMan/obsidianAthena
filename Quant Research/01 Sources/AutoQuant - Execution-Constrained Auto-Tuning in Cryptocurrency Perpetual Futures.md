---
type: source-note
source_kind: paper / execution-aware crypto-perpetual configuration-selection framework
asset_classes: [crypto, perpetual-futures, ML, backtest-validation, execution]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-08-06"
tags: [quant-source, crypto, perpetual-futures, auto-tuning, execution-constraints, backtest-governance]
concepts: [execution-aware-auto-tuning, funding-visibility, two-stage-window-screening, accounting-invariant-checks]
---

# AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures

## Citation / Link

Kaihong Deng, “AutoQuant: An Auditable Expert-System Framework for Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures,” arXiv:2512.22476v2, originally submitted 2025-12-27 and surfaced as updated/new feed item on 2026-08-06. https://arxiv.org/abs/2512.22476v2

Semantic Scholar lookup returned HTTP 429 during the 2026-08-06 run, so citation counts were not recorded.

## Summary

The abstract frames crypto-perpetual backtests as highly sensitive to execution timing, funding alignment, cost modeling, and repeated evaluation-window reuse during parameter search. AutoQuant is an expert-system-style configuration-selection framework that encodes execution timing, funding visibility, costs, feasibility constraints, two-stage window/cost screening, Bayesian search, deterministic artifacts, and accounting-invariant checks. It is applied to BTC/USDT, ETH/USDT, SOL/USDT, and AVAX/USDT perpetuals and reports that zero-cost or fee-only backtests materially inflate apparent performance relative to stricter execution-aware scenarios.

For this library, AutoQuant is a backtest-governance source rather than alpha. Its strongest use is to harden the standard audit block for crypto perpetual research before parameter tuning creates false confidence.

## Core Contribution

- Treats execution semantics, funding visibility, and feasibility constraints as explicit rules rather than implementation afterthoughts.
- Combines Bayesian parameter search with two-stage screening across windows and cost scenarios.
- Exports deterministic artifacts and accounting-invariant checks for traceability.
- Provides a crypto-perpetual-specific warning that cost/funding/execution assumptions can dominate signal ranking.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as validation/governance methodology; foundational / retail-adaptable**.
- Retail adaptation is realistic because the framework can be simplified into a reproducible tuning protocol for Binance/Bybit-style OHLCV, funding, and fee data.
- It should be added to crypto backtest audit design, not treated as a new trading strategy.

## Methods and Data

- Crypto perpetual contracts: BTC/USDT, ETH/USDT, SOL/USDT, AVAX/USDT.
- Expert-system constraints for timing, funding, costs, feasibility, and accounting.
- Bayesian search with two-stage validation across windows and cost scenarios.

## Leakage / Bias / Overfitting Concerns

- Bayesian tuning can still overfit if search budget, signal family, and windows are not frozen.
- Window reuse and selective reporting remain risks without an untouched final holdout.
- Strict accounting checks catch mechanical errors but do not prove economic edge.

## Transaction Cost / Capacity Treatment

The core relevance is transaction-cost treatment: fees, funding visibility/alignment, execution delay, feasibility filters, and cost-scenario robustness should be modeled before selecting configurations.

## Strategy Ideas Extracted

- Hypothesis: many crypto-perpetual strategy configurations that look attractive under zero/fee-only assumptions fail under strict timing, funding, and cost semantics.
- Minimum viable validation: implement an AutoQuant-lite protocol around any crypto strategy family: frozen signal family, chronological windows, funding timestamp rules, fee/slippage scenarios, two-stage selection, accounting invariants, and untouched holdout.
- Practical use: no-trade / no-promote gate for crypto ML or rule tuning.

## Connections to Existing Research

### Reinforces

- [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]]: model replacement must be evaluated in forward windows, not repeatedly recycled validation sets.
- Standard cost/regime/liquidity/decision audit block for backtests as tracked in the coding queue: crypto strategies need explicit execution/funding semantics.
- [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]]: small gross intraday edges can vanish under realistic friction and deployment gates.

### Contradicts / Weakens

Weakens crypto auto-tuning papers or bots that report optimized Sharpe without strict funding, timing, and post-selection validation.

### Transfers Across Asset Classes or Domains

Transfers to event-window crypto strategies, funding/carry systems, intraday futures/FX strategies, and any repeated parameter-search workflow with hidden cost assumptions.

### Missing Validation or Method Supplied

Supplies a concrete execution-constrained tuning protocol and accounting-invariant audit layer.

## Framework Potential

- Candidate framework: Cost-aware decision-process diagnostics.
- Linked notes: [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]], [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]].
- Testable composite hypothesis: execution/funding-aware configuration selection reduces false strategy promotion versus naive one-stage tuning.
- Minimum viable validation: apply AutoQuant-lite to a transparent crypto-perp signal family and compare selected configurations under zero-cost, fee-only, and strict funding/execution scenarios.
- What would falsify this connection? Strict execution-aware selection produces the same promoted models and net utility as naive tuning across multiple signal families and holdout windows.

## Keep / Reject Decision

**Keep.** High practical value as a validation/governance artifact; not promoted to coding queue because the queue already contains the broader standard audit block.

## Related Notes

- [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]]
- [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]]
- [[2026-08-02 Weekly Quant Synthesis and Strategy Decay Review]]
