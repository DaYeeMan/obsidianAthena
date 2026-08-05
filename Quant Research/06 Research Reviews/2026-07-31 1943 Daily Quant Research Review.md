---
type: daily-quant-research-review
date: 2026-07-31 1943
source_status: normal-with-partial-feed-failure
created: 2026-07-31
tags: [quant-research, daily-review]
---

# 2026-07-31 1943 Daily Quant Research Review

## Run Status

- Primary feed collector used `blogwatcher-cli` persistent state. Scan succeeded for 6 of 7 feeds and found 15 new articles.
- Quantocracy feed failed with HTTP 302 during the scan, so practitioner coverage is partial. The stdlib fallback RSS scanner was not used.
- arXiv leads were directly validated through the arXiv API before source notes were written.
- Semantic Scholar was rate-limited for most selected arXiv IDs; citation metadata is recorded only where a lookup succeeded.

## High-Signal Items Saved

### 1. [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]]

- Source: Aditya Dutta, arXiv:2607.28577v1.
- Classification: **Evidence-backed at abstract level as ML deployment methodology; foundational / retail-adaptable**.
- Why it matters: Shadow Before Swap (SBS) evaluates challenger and incumbent crypto forecasts on the same forward delayed-label week and promotes only if the challenger clears a paired NLL advantage. This is a practical antidote to calendar retraining and always-promote model churn.
- Decay/friction concerns: forecast-loss gains may not improve post-cost utility; Binance-only replay, threshold tuning, and pipeline leakage can still produce false promotion decisions.
- Validation priority: implement as a model-governance block only after a local crypto ML forecast exists; require NLL/calibration plus downstream net utility, turnover, fees, funding, and drawdown.

### 2. [[Optimal Execution with Passive Market Impact]]

- Source: Alexander Barzykin, Robert Boyce, Eyal Neuman, Sturmius Tuschmann, arXiv:2607.28323v1.
- Classification: **Evidence-backed at abstract level as execution-cost methodology; foundational / institutional-only as written / retail-adaptable as stress model**.
- Why it matters: passive limit orders are not free alpha. Fill probability decays with quote distance, while adverse selection and opportunity cost create a real trade-off between aggressive quoting and non-execution risk.
- Decay/friction concerns: venue-specific queue, rebate, latency, volatility, spread, and order-flow states dominate calibration.
- Validation priority: add passive-fill stress to short-horizon/stat-arb backtests: fill probability, adverse selection, non-fill opportunity cost, and sensitivity to quote distance/liquidity state.

### 3. [[Can Large Language Models Execute Parent Orders]]

- Source: Zane Shen et al., arXiv:2607.28410v1.
- Classification: **Plausible-to-evidence-backed at abstract level as execution-agent benchmark; foundational / institutional-only as written**.
- Why it matters: useful as a benchmark discipline for AI execution agents, not as retail alpha. Reported PACE improvement over TWAP/Almgren-Chriss/learning baselines is only 0.65 bps, so fill/cost assumptions are decisive.
- Decay/friction concerns: Level-1 data, prompt contamination, queue/fill realism, latency, market transfer, and fee/rebate assumptions can erase small bps gains.
- Validation priority: any LLM execution agent must beat TWAP/VWAP/arrival-price/AC and transparent learned baselines under identical fills, costs, latency, and impact assumptions.

### 4. [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]]

- Source: Maksym Nechepurenko, arXiv:2605.11640v2.
- Classification: **Evidence-backed at abstract level as public-record identification warning; foundational / retail-adaptable with public records**.
- Why it matters: the revision corrects the sample to a 2.285-day legacy-CTF-only Polymarket block range and makes maker/taker/mint/burn attribution limits explicit. Public fills do not automatically identify invariant buyer/seller or informed-flow behavior.
- Decay/friction concerns: short subsystem-specific sample, missing negative-risk markets, representation-dependent clustering, and side-attribution ambiguity.
- Validation priority: future Polymarket settlement/manipulation studies must log subsystem, block window, contract coverage, side convention, maker/taker treatment, and attribution-sensitivity panels.

