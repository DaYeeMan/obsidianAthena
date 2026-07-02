---
type: source-note
source_kind: paper
asset_classes: [equities, ai, thematic-factor]
implementation_class: institutional-only / retail-adaptable
importance: medium
last_reviewed: "2026-06-30"
tags: [quant-source, asset-pricing, ai-factor, thematic-risk-premium, proprietary-data]
concepts: [ai-beta, alternative-data, thematic-premium, factor-replication]
---

# AI Premium

## Citation / Link

Nicola Borri, Yukun Liu, Aleh Tsyvinski, “AI Premium,” arXiv:2606.30583v1, 2026-06-29. https://arxiv.org/abs/2606.30583v1

## Summary

The paper constructs an AI consumption factor from OpenRouter’s licensed proprietary dataset covering realized AI consumption across more than four hundred LLMs. The abstract reports that firms with higher return comovement to the AI factor subsequently earn higher returns, with a value-weighted long-short strategy earning 64.1 bps per week. The premium is concentrated in intensive/frontier-oriented AI use and extends beyond technology firms.

## Core Contribution

- Translates high-frequency AI usage data into an asset-pricing factor.
- Estimates firm-level AI betas from stock return comovement with that factor.
- Claims a large subsequent-return premium associated with high AI beta.
- Links market-implied AI exposure to occupation/task characteristics.

## Practical Relevance

- Classification: **Plausible but untested; institutional-only as written / retail-adaptable only via proxies**.
- The proprietary OpenRouter dataset is the main implementation barrier.
- Retail-adaptable proxy research could test whether public AI exposure proxies predict returns after controlling for sector, size, momentum, quality, valuation, and the broad AI trade.

## Methods and Data

Abstract-level details:

- 380 trillion tokens of realized AI consumption,
- 400+ LLMs,
- about 2% of current global monthly AI token consumption,
- AI factor constructed from growth in tokens, dollars, and users,
- firm-level AI betas estimated from return comovement,
- long-short portfolio sorted on AI beta.

Possible local proxy inputs:

- public company AI revenue/exposure disclosures from filings and earnings transcripts,
- AI ETF and basket returns as noisy tradable factors,
- supplier/customer exposure to AI infrastructure,
- job-posting/task-exposure datasets if available,
- sector-neutral and industry-neutral controls.

## Leakage / Bias / Overfitting Concerns

- Proprietary alternative data may be unavailable, nonstationary, revised, or sample-selected.
- AI beta estimated from returns can capture momentum, mega-cap tech exposure, growth duration, or sentiment rather than independent AI consumption risk.
- A very large weekly long-short premium demands replication with strict chronology, factor controls, and post-publication monitoring.
- The AI theme is crowded; publication may accelerate decay.

## Transaction Cost / Capacity Treatment

Equity long-short implementation needs:

- turnover and rebalance frequency from the original paper,
- borrow availability/cost for shorts,
- liquidity filters,
- sector/industry neutrality constraints,
- market-impact estimates for crowded AI baskets.

## Strategy Ideas Extracted

### AI-exposure proxy factor screen

Hypothesis: Firms with high exposure to frontier AI adoption earn a premium not fully explained by sector, size, momentum, valuation, profitability, investment, or broad tech beta.

Minimum viable retail backtest:

1. Build monthly/quarterly public AI-exposure proxies from filings/transcripts or public AI-related baskets.
2. Estimate lagged exposure only from information available at the portfolio formation date.
3. Sort U.S. equities into sector-neutral high/low AI-exposure portfolios.
4. Compare against controls: tech sector, Nasdaq beta, momentum, size, quality, value, and earnings-growth proxies.
5. Include transaction costs, borrow constraints, and post-2022 / post-publication splits.

## Connections to Existing Research

### Reinforces

- The need for Cost-aware decision-process diagnostics because alternative-data factors are vulnerable to hidden leakage and crowding.

### Contradicts / Weakens

- Weakens simplistic “AI stock basket” narratives: a true premium must survive factor controls and sector neutrality.

### Transfers Across Asset Classes or Domains

- Similar alternative-data beta construction could be tested for crypto AI tokens or AI infrastructure suppliers, but only after liquidity and survivorship controls.

### Missing Validation or Method Supplied

- Supplies a potential empirical asset-pricing candidate, but the original data path is not retail-practical.

## Framework Potential

- Candidate framework: Alternative-data thematic-premium replication discipline.
- Linked notes: [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]], [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]].
- Testable composite hypothesis: public proxy factors can approximate proprietary thematic betas only if they retain predictive power after neutralization and strict information timing.
- Minimum viable validation: sector-neutral AI-exposure proxy backtest using timestamped disclosures and public factor controls.
- What would falsify this connection? The proxy premium disappears after sector/momentum controls or is concentrated entirely in a few mega-cap tech names.

## Keep / Reject Decision

**Keep** as a medium-priority, high-skepticism asset-pricing lead. Do not treat as coding-ready until a public proxy and full control set are specified.

## Related Notes

- [[2026-06-30 0801 Daily Quant Research Review]]
- [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]]
