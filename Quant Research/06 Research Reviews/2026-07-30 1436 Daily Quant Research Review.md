---
type: daily-quant-research-review
created: 2026-07-30 1436 EDT
source_status: partial-blogwatcher-coverage
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review]
---

# 2026-07-30 1436 Daily Quant Research Review

## Run Status

- Primary RSS/practitioner collector: blogwatcher-cli was available and scanned 7 feeds using persistent state.
- Feed coverage was partial: Alpha Architect, Robot Wealth, and arXiv q-fin feeds scanned; Quantocracy failed with HTTP 302 and Quantpedia timed out during this scan. Practitioner coverage should therefore be treated as incomplete.
- arXiv metadata was directly validated through the arXiv API before source-note creation. Feed entries were used only as discovery leads.
- Semantic Scholar: arXiv:2607.27188 returned 0 citations / 0 influential citations / 40 references; arXiv:2605.10486 returned 0 citations. Other lookups were rate-limited and are recorded as unavailable rather than fabricated.

## High-Signal Items Saved

| Item | Classification | Practicality | Decision | Why it matters |
|---|---|---|---|---|
| [[Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes]] | Evidence-backed at abstract level as validation methodology | foundational / retail-adaptable with option-chain data | Saved source + registry row | Option-price fit is not density recovery; risk-neutral tail/skew features need density-level stress tests before SPX/SPXW short-vol or equity-premium timing use. |
| [[OpenMarket Synchronized Polymarket-Binance Dataset]] | Evidence-backed at abstract level as public dataset and negative-result benchmark | foundational / retail-adaptable with dataset | Saved source + registry row | Public paired Polymarket/Binance data reduces the data blocker for prediction-market settlement studies, while the reported negative trading result makes Polymarket book probability the hard baseline. |
| [[Crypto Perpetual Liquidation Cascades - Event-Heterogeneous Early Warnings]] | Evidence-backed at abstract level as crypto liquidation-risk methodology | foundational / retail-adaptable with exchange data | Saved source + registry row | Crash-warning variables are event-heterogeneous: price works for some endogenous buildups, leverage/order-flow for others, and sudden news shocks may have no early-warning signature. |
| [[Physics-Informed Cross-Covariance Forecasting]] | Plausible-to-evidence-backed at abstract level as covariance methodology | foundational / retail-adaptable | Saved source + registry row | Adds a constrained learned singular-value cleaner to the decision-aware covariance benchmark suite; must beat shrinkage/factor/EWMA after turnover and concentration controls. |
| [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]] | Evidence-backed at abstract level as market-design/stress-test methodology | foundational | Saved source + registry row | Revised event-linked perpetual papers warn that binary/event payoff support, settlement, collateral, and oracle design create failure modes that do not port from ordinary crypto perps. |

## Screened but Not Saved / Downgraded

- **Bitcoin Runs on a Clock: Why Every Price Indicator Dies and the Halving Clock Doesn't** (arXiv:2607.26188v1): watch-only. It has code/data and may be useful as a cycle-indicator decay warning, but retrospective turn identification and halving-cycle narrative risk are high. Not saved because it does not yet improve a concrete strategy or validation framework beyond the existing crypto bubble/outdated-watch notes.
- **Multi-Currency AMMs for Decentralized FOREX Markets** (arXiv:2607.26405v1): plausible DeFi market-design theory but outside the current equities/options/crypto-priority implementation path; not saved today.
- **Herding, Momentum, and Reversal in China's A-Share Market** (arXiv:2607.27063v1): agent-based simulation, not direct trading evidence; not saved because existing herding/liquidity-stress notes already cover the validation lesson more directly.
- **BayesAME: Bayesian Active Model Evaluation** and **Parameter-Free Dynamic Regret for Online Convex Optimization under Heavy-Tailed Noise**: adjacent-method leads only. Useful concepts for validation-budget and online learning, but not translated into a finance-specific candidate today.
- Rainfall, degree-distribution, network-reconstruction, and general physics/network items were outside scope or too indirect for source-note promotion.

