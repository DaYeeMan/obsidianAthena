---
type: research-candidate-registry
created: 2026-06-28
last_updated: 2026-07-03
tags: [quant-research, candidate-registry, phase-2]
---

# Research Candidate Registry

This is the cross-library sorting/filtering table for research ideas. Daily reviews should update this registry when a candidate is added, materially reclassified, rejected, or flagged as outdated.

## Status Legend

- **Evidence-backed**: credible empirical/statistical evidence, but still requires implementation-specific validation.
- **Plausible but untested**: credible rationale or early evidence; not yet independently replicated here.
- **Speculative**: possible research lead with high uncertainty or fragile evidence.
- **Low quality**: weak methodology, unclear rules, or insufficient evidence.
- **Rejected**: not worth pursuing unless new evidence appears.

## Practicality Legend

- **retail-practical**: feasible with common data/tools and realistic retail execution.
- **retail-adaptable**: original version may be complex/institutional, but a simpler proxy is testable.
- **institutional-only**: requires privileged data, execution, scale, or infrastructure.
- **foundational**: important for methods/baselines even if not directly tradable.
- **outdated-watch**: may be decayed, crowded, obsolete, or superseded.

## Candidate Table

| Candidate | Asset Class | Strategy / Method Family | Status | Practicality | Coding Priority | Decay Risk | Last Reviewed | Primary Note | Next Action |
|---|---|---|---|---|---|---|---|---|---|
| AI-agent guarded anomaly replication and decay audit | Equities / AI agents / factor research | Backtest governance; anomaly decay; replication audit | Evidence-backed as practitioner replication/governance warning | foundational | Reference | High for published equity anomalies: post-publication decay, survivorship bias, construction errors, and agent-generated implementation mistakes can create false positives | 2026-06-30 | [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]] | Add replication guardrail block before coding old anomaly papers: survivorship-free data, post-publication split, implementation review, costs, and error traps. |
| AI consumption beta / AI premium proxy factor | Equities / thematic asset pricing | Alternative-data factor; AI exposure; long-short equity | Plausible but untested | institutional-only as written / retail-adaptable via public proxies | Low/Medium | High: proprietary data, tech/momentum confounding, narrative crowding, publication decay, and possible lookahead in public proxies | 2026-06-30 | [[AI Premium]] | Do not code until a timestamped public AI-exposure proxy and sector/factor-neutral validation design are specified. |
| Sign-vs-magnitude decomposition for short-horizon return predictability | Equities / crypto / microstructure | Return predictability diagnostic; short-horizon reversal validation | Evidence-backed as diagnostic | foundational / retail-adaptable | Medium | High for naïve lag-1 reversal: apparent autocorrelation may be bid/ask bounce, stale pricing, or magnitude shrinkage rather than directional alpha | 2026-06-30 | [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]] | Add sign-vs-magnitude decomposition before testing ETF/crypto short-horizon reversal; require spread/slippage-aware profitability. |
| Distributional-output-first ML forecasting under fat tails | Equities / crypto / ML | Forecast uncertainty; density prediction; model validation | Evidence-backed as methodology | foundational / retail-adaptable | Medium | Medium: improved calibration can fail to improve downstream post-cost portfolio decisions; mixture heads may overfit limited tail samples | 2026-06-30 | [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]] | Compare point vs Gaussian/mixture/quantile/conformal outputs with CRPS, coverage, and downstream sizing utility before adding complex backbones. |
| Liquidity-demand audit for strategy backtests | Equities / crypto / options execution | Transaction costs; liquidity consumption; capacity audit | Plausible but untested | foundational / retail-adaptable | Medium | Medium/High: daily proxies may miss intraday execution; liquidity-demand estimates can be noisy but unmodeled liquidity costs can erase edge | 2026-06-30 | [[Liquidity-Based Audit of Algorithmic Trading Strategies]] | Add simplified liquidity-consumption/provider diagnostics to backtest reports; test whether strategy profits coincide with costly liquidity-demand states. |
| Cost-aware time-gated LLM portfolio-agent evaluation | Portfolio / ML agents | Benchmarking; leakage control; process diagnostics | Evidence-backed as benchmark design | foundational | Reference | High for return-only LLM trading demos: lookahead, benchmark contamination, prompt drift, and missing costs can create false alpha | 2026-06-30 | [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]] | Use as governance reference before trusting any LLM portfolio-agent result; require TimeGate, costs, audit trail, and fixed-rule baselines. |
| SPX/SPXW short-dated put-writing with VIX and fractional-Kelly sizing | Options / equities | Volatility risk premium; position sizing | Plausible but untested | retail-adaptable | High | High: crowded short-vol, 0DTE market-structure shift, crash risk, bid/ask realism | 2026-06-28 | [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] | Replicate fixed-risk baseline first; require bid/ask fills, regime splits, margin/cash treatment. |
| Decision-aware covariance estimation for GMVP under heavy tails | Portfolio/risk | Covariance estimation; portfolio construction | Evidence-backed as methodology | foundational / retail-adaptable | Medium | Low as concept; turnover/cost risk in application | 2026-06-28 | [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]] | Add decision-regret metrics to portfolio backtests; compare against equal-weight/inverse-vol/Ledoit-Wolf. |
| Forecast-uncertainty-aware ML asset pricing | Equities / ML | Forecast uncertainty; sizing/shrinkage | Evidence-backed as methodology | foundational / retail-adaptable | Medium | Medium: ML forecasts unstable; confidence intervals can be miscalibrated under regime shift | 2026-06-28 | [[2026-06-28 Daily Quant Research Review]] | Create source note if reused; apply uncertainty shrinkage to ML alpha forecasts. |
| CryptoGAT / price-only crypto sequence-model skepticism | Crypto / ML | Forecasting baseline / model warning | Plausible but untested | retail-adaptable / outdated-watch | Medium | High: crypto regimes change quickly; price-only DL often fails after fees | 2026-06-29 | [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]] | Replicate only against strong simple baselines and fee-aware crypto cross-sectional rules; treat as warning first, not production alpha. |
| Continuous heavy-tail HMMs for equity return simulation and regime-conditional VaR | Equities / portfolio / risk | Regime models; synthetic data; risk modeling | Plausible but untested | foundational / retail-adaptable | Medium | Medium: predictive value may be limited even if stylized-fact fit is strong; risk of complexity without downstream decision gain | 2026-06-29 | [[Continuous Hidden Markov Models for Equity Returns]] | Use as simulation/risk baseline first; compare against EWMA vol and simple regime filters before any strategy deployment. |
| Crypto Granger-causality interaction networks | Crypto | Lead-lag / network features | Speculative | retail-adaptable only at slower horizons | Low/Medium | High: multiple testing, latency, fees, delistings, nonstationarity | 2026-06-28 | [[2026-06-28 Daily Quant Research Review]] | Only test with false-discovery controls and slow-horizon proxy; otherwise deprioritize. |
| Square-root law of market impact in U.S. large-cap equity | Equities / microstructure | Slippage/capacity model | Evidence-backed as execution-cost reference | institutional-only / foundational | Medium | Low as concept; direct ITCH/metaorder inference not retail-practical | 2026-06-28 | [[2026-06-28 Daily Quant Research Review]] | Use as cost-model reference, not alpha. Consider square-root participation penalty when scaling strategies. |
| Regime-conditional distributional strategy evaluation | Equities / options / crypto / portfolio | Strategy validation; regime-aware performance diagnostics | Evidence-backed as methodology | foundational / retail-adaptable | Medium | Medium: regime slicing can become data mining; flexible distributional models can overfit fold-level metrics; costs must be included before declaring conditional dominance | 2026-07-01 | [[Regime-Conditional Distributional Comparison of Trading Strategies]] | Add fold-level, regime-conditioned net performance diagnostics to future backtests before promoting ML, short-vol, crypto, or allocation strategies. |
| Prediction-market settlement manipulation diagnostics | Crypto / prediction markets / microstructure | Event study; market-design risk; settlement-window reversal | Evidence-backed at abstract level | foundational / retail-adaptable | Low/Medium | High: effect may decay after platform design changes; minute-level execution, fees, exchange fragmentation, and latency can erase tradability | 2026-07-01 | [[Settlement Manipulation in Prediction Markets]] | If data are available, test BTC settlement-window order-flow/reversal against matched non-settlement windows and longer contract horizons; use first as a risk filter. |
| Cost-aware execution policy for statistical arbitrage | Equities / stat arb / execution | Path-dependent signal execution; turnover and impact control | Plausible but untested | foundational / retail-adaptable | Low/Medium | Medium/High: pair selection leakage, path-feature overfit, borrow/spread costs, and accounting-only outperformance can create false edge | 2026-07-01 | [[Signature-Based Optimal Execution for Statistical Arbitrage]] | Keep as execution-design reference; only code after defining a pairs universe, walk-forward pair selection, simple baselines, and realistic cost model. |
| End-to-end AI portfolio policies versus simple rules | Futures / ETFs / portfolio / ML | Cross-asset timing; parametric portfolio policies; AI benchmark design | Evidence-backed at abstract level as model-evaluation study | foundational / retail-adaptable | Medium | Medium/High: deep policies may overfit differentiable Sharpe, hidden leverage/turnover, roll assumptions, and pooled metrics; costs can erase LSTM-style gross gains | 2026-07-02 | [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]] | Use as benchmark design for any allocation ML: compare equal weight, risk parity, time-series momentum, and linear policies before LSTM/transformer; require turnover/cost/regime stress. |
| Liquidity-tail-aware market impact and price discovery | Equities / futures / crypto microstructure | Market impact; liquidity shocks; order-flow interpretation; cost stress | Evidence-backed as theory | foundational | Reference | Medium: theory may be hard to identify empirically; liquidity-tail proxies can be noisy and regime-dependent, but ignoring state-dependent impact can understate costs | 2026-07-02 | [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]] | Add liquidity-tail/large-order state diagnostics to cost models before interpreting volume spikes as informed alpha or assuming constant slippage. |
| Microstructure-conditioned short-term trend decay audit | Futures / ETFs / trend-following | Trend-following decay; tick-size/liquidity stratification; market-impact feedback | Evidence-backed at abstract level | foundational / retail-adaptable | Medium | High for short-speed trend: post-2009 decay, HFT market-making changes, small-tick execution costs, and pooling across contracts can hide nonstationarity | 2026-07-03 | [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]] | Add tick-size/liquidity buckets and post-2009 net-of-cost splits before coding short-term trend-following or trend/reversal hybrids. |
| Monthly liquidity-impact premium proxy | Equities | Liquidity premium; order-flow/price-impact asset pricing; cross-sectional returns | Plausible but untested | retail-adaptable / foundational | Low/Medium | High: 2020–2025 sample is short; signed order-flow may be inaccessible; small-cap liquidity premia can disappear after spreads, impact, delistings, and factor controls | 2026-07-03 | [[Liquidity Premium and Investment Horizons]] | Test only as a conservative lagged liquidity-stress proxy with survivorship-free data, factor controls, and strict liquidity/cost filters. |
| Cap-axis factor-model diagnostic | Equities / factor research | Factor model validation; cap-rank residual alpha; anomaly replication guardrail | Evidence-backed at abstract level as methodology | foundational | Reference | Medium: requires clean CRSP-style data; cap-rank effects can be microcap/cost artifacts; diagnostic should not become a fitted objective | 2026-07-03 | [[A Cap-Axis Integral Diagnostic of Factor Models]] | Add size/cap-rank residual diagnostics to anomaly replication before treating factor Sharpe or t-stats as robust evidence. |
| Regime-routed volatility specialist forecasts | ETFs / options / crypto risk | Volatility forecasting; state-dependent specialist routing; risk throttling | Plausible but untested | foundational / retail-adaptable | Medium | Medium: small ETF panel; gating can overfit regimes; forecast-loss gains may not improve downstream net utility or may increase turnover | 2026-07-03 | [[Risk-Sensitive Specialist Routing for Volatility Forecasting]] | Consider as a risk-control module for SPX put-writing/ML allocation after EWMA/GARCH/rolling-realized-vol baselines are implemented. |

