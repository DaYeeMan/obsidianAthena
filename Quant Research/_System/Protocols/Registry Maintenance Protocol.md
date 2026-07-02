---
type: registry-maintenance-protocol
tags: [quant-research, candidate-registry, phase-2]
---

# Registry Maintenance Protocol

Use this protocol to keep [[01 Research Candidate Registry|Research Candidate Registry]] useful as the central sorting/filtering layer.

## When to Add a Candidate

Add a row when an item is one of:

- a plausible or evidence-backed strategy idea
- a foundational method/reference that should be preserved
- a practical backtest-design or risk-modeling improvement
- an important outdatedness/decay warning
- a rejected idea likely to recur and worth remembering as rejected

Do not add routine low-signal papers or generic news.

## Required Fields

Every row should include:

- Candidate
- Asset Class
- Strategy / Method Family
- Status
- Practicality
- Coding Priority
- Decay Risk
- Last Reviewed
- Primary Note
- Next Action

## Updating Existing Rows

Before adding a new row, search the registry and strategy/source notes for similar names or concepts.

Update existing rows when:

- stronger evidence appears
- evidence weakens
- a better retail proxy is identified
- a strategy becomes outdated or crowded
- a backtest spec is created
- coding priority changes

## Coding Priority Scale

- **High**: feasible to backtest soon and plausibly useful.
- **Medium**: useful after prerequisites, data acquisition, or method integration.
- **Low**: interesting but not worth immediate implementation.
- **Reference**: keep as foundational or warning, not a direct coding target.

## Decay Risk Scale

Describe decay qualitatively, not just as High/Medium/Low. Mention the specific risk:

- post-publication decay
- crowding/arbitrage
- obsolete market structure
- unrealistic costs
- inaccessible data/execution
- overfitting/model complexity
- regime dependence

## Practicality Rule

A high-quality institutional paper should not automatically become a high-priority coding target. Prefer retail-practical and retail-adaptable candidates, while preserving institutional-only papers as foundational when they improve reasoning, baselines, or cost models.
