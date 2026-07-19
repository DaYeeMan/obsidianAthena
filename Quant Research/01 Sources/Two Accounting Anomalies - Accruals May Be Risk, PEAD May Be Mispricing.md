---
type: source-note
source_kind: practitioner summary of paper
asset_classes: [equities, factor-research, accounting-anomalies]
implementation_class: retail-adaptable / foundational
importance: high
last_reviewed: "2026-07-18"
tags: [quant-source, equities, accounting-anomalies, accruals, PEAD, factor-validation, anomaly-decay]
concepts: [accrual anomaly, post-earnings-announcement drift, multiperiod asset pricing, accounting hedge factor, anomaly reclassification]
---

# Two Accounting Anomalies - Accruals May Be Risk, PEAD May Be Mispricing

## Citation / Link

Larry Swedroe, “Two Accounting Anomalies: One May Be Risk, the Other Is Mispricing,” Alpha Architect, 2026-07-17. https://alphaarchitect.com/accounting-anomalies/

Discusses Stephen Penman and Julie Lei Zhu, “Explaining Two Prominent Accounting Pricing Anomalies: The Accrual Anomaly and the Post-Earnings-Announcement Drift,” June 2026, sample April 1982–March 2022.

## Summary

The Alpha Architect summary reports that Penman and Zhu revisit the accrual anomaly and post-earnings-announcement drift (PEAD) using an intertemporal asset-pricing framing instead of only one-period CAPM/Fama-French-style benchmarks. Their key modeling step is a two-factor model: the market portfolio plus a fundamental hedge factor constructed from accounting information. The hedge factor is an annually rebalanced long-short portfolio intended to capture exposure to future earnings risk.

The practical interpretation is asymmetric across the two anomalies: accrual-sorted returns may be explained by priced exposure to future-earnings risk, while PEAD remains harder to explain and is more consistent with delayed information incorporation / mispricing under the summary’s description.

## Core Contribution

- Separates “published accounting anomaly” into two different research buckets: accruals as possible risk compensation, PEAD as more likely behavioral/mispricing evidence.
- Shows that benchmark choice can materially change anomaly interpretation; a one-period factor failure is not automatically alpha.
- Reinforces the need to test candidate anomalies under mechanism-relevant benchmarks, not only generic factor regressions.
- Provides a concrete prompt for old-anomaly decay audits: check whether the anomaly is still abnormal after post-publication splits, transaction costs, modern accounting data availability, and a fundamental hedge/risk benchmark.

## Practical Relevance

- Classification: **Evidence-backed as a practitioner-reviewed paper summary; retail-adaptable / foundational**.
- Not immediately coding-ready, because the exact hedge-factor construction from the paper must be specified before replication.
- Most useful for anomaly triage: PEAD-like event drift may deserve more attention than generic accrual spreads, but both require conservative post-publication and cost tests.
- Retail adaptation: test PEAD/accrual signals on a liquid U.S. equity universe using public filing and earnings-announcement timestamps; include standard factors, sector/industry controls, size/liquidity filters, post-publication splits, and conservative spread/slippage assumptions.

## Methods and Data

From the summary:

- U.S. equity sample from April 1982 through March 2022.
- Portfolios sorted by earnings-to-price, accruals, momentum, standardized unexpected earnings / PEAD, revenue surprises, and analyst forecast revisions.
- Two-factor model: market portfolio plus annually rebalanced accounting-based fundamental hedge factor that is long firms with high implied risk to future earnings and short firms with low implied risk.
- Compares whether anomaly returns are explained by exposure to the hedge factor.

## Leakage / Bias / Overfitting Concerns

- Need original paper details before implementation: exact accounting variables, portfolio formation dates, announcement dates, lag conventions, rebalancing rules, and hedge-factor construction.
- Compustat/CRSP-style data require survivorship-free universes and delisting-return handling.
- Accounting data availability is not instantaneous; use public filing/earnings availability timestamps plus conservative execution lags.
- PEAD event studies require clean earnings-announcement timestamps and avoidance of lookahead in SUE/revisions.
- Post-publication decay is central: these are old, well-known anomalies, so modern net returns can be much weaker than full-sample evidence.

## Transaction Cost / Capacity Treatment

Not directly established from the summary. Any retail test should include:

- liquidity and price filters to avoid microcap accounting traps,
- estimated bid/ask and slippage by size/liquidity bucket,
- turnover decomposition for annual accrual sorts versus event-driven PEAD trades,
- shorting/borrow constraints for long-short portfolios,
- tax/implementation differences between monthly/quarterly event drift and annual accounting sorts.

## Strategy Ideas Extracted

1. **PEAD-first anomaly replication:** long positive standardized unexpected earnings / short negative SUE after earnings announcement, restricted to liquid names, with holding windows such as 1, 5, 20, and 60 trading days; compare post-cost returns against momentum, size, value, quality, and industry controls.
2. **Accrual anomaly risk-audit:** replicate accrual sorts, then add a fundamental hedge factor or proxy for future-earnings risk; downgrade if excess returns vanish after the benchmark and costs.
3. **Anomaly triage filter:** before coding any old accounting anomaly, ask whether the signal is a risk exposure, stale accounting-data artifact, post-publication-decayed anomaly, or true delayed information incorporation.

## Connections to Existing Research

### Reinforces

- [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]] — reinforces the need for independent replication, survivorship-free data, post-publication splits, and implementation guardrails before trusting anomaly claims.
- [[A Cap-Axis Integral Diagnostic of Factor Models]] — another reason to diagnose factor/anomaly residuals along size/cap axes and other omitted-risk dimensions.

### Contradicts / Weakens

- Weakens naive “accrual anomaly as pure mispricing” interpretations if the accounting hedge factor explains the spread.
- Does not weaken PEAD as much; under the summary, PEAD remains a more plausible delayed-information/mispricing candidate.

### Transfers Across Asset Classes or Domains

The benchmark-first lesson transfers to crypto and options: a return pattern should be tested against the mechanism-relevant risk/cost state before being labeled alpha.

### Missing Validation or Method Supplied

Adds a concrete omitted-risk benchmark idea for accounting anomalies: an accounting/fundamental hedge factor tied to future earnings risk.

## Framework Potential

- Candidate framework: benchmark-first anomaly reclassification and decay audit.
- Linked notes: [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]], [[A Cap-Axis Integral Diagnostic of Factor Models]].
- Testable composite hypothesis: old accounting anomalies split into risk-compensation and mispricing components once post-publication periods, realistic frictions, omitted-risk benchmarks, and liquidity/cap-rank diagnostics are applied.
- Minimum viable validation: replicate accrual and PEAD portfolios using point-in-time data; run full-sample and post-publication windows; add standard factors, cap-axis diagnostics, liquidity/cost stress, and accounting hedge-factor proxy.
- What would falsify this connection? Accrual and PEAD spreads both remain equally strong after the hedge factor, modern-period costs, cap/liquidity filters, and event-time leakage controls; or neither survives robust replication.

## Keep / Reject Decision

Keep as a high-value foundational/practitioner source. Do not promote to coding queue until the original paper’s hedge-factor construction and exact portfolio rules are inspected.

## Related Notes

- [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]]
- [[A Cap-Axis Integral Diagnostic of Factor Models]]
