---
type: supply-chain-map
sector: AI Supply Chain
created: 2026-07-05
last_updated: 2026-07-27
confidence: medium
---

# AI Supply Chain Master Map

This is the living model of the AI infrastructure value chain. Update this map when material events change capacity, bottlenecks, supplier/customer dependencies, pricing power, regulatory exposure, or demand visibility.

## Layered value chain

### 1. Demand and application pull

- Enterprise AI workloads and software platforms.
- Consumer AI, search, productivity, developer tools, coding assistants.
- Sovereign AI, defense, healthcare, financial services, industrial automation.
- Autonomous systems and robotics as a later-cycle demand vector.

Representative public exposures: MSFT, GOOGL, AMZN, META, ORCL, CRM, NOW, ADBE, PLTR. Private entities can matter as demand aggregators or market-structure signals: OpenAI, Anthropic, xAI, Databricks, Mistral, Perplexity.

### 2. Model labs, inference platforms, and cloud intermediaries

- Frontier model labs influence accelerator demand, networking needs, and datacenter leasing.
- Hyperscalers control capex cadence, custom silicon roadmaps, and infrastructure utilization.
- Neo-cloud and GPU-cloud providers can amplify near-term server/GPU demand but may carry financing and customer-concentration risk.

Key entities: OpenAI, Anthropic, xAI, CoreWeave, Lambda, Crusoe, Nebius, IREN, Galaxy/Helios, Applied Digital, CleanSpark, MARA, Hut 8/Beacon Point, Coravel/ACS/GIP, NAVER, SK Telecom, Microsoft Azure, Google Cloud/Alphabet, AWS, Oracle Cloud.

### 3. Datacenter physical infrastructure

- Site selection, power availability, grid interconnection queues, substations, transformers, backup power, cooling, racks, UPS, switchgear, and datacenter construction capacity.
- Bottlenecks can shift from chips to power, cooling, permitting, and construction lead times.

Representative public exposures: IREN, GLXY, APLD, CLSK, MARA, HUT, AEP where utility/interconnection exposure is material, ACS.MC, BLK/GIP where material, VRT, ETN, SU.PA, ABB, SMCI, DELL, HPE, MOD, PWR, Quanta/Inventec/Wistron/Wiwynn/Foxconn where listed.

### 4. AI servers, ODMs, and system integration

- AI servers integrate accelerators, CPUs, HBM packages, networking, power delivery, cooling, storage, and firmware.
- ODM and OEM order commentary can provide early signal on accelerator allocations and hyperscaler capex cadence.

Representative entities: Supermicro, Dell, HPE, Quanta, Wistron, Wiwynn, Inventec, Foxconn Industrial Internet, Lenovo.

### 5. Accelerators and custom silicon

- Merchant GPUs and accelerators: NVIDIA, AMD, Intel.
- Custom ASICs and XPUs: hyperscaler internal chips; Broadcom/Marvell and design-service ecosystems.
- Key constraints: HBM availability, advanced packaging, substrate supply, foundry wafers, networking, power envelope, software ecosystem.

Representative public exposures: NVDA, AMD, INTC, AVGO, MRVL, TSM, ARM, GFS where relevant.

### 6. Memory and storage

- HBM is a critical AI accelerator input and can constrain GPU/ASIC shipments.
- DRAM/NAND cycle interacts with AI server mix, capex allocation, and memory pricing.

Representative public exposures: SK Hynix, Samsung Electronics, Micron, Western Digital, Kioxia when relevant.

### 7. Foundry, advanced packaging, substrates, and materials

- Leading-edge foundry, CoWoS/SoIC/FoWLP and other advanced packaging capacity, ABF substrates, interposers, photoresists, gases, wafers, specialty chemicals.
- These layers often determine whether accelerator demand converts into shippable systems.

Representative exposures: TSMC, Samsung Foundry, Intel Foundry, UMC/GlobalFoundries for less advanced nodes, Ibiden, Unimicron, AT&S, Shinko, Sumitomo Bakelite, Ajinomoto.

### 8. Semiconductor capital equipment, EDA, and IP

- Lithography, deposition, etch, inspection/metrology, test, thermal processing, packaging equipment.
- EDA/IP shapes design cadence and custom silicon feasibility.

Representative public exposures: ASML, AMAT, LRCX, TEL, KLAC, ASMI, BESI, Teradyne, Advantest, Synopsys, Cadence, Siemens EDA, ARM.

### 9. Networking, optics, and interconnect

