---
type: source-note
source_kind: paper / FOMC event study and implied-volatility surface forecasting
asset_classes: [options, volatility, equities, event-studies, ML]
implementation_class: foundational / retail-adaptable with option-chain data
importance: medium
last_reviewed: "2026-08-13"
tags: [quant-source, options, implied-volatility, FOMC, event-study, volatility-surface, ML]
concepts: [FOMC-volatility-surface, pre-announcement-uncertainty, IV-surface-forecasting, event-risk]
---

# When the Fed Speaks - Volatility Surface Forecasts around FOMC

## Citation / Link

Lukasz Adamski, Robert Slepaczuk, “When the Fed Speaks: Dynamics and Forecasts of the Volatility Surface,” arXiv:2608.10693v1, submitted 2026-08-11. https://arxiv.org/abs/2608.10693v1

Semantic Scholar lookup returned HTTP 429 during the 2026-08-13 run, so citation counts were not recorded.

## Summary

The paper examines scheduled FOMC meeting dates as an exogenous event calendar for implied-volatility (IV) surface dynamics. The abstract asks whether IV rises before announcements, whether the effect is stronger for short-dated out-of-the-money options in high-volatility regimes, and whether an ML model with scheduled-FOMC features can beat a random-walk benchmark in forecasting the surface. The authors use a convolutional two-dimensional LSTM directly on the IV surface without dimensionality reduction. The abstract reports that noisy IV-surface characteristics limit the ML edge, but that ML can forecast abnormal-day surface behavior.

For this library, the high-signal point is the event-study design, not the CNN-LSTM. Scheduled FOMC meetings provide a clean pre-announcement uncertainty calendar, but any tradable option strategy must survive bid/ask, term/moneyness liquidity, event-time availability, and random-walk/simple-surface baselines.

## Core Contribution

- Studies IV surface behavior around scheduled FOMC events.
- Tests pre-announcement IV elevation, especially short-dated OTM options and high-volatility regimes.
- Adds event-calendar features to an ML IV-surface forecasting framework.
- Uses random-walk forecasting as a benchmark and acknowledges noisy surface limits.

## Practical Relevance

- Classification: **Plausible but untested at abstract level; foundational / retail-adaptable with option-chain data**.
- Retail-adaptable as an event-risk validation module for SPX/SPY option strategies, not immediately coding-ready as a deep-learning IV model.
- Could inform no-trade/risk-throttle rules for short-volatility strategies around FOMC if simple baselines show reliable net benefit.
- ML complexity is not justified until calendar dummy, VIX/term-structure, moneyness-tenor cell random-walk, and simple smoothing baselines are beaten.

## Transaction-Cost / Implementation Concerns

- Option bid/ask spreads, stale quotes, and moneyness/tenor liquidity can dominate event-window gains.
- Pre-announcement effects may be well-known/crowded and reflected in spreads or margin requirements.
- Surface interpolation and no-arbitrage cleaning can invent smooth signals around sparse short-dated OTM quotes.
- FOMC dates are known in advance, but announcement times and data timestamps must be decision-time aligned.

## Validation Priority

1. Use scheduled FOMC dates known before trading day and split event/pre-event/post-event windows.
2. Start with SPX/SPY IV metrics by tenor/moneyness and compare to random-walk/no-change, VIX, IV-rank, and term-structure baselines.
3. Evaluate strategy relevance: does excluding or resizing positions around FOMC improve net drawdown/utility versus missed-premium cost?
4. Add ML only after simple calendar and surface baselines are exhausted.
5. Require quote-quality filters, worse-side fills, and surface no-arbitrage checks.

## Connections to Existing Research

### Reinforces

- [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]]: FOMC calendars may be a risk-state or exclusion window for short-dated option selling.
- Option-chain data-quality and proxy-surface validation is a framework row, not a note; the practical connection is to source notes [[Inverse Learning of Latent Risk-Neutral Densities from Irregular Option Quotes]] and [[Decoupled Probabilistic IV Surface Forecasting and Arbitrage-Aware Refinement]].
- [[Velocity and Regime-Aware Detection of Intraday Options Market Manipulation]]: event and abnormal-day labels can improve option microstructure stress diagnostics.

### Framework Potential

- Candidate framework: event-conditioned option surface validation.
- Testable composite hypothesis: scheduled macro-event calendars improve option strategy risk control only if event-window IV-surface changes explain net action utility beyond VIX/IV-rank/random-walk baselines after option frictions.
- What would falsify it: forecast metrics improve on event days but trade resizing loses money after spreads and missed premium.
