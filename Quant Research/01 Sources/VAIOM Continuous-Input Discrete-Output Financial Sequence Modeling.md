---
type: source-note
source_kind: paper
asset_classes: [foreign-exchange, machine-learning, forecasting, sequence-modeling]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: "2026-07-16"
tags: [quant-source, ml-forecasting, decoder-only-transformer, ordinal-returns, probabilistic-forecasting, baselines]
concepts: [continuous-input-transformer, ordinal-return-buckets, mixture-of-market-states, likelihood-vs-utility]
---

# VAIOM Continuous-Input Discrete-Output Financial Sequence Modeling

## Citation / Link

Yiming Ma, Xinyu Chen, “VAIOM: Continuous-Input, Discrete-Output Decoder-Only Financial Sequence Modeling,” arXiv:2607.13929v1, 2026-07-15. https://arxiv.org/abs/2607.13929v1

## Summary

VAIOM is a decoder-only Transformer for probabilistic next-return modeling on one-hour foreign-exchange bars. The model keeps continuous multivariate financial-event vectors as inputs while predicting a categorical distribution over volatility-normalized next-return buckets. The abstract reports that models and preprocessing were fit using pre-2024 training data, selected on 2024H2 validation, and evaluated without refitting on two 2025 test periods. Across three seeds, every evaluated model beat a fixed single-bar LightGBM baseline in return likelihood; the canonical checkpoint improved paired test likelihood by 0.029 and 0.043 bits per event.

## Core Contribution

- Separates continuous financial inputs from discrete probabilistic output buckets instead of forcing all observations into tokenized symbolic inputs.
- Provides a useful architecture pattern for density/ordinal return forecasting: continuous event features, categorical asset metadata, mixture-of-market-states return head, volatility-regime and ordinal auxiliary objectives, and full-sequence supervision.
- Includes explicit train/validation/test timing: pre-2024 train, 2024H2 validation, and two 2025 test periods.
- Compares against a simple LightGBM baseline, which is better than many finance-transformer abstracts, though downstream trading utility is not established from the abstract.

## Practical Relevance

- Classification: **Plausible but untested at abstract level as ML return-density methodology; foundational / retail-adaptable**.
- Not yet a strategy signal. The reported gains are likelihood gains, not net trading performance, portfolio utility, or cost-adjusted PnL.
- Useful as a design lead for distributional-output-first ML: start with volatility-normalized ordinal buckets and strong tabular baselines before testing larger sequence models.
- Retail adaptation should be conservative: reproduce the ordinal-return likelihood task on liquid FX/crypto/ETF hourly data, then test whether better likelihood improves sizing, filtering, or risk controls after costs.

## Methods and Data

Abstract-level details:

- Data: one-hour foreign-exchange bars and continuous multivariate event vectors.
- Train/validation/test: pre-2024 training, 2024H2 validation, two 2025 test periods, no test refit.
- Architecture: decoder-only Transformer with continuous event features, categorical asset metadata, mixture-of-market-states return head, gap/volatility-regime/ordinal auxiliary objectives, and full-sequence supervision.
- Objective: categorical likelihood / cross-entropy over volatility-normalized next-return buckets.
- Baseline: fixed single-bar LightGBM.

## Leakage / Bias / Overfitting Concerns

- The abstract does not establish point-in-time feature availability, transaction costs, or downstream trading utility.
- Likelihood improvements of a few hundredths of a bit per event may or may not be economically material.
- Architecture choices and validation selection can overfit 2024H2 if many variants were tested.
- FX hourly bars do not guarantee transfer to equities, options, or crypto; crypto and equities require delisting/session/venue controls.

## Transaction Cost / Capacity Treatment

No transaction-cost result is visible from the abstract. Any trading translation must compare likelihood improvements against cost-aware decisions: thresholded trades, volatility targeting, turnover limits, maker/taker or spread/slippage assumptions, and simple non-ML baselines.

## Strategy Ideas Extracted

- Minimum viable research task: ordinal-bucket next-return likelihood on hourly FX or crypto with LightGBM, logistic/linear, momentum/reversal, and volatility-only baselines.
- Only after likelihood replication: test whether forecast distribution improves expected-utility sizing, trade skipping, or risk throttling net of costs.
- Use output-bucket calibration and regime-specific log loss before any directional accuracy claim.

## Connections to Existing Research

### Reinforces

- [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]]: output likelihood design and distributional heads may matter more than backbone novelty.
- [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]: likelihood/calibration is a more honest scoreboard than raw hit rate, but still must connect to economic utility.
- [[Forecasting Realized Volatility with Time Series Foundation Models]]: foundation/sequence models need econometric and tabular baselines.
- [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]]: complex sequence models must beat simple baselines and fees, not just headline metrics.

### Contradicts / Weakens

- Does not yet weaken the library's sequence-model skepticism because the abstract reports likelihood rather than net trading utility and uses FX rather than the user's priority assets.

### Transfers Across Asset Classes or Domains

- The continuous-input / ordinal-output pattern may transfer to crypto hourly returns or ETF intraday bars, but only with venue/session, delisting, spread, and fee controls.

### Missing Validation or Method Supplied

- Supplies a candidate benchmark design for probabilistic return modeling: volatility-normalized buckets, LightGBM baseline, rolling temporal splits, multiple seeds, and test-period separation.

## Framework Potential

- Candidate framework: Distributional-forecast-first ML strategy evaluation.
- Linked notes: [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]], [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]], [[Forecasting Realized Volatility with Time Series Foundation Models]], [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]].
- Testable composite hypothesis: ordinal/distributional return models can improve downstream allocation or trade filtering only when likelihood/calibration gains survive across assets/regimes and reduce economically relevant loss after costs.
- Minimum viable validation: compare VAIOM-like output buckets against LightGBM/logistic/linear/momentum/volatility baselines using log loss, calibration, CRPS-like scoring where applicable, turnover, and net utility.
- What would falsify this connection? Better likelihood fails to improve sizing/trade decisions net of costs or collapses under held-out assets/regimes.

## Keep / Reject Decision

Keep as a medium-importance ML methodology source. Do not promote to the coding queue; it is a benchmark-design lead, not a ready strategy.

## Related Notes

- [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]]
- [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]
- [[Forecasting Realized Volatility with Time Series Foundation Models]]
- [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]]
