---
type: event
date: 2026-07-31
status: active
confidence: high
materiality: high
source_quality: primary
segments: [Demand Model Labs and Cloud, Datacenter Power Cooling and Construction, Accelerators and Custom Silicon]
companies: [Amazon, Amazon Web Services, OpenAI, Anthropic]
public_exposures: [AMZN, NVDA, AMD, AVGO, MRVL, TSM, ANET, VRT, ETN, SU.PA, ABB, PWR, MOD, SMCI, DELL, HPE]
created: 2026-07-31
last_reviewed: 2026-07-31
superseded_by:
---

# Event: Amazon discloses AWS AI infrastructure commitments, capex, and OpenAI/Anthropic chip-linked contracts

## Facts

- Amazon filed a Form 8-K on July 30, 2026 with Exhibit 99.1 announcing Q2 2026 results, and filed its Q2 2026 Form 10-Q on July 31, 2026.
- Exhibit 99.1 says AWS segment sales increased 37% year over year to $42.2 billion, its fastest growth in 18 quarters and a $169 billion annualized revenue run rate.
- AWS segment operating income was $16.6 billion in Q2 2026, versus $10.2 billion in Q2 2025.
- Amazon's Q2 2026 Form 10-Q disclosed approximately $496 billion of performance obligations, primarily related to AWS, associated with commitments in customer contracts for future services not yet recognized, for contracts with original terms exceeding one year; weighted-average remaining life was 6.4 years.
- The 10-Q disclosed that in Q1 2026 AWS and OpenAI expanded an existing $38.0 billion multi-year commitment and commercial arrangement by $100.0 billion over 8.0 years, including contractual obligations related to the performance of AWS chips.
- The 10-Q disclosed that in Q2 2026 AWS and Anthropic expanded their strategic collaboration and existing multi-year commitment by more than $100.0 billion over 10.0 years, including contractual obligations related to the performance of AWS chips.
- Amazon reported cash capital expenditures of $53.1 billion in Q2 2026 versus $31.4 billion in Q2 2025, and $96.3 billion for H1 2026 versus $55.6 billion in H1 2025, primarily reflecting investments in technology infrastructure, most of which support AWS business growth, and fulfillment capacity; Amazon expects both to increase in 2026.
- Amazon's commitments table disclosed $137.214 billion of leases not yet commenced, $130.065 billion of unconditional purchase obligations, $116.350 billion of operating lease liabilities, $16.660 billion of finance lease liabilities including interest, $11.070 billion of financing obligations including interest, and $650.034 billion of total principal contractual commitments as of June 30, 2026.
- Amazon said it invested $28.7 billion in OpenAI Series C preferred stock during H1 2026, including $13.7 billion in Q2; subsequent to June 30, 2026 it funded the remaining $21.3 billion commitment amount. Amazon also invested $10.0 billion in Anthropic nonvoting preferred stock in Q2 2026.

## Source links

- Primary SEC 8-K: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260730.htm
- Primary SEC Exhibit 99.1 Q2 release: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm
- Primary SEC Q2 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm

## Affected supply-chain nodes

- Hyperscaler AI demand and AWS RPO / performance-obligation backlog.
- Custom AWS chips and accelerators used in OpenAI and Anthropic contractual arrangements.
- Datacenter construction, leases not yet commenced, power, cooling, networking, and server infrastructure tied to AWS technology-infrastructure capex.
- Supplier read-through to accelerators/custom silicon, foundry/advanced packaging, HBM, networking/optics, AI servers, and electrical/cooling suppliers.

## Interpretation

- This is primary evidence that AWS AI demand is converting into very large contractual cloud commitments, balance-sheet investments in frontier model labs, and sharply higher technology-infrastructure capex.
- The OpenAI and Anthropic contract language is especially relevant because Amazon explicitly says the expansions include contractual obligations related to the performance of AWS chips, making this a custom-silicon commercialization and capacity-availability signal, not just generic cloud revenue growth.
- The disclosure does not provide MW, datacenter locations, chip counts, GPU versus Trainium/Inferentia mix, foundry allocation, HBM requirements, or lease counterparties, so supplier-specific sizing remains uncertain.

## Investment / quant relevance

### Discretionary catalyst angle

- AMZN adds another primary hyperscaler datapoint validating the AI infrastructure capex and cloud-commitment cycle after Alphabet, Meta, and Microsoft. Supplier baskets exposed to custom silicon, HBM, advanced packaging, networking, servers, and datacenter electrical/cooling should be monitored for order conversion and estimate revisions.

### Quant-testable hypothesis

- Universe: AMZN, MSFT, GOOGL, META, ORCL; supplier baskets including NVDA, AMD, AVGO, MRVL, TSM, ANET, VRT, ETN, SU.PA, ABB, PWR, MOD, SMCI, DELL, HPE.
- Signal: SEC-filed hyperscaler AI/cloud commitments where capex, AWS/Azure/GCP RPO, non-commenced leases, purchase obligations, or named model-lab cloud commitments step up and explicitly reference AI infrastructure or custom chips.
- Target variable: 0-5 day direct and supplier-basket returns; 1-4 quarter supplier backlog, revenue, margin, and estimate-revision changes.
- Expected lead/lag: immediate sentiment read-through; supplier fundamentals over subsequent quarters.
- Data requirements: filing timestamps, capex/lease/purchase-obligation fields, cloud RPO/performance obligations, model-lab contract amounts, chip-language coding, supplier exposure maps, and consensus revisions.

## Confidence and uncertainty

- Confidence: high that the disclosure is material and primary-sourced.
- What remains uncertain: exact datacenter MW, delivery schedule, lease counterparties, GPU versus AWS-chip mix, NVIDIA/AMD/custom-ASIC pull-through, HBM/packaging allocation, and profitability after depreciation, lease, and financing burden.

## Follow-up triggers

- Amazon earnings call transcript for AI capex cadence, power constraints, custom-chip utilization, Trainium/Inferentia roadmap, AWS capacity availability, and 2026 financing plans.
- Later SEC filings for changes in AWS performance obligations, leases not commenced, purchase obligations, and capex.
- Supplier earnings commentary from AI servers, networking/optics, electrical/cooling, foundry/packaging, and HBM vendors referencing AWS/OpenAI/Anthropic demand.

## Change log

| Date | Change | Evidence |
|---|---|---|
| 2026-07-31 | Created event note from Amazon's Q2 2026 8-K, Exhibit 99.1, and 10-Q; Discord alert sent because this is same-day primary hyperscaler AI infrastructure and custom-chip-linked contract evidence. | Amazon July 30, 2026 Form 8-K / Exhibit 99.1 and July 31, 2026 Form 10-Q. |
