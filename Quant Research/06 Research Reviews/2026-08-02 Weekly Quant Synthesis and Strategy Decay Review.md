---
type: weekly-synthesis-decay-review
date: "2026-08-02"
run_time: "1940 EDT"
profile: quant-researcher
tags: [weekly-review, synthesis, decay-review]
---

# 2026-08-02 Weekly Quant Synthesis and Strategy Decay Review

## Executive Summary

This weekly pass reviewed the candidate registry, coding queue, framework registry, open research questions, recent daily reviews from 2026-07-27 through 2026-08-01, recent source notes, and selected adjacent-domain arXiv leads surfaced by the pre-run context. The week again produced more **validation infrastructure** than directly tradable alpha. The strongest conclusion is unchanged but sharper: **build the standard cost/regime/liquidity/decision audit block before adding new fragile strategies.**

Top decisions:

1. **Coding queue remains concentrated.** No new alpha strategy met the promotion rule. The standard audit block stays High / ready-to-code and was updated as the near-term implementation target; SPX short-dated put writing stays High but data-blocked and should start with a fixed-risk baseline, not Kelly/SDF/model overlays.
2. **Option research needs a three-gate validation chain before sizing overlays.** RIDGE-style invariant tests, robust HVA/funding/margin reserve accounting, and inverse-density identifiability checks now form a common option audit path before SPX/SPXW short-vol, option-implied SDF, or risk-neutral-tail features are trusted.
3. **Crypto/prediction-market/DeFi papers mostly strengthened no-trade and execution realism gates.** OpenMarket, Polymarket attribution limits, event-linked perps, liquidation cascades, passive fill impact, DEX routing, and dynamic AMM fees all argue against naïve midquote/book-probability/order-flow alpha without venue-specific fill, fee, state, and identification audits.

## Inputs Reviewed

- [[01 Research Candidate Registry]] through the 2026-08-01 entries.
- [[09 Coding-Ready Backtest Queue]].
- [[Framework Candidate Registry]] and [[Open Research Questions]].
- Daily reviews: [[2026-07-27 0803 Daily Quant Research Review]], [[2026-07-28 1219 Daily Quant Research Review]], [[2026-07-29 0801 Daily Quant Research Review]], [[2026-07-30 1436 Daily Quant Research Review]], [[2026-07-31 1943 Daily Quant Research Review]], and [[2026-08-01 1344 Daily Quant Research Review]].
- Recent source notes including [[Characteristic-Driven Covariance from Fundamentals]], [[Parameter-Efficient Neural GMVP for Volatility Drag Mitigation]], [[Physics-Informed Cross-Covariance Forecasting]], [[Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes]], [[OpenMarket Synchronized Polymarket-Binance Dataset]], [[Crypto Perpetual Liquidation Cascades - Event-Heterogeneous Early Warnings]], [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]], [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]], [[Optimal Execution with Passive Market Impact]], [[Can Large Language Models Execute Parent Orders]], [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]], [[Boundary-Induced Apparent Risk Aversion in Multiplicative Growth]], and [[Optimal Dynamic Fees in Automated Market Makers]].
- Adjacent-domain method leads from the pre-run arXiv context: arXiv:2607.28567v1 on doubly robust functional representation learning for irregular histories, arXiv:2607.28294v1 on bootstrap inference for autoregressive duration models, arXiv:2607.28385v1 on Riemannian factor models for manifold-valued time series, and selected rejected/watch-only optimization/complex-systems leads.

## Framework Candidates Added / Updated

