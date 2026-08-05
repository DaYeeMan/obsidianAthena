---
type: source-note
source_kind: paper / conformal-uncertainty position-sizing methodology
asset_classes: [portfolio, equities, crypto, options, risk-management]
implementation_class: foundational / retail-adaptable
importance: high
last_reviewed: "2026-08-04"
tags: [quant-source, conformal-prediction, kelly-sizing, position-sizing, forecast-uncertainty]
concepts: [conformal-kelly, uncertainty-scaled-sizing, fractional-kelly, downside-miss-leverage-cut]
---

# Conformal Kelly - Uncertainty-Scaled Fractional Position Sizing

## Citation / Link

Robert Jacob Ryan, “Conformal Kelly: Conformal Prediction Intervals as the Scale in Fractional Kelly Position Sizing,” arXiv:2608.01494v1, submitted 2026-08-02. https://arxiv.org/abs/2608.01494v1

Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper uses conformal prediction interval width as the scale input to fractional Kelly sizing. Wider intervals shrink positions; narrower intervals permit larger positions. The abstract reports a six-year development window from 2016–2021 with trading costs and leverage caps, where the simple slow, unweighted, per-asset rolling-quantile interval beat faster adaptive interval variants and textbook standard-deviation scaling at matched leverage.

For this library, the result is a high-value sizing-method lead, not yet a coding-ready alpha signal. The strongest reusable claim is that forecast uncertainty should be evaluated by downstream sizing utility and stability, not only by interval sharpness or nominal coverage.

## Core Contribution

- Converts conformal interval width into a fractional-Kelly scale variable.
- Emphasizes slow/stable interval estimation for sizing rather than fast local sharpness.
- Includes costs and leverage caps in the reported development-window comparison.
- Adds a downside-miss control: cut leverage when downside misses exceed historical rates.

## Practical Relevance

- Classification: **Plausible-to-evidence-backed at abstract level as sizing methodology; foundational / retail-adaptable**.
- Retail adaptation is feasible for ETF, liquid crypto, or strategy-pool allocations if a time-gated forecast or return-distribution proxy already exists.
- Do not apply directly to option selling or leveraged crypto until margin/cash, boundary distance, turnover, spreads, funding, and missed-rebound costs are included.

## Strategy / Backtest Translation

- Hypothesis: uncertainty-scaled fractional sizing improves log-growth/drawdown trade-offs versus fixed fraction, volatility targeting, and standard-deviation Kelly when forecasts are noisy and regimes shift.
- Universe: start with liquid ETFs or BTC/ETH daily returns; later adapt to SPX/SPXW risk-premia sizing after option-chain data are realistic.
- Signal: per-asset conformal interval width from strictly trailing calibration; position size shrinks as width grows and cuts leverage when downside miss frequency breaches a pre-set threshold.
- Baselines: buy-and-hold, equal weight, inverse-vol, fixed fractional Kelly, volatility target, standard-deviation Kelly, and no-forecast sizing.
- Validation: chronological folds, development/holdout separation, post-2021 out-of-sample, turnover/cost stress, leverage cap sensitivity, block/bootstrap interval comparisons, and action attribution.

## Risks / Failure Modes

- Development-window overfit: the abstract reports 2016–2021 development results; post-2021 performance and frozen rule transfer are required.
- Interval calibration can fail under structural breaks, volatility regime shifts, fat tails, and autocorrelation.
- Kelly sizing is sensitive to forecast error; uncertainty shrinkage can still over-lever during correlated downside misses.
- Turnover, financing, spreads, margin constraints, and missed-rebound opportunity costs can dominate raw log-growth.

## Connections to Existing Research

- Reinforces [[Boundary-Induced Apparent Risk Aversion in Multiplicative Growth]] by giving an uncertainty-scale companion to boundary-aware fractional Kelly.
- Reinforces [[tsbootstrap - Distribution-Free Uncertainty Quantification and Conformal Prediction for Time Series]] and [[Forecast-uncertainty-aware ML asset pricing]] as validation/sizing infrastructure.
- Connects to the SPX/SPXW queue item only as a future overlay after fixed-risk short-vol baselines and option-specific margin/fill modeling exist.
