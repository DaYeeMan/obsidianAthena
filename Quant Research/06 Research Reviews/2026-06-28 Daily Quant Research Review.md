---
type: daily-quant-research-review
date: "2026-06-28"
profile: quant-researcher
asset_focus: [equities, options, crypto]
tags: [daily-quant-review, arxiv, options, crypto, portfolio-construction, market-microstructure]
---

# Daily Quant Research Review — 2026-06-28

## Executive Summary

Screened recent arXiv/q-fin, ML-finance, crypto microstructure, and options-volatility candidates. Blogwatcher produced no unread/high-signal items in this cron run, so today's additions are paper-driven.

High-priority actionable lead: a 2025 paper on systematic SPX/SPXW 0–5 DTE put-writing position sizing is testable with retail-accessible index-option data, but should be treated as **Plausible but untested** until independently replicated with realistic bid/ask fills, assignment/cash-margin treatment, and tail-risk controls.

Two important research-design items were preserved: decision-aware covariance evaluation for GMVP portfolios and forecast-uncertainty-aware ML asset pricing. These are more useful for improving backtest/model design than as standalone alpha signals.

## New Research Candidates

| Candidate | Asset Class | Status | Practicality | Priority | Notes |
|---|---|---|---|---|---|
| [[Sizing the Risk - Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options]] | Options / SPX | Plausible but untested | retail-adaptable | High | Clear systematic strategy family: SPXW 0–5 DTE put-writing, Kelly/VIX/hybrid sizing. Needs replication with option spreads, margin, tail risk, and survivorship-free option-chain data. |
| [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]] | Portfolio/risk | Evidence-backed as methodology; not direct alpha | foundational | High | Strong modeling implication: evaluate covariance estimators by portfolio decision regret, not matrix norm. Useful for equity/crypto portfolio construction. |
| Forecast-uncertainty-aware ML asset pricing (Liao, Ma, Neuhierl, Schilling; arXiv:2503.00549) | Equities / ML | Evidence-backed as methodology | foundational / retail-adaptable | Medium | Use forecast confidence intervals or bootstrap uncertainty to shrink/size ML alpha forecasts. Practical guardrail against overconfident return forecasts. |
| CryptoGAT: Are Time Series Models Effective for Cryptocurrency Forecasting? (arXiv:2606.27670v1) | Crypto / ML | Plausible but untested as a warning/null result | retail-adaptable | Medium | Valuable if it shows pure price-based LSTM/GRU/Transformer crypto forecasting is weak. Use as baseline/decay warning before adding complex sequence models. |
| Empirical Confirmation of the Square-Root Law of Market Impact in a U.S. Large-Cap Equity (arXiv:2606.24019v1) | Equities / microstructure | Evidence-backed as execution-cost reference | institutional-only / foundational | Medium | AAPL ITCH-level metaorder reconstruction. Useful for slippage/capacity modeling, not retail alpha. |
| Time-dependent weighted directed networks of cryptocurrency interaction from high-frequency returns (arXiv:2606.25466v1) | Crypto | Speculative | retail-adaptable if using exchange OHLCV; institutional-only if true high-frequency | Low/Medium | Potential lead-lag/network feature idea, but Granger networks on high-frequency returns are fragile under multiple testing, exchange latency, and fee drag. |

## Evidence-Backed / High-Priority Items

### 1) Decision-aware covariance estimation for GMVP portfolios

- **Source:** Xavier Fonseca, “The Decision Geometry of Covariance Estimation for the Global Minimum-Variance Portfolio under Heavy Tails,” arXiv:2606.27462v1, 2026-06-25. https://arxiv.org/abs/2606.27462v1
- **Classification:** Evidence-backed as portfolio-methodology; **foundational**.
- **Core idea:** Covariance estimators should be evaluated by the downstream decision they support: GMVP regret. Matrix-norm error can penalize irrelevant covariance errors while missing errors that materially affect portfolio weights.
- **Practical use:** Add decision-regret metrics to covariance-model backtests:
  - realized variance of estimated-GMVP minus oracle/benchmark GMVP,
  - weight concentration / turnover,
  - stability under heavy tails,
  - shrinkage baseline comparison.
- **Retail practicality:** retail-adaptable for daily equity/ETF/crypto universes using public bars; foundational rather than direct alpha.
- **Decay/outdatedness:** durable methodological point; not an anomaly likely to decay. Risk is that exact theory may not improve net performance after turnover unless paired with cost-aware optimization.

### 2) SPX/SPXW short-dated put-writing sizing

- **Source:** Maciej Wysocki, “Sizing the Risk: Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options,” arXiv:2508.16598v1, 2025-08-09. https://arxiv.org/abs/2508.16598v1
- **Semantic Scholar check:** 0 citations / 50 references at retrieval; venue metadata returned as Knowledge-Based Systems but should be manually verified because arXiv/S2 venue matching can be noisy.
- **Classification:** Plausible but untested; **retail-adaptable**.
- **Hypothesis:** VIX-regime or conservative fractional-Kelly sizing may improve risk-adjusted returns of systematic short put exposure versus fixed notional sizing.
- **Why actionable:** Rules can be converted into a backtest quickly if option-chain data are available.
- **Key implementation concerns:** 0–5 DTE options are spread/slippage/tail-risk dominated. Realistic backtest must use bid/ask, no midpoint fantasy fills, margin/cash drag, crash-day gap risk, and position limits.
- **Decay/outdatedness:** volatility risk premium is persistent but heavily crowded; short-dated option selling after the 0DTE boom may have materially different participant mix and intraday risk than older samples.

