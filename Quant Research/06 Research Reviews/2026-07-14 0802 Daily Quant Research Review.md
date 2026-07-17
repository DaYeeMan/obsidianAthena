---
type: daily-quant-research-review
created: 2026-07-14 0802 EDT
tags: [quant-research, daily-review, arxiv, crypto, ml-validation, portfolio]
---

# 2026-07-14 0802 Daily Quant Research Review

## Run Context

- Scope: equities, options, crypto, portfolio/risk construction, market microstructure, ML validation.
- Discovery inputs: blogwatcher-cli persistent RSS state, arXiv query leads, adjacent-domain arXiv leads, existing candidate/framework registries.
- Feed health: blogwatcher-cli scanned 7 feeds; 5 succeeded. Quantocracy returned HTTP 302 and Quantpedia returned HTTP 429, so those practitioner feeds were not fully available this run. No fallback RSS scanner was used.
- Validation step: high-signal arXiv leads were validated directly through the arXiv API before notes were created. Feed entries were treated as leads only.

## High-Signal Items Saved

### 1. [[Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization]]

- Source: arXiv:2605.01176v4, updated 2026-07-13.
- Classification: **Evidence-backed at abstract level as methodology; foundational / retail-adaptable**.
- Why it matters: decision-focused portfolio optimization can inflate forecasts and churn rankings because the optimizer induces a risk/cost-adjusted ranking problem. This directly strengthens the library's cost-aware decision-process diagnostics.
- Practical implication: before using SPO or differentiable optimizer training, report forecast-scale inflation, rank turnover, weight turnover, clipping/rescaling effects, partial adjustment, and net utility after costs.
- Decay / failure mode: model gains can vanish under realistic transaction costs, leverage constraints, and partial fills; stabilizers can hide overfit if not benchmarked against simple turnover caps/no-trade bands.

### 2. [[The Extremity Premium - Sentiment Regimes and Adverse Selection in Cryptocurrency Markets]]

- Source: arXiv:2602.07018v3, updated 2026-07-11, with code/data linked in the abstract metadata.
- Classification: **Plausible-to-evidence-backed at abstract level; retail-adaptable / foundational**.
- Why it matters: extreme fear and extreme greed appear associated with wider crypto spreads; the author explicitly flags functional-form sensitivity and the difficulty of separating pure sentiment from the Fear & Greed Index's embedded volatility component.
- Practical implication: treat sentiment extremity first as a cost/liquidity/sizing filter, not directional alpha. Test it against volatility-only, drawdown, funding, and liquidity-state baselines.
- Decay / failure mode: public sentiment filters can decay after publication; daily data can miss intraday spreads, funding, and venue outages.

### 3. [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]]

- Source: arXiv:2607.08525v1, 2026-07-09.
- Classification: **Evidence-backed at abstract level as DeFi microstructure / causal-design methodology; foundational / retail-adaptable**.
- Why it matters: the paper uses Uniswap protocol-fee switch variation as a design-based event study for LP take-rate changes and finds no large short-run average active-liquidity/local-depth response at the design's resolution.
- Practical implication: AMM fee-controller simulations should not assume a fixed LP supply response without evidence; local research should separate LP supply, trader routing, LVR/adverse selection, and fee-income channels.
- Decay / failure mode: non-detection is not a precise zero; results may not transfer to trader-facing dynamic fee changes or other AMM designs.

### 4. [[Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters]]

- Source: arXiv:2607.11653v1, 2026-07-13; adjacent-domain ML/statistics lead.
- Classification: **Evidence-backed at abstract level as validation methodology; foundational / retail-adaptable**.
- Why it matters: it offers an online, non-IID, feature-aware audit of conditional quantile forecasters. This supplies a missing monitor for whether volatility/VaR/return-quantile forecasts fail in specific regimes.
- Practical implication: add feature-aware quantile calibration evidence to ML/volatility forecast validation, with auditor features fixed ex ante: volatility state, liquidity state, trend state, asset, expiry bucket, sentiment extreme, or option-skew bucket.
- Decay / failure mode: feature-aware alarms can become data-mined multiple testing unless auditor features and action rules are pre-registered.

## Screened but Not Saved as Source Notes

