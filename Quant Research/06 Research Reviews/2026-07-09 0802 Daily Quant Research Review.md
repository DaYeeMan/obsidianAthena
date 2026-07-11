---
type: daily-quant-research-review
date: 2026-07-09 0802
created: 2026-07-09
tags: [quant-research, daily-review, arxiv, ml-validation, covariance, portfolio-risk]
---

# 2026-07-09 0802 Daily Quant Research Review

## Scope and Inputs

- Pre-run collector used the persistent `blogwatcher-cli` database at `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Blogwatcher scan succeeded for 5/7 feeds; Quantocracy returned HTTP 302 and Quantpedia returned HTTP 429. No fallback RSS scanner was used.
- New arXiv/feed leads were treated as discovery inputs only and validated through the arXiv API before being saved.
- Existing registry and framework context were checked for overlap before adding notes.

## High-Signal Items Saved

| Item | Source | Classification | Practicality | Why it matters | Library action |
|---|---|---|---|---|---|
| [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]] | arXiv:2607.06690v1 | Evidence-backed at abstract level as methodology/software | foundational / retail-adaptable | Provides dependence-aware bootstrap and adaptive conformal calibration for financial time-series forecasts, where IID intervals under-cover. | New source note; candidate registry row; distributional-forecast framework updated. |
| [[Iterative Detection of Global Factors near the BBP Phase Transition]] | arXiv:2607.06908v1 | Evidence-backed at abstract level as statistical methodology | foundational / retail-adaptable | Adds participation-ratio/eigenvector delocalization to global-factor detection near the random-matrix phase transition; useful for calibrated covariance/risk-state dashboards. | New source note; candidate registry row; framework/open-question updates. |

## Screened but Not Promoted

| Lead | Classification | Reason |
|---|---|---|
| Dynamic Causal Portfolio Choice: Hedging the Rotation of the Common-Driver Manifold, arXiv:2607.06702v1 | Speculative / foundational watch | Interesting geometric portfolio-control model, but abstract validation is synthetic and continuous-time. No direct retail-testable rule yet. Keep as a watch item for causal-driver/state-variable portfolio research, not a registry candidate today. |
| ContestTrade: A Multi-Agent Trading System Based on Internal Contest Mechanism, arXiv:2508.00554v4 | Low quality / speculative as trading evidence | LLM multi-agent trading backtest claims on post-2024 A-shares are not enough without full leakage controls, costs, baselines, decision logs, and market-access realism. It reinforces the existing need for cost-aware time-gated LLM portfolio-agent evaluation, but does not deserve a source note. |
| Multi-Trigger Crypto CAT Bonds with On-Chain Settlement, arXiv:2607.06981v1 | Plausible but out-of-scope / institutional product design | More insurance/structured-product design than systematic trading. Interesting for crypto operational-risk transfer, but no actionable alpha/risk-control path for the current equities/options/crypto backtest library. |
| Mitigating the Winner's Curse While Controlling Multiplicity, arXiv:2607.07699v1 | Adjacent method lead | Anytime-valid inference and selection-charge ideas are relevant to strategy selection and multiple testing, but the paper is a clinical-trial method lead. Captured as a connection in open questions rather than a source note. |
| Robust Inference for Weighted Estimands, arXiv:2607.07524v1 | Adjacent method lead | Potentially useful for event-study weighting sensitivity, but not enough direct quant connection today to create a note. |
| On the Robustness in Data-Driven Nonlinear Optimal Control, arXiv:2607.07570v1 | Adjacent method lead | Potentially relevant to model-mismatch robustness for learned trading policies, but too abstract for promotion without a trading-system translation. |

## Literature Connections / Framework Leads

### Reinforces

- [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]] reinforces [[Forecast-uncertainty-aware ML asset pricing]] and [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]] by supplying implementation-oriented dependence-aware uncertainty intervals.
- [[Iterative Detection of Global Factors near the BBP Phase Transition]] reinforces [[Error Propagation in Spectral Functionals of Shrinkage Covariance Estimators]]: eigenstructure/risk-state diagnostics need uncertainty calibration before they become allocation triggers.

### Supplies Missing Validation

- `tsbootstrap` supplies a practical resampling/conformal toolkit for the distributional-forecast-first ML strategy evaluation framework. The key test is not coverage alone; it is whether dependence-aware uncertainty improves downstream turnover-adjusted utility or go/no-go decisions.
- The BBP/global-factor paper supplies a concrete factor-count diagnostic for calibrated spectral covariance and absorption-ratio risk diagnostics.

### Contradicts / Weakens

- ContestTrade weakens confidence in raw “LLM trading agent beats baselines” narratives unless the benchmark has time-gated inputs, costs, audit trails, and transparent simple-rule baselines. It was not promoted.

### Framework Potential

- No new standalone framework was created. Existing frameworks were strengthened:
  - Distributional-forecast-first ML strategy evaluation now has an explicit dependence-aware bootstrap/conformal implementation lead.
  - Regime-conditional distributional strategy evaluation and calibrated covariance diagnostics now have an additional high-dimensional factor-count/eigenvector-delocalization diagnostic.

## Candidate Registry Updates

Added two tracked candidates:

1. Dependence-aware bootstrap and conformal forecast validation for financial time series.
2. High-dimensional global-factor detection for covariance/risk-state dashboards.

Updated related sorting/decay context by noting that IID bootstrap/conformal intervals can under-cover under dependence and that rolling global-factor/eigenstructure signals can be noisy and turnover-inducing if used as raw regime triggers.

## Coding Queue Review

Coding queue reviewed and left unchanged. Neither new item is coding-ready as a standalone strategy. Both are better used as validation/risk-dashboard modules after a baseline forecast or allocation backtest exists.

## Practical Next Steps

- For the first ML/volatility forecast pipeline, compare IID intervals against block/sieve bootstrap and adaptive conformal intervals; require coverage plus downstream net utility.
- For any portfolio/risk dashboard, evaluate retained global-factor count alongside absorption ratio, leading-eigenvalue share, and uncertainty bands; do not convert it into a trade trigger until it beats simple volatility/drawdown filters after turnover costs.
- Continue treating LLM trading-agent papers as governance warnings unless they satisfy TimeGate, costs, audit-trail, and simple-rule benchmark requirements.

## Hygiene Check

- New source notes created under `01 Sources/`; no root-level notes were intentionally created.
- Source Index updated with both new source notes.
- Research Review Index updated with this timestamped review.
- Candidate registry updated; coding queue unchanged.
- Framework registry and open questions updated; no unresolved framework wikilinks were intentionally introduced.
