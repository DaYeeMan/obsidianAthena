---
type: daily-quant-research-review
date: "2026-08-06"
run_time: "1608 EDT"
profile: quant-researcher
asset_focus: [equities, options, crypto]
tags: [daily-quant-review]
source_status: partial
---

# Daily Quant Research Review — 2026-08-06 1608 EDT

## Run Status

- Primary collector: blogwatcher-cli was available and scanned persistent RSS state from `C:/Users/enson/.hermes/quant-research/state/blogwatcher-cli.db`.
- Feed coverage: 5 of 7 feeds succeeded. Quantocracy failed with HTTP 302; Quantpedia timed out. Alpha Architect and Robot Wealth had no new items; arXiv q-fin feeds produced six new arXiv leads.
- Fallback RSS scanner: not used.
- Validation: high-signal arXiv leads were validated through the arXiv API before note creation. Semantic Scholar mostly returned HTTP 429; citation counts were not fabricated.

## Executive Summary

Today’s useful additions were mostly validation/microstructure methods rather than immediately tradable strategies. The strongest item is [[Public Trader Identity - Adverse Selection and Return Predictability]], which suggests public wallet identity can add predictive adverse-selection information in transparent DEX order books. The most practical coding-support item is [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]], which strengthens the crypto execution/funding/tuning audit layer. No item met the promotion rule for the coding-ready queue.

## New Research Candidates

| Candidate | Asset Class | Status | Practicality | Priority | Notes |
|---|---|---|---|---|---|
| Public wallet-identity adverse-selection state | Crypto / DEX / prediction-market microstructure | Evidence-backed at abstract level | foundational / institutional-only as written / retail-adaptable as diagnostic | Medium | [[Public Trader Identity - Adverse Selection and Return Predictability]]: full-depth DEX order book with persistent wallet IDs; identity adds to one-second return prediction but needs strict time-gated ranking, fees, latency, and wallet-churn controls. |
| Execution-constrained crypto-perp auto-tuning audit | Crypto perpetuals / ML / backtest validation | Evidence-backed at abstract level as governance methodology | foundational / retail-adaptable | Medium/High for audit block | [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]]: use as AutoQuant-lite rules before trusting optimized crypto strategies. |
| GMADL decision-aligned ML trading loss | Equities / crypto / futures ML | Plausible but untested | foundational / retail-adaptable | Low/Medium | [[Generalized Mean Absolute Directional Loss for ML Trading Models]] is useful as a benchmark objective, but broad superiority claims need base-rate, simple-rule, cost, turnover, and held-out asset/regime tests. |
| Signed multiscale/multifractal portfolio risk functional | Portfolio / equities / crypto risk | Plausible-to-evidence-backed at abstract level as methodology | foundational / retail-adaptable | Medium | [[Portfolio Allocation under Heterogeneous Scales and Multifractality]] adds a candidate estimator to the covariance/risk-model benchmark suite; do not use before shrinkage/risk-parity baselines. |
| Covariate-shift goodness-of-fit gate | ML validation / strategy transfer | Evidence-backed at abstract level as adjacent statistical method | foundational / retail-adaptable | Medium for validation framework | [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]] supplies a target-regime validation method, not trading evidence. |

## Evidence-Backed / High-Priority Items

### [[Public Trader Identity - Adverse Selection and Return Predictability]]

- Hypothesis: on transparent venues with persistent public identifiers, prior wallet-level informativeness improves short-horizon adverse-selection and return-prediction state measurement beyond anonymous order flow.
- Economic rationale: informed traders normally value anonymity; if a venue publishes persistent IDs, public histories can reveal informedness and change adverse-selection dynamics.
- Data requirements: full-depth messages or trade/order records with stable wallet IDs, timestamps, order side, order book state, fees, and venue rules.
- Backtest design: rank wallets only on prior windows; forecast held-out one-second or trade-time returns; compare against anonymous price/quote/order-flow baselines and placebo wallet cohorts; convert to net utility only after fees/latency/capacity stress.
- Risks: sybil/wallet rotation, venue-specific transparency, post-publication crowding, attribution errors, and latency/costs can destroy tradability.

### [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]]

- Hypothesis: strict execution timing, funding visibility, cost scenarios, feasibility constraints, two-stage window screening, and accounting invariants reduce false promotion in crypto-perp strategy tuning.
- Economic rationale: high-friction crypto perpetuals make hidden timing/funding/cost semantics a large part of apparent edge.
- Implementation: add AutoQuant-lite to the standard audit block before optimizing any crypto signal family.
- Risks: still can overfit search budgets/windows; needs untouched final holdout and simple-rule baselines.

## Plausible but Untested Items

- [[Generalized Mean Absolute Directional Loss for ML Trading Models]]: keep as a decision-aligned objective candidate, but classify conservatively because custom trading losses can overfit and increase churn.
- [[Portfolio Allocation under Heterogeneous Scales and Multifractality]]: keep as a risk-model estimator candidate; validate versus Ledoit-Wolf/nonlinear shrinkage, EWMA, inverse-vol, and risk parity before adding complexity.

## Rejected / Low-Quality Items

