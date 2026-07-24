---
type: source-note
source_kind: negative empirical study / code-supported audit
asset_classes: [crypto, machine-learning, spot-trading, strategy-validation]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-23"
tags: [quant-source, crypto, ml-forecasting, negative-results, binance, transaction-costs, leakage-audit]
concepts: [predictive-extrema, policy-value-gap, candle-based-ml, no-trade-gate, evidence-integrity-audit]
---

# Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit

## Citation / Link

Ayoub Jadouli, “Predictive Extrema, Unprofitable Policies: An AI-Assisted Audit of Candle-Based Binance Spot Timing Models,” arXiv:2607.19453v1, 2026-07-21. https://arxiv.org/abs/2607.19453v1

Comment: simulation-only negative empirical study; code and available artifacts: https://github.com/AyoubJadouli/Quantbot-Research-Framework

## Summary

The paper audits whether candle-based ML models predicting cryptocurrency extrema or short-horizon outcomes can become positive Binance Spot paper-trading policies after assumed costs. The abstract’s strongest result is negative: a ten-pair mandatory-daily selector lost 6.72% over 19 July cycles at 31 bps completed-cycle cost, validation-selected local-minimum and local-maximum policies lost or underperformed holding, and a high-ROC-AUC OHLCV-only adaptation still produced poor average precision and a worse-than-buy-and-hold result. The audit also downgrades an earlier holdout because dates influenced architecture work, a four-hour horizon was not purged at split boundaries, same-close entry was used, and raw result directories were absent.

The key contribution is the distinction between predictive event-ranking metrics and executable policy value. High AUC or plausible extrema forecasts are not enough when costs, precision, action timing, and leakage controls fail. Every operational decision in the paper remains NO_TRADE.

## Core Contribution

- Shows a concrete policy-value gap: predictive extrema scores did not translate into net profitable trades.
- Highlights evidence-integrity checks for AI-assisted research: artifact reconciliation, independent critique, and leakage review.
- Reinforces no-trade gating when validation metrics are below cost/materiality thresholds.
- Provides a code-supported negative reference for crypto candle-based ML timing claims.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as a negative code-supported audit; foundational / retail-adaptable**.
- Practicality: **retail-adaptable as a validation checklist**, not as a signal.
- The local action is to add policy-value gates before testing any price-only crypto ML model: precision, turnover, timing lag, costs, and buy-and-hold / simple momentum / funding baselines.

## Data / Backtest Requirements

- Binance Spot or comparable crypto pair OHLCV with timestamp integrity and fee schedule.
- Strict train/validation/test splits with purged outcome horizons and no same-close lookahead entries.
- Baselines: buy-and-hold, no-trade, simple momentum/reversal, volatility filter, and if futures are used, funding/carry.
- Metrics: average precision, cost-aware net return, drawdown, turnover, missed-opportunity/action attribution, and per-pair robustness.

## Costs / Frictions

Crypto spot timing models with tens of bps gross event advantages can be eliminated by completed-cycle fees, spread, slippage, missing liquidity, execution delay, and taxes. The cost gate should be applied before policy promotion, not after model selection.

## Failure Modes / Decay Risks

- Short July evaluation windows and exploratory protocols limit generality.
- Binance market structure and fee tiers are venue-specific.
- Price-only candle features can overfit calendar/volatility artifacts and decay quickly.
- AI-assisted audit is useful only if artifacts, prompts, data splits, and raw outputs are preserved.

## Connections to Existing Research

### Reinforces

- [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]], [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]], and [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]]: predictive metrics can be misleading unless converted into post-cost decision utility.
- [[FinBench - Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting]] and [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]: time-gated, artifact-preserving evaluation matters for AI-assisted finance research.

### Contradicts / Weakens

- Weakens candle-based Binance spot timing and extrema-prediction claims that report AUC or extrema accuracy without policy returns, costs, purged splits, and raw artifact availability.

### Framework Potential

- Candidate framework: predictive-score-to-policy-value audit.
- Minimum viable backtest: rerun a simple crypto OHLCV ML classifier only if it includes purged splits, fee/slippage stress, no-trade gate, and simple-rule baselines.
- Falsifier: high AUC but low average precision and negative net policy return should remain NO_TRADE.