- Ethernet/InfiniBand switching, NICs, DPUs, optics, copper, coherent/DSP, optical transceivers, cables, fabrics.
- Cluster scale and inference workloads can shift bottlenecks toward networking and power efficiency.

Representative exposures: NVDA, AVGO, MRVL, ANET, CSCO, COHR, LITE, Fabrinet, MMM for physical optical-connectivity adoption where material, Innolight/Eoptolink where accessible.

### 10. Policy, geopolitics, and logistics

- Export controls, entity lists, customs, Taiwan/China risk, Korea/Japan materials, Netherlands/Japan equipment controls.
- Logistics disruptions and trade policy can affect lead times, location decisions, and inventory behavior.

## Current bottleneck watchlist

| Bottleneck | Current research question | Related segments | Evidence status |
|---|---|---|---|
| HBM | Is HBM still the binding constraint for accelerator shipments, and which vendor has incremental share/pricing power? | [[03 Segments/HBM and Memory]], [[03 Segments/Accelerators and Custom Silicon]] | Primary Micron HBM4 production evidence plus primary NVIDIA/SK Group evidence of a planned long-term NVIDIA-SK Hynix next-generation AI memory/HBM partnership for Vera Rubin-scale AI factories; binding agreement terms, volumes, allocation, pricing, and margin impact still unknown. |
| Advanced packaging / leading-edge foundry | Is CoWoS/advanced-packaging capacity easing fast enough to unlock AI accelerator supply, and how fast is leading-edge wafer capacity being absorbed by AI/HPC demand? | [[03 Segments/Foundry Advanced Packaging and Substrates]] | TSMC Q2 2026 primary evidence confirms strong leading-edge/HPC demand, 77% advanced-node wafer revenue, HPC at 66% of net revenue and +20% QoQ, and a steep 2nm ramp; CoWoS/advanced-packaging capacity still not quantified. |
| Datacenter power | Are power/interconnection constraints becoming a more important limiter than chip availability? | [[03 Segments/Datacenter Power Cooling and Construction]] | Primary NVIDIA evidence adds Korea sovereign-AI demand at stated MW/GW scale: NAVER/NVIDIA/Brookfield proposed 200 MW DSX AI factory expansion by 2028 with 1 GW path and conditional funding, plus SK Telecom's planned up-to-2 GW Vera Rubin DSX AI Factory under SK/NVIDIA LOIs. This sits alongside primary Alphabet evidence ($80.6B H1 2026 capex and $85.2B of non-commenced data-center lease payments), TeraWulf/Anthropic 401 MW lease evidence, Galaxy/Helios delivered load and priced financing, APLD/CLSK/HUT/IREN lease and AI-cloud-contract evidence, MARA/HIF powered-site pipeline, and Coravel/ACS/GIP secondary platform evidence; execution milestones still needed for future phases and LOI/nonbinding funding events should be weighted below closed financings, signed leases, and delivered-load evidence. |
| AI servers / systems | Are AI server OEM order books converting into shippable, profitable systems or signaling customer concentration / commitment-quality risk? | [[03 Segments/AI Servers ODMs and System Integration]], [[03 Segments/Accelerators and Custom Silicon]] | Primary Supermicro July 2026 preliminary update shows record backlog and >$60B of fiscal Q4 new orders, but also low-end revenue and explicit caveats that some orders may not be firm and may be cancellable/delayed; conversion and margin durability need verification. |
| Networking/optics | Are cluster scale and inference growth shifting value to Ethernet, optics, switching, and physical optical-connectivity layers? | [[03 Segments/Networking Optics and Interconnect]] | Arista 1.6T portfolio is product-cycle evidence; 3M/Microsoft EBO is early named-hyperscaler optical-connectivity deployment evidence, but volume/value and bottleneck impact remain unquantified. |
| Export controls | Are restrictions changing regional demand, inventory, or China-local substitution? | [[03 Segments/Policy Geopolitics and Logistics]] | Primary Federal Register evidence that BIS moved some China/Macau advanced-computing exports to case-by-case review, plus primary BIS evidence that UAE reclassified to A:5 with license-free advanced-computing access for approved UAE recipients; actual licenses, approved entities, and shipment impact still unknown. |

## Change log

