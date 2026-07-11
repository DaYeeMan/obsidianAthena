---
type: daily-research-review
date: 2026-07-10
time: "0801"
tags: [quant-research, daily-review]
---

# 2026-07-10 0801 Daily Quant Research Review

## Run Context

- Primary collection input: blogwatcher-cli persistent feed state from `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`, plus arXiv query leads and adjacent-domain arXiv leads from the pre-run script.
- Feed scan status: blogwatcher found 5 new arXiv feed articles; Alpha Architect and Robot Wealth succeeded with no new items; Quantocracy returned HTTP 302 and Quantpedia returned HTTP 429. No fallback RSS scanner was used.
- Validation: selected arXiv leads were validated through the arXiv API `id_list` metadata before being saved. Feed entries were treated as discovery leads only.
- Scope focus: equities, options, crypto/prediction markets, market microstructure, portfolio/risk construction, and validation frameworks.

## High-Signal Items Saved

| Item | Classification | Practicality | Decision | Why it matters |
|---|---|---|---|---|
| [[Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium]] | Evidence-backed at abstract level as options/asset-pricing methodology | foundational / retail-adaptable with option-chain data | Keep; add registry row | Option-implied SDF features may forecast the equity premium and could become a richer SPX risk-premium throttle than VIX/skew alone, but only after arbitrage-clean option-chain preprocessing. |
| [[Volatility in Prediction Markets - A Structural Approach]] | Evidence-backed at abstract level as prediction-market volatility methodology | foundational / retail-adaptable | Keep; add registry row | Replaces generic ARCH/GARCH thinking in binary event contracts with structural features: probability level, time-to-resolution, spread, volume, and information-arrival category. |
| [[Robustness in Sequential Decision Making under Evolving Uncertainty]] | Evidence-backed at abstract level as sequential decision / market-making methodology | foundational | Keep; add registry row | Separates uncertainty tolerance from action robustness; useful for auditing whether risk filters improve net utility or simply over-throttle trades in illiquid states. |
| [[Low-Turnover Rebalancing for Sparse Index Tracking]] | Plausible-to-evidence-backed at abstract level with code | retail-adaptable / foundational | Keep; add registry row | Practical portfolio-maintenance idea: separate initial sparse tracker construction from low-turnover Δw repairs, with code available. |
| [[SoK - Market Microstructure for Decentralized Prediction Markets]] | Evidence-backed as survey / foundational | foundational | Keep; add registry row | Provides market-design taxonomy for decentralized prediction markets; useful before pooling Kalshi/Polymarket-style event data or testing settlement/volatility effects. |

## Screened / Not Promoted

- Adjacent-domain leads such as design-based spillover testing, prediction-powered active testing, and dynamical-process network inference were plausible method leads, but none beat today's directly finance-relevant papers for library promotion. They remain watch-only adjacent methods rather than trading evidence.
- `Stablecoins under Stress in a National Economy` was outside the immediate strategy/backtest priority because it appears more macro/transaction-evidence oriented than a clear trading or validation method from the available metadata.
- `Any Axes Are Allowed` may extend the existing cap-axis factor diagnostic, but the existing [[A Cap-Axis Integral Diagnostic of Factor Models]] note already covers the immediate framework need; defer until a future synthesis pass if the extension materially changes factor diagnostics.

## Candidate Details

### Option-implied SDF equity-premium forecasting

- **Hypothesis:** option-implied volatility-scaled SDF features forecast the equity premium and improve SPX allocation or short-volatility risk sizing versus Martin bounds, VIX, IV-rank, skew, and realized-volatility baselines.
- **Economic rationale:** option prices embed state prices and forward-looking risk premia; SDF shape across moneyness/maturity may capture risk compensation not visible in a single implied-volatility statistic.
- **Asset class/universe:** SPX/SPY index allocation and SPX/SPXW option-selling risk throttles.
- **Signal definition:** lagged option-implied SDF-derived equity-premium forecast, initially bucketed into quantiles or simple risk-on/risk-off thresholds.
- **Data requirements:** historical SPX option chains with bid/ask, quote timestamps, rates/dividends, underlying index levels, no-arbitrage preprocessing, and realized returns.
- **Backtest design:** walk-forward construction, monthly/weekly decision times, out-of-sample evaluation against simple baselines, and downstream net utility after turnover/costs.
- **Transaction-cost concerns:** option-chain bid/ask and stale quotes in signal construction; strategy-level costs for SPX/SPXW fills, margin, crash gaps, and allocation turnover.
- **Risks/failure modes:** SDF interpolation/extrapolation sensitivity, performance concentrated in crisis periods, spurious OOS forecast improvement, and risk-neutral signals misread as physical forecasts.
- **Validation priority:** medium-high after option-chain infrastructure exists.

