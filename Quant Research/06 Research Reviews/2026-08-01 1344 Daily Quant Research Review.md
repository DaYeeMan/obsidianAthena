---
type: daily-quant-research-review
date: 2026-08-01 1344 EDT
source_status: normal
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review]
---

# 2026-08-01 1344 Daily Quant Research Review

## Run Status

- Pre-run collector status: blogwatcher-cli available and scan completed; 6 of 7 tracked feeds succeeded. Quantocracy returned HTTP 302 and was not treated as validated coverage.
- RSS/practitioner leads were treated as discovery inputs only, not evidence.
- arXiv validation: selected leads were validated through the arXiv API before saving notes.
- Semantic Scholar: rate-limited for selected lookups, so no citation counts were recorded for today’s new source notes.
- Coding queue reviewed: unchanged; no new item met the library’s promotion rule requiring fully specified rules, data, costs, baselines, validation design, and go/no-go criteria.

## High-Signal Items Saved

### 1. [[Boundary-Induced Apparent Risk Aversion in Multiplicative Growth]]

- Source: Ling Zhang, Boyan Xing, Zhenyu She, Zixiang Xu, “Boundary-Induced Apparent Risk Aversion in Nonergodic Multiplicative Growth,” arXiv:2607.28230v1.
- Classification: **Evidence-backed at abstract level as position-sizing methodology**.
- Practicality: **foundational / retail-adaptable**.
- Why saved: the absorbing-boundary setup maps directly to account survivability, margin calls, drawdown stops, and short-vol crash constraints. It strengthens boundary-aware fractional Kelly as a sizing guardrail rather than a standalone alpha signal.
- Implementation implication: future Kelly/vol-targeting tests should include distance-to-boundary, residual value after breach, margin/cash, drawdown CVaR, turnover, and missed-rebound action attribution.

### 2. [[Optimal Dynamic Fees in Automated Market Makers]]

- Source: Leonardo Baggiani, Martin Herdegen, Leandro Sánchez-Betancourt, “Optimal Dynamic Fees in Automated Market Makers,” arXiv:2506.02869v3.
- Classification: **Plausible-to-evidence-backed at abstract level as AMM market-design theory**.
- Practicality: **foundational / retail-adaptable as simulator and cost-model input**.
- Why saved: it adds trader-facing dynamic fee mechanics to the DeFi/AMM execution-cost framework. Fixed pool fees are an unsafe assumption when fees may respond to inventory and external-price changes.
- Implementation implication: DeFi/AMM backtests should add dynamic-fee stress scenarios alongside gas, stale-state, MEV/sandwich, failed-transaction, and route-support shortfall assumptions.

## Screened but Not Saved as Source Notes

| Lead | Classification | Decision |
|---|---|---|
| FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning, arXiv:2607.28127v1 | **Speculative / plausible but untested**; foundational only if used as an RL/NLP validation warning | Not saved. The abstract reports a 220% return improvement over the strongest baseline, but key risk details are absent at abstract level: timestamping, publication-time availability, asset universe, cost/slippage, benchmark contamination, reward overfit, and simple sentiment/price baselines. Keep watch-only until full methodology is inspected. |
| Learning Market Making with Closing Auctions, arXiv:2601.17247v2 | **Plausible but institutional-only as written** | Not saved today. Interesting for auction-aware market-making, but it requires intraday LOB/auction data and simulator validation; existing execution-agent and passive-impact notes already cover the immediate governance need. |
| No Trading Strategy Can Win on Every Price Path, arXiv:2604.13334v2 | **Foundational / no-trade theorem reminder** | Not saved as a separate note. Useful philosophical guardrail: every strategy needs an explicit market restriction, risk premium, or information advantage. The lesson is already compatible with the standard audit block; no direct candidate update needed. |
| Intraday Gas Fee Heterogeneity on Ethereum, arXiv:2604.19956v2 | **Plausible as operational gas-cost evidence; DeFi cost-model lead** | Not saved separately because [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]] already tracks gas-aware execution. Mentioned as support for adding time-of-day gas heterogeneity to DeFi cost stress. |
| Bootstrap inference in autoregressive duration models, arXiv:2607.28294v1 | **Foundational econometrics / market-duration inference** | Not saved. Potentially useful for transaction-duration modeling, including crypto ETF transaction durations, but no immediate current backtest blocker depends on ACD inference. |
| The Interplay between Utility and Risk in Portfolio Selection, arXiv:2509.10351v2 | **Foundational portfolio theory** | Not saved. The well-posedness criterion is relevant to utility-risk optimization, but today’s boundary/Kelly item was more directly connected to active sizing and the SPX/SPXW queue item. |

## Literature Connections / Framework Leads

### Reinforces

- [[Boundary-Induced Apparent Risk Aversion in Multiplicative Growth]] reinforces [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]] and [[Sizing the Risk - Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options]]: fractional Kelly should be tested under explicit margin/drawdown/continuation boundaries, not only estimated from mean/variance.
- [[Optimal Dynamic Fees in Automated Market Makers]] reinforces [[Causal Effects of Protocol-Fee Changes on Liquidity Provision in Automated Market Makers]] and [[DEX Routing Sub-Optimality - Information-Timely Gas-Aware AMM Execution]]: AMM fee design affects execution costs through multiple channels, and LP take-rate evidence does not identify trader-facing dynamic fee effects.

### Contradicts / Weakens

- Unconstrained Kelly sizing claims are weakened if they ignore finite horizon, absorbing boundaries, residual value after breach, margin, and funding.
- Fixed-fee DeFi strategy backtests are weakened if they treat AMM fees as static while routing, inventory, gas, and external-price state change through time.
- FinSMART-style market-aligned RL sentiment claims remain weak until they prove timestamp hygiene, simple baselines, and post-cost utility rather than reward-shaped return overfit.

### Transfers Across Asset Classes

- Boundary-aware sizing transfers across SPX/SPXW option selling, crypto leverage, and ML portfolio allocation as a survival-control layer.
- Dynamic-fee AMM control transfers into execution-cost stress testing: the actionable object is not a direct signal, but a more realistic cost/fill simulator.

### Framework Updates

- Framework registry updated to add today’s two links to the recent-update log.
- Open questions updated with: boundary-aware Kelly survival value and dynamic trader-facing AMM fee stress.

## Candidate Registry Updates

Added two tracked candidates:

1. Absorbing-boundary Kelly sizing guardrail — foundational / retail-adaptable; medium priority as a sizing audit layer.
2. Dynamic trader-facing AMM fee cost model — foundational / retail-adaptable; medium priority for DeFi/AMM execution-audit modules.

## Coding Queue Review

Unchanged. Today’s items improve validation and cost modeling but do not specify a complete new tradable strategy with data, frictions, baselines, and go/no-go rules.

## Hygiene Notes

- New source notes created under `01 Sources/` only; no root-level note stubs intentionally created.
- Source Index, Research Review Index, Candidate Registry, Framework Registry, and Open Research Questions were updated in the same run.
- Link probe checked the review note, new source notes, Source Index, Candidate Registry, Framework Registry, and Open Questions: 0 missing wikilinks.
- Vault-root zero-byte markdown check: 0 files.
