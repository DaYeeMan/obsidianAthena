---
type: weekly-synthesis-decay-review
date: "2026-08-09"
run_time: "1351 EDT"
profile: quant-researcher
source_status: weekly-synthesis-from-library-and-prerun-context
asset_focus: [equities, options, crypto, portfolio, prediction-markets, DeFi]
tags: [weekly-review, synthesis, decay-review]
---

# 2026-08-09 Weekly Quant Synthesis and Strategy Decay Review

## Executive Summary

This weekly pass reviewed the candidate registry, coding queue, framework registry, open questions, recent daily reviews from 2026-08-03 through 2026-08-08, recent source notes, strategy notes, and the adjacent-domain arXiv leads supplied by the pre-run context. The week produced almost no directly tradable alpha that satisfies the coding-queue promotion rule. It did produce a stronger synthesis conclusion: **the standard cost/regime/liquidity/decision audit block is now the highest-value coding artifact and should be implemented before new signal work, including the SPX/SPXW short-volatility baseline.**

Top decisions:

1. **Coding queue remains conservative; no new signal promoted.** SPX/SPXW short-dated put writing remains High but data-blocked. The standard audit block remains High / ready-to-code and is now the immediate implementation priority because it is prerequisite infrastructure for SPX, crypto-perp, option-surface, anomaly, ML, and microstructure work.
2. **Recent papers form three reinforcing validation stacks rather than standalone strategies:** (a) uncertainty-aware sizing and forecast calibration; (b) microstructure-conditioned decay and venue-state cost realism; (c) benchmark-first ML/model-complexity discipline.
3. **Several daily additions were explicitly preserved as foundational.** Localized conformal prediction, covariate-shift GOF, proper-score filters, non-Gaussian drawdown stress, AutoQuant, and manipulation-velocity diagnostics improve validation design even though they are not alpha signals.
4. **Adjacent-domain imports were accepted only as research-process or validation-method leads.** Anytime-valid agent evaluation, scalable VARMA, measurement-error-aware fixed-effect inference, and temporal-network event-graph contagion are useful only if translated into falsifiable evaluation or stress-test modules; no adjacent-domain lead was promoted as trading evidence.

## Inputs Reviewed

- [[01 Research Candidate Registry]] through the 2026-08-08 entries.
- [[09 Coding-Ready Backtest Queue]].
- [[Framework Candidate Registry]] and [[Open Research Questions]].
- Daily reviews: [[2026-08-03 1356 Daily Quant Research Review]], [[2026-08-04 1226 Daily Quant Research Review]], [[2026-08-05 1621 Daily Quant Research Review]], [[2026-08-06 1608 Daily Quant Research Review]], [[2026-08-07 1314 Daily Quant Research Review]], and [[2026-08-08 1313 Daily Quant Research Review]].
- Recent source notes including [[Decoupled Probabilistic IV Surface Forecasting and Arbitrage-Aware Refinement]], [[Microstructural Foundations of Rough Noise]], [[Conformal Kelly - Uncertainty-Scaled Fractional Position Sizing]], [[Drawdown Risk Beyond Brownian Motion - Non-Gaussian and Long-Memory Stress Tables]], [[Latent-Regime Bias Auditing for Volatility Forecasting]], [[Optimal Trading of Microstructure Mean Reversion]], [[Data-Driven Measures of High-Frequency Trading]], [[Axient Leveraged Event Markets - Credit and Finality Design]], [[Crypto Perpetual Liquidation Cascades - Event-Heterogeneous Early Warnings]], [[AMM Mandate Portfolios - Verifiable Band Rebalancing]], [[Proper-Score Observation-Driven Filters for Robust Forecast Validation]], [[Public Trader Identity - Adverse Selection and Return Predictability]], [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]], [[Generalized Mean Absolute Directional Loss for ML Trading Models]], [[Portfolio Allocation under Heterogeneous Scales and Multifractality]], [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]], [[Velocity and Regime-Aware Detection of Intraday Options Market Manipulation]], [[Cross-Sectional Heterogeneity in LSTM Networks for Financial Time Series]], [[Skewness Managed Anomaly Portfolios]], and [[Localized Conformal Prediction for Conditional Forecast Calibration]].
- Strategy notes: [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]], [[Option-Implied SDF Equity Premium Timing]], and [[Prediction-Market Structural Volatility Risk Filter]].
- Adjacent-domain pre-run leads across statistics, ML, econometrics, control/optimization, and complex systems.

## Framework Candidates Added / Updated