### Structural prediction-market volatility

- **Hypothesis:** probability level, time-to-resolution, spread, volume, and event category forecast prediction-market volatility better than plain ARCH/GARCH and improve risk sizing or no-trade filters around settlement/event windows.
- **Economic rationale:** binary contract prices are bounded probabilities that resolve at known deadlines; volatility should rise with unresolved uncertainty, deadline pressure, and informed/adverse order flow.
- **Asset class/universe:** Kalshi/Polymarket-style binary event contracts with clean historical quotes/trades.
- **Signal definition:** ex ante structural volatility forecast bucket; initially used as a risk filter rather than a directional signal.
- **Data requirements:** contract metadata, category, resolution deadline, price, spread, volume, fees, and outcome timestamps available at decision time.
- **Backtest design:** contract-panel OOS forecasting by time-to-resolution and category; compare rolling volatility/GARCH, structural-only, and structural-plus-residual models; test whether filters improve net event-window strategy results.
- **Transaction-cost concerns:** wide spreads, fill probability, fees, adverse selection, liquidity around resolution, and platform-specific settlement mechanics.
- **Risks/failure modes:** category overfit, stale/liquidity-biased quotes, venue-transfer failure, and costs overwhelming forecast value.
- **Validation priority:** medium if prediction-market data ingestion becomes available.

### Robustness/action-response audit for decision policies

- **Hypothesis:** uncertainty-aware risk filters should be evaluated by the action changes they cause and their state-dependent opportunity costs; excessive robustness can reduce net profitability in illiquid states.
- **Economic rationale:** a model can estimate uncertainty well yet respond with a suboptimal decision policy; execution opportunity and liquidity determine whether conservatism helps or hurts.
- **Asset class/universe:** execution, market making, crypto, short-volatility sizing, and ML allocation systems.
- **Signal definition:** uncertainty estimate plus action-response function: size reduction, quote widening, no-trade, or liquidation rule.
- **Data requirements:** backtest trade/weight logs, uncertainty/risk scores, liquidity/spread proxies, and realized counterfactual returns for changed actions.
- **Backtest design:** add action-attribution tables showing when filters changed trades, avoided losses, missed gains, changed costs, and interacted with liquidity states.
- **Transaction-cost concerns:** opportunity cost, spread/impact, queue/fill assumptions for HFT applications, and turnover effects for slower portfolios.
- **Risks/failure modes:** robustness parameters tuned to past drawdowns, improved drawdown with worse net utility, and non-transferability from HFT to daily horizons.
- **Validation priority:** medium as a reusable audit-block enhancement.

### Low-turnover sparse index-tracker maintenance

- **Hypothesis:** a Δw maintenance layer can reduce turnover and trading-cost drag versus rolling sparse tracker reconstruction without materially worsening tracking error.
- **Economic rationale:** repeated reconstruction treats every window as a new portfolio problem; a decision-level repair rule can preserve stable holdings unless deterioration and directional evidence justify intervention.
- **Asset class/universe:** liquid ETF baskets, large-cap equity index tracking, or benchmark-tracking sleeves.
- **Signal definition:** rebalance only when realized tracking deterioration and posterior directional evidence jointly pass a threshold.
- **Data requirements:** benchmark constituents/returns, tradable asset returns, spread/cost estimates, and survivorship-aware constituent history where possible.
- **Backtest design:** compare full benchmark ETF, rolling sparse reconstruction, hold-initial sparse tracker, and Δw repair policy with turnover, tracking error, and net cost metrics.
- **Transaction-cost concerns:** spread/market-impact conversion of turnover, constituent liquidity, tax-unaware churn, and capacity in smaller names.
- **Risks/failure modes:** 2020-2025 sample overfit, survivorship bias, low turnover at unacceptable tracking error, and hyperparameter sensitivity.
- **Validation priority:** medium-low relative to strategy alpha, medium as portfolio implementation support.

