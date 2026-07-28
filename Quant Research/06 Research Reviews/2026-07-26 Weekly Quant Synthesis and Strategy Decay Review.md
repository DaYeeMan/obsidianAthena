---
type: weekly-synthesis-decay-review
date: "2026-07-26"
run_time: "1410 EDT"
profile: quant-researcher
tags: [weekly-review, synthesis, decay-review]
---

# 2026-07-26 Weekly Quant Synthesis and Strategy Decay Review

## Executive Summary

This weekly pass reviewed the research candidate registry, coding queue, framework registry, open questions, recent daily reviews from 2026-07-20 through 2026-07-24, recent source notes, and selected adjacent-domain arXiv leads validated through the arXiv API. The week strengthened the library’s validation stack more than it produced new alpha. The main coding decision remains: **build the reusable standard cost/regime/liquidity/decision audit block before promoting any fragile options, crypto, DeFi, prediction-market, or ML strategy.**

Top decisions:

1. **Coding queue remains focused, not expanded.** No new strategy was promoted to immediate implementation. The audit block remains the best ready-to-code artifact; its scope should now include excluded-pool coverage audits and event-study pre-trend inference, not just trade-level cost/regime panels.
2. **Microstructure/venue execution costs dominate this week’s decay review.** DEX routing, crypto ADL, anchor failure, prediction-market AMM/settlement risk, and quarter-hour crypto order-flow all point to the same rule: do not trust quoted prices, mids, gross spread capture, or order-flow signals until venue-state and execution-state diagnostics are attached.
3. **Negative and falsification papers are high-value governance evidence.** Retail-signal failure, Binance candle-ML no-trade results, and quantum-kernel vanishing advantage should remain foundational/reference controls; they prevent wasted coding on popular rules, price-only ML, and exotic model novelty.

## Inputs Reviewed

- [[01 Research Candidate Registry]] through the 2026-07-24 entries.
- [[09 Coding-Ready Backtest Queue]].
- [[Framework Candidate Registry]] and [[Open Research Questions]].
- Daily reviews: [[2026-07-20 0801 Daily Quant Research Review]], [[2026-07-21 0802 Daily Quant Research Review]], [[2026-07-22 0801 Daily Quant Research Review]], [[2026-07-23 0803 Daily Quant Research Review]], [[2026-07-24 0803 Daily Quant Research Review]].
- Recent source notes including [[Risk-Based Auto-Deleveraging]], [[ARp-Focus Online Changepoint Detection under Autocorrelation]], [[FinBench - Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting]], [[Herding and Liquidity in Order-Book Markets II - Fundamental Anchoring and Liquidity Resilience]], [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]], [[Observable Matrix Dynamics of Stocks]], [[Mixing-Law Uncertainty for Robust Heavy-Tail Portfolio Decisions]], [[Illiquid-Asset Option Pricing via Liquid Benchmark Volatility Surfaces]], [[The Science and Practice of Trend-Following Systems]], [[Retail Traders Ruin - Anatomy of Popular Signal Failure]], [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]], [[Quantum Kernels and the Cross-Section of Stock Returns - Vanishing Advantage]], [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]], and [[Pathwise Roughness of Bitcoin Realized Volatility]].
- Adjacent-domain arXiv leads validated this run: arXiv:2607.21480v1, 2607.21312v1, 2607.21520v1, 2607.21542v1, 2607.21573v1, and 2607.21475v1.

## Framework Candidates Updated