| Framework | Linked Notes | Change | Next Validation Step |
|---|---|---|---|
| Cost-aware decision-process diagnostics | [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]]; [[Drawdown Risk Beyond Brownian Motion - Non-Gaussian and Long-Memory Stress Tables]]; [[Velocity and Regime-Aware Detection of Intraday Options Market Manipulation]]; [[Localized Conformal Prediction for Conditional Forecast Calibration]]; [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]]; [[Proper-Score Observation-Driven Filters for Robust Forecast Validation]]; [[Optimal Execution with Passive Market Impact]] | Upgraded as the near-term coding target. It now needs explicit modules for execution/funding timestamp invariants, drawdown/recovery stress, local forecast calibration, covariate-shift target-regime checks, manipulation-like state labels, passive-fill realism, and action-attribution. | Implement one reusable report block that can run on any backtest output before new signal complexity is added. Minimal version: time gates, costs, turnover/liquidity, baseline comparisons, fold/regime metrics, drawdown stress, uncertainty/calibration panels, and action-attribution. |
| Uncertainty-aware sizing and forecast-calibration stack | [[Conformal Kelly - Uncertainty-Scaled Fractional Position Sizing]]; [[Localized Conformal Prediction for Conditional Forecast Calibration]]; [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]]; [[Latent-Regime Bias Auditing for Volatility Forecasting]]; [[Proper-Score Observation-Driven Filters for Robust Forecast Validation]]; [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]] | Strengthened from generic conformal/uncertainty language into a specific hierarchy: global coverage is insufficient; intervals must pass local/state coverage, target-regime GOF, regime-bias/tail-underprediction, and downstream sizing/action-attribution checks. | Build these as validation panels rather than separate strategies. Compare against rolling coverage, EWMA/GARCH/HAR, volatility/drawdown filters, and fixed fractional sizing. |
| Microstructure-conditioned decay and venue-state validation | [[Optimal Trading of Microstructure Mean Reversion]]; [[Microstructural Foundations of Rough Noise]]; [[Data-Driven Measures of High-Frequency Trading]]; [[Velocity and Regime-Aware Detection of Intraday Options Market Manipulation]]; [[Public Trader Identity - Adverse Selection and Return Predictability]]; [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]; [[OpenMarket Synchronized Polymarket-Binance Dataset]]; [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]] | Strengthened as a cross-venue falsification framework. Short-horizon reversal, order-flow, public-identity, and venue-transparent signals should be decomposed into efficient-price gaps, fleeting noise, HFT liquidity supply/demand, public attribution conventions, manipulation-like velocity states, passive fill probabilities, and venue fees before alpha claims. | For intraday/crypto/prediction-market studies, implement no-trade/cost-state labels first: spread/depth/volatility, passive-fill/adverse-selection stress, wallet churn, exchange-quality flags, settlement window tags, and liquidity-tail states. |
| Benchmark-first ML/model-complexity discipline | [[Cross-Sectional Heterogeneity in LSTM Networks for Financial Time Series]]; [[Generalized Mean Absolute Directional Loss for ML Trading Models]]; [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]; [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]]; [[Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization]] | Recent ML additions reinforce that architecture/loss novelty is not strategy evidence. Sector embeddings and GMADL are admissible as benchmark components only if they beat point-in-time sector dummies, tabular models, simple momentum/reversal, base-rate/always-up, turnover, borrow/funding, and held-out regime tests. | Keep LSTM/GMADL out of the coding queue. Add feature-admission and loss-admission checks to future ML backtests. |
| Equity anomaly decay and outlier-dependence audit | [[Skewness Managed Anomaly Portfolios]]; [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]]; [[A Cap-Axis Integral Diagnostic of Factor Models]]; [[Retail Traders Ruin - Anatomy of Popular Signal Failure]]; [[Two Accounting Anomalies - Accruals May Be Risk, PEAD May Be Mispricing]] | New skewness note supplies a concrete missing audit: measure right-tail contribution, percentile-capped performance, expected-skewness exposure, microcap/capacity/borrow overlap, and post-publication decay before trusting anomalies. | Before coding anomaly variants, inspect the original Gong-Lynch-Ogden paper and create an anomaly audit template with tail-contribution, cap-axis, factor controls, post-publication splits, and after-cost panels. |

## Cross-Paper Connection Table

