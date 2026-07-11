---
type: strategy-idea
asset_classes: [options, equities]
status: plausible-but-untested
practicality: retail-adaptable
last_reviewed: "2026-07-10"
tags: [strategy-idea, options, equity-premium, risk-throttle, spx]
---

# Option-Implied SDF Equity Premium Timing

## Hypothesis

Option-implied volatility-scaled stochastic discount factor features can forecast the equity premium and improve SPX allocation or SPX/SPXW short-volatility risk sizing versus simple VIX, IV-rank, skew, realized-volatility, and drawdown filters.

## Source

- [[Estimating the Stochastic Discount Factor from Option Prices and Predicting the Equity Premium]]
- Related preprocessing reference: [[Arbitrage-Free Multi-Maturity Risk-Neutral Marginals]]

## Economic Rationale

Option prices encode state prices and forward-looking risk compensation. SDF shape across moneyness and maturity may capture market-implied risk aversion or crash-risk pricing that is not summarized by a single VIX or skew number.

## Asset Class / Universe

- SPX/SPY equity index allocation.
- SPX/SPXW option-selling risk throttle after the fixed-risk baseline exists.

## Signal Definition

Use only information available at decision time:

1. Build an arbitrage-cleaned SPX option-implied distribution/SDF estimate.
2. Extract an SDF-derived equity-premium forecast or stable shape feature.
3. Bucket the signal into conservative risk-on / neutral / risk-off states.
4. Apply initially to allocation sizing or option-selling exposure caps, not trade selection.

## Data Requirements

- Historical SPX/SPXW option chains with bid/ask and quote timestamps.
- Underlying SPX/SPY prices.
- Risk-free rates and dividend assumptions.
- VIX, realized volatility, skew/term-structure proxies.
- Strict point-in-time availability fields.

## Minimum Viable Backtest

1. Monthly or weekly SPX allocation timing: benchmark against buy-and-hold, VIX filter, realized-vol filter, skew filter, and Martin-bound-style forecast if implementable.
2. Only after allocation timing is understood, test as an SPX/SPXW short-vol risk cap against the fixed-risk baseline.
3. Use walk-forward construction, out-of-sample folds, and no lookahead in option quote selection.

## Transaction-Cost Concerns

- Signal construction can be corrupted by stale/wide option quotes.
- Downstream option-selling tests need bid/worse fills, margin/cash treatment, crash gaps, and assignment/settlement assumptions.
- Allocation timing needs turnover and whipsaw costs.

## Risks / Failure Modes

- Option-implied risk-neutral features do not translate to physical expected returns.
- Forecast value concentrated in crisis windows.
- Interpolation/extrapolation dominates the signal.
- No incremental net utility after simple VIX/skew/realized-vol controls.

## Validation Priority

Medium-high after the option-chain preprocessing layer is available; not coding-ready before then.
