---
type: event
date: 2026-07-20
status: active
confidence: high
materiality: high
source_quality: primary
segments: [Demand Model Labs and Cloud, Datacenter Power Cooling and Construction, Accelerators and Custom Silicon]
companies: [IREN, Microsoft, NVIDIA, Perplexity, Figure AI, Together AI, Fluidstack, Fireworks AI, Fal AI, Hume AI]
public_exposures: [IREN, MSFT, NVDA, VRT, ETN, SU.PA, ABB, PWR, MOD]
created: 2026-07-21
last_reviewed: 2026-08-13
superseded_by:
---

# Event: IREN signs $2.8B AI cloud contracts and raises 2026 ARR target above $4B

## Facts

- IREN filed a Form 8-K on July 20, 2026 with Exhibit 99.1 announcing new multi-year AI cloud services contracts with leading AI developers representing $2.8 billion of total contract value.
- IREN raised its year-end 2026 AI Cloud annualized run-rate revenue target from $3.7 billion to more than $4.0 billion and said approximately 85% of that target is now under contract.
- The press release says IREN's customer base now includes Microsoft, NVIDIA, Perplexity, Figure AI, Together AI, Fluidstack, Fireworks AI, Fal AI, Hume AI, and a new leading AI developer, across bare-metal and managed cloud services.
- IREN says demand from hyperscalers, enterprises, AI developers, and frontier labs continues to exceed its available and planned capacity, and that it is engaged with customers across its entire 2026 and 2027 expansion program.
- IREN says recent contracts include customer prepayments representing approximately 45% of the associated GPU capital expenditure, reducing IREN's net funding requirement for those deployments.
- Across the portfolio, IREN says customer contracts have a weighted average term of approximately four years.
- Management says IREN expanded from approximately 3 MW of self-built AI Cloud capacity over the past 12 months to 480 MW being delivered in 2026, with 1.2 GW targeted for 2027.
- IREN reported approximately $7.6 billion of cash and cash equivalents as of June 30, 2026.
- This event was discovered by the July 21, 2026 cron as a historical database gap; no Discord alert was sent solely because it was not newly announced on the cron date.
- IREN filed a Form 8-K on August 13, 2026 furnishing Exhibit 99.1 and announcing that Horizon 1 had been delivered to and accepted by Microsoft.
- IREN says Horizon 1 is the first of four 50 MW IT-load direct-to-chip liquid-cooled AI Cloud deployments scheduled for delivery to Microsoft at the Childress, Texas campus in 2026 under the five-year, $9.7 billion cloud services contract announced in November 2025.
- IREN also said it achieved NVIDIA Exemplar Cloud status on NVIDIA GB300 NVL72 after NVIDIA testing of the Horizon 1 deployment.
- IREN continues to target a broader expansion to 480 MW gross AI Cloud capacity in 2026 and 1.2 GW gross AI Cloud capacity in 2027.

## Source links

- Primary SEC filing: IREN Form 8-K filed July 20, 2026: https://www.sec.gov/Archives/edgar/data/1878848/000114036126028871/ef20078253_8k.htm
- Primary SEC-filed Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1878848/000114036126028871/ef20078253_ex99-1.htm
- Primary SEC filing: IREN Form 8-K filed August 13, 2026: https://www.sec.gov/Archives/edgar/data/1878848/000114036126032638/ef20080141_8k.htm
- Primary SEC-furnished Exhibit 99.1 Horizon 1 / Microsoft acceptance release: https://www.sec.gov/Archives/edgar/data/1878848/000114036126032638/ef20080141_ex99-1.htm

## Affected supply-chain nodes

- GPU cloud / neo-cloud demand aggregation: contracted AI cloud services revenue and customer prepayments convert model-lab and enterprise AI demand into deployable GPU capacity demand.
- Datacenter power and construction: the disclosed 480 MW 2026 delivery target and 1.2 GW 2027 target add another power-scale AI cloud capacity ramp to monitor.
- Accelerators / AI servers: customer prepayments tied to GPU capex and demand exceeding planned capacity imply continued pressure on GPU, server, networking, power, and cooling procurement. The August 13 update specifically validates a Microsoft-accepted NVIDIA GB300 NVL72 deployment, but the filing does not disclose GPU count, revenue-recognition schedule, margins, or named server/electrical/cooling suppliers.

## Interpretation