### DePM market-design taxonomy

- **Hypothesis:** prediction-market strategy performance, volatility, and manipulation risk are conditional on market design, resolution, settlement, and trading architecture.
- **Economic rationale:** decentralized and centralized event markets differ in oracle/resolution process, settlement finality, fee/liquidity structure, and manipulation defenses.
- **Asset class/universe:** Polymarket/DePMs and comparison with centralized event markets such as Kalshi.
- **Signal definition:** not a trading signal; use design tags as covariates and split variables.
- **Data requirements:** venue/contract design metadata, resolution rules, settlement process, historical quotes/trades, and event outcomes.
- **Backtest design:** do not pool prediction-market contracts until design variables are tagged; test volatility/manipulation effects by design category.
- **Transaction-cost concerns:** fees, on-chain costs, liquidity, oracle risk, and settlement uncertainty.
- **Risks/failure modes:** taxonomy without empirical measurement, fast-changing market design, incomplete archival data.
- **Validation priority:** reference/foundational.

## Literature Connections / Framework Leads

### Reinforces

- [[Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium]] reinforces [[Arbitrage-Free Multi-Maturity Risk-Neutral Marginals]]: option-implied signals should be built from arbitrage-consistent distributions before being used for SPX risk-premium timing.
- [[Volatility in Prediction Markets - A Structural Approach]] and [[SoK - Market Microstructure for Decentralized Prediction Markets]] reinforce [[Settlement Manipulation in Prediction Markets]] by adding volatility and market-design conditioning variables.
- [[Robustness in Sequential Decision Making under Evolving Uncertainty]] reinforces the existing cost-aware decision-process diagnostics framework by making action response and missed-opportunity cost explicit.
- [[Low-Turnover Rebalancing for Sparse Index Tracking]] reinforces [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]] by judging portfolio methods through decision outcomes under costs, not only estimator fit.

### Contradicts / Weakens

- Plain ARCH/GARCH prediction-market volatility modeling is downgraded when structural bounded-contract variables are available.
- Rolling-window portfolio reconstruction without explicit turnover/cost maintenance is downgraded for sparse tracking applications.
- Generic “more robustness is safer” risk-filter logic is downgraded; robustness can hurt in illiquid states if it suppresses profitable execution opportunities.

### Transfers Across Asset Classes

- Prediction-market structural volatility ideas may transfer to crypto event markets and bounded-payoff tokens, but only after venue-design tags and settlement mechanics are modeled.
- Low-turnover maintenance logic may transfer from sparse index tracking to factor portfolios, crypto baskets, and ETF rotation systems.
- Option-implied SDF forecasting may transfer to crypto options only if liquid, arbitrage-cleaned chains exist; otherwise keep the idea SPX-focused.

### Missing Link Supplied

- Today's strongest framework link is an emerging **structural event-contract risk modeling** layer: settlement effects + structural volatility + decentralized-market design taxonomy. This is not yet a separate framework row, but the existing microstructure-conditioned decay/liquidity framework was updated to include the new prediction-market design and volatility dimensions.

## Registry / Queue Decisions

- Candidate registry: updated with five new rows.
- Source index: updated with five new source notes.
- Strategy index: updated with two plausible-but-untested strategy ideas.
- Framework registry: updated existing rows for cost-aware decision-process diagnostics and microstructure-conditioned decay/liquidity-state validation; no new framework row created because the prediction-market structural framework still needs a minimum viable data/backtest path.
- Open research questions: updated with prediction-market structural volatility/design and action-robustness audit questions.
- Coding-ready queue: reviewed but unchanged. None of today's items has enough local data/rules/cost specification to be promoted ahead of the existing SPX option baseline and standard audit-block work.

## Link Hygiene

New source-note titles created this run:

- [[Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium]]
- [[Volatility in Prediction Markets - A Structural Approach]]
- [[Robustness in Sequential Decision Making under Evolving Uncertainty]]
- [[Low-Turnover Rebalancing for Sparse Index Tracking]]
- [[SoK - Market Microstructure for Decentralized Prediction Markets]]

Intentional non-wikilink framework labels in this note: structural event-contract risk modeling, cost-aware decision-process diagnostics, and microstructure-conditioned decay/liquidity-state validation when referring to registry rows rather than standalone notes.
