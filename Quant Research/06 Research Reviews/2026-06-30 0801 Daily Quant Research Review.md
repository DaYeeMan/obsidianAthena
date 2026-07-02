---
type: daily-quant-research-review
created: 2026-06-30 0801 EDT
asset_focus: [equities, options, crypto]
tags: [quant-research, daily-review, anomaly-decay, ai-factor, ai-agents]
---

# 2026-06-30 0801 Daily Quant Research Review

## Run Context

Pre-run feeds and arXiv scans were treated as discovery leads only. Existing registry context already contained the morning additions for microstructure diagnostics, liquidity audit, distributional forecasting, and CLQT. This run therefore focused on the one genuinely new feed item plus a newly surfaced arXiv asset-pricing paper.

## Items Screened

### 1. Quantpedia — Guardrails Make the Researcher: AI agent replication of nine equity anomalies

- Link: https://quantpedia.com/guardrails-make-the-researcher-what-an-ai-agent-got-right-and-wrong-replicating-nine-equity-anomalies/
- Classification: **Evidence-backed as practitioner replication/governance warning**.
- Practicality: **foundational**.
- Decision: **Keep** as a source note: [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]].
- Why it matters: the extracted article text says an autonomous agent replicated nine published U.S.-equity anomalies on survivorship-free data; faithful out-of-sample builds did not survive, and one apparent survivor was a construction error caught by the process.
- Research implication: use AI agents for replication only with guardrails: survivorship-free data, post-publication splits, independent implementation review, transaction-cost stress, and error traps.
- Decay / failure modes: old cross-sectional anomalies remain high-decay candidates; agent-generated code can create false positives through construction mistakes, not just statistical overfitting.

### 2. Borri, Liu, Tsyvinski — AI Premium

- Link: https://arxiv.org/abs/2606.30583v1
- Classification: **Plausible but untested**.
- Practicality: **institutional-only as written / retail-adaptable via proxies**.
- Decision: **Keep** as a source note: [[AI Premium]].
- Abstract claim: an AI consumption factor built from proprietary OpenRouter usage data predicts firm returns; the paper reports a value-weighted high-minus-low AI-beta strategy earning 64.1 bps per week.
- Research implication: potentially important thematic asset-pricing lead, but not directly implementable without proprietary data. A local test should use only timestamped public AI-exposure proxies and control for sector, mega-cap tech beta, momentum, size, quality, valuation, and crowding.
- Decay / failure modes: proprietary alternative-data leakage, factor crowding, AI narrative exposure masquerading as momentum/growth duration, and publication decay.

### 3. Asymmetric Nonlinear Return Extrapolation and Optimal Portfolio Choice under Stochastic Volatility

- Link: https://arxiv.org/abs/2606.10805v2
- Classification: **Foundational behavioral model; not added**.
- Practicality: **foundational / institutional math**.
- Rationale: useful for understanding nonlinear extrapolative beliefs under stochastic volatility, but the abstract is primarily theoretical and does not provide a retail-testable signal beyond existing behavioral extrapolation/momentum literature.

### 4. Large and Deep Factor Models

- Link: https://arxiv.org/abs/2402.06635v3
- Classification: **Evidence-backed/foundational ML asset-pricing method; not added this run**.
- Practicality: **foundational / institutional-only unless simplified**.
- Rationale: important Bryan Kelly et al. factor-model work, but not newly actionable relative to the current registry’s ML-governance focus. Candidate for a future synthesis pass on “deep factor models versus simple characteristic baselines.”

### 5. Adjacent-domain method leads

- Doubly Robust Adaptive Conformal Inference for Causal Effects Under Temporal Dependence and Discovering the Kalman-Bucy-Koopman Filter were screened as method leads only.
- Decision: no source notes today. DR-ACI may later connect to event-study inference under temporal dependence; KBK filtering may later connect to nonlinear latent-state filtering. Neither was translated into a market hypothesis in this run.

## Candidate Registry Updates

Added two tracked rows:

1. **AI-agent guarded anomaly replication and decay audit** — foundational governance/decay warning.
2. **AI consumption beta / AI premium proxy factor** — plausible but untested, institutional-only as written with possible retail proxy.

No existing rows were promoted to the coding-ready queue.

## Literature Connections / Framework Leads

### Reinforces

- [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]] reinforces [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]: agent workflows need time-gating, audit trails, and error detection.
- It also reinforces [[Liquidity-Based Audit of Algorithmic Trading Strategies]] and [[The Bounce Has No Direction - Sign Magnitude and Microstructure of Equity Return Predictability]] by emphasizing that implementation and microstructure details can flip apparent alpha into non-alpha.

### Contradicts / Weakens

- Weakens naive published-anomaly mining and any workflow that promotes equity factors without post-publication decay and survivorship-free replication.
- [[AI Premium]] weakens simple “buy AI winners” narratives unless the return premium survives sector, momentum, valuation, and mega-cap concentration controls.

### Transfers Across Asset Classes

- The replication-guardrail block should transfer to crypto factor discovery and options-volatility strategies: no candidate should enter the coding queue without a clean data-timing audit, cost model, and post-discovery/market-structure regime split.

### Missing Link Supplied

- Quantpedia supplies a practical example linking the existing LLM-agent benchmark note to real anomaly-replication governance.
- AI Premium supplies a possible thematic alternative-data factor, but the missing link is a public, timestamped proxy that does not simply reproduce tech momentum.

## Framework Potential

- Updated existing framework: **Cost-aware decision-process diagnostics** should explicitly include AI-agent anomaly-replication guardrails.
- New open question added for the AI premium proxy problem.
- No new framework row was created; the connection is better folded into existing governance/diagnostic framework for now.

## Coding Queue Review

Unchanged. Neither item has enough fully specified rules, data, costs, and validation design to enter [[09 Coding-Ready Backtest Queue]]. The SPX put-writing and decision-aware covariance items remain the highest coding priorities.

## Practical Next Actions

1. Add a standard “replication guardrail block” to future anomaly backtest specs.
2. For AI Premium, only proceed if a public timestamped AI-exposure proxy is defined and tested sector-neutral with factor controls.
3. During weekly synthesis, consider a framework thread: “AI-assisted research quality control = CLQT TimeGate + anomaly replication guardrails + liquidity/cost diagnostics.”