- Multidimensional stochastic liquidity in Kyle's model of informed trading — high-quality theory/foundational, but less immediately actionable than the AMM and crypto-liquidity state leads; keep watch-only for future execution-cost synthesis.
- Learning Predictive Ambiguity Sets for Decision-Focused Distributionally Robust Optimization — promising decision-focused DRO lead, but the headline portfolio performance claims need closer full-paper review and strong simple-baseline/cost scrutiny before saving.
- Recovering Structural Organization in Noisy Correlation Networks Using Financial Systems as a Testbed — relevant to spectral covariance/network diagnostics, but overlaps with existing random-matrix/eigenstructure notes and was not more urgent than the feature-aware forecast-audit lead.
- Depth-Efficient Quantum Topological Data Analysis for Regime-Specific Detection of Financial Stress and quantum portfolio-optimization items — downgraded for complexity and implementation practicality; no retail-practical edge without evidence versus simple volatility/drawdown/eigenstructure baselines.
- Alpha Architect intramonth momentum post — feed lead only; not saved because the run prioritized directly validated arXiv methodology and microstructure items. If revisited, require original paper details, rules, sample, costs, and post-publication decay checks.

## Literature Connections / Framework Leads

### Reinforces

- Distributional-forecast-first ML strategy evaluation now has a stronger online calibration-audit component through [[Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters]].
- Cost-aware decision-process diagnostics is strengthened by [[Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization]], because optimizer-induced rank pressure can create exactly the kind of action instability the audit block should catch.
- Microstructure-conditioned decay and liquidity-state validation is strengthened by [[The Extremity Premium - Sentiment Regimes and Adverse Selection in Cryptocurrency Markets]] and [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]]. These add public sentiment-state and protocol-design/event-study dimensions to the liquidity-state lens.

### Transfers Across Asset Classes / Domains

- Feature-aware quantile calibration can transfer from generic forecasting to volatility forecasts, tail-risk monitors, option-selling sizing, and crypto liquidity-state risk filters.
- AMM protocol-fee event-study design transfers the library's event-window rigor from prediction markets and centralized crypto microstructure into DeFi liquidity provision.
- Crypto sentiment extremity may be a retail-adaptable analog of herding/liquidity-stress state, but only as a cost/risk filter unless a fee-aware directional hypothesis survives.

### Missing Link Supplied

- The library had dependence-aware intervals and forecast uncertainty notes, but lacked an explicit online, feature-aware calibration monitor for quantile forecasts. The Bet on Features lead fills that gap.
- The library had decision-aware covariance and simple-rule AI policy frameworks, but lacked a direct warning that decision-focused training itself can inflate prediction scale and turnover. The SPO paper supplies that warning.

## Registry / System Updates

- Created 4 source notes under `01 Sources/`.
- Updated [[Source Index]] with the new source links.
- Updated [[01 Research Candidate Registry]] with 4 new tracked candidates:
  - Decision-focused portfolio optimizer stabilization.
  - Crypto sentiment-extremity liquidity premium / cost filter.
  - AMM protocol-fee causal liquidity response audit.
  - Feature-aware anytime calibration audit for quantile forecasters.
- Updated [[Framework Candidate Registry]]:
  - Added Bet on Features to Distributional-forecast-first ML strategy evaluation.
  - Added Decision-Induced Ranking to Cost-aware decision-process diagnostics.
  - Added Extremity Premium and AMM Protocol-Fee Changes to Microstructure-conditioned decay and liquidity-state validation.
- Updated [[Open Research Questions]] with sentiment-extremity liquidity filtering and feature-aware quantile calibration questions.
- Coding-ready queue reviewed but unchanged: none of today's items has full rules, data, costs, and go/no-go criteria ready for implementation.

## Validation Priority

1. Highest coding-support value: add decision-focused optimizer turnover/score-scale diagnostics to the standard backtest audit block.
2. Strongest retail-adaptable research lead: test crypto sentiment-extreme states as a spread/slippage/sizing filter, not alpha, against volatility-only and funding/liquidity baselines.
3. Strongest framework lead: feature-aware anytime quantile calibration for volatility/tail-risk forecast monitors.
4. DeFi lead: preserve AMM protocol-fee causal design as a template for future on-chain event studies.

## Hygiene Notes

- New note titles were kept consistent with wikilinks in this review, source index, candidate registry, and framework registry.
- No source note was created for watch-only or rejected items.
- Framework labels without standalone notes were kept as plain text where possible.
