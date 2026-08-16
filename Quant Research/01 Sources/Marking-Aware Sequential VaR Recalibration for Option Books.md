---
type: source-note
source_kind: paper / option-book VaR and leakage-safe risk recalibration
asset_classes: [options, equities, risk-management, model-validation]
implementation_class: foundational / retail-adaptable with option-chain data
importance: high
last_reviewed: "2026-08-14"
tags: [quant-source, options, VaR, risk-management, leakage, marking, recalibration]
concepts: [marking-aware-risk-targets, option-book-VaR, sequential-recalibration, leakage-safe-risk-controls]
---

# Marking-Aware Sequential VaR Recalibration for Option Books

## Citation / Link

Tenghan Zhong, Keyuan Wu, “Marking-Aware Sequential VaR Recalibration for Standardized Option Books,” arXiv:2604.03499v3, originally submitted 2026-04-03 and updated 2026-08-13. https://arxiv.org/abs/2604.03499v3

Semantic Scholar lookup succeeded during the 2026-08-14 run: 0 citations, 0 influential citations, 28 references returned.

## Summary

The paper argues that option-book VaR evaluation must define the risk target before selecting a quantile model: book construction, next-day marking rule, loss scale, and forecast-time information set. The abstract directly criticizes pipelines that apply VaR to underlying returns or already-constructed book loss series while leaving operational marking choices outside the statistical target.

The proposed framework targets normalized book-level loss directly, restricts the forecast state to information available at forecast time, and sequentially recalibrates upper-tail VaR using only past forecast residuals. Out-of-sample tests on SPX index options and QQQ ETF options report that a reference VaR undercovers all three standardized books in both markets, while sequential recalibration moves exceedance rates near target and improves average violation, pinball loss, and rolling 50-day maximum exceedance. Robustness checks reportedly hold under direct marking, stricter book screens, no VaR floor, alternative learners, recalibration windows, and decay rates.

For this library, the durable contribution is a leakage-safe option-risk target definition and recalibration layer, not a standalone alpha signal.

## Core Contribution

- Makes the option-book VaR target operational: book construction, marking rule, loss scale, and information set must be fixed before modeling.
- Uses only past forecast residuals for sequential upper-tail recalibration.
- Tests SPX and QQQ option books out of sample.
- Reports better exceedance control and pinball-loss performance versus unrecalibrated reference VaR.
- Explicitly addresses quote and marking frictions at the abstract level.

## Practical Relevance

- Classification: **Evidence-backed at abstract level as risk-control methodology; foundational / retail-adaptable with option-chain data**.
- Highly relevant to SPX/SPXW option-selling, earnings straddles, and any standardized option-book backtest where the loss target can be accidentally redefined after observing outcomes.
- More immediately useful as an audit block than as a new trading strategy.

## Implementation / Backtest Translation

Minimum viable use in a retail-style option backtest:

1. Define standardized book construction ex ante: delta/tenor/moneyness buckets, expiry handling, roll/close rules, collateral/margin proxy, stale quote filters, and worse-side or mid-minus-spread marking.
2. Define next-day marking and loss scale before fitting risk models.
3. Fit a simple reference VaR model using only forecast-time features.
4. Recalibrate residual exceedances sequentially using only past forecast errors.
5. Compare exceedance rate, pinball loss, rolling 50-day max exceedance, action attribution, and missed-premium cost versus no-recalibration, EWMA/GARCH/HAR volatility, VIX/IV-rank, and simple drawdown stop baselines.

## Costs / Frictions

- Requires historical option chains with bid/ask, quote timestamps, underlying prices, and corporate-action/expiry hygiene.
- Risk target is sensitive to marking choice; mid marks can materially overstate safety.
- Option spreads, early close/expiry mechanics, margin, and forced liquidation should be modeled separately from the VaR calibration score.

## Risks / Failure Modes

- Recalibrated VaR can become a false comfort if the book definition changes or if forecast-time features leak future quote quality.
- Good exceedance control does not imply positive expected return.
- Tail clustering and volatility-regime breaks may still produce undercoverage if recalibration windows are too slow or too short.
- Standardized SPX/QQQ books may not transfer to illiquid single-name options.

## Connections to Existing Research

### Reinforces

- [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] needs explicit marking-aware risk targets before any Kelly/VIX overlay is trusted.
- [[When the Fed Speaks - Volatility Surface Forecasts around FOMC]]: event-risk filters should be evaluated on book-level marked losses, not only IV-surface forecast metrics.
- [[Conformal Kelly - Uncertainty-Scaled Fractional Position Sizing]] and [[Marginally Useful - Conformal Prediction Information Gap]]: calibrated intervals/sizing tools need target-definition and conditional-coverage checks.

### Framework Potential

- Candidate framework: option risk controls as target-definition-first systems.
- Testable composite hypothesis: marking-aware sequential recalibration reduces realized tail violations for standardized short-option books after quote-quality and spread assumptions, while preserving enough premium capture to improve net utility versus simple volatility/drawdown throttles.
- What would falsify it: no improvement in book-level exceedance, pinball loss, or action utility after realistic bid/ask and margin assumptions, or instability across expiry/moneyness/liquidity buckets.