## Sorting Views

### Highest Coding Priority

1. [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] — High priority, but only if option-chain data with bid/ask are available.
2. Decision-aware covariance metrics — Medium priority, useful across portfolio/risk backtests.
3. Forecast-uncertainty-aware ML sizing and distributional-output validation — Medium priority, useful when ML scores are introduced.
4. Regime-conditional distributional strategy evaluation — Medium priority as a validation layer for ML, short-vol, crypto, and allocation backtests.
5. End-to-end AI portfolio policies versus simple rules — Medium priority as a benchmark design for allocation ML, but only after a clean futures/ETF universe and cost model are specified.
6. Liquidity-demand audit, liquidity-tail diagnostics, sign-vs-magnitude decomposition, and microstructure-conditioned short-term trend decay — Medium priority as validation layers before promoting short-horizon strategies.
7. Regime-routed volatility specialist forecasts — Medium priority as a risk-control module after EWMA/GARCH/rolling-realized-vol baselines exist.

### Outdated / Decay Watch

- Published equity anomaly replications without survivorship-free data, post-publication splits, transaction costs, and independent implementation checks.
- Public AI-theme factor claims that fail sector/momentum/mega-cap concentration controls or rely on inaccessible proprietary alternative data.
- Pure price-only deep learning for crypto forecasting.
- Crowded short-dated option-selling strategies, especially 0DTE-era variants.
- High-frequency crypto lead-lag/network claims without fee/latency/multiple-testing controls.
- Naïve lag-1 ETF/crypto reversal claims that do not separate directional predictability from magnitude shrinkage, stale pricing, or bid/ask bounce.
- Return-only LLM trading-agent benchmarks without time-gated inputs, transaction costs, and auditable decision trails.
- Ultra-short-horizon prediction-market contracts settling on manipulable underlying prices, especially when settlement-time order flow and post-settlement reversal are present.
- Stat-arb accounting outperformance that optimizes signal thresholds while ignoring execution path, turnover, inventory liquidation, borrow, and market impact.
- AI portfolio policies that beat simple rules only gross of costs, only through high turnover/leverage, or only in pooled metrics without regime/sub-asset robustness.
- Volume-spike or large-trade signals that assume large trades are always informed rather than possibly heavy-tailed liquidity shocks.
- Short-speed trend-following claims that pool contracts across tick-size/liquidity regimes or rely on pre-2009 gross performance without market-structure and cost splits.
- Liquidity-premium implementations concentrated in illiquid/small-cap names without spread, delisting, borrow, and capacity controls.
- Volatility forecast routers that improve average forecast loss but fail to improve downstream net utility, turnover, or drawdown control.