- This is stronger than a generic AI demand headline because it discloses contracted value, contracted share of the ARR target, named customer set, customer prepayments, weighted-average contract term, and MW-scale capacity targets.
- It is not directly comparable to the SEC-filed critical-IT-load lease events in the database because IREN is selling AI cloud services rather than leasing data center capacity to a single tenant; the relevant mechanism is GPU-cloud revenue visibility and capacity absorption rather than campus lease economics.
- Customer prepayments covering roughly 45% of associated GPU capex are important because they may reduce financing risk and help convert planned capacity into actual GPU deployments.
- The August 13 Horizon 1 acceptance is a stronger operational milestone than a pipeline reiteration because Microsoft accepted the first 50 MW IT-load deployment and NVIDIA testing resulted in Exemplar Cloud status on GB300 NVL72; however, it is still below a full four-Horizon completion because three additional 50 MW deployments remain scheduled for later 2026.

## Investment / quant relevance

### Discretionary catalyst angle

- Direct: IREN gains a high-signal AI cloud demand and financing datapoint, with $2.8B of new TCV and >$4B 2026 ARR target now ~85% contracted.
- Indirect: named customer set and demand exceeding capacity support continued monitoring of NVDA/GPU supply, AI server, electrical, cooling, and construction suppliers, but supplier-specific order conversion is not yet disclosed.

### Quant-testable hypothesis

- Universe: GPU-cloud / datacenter developers, former bitcoin-mining infrastructure owners pivoting to AI, accelerator vendors, AI server OEMs/ODMs, and datacenter electrical/cooling suppliers.
- Signal: SEC-filed AI cloud or AI datacenter contract announcements with TCV/ARR, MW capacity targets, named customers or customer class, and prepayment/financing fields.
- Target variable: 0-5 trading-day direct-stock reaction and 1-4 quarter revisions to revenue, capex, backlog, and supplier estimates.
- Expected lead/lag: immediate for direct neo-cloud/developer exposure; longer for GPU/server/electrical supplier fundamentals.
- Data requirements: SEC filing timestamp, TCV/ARR, contracted percentage, MW/GW capacity fields, customer identities/classes, prepayment terms, GPU capex, commissioning schedule, realized revenue ramp, and supplier order commentary.

## Confidence and uncertainty

- Confidence: high that IREN disclosed the contract value, ARR target, customer set, prepayment percentage, and MW capacity targets in a primary SEC-filed exhibit.
- What remains uncertain: customer-level revenue concentration, GPU model mix and procurement timing, whether all planned 2026/2027 capacity commissions on schedule, realized utilization and margins, customer acceptance timing, and which public equipment/cooling/electrical suppliers benefit.
- August 13 update: Microsoft acceptance of Horizon 1 and NVIDIA Exemplar Cloud status reduce execution risk for the first 50 MW IT-load tranche, but acceptance/revenue timing for Horizons 2-4, deployment economics, supplier bill of materials, and utilization remain open.

## Follow-up triggers

- Track future IREN filings for GPU procurement, capex, debt/equity financing, customer concentration, revenue recognition, and commissioning acceptance.
- Watch for supplier commentary from NVIDIA, server OEMs/ODMs, Vertiv, Eaton, Schneider Electric, ABB, MOD, and construction/electrical contractors that confirms order conversion.
- Compare IREN's realized AI Cloud revenue and MW commissioning against the >$4B 2026 ARR target and 1.2 GW 2027 target.
- Track Microsoft acceptance/revenue milestones for Horizons 2-4 and any filing that discloses GPU count, GB300 NVL72 economics, margins, capex, supplier names, or service-level obligations.

## Change log

| Date | Change | Evidence |
|---|---|---|
| 2026-08-13 | Updated with same-day primary SEC-furnished Horizon 1 operational milestone: IREN said the first of four 50 MW IT-load direct-to-chip liquid-cooled AI Cloud deployments at Childress was delivered to and accepted by Microsoft under the five-year $9.7B cloud services contract and achieved NVIDIA Exemplar Cloud status on GB300 NVL72; Discord alert sent as part of the Aug. 13 AI datacenter lease/delivery alert. | IREN August 13, 2026 Form 8-K and Exhibit 99.1. |
| 2026-07-21 | Created event note as historical database-gap discovery; no alert sent because the primary announcement was dated July 20, 2026 rather than the cron date. | IREN July 20, 2026 Form 8-K and Exhibit 99.1. |
