---
type: source-note
source_kind: paper / LLM execution-policy benchmark
asset_classes: [equities, execution, market-microstructure, ai-agents]
implementation_class: foundational / institutional-only as written
importance: medium
last_reviewed: "2026-07-31"
tags: [quant-source, llm-execution, parent-orders, execution-benchmark, ai-agents]
concepts: [pace-parent-order-execution, llm-execution-agent, twap-almgren-chriss-baseline, execution-governance]
---

# Can Large Language Models Execute Parent Orders

## Citation / Link

Zane Shen, Xinli Xu, Guangyi Zhang, Jialong Chen, Jinsong Zhou, Cong Chen, Guibao Shen, Dongyu Yan, Luozhou Wang, Zhen Yang, “Can Large Language Models Execute Parent Orders?”, arXiv:2607.28410v1, submitted 2026-07-30. https://arxiv.org/abs/2607.28410v1

Semantic Scholar lookup was rate-limited during this run, so citation counts were not recorded.

## Summary

The paper presents a systematic study of large language models for parent-order execution. The proposed PACE framework decomposes execution into long-horizon planning and short-horizon execution without task-specific training. Experiments on Shenzhen Stock Exchange Level-1 data reportedly outperform TWAP, Almgren-Chriss, and learning-based baselines, with the strongest baseline beaten by 0.65 bps.

For this library, the result is a governance signal, not a retail execution prescription. Parent-order execution is a highly friction-sensitive, institutionally skewed problem; a 0.65 bps improvement can be meaningful at scale but is also vulnerable to fee, latency, queue, market-impact, and benchmark-construction assumptions. The source is useful because it forces LLM execution agents to be judged against TWAP/AC/simple learning baselines, with decision trails and fill/cost accounting.

## Core Contribution

- Extends LLM finance evaluation from security selection to execution scheduling.
- Provides a hierarchical planning/execution structure for parent orders.
- Benchmarks against TWAP, Almgren-Chriss, and learning-based execution policies.
- Reports behavior diagnostics, including confidence/performance relations and timing behavior.

## Practical Relevance

- Classification: **Plausible-to-evidence-backed at abstract level as execution-agent benchmark; foundational / institutional-only as written**.
- Institutional-only as written because parent-order execution requires high-quality intraday order/fill data, market access, scale, and strict execution governance.
- Retail adaptation is limited to a validation lens: compare any execution agent against TWAP/VWAP/arrival-price/AC baselines and include realistic fees, slippage, latency, and queue-risk stress.

## Methods and Data

- Shenzhen Stock Exchange Level-1 data.
- Parent-order splitting objective.
- PACE hierarchical framework: plan-ahead control and short-horizon execution.
- Baselines: TWAP, Almgren-Chriss, and learning-based policies.

## Leakage / Bias / Overfitting Concerns

- Abstract does not prove that Level-1 data are enough for realistic queue/fill behavior.
- 0.65 bps edge may be fragile to fees, rebates, adverse selection, latency, market-impact calibration, and order-size distribution.
- LLM policy prompts/context can introduce hidden benchmark contamination or prompt-specific overfit.
- Market-specific structure in Shenzhen may not transfer to U.S. equities, futures, or crypto.

## Transaction Cost / Capacity Treatment

The target metric is execution cost, but practical adoption requires exact fee/rebate, fill, latency, queue priority, child-order constraints, market-impact, and rejected-order treatment. Treat any LLM improvement below a few bps as fragile until independently reproduced.

## Strategy Ideas Extracted

Execution-agent benchmark checklist:

1. Always compare against TWAP/VWAP/arrival-price/Almgren-Chriss and a transparent learned policy.
2. Require predeclared order-size buckets, participation caps, latency/fill assumptions, and cost metrics.
3. Log every LLM decision, prompt, market snapshot, and child order.
4. Stress test across volatility, spread, volume, imbalance, and market-open/close regimes.
5. Reject policies whose bps improvement disappears under realistic queue/fill assumptions.

## Connections to Existing Research

### Reinforces

- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]
- [[Can Reinforcement Learning Efficiently Discover Price Manipulation]]
- [[Optimal Execution with Passive Market Impact]]
- [[Liquidity-Based Audit of Algorithmic Trading Strategies]]

### Contradicts / Weakens

Weakens generic “LLM trader” claims that do not separate what-to-trade prediction from how-to-execute cost minimization.

### Transfers Across Asset Classes or Domains

The validation checklist transfers to equities, futures, and crypto execution agents, but the model itself should not be transferred without venue-specific replay and execution-cost calibration.

### Missing Validation or Method Supplied

Supplies an LLM-agent execution benchmark category that should be evaluated by execution bps, not return-only metrics.

## Framework Potential

- Candidate framework: cost-aware decision-process diagnostics for AI execution agents.
- Linked notes: [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]], [[Can Reinforcement Learning Efficiently Discover Price Manipulation]], [[Optimal Execution with Passive Market Impact]].
- Testable composite hypothesis: LLM execution agents add value only if they beat transparent execution schedules under identical fill/cost assumptions and do not exploit simulator artifacts.
- Minimum viable validation: reproduce on public/in-house intraday data with TWAP/VWAP/AC baselines and conservative passive-fill stress.
- What would falsify this connection? The reported gain disappears with queue/fill realism, latency, or a better simple schedule baseline.

## Keep / Reject Decision

Keep as a medium-importance execution-agent benchmark. Do not promote to coding queue; use it to strengthen validation requirements if an execution agent is ever tested.

## Related Notes

- [[CLQT Cost-Aware Benchmark for LLM Portfolio-Management Agents]]
- [[Can Reinforcement Learning Efficiently Discover Price Manipulation]]
- [[Optimal Execution with Passive Market Impact]]
