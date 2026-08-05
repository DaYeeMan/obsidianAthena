---
type: source-note
source_kind: paper / microstructure mean-reversion optimal trading model
asset_classes: [market-microstructure, equities, futures, crypto, execution]
implementation_class: foundational / institutional-only as written / retail-adaptable as diagnostic
importance: medium
last_reviewed: "2026-08-04"
tags: [quant-source, market-microstructure, mean-reversion, large-tick-assets, execution-costs]
concepts: [microstructure-mean-reversion, efficient-price-gap, large-tick-parity, spread-net-profit]
---

# Optimal Trading of Microstructure Mean Reversion

## Citation / Link

Lucas Rabechini Amaral, “Optimal Trading of Microstructure Mean Reversion,” arXiv:2608.00885v1, submitted 2026-08-01. https://arxiv.org/abs/2608.00885v1

Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper models seconds-scale midprice observations as a stationary mean-reverting error around a latent efficient price. In liquid large-tick assets, spread parity on the half-tick grid and the gap between observed mid and efficient price define the key state. The paper builds an order-book model where own flow produces the error and solves for a long-run average profit rule net of bid-ask spread, with Ornstein-Uhlenbeck-like conditional moments for the gap under a balanced-response condition.

For this library, this is not a retail day-trading prescription. It is a microstructure mechanism reference and a falsification lens for short-horizon reversal claims: a signal is only meaningful if it can be separated from spread parity, bid/ask bounce, and efficient-price estimation error.

## Core Contribution

- Formalizes seconds-scale microstructure mean reversion as an efficient-price gap problem.
- Links large-tick spread parity, jumpy midprice paths, and spread-net optimal trading.
- Provides a mechanism for why observed short-run reversal can exist without being easy profit.
- Reinforces the need for latent-efficient-price and fill-cost diagnostics.

## Practical Relevance

- Classification: **Plausible-to-evidence-backed at abstract level as microstructure theory; foundational / institutional-only as written / retail-adaptable as diagnostic**.
- Institutional-only as written because seconds-scale efficient-price estimation, queue/fill modeling, and large-tick LOB data are required.
- Retail adaptation is a no-trade gate: do not trust OHLCV or bar-level reversal unless spread, tick-size, and execution-state effects are explicitly handled.

## Strategy / Backtest Translation

- Hypothesis to test only with suitable data: gap-based mean reversion can earn spread-net profits in liquid large-tick instruments when efficient-price estimates are reliable and passive/aggressive fill assumptions are realistic.
- Data: tick trades/quotes/order book, spread parity, queue/fill data, fees/rebates, latency assumptions.
- Baselines: no-trade, bid/ask bounce filter, simple lag reversal, marketable execution, passive execution with adverse-selection stress.
- Validation: chronological venue-specific tests, cost/fill stress, liquidity-regime splits, post-publication decay, and comparison to [[Microstructural Foundations of Rough Noise]].

## Risks / Failure Modes

- Bar data can manufacture false reversal via bid/ask bounce and stale pricing.
- Efficient-price gap estimation is fragile and may require proprietary or expensive data.
- Spread capture can vanish after queue priority, non-fills, adverse selection, fees, and latency.

## Connections to Existing Research

- Reinforces [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]].
- Connects to [[Microstructural Foundations of Rough Noise]] and [[Optimal Execution with Passive Market Impact]] as a combined short-horizon reversal falsification framework.
