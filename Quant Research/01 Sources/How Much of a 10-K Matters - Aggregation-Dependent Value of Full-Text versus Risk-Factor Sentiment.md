---
type: source-note
source_kind: paper
asset_classes: [equities, volatility, text-data]
implementation_class: retail-adaptable / foundational
importance: medium
last_reviewed: 2026-07-17
tags: [quant-source, 10-k, sentiment, volatility, text-features]
concepts: [regulatory-disclosure sentiment, aggregation dependence, volatility labels]
---

# How Much of a 10-K Matters - Aggregation-Dependent Value of Full-Text versus Risk-Factor Sentiment

## Citation / Link

Sanggyu Sean Choi, “How Much of a 10-K Matters? Aggregation-Dependent Value of Full-Text versus Risk-Factor Sentiment,” arXiv:2607.14174v1, 2026-07-15. https://arxiv.org/abs/2607.14174

## Summary

Extends supervised lexicon learning to 10-K filings and Item 1A risk-factor sections, training sentiment against both return and realized-volatility labels at sector, portfolio, and individual-firm aggregation levels. In a sample of 1,383 filings from 94 Nasdaq-100 technology constituents from 2006–2023, full-filing text performs better at sector/portfolio levels, while Item 1A performs better at individual-firm level. A Loughran-McDonald dictionary baseline is strongly negatively correlated with price in the tested setup.

## Core Contribution

Shows that the usefulness of regulatory filing text depends on aggregation level and target variable. Volatility-labeled sentiment may be more natural than return-labeled sentiment for risk disclosures.

## Practical Relevance

- Retail-adaptable / foundational.
- EDGAR filings are public and timestamped, but building a clean, point-in-time filing/text pipeline is nontrivial.
- Most useful as a volatility/risk feature lead, not immediate directional alpha.

## Methods and Data

10-K full text and Item 1A risk-factor sections; supervised lexicon learning; Nasdaq-100 technology constituents; 2006–2023; labels include returns and realized volatility; evaluations by classification accuracy, correlations with realized outcomes, and lexical inspection.

## Leakage / Bias / Overfitting Concerns

- Nasdaq-100 technology-only sample creates selection and sector concentration risk.
- Current constituent lists can introduce survivorship if not reconstructed point-in-time.
- Filing availability timestamps matter: use filing acceptance time plus conservative execution lag.
- Supervised lexicons trained on return/vol labels can overfit if evaluated in-sample or without firm/time splits.

## Transaction Cost / Capacity Treatment

Not primarily an execution paper. Any trading translation must be low-turnover around annual filings and tested after spreads, borrow constraints for shorts, sector/size/momentum controls, and event-window capacity.

## Strategy Ideas Extracted

Test a filing-based volatility-risk screen: after 10-K release, compare full-text versus Item 1A supervised sentiment as predictors of next-quarter realized volatility or idiosyncratic volatility. Use sector-neutral portfolios or risk-sizing overlays, not raw long/short sentiment, until evidence supports return predictability.

## Connections to Existing Research

### Reinforces

- [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]
- Distributional-forecast-first ML strategy evaluation is a framework label tracked in [[Framework Candidate Registry]].

### Contradicts / Weakens

Weakens generic dictionary-sentiment claims when the dictionary is not trained/evaluated for the target and aggregation level.

### Transfers Across Asset Classes or Domains

Transfers text-feature design into volatility/risk forecasting rather than directional return prediction.

### Missing Validation or Method Supplied

Supplies an aggregation-level warning: sector/portfolio/firm-level labels should not be pooled blindly.

## Framework Potential

- Candidate framework: distributional/text-risk feature validation.
- Linked notes: [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]], [[Forecast-uncertainty-aware ML asset pricing]].
- Testable composite hypothesis: public regulatory text adds more reliable volatility/risk information than directional return alpha when evaluated point-in-time and aggregation-aware.
- Minimum viable validation: point-in-time 10-K sample, filing-lag execution rule, full-text vs Item 1A features, realized-volatility target, base-rate and volatility-only baselines, sector-neutral robustness.
- What would falsify this connection? No incremental predictive value beyond lagged volatility, size, sector, momentum, and filing-date seasonality in held-out firms/years.

## Keep / Reject Decision

Keep as Plausible but untested for local use; Evidence-backed at abstract level as a text-feature design finding. Practicality: retail-adaptable / foundational.

## Related Notes

- [[Framework Candidate Registry]]
- [[2026-07-17 0802 Daily Quant Research Review]]