### Foundational References to Keep

- Decision-aware covariance estimation.
- Forecast uncertainty and distributional-output evaluation in ML asset pricing.
- Square-root market impact / capacity modeling.
- Liquidity-demand audit and microstructure-aware predictability decomposition.
- Cost-aware, time-gated evaluation of LLM portfolio agents.
- Regime-conditional distributional strategy evaluation.
- Prediction-market settlement manipulation diagnostics.
- Cost-aware execution policy design for statistical arbitrage.
- Simple-rule benchmark-first evaluation of AI portfolio policies.
- Liquidity-tail-aware market impact and price-discovery modeling.
- Microstructure-conditioned trend decay and tick-size/liquidity stratification.
- Cap-axis and size-rank residual diagnostics for factor/anomaly validation.
- Regime-routed volatility specialist forecasts as risk-control modules.

## Maintenance Rules

- Update this note after each daily review when a new candidate is worth tracking.
- Do not add every screened paper; only add items that are useful as a strategy candidate, warning, foundational method, or rejection reference.
- If a candidate appears in multiple daily reviews, update the existing row rather than duplicating it.
- If evidence improves or worsens, update `Status`, `Practicality`, `Decay Risk`, and `Next Action`.
- If a candidate becomes coding-ready, create or link a backtest spec under [[Quant Research/04 Backtest Specs/Backtest Spec Index|Backtest Spec Index]].
