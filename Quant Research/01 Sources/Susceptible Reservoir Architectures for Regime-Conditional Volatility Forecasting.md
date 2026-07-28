---
type: source-note
source_kind: paper / adjacent-domain ML volatility method
asset_classes: [equities, etfs, options, crypto, volatility, risk-management]
implementation_class: foundational / retail-adaptable
importance: medium
last_reviewed: "2026-07-27"
tags: [quant-source, volatility-forecasting, reservoir-computing, regime-conditioning, qlike, risk-management]
concepts: [susceptible-architectures, reservoir-volatility-forecasting, regime-conditioned-experts, ar-ridge-anchor, qlike-validation]
---

# Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting

## Citation / Link

Aliaksei Kaliutau, “Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting,” arXiv:2607.22491v1, submitted 2026-07-24. https://arxiv.org/abs/2607.22491v1

## Summary

The paper argues that volatility forecasting is dominated by persistence and measurement noise, leaving only limited residual structure for nonlinear models. It introduces Susceptible Architectures (SUSA), implemented with complex-valued open-chain and periodic reservoir models plus regime-conditioned experts across calm, onset, recovery, and persistent-stress states. The design keeps an AR-Ridge anchor and trains bounded residual corrections under QLIKE. The abstract reports tests on 16 U.S. equity and ETF series using chronological train/validation/test folds, a 12-observation input window, and a five-observation forecast horizon. SUSA variants are competitive with GARCH, achieve statistically significant QLIKE gains for selected assets such as IWM and XLP, and complement HARQ-style forecasts in a stacked ensemble.

For this library, the strongest contribution is the discipline of anchored residual learning for volatility forecasts: any nonlinear model should first prove incremental value over AR/HAR/GARCH/EWMA anchors and then show downstream risk-control utility.

## Core Contribution

- Treats volatility forecasting as mostly persistent/noisy, so nonlinear models are residual-correction modules rather than full replacements for simple anchors.
- Uses regime-conditioned experts for calm, onset, recovery, and persistent-stress states.
- Evaluates against GARCH and HARQ-style forecasts using QLIKE and chronological folds.
- Suggests stacked ensembles can be more useful than claiming one architecture is universally superior.

## Practical Relevance

- Classification: **Plausible but untested at abstract level as volatility-forecasting methodology; foundational / retail-adaptable**.
- Retail adaptation is plausible with daily ETF/underlying returns and realized-volatility inputs.
- Not a direct alpha signal; possible use is position sizing, de-risking, or volatility-risk-premium throttling after simple baselines exist.
- The result is not enough to promote reservoir/quantum-style models as a production module because gains appear asset-specific and forecast-loss improvements may not improve net PnL.

## Methods and Data

Abstract-level details:

- 16 U.S. equity and ETF series,
- three disjoint chronological training, validation, and test folds,
- 12-observation input window,
- five-observation forecast horizon,
- AR-Ridge anchor with bounded residual correction,
- QLIKE training/evaluation,
- comparisons to GARCH and HARQ-style forecasts,
- regime-conditioned experts for volatility states.

## Leakage / Bias / Overfitting Concerns

- Regime labels and expert routing must be based only on decision-time available data.
- Reservoir design, complex-valued architectures, and quantum-style variants can overfit small panels and selected assets.
- Asset-specific wins such as IWM/XLP may not survive multiple-testing adjustment or a broader universe.
- Forecast-loss gains need a downstream decision test: drawdown, turnover, missed upside, and net utility.

## Transaction Cost / Capacity Treatment

The method changes risk forecasts and sizing rather than fills directly. Downstream trading tests should measure whether more reactive forecasts increase turnover, whipsaws, option-spread drag, crypto fees/funding, or missed carry during volatility spikes.

## Strategy Ideas Extracted

### Anchored residual volatility throttle

- **Hypothesis:** A bounded nonlinear residual model on top of AR/HAR/GARCH volatility anchors improves risk sizing only in specific volatility regimes.
- **Universe:** Liquid ETFs and SPX/crypto underlyings first; options strategy use only after underlying-volatility value is proven.
- **Signal:** Forecasted five-day volatility or volatility state from AR/HAR/GARCH anchor plus SUSA residual; use for sizing or risk throttle.
- **Backtest design:** Compare EWMA, GARCH, HAR/Log-HAR, AR-Ridge, existing specialist routing, SUSA residual, and stacked ensembles. Evaluate QLIKE plus downstream strategy utility, turnover, and drawdown.
- **Validation priority:** Medium as an addition to the volatility-forecast benchmark suite, not a standalone coding queue item.

## Connections to Existing Research

### Reinforces

- [[Risk-Sensitive Specialist Routing for Volatility Forecasting]]: volatility models should be routed or evaluated by regime rather than pooled unconditionally.
- [[Forecasting Realized Volatility with Time Series Foundation Models]]: complex models must beat econometric anchors and per-asset baselines, not only pooled headline metrics.
- [[Pathwise Roughness of Bitcoin Realized Volatility]]: volatility features are measurement-sensitive; robust baselines and downstream utility matter more than architecture novelty.

### Contradicts / Weakens

- Weakens any architecture-first volatility-forecasting claim: the abstract explicitly states persistence and measurement noise dominate, so nonlinear residual structure is limited.

### Transfers Across Asset Classes or Domains

The anchored-residual-plus-regime-expert pattern may transfer to crypto volatility and option-selling risk throttles, but only after exchange/funding/regime frictions are added.

### Missing Validation or Method Supplied

Supplies a useful benchmark design: simple anchor first, bounded nonlinear residual second, stacked ensemble third, and downstream utility last.

## Framework Potential

- Candidate framework: distributional-forecast-first ML strategy evaluation / regime-conditional distributional strategy evaluation.
- Linked notes: [[Risk-Sensitive Specialist Routing for Volatility Forecasting]], [[Forecasting Realized Volatility with Time Series Foundation Models]], [[Pathwise Roughness of Bitcoin Realized Volatility]].
- Testable composite hypothesis: nonlinear volatility models are acceptable only when they add regime-specific residual value over simple anchors and improve downstream net utility after turnover/costs.
- Minimum viable validation: chronological folds, QLIKE, per-asset tests, multiple-testing awareness, simple anchor baselines, and strategy-level utility tests.
- What would falsify this connection? No per-asset benefit after multiple-testing adjustment, unstable regime wins, or improved QLIKE without improved drawdown/utility.

## Keep / Reject Decision

**Keep as foundational / retail-adaptable method lead.** It strengthens the existing volatility-model benchmark framework but does not make the coding queue more ready.

## Related Notes

- [[Risk-Sensitive Specialist Routing for Volatility Forecasting]]
- [[Forecasting Realized Volatility with Time Series Foundation Models]]
- [[Pathwise Roughness of Bitcoin Realized Volatility]]
