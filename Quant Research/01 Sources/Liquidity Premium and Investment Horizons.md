---
type: source-note
source_kind: paper
asset_classes: [equities, market-microstructure, asset-pricing]
implementation_class: retail-adaptable / foundational
importance: medium
last_reviewed: "2026-07-03"
tags: [quant-source, equities, liquidity-premium, order-flow, price-impact, asset-pricing]
concepts: [kyle-lambda, signed-order-flow, liquidity-premium, adverse-selection, fama-macbeth]
---

# Liquidity Premium and Investment Horizons

## Citation / Link

Irene Aldridge, “Liquidity Premium and Investment Horizons,” arXiv:2607.01377v1, 2026-07-01. https://arxiv.org/abs/2607.01377v1

## Summary

The paper estimates Kyle's price-impact coefficient directly from daily equity order flow and tests whether it forecasts the cross-section of subsequent stock returns. In CRSP data from 2020–2025, the abstract reports that signed order flow predicts contemporaneous and one-month-ahead returns, while volume volatility predicts lower subsequent returns. The proposed interpretation is an adverse-selection mechanism for liquidity premia: low order flow widens price impact and depresses prices today; normalization later restores prices.

## Core Contribution

- Links firm-month price-impact estimates to cross-sectional expected returns.
- Makes liquidity premium potentially testable with order-flow or order-flow proxy data rather than a broad illiquidity label.
- Connects asset-pricing returns to daily microstructure variables over a recent sample.
- Complements liquidity-demand and liquidity-tail diagnostics already in the library.

## Practical Relevance

- Classification: **Plausible but untested / retail-adaptable-foundational**.
- Direct replication likely needs signed order-flow data that may not be retail-accessible.
- Retail proxy path is possible: Amihud illiquidity, dollar volume, spread proxies, volume volatility, and lagged return/order-imbalance proxies can be tested with common equity data.
- Do not treat as an immediate alpha until the 2020–2025 sample and order-flow measurement are stress-tested across regimes and costs.

## Methods and Data

Abstract-level details:

- CRSP equities, 2020–2025,
- firm-month signed order-flow measures,
- Kyle lambda estimated by within-month price-impact regression and Amihud-style ratio,
- Fama-MacBeth regressions with Newey-West adjustment,
- one-month-ahead cross-sectional return prediction.

Local proxy design:

1. Construct monthly liquidity variables using only lagged data: Amihud illiquidity, dollar-volume volatility, spread proxies, turnover, and return-volume interaction proxies.
2. Sort liquid U.S. equities or ETFs into high/low liquidity-stress buckets.
3. Test one-month-ahead returns net of trading costs and factor controls.
4. Compare against simple value/momentum/size/quality baselines and industry-neutral versions.

## Leakage / Bias / Overfitting Concerns

- 2020–2025 is short and includes unusual pandemic/zero-rate/inflation regimes.
- Signed order-flow reconstruction can be noisy or unavailable; proxy variables may capture size, distress, or volatility rather than liquidity premium.
- Small-cap liquidity premia can be impossible to harvest after spreads, market impact, borrow constraints, and delisting treatment.
- Cross-sectional regressions need survivorship-free data and robust factor controls.

## Transaction Cost / Capacity Treatment

Liquidity-premium strategies are especially prone to looking best in hard-to-trade names. Local tests should use conservative spread/slippage penalties by liquidity bucket and cap participation. If the premium is concentrated in names with high turnover cost or poor borrow, classify it as institutional-only or rejected for implementation.

## Strategy Ideas Extracted

### Monthly liquidity-impact premium proxy

- **Hypothesis:** Lagged price-impact/liquidity-stress proxies predict one-month-ahead stock returns after standard factor controls, but only a liquid subset may be implementable.
- **Asset class / universe:** U.S. equities; possible ETF proxy universe for robustness but weaker cross-section.
- **Signal:** Monthly ranking by lagged Amihud-style impact, volume-volatility, and spread/turnover proxies.
- **Backtest design:** Monthly rebalanced long-short and long-only tilt; factor-neutral variants; size/liquidity buckets; post-cost stress.
- **Validation priority:** Low/Medium until data and cost feasibility are proven.

## Connections to Existing Research

### Reinforces

- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]: liquidity demand and price impact should be observable strategy diagnostics.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]: liquidity state changes both price discovery and impact.

### Contradicts / Weakens

- Any broad “illiquidity premium” implementation that ignores spreads, turnover, and capacity.

### Framework Potential

- Adds an asset-pricing leg to the existing liquidity-tail/cost-audit framework: liquidity states can matter for both expected returns and implementation costs.
