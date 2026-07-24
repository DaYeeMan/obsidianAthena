---
type: daily-quant-research-review
created: 2026-07-24 0803 EDT
source_status: normal
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review, crypto, defi, volatility, microstructure]
---

# 2026-07-24 0803 Daily Quant Research Review

## Run Status

- Pre-run collector status: **normal**, with `blogwatcher-cli` available at `C:/Users/enson/.local/bin/blogwatcher-cli.EXE` and persistent DB `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Blogwatcher scan: 7 tracked feeds scanned; 6 succeeded, 1 failed. Quantocracy failed with HTTP 302. Four new feed articles were detected.
- arXiv validation: validated the high-signal feed/query leads through the arXiv API before saving. No Semantic Scholar citation lookup was used in this run.
- Quantpedia lead: `Getting the Target Right in Return Prediction` looked relevant, but direct page fetch returned HTTP 466, so it was treated as an unvalidated practitioner lead and not saved.

## Items Screened

### 1. [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]]

- Source: Weiye Xi, Ciamac C. Moallemi, “Quantifying Sub-Optimality in Routing for Automated Market Makers,” arXiv:2607.20762v1, 2026-07-22.
- Classification: **Evidence-backed at abstract level** as empirical DeFi execution-quality evidence.
- Practicality: **foundational / retail-adaptable** as a cost and execution-audit layer; not standalone alpha.
- Why saved: large-scale WETH-USDC routing audit over 2.98 million swaps; reports average routing shortfall of 2.02 bps per trade / about $24 million aggregate, with shortfall decomposed through support-constrained, full-venue, and gas-aware benchmark routes.
- Practical implication: any DEX or AMM strategy backtest should include gas, stale block-state delay, route-suboptimality, failed transactions, and sandwich/MEV exposure before trusting quoted pool prices.
- Decay/failure modes: routing APIs, aggregators, MEV protection, private relays, gas markets, and AMM designs change quickly; quoted route quality may not transfer across periods or venues.

### 2. [[Pathwise Roughness of Bitcoin Realized Volatility]]

- Source: Milan Pontiggia, “Pathwise Roughness of Bitcoin Realized Volatility: Stability Across Time, Sampling, and Volatility Measures,” arXiv:2507.00575v4, updated 2026-07-23.
- Classification: **Evidence-backed at abstract level** as volatility-measurement evidence.
- Practicality: **foundational / retail-adaptable** as a BTC volatility/risk-model feature; not a directional signal.
- Why saved: one-minute BTC/USD Bitstamp data from 2017–2024 show generally low pathwise roughness estimates below 1/2 across many windows, but root availability and magnitude vary by period, sampling frequency, truncation, and volatility measure.
- Practical implication: roughness can be considered as a lagged risk-throttle or volatility-state covariate only after EWMA/HAR/GARCH, realized-volatility, funding, drawdown, and venue-stress baselines are implemented.
- Decay/failure modes: exchange-specific data quality, window/frequency tuning, and overlap with ordinary realized-vol/jump features can create false model complexity.

### 3. Portfolio Optimization under Dynamic Rebalancing via Topological Data Analysis and News Sentiments

- Source: Divyanee Garg, arXiv:2607.21170v1, 2026-07-23.
- Classification: **Speculative / Plausible but untested** at abstract level.
- Practicality: **foundational / retail-adaptable only as a benchmark warning**; not saved as a source note today.
- Reason not promoted: the abstract claims S&P 500 outperformance from TDA clustering plus FinBERT news sentiment and frequent rolling rebalancing, but the lead lacks inspectable details here on point-in-time news availability, survivorship-free constituents, turnover/costs, sentiment timestamping, factor/sector controls, and simple baselines beyond broad comparison labels. It is worth watching only if the full paper supplies rigorous time-gated validation and realistic frictions.

### 4. Getting the Target Right in Return Prediction

- Source: Quantpedia practitioner post, 2026-07-23.
- Classification: **Unvalidated lead / watch only**.
- Practicality: potentially useful for ML target-definition discipline, but not saved because the page fetch failed with HTTP 466 and the pre-run feed snippet alone is not evidence.

## Version Maintenance

- Updated [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]] from arXiv:2607.17428v1 to v2 after arXiv validation. No classification change; still foundational / retail-adaptable, low coding priority.
- Updated [[Observable Matrix Dynamics of Stocks]] citation from arXiv:2607.19005v1 to v2. No classification change; still a correlation-geometry regime diagnostic rather than a standalone timing signal.
- Updated [[Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium]] citation from arXiv:2607.08500v1 to v2. No classification change; still option-chain-data-dependent and not coding-ready.

## Literature Connections / Framework Leads

### Reinforces

- [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]] reinforces [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]], [[Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures]], [[Risk-Based Auto-Deleveraging]], and [[Prediction-Market AMM and Market-Making Design - Uniform-Loss and Optimal Quoting]] by showing that crypto/DeFi market structure must be modeled through venue- and mechanism-specific execution losses, not generic fee assumptions.
- [[Pathwise Roughness of Bitcoin Realized Volatility]] reinforces [[Forecasting Realized Volatility with Time Series Foundation Models]], [[Regime-Conditional Distributional Comparison of Trading Strategies]], [[Risk-Based Auto-Deleveraging]], and [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]] by adding a measurement-sensitive BTC volatility-state candidate that must beat simple baselines.

### Contradicts / Weakens

- DEX routing evidence weakens naive on-chain backtests that use quoted pool state or execution-time reserves without gas, stale-state, failed-transaction, and MEV/sandwich charges.
- BTC roughness evidence weakens any claim that rough-volatility features are inherently superior; the paper itself emphasizes measurement instability and observed-vs-latent volatility limits.
- The TDA/news-sentiment portfolio lead weakens, rather than strengthens, the case for complex portfolio ML unless the full paper proves point-in-time news handling, turnover/cost realism, and simple-rule superiority.

### Framework Potential

- Microstructure-conditioned decay and liquidity-state validation: add DEX route-quality diagnostics — support-constrained/full-venue/gas-aware shortfall, stale-state delay, gas, failed transactions, sandwich/MEV flags, and trade-size buckets — to any DeFi execution audit.
- Regime-conditional distributional strategy evaluation: add BTC roughness only as an ex ante volatility-state covariate and require incremental downstream net utility over realized-volatility/funding/drawdown/venue-stress baselines.

## Registry / Queue Actions

- Candidate registry: **updated** with two new tracked candidates: DEX routing sub-optimality and BTC realized-volatility roughness. Also added corresponding decay warnings and foundational references.
- Source notes: **created** two new source notes and updated the Source Index.
- Framework registry / open questions: **updated** with two framework-update bullets and two new open questions.
- Coding-ready queue: **reviewed but unchanged**. Neither new item has the falsifiable rules, full data pipeline, cost assumptions, baselines, and go/no-go design needed for promotion. DEX routing belongs inside the standard audit block when DeFi execution is in scope; BTC roughness requires a baseline volatility-sizing experiment first.

## Hygiene Check

- New source-note titles are intentionally wikilinked and were added to `01 Sources/Source Index.md`:
  - [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]]
  - [[Pathwise Roughness of Bitcoin Realized Volatility]]
- Research Review Index updated with [[2026-07-24 0803 Daily Quant Research Review]].
- Known unresolved/concept references: none intentionally introduced as bracketed concept-only links in this review. Framework labels were kept as plain text unless an existing/source note was linked.