- Optimal life-insurance/DC pension mean-variance item: outside the library’s strategy/backtest priorities; not saved.
- Variable annuity design/taxation lead: outside systematic trading scope; not saved.
- Adaptive finite-budget CVaR Q-learning for Bitcoin: watch-only. It reports improved Bellman residuals, but the abstract is a training-stability result rather than a cost-aware trading edge; not saved today.
- Adjacent-domain leads on recursive language models, medical/atmospheric applications, operating-room allocation, and random trees: no direct falsifiable quant-research translation today; not saved.

## Literature Connections / Framework Leads

| New Item | Connects To | Connection Type | Possible Framework | Action |
|---|---|---|---|---|
| [[Public Trader Identity - Adverse Selection and Return Predictability]] | [[Fill-Side Behavioral Concentration on Polymarket - Attribution Limits]]; [[OpenMarket Synchronized Polymarket-Binance Dataset]]; [[When Large Trades Are Not News - Liquidity Tail Risk and Price Discovery]] | Supplies public-identity adverse-selection state | Microstructure-conditioned decay and liquidity-state validation | Updated framework registry; added candidate row. |
| [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]] | [[Train Often Deploy Selectively - Forward-Gated Model Replacement in Crypto Markets]]; [[Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures]]; [[2026-08-02 Weekly Quant Synthesis and Strategy Decay Review]] | Strengthens execution/funding/tuning governance | Cost-aware decision-process diagnostics | Updated framework registry; coding queue unchanged because broader audit block already exists. |
| [[Generalized Mean Absolute Directional Loss for ML Trading Models]] | [[When Directional Accuracy Lies - Base-Rate-Honest TimesFM Equity Forecasting]]; [[Decision-Induced Ranking Explains Prediction Inflation and Excessive Turnover in SPO-Based Portfolio Optimization]]; [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]] | Adds decision-aligned ML loss but raises turnover/overfit concerns | Distributional-forecast-first ML strategy evaluation | Source + registry only; no queue promotion. |
| [[Portfolio Allocation under Heterogeneous Scales and Multifractality]] | [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]]; [[Observable Matrix Dynamics of Stocks]]; [[Physics-Informed Cross-Covariance Forecasting]] | Adds signed multiscale covariance/risk estimator candidate | Decision-aware covariance/risk-model benchmark | Source + registry only. |
| [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]] | [[Regime-Conditional Distributional Comparison of Trading Strategies]]; [[Statistical Properties and Power Analysis of Divergence Measures for Credit Risk Model Monitoring]]; [[Bet on Features - Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters]] | Supplies target-regime GOF gate | Validation-budget and regime-transfer validation | Updated open question; source + registry only. |

## Adjacent-Domain Leads

| Lead | Domain | Quant Connection | Status | Next Step |
|---|---|---|---|---|
| [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]] | Statistics / ML validation | Test whether models validated in source regimes fail in target regimes/universes | Evidence-backed methodology; foundational | Add as optional validation gate for regime-transfer and ML forecast audits. |
| Exact moment equivalence and structural nonidentifiability in nonlinear epidemics | Complex systems / inference | Useful reminder that aggregate moments can be non-identifying; could inform cascade/contagion model skepticism | Watch-only; no source note | Mentioned only as conceptual support for not over-interpreting scalar cascade indicators. |

## Outdatedness / Model-Decay Watch

- Public wallet identity has high publication-decay risk: if participants know identities are ranked, they can split wallets, rotate addresses, or crowd the signal.
- Crypto auto-tuning without funding/execution semantics should be treated as outdated/low-quality. Fee-only and zero-cost backtests are not reliable evidence.
- GMADL-style custom losses can become another overfit objective if search procedures are not frozen and turnover/costs are omitted.
- Multifractal portfolio allocation can overfit scale/order/window choices and may lose to simple shrinkage once turnover and concentration are included.

## Foundational Items to Preserve

- [[Public Trader Identity - Adverse Selection and Return Predictability]] for transparent-venue participant identity and adverse-selection state design.
- [[AutoQuant - Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures]] for crypto execution/funding/tuning governance.
- [[Nonparametric Goodness-of-Fit Testing under Covariate Shift]] for source-to-target validation under regime/universe shift.

## Strategy Notes Created or Updated

No strategy idea notes were created. Five source notes were created under `01 Sources/`.

## Framework / Synthesis Notes Created or Updated

- Framework registry updated with 2026-08-06 bullets for public wallet identity, AutoQuant, GMADL, multiscale portfolio risk, and covariate-shift GOF.
- Open questions updated with wallet-identity and covariate-shift validation questions.

## Backtest Specs Suggested

No new coding-ready backtest spec. The existing standard cost/regime/liquidity/decision audit block remains the right first implementation target. AutoQuant should be folded into that block when crypto-perpetual tests are run.

## Coding Queue Review

Reviewed and unchanged. None of today’s items supplied all promotion requirements: falsifiable rules, defined universe, data path, realistic costs, baselines, validation design, and go/no-go criteria.

## Hygiene Check

Completed after writes:

- Each new source title and the review title resolves to exactly one markdown file in `Quant Research/`.
- New source titles appear in `01 Sources/Source Index.md`, the review note, the candidate registry, and the framework registry as appropriate.
- Candidate registry updated with five new rows and `last_updated: 2026-08-06`.
- Major wikilinks in the five new source notes and this review resolve to existing notes; one framework-label wikilink was converted to plain text.
- Vault-root zero-byte markdown files: 0.

## Discord Notification Candidate?

Notify: yes. Public trader identity and AutoQuant are useful framework/audit additions; coding queue unchanged.
