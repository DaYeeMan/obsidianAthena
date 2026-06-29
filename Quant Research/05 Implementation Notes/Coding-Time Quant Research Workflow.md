---
type: coding-time-research-workflow
tags: [quant-research, coding, backtesting]
---

# Coding-Time Quant Research Workflow

Use this workflow when the user is actively coding or backtesting a strategy and asks this profile for quantitative support. The research library is not only for market-event triage.

## User Inputs to Request When Missing

Ask only for inputs that materially change the research response:

- asset class and universe
- intended holding period
- data currently available
- target backtesting framework or language
- whether the user wants literature, feature ideas, validation checks, or implementation help

## Default Response Structure

When the user brings a strategy under development, respond with:

1. **Strategy family classification**
   - factor, event, options-volatility, crypto microstructure, regime/risk allocation, ML forecast, portfolio construction, etc.
2. **Relevant literature / notes**
   - search this Obsidian library first, then external sources if needed.
3. **Hypothesis refinement**
   - turn the idea into falsifiable rules.
4. **Minimum viable backtest**
   - baseline implementation before complexity.
5. **Data requirements**
   - fields, frequency, vendor constraints, survivorship/leakage issues.
6. **Cost and frictions model**
   - commissions, spread, slippage, borrow, funding, exchange fees, option liquidity, market impact.
7. **Robustness checks**
   - walk-forward, subsamples, regimes, purged CV if ML, post-publication decay, parameter stability.
8. **Simple baselines**
   - equal weight, buy-and-hold, inverse-vol, naive momentum/reversal, fixed-risk put-write, etc.
9. **Go/no-go recommendation**
   - Evidence-backed / Plausible but untested / Speculative / Low quality / Rejected.

## Practicality Preference

Prefer research that helps the user code and test something realistic. Institutional papers should be mined for simpler proxies, warnings, or foundational methods rather than treated as direct trading candidates.
