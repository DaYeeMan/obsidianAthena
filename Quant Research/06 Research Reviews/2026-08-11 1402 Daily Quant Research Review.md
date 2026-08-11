---
type: daily-quant-research-review
date: 2026-08-11 1402
source_status: partial
tags: [quant-research, daily-review]
---

# 2026-08-11 1402 Daily Quant Research Review

## Run Status

- Pre-run context generated at 2026-08-11T18:01:13Z.
- Persistent blogwatcher feed context was available and returned article metadata, but `blogwatcher-cli scan` reported `scan_ok: false` after printing only `Scanning 7 blog(s)...`. I treated feed entries as discovery leads only and did not claim fresh practitioner/RSS coverage beyond the returned metadata.
- arXiv metadata validation was run directly for selected leads via one `id_list` API call.
- Semantic Scholar lookups for selected papers returned HTTP 429, so citation counts were not recorded. Classifications below rely only on directly validated arXiv metadata.

## Items Preserved

| Item | Evidence Quality | Practicality | Decision | Why it matters |
|---|---|---|---|---|
| [[Robustness or Crowding - Experimental Design for Trading Strategy Capacity]] | Evidence-backed at abstract level as strategy-validation methodology | foundational / retail-adaptable | Saved as high-priority source and registry candidate | Turns capacity/crowding from a vague AUM heuristic into a causal identification problem; warns that same-date designs can absorb the aggregate crowding effect they need to measure. |
| [[Cross-Venue Agreement Is Not Price Discovery - Equity-Perpetual Oracle Disclosure]] | Evidence-backed at abstract level as market-design validation methodology | foundational / institutional-only as written / retail-adaptable as oracle-risk diagnostic | Saved as high-priority source and registry candidate | Strong warning for 24/7 equity-perp/oracle/prediction-market studies: cross-venue agreement is not price discovery unless disclosure or cash-reopen validation breaks observational equivalence. |
| [[Marginally Useful - Conformal Prediction Information Gap]] | Evidence-backed at abstract level as statistical validation warning | foundational / retail-adaptable | Saved as source and registry candidate | Reinforces that conformal marginal coverage is not forecast quality; interval overlays need conditional coverage, sharpness, exchangeability, and downstream net-utility tests. |
| [[Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models]] | Plausible but untested at abstract level as ML forecast methodology | foundational / institutional-only as written / retail-adaptable as benchmark design | Saved as source and registry candidate | Useful ablation lesson: Random Forest residual learning may contribute more than neural correction, so foundation-model trading claims need simple residual/tabular baselines before complexity. |
| [[Bias-Robust Causal Inference for Panel Data]] | Evidence-backed at abstract level as adjacent-domain causal-validation methodology | foundational / retail-adaptable | Saved as source and registry candidate | Adds counterfactual-error allowance to event-study validation; useful for PEAD/accounting, AMM protocol-fee, commodity shock, crypto venue, and prediction-market event studies. |

## Screened but Not Saved as Source Notes

- “On a Simple Relationship Between Order Imbalance, Skew and Width in Over-The-Counter Trading” (arXiv:2608.07690v1): useful institutional market-making theory, but sealed-bid OTC assumptions are less directly actionable for the current equities/options/crypto retail backtest queue. Mentioned as watch-only; no note created.
- “Lower spectrum of financial correlation matrices” (arXiv:2608.09641v1): potentially relevant to correlation-geometry risk states, but the abstract did not beat the library’s existing covariance/eigenstructure backlog enough to justify another source note today.
- Adjacent-domain Wasserstein-bias calibration (arXiv:2608.09863v1): useful for distribution-comparison tests but not saved because the library already has drift/divergence monitoring questions; revisit if Wasserstein/EMD becomes a chosen validation statistic.

## Literature Connections / Framework Leads

### Reinforces

- [[Robustness or Crowding - Experimental Design for Trading Strategy Capacity]] reinforces cost-aware decision-process diagnostics, liquidity-demand audits, square-root/replenishment impact, and anomaly decay checks. Capacity should be added after first-order cost/leakage filters, not inferred from full-period Sharpe.
- [[Marginally Useful - Conformal Prediction Information Gap]] reinforces [[Localized Conformal Prediction for Conditional Forecast Calibration]], [[Conformal Kelly - Uncertainty-Scaled Fractional Position Sizing]], and dependence-aware conformal/bootstrap validation. It supplies a concise reason not to promote marginal coverage into a sizing edge.
- [[Hybrid Neural-Classical Correction for Frozen Time Series Foundation Models]] reinforces the simple-rule benchmark-first AI portfolio-policy framework: ablate backbone, residual learner, neural correction, and simple baselines before any trading conversion.

### Contradicts / Weakens

- [[Cross-Venue Agreement Is Not Price Discovery - Equity-Perpetual Oracle Disclosure]] weakens naive cross-venue lead-lag/information-share claims in closed-window equity-perp or oracle-linked markets unless mark topology or cash-reopen validation is available.
- [[Bias-Robust Causal Inference for Panel Data]] weakens event-study findings with precise confidence intervals when counterfactual-imputation error is ignored.

### Transfers Across Asset Classes

- Capacity/crowding design transfers from portfolio/equity strategy evaluation to options risk premia, crypto funding/carry, and DEX/venue strategies via participation, open-interest, borrow, funding, and book-depth proxies.
- Oracle-disclosure validation transfers from equity perpetuals to prediction-market settlement, DeFi oracle, and event-linked derivative research.
- Counterfactual-error-aware panel inference transfers from econometrics to market-event studies and protocol/venue interventions.

### Missing Validation Supplied

- Add capacity/crowding stress and delayed-impact attribution to the standard audit block.
- Add closed-window oracle topology / cash-reopen validation to oracle-linked market backtests.
- Add conformal information-gap diagnostics: residual-feature dependence, interval sharpness, and state-conditional coverage.
- Add counterfactual-error allowance to event-study validation, especially when synthetic-control/factor-rank assumptions drive inference.

## Candidate Registry Updates

Added five new tracked candidates:

1. Strategy capacity/crowding experimental-design audit.
2. Equity-perpetual oracle disclosure and cash-reopen validation gate.
3. Conformal residual-information-gap forecast audit.
4. Frozen time-series foundation-model residual-ablation benchmark.
5. Bias-robust panel event-study inference gate.

No existing registry rows were promoted to coding-ready status.

## Coding Queue Review

The coding-ready queue was reviewed and left unchanged. The strongest coding implication is additive to the existing “Standard cost/regime/liquidity/decision audit block”: add capacity/crowding stress, conformal information-gap checks, and event-study counterfactual-error intervals as audit modules. None of today’s items supplies complete tradable rules, data requirements, frictions, baselines, and go/no-go criteria for standalone queue promotion.

## Hygiene Notes

- New source notes created under `Quant Research/01 Sources/` only; no root-level notes intentionally created.
- New source titles were added to the Source Index and linked from this review and the candidate registry.
- Post-write link probe checked 11 changed files and 485 wikilinks. All new source/review links resolved to exactly one file. The only unresolved target found was a pre-existing registry maintenance link to `Quant Research/04 Backtest Specs/Backtest Spec Index`, unrelated to this run.
- Root vault zero-byte markdown check returned 0 files.
- Framework labels in this review are plain text unless the linked note already exists.
