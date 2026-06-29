---
type: research-source-watchlist
tags: [quant-research, sources, phase-2]
---

# Research Source Watchlist

This note defines the source universe for Phase 2 continuous collection. The daily collector should prefer high-signal sources and avoid low-quality trading-content feeds.

## Primary Academic / Paper Sources

- arXiv queries across `q-fin`, `stat.ML`, `cs.LG`, `econ.EM`, and adjacent categories for:
  - empirical asset pricing
  - market microstructure
  - volatility risk premia
  - options/earnings/event studies
  - crypto market microstructure
  - regime detection
  - time-series forecasting
  - cross-sectional return prediction
  - portfolio/risk construction
- Semantic Scholar expansion from relevant papers:
  - citation counts and influential citations
  - references
  - citing papers
  - related/recommended papers
- SSRN / NBER / journal pages when accessible from web extraction.

## Adjacent-Domain Sources for Connection Discovery

Use a small portion of collection/synthesis time to scan adjacent fields when they may improve quant frameworks:

- statistics / econometrics: causal inference, panel methods, multiple testing, uncertainty estimation
- machine learning: representation learning, online learning, conformal prediction, graph learning, leakage-resistant validation
- signal processing: filtering, change-point detection, spectral/wavelet methods
- control theory / operations research: robust control, stochastic optimization, inventory/execution constraints
- network science / ecology / epidemiology: contagion, resilience, regime transitions, dependency networks
- physics / complex systems: heavy tails, critical transitions, agent-based models
- decision theory: decision-aware evaluation, regret, utility, risk constraints

Adjacent-domain material should be treated as method leads, not trading evidence, unless translated into a falsifiable market hypothesis.

## Practitioner Sources Worth Considering

Only include practitioner work when methodology is transparent enough to reproduce or falsify.

Examples of acceptable traits:
- code or notebooks
- public data references
- clear sample period
- transaction-cost assumptions
- walk-forward / out-of-sample tests
- comparison against simple baselines

## Exclusion Rules

Reject or quarantine sources dominated by:
- day-trading guru signals
- undocumented Discord/X/YouTube claims
- unsupported win rates
- chart-pattern folklore
- strategy claims without data, costs, and sample size
- paywalled black-box signals with no methodology

## Default Search Themes

Rotate across these themes so the library does not become event-only:

1. Equity event studies and post-event drift
2. Options volatility risk premia, earnings straddles, skew, term structure
3. Crypto momentum, funding, basis, liquidity, and market microstructure
4. Factor research, anomaly decay, and post-publication performance
5. ML/AI for forecasting with leakage-resistant temporal validation
6. Regime detection and risk allocation
7. Portfolio construction, covariance/risk models, drawdown control
8. Transaction costs, capacity, slippage, and realistic backtesting

## Practicality Filter

Every candidate should receive one implementation label:

- `retail-practical`
- `retail-adaptable`
- `institutional-only`
- `foundational`
- `outdated-watch`

The daily collector should prioritize `retail-practical` and `retail-adaptable`, preserve `foundational`, and avoid spending much attention on `institutional-only` unless conceptually useful.
