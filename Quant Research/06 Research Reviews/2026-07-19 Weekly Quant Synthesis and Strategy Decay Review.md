---
type: weekly-synthesis-decay-review
date: "2026-07-19"
run_time: "0901 EDT"
profile: quant-researcher
tags: [weekly-review, synthesis, decay-review]
---

# Weekly Quant Synthesis and Strategy Decay Review — 2026-07-19

## Executive Summary

This weekly pass reviewed the candidate registry, coding queue, framework registry, open questions, source index/source notes, and daily reviews from 2026-07-13 through 2026-07-19. The week produced many useful validation and decay warnings, but only one artifact is genuinely coding-ready: the reusable **standard cost/regime/liquidity/decision audit block**. Most new papers should be preserved as foundational or retail-adaptable validation modules rather than promoted as alpha.

Top synthesis decisions:

1. **Upgrade the audit block as the main coding target.** Recent notes on OHLCV falsification, base-rate-honest ML, crypto venue-quality complexity, PSI/JSD/KL drift power, feature-aware quantile audits, and action-attribution all converge on one immediate deliverable: a reusable audit/report module for any backtest.
2. **Keep quarter-hour crypto futures as high-interest but not coding-ready.** It is the most signal-like lead this week, but it remains vulnerable to publication decay, Binance-specific microstructure, fee/funding drag, overlapping-return inference, and venue-quality distortions.
3. **Split old accounting anomalies before coding.** PEAD is more promising than accruals under the Penman-Zhu/Alpha Architect lead, but both stay medium priority until the original paper rules, point-in-time data, accounting hedge factor, cap/liquidity diagnostics, and cost/borrow controls are specified.
4. **Commodity shocks improve regime validation, not alpha.** The Quantpedia commodity-crisis item is useful as a stress-test label family for portfolios and short-volatility, but it should not become a trading signal without frozen ex ante labels and baseline comparisons.

## Framework Candidates Added / Updated

| Framework | Linked Notes | Change | Next Validation Step |
|---|---|---|---|
| [[Framework Candidate Registry|Cost-aware decision-process diagnostics]] | [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]]; [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]; [[Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring]]; [[Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters]]; [[Robustness in Sequential Decision Making under Evolving Uncertainty]]; [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]] | Upgraded from broad governance lens to the highest-priority coding support artifact: the audit block should now include deployment gates, base-rate baselines, drift power/false-alarm analysis, feature-aware calibration, venue/data-quality flags, and action-attribution. | Implement the queue item as a report module that consumes trades/weights, fold metrics, costs, liquidity/regime proxies, and timestamps; produce go/no-go diagnostics before any strategy promotion. |
| [[Framework Candidate Registry|Microstructure-conditioned decay and liquidity-state validation]] | [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]]; [[When Does Order Flow Matter - State-Dependent L2 Liquidity-State Transitions in Crypto Futures]]; [[Herding and Liquidity in Order-Book Markets - A Robust Liquidity-Stress Crossover]]; [[The Extremity Premium - Sentiment Regimes and Adverse Selection in Cryptocurrency Markets]]; [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]] | Reinforced as the dominant crypto screening layer. Trade-count/order-flow effects must be conditioned on clock phase, exchange quality, pre-event liquidity state, sentiment/liquidity extremes, funding, and fees. | For any crypto intraday/order-flow backtest, start with BTC/ETH, explicit venue-quality flags, pre-event liquidity-state baseline, time-of-day/quarter-hour baseline, funding/carry baseline, and non-overlap inference. |
| [[Framework Candidate Registry|Regime-conditional distributional strategy evaluation]] | [[Commodity Crisis Analysis - How Portfolios React to Commodity Shocks]]; [[Dynamic Causal Portfolio Choice - Hedging the Rotation of the Common-Driver Manifold]]; [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] | Commodity-shock labels now act as practical regime slices for portfolio and options stress tests. | Add positive/negative commodity-shock state columns to backtest reports and compare conditional net distributions against VIX/EWMA/drawdown filters. |
| [[Framework Candidate Registry|Distributional-forecast-first ML strategy evaluation]] | [[VAIOM Continuous-Input Discrete-Output Financial Sequence Modeling]]; [[How Much of a 10-K Matters - Aggregation-Dependent Value of Full-Text versus Risk-Factor Sentiment]]; [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]] | Reinforced, but not promoted to coding. New sequence/text models report likelihood/forecast relevance, not net trading utility. | Convert any likelihood or text-sentiment gain into CRPS/calibration/coverage and downstream sizing utility against LightGBM/logistic, lagged volatility, and simple rules before allocating coding time. |
| [[Framework Candidate Registry|Validation-budget and value-of-information audit triage]] | Adjacent-domain leads: sequentially calibrated goodness-of-fit augmentation; scenario-based dynamic optimization inference; robust switched-system performance certificates | Preserved as watch. These methods may improve validation design, but are not trading evidence. | Pilot only inside an expensive data-cleaning or model-monitoring project: compare random/manual audit order versus prediction/statistical-priority audit order by error discovery and confidence tightening per audit hour. |

