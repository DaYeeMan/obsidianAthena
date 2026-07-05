---
type: protocol
created: 2026-07-05
last_updated: 2026-07-05
---

# Event Retention Policy

## Default policy

Use an **append-only event archive** with status-based aging. Do not delete older material events simply because they are stale.

## Keep permanently

- Material events that affected or could affect supply, demand, capacity, pricing, margins, regulation, or public-market expectations.
- Events linked to active, dormant, rejected, or resolved opportunities.
- Disproven or failed signals if they were market-moving or useful for source-quality calibration.

## Update status rather than delete

Allowed statuses: `watching`, `active`, `resolved`, `superseded`, `stale`, `rejected`.

If superseded, add a `superseded_by` wikilink. If rejected, explain why.

## Delete only

- Exact duplicates.
- Accidental test notes.
- Generic AI news with no supply-chain or investment relevance.
- Broken/empty notes created by tooling errors.

## Active views

Keep dashboard and active opportunity files curated. Archive or move non-current items to Dormant or Rejected Opportunities.
