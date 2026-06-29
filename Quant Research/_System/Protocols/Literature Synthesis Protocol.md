---
type: literature-synthesis-protocol
tags: [quant-research, synthesis, frameworks]
---

# Literature Synthesis Protocol

Use this protocol when a cron job or interactive session is asked to find non-obvious connections in the quant research library.

## Goal

Create falsifiable research frameworks from multiple papers, strategy notes, source notes, and adjacent-domain ideas. The goal is not novelty for its own sake; it is to create better strategy hypotheses, validation frameworks, cost models, risk controls, and portfolio-construction methods.

## Inputs

Review:

1. [[Research Candidate Registry]]
2. [[09 Coding-Ready Backtest Queue]]
3. recent daily research reviews
4. source notes and strategy notes
5. [[07 Literature Synthesis/Framework Candidate Registry|Framework Candidate Registry]]
6. [[07 Literature Synthesis/Open Research Questions|Open Research Questions]]
7. selected adjacent-domain leads from ML, statistics, signal processing, control theory, network science, causal inference, operations research, ecology/epidemiology, physics/complex systems, and decision theory.

## Connection Types

Classify each useful connection as one or more of:

- **reinforces**: new evidence supports an existing candidate;
- **contradicts**: new evidence weakens an existing candidate;
- **missing validation**: supplies a needed backtest, cost, robustness, or decision-evaluation method;
- **method transfer**: a method from one asset class/domain may apply to another;
- **mechanism bridge**: a shared causal or behavioral mechanism connects otherwise separate papers;
- **framework candidate**: multiple ideas combine into a reusable falsifiable framework;
- **decay warning**: newer evidence suggests a model/strategy is stale, crowded, or cost-infeasible.

## Framework Admission Criteria

Add a framework only when it has:

1. at least two linked notes/sources;
2. a mechanism, not only a topic label;
3. a falsifiable hypothesis;
4. a minimum viable validation or backtest design;
5. explicit costs/data/leakage/failure-mode concerns;
6. a clear next action.

## Adjacent-Domain Rule

Include ideas from other fields only when they improve a quant research task:

- signal extraction or filtering;
- regime/change-point detection;
- network/contagion modeling;
- causal validation;
- uncertainty estimation;
- decision-making under risk;
- optimization under costs/constraints;
- robustness/stress testing.

Reject domain analogies that remain metaphorical or cannot be translated into data, rules, or validation tests.

## Output Sections

A synthesis review should include:

- Framework candidates added/updated
- Cross-paper connection table
- Adjacent-domain imports worth tracking
- Contradictions/decay warnings
- Open research questions added/retired
- Registry/coding queue changes
