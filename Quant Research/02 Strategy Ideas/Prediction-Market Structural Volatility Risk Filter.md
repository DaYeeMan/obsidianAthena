---
type: strategy-idea
asset_classes: [prediction-markets, crypto]
status: plausible-but-untested
practicality: retail-adaptable
last_reviewed: "2026-07-10"
tags: [strategy-idea, prediction-markets, volatility, event-contracts, risk-filter]
---

# Prediction-Market Structural Volatility Risk Filter

## Hypothesis

For binary event contracts, structural variables -- probability level, time-to-resolution, spread, volume, event category, and venue/design tags -- forecast volatility and adverse liquidity states better than generic ARCH/GARCH. A structural-volatility filter may improve event-window or settlement-window strategies by reducing exposure during high-risk/high-cost states.

## Source

- [[Volatility in Prediction Markets - A Structural Approach]]
- [[SoK - Market Microstructure for Decentralized Prediction Markets]]
- [[Settlement Manipulation in Prediction Markets]]

## Economic Rationale

Prediction-market prices are bounded probabilities that resolve to binary payoffs at known deadlines. Volatility is mechanically and informationally tied to unresolved uncertainty, event timing, order flow, spread, and resolution/settlement rules.

## Asset Class / Universe

- Kalshi event contracts if historical quote/trade data are available.
- Polymarket/DePM contracts only after venue/design metadata and on-chain/friction issues are handled.

## Signal Definition

Use an ex ante structural-volatility risk bucket:

- price/probability level,
- time to resolution,
- spread and volume,
- event category,
- venue/design/resolution tags,
- optional residual rolling/GARCH volatility.

Start as a no-trade or exposure-cap filter, not a directional predictor.

## Data Requirements

- Contract metadata and resolution deadline known at decision time.
- Historical prices, bid/ask or spread, volume, fees, and outcomes.
- Venue/design tags for decentralized markets.
- Event timestamps and settlement mechanics.

## Minimum Viable Backtest

1. Forecast next-window absolute return or variance for event contracts.
2. Compare rolling volatility, GARCH, structural-only, and structural-plus-residual models.
3. Validate by time-to-resolution and category using contract-clustered splits.
4. Apply the best risk forecast as a filter to a settlement/event-window strategy and test whether net risk-adjusted performance improves after spreads/fees.

## Transaction-Cost Concerns

- Wide spreads and low depth can dominate expected edge.
- Fill probability and adverse selection matter more than mid-price forecasts.
- On-chain venues add fees, oracle risk, indexing delays, and settlement uncertainty.

## Risks / Failure Modes

- Structural model improves forecast scores but not tradable net utility.
- Category-specific effects overfit.
- Venue design changes cause decay.
- Event timing or resolution information leaks into the feature set.

## Validation Priority

Medium if prediction-market data ingestion becomes available; not promoted to coding queue until data access and fill assumptions are specified.
