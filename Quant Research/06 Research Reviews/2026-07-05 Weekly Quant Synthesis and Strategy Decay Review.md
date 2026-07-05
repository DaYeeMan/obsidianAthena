---
type: weekly-synthesis-decay-review
date: "2026-07-05"
profile: quant-researcher
tags: [weekly-review, synthesis, decay-review, cron]
---

# Weekly Quant Synthesis and Strategy Decay Review — 2026-07-05

## Executive Summary

This weekly pass reviewed the candidate registry, coding queue, framework registry, open questions, recent source notes, and daily research reviews from 2026-06-28 through 2026-07-05. The library is correctly accumulating mostly **validation, cost, decay, and risk-control research**, not raw alpha claims. That is a strength: the strongest recent papers are telling us how to avoid false positives before coding short-volatility, short-horizon trend/reversal, crypto ML, factor anomalies, or AI allocation policies.

Main decisions:

1. **Promote a standard backtest audit block to the coding queue** as a reusable implementation artifact. This is more immediately actionable than most new alpha leads: TimeGate/leakage checks, survivorship/replication guardrails, cost/liquidity diagnostics, regime-conditioned fold metrics, simple baselines, and decision-regret outputs can be added to future backtests.
2. **Add a new framework candidate: Microstructure-conditioned decay and liquidity-state validation.** This connects short-term trend decay, sign-vs-magnitude reversal diagnostics, liquidity premia, settlement manipulation, liquidity-demand audits, and liquidity-tail risk into one falsifiable validation layer.
3. **Downgrade crypto network/lead-lag ideas from Low/Medium to Low priority / outdated-watch unless slower-horizon, fee-aware, delisting-controlled designs are specified.** Current evidence is not enough to justify implementation before simpler crypto baselines.
4. **Preserve SPX short-dated put-writing as the highest strategy-priority item, but do not promote beyond “research spec needed.”** Its edge is plausible, but 0DTE market-structure change, bid/ask realism, margin treatment, crash tails, and data availability remain make-or-break blockers.
5. **Treat adjacent-domain imports as validation tools, not trading evidence.** Cross-audit projection, value-of-information validation, online safety monitoring, extreme-event transformers, granular IVs, and complex-network avalanche models are useful only if translated into concrete leakage, uncertainty, data-acquisition, or stress-test modules.

## Framework Candidates Added / Updated

| Framework | Linked Notes | Change | Next Validation Step |
|---|---|---|---|
| [[Framework Candidate Registry|Microstructure-conditioned decay and liquidity-state validation]] | [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]]; [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]]; [[Liquidity Premium and Investment Horizons]]; [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]; [[Liquidity-Based Audit of Algorithmic Trading Strategies]]; [[Settlement Manipulation in Prediction Markets]] | **Added** as a new framework. Mechanism: apparent short-horizon alpha and liquidity premia must be conditioned on tick size, spread/liquidity state, order-flow/volume tails, settlement windows, and post-market-structure-change periods. | For any trend/reversal/liquidity/settlement event study, report net performance by microstructure bucket, post-2009/0DTE/venue regime, liquidity-tail proxy, and spread/impact stress. |
| [[Framework Candidate Registry|Cost-aware decision-process diagnostics]] | Liquidity audit; CLQT; AI-agent anomaly guardrails; cap-axis diagnostics; decision-aware covariance; settlement manipulation; execution policy; liquidity-tail risk; trend decay | **Updated in interpretation**: this is now ready to become a reusable coding artifact rather than just a conceptual framework. | Implement a standard audit block in the first available backtest harness and require it before queue promotion of short-horizon, ML, factor, options, or crypto strategies. |
| [[Framework Candidate Registry|Distributional-forecast-first ML strategy evaluation]] | Heads Not Backbones; Forecast-uncertainty-aware ML; Risk-sensitive specialist routing; HMMs; CryptoGAT | **Preserved / no promotion**. Evidence supports methodology, but downstream trading utility remains unproven. | Test point vs density/quantile/conformal outputs only after simple baselines exist; measure CRPS/coverage plus turnover-adjusted utility. |
| [[Framework Candidate Registry|Simple-rule benchmark-first AI portfolio-policy evaluation]] | End-to-end portfolio policies; CLQT; regime-conditional evaluation; forecast uncertainty | **Preserved / no promotion**. Useful for future allocation ML, not a standalone coding priority today. | Implement equal weight, inverse-vol/risk parity, time-series momentum, and linear policies before LSTM/transformer allocation models. |

