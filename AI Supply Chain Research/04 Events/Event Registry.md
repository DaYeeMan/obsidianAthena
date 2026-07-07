---
type: event-registry
sector: AI Supply Chain
created: 2026-07-05
last_updated: 2026-07-07
---

# Event Registry

Permanent index of material AI supply-chain events. Event notes should live under `04 Events/YYYY/` and should generally be retained rather than deleted.

## Event lifecycle statuses

- `watching` — potentially material, needs more evidence.
- `active` — currently relevant to the supply-chain model or opportunity watchlist.
- `resolved` — outcome known; preserve evidence.
- `superseded` — replaced by a newer/better event note; link `superseded_by`.
- `stale` — no longer decision-relevant but retained.
- `rejected` — false, immaterial, or weakly supported; retained only if useful for source-quality calibration.

## Events

| Date | Event | Status | Segments | Companies | Materiality | Notes |
|---|---|---|---|---|---|---|
| 2026-03-16 | [[04 Events/2026/2026-03-16 Micron HBM4 High Volume Production for NVIDIA Vera Rubin|Micron HBM4 in high-volume production for NVIDIA Vera Rubin]] | active | [[03 Segments/HBM and Memory]], [[03 Segments/Accelerators and Custom Silicon]], [[03 Segments/Foundry Advanced Packaging and Substrates]] | Micron Technology, NVIDIA | medium | Primary historical baseline for HBM4 production tied to NVIDIA Vera Rubin; volume/share economics still unquantified, so no alert. |
| 2026-06-09 | [[04 Events/2026/2026-06-09 Arista 1.6T AI Fabric Portfolio|Arista introduces 1.6T AI fabric portfolio]] | active | [[03 Segments/Networking Optics and Interconnect]], [[03 Segments/AI Servers ODMs and System Integration]] | Arista Networks | medium | Primary product-cycle signal for AI Ethernet fabrics; no customer/order volume yet, so no alert. |
