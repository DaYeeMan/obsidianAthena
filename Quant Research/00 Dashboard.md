---
type: quant-research-dashboard
created: 2026-06-28
profile: quant-researcher
tags: [quant-research, dashboard]
---

# Quant Research Dashboard

This is the user-facing entry point for the Hermes `quant-researcher` library.

## Primary Views

- [[01 Research Candidate Registry]] — cross-library sortable/filterable strategy and method registry
- [[09 Coding-Ready Backtest Queue]] — ideas ready or nearly ready to implement
- [[02 Strategy Ideas/Strategy Index|Strategy Ideas]] — detailed strategy hypotheses
- [[04 Backtest Specs/Backtest Spec Index|Backtest Specs]] — coding-ready research designs
- [[01 Sources/Source Index|Sources]] — paper/source notes
- [[06 Research Reviews/Research Review Index|Daily Research Reviews]] — scheduled research collection logs
- [[05 Implementation Notes/Implementation Index|Implementation Notes]] — data, engineering, and coding-time support

## Current Highest-Priority Candidate

- [[SPX Short-Dated Put-Writing with VIX and Fractional-Kelly Sizing]]

## Research Mission

Maintain an evidence-based, implementable systematic-trading research library for equities, options, and crypto.

The library supports both:

- event/opportunity triage from other Hermes profiles
- coding-time help when designing, implementing, or validating a strategy

## Standards

Accept ideas only when they can plausibly become testable, statistically defensible strategies.

Prioritize:
- academic and empirical finance literature
- market microstructure and event studies
- factor and behavioral anomaly research
- volatility/risk-premia research
- credible ML/AI papers with temporal validation and leakage controls
- reproducible practitioner research with code/data/methodology

Reject or quarantine:
- guru-style trading content
- unsupported win-rate claims
- vague price-action folklore
- strategies without sample size, costs, or data requirements
- methods requiring institutional-only infrastructure unless adapted into a retail-practical proxy

## Practicality Lens

Each candidate should be tagged by implementation class:

- `retail-practical`: feasible with common data/tools and realistic costs
- `retail-adaptable`: original form is institutional/heavy, but a simpler proxy may be testable
- `institutional-only`: requires privileged data, infrastructure, execution, scale, or balance sheet
- `foundational`: important for understanding or model design even if not directly tradable
- `outdated-watch`: may have decayed, been arbitraged, or been superseded

## Hidden System Files

Guidelines, protocols, templates, scripts, and frameworks live under:

- `Quant Research/_System/`

That folder is still present in the vault for Hermes to read, but it is excluded from Obsidian search/graph so it does not clutter your visual research graph.