| Framework | Linked Notes | Change | Next Validation Step |
|---|---|---|---|
| [[Framework Candidate Registry|Cost-aware decision-process diagnostics]] | [[Optimal Execution with Passive Market Impact]]; [[Can Large Language Models Execute Parent Orders]]; [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]]; [[Boundary-Induced Apparent Risk Aversion in Multiplicative Growth]]; [[RIDGE Autonomous Validation for LLM-Generated Option Pricing]]; [[Robust HVA for Deep Hedging under Market Frictions]] | Upgraded as the single most useful coding-support framework. It now spans passive-fill realism, AI execution-agent baselines, forward-gated model replacement, boundary-aware sizing, option-code invariants, and reserve-aware hedging diagnostics. | Implement one reusable audit report module before new alpha: time-gated/leakage checks, costs/fills, baseline comparisons, action attribution, margin/boundary survival, uncertainty/calibration, venue state, and deployment-gate outputs. |
| [[Framework Candidate Registry|Option-chain data-quality and proxy-surface validation]] | [[Arbitrage-Free Multi-Maturity Risk-Neutral Marginals]]; [[Illiquid-Asset Option Pricing via Liquid Benchmark Volatility Surfaces]]; [[Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes]]; [[RIDGE Autonomous Validation for LLM-Generated Option Pricing]]; [[Robust HVA for Deep Hedging under Market Frictions]] | Expanded from surface cleaning into an option research validation stack: no-arbitrage/pricing-code invariants, sparse-quote density identifiability, proxy-IV disagreement, bid/ask/stale quote filters, and margin/funding/tail reserve. | For SPX/SPXW work, create the fixed-risk put-write spec first; add quote-quality and worse-side fills before testing VIX/Kelly/SDF/risk-neutral-tail overlays. |
| [[Framework Candidate Registry|Microstructure-conditioned decay and liquidity-state validation]] | [[OpenMarket Synchronized Polymarket-Binance Dataset]]; [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]]; [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]]; [[Crypto Perpetual Liquidation Cascades - Event-Heterogeneous Early Warnings]]; [[Optimal Dynamic Fees in Automated Market Makers]]; [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]] | Strengthened as a cross-venue no-overclaim framework. Public prediction-market records, DeFi/AMM quotes, and crypto-perp venue states require explicit metadata and fill/cost conventions before order-flow, spread-capture, or risk-filter claims are evidence. | When prediction-market or DeFi data are available, reproduce negative/no-trade baselines first: Polymarket book probability, near-resolution avoidance, fixed-fee versus dynamic-fee stress, gas/MEV/stale-state routing shortfall, and liquidation/ADL false-exit costs. |
| Decision-aware covariance/risk-model benchmark suite | [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]]; [[Characteristic-Driven Covariance from Fundamentals]]; [[Parameter-Efficient Neural GMVP for Volatility Drag Mitigation]]; [[Physics-Informed Cross-Covariance Forecasting]]; [[Observable Matrix Dynamics of Stocks]] | Consolidated this week’s covariance notes as estimator candidates, not separate strategies. Characteristic-driven risk, compact neural eigencleaning, and learned singular-value cleaning should compete in one decision-aware benchmark. | Define an estimator zoo and score realized variance, regret, turnover, concentration, drawdown, and costs versus equal weight, inverse-vol/risk parity, sample, Ledoit-Wolf/nonlinear shrinkage, EWMA, and factor covariance. |

## Cross-Paper Connection Table

| Connection | Type | Synthesis Decision | Falsification / Minimum Test |
|---|---|---|---|
| [[Boundary-Induced Apparent Risk Aversion in Multiplicative Growth]] + [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] + [[Robust HVA for Deep Hedging under Market Frictions]] | Missing validation / decay warning | Kelly and VIX sizing for short-vol should be treated as a boundary/margin survival problem, not an optimal-growth plug-in. | Fixed-risk SPX/SPXW baseline with bid/worse fills, then add boundary-aware sizing only if it improves drawdown-CVaR/survival-adjusted utility after turnover and missed-rebound costs. |
| [[Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes]] + [[Option-Implied SDF Equity Premium Timing]] + [[Arbitrage-Free Multi-Maturity Risk-Neutral Marginals]] | Contradicts / missing validation | Option-price fit and smooth arbitrage-free surfaces do not prove tail/skew/SDF feature validity; sparse quotes can leave density directions nearly unidentified. | Compare SDF/tail features against VIX, IV-rank, simple skew, realized vol, and drawdown filters; perturb densities inside price-near-null directions and require stable downstream decisions. |
| [[OpenMarket Synchronized Polymarket-Binance Dataset]] + [[Settlement Manipulation in Prediction Markets]] + [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]] | Reinforces / no-trade gate | Public paired data are valuable, but the book-implied probability is a hard baseline and public fills do not identify side/informed-flow behavior without attribution sensitivity. | Reproduce OpenMarket’s negative logistic benchmark; then test settlement windows with side-convention, maker/taker, mint/burn, subsystem, and block-window sensitivity panels. |
| [[Optimal Execution with Passive Market Impact]] + [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]] | Mechanism bridge | Some short-horizon “alpha” is likely execution artifact: apparent directional predictability can collapse once passive fill probability, adverse selection, and non-fill opportunity cost are charged. | Any ETF/crypto reversal/stat-arb test should include sign-vs-magnitude decomposition plus marketable-fill, passive-fill, and no-fill opportunity-cost scenarios. |
| [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]] + [[FinBench - Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting]] + [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]] | Reinforces / deployment gate | Frequent retraining is not a reason to deploy. A challenger must beat a maintained incumbent on the same forward delayed-label window and then improve net utility. | Shadow-before-swap promotion only after paired NLL/calibration advantage and downstream turnover, fee, funding, drawdown, and no-trade baseline checks. |
| [[Optimal Dynamic Fees in Automated Market Makers]] + [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]] + [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]] | Missing validation / market-design bridge | Fixed-fee AMM simulations are fragile. LP protocol-fee event studies do not identify trader-facing dynamic fee cost. | Add fixed-fee vs inventory/external-price dynamic-fee scenarios to AMM/DEX simulations with gas, stale-state, MEV/sandwich, failed transaction, and route-support shortfall fields. |

## Adjacent-Domain Imports Worth Tracking

