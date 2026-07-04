---
type: daily-quant-research-review
date: 2026-07-02
generated_at: 2026-07-02 0801 EDT
tags: [quant-research, daily-review, arxiv, synthesis]
---

# 2026-07-02 0801 Daily Quant Research Review

## Scope and Inputs

Pre-run blogwatcher and arXiv outputs were treated as discovery leads, not evidence. I validated the highest-signal items by retrieving arXiv metadata/abstracts for:

- [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]] — arXiv:2607.00475v1.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]] — arXiv:2607.01198v1.
- “Real-time identification of the onset of financial rogue waves” — arXiv:2606.31475v1.
- Adjacent-domain method leads: “Hierarchical Variational Kalman Filtering” and “TiRex-2: Generalizing TiRex to Multivariate Data and Streaming.”

Feed note: blogwatcher-cli was available and article listing succeeded, but the scan reported a SQLite UNIQUE constraint failure for the arXiv q-fin portfolio-management feed. I used the successfully returned article list and arXiv API validation rather than treating the scan as complete evidence.

Semantic Scholar citation checks for arXiv:2607.00475 and arXiv:2607.01198 returned HTTP 429 rate-limit errors, so citation metadata was not used.

## High-Signal Items Kept

### 1. End-to-end AI portfolio policies versus simple rules

- Source note: [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]].
- Classification: **Evidence-backed at abstract level as a model-evaluation study; foundational / retail-adaptable**.
- Why kept: the paper directly asks the right question for ML allocation research: when do AI policies beat equal weight, risk parity, and time-series momentum after costs?
- Practical implication: any local AI allocation project should start with equal weight, inverse-vol/risk parity, time-series momentum, and a linear parametric policy before LSTM/transformer complexity.
- Failure modes: differentiable Sharpe objectives can overfit turnover, leverage, and tail events; futures roll/margin/cash handling can dominate; pooled gross performance can hide weak sub-asset or regime results.

### 2. Liquidity-tail-aware market impact and price discovery

- Source note: [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]].
- Classification: **Evidence-backed as theory; foundational**.
- Why kept: it strengthens the cost-modeling layer by arguing that large trades/imbalances are not always information; under heavy-tailed liquidity demand they may be liquidity shocks, with slower price discovery and persistent adverse-selection premia.
- Practical implication: backtests should not interpret volume spikes or large-order moves as automatically informed alpha, and slippage/impact stress should be state-dependent when liquidity-tail risk is high.
- Failure modes: empirical identification of informed versus uninformed flow is hard; rolling tail proxies may be noisy and regime-dependent.

## Screened but Not Promoted

### Real-time identification of financial rogue waves

- arXiv:2606.31475v1.
- Classification remains **Speculative / foundational-watch**.
- Update: today’s abstract retrieval confirms the method detects most major VIX/VXO/VSTOXX peaks using a Schrödinger/Kerr-nonlinearity analogy and eigenvalue-gradient spike, but this still needs replication versus simple VIX/EWMA/drawdown/change-point baselines before registry promotion.
- Possible future use: crisis-onset risk-control benchmark for short-vol strategies, not an alpha signal yet.

### Adjacent method leads

- “Hierarchical Variational Kalman Filtering” may be useful later for online covariance/noise tracking, but it is not finance evidence and was not saved.
- “TiRex-2” is a promising streaming multivariate time-series foundation-model lead, but it needs finance-specific leakage/cost/baseline validation before entering the library.

### Practitioner feed leads

- Alpha Architect behavioral-finance articles and older feed items did not beat the new validated arXiv items for preservation today.
- SSRN query leads remained search prompts only; no SSRN paper was saved without direct validation.

## Candidate Registry Updates

Added two candidates:

1. End-to-end AI portfolio policies versus simple rules.
2. Liquidity-tail-aware market impact and price discovery.

Also updated sorting, decay-watch, and foundational-reference sections to reflect AI-policy benchmark discipline and liquidity-tail cost stress.

## Literature Connections / Framework Leads

### Reinforces

- [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]] reinforces [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]] by demanding cost-aware policy evaluation rather than return-only AI claims.
- [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]] reinforces [[Regime-Conditional Distributional Comparison of Trading Strategies]]: model superiority should be tested across folds, regimes, and sub-asset classes.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]] reinforces [[Liquidity-Based Audit of Algorithmic Trading Strategies]] and [[Signature-Based Optimal Execution for Statistical Arbitrage]] by making liquidity state and tail risk central to cost/capacity analysis.

### Contradicts / Weakens

- Weakens blanket “AI beats rules” allocation narratives: the abstract reports non-uniform performance and cost-sensitive model rankings.
- Weakens volume-spike/large-trade signal folklore: large trades may be heavy-tailed liquidity shocks rather than private information.

### Framework Candidate Added / Updated

- Added framework row: **Simple-rule benchmark-first AI portfolio-policy evaluation**.
  - Linked notes: [[End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing]], [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]], [[Regime-Conditional Distributional Comparison of Trading Strategies]], [[Forecast-uncertainty-aware ML asset pricing]].
  - Minimum viable validation: simple allocation baselines, linear policy, walk-forward training, turnover/cost stress, uncertainty shrinkage, and regime-conditional fold distributions.
- Updated existing **Cost-aware decision-process diagnostics** framework to include the new AI policy and liquidity-tail source notes.

### Open Research Questions Added

- When do end-to-end AI portfolio policies beat equal weight, risk parity, and time-series momentum after costs, turnover caps, margin/roll assumptions, and regime validation?
- Can liquidity-tail-risk proxies improve backtest cost stress by identifying states where large trades are less informative but spreads/impact remain elevated?

## Coding Queue Decision

Reviewed [[09 Coding-Ready Backtest Queue]]. No update was made. The new AI-policy candidate is a useful benchmark design, but it is not coding-ready until a clean futures or ETF proxy universe, features, roll/cash treatment, frictions, and go/no-go thresholds are specified.

## Hygiene Check Notes

- Created two source notes and added both to [[Source Index]].
- Added this review to [[Research Review Index]].
- Used wikilinks only for created or existing source/queue/index notes. Non-promoted method leads were left as plain text.
- Blogwatcher scan error and Semantic Scholar 429 were recorded explicitly rather than papering over missing metadata.

## Next Actions

- For future ML allocation work, implement equal weight, risk parity/inverse vol, time-series momentum, and a linear parametric policy before any deep sequence model.
- Add liquidity-tail or large-order state diagnostics to the cost-aware backtest audit block.
- Keep “rogue wave” VIX detection on watch only until replicated against simpler risk-control baselines.
