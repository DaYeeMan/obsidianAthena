---
type: protocol
created: 2026-07-05
last_updated: 2026-07-05
---

# Daily Monitoring Protocol

## Mission

Maintain the AI Supply Chain Research database silently unless a high-signal event appears. Preserve evidence, update the living map, and surface only actionable or testable developments.

## Daily steps

1. Review [[01 Sources/Source Watchlist]] and scan broad AI supply-chain sources.
2. Identify only material developments affecting capacity, pricing, margins, demand, supplier/customer relationships, capex, regulation, logistics, power, cooling, or public-market expectations.
3. For each material event, create or update an event note under `04 Events/YYYY/` using [[_System/Templates/Event Note Template]].
4. Update [[04 Events/Event Registry]].
5. If the event changes the current model, update relevant segment notes and [[01 Supply Chain Map/AI Supply Chain Master Map]].
6. If it creates an opportunity, update [[05 Opportunity Watchlist/Active Opportunities]] using [[_System/Templates/Opportunity Note Template]] as needed.
7. If high-signal by [[_System/Protocols/Discord Alert Protocol]], send an alert to Discord channel `1522119384477208596`.
8. Otherwise stay quiet; routine maintenance should not be messaged to the user.

## Evidence standards

Prefer primary sources. Clearly label secondary sources and uncertainty. Keep facts separate from interpretation.

## Output discipline

The daily cron job should save notes and local logs. It should not send Discord messages unless the alert threshold is met.