## Version / Existing-Note Maintenance

- Updated [[Observable Matrix Dynamics of Stocks]] with a follow-up note on “Are Three Matrices All You Need To Beat the Market?” arXiv:2607.27461v1.
- Classification remains conservative: the new OMD portfolio claim is a **Plausible but untested / foundational-retail-adaptable method lead**, not coding-ready alpha.
- Required before any implementation: point-in-time S&P 500 membership, delisting controls, cost sensitivity beyond 5 bps, borrow/shorting feasibility, turnover/capacity, sector/factor attribution, and simple momentum/low-vol/risk-parity baselines.

## Screened but Not Saved as Source Notes

- FinSMART, arXiv:2607.28127v1: **Speculative / low-priority** for now. Market-aligned RL sentiment claims include a 220% cumulative-return improvement, but the abstract does not provide enough leakage controls, cost details, timestamped text/data availability, or simple tabular/sentiment baselines to preserve it as a source note.
- Optimal Dynamic Fees in Automated Market Makers, arXiv:2506.02869v3: useful theory lead, but not prioritized today because the existing prediction-market/AMM framework already has several market-design notes and this update did not supply a near-term retail backtest path.
- No Trading Strategy Can Win on Every Price Path, arXiv:2604.13334v2: foundational philosophical/computability reminder, but it does not add an implementation gate beyond the existing base-rate/no-universal-strategy discipline.

## Literature Connections / Framework Leads

### Reinforces

- Cost-aware decision-process diagnostics: [[Optimal Execution with Passive Market Impact]] and [[Can Large Language Models Execute Parent Orders]] push execution evaluation beyond return-only models into fill/cost/action-trail accounting.
- Microstructure-conditioned decay and liquidity-state validation: passive fills and order-flow adverse selection are concrete ways small short-horizon edges decay after realistic execution.
- ML deployment/time-gated validation: [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]] connects [[FinBench - Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting]], [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]], and crypto model-decay monitoring.
- Prediction-market data-quality framework: [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]] strengthens the identification side of [[OpenMarket Synchronized Polymarket-Binance Dataset]] and [[Settlement Manipulation in Prediction Markets]].

### Contradicts / Weakens

- Weakens optimistic passive-limit-order and maker-rebate backtests that assume favorable fills without adverse selection or non-fill costs.
- Weakens LLM/AI trading-agent demos that report return or bps improvements without transparent execution baselines and fill realism.
- Weakens public-chain/prediction-market behavioral claims that infer buyer/seller intent from public fills without side-convention sensitivity.

### Framework Potential

- Candidate framework strengthened: cost-aware model deployment and execution-governance gates.
- Testable composite hypothesis: many apparent improvements from retrained models, passive fills, and AI execution agents vanish unless incumbent/challenger gates, passive-fill stress, and simple execution baselines are enforced.
- Minimum viable backtest/report addition: in the standard audit block, add fields for model-promotion policy, passive-fill assumptions, execution baseline family, and public-record attribution scope.
- What would falsify it: the added gates do not change model/strategy rankings or net utility versus existing spread/slippage and validation checks.

## Registry / Queue Updates

- Candidate registry updated with four tracked candidates:
  - Forward-gated crypto ML model replacement.
  - Passive-limit-order execution realism.
  - LLM parent-order execution-agent benchmark.
  - Public Polymarket fill-side attribution limits.
- Framework registry updated with 2026-07-31 framework-lead entries.
- Open questions updated with three new questions on forward-gated model replacement, passive-fill realism, and public prediction-market attribution.
- Coding-ready queue reviewed and unchanged: none of today’s items has complete data, rules, costs, baselines, and go/no-go criteria sufficient for promotion.

## Hygiene Check Notes

- New source notes were created under `01 Sources/` only; no root-level source notes were intentionally created.
- Source Index was updated for all four new source notes.
- Research Review Index was updated with this timestamped review note.
- Major wikilinks in this review point to existing notes or notes created in this run.
