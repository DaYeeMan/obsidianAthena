---
type: supply-chain-map
sector: AI Supply Chain
created: 2026-07-05
last_updated: 2026-07-05
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

Key entities: OpenAI, Anthropic, xAI, CoreWeave, Lambda, Crusoe, Nebius, Microsoft Azure, Google Cloud, AWS, Oracle Cloud.

### 3. Datacenter physical infrastructure

- Site selection, power availability, grid interconnection queues, substations, transformers, backup power, cooling, racks, UPS, switchgear, and datacenter construction capacity.
- Bottlenecks can shift from chips to power, cooling, permitting, and construction lead times.

Representative public exposures: VRT, ETN, SU.PA, ABB, SMCI, DELL, HPE, MOD, PWR, Quanta/Inventec/Wistron/Wiwynn/Foxconn where listed.

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

Representative exposures: NVDA, AVGO, MRVL, ANET, CSCO, COHR, LITE, Fabrinet, Innolight/Eoptolink where accessible.

### 10. Policy, geopolitics, and logistics

- Export controls, entity lists, customs, Taiwan/China risk, Korea/Japan materials, Netherlands/Japan equipment controls.
- Logistics disruptions and trade policy can affect lead times, location decisions, and inventory behavior.

## Current bottleneck watchlist

| Bottleneck | Current research question | Related segments | Evidence status |
|---|---|---|---|
| HBM | Is HBM still the binding constraint for accelerator shipments, and which vendor has incremental share/pricing power? | [[03 Segments/HBM and Memory]], [[03 Segments/Accelerators and Custom Silicon]] | Ongoing |
| Advanced packaging | Is CoWoS/advanced-packaging capacity easing fast enough to unlock AI accelerator supply? | [[03 Segments/Foundry Advanced Packaging and Substrates]] | Ongoing |
| Datacenter power | Are power/interconnection constraints becoming a more important limiter than chip availability? | [[03 Segments/Datacenter Power Cooling and Construction]] | Ongoing |
| Networking/optics | Are cluster scale and inference growth shifting value to Ethernet, optics, and switching? | [[03 Segments/Networking Optics and Interconnect]] | Ongoing |
| Export controls | Are restrictions changing regional demand, inventory, or China-local substitution? | [[03 Segments/Policy Geopolitics and Logistics]] | Ongoing |

## Change log

| Date | Change | Evidence |
|---|---|---|
| 2026-07-05 | Initial broad-stack AI supply-chain map created. | User-approved setup. |