## Plausible but Untested Items

### 3) CryptoGAT / skepticism about pure price-based crypto sequence models

- **Source:** Yu Peng, Matloob Khushi, Josiah Poon, “CryptoGAT: Are Time Series Models Effective for Cryptocurrency Forecasting?” arXiv:2606.27670v1, 2026-06-26. https://arxiv.org/abs/2606.27670v1
- **Classification:** Plausible but untested; **retail-adaptable** as a model-selection warning.
- **Potential value:** If the paper provides strong baselines and temporal validation, it can help prevent wasted effort on complex LSTM/GRU/Transformer crypto price-only models.
- **Research implication:** Before testing GAT/Transformer crypto models, require baselines: naive return=0, moving-average momentum/reversal, volatility-scaled momentum, funding/basis/open-interest features, and transaction-cost-aware cross-sectional ranking.
- **Decay/outdatedness:** crypto market structure changes quickly; price-only models trained on 2018–2022/2025 windows may fail across exchange regimes, token listings, stablecoin crises, and fee tiers.

### 4) Crypto Granger-causality interaction networks

- **Source:** Shubhangam Shukla, Mahesh Peyyala, Abhijit Chakraborty, “Time-dependent weighted directed networks of cryptocurrency interaction from high-frequency returns,” arXiv:2606.25466v1, 2026-06-24. https://arxiv.org/abs/2606.25466v1
- **Classification:** Speculative; **retail-adaptable** only at slower horizons.
- **Hypothesis:** Leadership/centrality in statistically significant crypto return-interaction networks may predict short-horizon cross-sectional returns or risk contagion.
- **Main concern:** Granger networks over many coins are multiple-testing machines. Any tradable signal must survive false-discovery controls, purged walk-forward validation, exchange-specific latency/fee modeling, and delisting/liquidity filters.

## Rejected / Low-Quality Items

No day-trading/guru content was included. Some recent arXiv items were screened out because they were either macro/remittance forecasting, fraud detection, ESG optimization, or derivative-pricing mathematics with limited immediate relevance to equities/options/crypto systematic strategy research.

## Outdatedness / Model-Decay Watch

- **Pure price-only deep learning for crypto forecasting:** Treat as an outdated-watch candidate unless it beats simple momentum/reversal/volatility/funding/basis baselines after fees. Complex sequence models often look good in leaky or costless validation and deteriorate after exchange fees and regime shifts.
- **Short-dated option selling:** Persistent risk premium, but crowded and crash-sensitive. 0DTE market structure changed the realized path risk; historical VRP evidence should not be assumed stable without recent sample splits.
- **Microstructure alpha from Granger/lead-lag networks:** Likely decays fastest where latency, maker/taker fees, and adverse selection dominate. Slow retail proxies should be tested separately from high-frequency claims.

## Foundational Items to Preserve

- **Square-root market impact:** Aniket Vasaikar, “Empirical Confirmation of the Square-Root Law of Market Impact in a U.S. Large-Cap Equity,” arXiv:2606.24019v1, 2026-06-22. https://arxiv.org/abs/2606.24019v1
  - Use as a slippage/capacity reference, not as alpha. Retail implementation can approximate impact with square-root participation penalties when scaling strategies.
- **Forecast uncertainty in ML asset pricing:** Yuan Liao, Xinjie Ma, Andreas Neuhierl, Linda Schilling, “The Uncertainty of Machine Learning Predictions in Asset Pricing,” arXiv:2503.00549v1, 2025-03-01. https://arxiv.org/abs/2503.00549v1
  - Use confidence intervals/bootstrap uncertainty to shrink forecasts and avoid overweighting noisy ML predictions. Especially relevant when converting model scores into portfolio weights.

## Strategy Notes Created or Updated

- Created [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]]
- Created [[Sizing the Risk - Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options]]
- Created [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]]

## Backtest Specs Suggested

### A) SPX/SPXW short put-writing sizing replication

- **Universe:** SPX/SPXW liquid OTM puts, 0–5 DTE; compare 1D, 2D, weekly and 0DTE variants separately.
- **Signal/rules:** Sell cash-secured or margin-constrained OTM put by delta/moneyness; size via fixed notional, VIX scaler, fractional Kelly, and VIX+Kelly hybrid.
- **Data:** Full option chain with bid/ask/greeks/volume/open interest, SPX levels, VIX, risk-free rates; ideally minute data for 0DTE exits, otherwise avoid claiming intraday realism.
- **Costs:** Enter at bid or conservative bid/ask model; include commissions, exchange fees, slippage, margin/cash drag, exercise/settlement handling.
- **Validation:** Walk-forward; 2018 vol event, 2020 crash, 2022 bear, 2023–2026 0DTE era as separate regimes. Report max drawdown, expected shortfall, crash-day losses, turnover, margin utilization.

### B) Decision-aware covariance backtest

- **Universe:** liquid sector ETFs, top equities, and/or crypto majors.
- **Models:** sample covariance, Ledoit-Wolf shrinkage, EWMA, robust/heavy-tail covariance, factor covariance.
- **Evaluation:** realized out-of-sample GMVP variance, turnover-adjusted returns, concentration, regret versus benchmark covariance, and sensitivity to estimation window.
- **Baseline:** equal-weight and inverse-volatility portfolios.

## Discord Notification Candidate?

Yes. Notify because the SPX short-dated put-writing sizing paper is actionable and because the covariance-decision item improves the library's future portfolio/backtest design standards.