| Framework | Change | Evidence / Link | Next Validation Step |
|---|---|---|---|
| [[Framework Candidate Registry|Validation-budget and value-of-information audit triage]] | Strengthened with excluded-pool coverage audits and event-study pre-trend inference. | arXiv:2607.21480v1 shows that auditing only accepted candidates cannot certify missed relevant mass; arXiv:2607.21312v1 uses pre-treatment paths as a reference distribution for DID inference without relying on parallel trends. | Add an audit-triage panel to the standard backtest/research report: sample rejected/excluded candidates, quote-filter rejects, vendor-row drops, strategy-screen losers, and pre-event placebo paths before declaring a research screen or event study clean. |
| [[Framework Candidate Registry|Cost-aware decision-process diagnostics]] | Reaffirmed as the top coding-support framework. | Recent notes on FinBench calibration, retail-signal falsification, Binance candle-ML no-trade gates, quantum-kernel model controls, DEX routing shortfall, and ADL/venue stress all target false decision quality rather than raw prediction. | Implement the audit block as a reusable report module before coding new alpha; include leakage, baseline, cost, calibration, venue-state, coverage-audit, and action-attribution outputs. |
| [[Framework Candidate Registry|Microstructure-conditioned decay and liquidity-state validation]] | Expanded conceptually from spread/depth/liquidity states to **mechanism-specific execution states**: ADL queues, anchor failure, settlement risk, AMM loss, stale block state, MEV/sandwich exposure, and route support. | [[Risk-Based Auto-Deleveraging]], [[Herding and Liquidity in Order-Book Markets II - Fundamental Anchoring and Liquidity Resilience]], [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]], and [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]]. | For crypto/DeFi/prediction-market backtests, require venue/execution state fields before treating fills or marks as reliable: funding, liquidation/ADL stress, stale-state delay, gas, failed transactions, route shortfall, settlement proximity, fee/subsidy design, and anchor-quality proxies. |
| [[Framework Candidate Registry|Regime-conditional distributional strategy evaluation]] | Reinforced but not expanded into a new framework. | [[Observable Matrix Dynamics of Stocks]], [[Commodity Crisis Analysis - How Portfolios React to Commodity Shocks]], [[Pathwise Roughness of Bitcoin Realized Volatility]], and [[ARp-Focus Online Changepoint Detection under Autocorrelation]] all add possible ex ante regime labels. | Use OMD/correlation geometry, commodity shocks, BTC volatility roughness, and AR-aware alarms only as conditional validation labels until they beat VIX/EWMA/drawdown/funding/simple volatility filters after turnover and missed-rebound costs. |

## Cross-Paper Connection Table

| Connection | Type | Synthesis Decision | Falsification / Minimum Test |
|---|---|---|---|
| [[The Science and Practice of Trend-Following Systems]] + [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]] + [[Retail Traders Ruin - Anatomy of Popular Signal Failure]] | Reinforces / decay warning | Trend is not one bucket. Slower diversified trend may survive as a cost-aware persistence/skew strategy, while short-speed or retail-parameter trend rules remain decay-watch unless they pass cost-optimal span, tick-size/liquidity, multiplicity, and net materiality gates. | Walk-forward trend spans across liquid ETFs/futures/crypto; report turnover, spread/roll/funding costs, volatility-normalized spectral persistence, post-2009 splits, and exposure-matched benchmarks. |
| [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]] + [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]] + [[Quantum Kernels and the Cross-Section of Stock Returns - Vanishing Advantage]] | Contradiction to model-novelty alpha | Forecast metrics, AUC, likelihood, or model novelty are not alpha unless converted to net policy utility versus no-trade, buy/hold, simple momentum/funding/carry, linear/logistic/LightGBM, and equal-budget controls. | Any ML strategy must report calibration, average precision or utility-relevant metrics, purged splits, costed trades, held-out assets/regimes, and equal-budget simple baselines. |
| [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]] + [[Risk-Based Auto-Deleveraging]] + [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]] | Missing validation / method bridge | Crypto order-flow or DeFi edge must be conditioned on exchange and execution-state variables, not just signal value. A slow quarter-hour effect can still fail if venue quality, funding, liquidation/ADL, stale-state routing, and fees explain the realized PnL. | Quarter-hour event study should include fee/funding, non-overlap inference, venue-quality flags, liquidation/ADL stress, pre-event spread/depth, and time-of-day baselines; DeFi backtests should include gas-aware route shortfall and MEV flags. |
| [[Illiquid-Asset Option Pricing via Liquid Benchmark Volatility Surfaces]] + [[Arbitrage-Free Multi-Maturity Risk-Neutral Marginals]] + [[Option-Implied SDF Equity Premium Timing]] + [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] | Missing validation | Option-derived signals are only as good as the quote panel. Proxy surfaces and arbitrage smoothing are useful diagnostics, not executable mids. | Before SDF/skew/tail or put-writing tests, build a quote-quality report: bid/ask, stale quote, maturity alignment, direct-vs-proxy IV disagreement, arbitrage checks, and worse-side fill stress. |
| arXiv:2607.21480v1 + existing audit-block notes | Adjacent-domain method transfer | Research screens that only audit surviving candidates are unverifiable. The excluded pool matters: discarded tickers, quotes, papers, signals, or feed leads can hide missed relevant mass. | In the audit block, sample excluded candidates and quantify missed-signal or missed-error mass; no non-trivial coverage claim from included-only labels. |
| arXiv:2607.21312v1 + event-study candidates such as PEAD, settlement windows, commodity shocks, and protocol-fee changes | Causal-validation bridge | Many event studies have long pre-periods; use pre-treatment paths as an empirical reference distribution before trusting post-event DID/event-window effects. | Add pre-event placebo/path reference tests to PEAD, prediction-market settlement, AMM fee-change, and commodity-shock studies; reject effects that are not unusual relative to pre-event shocks. |