## Literature Connections / Framework Leads

### Reinforces

- [[Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes]] reinforces [[Arbitrage-Free Multi-Maturity Risk-Neutral Marginals]], [[Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium]], and [[RIDGE Autonomous Validation for LLM-Generated Option Pricing]] by adding an inverse-problem identifiability gate: recovered density features can be economically unstable even when option prices fit.
- [[OpenMarket Synchronized Polymarket-Binance Dataset]] reinforces [[Settlement Manipulation in Prediction Markets]] and [[Prediction-Market Structural Volatility Risk Filter]] by supplying a public paired dataset and a negative baseline.
- [[Crypto Perpetual Liquidation Cascades - Event-Heterogeneous Early Warnings]] reinforces [[Risk-Based Auto-Deleveraging]] by turning liquidation/ADL risk into event-clustered, state-variable-specific validation rather than one universal crypto crash indicator.
- [[Physics-Informed Cross-Covariance Forecasting]] reinforces [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]], [[Characteristic-Driven Covariance from Fundamentals]], and [[Parameter-Efficient Neural GMVP for Volatility Drag Mitigation]].
- [[Event-Linked Perpetual Futures - Mechanical Stress Tests and Taxonomy]] reinforces [[SoK - Market Microstructure for Decentralized Prediction Markets]], [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]], and [[Settlement Manipulation in Prediction Markets]].

### Contradicts / Weakens

- OpenMarket weakens naive “external BTC order flow predicts Polymarket settlement better than the venue book” claims: reported walk-forward logistic trading was negative after stated fees/slippage.
- The liquidation-cascade paper weakens one-size-fits-all crypto crash-warning filters: early-warning location varies by event type.
- The risk-neutral-density paper weakens option pipelines that treat pricing RMSE as sufficient proof of tail/skew signal validity.
- Event-linked perps weaken direct transplantation of crypto perpetual funding/leverage mechanics into bounded binary/event claims.

### Transfers Across Asset Classes

- Option inverse-problem null-space diagnostics transfer to any latent market-state reconstruction problem: validate downstream decisions, not only reconstruction or price fit.
- Crypto liquidation event heterogeneity transfers to equity/options stress testing: endogenous positioning/liquidity crises and exogenous news jumps should be bucketed separately.
- Prediction-market book-probability baselines transfer to other event-linked markets: venue-implied prices are strong baselines that external features must beat after costs.

## Registry / Queue Decisions

- Candidate registry: updated with five new candidates.
- Framework registry: updated in the recent framework section for option-chain inverse validation, prediction-market dataset/design validation, crypto liquidation risk, and covariance model benchmarking.
- Open questions: updated with new option-density, prediction-market data, and liquidation early-warning questions.
- Coding-ready backtest queue: reviewed and left unchanged. None of today’s items supplies full rules, data access confirmation, cost assumptions, baselines, validation design, and go/no-go thresholds sufficient for queue promotion. The most actionable future path is to verify/reproduce OpenMarket as a dataset before designing prediction-market settlement studies.

## Validation Priority

1. If prediction-market research becomes active: obtain/reproduce the OpenMarket v0.5.2 data pipeline, reproduce the negative logistic benchmark, then test settlement-window hypotheses with matched non-settlement controls.
2. For SPX/SPXW option research: add density-identifiability checks to the option-chain preprocessing plan before using risk-neutral tails/skew as sizing features.
3. For crypto futures risk throttles: label liquidation cascades by endogenous-buildup versus exogenous-shock type and compare early-warning variables against simple volatility/drawdown/funding filters with false-exit cost accounting.
4. For covariance research: keep adding estimators only inside the existing decision-aware suite; do not let neural cross-covariance claims bypass Ledoit-Wolf, nonlinear shrinkage, EWMA, factor covariance, equal weight, inverse-vol, and risk-parity baselines.

## Hygiene Notes

Post-write hygiene check should verify that all five new source-note titles appear in this review, Source Index, and registry; no intentional unresolved wikilinks were added for concept/framework labels.