## Cross-Paper Connection Table

| Source A | Source B / Existing Candidate | Connection Type | Framework Potential | Action |
|---|---|---|---|---|
| [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]] | [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]] | Reinforces / decay warning | Strong: both weaken naive short-horizon trend/reversal claims when microstructure is ignored. | Add microstructure-conditioned decay framework. Require tick-size/liquidity and sign-vs-magnitude splits. |
| [[Liquidity Premium and Investment Horizons]] | [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]] | Mechanism bridge | Strong: liquidity premia and market impact may both be state-dependent, but high apparent returns may be concentrated in costly liquidity states. | Liquidity-premium tests must include liquidity-tail/cost-state diagnostics and small-cap trap controls. |
| [[Settlement Manipulation in Prediction Markets]] | [[Liquidity-Based Audit of Algorithmic Trading Strategies]] | Method transfer / event-risk audit | Medium/strong: settlement-window reversals are a special case where strategy profits may coincide with liquidity-demand pressure and market-design fragility. | Keep as event-study/risk-filter candidate, not immediate alpha. |
| [[A Cap-Axis Integral Diagnostic of Factor Models]] | [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]] | Missing validation / governance | Strong: published factor/anomaly evidence needs residual cap-rank diagnostics plus survivorship-free post-publication replication. | Add cap-axis diagnostics to anomaly replication guardrails. |
| [[Risk-Sensitive Specialist Routing for Volatility Forecasting]] | [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] | Method transfer | Medium: volatility underprediction loss is directly relevant to short-put sizing, but must beat VIX/EWMA/GARCH baselines. | Treat as later risk-throttle module, not first version. |
| [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]] | [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]] | Reinforces / benchmark discipline | Strong for validation, weak as alpha. | AI policies must beat simple rules with costs, turnover caps, and regime diagnostics. |
| [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]] | Crypto Granger-causality interaction networks | Contradiction / decay warning | Medium: graph/network ideas may help, but price-only sequence/network models remain fragile under fees, delistings, and nonstationarity. | Downgrade crypto network lead-lag to low priority unless a slow-horizon, fee-aware, delisting-controlled design is specified. |

## Adjacent-Domain Imports Worth Tracking

| Idea | Domain | Quant Use | Evidence / Caveat | Next Step |
|---|---|---|---|---|
| Cross-Audit Projection for Model Risk Prediction | Statistics / model validation | Warns that K-fold CV can misestimate class-specific risk; relevant to classifier-based event strategies and regime filters. | Not finance evidence; keep as validation-method lead only. | Add to open question: can cross-audit methods improve temporal validation of market classifiers beyond random/K-fold CV? |
| Value-of-Information analysis for external validation | Statistics / decision analysis | Could help decide whether expensive data acquisition, option-chain history, or alternative data is worth buying before coding. | Medical-risk-model context; not trading evidence. | Use as a framework for “is more validation data worth the cost?” decisions. |
| Online Safety Monitoring for LLMs | ML / online risk control | Threshold-calibrated monitors map to live strategy kill-switches or agent-output monitors. | LLM safety paper, not finance. The transfer is only a risk-control pattern. | Consider for future agent/backtest governance: online alarm when verifier risk exceeds calibrated threshold. |
| Extreme Adaptive Transformer for Time Series Forecasting | ML / extreme-event forecasting | Extreme-event attention may inspire tail-risk forecasting, but only after simple crisis filters. | Hydrology context; high metaphor risk and architecture novelty risk. | Watch only; require comparison with VIX/EWMA/drawdown/change-point filters before saving as source. |
| Granular Instrumental Variables in Large Panels | Econometrics / causal inference | Potentially useful for causal identification in panel event studies where dominant firms/sectors drive aggregates. | Method lead only; no current strategy translation. | Revisit if AI-exposure, liquidity premium, or policy-shock event studies need causal identification. |
| Sandpile models on complex networks | Physics / complex systems | Possible stress-test metaphor for liquidity cascades or contagion, but currently too metaphorical. | Reject as trading evidence; high analogy risk. | Do not save unless translated into measurable network stress variables and falsifiable market tests. |

