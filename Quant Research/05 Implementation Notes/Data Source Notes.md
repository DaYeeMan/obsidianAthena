---
type: data-source-notes
tags: [quant-research, data, equities, options, crypto]
---

# Data Source Notes

This note tracks data requirements, likely vendors/sources, and known traps for equities, options, and crypto research.

## Equities

### Required fields by strategy type

- Daily bars: adjusted OHLCV, corporate actions, delisting handling.
- Fundamentals/factors: point-in-time fields, reporting dates, restatement handling.
- Events: announcement timestamps, after-hours vs regular-session alignment.
- Shorting: borrow availability and borrow cost if short books are tested.

### Common traps

- survivorship bias from current-index membership
- lookahead from adjusted fundamentals or revised datasets
- using announcement dates without timestamps
- ignoring delisting returns
- unrealistic market-on-close or next-open fills for illiquid names

## Options

### Required fields

- option chain history with bid/ask, strike, expiry, call/put, volume, open interest
- underlying price and corporate-action handling
- implied volatility and greeks, or enough fields to compute them
- risk-free rate/dividend assumptions
- settlement/exercise/assignment rules
- commissions, exchange fees, and margin/cash assumptions

### Common traps

- midpoint fills that are not executable
- stale quotes
- missing delisted/expired contracts
- ignoring early exercise for American single-name options
- treating 0DTE intraday risk with daily data
- not widening spreads during volatility stress
- ignoring capacity and quoted size

## Crypto

### Required fields

- exchange-specific OHLCV/trades/order book when possible
- funding rates, open interest, borrow/funding costs for perps/margin
- fee tier, maker/taker assumptions, rebates if relevant
- delisting and symbol-mapping history
- stablecoin/depeg and exchange-outage events

### Common traps

- cross-exchange timestamp alignment
- survivorship bias from currently listed coins
- inflated returns from illiquid tokens
- ignoring maker/taker fees and funding
- overfitting to exchange-specific microstructure
- lookahead from using final daily candles before live availability

## Practical Priority

For retail-implementable research, prefer candidates that can be tested with affordable data first. Institutional-only datasets can still be useful as foundational references or for designing conservative proxies.
