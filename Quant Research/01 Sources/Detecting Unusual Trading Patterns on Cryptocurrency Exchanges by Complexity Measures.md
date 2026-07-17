---
type: source-note
source_kind: paper
asset_classes: [crypto, market-microstructure, exchange-quality, surveillance]
implementation_class: retail-adaptable / foundational
importance: high
last_reviewed: "2026-07-16"
tags: [quant-source, crypto, market-microstructure, exchange-quality, complexity-measures, manipulation-surveillance]
concepts: [artificial-transaction-generation, exchange-specific-anomaly-detection, transaction-count-complexity, wash-trading-warning]
---

# Detecting Unusual Trading Patterns on Cryptocurrency Exchanges by Complexity Measures

## Citation / Link

Jakub Zwydak, Marcin Wątorek, Jarosław Kwapień, Stanisław Drożdż, “Detecting unusual trading patterns on cryptocurrency exchanges by means of complexity measures,” arXiv:2607.13916v1, 2026-07-15. https://arxiv.org/abs/2607.13916v1

## Summary

This paper proposes a diagnostic framework for detecting exchange-specific unusual trading patterns in high-frequency cryptocurrency trade data. It studies BTC, ETH, and XRP on Binance, Bitget, KuCoin, and Kraken from 2025-04-01 to 2025-06-30 using log returns, trading volume, and transaction counts. The abstract reports a pronounced Bitget BTC/ETH anomaly after mid-May 2025: transaction counts rose sharply without proportional increases in traded volume or return fluctuations, with weaker autocorrelation, reduced multifractal organization, higher short-pattern irregularity, and weaker cross-correlations involving transaction counts. The authors frame this as consistent with a noise-like trading component and possible artificial transaction generation, but not direct proof of wash trading.

## Core Contribution

- Adds exchange-quality and artificial-volume diagnostics beyond price-only crypto microstructure screens.
- Treats transaction count, volume, returns, entropy/complexity, multifractality, and cross-correlation structure as a joint surveillance panel.
- Supplies a practical warning that reported liquidity can become less informative when trade-splitting or artificial low-volume transactions inflate counts.
- Reinforces the need to condition crypto backtests on venue-level market-quality regimes rather than pooling exchanges blindly.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as exchange-surveillance / data-quality methodology; retail-adaptable / foundational**.
- Not a directional alpha signal by itself.
- Useful as a data-quality and execution-risk filter for crypto strategies: downweight, exclude, or stress-test venues/periods where transaction-count complexity diverges from volume and return behavior.
- Retail adaptation is feasible if trade-level or sufficiently granular aggregated trade data are available; a simplified proxy can monitor transaction-count/volume divergence, average trade size collapse, spread/depth changes, and return/volume decoupling.

## Methods and Data

Abstract-level details:

- Assets: BTC, ETH, XRP.
- Venues: Binance, Bitget, KuCoin, Kraken.
- Sample: 2025-04-01 through 2025-06-30.
- Inputs: high-frequency trade-level log returns, trading volume, and transaction counts.
- Measures: tail distributions, autocorrelation functions, multifractal characteristics, approximate entropy, and detrended cross-correlations.
- Key reported anomaly: Bitget BTC/ETH after mid-May 2025 shows many low-volume trades without commensurate volume or return-volatility increase.

## Leakage / Bias / Overfitting Concerns

- The abstract highlights one short 2025 window; results may be venue/event-specific and require longer samples.
- Exchange API changes, fee promotions, market-maker programs, or internal trade-reporting conventions could mimic manipulation-like patterns.
- Complexity metrics can be sensitive to sampling frequency, missing trades, aggregation rules, and multiple testing across venues/assets/windows.
- The paper does not prove wash trading; treat it as an anomaly detector that flags periods for exclusion or additional validation.

## Transaction Cost / Capacity Treatment

This is mainly a market-quality/cost-model input. If reported liquidity is artificially inflated by low-volume transaction bursts, naive volume-based capacity and spread/slippage assumptions may be too optimistic. Backtests using affected venue data should stress fills, maker/taker fee assumptions, adverse selection, and exchange-specific outages/quality controls.

## Strategy Ideas Extracted

- Add a crypto venue-quality audit before using exchange trade data in momentum, funding, basis, or intraday order-flow studies.
- Test whether transaction-count/volume divergence predicts future spread widening, depth deterioration, exchange-specific slippage, or reduced signal transferability.
- Use flagged anomalous windows as exclusion/stress-test regimes rather than as direct long/short signals.

## Connections to Existing Research

### Reinforces

- [[When Does Order Flow Matter - State-Dependent L2 Liquidity-State Transitions in Crypto Futures]]: exchange/venue state should be a baseline before adding order-flow features.
- [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]]: clock-phase/order-flow signals need venue-quality checks to avoid learning artificial trade-count patterns.
- [[The Extremity Premium - Sentiment Regimes and Adverse Selection in Cryptocurrency Markets]]: public-state filters should be complemented with exchange-specific liquidity-quality filters.
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]: capacity and liquidity-demand metrics are unreliable if volume/count inputs are distorted.

### Contradicts / Weakens

- Weakens naive crypto backtests that pool exchange trade counts or volume as if they were homogeneous, manipulation-free liquidity measures.

### Transfers Across Asset Classes or Domains

- Similar surveillance logic can be applied to equities/ETFs using trade-size distributions, odd-lot behavior, volume-return decoupling, and quote/trade consistency, but crypto venues are the more immediate use case.

### Missing Validation or Method Supplied

- Supplies a venue-quality diagnostic that should sit before return prediction: detect whether the input data environment is trustworthy enough to support a signal claim.

## Framework Potential

- Candidate framework: Microstructure-conditioned decay and liquidity-state validation.
- Linked notes: [[When Does Order Flow Matter - State-Dependent L2 Liquidity-State Transitions in Crypto Futures]], [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]], [[Liquidity-Based Audit of Algorithmic Trading Strategies]], [[The Extremity Premium - Sentiment Regimes and Adverse Selection in Cryptocurrency Markets]].
- Testable composite hypothesis: crypto signals conditioned on exchange-quality anomalies have lower post-cost reliability than the same signals in normal venue-quality states.
- Minimum viable validation: compute average trade size, transaction-count/volume divergence, return-volume decoupling, spread/depth proxies, and signal PnL by venue-quality bucket.
- What would falsify this connection? Venue-quality flags do not predict slippage, spread/depth deterioration, or signal degradation out of sample.

## Keep / Reject Decision

Keep as a high-value foundational/retail-adaptable crypto market-quality reference. It should not be promoted to the coding-ready queue until a concrete data source and simplified diagnostic specification are available.

## Related Notes

- [[When Does Order Flow Matter - State-Dependent L2 Liquidity-State Transitions in Crypto Futures]]
- [[The Quarter-Hour Effect - Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures]]
- [[The Extremity Premium - Sentiment Regimes and Adverse Selection in Cryptocurrency Markets]]
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]
