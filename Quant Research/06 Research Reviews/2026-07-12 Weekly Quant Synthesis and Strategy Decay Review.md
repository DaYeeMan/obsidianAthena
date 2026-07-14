---
type: weekly-synthesis-decay-review
date: "2026-07-12"
created: 2026-07-12 0900 EDT
profile: quant-researcher
tags: [weekly-review, synthesis, decay-review, cron]
---

# Weekly Quant Synthesis and Strategy Decay Review — 2026-07-12

## Executive Summary

This weekly pass reviewed the candidate registry, coding queue, framework registry, open questions, source notes, and daily reviews from 2026-07-07 through 2026-07-12, with the prior 2026-07-05 weekly review as the baseline.

The library is still behaving correctly: the strongest additions are **research-governance, execution-cost, options-data, covariance/risk-state, prediction-market microstructure, and uncertainty-validation methods**, not easy standalone alpha. The key synthesis decision is to keep the coding queue concentrated on reusable validation infrastructure and the SPX fixed-risk baseline, while resisting premature promotion of option-implied SDF timing, driver-manifold rotation, structural prediction-market volatility, or AI/deep learning policy papers.

Main decisions:

1. **Preserve SPX/SPXW short-dated put-writing as the highest strategy-priority item, but keep it data/spec-blocked.** New option-implied SDF and arbitrage-free risk-neutral marginal papers are useful upgrades to the future risk-throttle layer, not a reason to skip the fixed-risk bid/worse-fill baseline.
2. **Tighten crypto/ML decay treatment.** Price-only crypto deep learning and fast crypto lead-lag/network claims remain outdated-watch/low priority unless they beat slow-horizon, fee-aware, delisting-controlled simple baselines. The recent TSFM, tsbootstrap, and CryptoGAT evidence all argue for benchmark-first validation rather than architecture-first strategy research.
3. **Upgrade the standard audit block conceptually, not by adding more strategies to the queue.** The queue item should now explicitly cover TimeGate/availability checks, action-attribution, manipulation-like RL/execution diagnostics, dependence-aware uncertainty intervals, calibrated covariance/risk-state bands, and microstructure-conditioned cost/regime slices.
4. **Create one new framework candidate: validation-budget and value-of-information audit triage.** Adjacent-domain PPAT/design-based testing leads are not trading evidence, but they can improve how scarce manual labels, option-chain cleaning, data-vendor reviews, and suspected-leak audits are prioritized.
5. **Do not promote recent driver-manifold, structural prediction-market volatility, low-turnover sparse tracking, or option-implied SDF ideas into the coding queue.** Each is useful, but each still lacks either accessible data, a minimum executable rule, or evidence of downstream net utility versus simple baselines.

## Registry and Queue Decisions

| Item | Decision | Rationale | Next Action |
|---|---|---|---|
| [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] | Preserve as High priority, but keep as research-spec/data-blocked | Strong economic rationale from volatility risk premium, but 0DTE market-structure change, bid/ask realism, margin, crash gaps, and option-chain availability dominate any sizing sophistication | Code only a fixed-risk baseline spec first: bid/worse fills, cash/margin, expiration buckets, regime splits, crash scenarios, and audit-block outputs |
| [[Option-Implied SDF Equity Premium Timing]] | Preserve as medium research candidate; do not queue | It may improve risk throttling once SPX option-chain infrastructure exists, but option-implied risk-neutral objects can be interpolation- and crisis-sample-sensitive | Treat as a later throttle after VIX, IV-rank, skew, realized-vol, drawdown, and Martin-bound-style baselines |
| [[Prediction-Market Structural Volatility Risk Filter]] | Preserve as medium candidate; not queue-ready | Structural volatility variables are promising but require historical contract panels, spreads, fees, venue tags, and leakage-safe resolution metadata | Keep as a data-dependent risk-filter candidate, not a directional alpha |
| Driver-manifold rotation as portfolio risk diagnostic | Preserve as foundational / low-medium coding priority | The mechanism connects covariance/eigenstructure to causal-driver rotation, but evidence is abstract/synthetic and driver choice can be data-mined | Use only as a diagnostic after defining ex ante drivers and comparing to volatility/drawdown/correlation filters; primary note is [[Dynamic Causal Portfolio Choice - Hedging the Rotation of the Common-Driver Manifold]] |
| CryptoGAT / price-only crypto sequence-model skepticism | Downgrade coding priority from Medium to Low | Newer evidence reinforces that crypto DL claims need strong simple baselines and fees; price-only models are high-decay and easily overfit | Keep as a warning/reference; code only if part of a benchmark suite against momentum, carry/funding, basis, and naive rules |
| Standard cost/regime/liquidity/decision audit block | Keep in coding queue; broaden scope | Multiple recent papers supply concrete audit modules: temporal non-interference, RL manipulation diagnostics, action attribution, dependence-aware bootstrap/conformal intervals, and calibrated covariance bands | Implement as reusable report infrastructure before adding complex strategy variants |