## Cross-Paper Connection Table

| Source A | Source B / Existing Candidate | Connection Type | Framework Potential | Action |
|---|---|---|---|---|
| [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]] | [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]] | Reinforces / contradiction to weak ML and intraday claims | Both show that headline performance metrics can be base-rate or cost artifacts unless deployment gates and trivial baselines are reported. | Add base-rate/always-up and deployment-gate diagnostics to the audit block. |
| [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]] | [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]] | Missing validation / decay warning | A clock-phase order-flow signal can be distorted by venue-level trade-count anomalies; venue quality must be audited first. | Do not promote quarter-hour crypto until average trade size, transaction-count/volume divergence, spread/depth stress, funding, and fee controls exist. |
| [[When Does Order Flow Matter - State-Dependent L2 Liquidity-State Transitions in Crypto Futures]] | [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]] | Method transfer | Use pre-event liquidity-state baselines to test whether clock-phase order flow adds incremental value. | Define staged feature admission: time-of-day baseline → funding/momentum → pre-event liquidity state → quarter-hour imbalance. |
| [[The Extremity Premium - Sentiment Regimes and Adverse Selection in Cryptocurrency Markets]] | [[Herding and Liquidity in Order-Book Markets - A Robust Liquidity-Stress Crossover]] | Mechanism bridge | Sentiment extremes and herding/order-flow stress both imply liquidity withdrawal rather than directional alpha. | Treat sentiment extremes as spread/slippage/sizing state; compare to volatility and drawdown filters. |
| [[Two Accounting Anomalies - Accruals May Be Risk, PEAD May Be Mispricing]] | [[A Cap-Axis Integral Diagnostic of Factor Models]]; [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]] | Missing validation / decay warning | Old anomaly research needs mechanism-relevant benchmarks plus cap/liquidity and post-publication audits. | Prioritize PEAD-first rule extraction; keep accrual alpha low priority unless it survives accounting hedge-factor and cost controls. |
| [[Commodity Crisis Analysis - How Portfolios React to Commodity Shocks]] | [[Regime-Conditional Distributional Comparison of Trading Strategies]]; [[Dynamic Causal Portfolio Choice - Hedging the Rotation of the Common-Driver Manifold]] | Method transfer / regime bridge | Commodity shocks give practical regime labels for driver-rotation and short-vol stress testing. | Add frozen commodity-shock labels, but reject hand-picked narrative windows as alpha evidence. |
| [[Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring]] | [[Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters]] | Missing validation | Drift alarms and calibration alarms should be treated as statistical tests with power/false-positive costs and action consequences. | Add false-alarm, missed-break, and missed-opportunity reporting before using any kill-switch. |
| [[SciPhy Reinforcement Learning for Portfolio Optimization]] | [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]]; [[Learning Predictive Ambiguity Sets for Decision-Focused DRO]] | Reinforces / complexity warning | AI/RL portfolio policies are not useful unless they beat simple rules with non-oracle signals, costs, turnover, and regime splits. | Keep foundational; do not implement PINN/RL before equal-weight, inverse-vol, myopic/linear policies, and cost-aware audit outputs exist. |

## Adjacent-Domain Imports Worth Tracking

| Idea | Domain | Quant Use | Evidence / Caveat | Next Step |
|---|---|---|---|---|
| Sequentially calibrated secondary goodness-of-fit statistics | Statistics | Could create staged deployment gates: primary net-PnL/cost gate, then secondary rejection decomposition by regime, liquidity, calibration, turnover, or drawdown. | Plausible method transfer only; not finance evidence. Risk of overcomplicated testing unless stages are pre-registered. | Add as an open question; revisit when implementing the audit block's deployment-gate table. |
| Statistical inference for scenario-based dynamic optimization under uncertainty | Control / operations research | Useful for evaluating scenario-based stress tests such as commodity-shock regimes: estimate uncertainty of scenario-optimized values instead of treating sampled stress windows as truth. | Adjacent-domain abstract; process-operation motivation, not markets. Metaphor risk is moderate. | Use only as a framework lead for commodity/regime stress-testing uncertainty, not strategy alpha. |
| Robust optimal control of arbitrarily switched systems with performance certificates | Robust control | Could inform kill-switch/risk-throttle certification: policy plus upper-bound performance certificate under regime switches. | Too theoretical for direct trading; institutional-level implementation. | Watch only; local adaptation must beat simple drawdown/volatility throttle baselines. |
| Data-driven block replacement scheduling | Operations research / bandits | Possible analogy for validation/data-refresh cadence: choose when to refresh models, clean data, or replace features under censored failure information. | Weak market connection; keep as metaphor-risk example unless tied to measurable model-failure costs. | Do not save as source note; mention only as a validation-budget watch idea. |

