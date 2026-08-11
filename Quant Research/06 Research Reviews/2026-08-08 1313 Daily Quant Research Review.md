---
type: daily-quant-research-review
date: 2026-08-08
time: "13:13 EDT"
source_status: partial
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review]
---

# 2026-08-08 1313 Daily Quant Research Review

## Run Status

- Primary feed state used: `blogwatcher-cli` pre-run context with persistent DB `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Feed coverage: 6 of 7 blogs scanned successfully. Quantocracy failed with HTTP 302, so practitioner/RSS coverage is partial. The stdlib fallback RSS scanner was **not** used.
- Direct validation performed this run:
  - Alpha Architect article `https://alphaarchitect.com/anomaly-returns/` fetched successfully and parsed for the skewness/anomaly lead.
  - arXiv API `id_list` validation for arXiv:2608.05991v1, arXiv:2608.06048v1, and arXiv:2608.06206v1.
- Semantic Scholar lookups for arXiv:2608.05991 and arXiv:2608.06206 returned HTTP 429. Citation counts were not fabricated.
- Many feed items were already seen and/or already saved in recent runs; today promoted only two useful additions.

## Executive Summary

Today produced two useful source notes. [[Skewness Managed Anomaly Portfolios]] is the actionable equity/factor addition: the validated Alpha Architect article suggests many anomaly returns are heavily shaped by rare positive-return outliers and that expected-skewness tilts may improve anomaly legs, but the original paper was not inspected, so classification remains conservative. [[Localized Conformal Prediction for Conditional Forecast Calibration]] is a foundational adjacent-method addition: it strengthens the forecast-uncertainty framework by requiring local/feature-conditional coverage checks before conformal intervals are used for sizing, kill-switches, or model promotion.

Coding queue reviewed: unchanged. Neither item yet supplies a complete backtest specification with fully inspected rules, data path, friction assumptions, baselines, and go/no-go criteria.

## Candidate Triage

| Candidate | Classification | Practicality | Decision | Notes |
|---|---|---|---|---|
| [[Skewness Managed Anomaly Portfolios]] | Plausible but untested from practitioner summary | retail-adaptable / foundational | **Saved source note; registry updated** | High-signal as an anomaly validation overlay and outlier-dependence diagnostic. Need original paper inspection before coding. |
| [[Localized Conformal Prediction for Conditional Forecast Calibration]] | Evidence-backed at abstract level as statistical validation methodology | foundational / retail-adaptable | **Saved source note; registry updated** | Useful for ML/volatility/VaR/sizing validation; not alpha. Adds local coverage gates by regime, asset group, liquidity, option quote state, crypto venue state, and post-publication window. |
| Knowledge-Optimising Investment Decisions with Informative Datasets | Speculative / low-actionability from abstract | foundational only if later formalized | **Not saved** | Direct arXiv abstract is high-level decision-process theory with no clear falsifiable trading/backtest improvement beyond existing validation-budget framework. |
| Thermodynamic statistics of given names in USA and France | Rejected for current scope | not applicable | **Not saved** | q-fin.ST cross-list but unrelated to equities/options/crypto strategy design or validation. |
| Previously saved 2026-08-06/07 arXiv leads | Already in library | varies | **No duplicate notes** | Recent notes already cover public trader identity, AutoQuant, GMADL, multifractal allocation, options manipulation velocity, and sector-LSTM leads. |

## Source Notes Created or Updated

- Created: [[Skewness Managed Anomaly Portfolios]]
- Created: [[Localized Conformal Prediction for Conditional Forecast Calibration]]

## Literature Connections / Framework Leads

### Reinforces

- [[Skewness Managed Anomaly Portfolios]] reinforces [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]], [[A Cap-Axis Integral Diagnostic of Factor Models]], and [[Retail Traders Ruin - Anatomy of Popular Signal Failure]]: anomaly research needs outlier contribution, cap/size exposure, lottery-demand, costs, and post-publication decay controls before a factor edge is trusted.
- [[Localized Conformal Prediction for Conditional Forecast Calibration]] reinforces [[Conformal Kelly - Uncertainty-Scaled Fractional Position Sizing]], [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]], [[Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters]], and [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]]: global coverage is not enough if forecast intervals fail exactly where the strategy trades risk.

### Contradicts / Weakens

- The skewness/anomaly lead weakens mean/Sharpe-only anomaly evaluation. If returns collapse after capping a small number of right-tail observations, the anomaly may be an outlier/capacity bet rather than a stable premium.
- The localized conformal paper weakens global-conformal claims that report marginal coverage without state-specific coverage, interval-width, and downside-miss diagnostics.

### Transfers Across Asset Classes

- Skewness diagnostics may transfer to options and crypto only as tail-contribution and payoff-asymmetry audits; execution frictions and tail risk are too large for direct transfer without explicit rules.
- Localized conformal calibration transfers naturally to equities, options, crypto, and portfolio forecasts as a validation layer for uncertainty-aware sizing and model promotion.

### Missing Link Supplied

- Equity anomaly validation now has a concrete right-tail/outlier audit: percentile cap tests, tail-contribution reports, within-leg expected-skewness tilts, and state-conditional performance.
- Forecast-uncertainty validation now has a sharper local coverage target: intervals must be checked in the predeclared states that matter for decisions, not only across the full sample.

## Registry / Framework / Queue Changes

- Candidate registry updated with:
  - Skewness-managed equity anomaly overlay.
  - Localized conformal forecast-calibration gate.
- Source Index updated with both new source notes.
- Framework Candidate Registry updated with two 2026-08-08 framework notes.
- Open Research Questions updated with one skewness/anomaly question and one localized-conformal calibration question.
- Coding-ready queue reviewed and left unchanged.

## Backtest / Validation Implications

1. Before coding old or new equity anomalies, add outlier-dependence panels: percentile-capped returns, tail contribution to CAGR/Sharpe, skewness exposure, microcap/liquidity/borrow filters, and post-publication splits.
2. If a baseline anomaly already exists, test a within-leg skewness overlay only after inspecting the original Gong-Lynch-Ogden paper and freezing ex ante skewness predictors.
3. Add local coverage panels to ML/volatility/VaR forecasts by predeclared states: volatility, drawdown, liquidity, asset group, option quote quality, crypto venue quality, and post-publication window.
4. Treat localized conformal alarms as useful only if action attribution shows better net utility than simple rolling coverage, volatility, drawdown, and liquidity filters after turnover and false-exit costs.

## Hygiene Check

Post-write hygiene completed after creating notes and patching indexes/registries.

- Exact source-note files exist for [[Skewness Managed Anomaly Portfolios]] and [[Localized Conformal Prediction for Conditional Forecast Calibration]].
- Exact review note file exists for [[2026-08-08 1313 Daily Quant Research Review]], and Research Review Index links to it.
- New source-note titles appear in Source Index, Candidate Registry, Framework Registry, and this review note as intended.
- Open Research Questions uses the new framework questions as plain text rather than wikilinks, which is intentional because they are question text rather than separate notes.
- Link probe across the new review, new source notes, Source Index, Candidate Registry, Framework Registry, Open Questions, Review Index, and Coding Queue found no new missing wikilink targets. One pre-existing path-style link target in Candidate Registry (`Quant Research/04 Backtest Specs/Backtest Spec Index`) remains unrelated to this run.
- Vault-root zero-byte markdown check returned `[]`.
- Coding queue unchanged.
