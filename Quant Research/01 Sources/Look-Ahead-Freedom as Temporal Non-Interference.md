---
type: source-note
source_kind: paper
asset_classes: [portfolio, backtesting, ai-agents, software-verification]
implementation_class: foundational
importance: high
last_reviewed: "2026-07-07"
tags: [quant-source, backtesting, lookahead-bias, leakage, agentic-pipelines, verification]
concepts: [temporal-non-interference, time-gated-data, point-in-time-joins, leakage-checking]
---

# Look-Ahead-Freedom as Temporal Non-Interference

## Citation / Link

Xavier Fonseca, “Look-Ahead-Freedom as Temporal Non-Interference: A Verifiable Correctness Property for Backtesting and Agentic Trading Pipelines,” arXiv:2607.04958v1, 2026-07-06. https://arxiv.org/abs/2607.04958v1

## Summary

The paper formalizes look-ahead freedom as a temporal non-interference property over a time-indexed information lattice. Instead of relying only on channel-specific recipes for windows, joins, point-in-time reads, or empirical leak detectors, it separates each datum's availability time from its reference time and asks whether future information can influence present decisions. The abstract reports a decidability boundary: when availability can depend on data values, freedom from leakage is undecidable; for the value-independent fragment covering common windowing, resampling, joins, point-in-time/vintage reads, and agentic retrieval, a sound linear-time type-and-effect checker is possible.

## Core Contribution

- Recasts look-ahead bias as a formal correctness property rather than a checklist item.
- Distinguishes data availability time from reference/economic time, which is directly relevant to fundamentals, revisions, filings, option chains, alternative data, news, and agent retrieval.
- Claims a sound decidable checker for a practical fragment of common quant pipelines.
- Explicitly includes agentic trading/research pipelines, where retrieval tools can silently introduce future information.

## Practical Relevance

- Classification: **Evidence-backed as verification methodology / foundational** at abstract level.
- Not a trading signal; it is a backtest-governance and pipeline-design reference.
- High relevance to any local backtest harness, especially ML/AI workflows and factor research where point-in-time joins and vintage data are common failure modes.
- Retail use does not require the full formal system at first: add mandatory fields for `available_at`, `observed_at/reference_time`, and `decision_time` to datasets and pipeline artifacts.

## Methods and Data

Abstract-level details:

- temporal non-interference over time-indexed information lattices,
- pipeline calculus distinguishing availability from reference time,
- undecidability result for value-dependent availability,
- linear-time type-and-effect system for value-independent pipeline fragments,
- artifact evaluation with planted leak detection.

## Leakage / Bias / Overfitting Concerns

- The paper itself is a guardrail; practical risk is incomplete adoption where only some data sources carry availability metadata.
- Value-dependent availability remains hard: for example, news visibility, vendor corrections, exchange halts, or API retrieval failures may depend on market state.
- A checker can verify only the model of the pipeline it sees; manual spreadsheet steps, cached files, and agent-created summaries can still leak.

## Local Use / Backtest Translation

Minimum viable implementation for the local research stack:

1. Require every dataset or feature table to carry `available_at`, `reference_time`, and `decision_time` semantics.
2. For joins, assert `available_at <= decision_time` for every feature consumed by the decision rule.
3. For model training, freeze train/validation/test splits by decision time, not by row order or publication date alone.
4. For agentic retrieval, log query time, source URL, retrieved timestamp, and any cached version.
5. Include a leakage verdict in the standard cost/regime/liquidity/decision audit block.

## Connections to Existing Research

### Reinforces

- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]: TimeGate and audit-trail requirements become a broader formal non-interference requirement.
- [[Guardrails Make the Researcher - AI Agent Replication of Nine Equity Anomalies]]: anomaly replication failures need explicit point-in-time and survivorship checks.
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]: cost and liquidity diagnostics should be computed only from information available at the decision epoch when used for sizing.

### Framework Potential

- Candidate framework: Cost-aware decision-process diagnostics.
- Testable composite hypothesis: strategies that pass explicit time-availability checks will show lower apparent-to-realized performance decay than strategies validated only by conventional split rules.
- Minimum viable backtest: instrument the next backtest report with a `time_availability_check` table and planted-leak negative controls.
- Falsification: checker overhead is high but catches no additional leaks beyond simple point-in-time assertions across several diverse backtests.
