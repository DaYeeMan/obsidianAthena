---
type: daily-quant-research-review
created: 2026-07-21 0802 EDT
source_status: normal-with-partial-feed-errors
tags: [quant-research, daily-review, arxiv, blogwatcher]
---

# 2026-07-21 0802 Daily Quant Research Review

## Run Status

- Primary feed context came from persistent `blogwatcher-cli` state, not the degraded stdlib fallback.
- Feed scan found 10 new articles; 5 of 7 feeds succeeded. Quantocracy returned HTTP 302 and Quantpedia timed out during scan, so practitioner coverage is partial today.
- arXiv metadata was directly validated for selected high-signal leads via the arXiv API before notes were created.
- Coding-ready queue reviewed and left unchanged: today’s items improve validation/framework coverage but do not yet provide complete rules, data, costs, baselines, and go/no-go criteria for a new implementation.

## High-Signal Items Saved

| Item | Evidence Quality | Practicality | Action | Why it matters |
|---|---|---|---|---|
| [[FinBench - Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting]] | Evidence-backed at abstract level as benchmark design | foundational / retail-adaptable | New source note; registry/framework update | Adds Brier/Winkler calibration and interval scoring to time-gated LLM/agentic financial forecasting. Useful governance before any agent forecast affects sizing or allocation. |
| [[Herding and Liquidity in Order-Book Markets II - Fundamental Anchoring and Liquidity Resilience]] | Evidence-backed at abstract level as market-microstructure theory/simulation | foundational / retail-adaptable via proxies | New source note; registry/framework update | Extends the existing herding-liquidity note by identifying fundamental anchoring and one-sided book stress as the persistence mechanism behind liquidity crises. |
| [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]] | Evidence-backed at abstract level as market-design / market-making theory | foundational / retail-adaptable if quote/trade data become available | New source note; registry/framework update | Adds AMM loss distribution, binary settlement risk, and optimal quoting mechanics to the existing prediction-market settlement/volatility/venue-design thread. |

## Screened But Not Promoted

- AlphaZeroBeta: Deep Reinforcement Learning for Market-Neutral Portfolios (arXiv:2607.18001v1) — plausible but not saved today. It reports DRL portfolio gains and includes transaction costs/walk-forward claims, but adds little beyond existing AI portfolio-policy warnings until the full paper verifies baseline strength, turnover, leverage, constituent handling, and regime/fold robustness. Existing note [[SciPhy Reinforcement Learning for Portfolio Optimization]] plus the simple-rule benchmark-first framework already cover the immediate governance implication.
- Portfolio Optimization under Heavy Tails and Asymmetric Volatility: Evidence from Taiwan-Exposed ETFs (arXiv:2607.16450v1) — plausible regional ETF risk study, not promoted. It reinforces heavy-tail/CVaR and asymmetric-volatility stress testing but appears narrow and does not beat the library’s existing regime-conditional and covariance/risk-state references.
- Asymptotic and finite-sample distributions of empirical relative entropy (arXiv:2512.16411v2) — useful adjacent statistical update, not separately saved. It reinforces power-calibrated divergence monitoring, but current note [[Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring]] is already the more finance-specific anchor.
- Volatility-Aware Extreme Event Detection in High-Frequency Financial Markets (arXiv:2607.17555v1) — watch only. The target-design lesson is useful, but the abstract reports high-frequency Bitcoin LOB classification rather than post-cost trading utility; save only if the full paper provides leakage controls, realistic execution, and strong naive/volatility baselines.
- Alpha Architect “Cashless payment and financial inclusion” — outside systematic trading scope for this library; not promoted.

## Literature Connections / Framework Leads

### Reinforces

- [[FinBench - Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting]] strengthens [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]], [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]], and [[Forecast-uncertainty-aware ML asset pricing]] by making calibrated probability and interval forecasts the required intermediate object before sizing.
- [[Herding and Liquidity in Order-Book Markets II - Fundamental Anchoring and Liquidity Resilience]] strengthens [[Herding and Liquidity in Order-Book Markets - A Robust Liquidity-Stress Crossover]], [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]], and [[When Does Order Flow Matter - State-Dependent L2 Liquidity-State Transitions in Crypto Futures]] by separating ordinary volatility from one-sided liquidity stress and anchor failure.
- [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]] strengthens [[Settlement Manipulation in Prediction Markets]], [[Volatility in Prediction Markets - A Structural Approach]], [[SoK - Market Microstructure for Decentralized Prediction Markets]], and [[Prediction-Market Structural Volatility Risk Filter]] by adding market-maker/AMM loss mechanics and binary settlement risk.

### Transfers Across Asset Classes

- Fundamental anchoring can be proxied differently across venues: ETF NAV/futures fair value in equities/futures, spot-perp basis/funding in crypto, and conditional event probability/time-to-resolution in prediction markets. The common test is whether a strategy’s gross edge survives in states where the anchor weakens and liquidity becomes one-sided.
- Agentic forecast calibration transfers from LLM portfolio agents to any ML return/volatility forecast: probability/interval quality must beat base-rate, volatility-only, and simple tabular baselines before position sizing.

### Missing Link Supplied

- The prediction-market AMM pair supplies the liquidity-provider side of the market-design framework. Prior notes focused on settlement manipulation, volatility, and venue taxonomy; today’s papers explain why spreads/subsidies/AMM losses may be rational compensation for resolution risk rather than obvious inefficiency.
- Herding II supplies an anchor-quality variable missing from the microstructure-conditioned validation framework.

## Candidate Registry Updates

Added or updated rows for:

1. Agentic financial forecast calibration benchmark.
2. Fundamental-anchoring liquidity-stress filter.
3. Prediction-market AMM / market-making design risk.

## Coding Queue Review

No changes. None of today’s items has enough implementation detail and data availability to enter the queue. Practical next use is to expand the standard audit block with calibration metrics, anchor/liquidity-state buckets, and prediction-market structural tags when relevant.

## Hygiene Check Notes

Planned source-note titles are exact-file matches and were added to Source Index. Major wikilinks point to existing notes or notes created in this run. A final search was run after writing to verify source/index/registry/review references and root zero-byte markdown files.