## Cross-Paper / Framework Synthesis

### 1. Options path: option-implied information should be a later risk-throttle layer, not the first backtest

- [[Arbitrage-Free Multi-Maturity Risk-Neutral Marginals]] supplies a cleaner way to build implied distributions from discrete option chains.
- [[Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium]] suggests option-implied SDF features may forecast the equity premium.
- [[Forecasting Realized Volatility with Time Series Foundation Models]] and [[Risk-Sensitive Specialist Routing for Volatility Forecasting]] warn that volatility/risk forecasts must beat EWMA/GARCH/Log-HAR/simple filters and improve downstream utility.

**Synthesis:** the SPX put-writing research path should remain staged:

1. fixed-risk short-put baseline with executable bid/worse fills;
2. simple VIX/IV-rank/skew/realized-vol/drawdown risk filters;
3. only then arbitrage-clean implied-distribution/SDF features;
4. validate net utility and crash behavior, not forecast score alone.

**Decay warning:** crowded short-vol and 0DTE market-structure changes mean any sizing method can look good before fees/margin/crash paths and fail live.

### 2. Risk-state dashboards need uncertainty calibration before becoming allocation rules

- [[Error Propagation in Spectral Functionals of Shrinkage Covariance Estimators]] warns that absorption-ratio/eigenspace movement can be estimator noise.
- [[Iterative Detection of Global Factors near the BBP Phase Transition]] adds factor-count/eigenvector-delocalization diagnostics near random-matrix phase transitions.
- [[Dynamic Causal Portfolio Choice - Hedging the Rotation of the Common-Driver Manifold]] supplies an economic mechanism for driver-geometry rotation.
- [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]] adds dependence-aware uncertainty tooling.

**Synthesis:** covariance, global-factor-count, and driver-rotation signals should be treated as **risk-state covariates with uncertainty bands**, not automatic risk-off triggers. Any allocation use must beat volatility targeting, drawdown filters, equal weight, inverse-vol, risk parity, and Ledoit-Wolf-style baselines after turnover costs.

### 3. Prediction-market research should model venue design and structural volatility before settlement-window trading claims

- [[Settlement Manipulation in Prediction Markets]] supplies the event-window manipulation warning.
- [[Volatility in Prediction Markets - A Structural Approach]] adds probability-level, time-to-resolution, spread, volume, and category variables.
- [[SoK - Market Microstructure for Decentralized Prediction Markets]] explains why venue/resolution/settlement design cannot be pooled casually.

**Synthesis:** prediction-market backtests should begin with risk/volatility filters and venue-design tags. Directional settlement-window alpha is lower priority until fill probability, spreads, fees, resolution timing, and manipulation/venue design are modeled.

### 4. Adjacent-domain method transfer: validation-budget and value-of-information triage

Selected adjacent-domain leads this week:

- `Prediction-Powered Active Testing` (arXiv:2607.08347v1): label-efficient unbiased risk estimation using black-box predictions as control variates.
- `A Design-Based Approach to Testing and Inference in (Quasi-)Experiments with Spillovers` (arXiv:2607.08640v1): data-informed exposure-measure testing under network/spatial dependence.
- `Finite-Population Inference for Heterogeneity in Many-Group Synthetic Difference-in-Differences` (arXiv:2607.08324v1): heterogeneous effect inference with shared donor dependence.

These are **not trading evidence**. Their useful quant transfer is narrower: decide where scarce validation resources should go. Examples:

- which option-chain quotes/months deserve manual cleaning first;
- which suspicious backtest periods deserve planted-leak or point-in-time audit;
- which strategy families need more expensive data before coding;
- which event-study exposure definitions or spillover/network measures survive orthogonality/robustness checks.

This becomes a new **Watch** framework candidate, not a coding-queue promotion.

## Decay Review

### High decay / do not code before guardrails

- 0DTE/short-dated option-selling variants without bid/worse fills, margin/cash treatment, crash paths, and post-2023/0DTE regime splits.
- Price-only crypto deep learning and fast crypto network/lead-lag claims without fees, latency, delistings, false-discovery control, and simple momentum/funding/basis baselines.
- AI/LLM/RL trading-agent results without TimeGate inputs, audit trails, costs, manipulation-like action checks, and simple-rule benchmarks.
- Raw absorption-ratio/global-factor-count/driver-rotation regime triggers without uncertainty bands and turnover-cost comparisons.
- Prediction-market event-window trades that ignore resolution/settlement design, spreads/fees, stale quotes, and venue-specific liquidity.

### Foundational items to preserve

- Formal look-ahead-freedom / temporal non-interference checks.
- Cost-aware decision-process diagnostics and action attribution.
- Dependence-aware bootstrap/conformal forecast validation.
- Calibrated covariance/eigenstructure/risk-state diagnostics.
- Arbitrage-clean option-implied distributions and SDF features.
- Microstructure-conditioned trend/reversal/liquidity decay diagnostics.
- Simple-rule benchmark-first AI portfolio-policy evaluation.

## Coding Queue Review

Queue reviewed and kept intentionally narrow.

- **Updated:** Standard cost/regime/liquidity/decision audit block remains the most immediately codeable infrastructure artifact. It should now include formal availability-time checks, planted-leak negative controls, manipulation-like RL/execution diagnostics, action-attribution for risk filters, block/sieve/conformal uncertainty intervals, and calibrated covariance/risk-state reporting.
- **Unchanged:** SPX short-dated put-writing remains high priority but research-spec/data-blocked.
- **Unchanged:** decision-aware covariance metrics and forecast-uncertainty-aware ML sizing remain method integrations, not standalone strategies.
- **Not promoted:** option-implied SDF timing, prediction-market structural volatility, low-turnover sparse tracking, and driver-manifold rotation.

## Framework Registry / Open Question Updates

- Added framework candidate: **Validation-budget and value-of-information audit triage** with Watch status.
- Open questions updated to explicitly include PPAT/control-variate active testing and design-based exposure testing as possible audit-prioritization methods.
- No weak metaphor-only adjacent-domain leads were promoted.

## Practical Next Steps

1. When coding resumes, implement the **standard audit block** before adding complex strategy variants.
2. For SPX/SPXW, write the fixed-risk baseline spec before VIX/Kelly/SDF/TSFM routing.
3. For any ML, covariance, or regime dashboard, record whether the added uncertainty/risk-state diagnostic improves **downstream net decision utility**, not only forecast or classification metrics.

## Hygiene Notes

- Candidate registry reviewed and patched for crypto/ML decay and SPX review status.
- Framework registry updated with one Watch framework candidate.
- Open questions updated with one validation-budget question.
- Coding queue patched to include the 2026-07-12 weekly note and broadened audit-block scope.
- Research Review Index updated with this weekly review link.