| Date | Change | Evidence |
|---|---|---|
| 2026-07-27 | Added NVIDIA's Korea AI factory partnership releases as a recent sovereign AI infrastructure and HBM/platform signal: NAVER/NVIDIA/Brookfield proposed 200 MW GAK Sejong DSX expansion by 2028 with a stated 1 GW path and conditional NVIDIA/Brookfield funding, plus SK Group/NVIDIA LOIs for a $500B+ initiative including SK Telecom's up-to-2 GW Vera Rubin DSX AI Factory and SK Hynix next-generation AI memory/HBM partnership. | [[04 Events/2026/2026-07-24 NVIDIA Korea AI Factory Partnerships]]; NVIDIA July 24, 2026 primary newsroom releases. |
| 2026-07-26 | Added two historical Applied Digital lease-gap datapoints: Delta Forge 1's 300 MW / ~$7.5B lease with a new U.S. investment-grade hyperscaler and Polaris Forge 3's 300 MW / ~$7.5B take-or-pay follow-on lease with the same hyperscaler, lifting APLD's disclosed contracted portfolio to 1,200 MW net critical IT load before the later Delta Forge 2 event. | [[04 Events/2026/2026-04-23 Applied Digital Delta Forge 1 Hyperscaler Lease]]; [[04 Events/2026/2026-05-20 Applied Digital Polaris Forge 3 Hyperscaler Lease]]; Applied Digital primary SEC/company releases. |
| 2026-07-24 | Updated Galaxy Helios Phase II from financing launch toward priced project financing: $3.507B of senior secured notes priced at 9.875%, with closing expected July 28 subject to conditions; financing cost is now part of the AI datacenter bottleneck model. | [[04 Events/2026/2026-07-22 Galaxy Helios Phase II Financing]]; Galaxy July 24, 2026 Form 8-K and Exhibit 99.1 pricing release. |
| 2026-07-23 | Added Alphabet/Google Cloud as a primary hyperscaler AI-infrastructure financing/capex datapoint: $49.6B common/preferred equity net proceeds partly for AI infrastructure/global compute, $20.3B Q2 debt issuance, $80.6B H1 2026 capex vs $39.6B year ago, $85.2B non-commenced data-center lease payments, and TPU-system revenue beginning with most expected in 2027. | [[04 Events/2026/2026-07-22 Alphabet AI Infrastructure Financing and Capex]]; Alphabet July 22, 2026 Form 8-K / Exhibit 99.1 and July 23, 2026 Q2 Form 10-Q. |
| 2026-07-22 | Added Galaxy Helios Phase II financing launch as a same-day primary SEC-filed capacity-conversion datapoint: proposed $3.507B senior secured notes to finance part of a CoreWeave-leased 400 MW utility / 260 MW critical IT-load project with $10.4B minimum contracted lease payments and Q2 2027 initial targeted rent commencement. | [[04 Events/2026/2026-07-22 Galaxy Helios Phase II Financing]]; Galaxy July 22, 2026 Form 8-K and Exhibit 99.1. |
| 2026-07-22 | Added Supermicro preliminary fiscal Q4 2026 update as a primary AI-server backlog/margin datapoint: >$60B of Q4 new orders, record backlog, and preliminary 15%-17% gross margins, with order-firmness and export-control caveats. | [[04 Events/2026/2026-07-21 Supermicro Q4 2026 Preliminary Orders Backlog]]; Supermicro July 21, 2026 Form 8-K and Exhibit 99.1. |
| 2026-07-21 | Added IREN as a primary-sourced AI cloud capacity absorption datapoint: $2.8B new multi-year customer contracts, >$4B 2026 ARR target now ~85% contracted, customer prepayments around 45% of associated GPU capex, 480 MW being delivered in 2026, and 1.2 GW targeted for 2027. | [[04 Events/2026/2026-07-20 IREN AI Cloud Customer Contracts]]; IREN July 20, 2026 Form 8-K and Exhibit 99.1. |
| 2026-07-20 | Added Hut 8 / Beacon Point Phase 2 as a same-day primary SEC-filed AI datacenter lease datapoint: second 15-year lease for 352 MW IT capacity, $9.8B base-term value, 704 MW total tenant capacity at the campus, 1,000 MW utility capacity secured through AEP Texas interconnection, and Q2 2028 initial Phase 2 delivery target. | [[04 Events/2026/2026-07-20 Hut 8 Beacon Point Phase 2 Lease]]; Hut 8 July 20, 2026 Form 8-K and Exhibit 99.1. |
| 2026-07-19 | Added Coravel/ACS/GIP as a high-quality secondary-sourced AI datacenter platform/campus datapoint: 1.7 GW development portfolio, 1.2 GW IT load, 150 MW under construction, and first hyperscaler agreement for ~140 MW critical IT load at Dallas-Fort Worth; treated below SEC-filed lease evidence because delivery timing/economics and primary-source MW fields remain unverified. | [[04 Events/2026/2026-07-16 Coravel ACS GIP Hyperscaler Data Center Platform]]; Data Center Dynamics July 16, 2026 article; Coravel website. |
| 2026-07-18 | Added MARA/HIF Matagorda as a primary-sourced 2 GW powered-site pipeline datapoint for AI/HPC campus monitoring; no signed HPC tenant yet, so this is a power/site-control signal rather than confirmed AI lease or delivered capacity. | [[04 Events/2026/2026-07-09 MARA HIF Matagorda Powered Land Site]]; MARA July 9, 2026 Form 8-K and Exhibit 99.1. |
| 2026-07-17 | Added 3M/Microsoft Expanded Beam Optical deployment as an early named-hyperscaler physical optical-connectivity signal for AI data centers; materiality is medium because no volume/value or cluster-level capacity impact was disclosed. | [[04 Events/2026/2026-07-15 3M Microsoft EBO Azure Data Centers]]; 3M primary press release. |
| 2026-07-16 | Added TSMC Q2 2026 primary earnings materials as a leading-edge foundry/HPC demand datapoint: Q2 revenue +36% YoY, advanced technologies 77% of wafer revenue, HPC 66% of net revenue and +20% QoQ, Q3 guide US$44.6-45.8B, 2026 USD revenue growth expected slightly above 40%, and Q2 capex NT$496B. | [[04 Events/2026/2026-07-16 TSMC Q2 AI Leading Edge Demand]]; TSMC Q2 2026 quarterly results materials. |
| 2026-07-15 | Added Applied Digital's Polaris Forge 1 Building 2 Phase 1 Ready-for-Service milestone as a historical operational-delivery datapoint: 75 MW delivered on schedule, lifting live campus capacity to 175 MW against 400 MW contracted full buildout. | [[04 Events/2026/2026-07-01 Applied Digital Polaris Forge 1 Building 2 Delivery]]; Applied Digital primary press release. |
| 2026-07-14 | Added CleanSpark/Sandersville as another primary-sourced MW-scale AI/HPC datacenter lease datapoint and added CLSK to the direct public-exposure set for the campus lease theme. | [[04 Events/2026/2026-07-14 CleanSpark Sandersville Global Tech Lease]]; CleanSpark SEC 8-K and Exhibit 99.1. |
| 2026-07-12 | Added BIS UAE export-control easing as a primary-sourced Gulf AI infrastructure demand/policy datapoint: UAE was reclassified to A:5 and approved UAE recipients may receive advanced computing items license-free, including AI chips and servers. | [[04 Events/2026/2026-07-10 BIS UAE Export Control Easing]]; BIS primary announcement. |
| 2026-07-11 | Added BIS January 2026 advanced-computing export license-review rule as a primary-sourced historical policy datapoint for China/Macau H200-class accelerator demand and foundry-capacity allocation monitoring. | [[04 Events/2026/2026-01-15 BIS Advanced Computing Export License Review Policy]]; Federal Register 91 FR 1684. |
| 2026-07-10 | Added Applied Digital / Delta Forge 2 as another primary-sourced AI datacenter MW lease datapoint and added APLD to the direct public-exposure set for the campus lease theme. | [[04 Events/2026/2026-06-08 Applied Digital Delta Forge 2 Hyperscaler Lease]]; Applied Digital SEC-filed Exhibit 99.1. |
| 2026-07-09 | Added Galaxy Helios Phase I / CoreWeave 133 MW delivery as operational evidence that power-ready campuses are converting into revenue-generating AI/HPC capacity. | [[04 Events/2026/2026-07-06 Galaxy Helios Phase I CoreWeave Delivery]]; Galaxy primary press release. |
| 2026-07-08 | Added TeraWulf/Anthropic 401 MW AI campus lease as high-signal evidence that model-lab demand is converting into long-duration power/datacenter commitments. | [[04 Events/2026/2026-07-06 TeraWulf Anthropic Justified Data Campus Lease]]; TeraWulf SEC 8-K. |
| 2026-07-07 | Added Micron HBM4 production for NVIDIA Vera Rubin as a primary historical baseline for HBM bottleneck monitoring. | [[04 Events/2026/2026-03-16 Micron HBM4 High Volume Production for NVIDIA Vera Rubin]]; Micron primary sources. |
| 2026-07-05 | Initial broad-stack AI supply-chain map created. | User-approved setup. |
