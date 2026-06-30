---
type: source-note
source_kind: paper
asset_classes: [portfolio, ml, ai-agents]
implementation_class: foundational
importance: medium
last_reviewed: "2026-06-30"
tags: [quant-source, llm-agents, portfolio-management, benchmark, leakage, transaction-costs]
concepts: [closed-loop-evaluation, timegate, audit-trail, strategy-consistency]
---

# CLQT - Cost-Aware Benchmark for LLM Portfolio-Management Agents

## Citation / Link

Bo Qu, Mingguang Chen, “CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent Benchmark for Diagnostic Evaluation of LLM Portfolio-Management Agents,” arXiv:2606.29771v1, 2026-06-29. https://arxiv.org/abs/2606.29771v1

## Summary

CLQT reframes evaluation of LLM portfolio-management agents as diagnostic process evaluation rather than a return-ranking contest. The abstract emphasizes temporal gating, transaction and financing costs, strategy-consistency scoring, memory, tool use, and recompute-verifiable audit trails.

## Core Contribution

- Moves agent evaluation from “who had the highest return in one path?” to “where did the decision process succeed or fail?”
- Explicitly controls for look-ahead leakage with a TimeGate.
- Requires closed-loop decisions, execution modeling, and auditability.

## Practical Relevance

- Classification: **foundational**.
- Not a tradable strategy. Useful as a benchmark-design reference for any future LLM-assisted research or portfolio agent workflow.
- Retail relevance is mostly in preventing false confidence from leaky LLM trading demos.

## Methods and Data

Abstract-level details only: agents run a gather/synthesize/allocate/execute/reflect cycle; each decision round is sealed into a hash chain; evaluation includes cost-aware and strategy-consistency metrics.

Local adaptation:

- timestamp all data available to an agent,
- forbid future revisions/news leakage,
- store decision logs and prompts,
- compare against fixed-rule baselines and cost-aware portfolios.

## Leakage / Bias / Overfitting Concerns

This paper is mainly a leakage warning. LLM agents are highly prone to hidden lookahead, benchmark contamination, prompt drift, and narrative overfitting. A closed-loop benchmark should not be trusted unless every input is time-gated.

## Transaction Cost / Capacity Treatment

The abstract explicitly includes transaction and financing costs. Any local agent benchmark should include spreads, commissions, turnover, financing/cash, and failed-execution assumptions.

## Strategy Ideas Extracted

No direct strategy. Use as a governance framework if the user later tests LLM portfolio agents or AI-assisted trade selection.

## Connections to Existing Research

### Reinforces

- [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]]: evaluate the decision, not only prediction quality.
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]: cost-aware diagnostics should be part of model/agent evaluation.

### Contradicts / Weakens

- Weakens return-only LLM trading benchmark claims and agent demos lacking temporal gating and cost modeling.

### Transfers Across Asset Classes or Domains

- Applies to equities, crypto, and options agent workflows as an evaluation protocol, not asset-specific alpha.

### Missing Validation or Method Supplied

- Supplies an audit-trail/TimeGate design pattern for any Hermes-driven research automation that emits trade recommendations.

## Framework Potential

- Candidate framework: decision-process-first model evaluation.
- Linked notes: [[Decision Geometry of Covariance Estimation for GMVP under Heavy Tails]], [[Liquidity-Based Audit of Algorithmic Trading Strategies]], [[Heads Not Backbones - Output Heads Dominate Architectures on Fat-Tailed Returns]].
- Testable composite hypothesis: decision-process diagnostics and cost-aware audit trails reduce false-positive strategy selection more than return-only benchmark rankings.
- Minimum viable validation: replay candidate strategies through frozen timestamped inputs and compare process score vs realized post-cost performance.
- What would falsify this connection? Diagnostic scores fail to predict out-of-sample degradation or identify known leakage/cost failures.

## Keep / Reject Decision

**Keep** as a foundational LLM/agent benchmark and leakage-control reference.

## Related Notes

- [[2026-06-30 0044 Daily Quant Research Review]]
