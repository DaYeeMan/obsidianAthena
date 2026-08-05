---
type: source-note
source_kind: paper / market-microstructure noise and roughness diagnostics
asset_classes: [equities, market-microstructure, execution, volatility]
implementation_class: foundational / retail-adaptable as diagnostic if tick data are available
importance: medium
last_reviewed: "2026-08-03"
tags: [quant-source, market-microstructure, rough-noise, tick-data, short-run-reversal]
concepts: [rough-microstructure-noise, fleeting-price-changes, tick-data-gmm, reversal-days]
---

# Microstructural Foundations of Rough Noise

## Citation / Link

Peter Korsbakke Christensen, Anders Midtgaard Norlyk, “Microstructural Foundations of Rough Noise,” arXiv:2607.29442v1, submitted 2026-07-31. https://arxiv.org/abs/2607.29442v1

Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper gives a microstructural foundation for rough-noise models in high-frequency prices by separating permanent price changes from fleeting price changes due to noise. The authors derive convergence to a semimartingale permanent-price process plus a rough-noise term, develop a GMM estimator/test for tick-by-tick data, validate it in simulation, and apply it to Dow Jones Industrial Average constituents in 2024. The abstract reports that rough noise is present but not universal; when detected, it is most pronounced on days dominated by short-run price reversals.

For this library, the source is a diagnostic reference, not alpha. It strengthens the view that short-horizon reversal, realized-volatility, and intraday signals should distinguish permanent moves from transient microstructure noise before being interpreted as tradable predictability.

## Core Contribution

- Provides a tick-level model separating permanent and fleeting price changes.
- Derives a rough-noise term from microstructure rather than assuming roughness phenomenologically.
- Supplies a GMM estimator and formal test for rough noise using tick-by-tick data.
- Empirically links stronger rough-noise detection to days dominated by short-run reversals.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as microstructure-noise methodology; foundational / retail-adaptable only with tick data**.
- Retail adaptation without tick data is limited; a coarser proxy could tag high bid/ask-bounce or reversal-heavy states, but should be treated as a weak approximation.
- Useful for validation of short-horizon ETF/futures/crypto strategies: do not interpret apparent reversal or volatility roughness as directional alpha unless costs, spread bounce, and noise/permanent decomposition are handled.

## Methods and Data

Validated from arXiv API metadata:

- tick-by-tick price-change model;
- permanent versus fleeting price-change decomposition;
- convergence to permanent semimartingale plus rough-noise term;
- GMM estimator and formal rough-noise test;
- simulation finite-sample check;
- Dow Jones Industrial Average constituents in 2024.

## Leakage / Bias / Overfitting Concerns

- Tick-data implementation requires high-quality quote/trade filtering and time synchronization.
- One-year DJIA evidence may not transfer to ETFs, futures, options, or crypto venues.
- Roughness/reversal-day tags could be data-mined if thresholds are fit to strategy PnL.
- Coarse OHLCV proxies may confuse volatility bursts, bid/ask bounce, and true transient-noise roughness.

## Transaction Cost / Capacity Treatment

Rough-noise states are likely exactly when spreads, adverse selection, and fill uncertainty matter. Any strategy using short-run reversals or roughness features should include spread/slippage stress, passive-fill realism, and action attribution for skipped trades or de-risking decisions.

## Strategy Ideas Extracted

No direct strategy. Candidate validation hypothesis: short-horizon reversal signals should be bucketed by rough-noise/reversal-day proxies; if profits concentrate in high-noise states and disappear after spread/adverse-selection costs, treat the signal as microstructure artifact rather than alpha.

## Connections to Existing Research

### Reinforces

- [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]]: directional predictability can be an artifact of microstructure noise and magnitude effects.
- [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]]: short-speed trend/reversal behavior must be conditioned on tick-size/liquidity/noise regimes.
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]: observed price changes should be decomposed into information and liquidity/noise components before acting.
- [[Pathwise Roughness of Bitcoin Realized Volatility]]: roughness can be measurement-sensitive and should be tied to microstructure mechanisms and downstream utility, not used as a magic signal.

### Contradicts / Weakens

- Weakens naive intraday reversal/rough-volatility signals that ignore bid/ask bounce, transient noise, and execution costs.

### Transfers Across Asset Classes or Domains

- Transfers most cleanly to liquid equities with tick data. Crypto transfer requires exchange-specific quote/trade data quality, artificial-transaction checks, and fee/funding controls.

### Missing Validation or Method Supplied

- Supplies a formal tick-data test that could become a positive/negative control for reversal-day classification.

## Framework Potential

- Candidate framework: microstructure-conditioned decay and liquidity-state validation.
- Linked notes: [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]], [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]], [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]], [[Pathwise Roughness of Bitcoin Realized Volatility]].
- Testable composite hypothesis: short-horizon strategies decay after costs when their gross edge is concentrated in transient-noise or rough-noise states rather than permanent information states.
- Minimum viable validation: compute spread/bounce/reversal-day proxies on available intraday data and compare signal performance, turnover, and slippage by noise-state buckets.
- What would falsify this connection? If noise-state buckets do not explain realized spreads, reversal concentration, forecast errors, or post-cost strategy decay beyond simple volatility and volume controls.

## Keep / Reject Decision

Keep as a foundational market-microstructure diagnostic. Do not promote as a standalone alpha strategy.

## Related Notes

- [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]]
- [[Is Trend Still Your Friend - Microstructural Demise of Short-Term Trend-Following]]
- [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]]
- [[Pathwise Roughness of Bitcoin Realized Volatility]]
