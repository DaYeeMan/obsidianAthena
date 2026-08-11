---
type: coding-ready-backtest-queue
created: 2026-06-28
last_updated: 2026-08-09
tags: [quant-research, backtest-queue, coding]
---

# Coding-Ready Backtest Queue

This queue tracks ideas that are ready or nearly ready to implement. It is separate from the broader [[01 Research Candidate Registry]] because not every useful research item should become code immediately.

## Queue

| Strategy / Spec | Asset Class | Priority | Implementation Status | Data Needed | Main Blocker | Linked Research | Next Coding Step |
|---|---|---|---|---|---|---|---|
| SPX/SPXW short-dated put-writing with VIX and fractional-Kelly sizing | Options / equities | High | Research spec needed / data blocked | Historical SPX/SPXW option chains with bid/ask, SPX, VIX, rates, fees/margin assumptions | Data availability and realistic fill/margin modeling, especially in the 0DTE era | [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]]; [[2026-07-12 Weekly Quant Synthesis and Strategy Decay Review]]; [[2026-08-02 Weekly Quant Synthesis and Strategy Decay Review]]; [[2026-08-09 Weekly Quant Synthesis and Strategy Decay Review]] | Create fixed-risk baseline backtest spec with bid/worse fills, margin/cash, expiration buckets, crash regimes, and audit-block outputs before adding VIX/Kelly, option-implied SDF, risk-neutral-tail, conformal, or specialist-volatility routing. |
| Decision-aware covariance metrics for GMVP backtests | Equities / crypto / ETFs | Medium | Method integration | Daily returns for test universes; covariance estimators | Need define benchmark/oracle/regret metrics | [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]] | Add decision-regret metrics to any portfolio-construction backtest. |
| Forecast-uncertainty-aware ML sizing | Equities / crypto | Medium | Method integration | ML forecast distributions or bootstrap/ensemble predictions | Need existing ML forecast pipeline | [[Forecast-uncertainty-aware ML asset pricing]] | Apply uncertainty shrinkage only after a baseline model exists; compare against volatility targeting, inverse-vol, and linear baselines. |
| Standard cost/regime/liquidity/decision audit block for backtests | Equities / options / crypto / futures / portfolio | High | Ready to code as reusable report module / immediate implementation target | Backtest trades/weights, asset prices/returns, turnover, spread or liquidity proxies, fold metrics, baseline returns, regime covariates, availability/reference/decision timestamps where available, rejected/excluded candidate pools where available | Integrate into a backtest harness and define minimal proxy defaults when bid/ask, intraday data, rejected-pool labels, option-chain quote diagnostics, local-calibration states, target-regime GOF variables, manipulation-like state labels, or pre-event paths are unavailable | [[2026-07-05 Weekly Quant Synthesis and Strategy Decay Review]]; [[2026-07-12 Weekly Quant Synthesis and Strategy Decay Review]]; [[2026-07-19 Weekly Quant Synthesis and Strategy Decay Review]]; [[2026-07-26 Weekly Quant Synthesis and Strategy Decay Review]]; [[2026-08-02 Weekly Quant Synthesis and Strategy Decay Review]]; [[2026-08-09 Weekly Quant Synthesis and Strategy Decay Review]]; [[Framework Candidate Registry]] | Implement a report block with TimeGate/leakage checklist, planted-leak controls where possible, survivorship/replication guardrails, base-rate/always-up and simple-rule baselines, deployment gates, turnover/cost stress, liquidity-demand/tail and venue-quality proxies, manipulation-like RL/execution and pump-reversal/velocity diagnostics, AutoQuant-lite execution/funding/accounting invariants, action-attribution for risk filters, PSI/JSD/KL drift false-alarm/power checks, local/feature-aware calibration, target-regime covariate-shift GOF, dependence-aware interval/fold uncertainty, regime-conditioned fold metrics, decision-regret outputs, excluded-pool coverage audits, pre-treatment path reference tests for event studies, option-code invariant tests, option-density identifiability checks, non-Gaussian drawdown/recovery stress, boundary/margin survival metrics, passive-fill realism, and dynamic venue-fee/fill stress. |

## Status Definitions

- **Research spec needed**: candidate is promising but needs a formal backtest spec.
- **Data blocked**: implementation depends mainly on data access.
- **Ready to code**: rules, data, costs, and validation plan are clear enough to implement.
- **In progress**: coding/backtest work has begun.
- **Done / rejected**: implemented and accepted, revised, or rejected.

## Promotion Rule

Promote a candidate from the registry into this queue only when it has:

1. a falsifiable hypothesis,
2. a defined universe,
3. known data requirements,
4. realistic cost/friction assumptions,
5. baseline comparisons,
6. validation design,
7. a clear go/no-go decision rule.