## Registry Upgrades / Downgrades

- **SPX/SPXW short-dated put-writing** remains **High coding priority**, but only as “research spec needed.” It should not be treated as ready to code until option-chain bid/ask, cash/margin, settlement, crash-tail, and regime-split assumptions are explicit.
- **Forecast-uncertainty-aware ML asset pricing** now has a dedicated source note and should link to [[Forecast-uncertainty-aware ML asset pricing]] rather than only the 2026-06-28 daily review.
- **Crypto Granger-causality interaction networks** is downgraded to **Low** coding priority and explicitly **outdated-watch**. It should not compete with SPX put-writing, covariance/regret metrics, or reusable audit-block implementation.
- **Liquidity-demand audit / cost-aware diagnostics** are upgraded in implementation priority as a **coding-support artifact**, not as alpha.
- **Regime-routed volatility specialist forecasts** remain Medium but subordinate to simple volatility baselines; no direct promotion.

## Decay / Outdatedness Decisions

1. **Short-speed trend and naive reversal are on strong decay watch.** Recent evidence points to post-2009 market-structure change, tick-size/liquidity dependence, bid/ask bounce, stale pricing, and magnitude shrinkage as major confounders.
2. **Short-dated option selling remains plausible but crowded and structurally unstable.** The 0DTE era may have changed flow, spreads, crash dynamics, and intraday liquidity. Any SPX strategy must use conservative fills and regime splits before VIX/Kelly sophistication.
3. **Architecture-first ML is deprioritized.** Distributional outputs, uncertainty calibration, regime/fold diagnostics, and simple baselines are more important than LSTM/transformer novelty.
4. **Crypto graph/network lead-lag remains speculative.** Multiple testing, delistings, exchange fragmentation, fees, and latency are too large to ignore.
5. **Published equity anomalies require stronger guardrails.** Post-publication splits, survivorship-free data, cap-rank diagnostics, construction-error checks, and costs are mandatory before any anomaly enters the queue.

## Coding Queue Changes

**Added one coding-support item:** Standard cost/regime/liquidity/decision audit block for backtests.

This is not an alpha strategy, but it is coding-ready enough to implement as a reusable report module. It supports every higher-risk strategy family currently in the library: SPX put-writing, short-horizon trend/reversal, equity factors, crypto ML, stat arb, and AI portfolio policies.

No alpha candidate was promoted to “ready to code.” SPX put-writing remains the closest strategy candidate, but still needs a formal fixed-risk baseline spec and data confirmation.

## Open Research Questions Added / Retired

Added:

- Can cross-audit or value-of-information methods improve strategy validation decisions by estimating when more validation data, option-chain history, or alternative data are worth acquiring before coding?
- Can an online risk-monitor / kill-switch framework detect when a live strategy, model, or AI research agent leaves its validated regime using only time-gated verifier signals?

Retired: none.

## Notes Updated

Planned/actual updates from this run:

- Created this weekly review note.
- Updated [[Research Review Index]] with this periodic review link.
- Updated [[01 Research Candidate Registry]] for last-reviewed dates, crypto-network downgrade, and forecast-uncertainty source-note link.
- Updated [[Framework Candidate Registry]] with the new microstructure-conditioned decay framework.
- Updated [[Open Research Questions]] with validation-data value and online-monitor questions.
- Updated [[09 Coding-Ready Backtest Queue]] with the reusable backtest audit block.

## Discord Summary Candidate

Weekly synthesis created: `06 Research Reviews/2026-07-05 Weekly Quant Synthesis and Strategy Decay Review.md`. Main changes: added microstructure-conditioned decay framework; added standard backtest audit block to coding queue; downgraded crypto network/lead-lag to low/outdated-watch; preserved SPX put-writing as high priority but not ready without bid/ask/margin/regime spec.
