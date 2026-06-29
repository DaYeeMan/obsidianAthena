---
type: coding-ready-backtest-queue
created: 2026-06-28
last_updated: 2026-06-28
tags: [quant-research, backtest-queue, coding]
---

# Coding-Ready Backtest Queue

This queue tracks ideas that are ready or nearly ready to implement. It is separate from the broader [[01 Research Candidate Registry]] because not every useful research item should become code immediately.

## Queue

| Strategy / Spec | Asset Class | Priority | Implementation Status | Data Needed | Main Blocker | Linked Research | Next Coding Step |
|---|---|---|---|---|---|---|---|
| SPX/SPXW short-dated put-writing with VIX and fractional-Kelly sizing | Options / equities | High | Research spec needed | Historical SPX/SPXW option chains with bid/ask, SPX, VIX, rates, fees/margin assumptions | Data availability and realistic fill/margin modeling | [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] | Create fixed-risk baseline backtest spec before adding VIX/Kelly sizing. |
| Decision-aware covariance metrics for GMVP backtests | Equities / crypto / ETFs | Medium | Method integration | Daily returns for test universes; covariance estimators | Need define benchmark/oracle/regret metrics | [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]] | Add decision-regret metrics to any portfolio-construction backtest. |
| Forecast-uncertainty-aware ML sizing | Equities / crypto | Medium | Method integration | ML forecast distributions or bootstrap/ensemble predictions | Need existing ML forecast pipeline | [[2026-06-28 Daily Quant Research Review]] | Create source note and apply uncertainty shrinkage only after a baseline model exists. |

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
