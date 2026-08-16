---
type: daily-quant-research-review
date: 2026-08-13
generated_at: 2026-08-13 1244 EDT
source_status: partial
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review, arxiv, volatility, ML, options, crypto]
---

# 2026-08-13 1244 Daily Quant Research Review

## Run Status

- Pre-run collector used persistent `blogwatcher-cli` state from `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Feed scan was **partial**: 5 of 7 feeds succeeded. Alpha Architect, Robot Wealth, and three arXiv q-fin feeds succeeded; Quantocracy failed with HTTP 302 and Quantpedia timed out. No stdlib RSS fallback was used.
- Feed entries and query results were treated as discovery leads only. Saved items below were validated through arXiv API metadata/abstracts.
- Semantic Scholar impact lookups were attempted for selected saved papers. Three returned HTTP 429; one crypto stylized-facts paper returned 0 citations / 0 influential citations / 36 references. Classifications remain conservative and abstract-level.

## High-Signal Items Saved

| Item | Classification | Practicality | Why saved | Library action |
|---|---|---|---|---|
| [[Regime-Gated Residual MoE for Cross-Sectional Volatility Forecasting]] | Plausible but untested at abstract level | foundational / retail-adaptable as benchmark design | Strong validation-design lesson: regime variables may be useful as routing context for residual experts but harmful as naive direct inputs. | New source note; candidate registry row; framework/open-question update. |
| [[Calibration Bets on the Past - Quantization Calibration for Financial Forecasting]] | Evidence-backed at abstract level as deployment warning | foundational / retail-adaptable | Low-precision inference can silently change forecast distributions; activation calibration must be time-gated and walk-forward validated. | New source note; candidate registry row; framework/open-question update. |
| [[When the Fed Speaks - Volatility Surface Forecasts around FOMC]] | Plausible but untested at abstract level | foundational / retail-adaptable with option-chain data | Scheduled FOMC dates are a clean option-event risk-state lead, but ML surface forecasting must beat random-walk/VIX/IV-rank/calendar baselines after option frictions. | New source note; candidate registry row; framework/open-question update. |
| [[Crypto Stylized Facts - Universality and Heterogeneity across Crypto and Equity Markets]] | Evidence-backed at abstract level as diagnostic evidence | foundational / retail-adaptable as regime diagnostic | Warns that crypto “maturity” does not imply equity-like dynamics; useful for transferability stress tests and post-shock risk controls. | New source note; candidate registry row; framework/open-question update. |

## Screened but Not Promoted

- **Large Language Model-Driven Small-Capitalization Trading** (arXiv:2608.12283v1): interesting reported Russell 2000 small-cap sentiment/macro trigger results, but Sharpe 2.33 at 100 bps from abstract alone is too strong to promote without paper-level inspection of survivorship, trade timing, news timestamps, small-cap liquidity, turnover, and model-selection grid. Watch-only.
- **AgonAlpha** (arXiv:2608.11250v1): agentic alpha-mining system with impressive WorldQuant BRAIN claims, but platform-specific fitness metrics, prompt/search multiplicity, and hidden submission constraints make it governance evidence at best. Not saved today because existing agentic evaluation/guardrail notes already cover the main warning.
- **TradingMoE** (arXiv:2608.11785v1): LLM sparse-MoE trading claims on stocks/crypto are too complex and likely data-mining-sensitive from abstract alone. Needs exact temporal split, costs, baselines, and paper-trading audit before preservation.
- **Optimal Execution under Incomplete Information** (arXiv:2411.04616v2): rigorous microstructure/execution theory update, but primarily HFT/LOB/impulse-control and institutional-only as written. Existing execution realism notes are enough unless a future execution project needs it.
- **Does a Structural Model Add Anything to the Closing Price?** is sports forecasting, outside current trading scope; not saved.

## Literature Connections / Framework Leads

### Reinforces

- [[Regime-Gated Residual MoE for Cross-Sectional Volatility Forecasting]] reinforces [[Forecasting Realized Volatility with Time Series Foundation Models]], [[Risk-Sensitive Specialist Routing for Volatility Forecasting]], and [[Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting]]: volatility ML should start from simple/econometric anchors, add residual/state modules only when they improve calibration and downstream utility, and report action attribution.
- [[Calibration Bets on the Past - Quantization Calibration for Financial Forecasting]] reinforces [[FinBench - Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting]] and [[Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models]] by adding deployment precision as a separate validation state.
- [[When the Fed Speaks - Volatility Surface Forecasts around FOMC]] reinforces [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] and option-chain validation notes: scheduled event calendars are plausible risk-state covariates, not alpha, until they beat simple event/no-change baselines after spreads.
- [[Crypto Stylized Facts - Universality and Heterogeneity across Crypto and Equity Markets]] reinforces [[Crypto Perpetual Liquidation Cascades - Event-Heterogeneous Early Warnings]], [[Pathwise Roughness of Bitcoin Realized Volatility]], and [[Microstructural Foundations of Rough Noise]]: crypto risk states need venue/event/post-shock conditioning, not blind equity model transfer.

### Framework Potential

- The run strengthens the existing distributional/regime/deployment validation stack rather than creating a separate framework. New framework registry wording now groups regime routing, quantization calibration, FOMC option-surface event risk, and crypto-equity transferability as validation gates.
- Added open questions for: regime-gated volatility utility, quantized deployment equivalence, FOMC IV-surface risk-control value, and crypto post-shock transferability.

## Candidate Registry Updates

Added four rows:

1. Regime-gated residual volatility forecast benchmark.
2. ML quantization calibration deployment audit.
3. FOMC-conditioned IV-surface risk-state validation.
4. Crypto-equity stylized-facts transferability stress test.

## Coding Queue Review

- Reviewed [[09 Coding-Ready Backtest Queue]]. No promotion today.
- Reason: all saved items improve validation/framework design but do not yet supply complete executable trading rules, data/cost assumptions, baselines, and go/no-go thresholds.
- Near-term coding implication remains unchanged: prioritize the standard cost/regime/liquidity/decision audit block before adding new alpha or ML complexity.

## Hygiene Check

Completed after writes:

- New source note titles appear in [[Source Index]].
- Link probe found exactly one source-note file for each new title and resolved the new daily-review link from [[Research Review Index]].
- One accidental framework-label wikilink in the FOMC source note was converted to plain text.
- No zero-byte markdown files were found at the vault root.
