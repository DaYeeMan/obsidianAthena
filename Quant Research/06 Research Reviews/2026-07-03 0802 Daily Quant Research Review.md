---
type: daily-quant-research-review
created: 2026-07-03 0802 EDT
period: daily
source_mode: blogwatcher-cli primary plus arXiv API validation
asset_focus: [equities, options, crypto, futures, portfolio]
tags: [quant-research, daily-review]
---

# 2026-07-03 0802 Daily Quant Research Review

## Run Context

- Primary feed collector: blogwatcher-cli persistent state. Scan succeeded for 5/7 feeds; Quantocracy returned HTTP 302 and Quantpedia returned HTTP 429, so those practitioner feeds were not usable today.
- arXiv/API metadata was used to validate the saved candidates. Feed entries were treated as discovery leads only.
- No coding queue promotion today: the new items improve validation, decay, and risk modules, but none yet have full rules/data/cost/go-no-go specification.

## High-Signal Items Saved

| Item | Classification | Practicality | Why saved | Action |
|---|---|---|---|---|
| [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]] | Evidence-backed at abstract level | foundational / retail-adaptable | Strong microstructure explanation for short-speed trend decay after ~2009; tick-size/liquidity conditioning is directly useful for trend and reversal backtest design. | Add tick-size/liquidity bucket and post-2009 net-cost splits before coding short-term trend. |
| [[Liquidity Premium and Investment Horizons]] | Plausible but untested | retail-adaptable / foundational | Recent CRSP/order-flow evidence that Kyle lambda and signed order flow predict one-month returns; useful but likely hard to implement without order-flow data. | Test only with lagged liquidity-impact proxies, strict factor controls, and liquidity/cost filters. |
| [[A Cap-Axis Integral Diagnostic of Factor Models]] | Evidence-backed at abstract level as methodology | foundational | Adds a cap-rank residual diagnostic for factor models that is distinct from Sharpe gain and size exposure. | Add size/cap-rank residual tables to anomaly/factor replication guardrails. |
| [[Risk-Sensitive Specialist Routing for Volatility Forecasting]] | Plausible but untested | foundational / retail-adaptable | State-dependent volatility model routing may be useful for risk throttles; abstract reports lower high-volatility and underprediction loss in ETF walk-forward tests. | Consider as a later SPX put-writing / allocation risk module after EWMA/GARCH/rolling-vol baselines. |

## Screened but Not Saved as Source Notes

- Reliability-Aware ETF Tail-Risk Monitoring (arXiv:2604.08765v3): useful companion idea for data-quality-aware tail-risk surveillance, but the specialist-routing paper was the stronger single method note today.
- What Happens When Institutional Liquidity Enters Prediction Markets (arXiv:2604.10005v3): **not promoted** because the arXiv metadata says the paper has been withdrawn and superseded by a substantially different empirical paper. Keep as a watch lead only; do not use synthetic proof-of-concept claims as evidence.
- Adjacent-domain leads from LLM monitoring, econometrics, robust control, and complex systems were screened but not saved because none supplied a direct, falsifiable improvement beyond existing library frameworks today.
- Alpha Architect feed items were seen from prior run context and did not beat the academic additions for today’s limited save set.

## Literature Connections / Framework Leads

### Reinforces

- [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]] reinforces [[Regime-Conditional Distributional Comparison of Trading Strategies]]: short-horizon strategy performance should be conditioned on market-structure regimes, not averaged across decades.
- [[Liquidity Premium and Investment Horizons]] reinforces [[Liquidity-Based Audit of Algorithmic Trading Strategies]] and [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]: liquidity state matters both for expected returns and for implementation/cost stress.
- [[A Cap-Axis Integral Diagnostic of Factor Models]] reinforces [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]] by adding another diagnostic before accepting factor/anomaly evidence.
- [[Risk-Sensitive Specialist Routing for Volatility Forecasting]] reinforces [[Forecast-uncertainty-aware ML asset pricing]] and [[Continuous Hidden Markov Models for Equity Returns]] by tying state-dependent forecasts to a practical sizing/risk decision.

### Contradicts / Weakens

- Generic short-term trend-following claims that pool futures contracts across tick-size/liquidity regimes or rely on pre-2009 gross performance are now on stronger decay watch.
- Broad illiquidity-premium claims are not implementable by default: if the premium lives in high-spread, low-capacity names, retail feasibility is doubtful.
- Prediction-market liquidity research based on the withdrawn synthetic proof-of-concept should not be cited as evidence until the superseding empirical paper appears.

### Framework Updates

Updated the framework registry rather than adding a new standalone framework:

- Cost-aware decision-process diagnostics now links cap-axis factor diagnostics, liquidity-impact premia, and microstructure-conditioned trend decay.
- Regime-conditional distributional strategy evaluation now links specialist volatility routing and trend-decay market-structure conditioning.
- Distributional-forecast-first ML strategy evaluation now includes risk-sensitive specialist routing as a practical state-dependent forecast architecture.

## Candidate Registry Updates

Added four tracked candidates:

1. Microstructure-conditioned short-term trend decay audit.
2. Monthly liquidity-impact premium proxy.
3. Cap-axis factor-model diagnostic.
4. Regime-routed volatility specialist forecasts.

Also updated sorting/decay/foundational sections to reflect short-term trend decay, liquidity-premium implementation traps, cap-axis diagnostics, and volatility-routing utility tests.

## Coding Queue Review

No change. The new candidates are useful but not coding-ready. The closest future coding support item is to add microstructure/tick-size splits and regime-conditioned net metrics to any trend-following or short-horizon reversal backtest.

## Hygiene Notes

- New source notes were created under `Quant Research/01 Sources/` and added to [[Source Index]].
- Review index was updated separately to link this timestamped note.
- Major wikilinks in this note point to existing source notes or notes created in this run.
