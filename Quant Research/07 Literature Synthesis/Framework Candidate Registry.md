---
type: framework-candidate-registry
created: 2026-06-29
tags: [quant-research, framework-registry, synthesis]
---

# Framework Candidate Registry

This registry tracks multi-paper / multi-domain frameworks that may become reusable research programs, validation standards, or strategy families.

## Status Legend

- **Active**: worth developing or validating.
- **Watch**: promising but needs more evidence or clearer implementation path.
- **Backtest-ready**: framework has a minimum viable test design.
- **Rejected**: connection was weak, non-falsifiable, or not useful after review.
- **Foundational**: keep as a reusable research lens, not necessarily a strategy.

## Framework Table

| Framework | Linked Papers / Notes | Mechanism | Asset Classes | Hypothesis Type | Backtestability | Evidence Level | Novelty | Fragility / Failure Modes | Next Validation Step | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Distributional-forecast-first ML strategy evaluation | [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]]; [[Forecast-uncertainty-aware ML asset pricing]]; [[Continuous Hidden Markov Models for Equity Returns]]; [[CryptoGAT - Are Time Series Models Effective for Cryptocurrency Forecasting]] | Treat predictive distribution/calibration as first-class; compare output heads and uncertainty estimates before complex backbones | Equities, crypto, portfolio/risk | Validation / sizing framework | Medium: can be tested with existing return forecasts and simple baselines | Evidence-backed as methodology, strategy impact untested | Moderate: shifts ML research from architecture novelty to downstream distributional utility | Better CRPS/coverage may not improve post-cost decisions; mixture heads may overfit limited tail events | Add point-vs-density forecast comparison to the first ML return-prediction backtest and evaluate turnover-adjusted allocation utility | Active |
| Cost-aware decision-process diagnostics | [[Liquidity-Based Audit of Algorithmic Trading Strategies]]; [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]; [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]]; [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]] | Evaluate strategies/models by decision trail, liquidity demand, time gating, costs, and downstream regret rather than return-only or prediction-score-only rankings | Equities, options, crypto, portfolio agents | Backtest governance / model validation | Medium: simplified audit fields can be added to local backtest reports | Plausible-to-evidence-backed as a framework assembled from multiple methods | High practical value: unifies leakage, cost, and decision-aware evaluation | Diagnostics may be noisy; full intraday execution data may be unavailable; can become bureaucracy unless tied to go/no-go rules | Define a standard backtest audit block: TimeGate/leakage, liquidity-demand proxy, turnover/cost stress, and downstream decision regret | Active |

## Maintenance Rules

- Add only frameworks that connect multiple sources or transfer a mechanism across domains.
- Do not add vague themes like "use ML for crypto" unless they become falsifiable.
- Prefer frameworks that improve strategy design, model validation, cost modeling, regime handling, or portfolio construction.
- Record why a connection may fail; novelty without falsifiability is not useful.
