---
type: strategy-idea
status: Plausible but untested
asset_classes: [options, equities]
universe: "SPX/SPXW index options, 0-5 DTE"
implementation_class: retail-adaptable
validation_priority: High
last_reviewed: "2026-06-28"
tags: [quant-research, options, volatility-risk-premium, put-writing, position-sizing]
---

# SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing

## Classification

- Status: Plausible but untested
- Implementation class: retail-adaptable
- Asset class: options / equities
- Validation priority: High

## Hypothesis

A systematic short SPX/SPXW put strategy can improve risk-adjusted performance and reduce crash exposure when position size is scaled by volatility regime and conservative fractional-Kelly estimates, compared with fixed notional or fixed margin allocation.

## Source / Evidence

Primary source: [[Sizing the Risk - Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options]]

Underlying mechanism: equity-index implied volatility typically exceeds subsequent realized volatility, creating a volatility risk premium. The edge is compensation for bearing crash and liquidity risk, not free alpha.

## Economic Rationale

Put sellers earn insurance premia from investors hedging downside risk. Expected returns can be positive over long samples but are negatively skewed and crash-sensitive. Sizing rules may matter more than entry rules because ruin risk is dominated by rare volatility spikes.

## Signal Definition

Candidate design variants to test:

1. Sell OTM SPX/SPXW put at target delta or moneyness.
2. Expiration buckets: 0DTE, 1DTE, 2–5DTE, weekly; evaluate separately.
3. Position sizing:
   - fixed notional,
   - fixed margin utilization,
   - VIX regime scaler,
   - fractional Kelly estimated only from prior rolling window,
   - hybrid VIX cap + fractional Kelly.
4. Exit/settlement:
   - hold to cash settlement,
   - intraday stop/roll variants only if intraday data are available.

## Universe

- SPX/SPXW index options.
- Use liquid strikes only; minimum volume/open-interest filters.
- Avoid single-name options for first replication because early exercise, assignment, and idiosyncratic gap risks complicate interpretation.

## Data Requirements

- Historical SPX/SPXW option chains with bid/ask, volume, open interest, expiration, strike, and greeks if available.
- SPX index levels.
- VIX.
- Risk-free rates.
- Commission/fee schedule.
- Margin/cash assumptions.
- Intraday bars if testing 0DTE stops or intraday exits.

## Backtest Design

- Walk-forward sizing: estimate Kelly inputs only from prior data.
- Compare regimes: 2018 vol shock, 2020 COVID crash, 2022 bear market, 2023–2026 0DTE market-structure era.
- Report total return, CAGR, Sharpe, Sortino, max drawdown, expected shortfall, skew/kurtosis, worst day/week, margin utilization, and probability of margin breach.
- Compare against simple baselines: buy-and-hold SPY, fixed-notional put-write, CBOE PUT/BXM-style indices if available.

## Portfolio Construction

- Start with a single-risk-sleeve allocation cap.
- Use hard notional/margin limits regardless of Kelly output.
- Consider volatility targeting only if it does not mechanically increase exposure before volatility spikes.

## Transaction-Cost / Slippage / Liquidity Concerns

This is the make-or-break section:

- fill short option sales at bid or worse, not midpoint,
- include commissions and exchange fees,
- model wider spreads during stress,
- handle cash settlement and expiration mechanics,
- include margin/cash drag,
- cap size by quoted liquidity.

## Risks and Failure Modes

- Short convexity / crash losses.
- Kelly overestimation from non-stationary returns.
- Volatility regime changes after 0DTE adoption.
- Tail events absent from short calibration samples.
- Backtest overstated by midpoint fills or stale quotes.
- Strategy crowding compresses premium and worsens exits.

## Outdatedness / Decay Check

- VRP is persistent but not stable; crowded option-selling strategies can decay or become more tail-heavy.
- 0DTE market structure may invalidate older short-dated option samples.
- Treat any high Sharpe as suspect unless robust to recent years and conservative execution.
- Simpler benchmark: fixed-risk put-write after costs. Hybrid sizing must beat this with lower tail risk, not just higher leverage.

## Next Validation Steps

1. Acquire option-chain data with bid/ask.
2. Implement fixed-notional baseline.
3. Add VIX scaler and rolling fractional-Kelly sizing.
4. Run strict walk-forward test and regime splits.
5. Stress test 1987/2020-style synthetic gaps and margin constraints.

## Links

- [[Sizing the Risk - Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options]]
- [[2026-06-28 Daily Quant Research Review]]
