---
type: source-note
source_kind: paper / empirical crypto bubble diagnostics
asset_classes: [crypto, bitcoin, ether, risk-management]
implementation_class: foundational / retail-adaptable / outdated-watch
importance: medium
last_reviewed: "2026-07-27"
tags: [quant-source, crypto, bubble-diagnostics, lppl, psy-test, risk-management]
concepts: [crypto-bubble-detection, log-periodic-power-law, bsadf, regime-risk-filter, post-bubble-crash-risk]
---

# Crypto Bubble Diagnostics - LPPL and PSY Tests for Bitcoin and Ether

## Citation / Link

Marco Bianchetti, Camilla Ricci, Marco Scaringi, “Are cryptocurrencies real financial bubbles? Evidence from quantitative analyses,” arXiv:2607.21826v1, submitted 2026-07-23; comment states first version 2017-12-23. https://arxiv.org/abs/2607.21826v1

## Summary

The paper applies two bubble-detection families to Bitcoin and Ether: Log Periodic Power Law (LPPL/JLS) models estimated by OLS, GLS, and MLE, and Phillips-Shi-Yu explosive-root tests (BSADF and BSADF*). The sample in the abstract is 2016-12-01 through 2018-01-16. The reported signals identify Bitcoin bubble hallmarks in mid-December 2017 and early January 2018 before the subsequent crashes, Ether bubble evidence in mid-June 2017 before the June crash, and a weaker Ether signal around January 2018.

For this library, the useful object is not a fresh crypto alpha claim. It is a bubble/regime-diagnostic reference and an outdatedness warning: the empirical sample is historically important but covers the 2017 retail mania, not current fragmented spot/perpetual/ETF-era crypto microstructure.

## Core Contribution

- Combines LPPL/JLS model fitting with PSY explosive-root tests for crypto bubble identification.
- Frames bubble diagnostics as risk-management inputs rather than standalone return predictors.
- Adds a historical benchmark for crash-risk filters during parabolic crypto regimes.
- Highlights the need to separate bubble-state detection from executable timing, because warning signals can be early, unstable, or heavily parameterized.

## Practical Relevance

- Classification: **Evidence-backed at abstract level for historical 2017 bubble diagnostics; foundational / retail-adaptable / outdated-watch**.
- Retail adaptation is possible using daily BTC/ETH prices and public OHLCV data, but any modern test must include post-2018, post-2020, and ETF/perpetual-futures-era regimes.
- Best use: a risk-off/throttle covariate or stress label for crypto momentum, carry/funding, and volatility strategies, not a standalone short signal.

## Methods and Data

Abstract-level details:

- Bitcoin and Ether prices,
- sample from 2016-12-01 to 2018-01-16,
- LPPL/JLS variants: OLS, GLS, MLE,
- PSY tests: BSADF and BSADF*,
- qualitative mapping from detected bubble windows to subsequent crashes.

## Leakage / Bias / Overfitting Concerns

- The arXiv comment says the first version dates to 2017-12-23; treat the new 2026 arXiv appearance as a versioning/publication event, not necessarily new evidence.
- LPPL fits can be parameter-sensitive and may identify bubbles after a large portion of the run-up has already occurred.
- Crash mapping risks narrative hindsight unless critical-time estimates and alert thresholds are frozen ex ante.
- Crypto market structure changed materially after 2018: derivatives dominance, stablecoins, cross-exchange fragmentation, ETFs, and institutional flows.

## Transaction Cost / Capacity Treatment

The paper is about detection/risk management, not execution. Any trading use must test signal latency, exchange fees, spread/slippage, funding, borrow/shorting constraints, and whether de-risking improves net utility versus simple drawdown, realized-volatility, moving-average, and funding filters.

## Strategy Ideas Extracted

### Crypto bubble-risk throttle

- **Hypothesis:** LPPL/PSY bubble-state flags identify parabolic crypto regimes where long-only or leveraged momentum/carry strategies should reduce exposure before crash risk dominates expected return.
- **Universe:** BTC and ETH first; later liquid majors only if data quality and delisting controls are solved.
- **Signal:** Predeclared LPPL fit-quality/critical-time windows plus PSY explosive-root flags, lagged to decision time.
- **Backtest design:** Compare against buy-and-hold, time-series momentum, realized-volatility throttle, moving-average break, drawdown stop, and funding/basis filters across 2017, 2020-2021, 2022, 2024-2026 regimes.
- **Validation priority:** Medium/Low until signal definitions are frozen and shown to add value over simple filters after fees and funding.

## Connections to Existing Research

### Reinforces

- [[Pathwise Roughness of Bitcoin Realized Volatility]]: crypto risk-state variables are measurement-sensitive and should not be promoted without incremental downstream utility.
- [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]]: predictive diagnostics can fail to become profitable policies after timing and cost constraints.

### Contradicts / Weakens

- Weakens naive “bubble detector as alpha” claims: the historical evidence is useful, but a 2017-focused sample and parameterized models are insufficient for a modern standalone trading rule.

### Transfers Across Asset Classes or Domains

Bubble-state diagnostics can become a regime label for crypto strategy validation, analogous to equity crisis-regime diagnostics in [[Observable Matrix Dynamics of Stocks]], but the mechanism and market structure differ.

### Missing Validation or Method Supplied

Provides candidate LPPL/PSY diagnostics for stress-labeling crypto regimes; still missing a modern, predeclared, fee-aware validation design.

## Framework Potential

- Candidate framework: regime-conditional distributional strategy evaluation.
- Linked notes: [[Pathwise Roughness of Bitcoin Realized Volatility]], [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]], [[Observable Matrix Dynamics of Stocks]].
- Testable composite hypothesis: crypto crash-risk filters must beat simple realized-volatility/drawdown/funding baselines in downstream net utility, not merely identify historical bubbles in-sample.
- Minimum viable validation: frozen LPPL/PSY thresholds, rolling/expanding estimation, decision-time lags, multiple market regimes, and fee/funding-aware performance attribution.
- What would falsify this connection? No incremental drawdown or utility improvement versus simple risk filters, unstable critical-time estimates, or signal timing that exits after most losses have occurred.

## Keep / Reject Decision

**Keep as foundational / outdated-watch.** It is worth preserving as a historical crypto bubble-diagnostic reference and validation caution, but it is not coding-ready.

## Related Notes

- [[Pathwise Roughness of Bitcoin Realized Volatility]]
- [[Predictive Extrema Unprofitable Policies - Binance Spot Timing Audit]]
- [[Observable Matrix Dynamics of Stocks]]
