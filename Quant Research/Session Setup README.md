---
type: session-setup-readme
created: 2026-06-29
tags: [quant-research, hermes, setup]
---

# Quant Research System Setup README

This note summarizes the quant-research system created for the Hermes `quant-researcher` profile during this setup session.

## Goal

Build a continuously maintained, Obsidian-backed quantitative research library focused on evidence-based, implementable systematic trading ideas.

The system is designed so the user can come to this profile when:

- another Hermes profile surfaces a market event or opportunity,
- the user wants research support while coding/backtesting a strategy,
- the user wants evidence-backed quantitative strategy ideas with clear data, math, and validation requirements.

## Scope

Primary asset classes:

- equities
- options
- crypto

Research themes:

- short/medium-horizon event strategies
- factor and empirical asset-pricing research
- ML/AI forecasting methods
- regime detection and risk allocation
- portfolio/risk construction
- volatility and options risk premia
- crypto market structure
- transaction-cost, slippage, and capacity modeling

## Core Obsidian Files

Main dashboard:

- [[00 Dashboard]]

Main registry:

- [[01 Research Candidate Registry]]

Coding queue:

- [[09 Coding-Ready Backtest Queue]]

Important folders:

- [[01 Sources/Source Index|Sources]]
- [[02 Strategy Ideas/Strategy Index|Strategy Ideas]]
- [[03 Event-to-Strategy Maps/Event-to-Strategy Index|Event-to-Strategy Maps]]
- [[04 Backtest Specs/Backtest Spec Index|Backtest Specs]]
- [[05 Implementation Notes/Implementation Index|Implementation Notes]]
- [[06 Research Reviews/Research Review Index|Research Reviews]]

## Hidden System Folder

Internal protocol/template/framework/script files were moved under:

`Quant Research/_System/`

This folder remains in the vault so Hermes can read it, but it is excluded from Obsidian graph/search via:

- `.obsidian/app.json` → `userIgnoreFilters: ["Quant Research/_System/"]`
- `.obsidian/graph.json` → `search: -path:"Quant Research/_System"`

The folder may still appear in the file explorer depending on Obsidian settings, but it should not clutter graph/search views.

## Research Classification System

Every candidate should be classified by evidence quality:

- Evidence-backed
- Plausible but untested
- Speculative
- Low quality
- Rejected

Every candidate should also be classified by practicality:

- retail-practical
- retail-adaptable
- institutional-only
- foundational
- outdated-watch

This distinction is important because some high-quality institutional research is not directly practical for retail implementation, while some simpler ideas may be more useful for near-term backtesting.

## Candidate Registry

The candidate registry tracks research ideas across time with fields for:

- candidate
- asset class
- strategy / method family
- status
- practicality
- coding priority
- decay risk
- last reviewed
- primary note
- next action

The registry is intended to change over time as new evidence appears, strategies decay, candidates become coding-ready, or ideas are rejected.

## Coding-Ready Backtest Queue

The coding queue tracks ideas that are ready or nearly ready to implement. It is separate from the broader registry because not every useful research item should become code immediately.

Initial queue items included:

- SPX/SPXW short-dated put-writing with VIX/fractional-Kelly sizing
- decision-aware covariance metrics for GMVP backtests
- forecast-uncertainty-aware ML sizing

## Scheduled Hermes Jobs

Two cron jobs were created.

### Daily Quant Research Collector

- Job name: `daily-quant-research-collector`
- Job ID: `1c3a1db27acf`
- Schedule: daily at 8:00 AM local time
- Delivery: Discord
- Model target: `gpt-5.4`, medium reasoning via profile config

Purpose:

- discover credible new or newly relevant quant research,
- classify candidates by evidence and practicality,
- identify outdated/decayed models and strategies,
- preserve foundational research,
- write daily review notes,
- update the candidate registry,
- update the coding queue when something becomes implementation-ready.

### Weekly Strategy/Model Decay Review

- Job name: `weekly-quant-strategy-decay-review`
- Job ID: `810de174cd0f`
- Schedule: Sundays at 9:00 AM local time
- Delivery: Discord
- Model target: `gpt-5.4`, medium reasoning via profile config

Purpose:

- review the registry and recent research notes,
- upgrade/downgrade candidates,
- flag outdated strategies,
- preserve foundational items,
- adjust coding priorities,
- update the coding queue.

## Source Ingestion

A stdlib-only feed scanner was created because `blogwatcher-cli` was not installed yet:

`Quant Research/_System/Scripts/feed_scan.py`

Verified feed sources:

- Quantocracy
- Alpha Architect
- Robot Wealth
- Quantpedia
- arXiv q-fin trading / statistical finance / portfolio management query

The feed scanner is a fallback/source-lead tool. Feed entries are not treated as evidence unless they pass the research-quality filters.

## Blogwatcher-CLI Installation Notes

`blogwatcher-cli` is not currently installed. On this Windows machine, Docker is available but Go was not found during setup.

Recommended options:

1. Docker, no native install:
   - Use the published container with a persistent database volume.
2. Go install, if Go is installed later:
   - `go install github.com/JulienTant/blogwatcher-cli/cmd/blogwatcher-cli@latest`
3. Manual release binary:
   - Check https://github.com/JulienTant/blogwatcher-cli/releases for a Windows binary if available.

Until Blogwatcher is installed, the custom feed scanner provides basic RSS/Atom coverage.

## Hermes Model Configuration

The quant-researcher profile was updated to use:

- model: `gpt-5.4`
- provider: `openai-codex`
- reasoning effort: `medium`

The scheduled cron jobs were also pinned to `openai-codex / gpt-5.4`.

A fresh Hermes session or gateway restart may be required for global config changes to affect already-running interactive/gateway processes.

## Current State

The system now has:

- an Obsidian dashboard,
- a research candidate registry,
- a coding-ready queue,
- daily research collection,
- weekly decay review,
- source ingestion protocols,
- data-source notes,
- hidden protocol/template/system files,
- Discord delivery for scheduled outputs,
- model target set to GPT-5.4 medium.

## Next Optional Improvements

Potential future additions:

- install `blogwatcher-cli` for persistent RSS read/unread state,
- add Dataview-compatible metadata views,
- add detailed option/crypto data-vendor comparison notes,
- create formal backtest specs for the top coding queue items,
- convert this operating procedure into a reusable Hermes skill.
