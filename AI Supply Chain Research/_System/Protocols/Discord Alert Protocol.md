---
type: protocol
created: 2026-07-05
last_updated: 2026-07-05
---

# Discord Alert Protocol

Discord channel target: `discord:1522119384477208596`

Send an alert only when a high-signal event appears or a major update changes an active opportunity.

## Alert-worthy events

- Capacity/bottleneck inflection likely to affect shipment expectations.
- Supplier/customer relationship change with public-market exposure.
- Meaningful capex/procurement/funding signal.
- Regulatory/export-control shift affecting supply, demand, or pricing.
- Datacenter power/cooling/construction constraint or relief that affects deployment capacity.
- Strong contradiction to the existing supply-chain model.
- Event that creates or materially updates a discretionary catalyst or quant-testable hypothesis.

## Do not alert

- Routine database maintenance.
- Generic AI product news.
- Low-quality rumors without corroboration.
- Minor reiterations of known information.

## Alert format

```md
[AI Supply Chain Alert] <short title>

Facts:
- ...

Why it matters:
- ...

Affected public exposures:
- ...

Opportunity angle:
- Discretionary: ...
- Quant-testable: ...

Confidence: low/medium/high
Evidence: primary/secondary/mixed
Obsidian: [[event note]]
Follow-up:
- ...
```

## Sending command

From a cron job with terminal access, use:

```bash
hermes --profile supply-chain-researcher send --to discord:1522119384477208596 --file /path/to/alert.md
```