## Registry Upgrades / Downgrades

- **Upgraded coding emphasis:** Standard cost/regime/liquidity/decision audit block is now the most useful near-term implementation target, above new signal hunting. The candidate registry sorting view and coding queue were updated to reflect this.
- **Preserved as foundational:** base-rate-honest ML benchmark, OHLCV deployment gates, crypto exchange-quality diagnostics, drift-monitoring power analysis, feature-aware quantile audits, action-attribution robustness, and SciPhyRL cost-aware policy design.
- **Kept as retail-adaptable but unready:** quarter-hour crypto futures order-imbalance effect remains Medium/High research priority but needs data/cost/inference design before queue promotion.
- **Downgraded/deferred in practice:** continuous-input ordinal sequence modeling and aggregation-aware 10-K sentiment should not be coded before simpler baselines and downstream utility tests exist.
- **Accounting anomalies reclassified:** PEAD gets medium research interest; accrual alpha is downgraded to benchmark/risk-compensation audit unless it survives accounting hedge-factor and cost controls.

## Decay / Outdatedness Decisions

- **0DTE / short-dated option selling:** remains high priority but high decay/crowding risk. Do not add VIX/Kelly/option-implied SDF sophistication until fixed-risk baseline, bid/worse fills, margin/cash, crash periods, 0DTE-era splits, and audit-block outputs exist.
- **Crypto microstructure alpha:** highest decay risk this week. Clock-phase and order-flow findings must survive fees/funding, exchange-quality flags, liquidity-state controls, overlapping-return inference, and post-publication adaptation.
- **Directional ML/foundation models:** raw hit rate, likelihood gains, or architecture novelty are insufficient; require base-rate and downstream net-utility superiority.
- **Old accounting anomalies:** high post-publication and crowding risk; only PEAD-like delayed-information hypotheses remain interesting after point-in-time and cost controls.
- **Commodity regime narratives:** useful as stress tests, risky as trading narratives unless labels are frozen ex ante and tested against simple VIX/EWMA/drawdown baselines.

## Coding Queue Changes

- Updated `last_updated` to 2026-07-19.
- Updated the **Standard cost/regime/liquidity/decision audit block for backtests** queue row from Medium/High to High priority and linked this weekly review.
- Kept SPX/SPXW short-dated put-writing in the queue, but still data-blocked and explicitly subordinate to the fixed-risk baseline/audit-block design.
- Did **not** promote quarter-hour crypto, accounting anomalies, commodity shocks, VAIOM, 10-K sentiment, or SciPhyRL; each lacks the full data/cost/baseline/go-no-go specification required by the queue promotion rule.

## Open Research Questions Added / Retired

Added one question:

- Can sequentially calibrated secondary goodness-of-fit/deployment-gate tests improve intraday, crypto, option, and ML strategy validation by decomposing first rejection into cost, base-rate, regime, calibration, liquidity, or turnover failure modes without inflating Type I error or creating bureaucratic overfit?

No questions retired. Several existing questions were reinforced: quarter-hour crypto viability, exchange-quality anomaly flags, power-calibrated drift alarms, accounting anomaly reclassification, commodity-shock conditional validation, and action-attribution for risk throttles.

## Notes Updated

- [[01 Research Candidate Registry]] — sorting view updated to raise the audit block's coding emphasis and keep new signal leads conservative.
- [[09 Coding-Ready Backtest Queue]] — updated weekly link/priority for the audit block and `last_updated`.
- [[07 Literature Synthesis/Framework Candidate Registry]] — updated validation-budget/value-of-information framework with drift-power, staged deployment-gate, and scenario-optimization uncertainty method leads.
- [[07 Literature Synthesis/Open Research Questions]] — added staged deployment-gate question.
- [[06 Research Reviews/Research Review Index]] — added this weekly review link.

## Discord Summary Candidate

Weekly synthesis complete. Main outcome: prioritize the standard audit/report module before new signal coding; keep quarter-hour crypto high-interest but not queue-ready; treat commodity shocks and accounting anomalies as validation/reclassification work rather than immediate alpha.