## Adjacent-Domain Imports Worth Tracking

| Lead | Validated Metadata | Accepted Use | Rejected / Caution |
|---|---|---|---|
| Finite-Sample Coverage Audits for High-Recall Candidate Generation | Martin Anthony, Kaveh Salehzadeh Nobari, arXiv:2607.21480v1, 2026-07-23. | Add to validation-budget framework: audit excluded/rejected pools in research screens, data filters, source triage, and candidate generation. | Not trading evidence; do not create a strategy note. |
| Using Pre-Trends for Inference in Difference-in-Differences | Clément de Chaisemartin, arXiv:2607.21312v1, 2026-07-23. | Add to event-study/causal validation: use pre-treatment paths as reference distributions for policy/protocol/event claims. | Does not prove event-study alpha; helps avoid overconfident causal claims. |
| Asymptotic Analysis of Empirical Dynamic Programming in Infinite-Horizon Stochastic Optimal Control | Chen, Isik, Milz, arXiv:2607.21520v1. | Watch as methodology for uncertainty in empirical dynamic programming and RL/allocation policies. | Too theoretical for current coding queue; do not use as a reason to build RL allocation now. |
| Zero-Flow Two-Sample Tests | Wang, Wang, Liu, Suzuki, arXiv:2607.21542v1. | Watch for structured distribution-shift testing if existing PSI/JSD/KL and changepoint tests fail. | Neural witness tests add complexity; require calibration/power tests and simple-drift baselines first. |
| Beyond Sufficiency: Time Series Explanation with Counterfactual Necessity | Ma et al., arXiv:2607.21573v1. | Possible future diagnostic for whether ML time-series signals rely on necessary temporal features or spurious sufficient subsequences. | High metaphor/complexity risk; no trading evidence and not needed before simple feature ablations/action attribution. |
| Error Certificates for KV-Cache Eviction via Randomized Design | Peng Xie, arXiv:2607.21475v1. | Conceptual reminder: deterministic pruning may make error unknowable; randomized audit designs can identify what was lost. | LLM systems paper, not finance-specific; only relevant by analogy to research-screen sampling design, already better captured by the finite-sample coverage audit paper. |

## Candidate Upgrade / Downgrade / Preservation Decisions

### Upgrade / strengthen

- **Standard cost/regime/liquidity/decision audit block** remains **High / ready to code**. The weekly synthesis adds two concrete requirements: excluded-pool coverage audits and event-study pre-trend reference tests.
- **Validation-budget and value-of-information audit triage** becomes more operational: sample what the pipeline rejected, not only what survived.
- **Microstructure-conditioned decay and liquidity-state validation** should now explicitly include DeFi route quality, AMM/settlement economics, ADL/liquidation/venue stress, and anchor-quality states.

### Preserve as foundational / reference

