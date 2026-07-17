---
type: source-note
source_kind: paper
asset_classes: [equities, machine-learning, forecasting, validation]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-07-15"
tags: [quant-source, ml-forecasting, equity-forecasting, base-rate, timesfm, validation]
concepts: [base-rate-honest-benchmark, directional-accuracy-trap, expanding-walk-forward, held-out-ticker-split, fdr-control]
---

# When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting

## Citation / Link

Taizhen Cheung, SA Kwon, “When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting,” arXiv:2607.12248v1, 2026-07-14. https://arxiv.org/abs/2607.12248v1

## Summary

This paper is a negative-result benchmark for equity forecasting with a LoRA-adapted TimesFM model. The abstract reports that an apparent roughly 80% directional-accuracy result was a base-rate artifact in a rising equity market: a trivial always-up rule achieved comparable accuracy, and the fine-tuned model did not produce excess directional skill over that base rate across NASDAQ-100 and S&P 500 universes. The paper uses frozen data, expanding walk-forward folds, held-out ticker splits, honest baselines, paired tests, and Benjamini-Hochberg FDR control.

## Core Contribution

- Demonstrates why raw directional accuracy is a weak scoreboard for equity forecasting.
- Requires excess accuracy over base-rate and naive baselines rather than headline hit rate.
- Uses held-out-ticker and walk-forward validation to reduce memorization and leakage concerns.
- Provides a useful negative-result reference for evaluating time-series foundation models and fine-tuned adapters in finance.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as ML validation / negative-result methodology; foundational / retail-adaptable**.
- Not a trading signal.
- Practical translation: every ML directional model should report always-up/base-rate, random-walk, persistence, AR(1), and simple return/volatility baselines before any claim of directional edge.
- Especially relevant to crypto/equity ML pipelines where class imbalance, drift, and rising-market samples can make high hit rates meaningless.

## Methods and Data

Abstract-level details:

- LoRA-adapted TimesFM and zero-shot TimesFM,
- NASDAQ-100 and S&P 500 universes,
- expanding walk-forward folds,
- stratified held-out-ticker split,
- baselines: always-up, random walk, persistence, AR(1),
- McNemar and Diebold-Mariano paired tests,
- Benjamini-Hochberg FDR control.

## Leakage / Bias / Overfitting Concerns

The paper is valuable precisely because it exposes a base-rate / benchmark-selection trap. Local use should still verify frozen universes, constituent availability, no future membership leakage, corporate-action treatment, feature availability timestamps, and whether horizons overlap.

## Transaction Cost / Capacity Treatment

Directional accuracy alone says nothing about profitability. A local trading test would need turnover, spreads, slippage, borrow/shorting constraints if short signals are used, and a threshold translating forecasts into positions.

## Strategy Ideas Extracted

No direct alpha. Extract a validation gate: any directional ML strategy must beat base-rate and naive baselines on excess directional accuracy and downstream net utility, not only raw hit rate or point-forecast loss.

## Connections to Existing Research

### Reinforces

- [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]] — reinforces skepticism toward price-only or generic sequence-model forecasting unless it beats simple baselines after fees.
- [[Forecasting Realized Volatility with Time Series Foundation Models]] — reinforces benchmark-first evaluation for foundation models, though this paper concerns directional returns rather than realized volatility.
- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]] — reinforces that agent/model benchmarks need transparent, time-gated baselines.

### Contradicts / Weakens

Weakens any claim that high directional accuracy from fine-tuned foundation models is evidence of tradable edge unless excess accuracy over base-rate and net utility are reported.

### Transfers Across Asset Classes or Domains

The base-rate-honest benchmark transfers to crypto trend/funding models, options directional filters, and event-study classifiers where class imbalance or a dominant market regime can inflate accuracy.

### Missing Validation or Method Supplied

Supplies a concrete validation block for directional ML: frozen data, expanding walk-forward, held-out assets, honest baselines, paired tests, and FDR control.

## Framework Potential

- Candidate framework: Simple-rule benchmark-first AI portfolio-policy evaluation; cost-aware decision-process diagnostics.
- Linked notes: [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]], [[Forecasting Realized Volatility with Time Series Foundation Models]], [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]].
- Testable composite hypothesis: directional ML models that pass raw-accuracy screens will often fail once scored by excess accuracy over base-rate and downstream net-of-cost utility.
- Minimum viable validation: add an always-up/base-rate comparator and naive forecasting baselines to the next equity or crypto ML forecast backtest.
- What would falsify this connection? A model that robustly beats base-rate and naive baselines across held-out assets, regimes, horizons, and cost-aware allocation tests.

## Keep / Reject Decision

**Keep as a high-priority foundational validation reference.** It is not alpha, but it directly prevents false positives in ML-return research.

## Related Notes

- [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]]
- [[Forecasting Realized Volatility with Time Series Foundation Models]]
- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]
- [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]]