| Source A | Source B / Existing Candidate | Connection Type | Framework Potential | Action |
|---|---|---|---|---|
| [[Localized Conformal Prediction for Conditional Forecast Calibration]] | [[Conformal Kelly - Uncertainty-Scaled Fractional Position Sizing]]; [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]] | Missing validation / reinforcement | High: conformal intervals used for sizing must pass local/state-specific calibration, not only full-sample coverage. | Add local coverage and downside-miss panels to forecast-uncertainty sizing experiments. |
| [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]] | [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]]; [[Regime-Conditional Distributional Comparison of Trading Strategies]] | Method transfer / deployment gate | Medium/high: target-regime GOF can catch source-to-target failures across assets, venues, and post-publication periods. | Treat as optional target-regime gate after simple drift/vol/drawdown alarms. |
| [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]] | [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]]; crypto futures ADL / exchange-risk stress filter | Missing validation / decay warning | High for crypto: funding visibility, timing, execution feasibility, cost scenarios, and accounting invariants are prerequisites before tuning. | Crypto-perp ideas remain unpromoted until AutoQuant-lite audit fields exist. |
| [[Velocity and Regime-Aware Detection of Intraday Options Market Manipulation]] | [[Optimal Trading of Microstructure Mean Reversion]]; [[Microstructural Foundations of Rough Noise]]; [[Can Reinforcement Learning Efficiently Discover Price Manipulation]] | Reinforces / contradiction | High for intraday: velocity states can be no-trade/stress labels, but incomplete labels and low precision prevent treating alerts as alpha. | Add manipulation-like shape diagnostics only as audit labels with action-attribution. |
| [[Skewness Managed Anomaly Portfolios]] | [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]]; [[A Cap-Axis Integral Diagnostic of Factor Models]] | Missing validation / decay warning | High for anomaly replication: performance may be concentrated in rare right-tail names rather than broad premium. | Do not promote anomaly overlays until original-paper rules, survivorship-free data, borrow, and tail-contribution diagnostics are specified. |
| [[Public Trader Identity - Adverse Selection and Return Predictability]] | [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]]; [[OpenMarket Synchronized Polymarket-Binance Dataset]] | Mechanism bridge / cross-venue caution | Medium: public identity can matter on transparent venues, but attribution conventions and wallet churn can dominate. | Keep as foundational diagnostic; require time-gated wallet ranking, placebo cohorts, book-probability/anonymous-flow baselines, and fees. |
| [[AMM Mandate Portfolios - Verifiable Band Rebalancing]] | [[Optimal Dynamic Fees in Automated Market Makers]]; [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]] | Cross-asset/domain bridge | Medium: AMM portfolio products bridge rebalancing and execution costs, but superiority depends on gas, MEV, dynamic fees, and stale-state arbitrage. | Keep as simulator/audit candidate, not LP alpha. |
| [[Portfolio Allocation under Heterogeneous Scales and Multifractality]] | [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]]; [[Characteristic-Driven Covariance from Fundamentals]]; [[Physics-Informed Cross-Covariance Forecasting]] | Method addition | Medium: signed multiscale dependence is another estimator candidate in a benchmark suite, not a new portfolio strategy. | Evaluate only after shrinkage/risk-parity/equal-weight baselines with turnover/concentration costs. |

## Adjacent-Domain Imports Worth Tracking

| Idea | Domain | Quant Use | Evidence / Caveat | Next Step |
|---|---|---|---|---|
| AV-AIVAT anytime-valid stopping for agent evaluation (`2608.06362v1`) | ML / decision theory / imperfect-information games | Research-process lead for expensive strategy-agent or model-challenger evaluations: stop when evidence is sufficient without invalid optional stopping. | Useful mechanism, but not finance evidence. Control-variate structure may not map cleanly to market backtests. | Add to validation-budget framework as a watch-only method for agent/backtest comparison; compare with fixed-holdout and sequential-testing baselines before use. |
| Scalable VARMA estimation (`2608.06340v1`) | Time-series / econometrics | Possible transparent benchmark for multivariate return/volatility/residual dynamics before deep sequence models or graph models. | Methodological lead only; no market edge. VARMA can still overfit high-dimensional finance without shrinkage and blocked validation. | Track as a baseline candidate for portfolio/risk dashboards if implementation/code becomes available. |
| Fixed-effect saturation and measurement-error inference (`2608.06053v1`) | Econometrics / causal inference | Event-study and panel strategy validation: distinguish fixed-effect saturation from weak identification and measurement-error attenuation in treatment/exposure variables. | Adjacent method; useful for PEAD, AMM protocol-fee, commodity-shock, and event-window research, but not alpha. | Add as a caution under event-study validation; require exposure reliability checks and pre-treatment path tests. |
| Temporal network spreading via event graphs (`2608.06175v1`) | Network science / complex systems | Potential framework for liquidation/contagion or settlement-event reachability where timestamps form event networks. | High metaphor risk. Needs actual event nodes/edges and out-of-sample warning improvement versus simple venue stress filters. | Watch-only; do not save as source note unless a future crypto venue dataset supports event-graph construction. |
| Risk in a Data-Rich Model (`2608.05676v1`) | Macro/financial econometrics | Macro tail-risk factor heterogeneity could supply ex ante regime covariates for portfolio/short-vol stress tests. | Adjacent macro risk, not a trading rule; may require vintage macro data and factor-estimation choices. | Watch-only until a public, timestamped macro/financial-condition panel is available. |
| Stiefel Muon / Skewon, SG-TULA, transport PDE stabilization | Optimization / control | Rejected for current library unless tied to a concrete portfolio estimator or robust-control validation problem. | Mostly optimizer/theory leads with no finance mechanism in current context. | No registry action. |