- [[Retail Traders Ruin - Anatomy of Popular Signal Failure]], [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]], and [[Quantum Kernels and the Cross-Section of Stock Returns - Vanishing Advantage]] should stay in the registry as reference controls. They are useful because they prevent low-quality or overfit strategy coding.
- [[Observable Matrix Dynamics of Stocks]], [[Mixing-Law Uncertainty for Robust Heavy-Tail Portfolio Decisions]], [[Illiquid-Asset Option Pricing via Liquid Benchmark Volatility Surfaces]], and [[Pathwise Roughness of Bitcoin Realized Volatility]] should remain foundational/retail-adaptable methodology, not standalone alpha.

### Keep but do not promote

- **Quarter-hour crypto futures order-imbalance effect** remains Medium/High research priority but not coding-ready without reliable intraday/trade data, funding/fees, non-overlap inference, and venue-state controls.
- **SPX/SPXW short-dated put-writing** remains high priority but data-blocked. New option-chain quality notes make it less acceptable to start from midpoint-only or poorly timestamped chains.
- **Option-implied SDF equity-premium timing** remains plausible/foundational, but only after quote cleaning and simple VIX/skew/realized-vol baselines exist.

### Downgrade / decay watch emphasis

- Generic price-only crypto ML, popular retail signals, exotic quantum/representation models, raw OMD/correlation-regime timing, rough-volatility features, and option proxy-IV strategies should be treated as **outdated-watch or reference-only** unless they beat simple baselines net of costs and implementation constraints.

## Coding Queue Review

Coding queue updated but not expanded. The queue remains:

1. SPX/SPXW short-dated put-writing with VIX/fractional-Kelly sizing — **High but data blocked**; first step is still fixed-risk baseline spec and quote-quality preprocessing.
2. Decision-aware covariance metrics — **Medium method integration**.
3. Forecast-uncertainty-aware ML sizing — **Medium method integration** after a baseline forecast pipeline exists.
4. Standard cost/regime/liquidity/decision audit block — **High / ready to code**, now explicitly expanded to include excluded-pool coverage audits and pre-trend/event-study reference tests.

No new strategy was promoted because none of this week’s items supplied complete falsifiable rules, data, costs, baselines, and go/no-go criteria beyond validation/reporting enhancements.

## Open Questions Added

- Can excluded-pool coverage audits detect missed alpha, missed data-quality failures, or survivorship introduced by research-candidate screens, option-chain filters, feed triage, and model-feature selection better than included-only validation?
- Can pre-treatment path reference distributions improve event-study inference for PEAD, prediction-market settlement windows, AMM protocol-fee changes, commodity shocks, and crypto venue events versus standard parallel-trend or placebo tests?

## Decay Watch List for Next Week

- **0DTE/short-vol:** watch for any strategy that ignores 0DTE-era market-structure, bid/ask/worse fills, margin, and crash liquidity.
- **Crypto intraday/order-flow:** keep quarter-hour and L2 signals behind venue-quality, fee/funding, non-overlap, and ADL/liquidation gates.
- **DeFi/AMM:** treat pool quotes and execution-time reserves as non-executable unless gas, route, stale-state, failure, and MEV/sandwich costs are modeled.
- **ML/AI/LLM:** require time-gating, calibration, simple baselines, artifact retention, and policy-value conversion; model novelty is not evidence.
- **Event studies:** apply pre-trend/reference-path checks and sample excluded cases to avoid survivorship and post-hoc event-window stories.

## Obsidian Updates Made

- Created this weekly review note.
- Updated [[Research Review Index]] with this periodic review.
- Updated [[Framework Candidate Registry]] recent updates for validation-budget, audit-block, and microstructure/execution-state synthesis.
- Added two adjacent-method candidate rows to [[01 Research Candidate Registry]] and refreshed sorting/decay/foundational sections.
- Updated [[Open Research Questions]] with two validation questions.
- Updated [[09 Coding-Ready Backtest Queue]] to link this weekly review and add excluded-pool/pre-trend requirements to the audit block.
