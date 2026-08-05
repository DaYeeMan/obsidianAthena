---
type: source-note
source_kind: paper / drawdown-risk simulation methodology
asset_classes: [portfolio, equities, options, crypto, risk-management]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-08-04"
tags: [quant-source, drawdown-risk, monte-carlo, heavy-tails, long-memory, risk-management]
concepts: [drawdown-stress-tables, non-gaussian-risk, long-memory-scaling, sharpe-estimation-uncertainty]
---

# Drawdown Risk Beyond Brownian Motion - Non-Gaussian and Long-Memory Stress Tables

## Citation / Link

Francesco Landolfi, “Drawdown Risk Beyond Brownian Motion: A Monte-Carlo Framework, Non-Gaussian Extensions, and Long Memory,” arXiv:2608.00127v1, submitted 2026-07-31. https://arxiv.org/abs/2608.00127v1

Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper extends the Rej, Seager, and Bouchaud drawdown framework from Gaussian closed-form intuition into transparent Monte Carlo stress tables. It maps strategy Sharpe and return structure to maximum drawdown, maximum loss, final negative time, and longest recovery time, then varies skewness, fat tails, volatility clustering, Sharpe-estimation uncertainty, and fractional-Brownian long memory. The abstract stresses that a single Gaussian drawdown table can mis-warn because drawdown depth, loss, and recovery duration respond differently to non-Gaussian features.

For this library, this is a foundational risk-reporting upgrade for backtests, especially for short-volatility, leveraged crypto, and ML allocation strategies where Gaussian Sharpe-based comfort is dangerous.

## Core Contribution

- Recasts drawdown-risk benchmarks as reproducible Monte Carlo lookup tables.
- Separates multiple drawdown pain metrics rather than using maximum drawdown alone.
- Shows skew, fat tails, volatility clustering, and Sharpe uncertainty affect metrics differently.
- Frames long-memory drawdown amplification as a square-root-of-time calibration failure in maximum-drawdown depth.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as risk methodology; foundational / retail-adaptable**.
- Retail adaptation is straightforward: add non-Gaussian drawdown stress tables to strategy reports using only strategy return series and simulated return processes.
- The paper is not an alpha source; it is a go/no-go and sizing/communication tool.

## Backtest Translation

- Hypothesis: many apparently acceptable strategy Sharpes imply intolerable drawdown/recovery distributions once skew, fat tails, volatility clustering, and Sharpe uncertainty are simulated.
- Apply to: SPX/SPXW put-writing, crypto trend/carry/leverage, ML allocation, and anomaly portfolios.
- Inputs: net strategy returns, estimated Sharpe/volatility, skew/kurtosis, volatility-clustering proxy, block/bootstrap or parametric simulation assumptions.
- Outputs: max drawdown, max loss, longest recovery, final negative time, breach probability for drawdown/margin/capital boundaries.
- Baselines: Gaussian IID lookup, historical block bootstrap, t/GARCH-style stress, fractional-Brownian scaling scenarios.

## Risks / Failure Modes

- Simulation choices can create false precision; present as stress scenarios, not forecasts.
- Tail estimates are unstable in short samples; use conservative uncertainty bands.
- Long-memory parameter estimation can be noisy; compare against simpler block-bootstrap and volatility-clustering baselines.

## Connections to Existing Research

- Strengthens the standard cost/regime/liquidity/decision audit block in [[09 Coding-Ready Backtest Queue]].
- Complements [[Boundary-Induced Apparent Risk Aversion in Multiplicative Growth]] by mapping continuation-boundary breach probabilities to drawdown and recovery-time distributions.
- Reinforces volatility/risk-control candidates such as [[Long-Memory GARCH via Two-Dimensional Markov State]] without promoting a new signal.
