---
type: event
date: 2026-07-28
status: active
confidence: high
materiality: high
source_quality: primary
segments: [Demand Model Labs and Cloud, Datacenter Power Cooling and Construction, Accelerators and Custom Silicon]
companies: [Core Scientific, AMD]
public_exposures: [CORZ, AMD, NVDA, TSM, SK Hynix, Samsung Electronics, MU, VRT, ETN, SU.PA, ABB, PWR, MOD]
created: 2026-08-02
last_reviewed: 2026-08-14
superseded_by:
---

# Event: Core Scientific and AMD announce AI infrastructure partnership for 530 MW initial capacity

## Facts

- Core Scientific filed a Form 8-K on July 28, 2026 furnishing Exhibit 99.1 announcing a partnership with AMD.
- The primary press release says AMD secured more than 500 MW of U.S. AI-ready infrastructure capacity beginning in 2027, with the ability to expand up to 2.5 GW.
- Core Scientific's Q2 2026 Form 10-Q says that on July 27, 2026 the company entered into lease agreements with AMD for an aggregate 377 MW of critical IT capacity at Pecos, Texas; Muskogee, Oklahoma; and Hunt County, Texas.
- The same 10-Q says Core Scientific entered into separate Neocloud leases for 152 MW of critical IT capacity at Auburn, Alabama and Dalton Phase 3, Georgia; AMD is party to credit-support agreements that protect AMD equipment, give AMD cure rights for certain Neocloud defaults, and establish AMD rights/obligations after certain material Neocloud defaults.
- The 10-Q says each lease has a 15-year term with three five-year options.
- The AMD leases give AMD a reservation right for an additional 1,925 MW of critical IT capacity through December 28, 2028.
- Core Scientific issued AMD a warrant to purchase up to 30 million Core Scientific common shares at $23.47 per share; warrant shares vest at 12,222 shares per MW of critical IT load, and about 6.5 million shares vested when the July 27 leases were executed.
- Core Scientific's July 2026 investor deck breaks the initial approximately 530 MW leased-power footprint into Pecos (~185 MW), Dalton (~120 MW), Hunt County (~110 MW), Muskogee (~82 MW), and Auburn (~32 MW). It says initial delivery for AMD is expected in early 2027 and the full 530 MW is expected by the end of 2028.
- The deck says Core Scientific now has about 1.1 GW of customer-contracted power and more than $24B in contracted revenue across its footprint, with significant expansion potential through the AMD relationship for over 3 GW of customer-contracted capacity.
- On August 14, 2026 Core Scientific filed an 8-K saying it completed the previously announced August 13 acquisition of Polaris DS LLC for approximately $444.3 million in cash. The acquired assets are tied to the May 5, 2026 merger agreement, under which Polaris DS's material assets at closing were approximately 40 acres adjacent to Core Scientific's Muskogee, Oklahoma datacenter operations, an electrical substation, and electrical service agreements with Oklahoma Gas and Electric Company providing up to 440 MW of continuous electricity to the premises; the purchase price can increase by $40 million if an additional 40 MW of firm electric capacity becomes available before December 31, 2026.
- This event was discovered by the daily monitoring job on August 2, 2026. Discord alert sent despite delayed discovery because the July 28 primary SEC-filed event was recent, not already captured, and materially updates the AMD AI accelerator / power-rich datacenter capacity model.

## Source links

- Primary SEC filing: Core Scientific July 28, 2026 Form 8-K: https://www.sec.gov/Archives/edgar/data/1839341/000183934126000012/core-20260727.htm
- Primary SEC-filed Exhibit 99.1 press release: https://www.sec.gov/Archives/edgar/data/1839341/000183934126000012/amdpr.htm
- Primary SEC-filed Q2 2026 investor deck: https://www.sec.gov/Archives/edgar/data/1839341/000183934126000012/q2fy26earningsdeck728am.htm
- Primary SEC filing: Core Scientific Q2 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1839341/000183934126000014/core-20260630.htm
- Primary SEC filing: Core Scientific August 14, 2026 Form 8-K announcing Polaris DS acquisition close: https://www.sec.gov/Archives/edgar/data/1839341/000183934126000018/core-20260813.htm
- Primary SEC filing: Core Scientific May 5, 2026 Form 8-K announcing Polaris DS merger agreement: https://www.sec.gov/Archives/edgar/data/1839341/000162828026030918/core-20260505.htm

