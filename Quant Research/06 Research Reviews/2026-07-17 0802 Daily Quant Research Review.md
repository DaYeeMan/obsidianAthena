---
type: daily-quant-research-review
date: 2026-07-17 0802
source_status: degraded
script_status: "primary data-collection script timed out after 120s"
tags: [quant-research, daily-review]
---

# 2026-07-17 0802 Daily Quant Research Review

## Run Status

The primary data-collection script failed before this run started:

```text
Script timed out after 120s: C:\Users\enson\AppData\Local\hermes\profiles\quant-researcher\scripts\quant_research_collect_sources.py
```

Because `blogwatcher_feed_leads` were unavailable, this review used direct arXiv validation only. No practitioner/RSS feed items were treated as evidence today.

## Context Checked

- Existing [[01 Research Candidate Registry]] through 2026-07-16.
- Existing [[Framework Candidate Registry]] and [[Open Research Questions]].
- Existing [[09 Coding-Ready Backtest Queue]].

## High-Signal Items Kept

### 1. [[SciPhy Reinforcement Learning for Portfolio Optimization]]

- Source: arXiv:2607.15195v1, 2026-07-16, q-fin.PM. https://arxiv.org/abs/2607.15195
- Classification: Plausible but untested as local allocation improvement; Evidence-backed at abstract level as methodology.
- Practicality: foundational / retail-adaptable; original framing is closer to institutional allocation.
- Why it matters: explicitly combines cumulative costs, target holdings, volatility control, and policy learning in an HJB/PINN framework. It reinforces the library rule that AI/RL allocation policies must be evaluated as cost-aware decision processes, not just forecast-score or gross-return contests.
- Decay/failure modes: engineered oracle signal may dominate results; PINN/RL complexity can overfit; cost coefficients and turnover stress must be validated out of sample.
- Validation priority: use as a benchmark-design note for future ETF/futures allocation ML. Start with equal weight, inverse-vol/risk parity, myopic mean-variance, and linear parametric policies before any RL/PINN layer.

### 2. [[How Much of a 10-K Matters - Aggregation-Dependent Value of Full-Text versus Risk-Factor Sentiment]]

- Source: arXiv:2607.14174v1, 2026-07-15, cs.LG/q-fin.CP/q-fin.MF/q-fin.ST. https://arxiv.org/abs/2607.14174
- Classification: Plausible but untested for local strategies; Evidence-backed at abstract level as text-feature design evidence.
- Practicality: retail-adaptable / foundational because EDGAR filings are public, but point-in-time text processing is nontrivial.
- Why it matters: suggests regulatory-disclosure sentiment may be more reliable for volatility/risk than directional alpha, and that full-text versus Item 1A usefulness depends on sector/portfolio/firm aggregation.
- Decay/failure modes: Nasdaq-100 technology-only sample, survivorship risk, filing-timestamp leakage, and supervised-lexicon overfit.
- Validation priority: test as a low-turnover filing-based realized-volatility or risk-sizing feature, not as immediate long/short sentiment alpha.

### 3. [[Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring]]

- Source: arXiv:2607.12407v1, 2026-07-14, q-fin.ST/stat.ML. https://arxiv.org/abs/2607.12407
- Classification: Evidence-backed at abstract level as monitoring methodology.
- Practicality: foundational / retail-adaptable.
- Why it matters: reframes PSI/Jensen-Shannon/KL drift metrics as power/type-I-error choices. This is useful for ML feature drift, option-chain quality, crypto exchange-quality diagnostics, and live-model kill-switch design.
- Decay/failure modes: drift alarms can duplicate volatility filters, overfire in benign regimes, or reduce net utility unless tied to action attribution.
- Validation priority: compare PSI/JSD/KL alarms on forecast residuals and feature distributions against rolling coverage, volatility/drawdown filters, and net-utility outcomes.

## Screened but Not Promoted

### A Noise-Robust Elicit-to-Optimize Framework for Distortion Riskmetrics via Inverse Reinforcement Learning

- Source: arXiv:2607.14373v1.
- Classification: Plausible but untested / foundational.
- Reason not promoted: useful for risk-preference elicitation and distortion-risk RL, but it is too abstract for a near-term retail backtest and overlaps with existing uncertainty-aware decision-policy notes. Keep as a watch lead for risk-objective design.

### Minimizing Benchmark-Relative Drawdown Duration via Occupation Time Penalization

- Source: arXiv:2607.11335v1.
- Classification: Plausible but untested / foundational.
- Reason not promoted: interesting downside-risk objective for benchmark-relative underperformance duration, but currently a continuous-time control result rather than a coding-ready allocation rule. Watch for a discrete-time empirical implementation.

## Literature Connections / Framework Leads

### Reinforces

- Simple-rule benchmark-first AI portfolio-policy evaluation: SciPhyRL strengthens the requirement that AI portfolio policies report costs, turnover, policy path, volatility control, and simple-rule baselines.
- Cost-aware decision-process diagnostics: SciPhyRL and the divergence-monitoring paper both reinforce that decisions should be evaluated through action/cost/risk consequences, not only predictive fit.
- Distributional-forecast-first ML strategy evaluation: the 10-K sentiment paper shifts text features toward volatility/risk labels; the divergence paper adds calibrated drift monitoring around model inputs and residuals.

### Contradicts / Weakens

- Generic dictionary-based filing sentiment and return-only text alpha claims are weakened when aggregation level, target choice, and supervised validation are not specified.
- Fixed drift thresholds are weakened when sample size, false-alarm rate, and power are not stated.
- RL allocation papers without cost accumulation and simple-rule baselines remain low quality relative to the SciPhyRL framing.

### Transfers Across Asset Classes

- 10-K text sentiment is equity-specific, but the validation lesson transfers to other text/alternative-data features: choose the target and aggregation level before claiming alpha.
- Divergence-monitoring methods transfer from credit-risk monitoring to crypto exchange-quality flags, option-chain quote-quality checks, and ML forecast residual drift.

### Missing Link Supplied

Today’s best missing link is model-monitoring calibration: drift/feature alarms should be treated as statistical tests with power/false-positive trade-offs, then evaluated by action attribution.

## Registry / Queue Actions

- Candidate registry: updated with three new tracked candidates.
- Source notes: created three new source notes and added them to [[Source Index]].
- Framework registry/open questions: updated to include today’s cost-aware RL, filing-text volatility, and divergence-monitoring links.
- Coding queue: reviewed and left unchanged. None of today’s items specify enough falsifiable rules, data, costs, baselines, and go/no-go thresholds to promote directly.

## Hygiene Notes

- No fallback RSS scanner was used; direct arXiv API validation only.
- Wikilinks in new notes are intended to point to existing notes or notes created in this run.
- The collection-script timeout should be investigated separately because it blocks feed/practitioner coverage.