| Idea | Domain | Quant Use | Evidence / Caveat | Next Step |
|---|---|---|---|---|
| Doubly robust functional representation learning for irregular histories, arXiv:2607.28567v1 | Longitudinal causal inference / representation learning | Potential design pattern for irregular alternative-data histories, option quote panels, and event-study exposure histories where prediction loss alone may not stabilize the estimand. | Adjacent-method lead only; not trading evidence. Needs translation into time-gated finance panels and must beat simpler summaries. | Watch for use in validation-budget/event-study framework: compare functional states versus simple lagged summaries under cross-fitting and decision-time availability. |
| Bootstrap inference in autoregressive duration models, arXiv:2607.28294v1 | Econometrics / event-history duration models | Useful for transaction-duration, quote-update, trade-arrival, or settlement-window intensity inference when event count is random over fixed calendar spans. | Adjacent-method lead only; ACD inference is not alpha and needs event-time data. | Add as a watch question for microstructure/event-study duration inference once trade/quote data are available. |
| Riemannian factor model for manifold-valued time series, arXiv:2607.28385v1 | Statistics / geometry-aware time series | Possible method lead for covariance/correlation-matrix or OMD-style geometry states; useful only if it improves calibrated risk-state monitoring. | High metaphor/complexity risk; do not implement before absorption ratio, leading eigenvalue, shrinkage, and OMD baselines. | Keep as watch-only within covariance/risk-state framework; require downstream drawdown/control utility. |
| TEAM-IV robust instrument aggregation, arXiv:2607.28289v1 | Causal inference / instrumental variables | Possible validation tool for alternative-data or event-exposure studies when most instruments/proxies are invalid. | Adjacent-method lead only; many quant problems lack credible instruments. | Track only as causal-validation reference; no source note until a concrete finance exposure study needs it. |

Rejected adjacent-domain imports this week: Kemeny aggregation complexity, decision diagrams for binary polynomial optimization, Egyptian fraction optimal control, generic complex-systems mobility/network leads, and power-grid frequency inference were not saved because the connection to current equities/options/crypto strategy validation was either too indirect or metaphorical.

## Registry Upgrades / Downgrades

- **No new candidate rows added.** Daily runs already added the week’s useful candidates; this pass consolidated them rather than duplicating rows.
- **SPX/SPXW short-dated put-writing** remains High priority but not more coding-ready: boundary-aware Kelly, HVA, RIDGE, and density-identifiability notes all make the required fixed-risk baseline stricter before overlays.
- **Decision-aware covariance metrics** remain Medium priority but now have a clearer estimator suite: characteristic-driven covariance, compact neural GMVP, physics-informed singular-value cleaning, and OMD/correlation geometry should be tested together, not as standalone strategy ideas.
- **Forward-gated crypto ML model replacement, passive-fill execution realism, dynamic AMM fee stress, and Polymarket attribution limits** are preserved as foundational/audit candidates rather than promoted to alpha.

## Decay / Outdatedness Decisions

- **Crowded 0DTE/short-vol decay risk remains high.** The post-2022 0DTE regime, bid/ask stress, margin/cash treatment, crash gaps, and volatility underprediction dominate any VIX/Kelly/SDF sizing optimism.
- **Prediction-market settlement/order-flow alpha is downgraded unless it beats book probability and no-trade baselines.** OpenMarket’s negative trading result makes Polymarket book probability the first benchmark, not a weak baseline.
- **Crypto price-only and high-frequency order-flow ML remain decay-watch.** Model replacement gates help governance but do not validate a strategy; costs, funding, venue changes, and false promotions can erase forecast-loss gains.
- **AMM/DEX alpha claims using static quoted reserves or fixed fees are decay-watch.** Dynamic fees, gas, stale state, MEV/sandwich exposure, failed transactions, and route support are first-order costs.
- **Covariance/portfolio ML remains foundational until downstream utility beats simple baselines.** The library now has enough candidate estimators; next value comes from a common decision-aware benchmark, not more estimator accumulation.

## Coding Queue Changes

- [[09 Coding-Ready Backtest Queue]] updated only for hygiene/context:
  - `last_updated` moved to 2026-08-02.
  - The standard audit block row now links this weekly review and remains High / Ready to code.
  - The SPX/SPXW row now links this weekly review and explicitly starts with a fixed-risk baseline before VIX/Kelly/SDF/risk-neutral-tail overlays.
- No new strategy was promoted; no item was removed.

## Open Research Questions Added / Retired

Added two watch questions:

- Can doubly robust functional representation learning for irregular histories improve point-in-time event-study exposure states, option quote-history summaries, or alternative-data panels versus simple lagged summaries after cross-fitting and downstream decision-utility checks?
- Can autoregressive-duration bootstrap inference improve microstructure/event-study inference for trade-arrival, quote-update, liquidation, or settlement-window intensity effects versus simpler clustered/block bootstrap tests?

No questions retired. Several existing questions were sharpened through framework updates rather than closed.

## Notes Updated

- Created this weekly review note.
- Updated [[Research Review Index]].
- Updated [[09 Coding-Ready Backtest Queue]].
- Updated [[01 Research Candidate Registry]] metadata and sorting/context rows.
- Updated [[Framework Candidate Registry]] recent framework updates.
- Updated [[Open Research Questions]].

## Discord Summary Candidate

Weekly synthesis saved: [[2026-08-02 Weekly Quant Synthesis and Strategy Decay Review]]. Coding queue stays focused: standard audit block remains the top ready-to-code artifact; SPX put-writing remains high-priority but data/realism blocked; no new alpha promoted.