## Affected supply-chain nodes

- AMD accelerator ecosystem and customer deployments.
- Power-rich AI datacenter capacity and high-density colocation.
- Datacenter electrical/cooling/construction suppliers serving large multi-site AI deployments.
- HBM, advanced packaging, and foundry demand indirectly if AMD converts reserved capacity into MI-series accelerator deployments at scale.

## Interpretation

- This is not just a generic AI partnership: primary SEC evidence shows named public parties, critical-IT-capacity terms, lease tenor, site list, delivery timing, an AMD reservation right for nearly 2 GW of incremental capacity, and equity-linked commercial economics.
- The event strengthens the thesis that accelerator vendors are competing not only on chips/software but also on access to power and deployable datacenter capacity for customers.
- Compared with LOI-stage sovereign announcements or generic site-control news, the signed 15-year leases and SEC-filed warrant terms make this a higher-confidence capacity/procurement datapoint. Execution risk remains because the capacity is future-delivery, with full initial 530 MW expected by end-2028.

## Investment / quant relevance

### Discretionary catalyst angle

- Direct: CORZ gains a named AMD relationship, a large initial leased-capacity block, warrant-linked upside/alignment, and an incremental path to multi-GW capacity reservations. AMD gains a power/datacenter capacity channel that could reduce deployment friction for customers adopting AMD AI platforms.
- Read-through: adds another large multi-site demand signal for datacenter power/cooling/electrical suppliers and for AI infrastructure developers competing for utility-scale powered capacity.

### Quant-testable hypothesis

- Universe: CORZ, AMD, other power-rich datacenter developers/former miners, AI accelerator vendors, electrical/cooling suppliers, HBM/foundry suppliers.
- Signal: SEC-filed named accelerator-vendor datacenter-capacity lease/reservation events with disclosed MW, lease tenor, delivery window, and equity/credit-support mechanics.
- Target variable: 0-5 day direct/peer returns; 1-4 quarter revisions to developer revenue/backlog, AMD accelerator expectations, and supplier orders.
- Expected lead/lag: immediate for CORZ/AMD and peer developer sentiment; later for equipment, cooling, HBM, and foundry order conversion.
- Data requirements: filing timestamp, MW and reservation fields, delivery milestones, named customer/vendor, lease tenor, credit support, warrants, capex/funding needs, follow-on commissioning and AMD accelerator-shipment commentary.

## Confidence and uncertainty

- Confidence: high that the partnership and lease/reservation terms exist because they are disclosed in SEC filings and SEC-filed exhibits.
- What remains uncertain: actual customer identity behind the Neocloud leases, AMD customer deployments, GPU counts/model mix, HBM/foundry allocation, financing/capex burden, utility/interconnection execution, supplier awards, and whether AMD exercises the additional capacity reservation rights.

## Follow-up triggers

- Core Scientific updates on site construction, energization, billable MW, capex, financing, and lease revenue recognition for the AMD-related sites.
- AMD earnings/commentary tying Instinct GPU demand, customer wins, or cloud availability to the Core Scientific capacity.
- Any exercise or expansion of AMD's additional 1,925 MW reservation right.
- Electrical/cooling supplier commentary indicating orders tied to Pecos, Muskogee, Hunt County, Dalton, or Auburn deployments.

## Change log

| Date | Change | Evidence |
|---|---|---|
| 2026-08-02 | Created event note from recent primary SEC-filed evidence; Discord alert sent because this materially updates an active AI datacenter capacity and AMD accelerator-deployment thesis. | Core Scientific July 28, 2026 Form 8-K / Exhibit 99.1; Q2 2026 Form 10-Q; SEC-filed investor deck. |
| 2026-08-14 | Added Core Scientific's same-day Polaris DS acquisition close as an execution/site-power follow-up: approximately $444.3M cash close for assets tied to 40 acres adjacent to Muskogee operations, substation assets, and up to 440 MW of continuous electricity under OG&E service agreements; no new Discord alert because the original agreement was from May 2026 and the close does not add a new signed AI tenant, critical-IT-load lease economics, RFS/rent milestone, or AMD reservation exercise. | Core Scientific August 14, 2026 Form 8-K; Core Scientific May 5, 2026 Form 8-K. |