## Registry Upgrades / Downgrades

No new row was added to the candidate registry because the daily runs already added the useful 2026-08-03 through 2026-08-08 candidates. The weekly review made the following hygiene/classification decisions:

- **Standard cost/regime/liquidity/decision audit block:** effectively upgraded in priority relative to new signal work. It remains in the coding queue as High / ready-to-code and should be treated as the immediate coding target.
- **SPX/SPXW short-dated put-writing:** remains High but still data-blocked. It should not receive Kelly, VIX/SDF, conformal, density, or specialist-volatility overlays until a fixed-risk baseline with quote/fill/margin/audit outputs exists.
- **Sector-heterogeneous LSTM and GMADL:** preserved as foundational ML benchmark-design leads, not strategy candidates. Their coding priority remains Low/Medium because they lack point-in-time universe/data/cost/baseline evidence.
- **Skewness-managed anomaly overlay:** preserved as a Medium-priority anomaly validation overlay, not promoted. Original paper inspection is required before any coding.
- **Public wallet identity, options manipulation velocity, AMM mandate portfolios, Axient, and HFT measures:** preserved as foundational or diagnostic framework inputs. They are not retail-practical alpha without specialized data and cost/fill handling.
- **Adjacent-domain imports:** no registry rows added; accepted leads are watch-only validation/process methods unless later connected to a source note and falsifiable backtest design.

## Decay / Outdatedness Decisions

- Crowded **short-dated option selling** remains a high-decay-risk family because 0DTE market structure, crash gaps, quote widths, cash/margin accounting, and crowding can dominate sizing rules.
- **Equity anomalies** need post-publication, microcap/liquidity, borrow, cap-axis, and right-tail contribution diagnostics. Mean/Sharpe-only evidence is no longer acceptable for promotion.
- **Crypto order-flow / clock-phase / wallet-identity signals** face high decay from venue-specific mechanics, fees/funding, wallet churn, sybil behavior, exchange-quality shifts, and rapid public adaptation.
- **Prediction-market and DeFi/AMM strategies** are not portable across venues without settlement/oracle, fee, gas, MEV, stale-state, and attribution metadata.
- **Deep ML/AI portfolio policies and custom losses** are downgraded in practical urgency whenever they have not beaten simple tabular/rule baselines with temporal validation, turnover/costs, borrow/funding, and held-out regimes.

## Coding Queue Changes

Updated the coding queue wording to link this review and sharpen the immediate priority:

1. **Standard cost/regime/liquidity/decision audit block** stays High / Ready to code and is the next practical implementation target.
2. **SPX/SPXW short-dated put-writing** stays High but remains Research spec needed / data blocked; first coding step is still the fixed-risk baseline and audit outputs, not advanced sizing overlays.
3. **Forecast-uncertainty-aware ML sizing** and **Decision-aware covariance metrics** remain Medium method-integration items; neither has become a standalone strategy.

No new item was promoted into the coding queue.

## Open Research Questions Added / Retired

Added watch-only questions around adjacent-domain validation-method transfer:

- Can anytime-valid / control-variate evaluation methods reduce wasted agent/backtest comparisons without invalid optional stopping or under-testing rare tail failures?
- Can scalable VARMA or related transparent multivariate baselines improve risk-dashboard or sequence-model evaluation enough to justify complexity versus EWMA/HAR/GARCH, shrinkage covariance, and simple factor models?
- Can measurement-error-aware fixed-effect inference improve event-study validation for accounting anomalies, AMM protocol-fee changes, commodity shocks, and crypto venue events versus pre-treatment path tests and conventional clustered inference?
- Can temporal event-graph reachability describe liquidation, settlement, or venue-contagion episodes in a way that beats simple volatility, funding, open-interest, and exchange-quality stress filters?

No existing question was retired.

## Notes Updated

- Created this weekly review note.
- Updated [[Research Review Index]] with this review link.
- Updated [[Framework Candidate Registry]] with the 2026-08-09 synthesis summary.
- Updated [[Open Research Questions]] with selected adjacent-domain validation questions.
- Updated [[09 Coding-Ready Backtest Queue]] to link this weekly review and clarify the audit block as the immediate implementation target.
- Updated [[01 Research Candidate Registry]] metadata/sorting view to reflect the weekly priority shift toward audit infrastructure.

## Discord Summary Candidate

Weekly synthesis complete. The main decision is to code the standard audit block before new alpha or SPX overlays. No new signal was promoted. Recent papers strengthen uncertainty calibration, microstructure/venue-state realism, and benchmark-first ML discipline; adjacent-domain imports remain watch-only validation methods.
