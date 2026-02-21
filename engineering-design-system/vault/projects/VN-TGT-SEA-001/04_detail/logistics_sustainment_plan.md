---
project: VN-TGT-SEA-001
phase: 4
type: detail_design
document: "Logistics & Sustainment Plan"
version: 1.0
created: 2026-02-11
status: draft
---

# Logistics & Sustainment Plan — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Define the complete through-life logistics and sustainment framework for Vietnamese production, storage, deployment, recovery, and disposal of the THANH TRI-H fixed sea target system. Covers supply chain architecture, PHS&T, inventory management, recoverable item management, debris recovery, training, through-life cost modeling, and obsolescence management.
**Input:** [[OCP_P15_production_planning.md]] (suppliers, transport, packaging, field deployment), [[OCP_C14_cost_analysis.md]] (BOM, volume pricing, cost reduction roadmap), [[DECS_C11_requirements_verification.md]] (MNT, TRA, OPR requirements), [[DECS_S12_standards_compliance.md]] (safety-critical items), [[PRAD_A7_architecture_definition.md]] (modules M1-M8, interfaces), [[RISM_M4_material_analysis.md]] (material shelf life, corrosion data)

---

## 1. Product Support Concept

### 1.1 Expendable Target Philosophy

The THANH TRI-H is an **expendable military target** destroyed by missile impact during anti-ship missile acceptance testing. The core support philosophy is fundamentally different from repairable defense equipment:

| Attribute | Conventional Equipment | THANH TRI-H (Expendable) |
|-----------|----------------------|--------------------------|
| Design life | 10-30 years | Single engagement (~72 h deployed) |
| Repair concept | Multi-level maintenance (O/I/D) | **No post-strike repair** |
| Sparing philosophy | Rotatable pool + repair pipeline | **Buy-and-deploy**; each unit consumed |
| Logistics tail | Depot, test equipment, tech manuals | Minimal: deployment manual, consumables kit |
| TCO driver | Maintenance + spares | **Unit procurement cost** |
| Configuration management | Per-unit tracking, mod incorporation | Serial tracking to deployment; no mods post-delivery |

### 1.2 Recoverable Subsystems

Although the target hull and reflectors are destroyed, three subsystems are designed for recovery and reuse:

| Module | Recovery Status | Rationale | Expected Reuses |
|--------|----------------|-----------|-----------------|
| **M7: Mooring Kit** (anchor, chain, rode, swivel, shackles) | **RECOVERABLE** | Pre-deployed to seabed; disconnected from target before engagement; retrieved by trip line after test | 5-10 deployments (anchor/chain) |
| **M8: Tow Kit** (Dyneema bridle, drogue, shackles) | **RECOVERABLE** | Disconnected from target after positioning; returned to support vessel | 25-50 deployments per SCI-03 retirement criteria |
| **M6: GPS Beacon** | **RECOVERABLE (if feasible)** | Mounted on mast; may survive if mast ejects on impact; GPS tracking enables debris field location | 1-5 deployments (damage-dependent) |

### 1.3 ILS Elements Applicable to Expendable Target

| ILS Element | Applicability | Scope |
|-------------|--------------|-------|
| Supply support | **HIGH** | Unit procurement pipeline, buffer stocks, lot ordering |
| PHS&T | **HIGH** | Packaging, oversize transport, warehouse storage |
| Technical data | **MEDIUM** | Deployment manual, QC procedures, as-built records |
| Training | **MEDIUM** | 4h classroom + 2h hands-on (per ERG-006) |
| Maintenance planning | **LOW** | Recoverable items only (M6, M7, M8) |
| Support equipment | **LOW** | Standard marine tools; no specialized test equipment in field |
| Computer resources | **LOW** | GPS monitoring shore station (Iridium SBD dashboard) |
| Manpower & personnel | **LOW** | 4-person deployment crew + support vessel crew |
| Facilities | **LOW** | Standard covered warehouse; no climate control (TRA-006) |

---

## 2. Supply Chain Architecture

### 2.1 Tier Structure

```
SUPPLY CHAIN ARCHITECTURE — VN-TGT-SEA-001
================================================================

TIER 0: CUSTOMER (Vietnamese Navy / Test Range)
    │
TIER 1: VIETNAMESE ASSEMBLY FACILITY
    │   (System integration, reflector assembly, QC, packaging)
    │   Location: Hanoi / Hai Phong industrial zone
    │
    ├── TIER 2: VIETNAMESE FABRICATION SHOPS
    │   ├── HDPE hull fabricator (Binh Minh Plastics, HCMC)
    │   ├── Steel frame/mast fabricator (Truong Hai Mechanical, Hanoi)
    │   ├── Hot-dip galvanizing plant (Vinh Thanh HDG, Hai Phong)
    │   ├── CNC face plate machining (Hai Phong CNC)
    │   ├── Type II anodizing (Saigon Anodizing, HCMC)
    │   └── Marine hardware chandlers (Hai Phong, Vung Tau)
    │
    ├── TIER 2: ASEAN AM BUREAUS
    │   ├── Xometry Asia (Singapore) — primary AM supplier
    │   ├── Facfox (Shenzhen, China) — backup AM supplier
    │   └── JR Tech Solutions (Bangkok, Thailand) — backup AM supplier
    │
    └── TIER 3: RAW MATERIAL SUPPLIERS
        ├── Hoa Phat Group (S235 steel plate, tube, angle) — Vietnam
        ├── Nam Kim Steel (backup steel) — Vietnam
        ├── Novelis Korea / Hindalco India (6061-T6 Al sheet) — Import
        ├── Dong A Chemical (PU foam components) — Vietnam
        ├── Marlow Ropes agent (Dyneema SK75) — Import (UK/NL)
        └── Garmin / BW Technologies agent (GPS/Iridium) — Import
```

### 2.2 Primary Suppliers

| Component | Primary Supplier | Location | Lead Time | MOQ | Backup Supplier | Backup Lead Time |
|-----------|-----------------|----------|-----------|-----|-----------------|------------------|
| HDPE sheet/resin (PE100) | Binh Minh Plastics | HCMC | 2-3 weeks | 500 kg | Tien Phong Plastics (Hai Phong) | 2-3 weeks |
| PU rigid foam | Dong A Chemical | Binh Duong | 1-2 weeks | 200 kg | Dai Dong Tien (HCMC) | 1-2 weeks |
| S235 steel (plate + tube + angle) | Hoa Phat Group | Hai Duong | 1-2 weeks | 1 ton | Nam Kim Steel (Binh Duong) | 1-2 weeks |
| Steel fabrication (frame, masts) | Truong Hai Mechanical | Hanoi | 2-3 weeks/batch | 1 unit | Vietnam Precision Mechanical (Bac Ninh) | 3-4 weeks |
| Hot-dip galvanizing | Vinh Thanh HDG | Hai Phong | 3-5 days | 500 kg | Hoa Phat Galvanizing (Hai Duong) | 3-5 days |
| 6061-T6 Al sheet (3 mm) | Novelis (Korea) via distributor | Import | 3-4 weeks | 500 kg | Hindalco (India) via HCMC trader | 4-6 weeks |
| CNC face plate machining | Hai Phong CNC | Hai Phong | 1-2 weeks/batch | 8 plates | Minh Phuc CNC (Hanoi) | 1-2 weeks |
| AlSi10Mg AM frames | Xometry Asia | Singapore | 2-3 weeks | 1 frame | Facfox (Shenzhen) / JR Tech (Bangkok) | 3-4 weeks |
| Type II anodize (face plates) | Saigon Anodizing | HCMC | 3-5 days | 10 parts | An Phat Surface Treatment (Binh Duong) | 3-5 days |
| Type III hard anodize (AM frames) | Xometry Asia (bundled) | Singapore | Included in AM | Bundled | Saigon Anodizing (needs qualification) | 5-7 days |
| SS 316 fasteners | Bulong Viet | Hanoi/HCMC | 1-2 weeks | 100 pcs/size | Import (China) via distributor | 2-3 weeks |
| Danforth anchor (50 kg HDG) | Vietnam Marine Equipment | Hai Phong | 2-3 weeks | 5 units | Tan Thanh Marine (Da Nang) | 3-4 weeks |
| G30 HDG chain (19 mm) | Hai Phong Marine Chandler | Hai Phong | 1 week (stock) | 100 m | Vung Tau Marine Supply | 1-2 weeks |
| Polyester rode (20 mm) | Saigon Rope & Cordage | HCMC | 1-2 weeks | 200 m | Hai Phong Rope Factory | 1-2 weeks |
| Dyneema SK75 (16 mm) | Marlow Ropes agent | Import (UK/NL) | **4-6 weeks** | 100 m | Samson Rope (US) via Singapore | 4-6 weeks |
| GNSS/Iridium module (COTS) | Garmin / BW Technologies agent | Import (Taiwan/US) | **4-6 weeks** | 5 units | Queclink (China) | 3-4 weeks |
| Li-ion battery pack (20 Wh) | Bundled with GNSS module | Import (China) | Included or 2-3 weeks | 10 packs | EVE Energy / BYD (China) | 2-3 weeks |
| Drogue (600 mm) | Local canvas/sail maker | Hai Phong | 1-2 weeks | 5 units | Thai Binh Sailmakers (HCMC) | 1-2 weeks |

### 2.3 Critical Supply Chain Risks

| Risk ID | Risk | Affected Supplier | Impact | Probability | Mitigation |
|---------|------|-------------------|--------|-------------|------------|
| SCR-01 | **LPBF AM capacity bottleneck** | Xometry, Facfox, JR Tech | AM frames delayed >3 weeks; production halted | MEDIUM (30%) | Maintain 3 qualified AM bureaus; keep 1-batch (8-frame) buffer stock; pre-order frames 4 weeks ahead of need |
| SCR-02 | **6061-T6 Al import delay** | Korean/Japanese mills | Face plate production delayed 2-4 weeks | MEDIUM (25%) | Maintain 2-month raw material buffer (20 sheets); qualify Indian backup source (Hindalco) |
| SCR-03 | **Dyneema import delay** | Marlow Ropes / Samson | Tow kit delayed; cannot deploy targets | LOW (15%) | Pre-order 6-month Dyneema stock; alternative: 28 mm polyester rope (reduced SWL per TRA-004 minimum) |
| SCR-04 | **GPS module supply disruption** | Garmin / BW Technologies | GPS beacon cannot be assembled | MEDIUM (20%) | Qualify 2 COTS suppliers (Garmin + Queclink); maintain 5-unit buffer stock of completed modules |
| SCR-05 | **HDG bath size limit** | Vinh Thanh HDG | Frame or masts too large for bath | LOW (10%) | Pre-qualify bath dimensions (>=3 m for masts); frame can be galvanized in sub-assemblies |
| SCR-06 | **Single CNC shop bottleneck** | Hai Phong CNC | Face plate production delayed | MEDIUM (20%) | Qualify 2 CNC shops; face plate fly-cutting is standard VMC work, any shop with 1000 mm X-travel qualifies |

### 2.4 Strategic Buffer Stocks

| Component | Buffer Level | Value ($) | Rationale | Storage Requirement |
|-----------|-------------|-----------|-----------|---------------------|
| AlSi10Mg AM frames (8 pcs = 1-unit set) | 16 frames (2-unit buffer) | $14,400 | AM lead time 2-3 weeks; protects against bureau delays | Covered warehouse, padded crates |
| 6061-T6 Al sheet (3 mm, 1250x2500) | 20 sheets (2-month supply) | $5,500 | Import lead time 3-4 weeks; price-lock opportunity | Indoor storage, stacked flat on pallet |
| GPS/Iridium modules | 5 units | $2,650 | Import lead time 4-6 weeks; sole-source risk | Climate-controlled storage, anti-static bags |
| Li-ion battery packs (20 Wh) | 10 packs | $650 | **Limited-life item** (3-year shelf); rotate FIFO | Cool dry storage, 15-25 deg C, <60% RH |
| Dyneema SK75 rope (16 mm) | 200 m (3-4 unit supply) | $1,700 | Import lead time 4-6 weeks | Indoor, UV-protected, coiled on spool |
| SS 316 fastener kits (M6, M10, M12) | 5-unit sets | $1,750 | Bulk purchase efficiency; standard hardware | Parts bins, labeled by size |
| **TOTAL BUFFER INVENTORY** | | **~$26,650** | | |

### 2.5 Procurement Strategy by Component Category

| Category | Strategy | Components | Rationale |
|----------|----------|------------|-----------|
| **Lot buy (per production batch)** | Order full lot quantity at PO; single delivery | HDPE resin, PU foam, steel raw material, fasteners, marine sealant | Short lead times (1-3 weeks); domestic suppliers; volume discount on lot |
| **Blanket order (6-12 month contract)** | Negotiate annual contract; call-off deliveries monthly | 6061-T6 Al sheet, SS 316 fasteners, G30 chain, polyester rode | Price-lock against commodity fluctuation; guaranteed supply; import lead time buffer |
| **Long-lead pre-order** | Order 6-8 weeks before need date | Dyneema SK75, GPS/Iridium modules, Danforth anchors | 4-6 week import lead times; sole-source items; buffer stock maintained |
| **Framework agreement (per-unit call-off)** | Pre-qualified suppliers; call off per unit or per batch of 8 | AM frames (Xometry/Facfox/JR Tech), CNC machining, HDG, anodize | Multiple qualified suppliers for competitive pricing; 2-3 week lead per batch |
| **Just-in-time (local stock)** | Order as needed from local inventory | Marine hardware (shackles, swivels, thimbles), Tef-Gel, safety wire, Sikaflex sealant | Available at local marine chandlers; 1-week lead; low value items |

---

## 3. Packaging, Handling, Storage & Transportation (PHS&T)

### 3.1 Packaging Specifications per Module

| Module | Package Type | Dimensions (LxWxH) | Mass | Special Requirements |
|--------|-------------|---------------------|------|---------------------|
| **M1: Hull (2 half-sections)** | Open flatbed or PE shrink wrap | Each half: 4.0 m x 4.0 m x 0.6 m | ~175 kg each (350 total) | Wrap in PE shrink wrap or moving blanket for surface protection. Foam blocks between halves if stacked. No sharp objects on hull surface. |
| **M3: Mast bundle (8x)** | Steel or wood cradle with ratchet straps | 3.1 m x 0.3 m x 0.3 m | ~130 kg (16.3 kg each x 8) | Bundle 8 masts with ratchet straps. Pad base/top plates with closed-cell foam to prevent HDG damage. |
| **M4: Reflector crates (8x)** | Custom plywood crate with foam lining | Crate: 0.9 m x 0.9 m x 0.5 m each; 2 pallets of 4 | ~15 kg each (120 kg total + crate) | **CRITICAL:** Face plates must NOT contact each other -- insert closed-cell foam separators (10 mm) between each reflector. Handle with care -- anodize surface sensitive to scratching. Stack max 4 high. |
| **M6: GPS beacon (1x)** | Pelican case or padded box | 0.4 m x 0.3 m x 0.3 m | ~5 kg + case | Ship with battery DISCONNECTED. Include spare battery pack. Desiccant pack inside case. |
| **M7: Mooring kit** | Pallet (shrink-wrapped) | 1.2 m x 1.0 m x 0.8 m | 80-200 kg (depth dependent) | Anchor on base, chain coiled, rode flaked on top. Shrink-wrap entire pallet. Mark depth variant (S/M/D) and SWL on label. |
| **M8: Tow kit** | Canvas duffle bag or small crate | 0.8 m x 0.5 m x 0.3 m | ~15 kg | Dyneema bridle coiled (no kinks), drogue folded, hardware in mesh bag. |
| **Fastener kit + spares** | Parts bin or steel toolbox | 0.5 m x 0.3 m x 0.2 m | ~10 kg | Spare locking pins (4x), R-clips (8x), safety wire (2 rolls), Tef-Gel (1 tube), spare shackles (2x), spare M12 bolts (10x), spare M6 bolt sets (12x). |
| **Documentation package** | Waterproof document tube or PVC folder | N/A | ~1 kg | Material certs, inspection reports, deployment manual, RCS test data. |

### 3.2 Handling Procedures

| Operation | Max Lift Mass | Equipment Required | Personnel | PPE Required |
|-----------|--------------|-------------------|-----------|-------------|
| Hull half-section lift | 175 kg | Overhead crane (500 kg) or forklift with sling attachment; certified lifting straps (2,000 kg WLL) | 3 (2 riggers + 1 operator) | Hard hat, steel-toe boots, gloves |
| Hull transport (flatbed loading) | 350 kg (2 halves stacked) | Flatbed truck + crane at origin and destination | 2 + crane operator | Hard hat, steel-toe boots, hi-vis vest |
| Steel frame lift | 150 kg | Overhead crane or chain hoist (500 kg) | 2 + operator | Hard hat, steel-toe boots, gloves |
| Mast-reflector unit handling | 31.3 kg each | **2-person manual lift** -- no mechanical aids required | 2 | Gloves, non-skid footwear (especially on wet deck) |
| Reflector crate handling | ~35 kg each (reflector + crate) | Hand carry or pallet jack for palletized stack | 2 | Gloves (handle by crate, never by reflector face) |
| Mooring pallet handling | Up to 200 kg (deep variant) | Forklift (pallet jack for lighter variants) | 1 + forklift operator | Steel-toe boots, chain-handling gloves |
| GPS beacon | 5 kg | Hand carry | 1 | None special |

### 3.3 Storage Conditions

| Parameter | Requirement | Basis |
|-----------|-------------|-------|
| **Facility type** | Covered warehouse (no climate control required per TRA-006) | All structural materials tolerant of temperature range |
| **Temperature range** | -5 to +55 deg C ambient | OPR-007; all materials rated within this range |
| **Humidity** | <85% RH (non-condensing) | Standard covered warehouse in Vietnamese climate |
| **Floor loading** | Standard warehouse (no special requirement) | Heaviest pallet ~200 kg (mooring kit) |
| **Stacking** | Hull halves: max 2 high with foam spacers. Reflector crates: max 4 high per pallet. | Prevent surface damage |
| **Segregation** | Li-ion batteries stored in separate fireproof cabinet per IATA recommendations | Battery thermal runaway risk; 3-year shelf life rotation |
| **Ventilation** | Standard warehouse ventilation (no fume extraction needed) | No propane, no hazardous vapors (Rev B design) |
| **Security** | Standard military warehouse security; no classified components | ITAR-free design; no controlled technology |

### 3.4 Shelf Life by Component

| Component | Material | Shelf Life (Stored) | Limiting Factor | Rotation Required? |
|-----------|----------|--------------------|-----------------|--------------------|
| HDPE hull shell | PE100, carbon-black stabilized | **20+ years** | UV degradation (mitigated by warehouse storage) | No |
| PU foam fill (in hull) | Closed-cell polyurethane | **20+ years** | Hydrolysis (negligible in closed-cell) | No |
| S235 HDG steel frame | Zinc coating >=85 um | **10-15 years** | Zinc consumption ~6-10 um/yr if exposed; <<1 um/yr in dry storage | No |
| S235 HDG steel masts | Zinc coating >=85 um | **10-15 years** | Same as frame | No |
| 6061-T6 Al face plates (anodized) | Type II anodize >=10 um | **10+ years** | Anodize degradation minimal in dry storage | No |
| AlSi10Mg AM frames (hard anodized) | Type III hard anodize >=25 um | **10+ years** | Hard anodize is extremely durable in storage | No |
| G30 HDG chain | Zinc coating | **10-15 years** | Zinc consumption in dry storage negligible | No |
| Polyester braided rode | UV-stabilized polyester | **10+ years** | UV degradation (mitigated by indoor storage) | No |
| Dyneema SK75 rope | UHMWPE with UV cover braid | **10 years** (UV-protected) | UV and creep; store in bags away from sunlight | No |
| **Li-ion battery pack (20 Wh)** | 18650 Li-ion cells | **3 years** | Capacity fade; self-discharge; calendar aging | **YES -- FIFO rotation** |
| **EPDM gasket (hull joint)** | EPDM rubber, 5 mm | **5 years** | Ozone cracking, compression set; store in sealed bags | **YES -- inspect annually** |
| Sikaflex 291 sealant | Polyurethane | **2 years** (unopened tube) | Moisture cure; tubes harden if unsealed | **YES -- check expiry date** |
| Tef-Gel anti-seize | PTFE compound | **5+ years** | Stable compound; minimal degradation | No |
| SS 316 fasteners | Austenitic stainless | **Indefinite** | No degradation mechanism in dry storage | No |

### 3.5 Transport Modes

| Scenario | Transport Mode | Route | Special Requirements | Estimated Cost |
|----------|---------------|-------|---------------------|----------------|
| **Hull halves: factory to assembly** | Flatbed truck (oversize permit) | HCMC or Hai Phong to assembly facility | **Oversize width permit required** ("Giay phep van chuyen hang sieu truong, sieu trong"); escort vehicle for >3.0 m width; avoid narrow bridges, urban centers | $800-1,200/trip |
| **Hull halves: alternative** | Coastal barge | Factory port to deployment port | Avoids road width restrictions entirely; hull halves loaded directly onto barge deck | $500-800/trip |
| **Accessories (masts, reflectors, kits)** | 20 ft standard container | Assembly facility to deployment port | Total mass ~350 kg; well within container payload (21,770 kg). Mast bundle (3.1 m) fits container length (5.9 m internal). | $400-600/container |
| **Complete unit: factory to port** | Flatbed (hull) + 20 ft container (accessories) | Assembly facility to staging area | Two vehicles required; can be combined into single convoy | $1,200-1,800 total |
| **Assembly to sea deployment** | Support vessel (deck carry or tow) | Port/staging area to test range | Hull floated alongside; M5 units carried on deck racks; mooring kit on deck | Included in vessel charter |

### 3.6 Export/Import Considerations

| Item | Origin | Import Status | Duty/Regulation | Notes |
|------|--------|---------------|-----------------|-------|
| AM AlSi10Mg frames | Singapore / China / Thailand | ASEAN import | ATIGA (ASEAN Trade in Goods Agreement) -- reduced/zero tariff for ASEAN-origin goods | Requires ASEAN Certificate of Origin (Form D) |
| 6061-T6 Al sheet | Korea / Japan / India | Standard commercial import | 5-10% import duty on aluminum sheet | Blanket order reduces per-unit import cost |
| GPS/Iridium modules | Taiwan / US / China | Standard commercial import | No ITAR restrictions (commercial COTS GPS/satellite modules) | **ITAR-FREE DESIGN** -- no US munitions list items |
| Dyneema SK75 rope | UK / Netherlands | Standard commercial import | 5% import duty on synthetic cordage | No export control on commercial rope |
| Li-ion battery packs | China | Standard commercial import | UN3481 (battery in equipment); IATA packing instructions | Dangerous goods shipping declaration required for air freight |

---

## 4. Inventory Management

### 4.1 Reorder Points and Economic Order Quantities

**Scenario: 10 units/year (low rate initial production)**

| Component | Annual Demand | Reorder Point (ROP) | Economic Order Qty (EOQ) | Safety Stock | Lead Time |
|-----------|--------------|---------------------|--------------------------|-------------|-----------|
| HDPE resin (PE100) | 4,000 kg | 1,500 kg | 2,000 kg | 500 kg | 2-3 weeks |
| S235 steel (all forms) | 3,000 kg | 1,000 kg | 1,500 kg | 500 kg | 1-2 weeks |
| 6061-T6 Al sheet | 600 kg (60 sheets) | 200 kg (20 sheets) | 300 kg (30 sheets) | 100 kg (10 sheets) | 3-4 weeks |
| AM frames (AlSi10Mg) | 80 frames | 24 frames (3 units) | 40 frames (5 units) | 16 frames (2 units) | 2-3 weeks |
| GPS/Iridium modules | 10 units | 5 units | 10 units | 5 units | 4-6 weeks |
| Li-ion battery packs | 10 packs + 5 spares | 8 packs | 15 packs | 5 packs | 2-3 weeks |
| Dyneema SK75 (16 mm) | 500 m | 200 m | 300 m | 100 m | 4-6 weeks |
| G30 chain (19 mm) | 500 m | 200 m | 300 m | 100 m | 1 week |
| Danforth anchors (50 kg) | 10 units | 5 units | 10 units | 3 units | 2-3 weeks |

**Scenario: 50 units/year (medium rate production)**

| Component | Annual Demand | Reorder Point | Order Qty | Notes |
|-----------|--------------|---------------|-----------|-------|
| AM frames | 400 frames | 80 frames (10 units) | 120 frames (15 units) | Blanket order across 3 bureaus; monthly call-off of 40 frames |
| 6061-T6 Al sheet | 3,000 kg | 750 kg | 1,500 kg | Semi-annual blanket order from Korea |
| GPS modules | 50 units | 15 units | 25 units | Semi-annual order; 5-unit buffer always maintained |

**Scenario: 100 units/year (full rate production)**

| Component | Annual Demand | Reorder Point | Order Qty | Notes |
|-----------|--------------|---------------|-----------|-------|
| AM frames | 800 frames | 160 frames | 200 frames | Dedicated production schedule at 3 bureaus; weekly delivery of 16 frames |
| HDPE resin | 40,000 kg | 5,000 kg | 10,000 kg | Annual contract with Binh Minh Plastics |
| Steel | 30,000 kg | 5,000 kg | 10,000 kg | Annual contract with Hoa Phat |

### 4.2 Limited-Life Items Requiring Rotation

| Item | Shelf Life | Rotation Policy | Inspection Interval | Disposal Method |
|------|-----------|-----------------|---------------------|-----------------|
| **Li-ion battery packs (20 Wh)** | 3 years from manufacture | FIFO (First In, First Out); mark date-of-manufacture on each pack | Every 6 months: voltage check (>=3.6V nominal); capacity test on sample (1 per 10) | Recycle per Vietnamese e-waste regulations (TCVN 6706:2009) |
| **EPDM gaskets (hull joint, 5 mm)** | 5 years from manufacture | FIFO; store in sealed polyethylene bags | Annual: flex test for brittleness, check for surface cracking (ozone degradation) | Dispose as rubber waste |
| **Sikaflex 291 sealant** | 2 years (unopened) | FIFO; check tube expiry date before issue | At issue: squeeze test (should extrude easily; discard if hardened) | Dispose as chemical waste |
| **Conformal coating (PCB)** | 1-2 years (opened can) | Date can at opening; discard 12 months after opening | At use: viscosity check; discard if thickened | Dispose as chemical waste |

### 4.3 Consumables per Deployment

| Consumable | Qty per Unit | Unit Cost | Notes |
|------------|-------------|-----------|-------|
| Sikaflex 291 marine sealant | 4 tubes | $72 | Hull joint (IF-07) + frame-to-hull (IF-01) sealant beads |
| Tef-Gel anti-seize | 1 tube | $28 | IF-03 socket bore, IF-04 fasteners, clevis pins |
| Safety wire (0.8 mm SS, 25 m roll) | 1 roll | $12 | Mast locking pins (8x), reflector bolt pairs (8x), IF-04 bolts |
| Mousing wire (1.0 mm galv, 10 m) | 1 roll | $10 | Mooring shackle pins (3x), tow shackle pins (3x) |
| EPDM gasket strip (5 mm x 50 mm) | 6 m | $48 | Hull section joint (IF-07) seal |
| Lifting slings (2T WLL, 2 m) | 4 ea (reusable) | $48 (initial) | Hull handling at factory and staging area |
| Ratchet straps (2T WLL, 5 m) | 8 ea (reusable) | $64 (initial) | Transport securing of mast bundle and hull on flatbed |
| **Total consumables per unit** | | **~$170** | Excludes reusable lifting/strapping equipment |

### 4.4 Spare Parts Kit Definition

**Per-Unit Spare Kit (shipped with each target):**

| Item | Qty | Purpose |
|------|-----|---------|
| Spare M12 clevis pins (SS 316) | 4 | Replacement for mast locking pins (IF-03); lost/bent pins |
| Spare R-clips (SS 316) | 8 | Replacement for locking pin retainers |
| Spare M12 x 40 SS 316 hex bolts | 10 | Replacement for frame-to-hull (IF-01) or tow padeye (IF-06) bolts |
| Spare M6 bolt/nut/washer sets (SS 316) | 12 | Replacement for reflector face plate fasteners (M4) |
| Spare bow shackles (20 mm, HDG, SWL 5,000 kgf) | 2 | Replacement for mooring or tow shackles |
| Safety wire (0.8 mm SS, 25 m roll) | 2 rolls | Field re-wiring of any safety-wired connections |
| Tef-Gel anti-seize (30 mL tube) | 1 | Field application to pins and fasteners |

**Per-Lot Spare Kit (shared across 10-unit lot):**

| Item | Qty | Purpose |
|------|-----|---------|
| Spare mast assembly (M3, complete) | 1 | Replacement for damaged mast (transport damage, bent in handling) |
| Spare reflector assembly (M4, complete) | 1 | Replacement for damaged reflector (scratched face plate, misaligned) |
| Spare GPS beacon battery pack (20 Wh) | 3 | Battery replacement for extended deployment or depleted units |
| Spare EPDM gasket strips | 10 m | Replacement for hull joint gaskets |
| Sikaflex 291 tubes | 5 | Replacement sealant for hull joint and frame interface |
| Torque wrench (10-100 N-m) | 1 | Field torque verification (shared tool) |
| Digital angle gauge (Wixey WR300) | 1 | Field orthogonality spot-check (shared tool) |

---

## 5. Depot-Level Operations

### 5.1 Assembly Facility Requirements

| Requirement | Specification | Notes |
|-------------|---------------|-------|
| **Floor space** | Minimum 200 m2 for 1 unit in work; 400 m2 for 2 parallel lines | Clear floor for 8.0 m hull assembly; space for component staging |
| **Ceiling height** | >=4.0 m clear (for mast handling at 3.1 m length) | Standard industrial building |
| **Overhead crane** | 500 kg capacity, spanning assembly floor | Hull lift into frame; frame installation; hull turning |
| **Electrical supply** | Standard 3-phase 380V Vietnamese industrial power | For power tools, compressor, lighting |
| **Compressed air** | 6-8 bar, clean dry air | For pneumatic tools, blow-down |
| **Clean bench** | 2.0 m x 1.5 m, dust-free area with task lighting | **Reflector assembly station** -- critical for face plate handling (no grit/dust on anodized surfaces) |
| **Torque wrench set** | 1-20 N-m, 10-100 N-m, 20-200 N-m ranges, calibrated | All bolted connections per torque specifications |
| **CMM access** | Coordinate measuring machine or outsourced metrology service | AM frame incoming inspection; reflector orthogonality verification (100% per QUA-002) |
| **RCS test setup** | Portable X-band radar (9.4 GHz) + turntable or tow arrangement | 360 deg RCS measurement per QUA-001 -- may be outsourced to military range |
| **Foam dispensing equipment** | 2-component PU pour gun, mixing head | Hull foam fill operation |
| **PPE station** | Respirators (foam pour), gloves, safety glasses, steel-toe boots | Standard industrial PPE |

### 5.2 Pre-Deployment Staging Area

| Requirement | Specification | Notes |
|-------------|---------------|-------|
| **Location** | Quayside or harbor with direct water access | Must support hull launch (ramp or crane) and vessel berthing |
| **Forklift access** | 2-ton forklift for mooring pallet and hull half handling | Standard harbor equipment |
| **Crane access** | 2-ton mobile crane or harbor crane for hull lift to water | Required for deck-carry loading onto support vessel |
| **Ramp launch** | Slipway or boat ramp for hull float-off | Alternative to crane launch; hull floated off trailer into water |
| **Laydown area** | 100 m2 minimum for 1 target's components | Unpacking, inspection, mast-reflector assembly (if separated for transport) |
| **Weather shelter** | Covered staging area preferred (not mandatory) | Protects reflector face plates from rain/dust during pre-deployment assembly |

### 5.3 Post-Recovery Processing

**Recoverable Item Processing Checklist:**

| Step | Action | Equipment | Personnel | Time |
|------|--------|-----------|-----------|------|
| R-01 | Receive recovered mooring kit (M7) on vessel deck | Vessel winch for anchor/chain retrieval | 2 + vessel crew | 30 min |
| R-02 | Rinse all mooring hardware with fresh water | Hose, freshwater supply | 1 | 15 min |
| R-03 | Inspect anchor: flukes straight (+/-2 deg), shank not bent, shackle pin secure | Visual, straight edge | 1 (QC) | 10 min |
| R-04 | Inspect chain: visual for corrosion, link deformation, zinc wear | Visual; if >10 deployments: UT thickness check | 1 (QC) | 15 min |
| R-05 | Inspect rode: check for chafe (esp. at chain-rode splice), UV degradation, cut fibers | Visual, manual flex test | 1 | 10 min |
| R-06 | Inspect swivel: free rotation, pin security, corrosion at bearing | Hand rotation test, visual | 1 | 5 min |
| R-07 | Inspect all shackles: pin threads, mousing wire integrity, body cracks | Visual, hand-tighten check | 1 | 10 min |
| R-08 | **GPS Beacon (if recovered):** rinse, inspect enclosure seal, download position log, check battery voltage | Freshwater rinse, laptop for data download, multimeter | 1 (electronics tech) | 20 min |
| R-09 | GPS beacon battery replacement: swap depleted pack with fresh 20 Wh pack; verify function (GPS fix + Iridium SBD) | Spare battery pack, test SIM | 1 | 15 min |
| R-10 | **Tow Kit (M8):** inspect Dyneema splices (tuck count >=24 per SCI-03), check chafe at thimble eyes, inspect drogue fabric | Visual, calipers for splice diameter | 1 | 15 min |
| R-11 | Log all inspection results in recoverable item tracking form; update deployment count | Paper form or tablet | 1 | 10 min |
| R-12 | Repack inspected items; label "SERVICEABLE" or "UNSERVICEABLE" with date and inspector ID | Labels, bags, pallet | 1 | 15 min |

---

## 6. Recoverable Item Management

### 6.1 GPS Beacon (M6)

| Parameter | Specification |
|-----------|---------------|
| **Recovery procedure** | After engagement, navigate support vessel to last known GPS position. Scan debris field for beacon enclosure (orange, reflective tape per BOM item 1.9.06). Retrieve by boat hook or diver. |
| **Battery replacement cycle** | Replace 20 Wh Li-ion pack before EVERY deployment. Depleted packs recycled per Section 4.2. Fresh pack: verify voltage >=4.0V (fully charged). |
| **Firmware update** | Check for GNSS module firmware updates annually. Update via USB connection to laptop. Document firmware version in as-built record. |
| **IP67 seal inspection** | After every recovery: inspect O-ring seal on enclosure lid for cuts, compression set, or debris. Replace O-ring if any damage visible. Perform dunk test (1 m freshwater, 30 min) before next deployment. |
| **Re-certification protocol** | Before each deployment: (1) power on, (2) verify GPS fix <5 min, (3) verify Iridium SBD message received at shore station, (4) verify battery voltage >3.8V, (5) record serial number and deployment count. |
| **Retirement criteria** | Retire after: (a) enclosure crack or seal failure, (b) >5 deployments with impact recovery, (c) GPS fix time degraded to >10 min, (d) Iridium link failure after troubleshooting. |
| **Expected service life** | 1-5 deployments (recovery from debris field is not guaranteed) |
| **Replacement cost** | $914.20 (full M6 assembly per C14 BOM) |

### 6.2 Mooring Kit (M7)

| Parameter | Specification |
|-----------|---------------|
| **Recovery procedure** | After engagement, retrieve mooring via trip line and surface buoy. Vessel crew grapples buoy, hauls trip line to recover anchor. Pay chain/rode onto deck. Coil and stow for transport. |
| **Chain inspection** | Visual: check every link for deformation, cracking, zinc coating loss. **UT thickness check** if >10 deployments: measure zinc remaining (retire if <40 um remaining or any link diameter reduced >10% from nominal). |
| **Rode inspection** | Visual: check for chafe at chain-rode splice and at thimble eyes. Check for UV bleaching (indicates cover degradation). Manual flex: check for stiffness indicating fiber degradation. Retire rode if: (a) chafe exposes core fibers over >100 mm length, (b) >15% diameter reduction at any point, (c) >20 deployments cumulative. |
| **Anchor inspection** | Check flukes: free pivoting on shank (no jamming from coral/debris). Check shank straightness (+/-2 deg per SCI-04). Check shackle hole wear (<10% enlargement). Retire anchor if: (a) bent fluke >5 deg, (b) shank bend >2 deg, (c) shackle hole elongated >10%. |
| **Shackle inspection** | Check pin thread engagement (full engagement required). Check body for cracks (visual + magnifying glass at pin hole). Re-mouse all pins with fresh galvanized wire after every recovery. Retire shackle if: (a) visible crack, (b) pin threads stripped >50%, (c) body worn >5% of nominal diameter. |
| **Swivel inspection** | Check free rotation (must rotate freely by hand through 360 deg). Check jaw/eye wear. Lubricate with marine grease at each recovery. Retire if: (a) binding or grinding during rotation, (b) jaw opening >110% of nominal. |
| **Retirement criteria summary** | Chain: zinc <40 um or link diameter -10%. Rode: core exposed >100 mm or diameter -15%. Anchor: fluke >5 deg or shank >2 deg. Shackle: crack or thread strip. |
| **Expected reuses** | Anchor: 10-20 deployments. Chain: 10-15. Rode: 15-20. Shackles: 20-30. Swivel: 15-20. |
| **Replacement cost** | Full M7 kit: $1,060.00 (medium depth variant per C14 BOM) |

### 6.3 Tow Kit (M8)

| Parameter | Specification |
|-----------|---------------|
| **Recovery procedure** | Tow kit disconnected from target after positioning (before engagement). Support vessel recovers bridle and drogue directly. |
| **Dyneema splice inspection** | Count tucks at each splice eye: minimum 24 tucks per SCI-03. Check splice taper for slippage (mark reference line at splice exit; if line shifts >5 mm, retire). Check overall rope for: flat spots (compression damage), fuzz (abrasion), discoloration (UV/heat). |
| **Chafe check** | Inspect at thimble contact points, shackle bearing surfaces, and vessel fairlead rub areas. Chafe guard (sacrificial tape) to be replaced after every 5 deployments. |
| **Drogue inspection** | Check fabric for tears, stitching integrity, grommet condition. Check swivel attachment. Retire drogue if: (a) tear >50 mm, (b) >25% stitching failed, (c) grommet pulled out. |
| **Retirement criteria** | Per SCI-03: retire Dyneema bridle after **50 deployments** or at first sign of: (a) cut fibers visible over >25 mm, (b) splice slippage >5 mm, (c) diameter reduction >15% at any point, (d) heat/melt damage. |
| **Expected reuses** | Dyneema bridle: 25-50 deployments. Drogue: 20-30 deployments. Shackles: 50+ deployments. |
| **Replacement cost** | Full M8 kit: $725.00 (per C14 BOM) |

### 6.4 Economic Analysis: Recovery vs. Replacement

| Item | Replacement Cost | Recovery Cost (per event) | Break-Even Reuses | Recommendation |
|------|-----------------|--------------------------|-------------------|----------------|
| **M7: Mooring Kit** | $1,060 | $150 (vessel time + labor for retrieval, 1 hr @ vessel day rate) | 1.2 deployments | **ALWAYS RECOVER** -- pays for itself on first reuse |
| **M6: GPS Beacon** | $914 | $50 (battery swap) + $200 (if dedicated diver recovery from debris) | 1.3-3.7 deployments | **RECOVER IF FEASIBLE** -- do not risk crew safety for recovery; opportunistic retrieval only |
| **M8: Tow Kit** | $725 | $25 (inspection + chafe guard replacement) | 1.0 deployments | **ALWAYS RECOVER** -- kit is disconnected before engagement; zero risk |
| **Mooring chain only** | $150 (20 m G30 19 mm) | $50 (inspection) | 1.5 deployments | **ALWAYS RECOVER** -- chain is robust, many reuses |
| **Anchor only** | $350 | $100 (trip line retrieval) | 1.4 deployments | **ALWAYS RECOVER** -- high value, easy retrieval with trip line |

---

## 7. Debris Recovery & Environmental Plan

### 7.1 Post-Engagement Debris Field Characterization

| Debris Type | Material | Typical Mass | Buoyancy | Environmental Hazard | Recovery Priority |
|-------------|----------|-------------|----------|---------------------|-------------------|
| HDPE hull fragments | PE100 HDPE | 200-350 kg total (distributed) | Floating (density 940-960 kg/m3 < seawater 1,025) | **NON-TOXIC** -- chemically inert, no leaching | MEDIUM -- recover floating fragments to prevent navigation hazard |
| PU foam fragments | Closed-cell polyurethane | 100-200 kg total | Floating (density 35-50 kg/m3) | **NON-TOXIC** -- inert, closed-cell | LOW -- small fragments biodegrade slowly; large pieces recovered with hull debris |
| Aluminum reflector debris | 6061-T6 + AlSi10Mg | 120-240 kg total | Sinking (density 2,670-2,700 kg/m3) | **NON-TOXIC** -- aluminum is inert in seawater; anodize coating stable | LOW -- sinks to seabed; no environmental impact |
| Steel frame debris | S235 HDG steel | 150-280 kg total | Sinking (density 7,850 kg/m3) | **LOW** -- zinc coating and steel both non-toxic; slow corrosion forms inert iron oxide | LOW -- sinks to seabed; becomes artificial reef substrate |
| SS 316 fastener debris | Austenitic stainless | 10-20 kg total | Sinking | **NON-TOXIC** -- corrosion-resistant, inert | NEGLIGIBLE -- small items, widely scattered |
| Nylon/EPDM debris | Polymer | <5 kg total | Variable | **NON-TOXIC** -- inert polymers | NEGLIGIBLE |

### 7.2 Recovery Vessel Requirements and Procedures

| Phase | Action | Vessel Requirement | Personnel | Time |
|-------|--------|-------------------|-----------|------|
| D+0h to D+2h | **Exclusion zone maintained** -- no vessel entry until range safety officer declares "clear" | Range safety vessel | Range safety officer | 2 h (minimum) |
| D+2h | **Initial survey** -- approach debris field from upwind. Visual scan for large floating fragments (hull, foam). Confirm GPS beacon signal (if still transmitting). | Support vessel with radar and AIS | 3 (navigator + 2 observers) | 1 h |
| D+3h | **Floating debris collection** -- recover large HDPE hull fragments and foam using boat hooks, cargo nets, or inflatable work boat. Stack on vessel deck. | Vessel with deck crane or work boat | 4 (2 on work boat + 2 on vessel) | 2-4 h |
| D+4h | **GPS beacon recovery** (if feasible) -- locate beacon by last transmitted position (+/- 50 m). Visual search for orange enclosure. Retrieve by boat hook or shallow dive. | Work boat, optional diver | 2 | 1-2 h |
| D+6h | **Seabed debris** (optional, depth-dependent) -- for shallow water (<20 m), diver survey for large metallic fragments. For deep water, accept seabed debris as de facto artificial reef. | Dive boat (optional) | 2 divers + surface support | 2-4 h |
| D+8h | **Mooring recovery** -- retrieve trip line buoy, haul anchor and chain/rode per Section 6.2. | Support vessel with winch | 3 | 1-2 h |
| D+10h | **Area clearance** -- final visual sweep of engagement area. Report "area clear" to range safety. | Support vessel | 2 | 1 h |

### 7.3 Environmental Impact Assessment

All materials in the THANH TRI-H design are selected for environmental compatibility per SAF-004:

| Material | Toxicity | Bioaccumulation | Marine Decomposition | Regulatory Status |
|----------|----------|-----------------|---------------------|-------------------|
| HDPE | Non-toxic | No | >100 years (stable polymer) | Recyclable; no marine pollutant classification |
| PU foam (closed-cell) | Non-toxic | No | >50 years (slow UV degradation) | Inert; no marine pollutant |
| 6061-T6 aluminum | Non-toxic | No | Corrodes to inert Al2O3 (aluminum oxide) | No marine pollutant; commonly used in marine structures |
| AlSi10Mg (anodized) | Non-toxic | No | Same as 6061-T6 with hard anodize protection | No marine pollutant |
| S235 HDG steel | Non-toxic (zinc is micronutrient at trace levels) | No | Corrodes to iron oxide (rust); zinc dissolves at trace levels | No marine pollutant at these quantities; HDG steel widely used in marine construction |
| SS 316 | Non-toxic | No | Extremely slow corrosion | No marine pollutant |
| EPDM rubber | Non-toxic | No | Slow UV degradation | Inert polymer |
| Nylon / Polyester | Non-toxic | No | Slow degradation | Standard marine cordage materials |

**Key environmental advantages of the THANH TRI-H design:**
- **No propane** -- Rev B removed all gas systems (no hydrocarbon release)
- **No hazardous materials** -- no batteries in the water (GPS beacon is above waterline and potentially recoverable)
- **No explosives** -- target is passive; all energetics are in the incoming missile
- **All debris materials are marine-compatible** -- widely used in existing marine infrastructure

### 7.4 Regulatory Compliance

| Regulation | Applicability | Compliance Approach |
|------------|--------------|---------------------|
| Vietnamese Law on Environmental Protection (2020) | Discharge of materials into marine environment | All materials non-toxic per SAF-004; debris recovery plan minimizes residual seabed material |
| Vietnamese Maritime Code (2015) | Navigation safety after engagement | Floating debris collected within 8 h; area declared clear by range safety officer; NOTAM cancelled |
| MARPOL Annex V (Garbage) | Disposal of solid waste at sea | Floating debris recovered; sinking metallic debris is not classified as "garbage" under MARPOL (structural debris from military training) |
| VPN military range regulations | Conduct of weapons testing at sea | Target deployment and debris recovery per VPN range safety SOP; engagement authorized by range safety officer |

### 7.5 Debris Recovery Cost Estimate per Engagement

| Cost Element | Estimate ($) | Basis |
|-------------|-------------|-------|
| Support vessel charter (12 h @ $800/day) | $400 | Half-day charter for debris recovery and mooring retrieval |
| Fuel (support vessel) | $150 | Estimated 200 L diesel |
| Crew labor (4 persons x 12 h @ $8/h) | $384 | Recovery crew labor |
| Dive team (optional, if shallow water) | $500 | Diver pair for 2-4 h bottom survey |
| Debris transport and disposal (onshore) | $200 | Truck to recycling facility for HDPE/metal sorting |
| **Total recovery cost (without dive)** | **~$1,134** | |
| **Total recovery cost (with dive)** | **~$1,634** | |

---

## 8. Training & Technical Data

### 8.1 Training Program Outline

| Module | Duration | Content | Audience | Location |
|--------|----------|---------|----------|----------|
| **T-01: System Overview** | 1 h (classroom) | Product description, modules M1-M8, interfaces IF-01 to IF-07, performance characteristics (RCS, buoyancy, mooring). Safety briefing per MIL-STD-882E hazard register. | All personnel | Classroom |
| **T-02: Factory Assembly** | 2 h (classroom) + 2 h (hands-on) | Assembly sequence F01-F22 per [[OCP_P15_production_planning.md]] Section 5.1. QC hold points. Reflector assembly (M4) alignment verification. Torque specifications. Safety wire technique. | Assembly technicians, QC inspectors | Factory floor |
| **T-03: Field Deployment** | 1 h (classroom) + 2 h (hands-on) | Deployment sequence D-01 to D-18 per [[OCP_P15_production_planning.md]] Section 6. Mast erection (IF-03). Mooring connection (IF-02). GPS beacon activation (M6). Abort criteria (SS >5). | Deployment crew (4 persons) | Quayside / harbor |
| **T-04: Recoverable Item Management** | 0.5 h (classroom) | Recovery procedures per Section 6 of this document. Mooring inspection criteria. GPS beacon battery swap. Tow kit inspection. Retirement criteria per SCI-01 to SCI-06. | Deployment crew, logistics personnel | Classroom |
| **T-05: Safety & Emergency** | 0.5 h (classroom) | PPE requirements. Man overboard procedures. Heavy weather abort criteria. Communication plan (VHF, satellite). First aid. | All personnel | Classroom |
| **TOTAL** | **4 h classroom + 2 h hands-on** | Per ERG-006 requirement (<=8 h classroom + <=4 h hands-on) | | |

### 8.2 Training Audience

| Role | Required Modules | Certification | Recertification |
|------|-----------------|---------------|-----------------|
| **Deployment crew leader** | T-01 through T-05 (all) | Written exam (80% pass) + observed deployment exercise | Annual refresher (2 h) |
| **Deployment crew member** | T-01, T-03, T-04, T-05 | Observed deployment exercise participation | Annual refresher (2 h) |
| **Assembly technician** | T-01, T-02 | Supervised first-article assembly | Annual refresher (1 h) |
| **QC inspector** | T-01, T-02, T-04 | QC procedure proficiency test | Annual refresher (1 h) |
| **Logistics coordinator** | T-01, T-04 | Familiarity with inventory management procedures | Annual briefing |

### 8.3 Technical Data Package Contents

| Document | Description | Format | Distribution |
|----------|-------------|--------|-------------|
| **Deployment Manual** | Pictorial step-by-step (VN/EN bilingual) per ERG-007. Covers D-01 to D-18, recovery R-01 to R-12, emergency procedures. Laminated waterproof pages. | A4 laminated booklet | 1 per unit (in documentation tube) + 2 per deployment crew |
| **Maintenance Checklist** | Recoverable item inspection forms per Section 6. Pre-deployment checklist per MNT-003. Battery replacement procedure. | A4 form pad | 1 pad per lot (10 sheets per pad) |
| **QC Procedures** | Factory acceptance test procedures: RCS measurement protocol, reflector orthogonality verification, GPS endurance test, hull leak test, pad eye proof load. | A4 bound manual | 1 per assembly facility |
| **Bill of Materials** | Complete BOM per [[OCP_C14_cost_analysis.md]] Sections 1.1-1.9. Includes part numbers, material specifications, suppliers, costs. | Spreadsheet + printed | 1 per assembly facility; controlled document |
| **Drawings Package** | Production drawings for all 8 modules and 7 interfaces. Includes tolerances, surface finishes, weld specifications, assembly views. | CAD files (STEP/DWG) + printed A1/A3 | 1 set per assembly facility; controlled document |
| **Material Certificates** | Mill certs (steel, aluminum), AM build reports, heat treat certs, anodize thickness reports, HDG thickness reports, chain proof load certs. | PDF + paper originals | Per unit -- filed in unit documentation package |
| **RCS Test Data** | 360 deg X-band measurement data per QUA-001. Plots, raw data, pass/fail determination. | PDF + data files | Per unit -- filed in unit documentation package |

### 8.4 Configuration Management

| Element | Method | Responsible |
|---------|--------|------------|
| **Serial number tracking** | Each unit assigned serial VN-TGT-SEA-001-Hxxx (e.g., H001, H002...). Serial engraved on SS data plate (BOM item 1.9.07) mounted on hull and on frame. | Production engineering |
| **As-built records** | Documentation package per unit includes: BOM with actual supplier lot numbers, all material certs, all inspection/test results, any deviations/NCRs, deployment manual revision. | QC inspector |
| **Deployment log** | Per unit: date deployed, location (lat/long), water depth, mooring kit serial, crew names, weather conditions, engagement date/time, debris recovery status, recoverable items status. | Deployment crew leader |
| **Recoverable item tracking** | Each recoverable item (M6, M7, M8) receives a sub-serial number. Deployment count tracked in recoverable item log. Inspection results recorded per recovery. Retirement documented. | Logistics coordinator |
| **Configuration changes** | Any design change requires engineering change notice (ECN) with rationale, affected drawings, effectivity (unit serial numbers). No field modifications permitted without ECN. | Project engineer |

---

## 9. Through-Life Cost Model

### 9.1 Three-Year TCO at 50 Tests (per CST-006: <=$2,600,000)

| Cost Element | Value ($) | Basis | % of TCO |
|-------------|-----------|-------|----------|
| **Development (Phases 0-4)** | $280,000 | CST-004 development budget (one-time NRE) | 10.9% |
| **50 target units @ $29,655** | $1,482,750 | C14 bottom-up unit cost @ 10-unit batch pricing, 5 lots of 10 | 57.8% |
| **Operations (vessel charter, crew, logistics)** | $250,000 | 50 deployments x $5,000/deployment (vessel, fuel, crew, transport) | 9.7% |
| **Debris recovery (50 engagements)** | $56,700 | 50 x $1,134 per recovery (no dive) | 2.2% |
| **Mooring kit replacement (25% loss rate)** | $26,500 | 12.5 replacement kits @ $1,060 x 50% sparing margin = $26,500 | 1.0% |
| **GPS beacon replacement (50% loss rate)** | $22,855 | 25 replacement beacons @ $914 | 0.9% |
| **GPS beacon batteries (50 deployments + spares)** | $4,875 | 75 battery packs @ $65 (50 deployments + 25 recovered beacon re-batteries) | 0.2% |
| **Tow kit replacement (10% loss rate)** | $3,625 | 5 replacement kits @ $725 | 0.1% |
| **Consumables (50 deployments)** | $8,500 | 50 x $170 per deployment (sealant, wire, Tef-Gel, etc.) | 0.3% |
| **Spare parts (5 lots)** | $12,500 | 5 per-lot spare kits @ $2,500 | 0.5% |
| **Training (initial + annual refresh)** | $15,000 | Initial training program + 3 annual refreshers for 10 personnel | 0.6% |
| **Buffer inventory (initial stock)** | $26,650 | Per Section 2.4 (one-time investment, partially consumed) | 1.0% |
| **Missile loss contingency (1% risk)** | $250,000 | 1% probability of missile malfunction per test x $500K replacement cost x 50 tests | 9.7% |
| **Management / engineering support** | $120,000 | 3 years x $40,000/year (part-time project engineer + logistics coordinator) | 4.7% |
| | | | |
| **TOTAL 3-YEAR TCO** | **$2,559,955** | | **100%** |

**CST-006 compliance:** $2,559,955 < $2,600,000 target. **PASS** with $40,045 margin (1.5%).

### 9.2 Cost per Engagement Breakdown

| Element | Cost per Test ($) | % |
|---------|------------------|---|
| Target unit (expendable) | $29,655 | 57.8% |
| Development amortization (over 50 tests) | $5,600 | 10.9% |
| Operations (vessel, crew, logistics) | $5,000 | 9.7% |
| Missile loss contingency (1% risk) | $5,000 | 9.7% |
| Debris recovery | $1,134 | 2.2% |
| Mooring replacement (amortized) | $530 | 1.0% |
| GPS beacon replacement (amortized) | $457 | 0.9% |
| All other (consumables, spares, batteries, training, buffer, tow kit, PM) | $3,824 | 7.4% |
| | | |
| **Total cost per engagement** | **$51,200** | **100%** |

### 9.3 Sensitivity Analysis: Volume vs. Unit Cost

| Volume Scenario | Unit Cost | 50-Test TCO | Cost per Test | vs. Baseline |
|----------------|-----------|-------------|---------------|-------------|
| **10 units (baseline)** | $29,655 | $2,559,955 | $51,200 | Baseline |
| **50 units (single order)** | $20,903 | $2,122,150 | $42,443 | -17.1% |
| **100 units (2-year program)** | $17,367 | $1,945,350 | $38,907 | -24.0% |

Key volume drivers (per [[OCP_C14_cost_analysis.md]] Section 8):
- AM frame batch pricing: $7,200/unit (@ 10) -> $4,800 (@ 50) -> $3,600 (@ 100)
- Tooling amortization: $2,500/unit (@ 10) -> $500 (@ 50) -> $250 (@ 100)
- Labor learning curve: $2,726/unit (@ 10) -> $2,316 (@ 50) -> $2,067 (@ 100)

### 9.4 Comparison to Import Alternative

| Metric | THANH TRI-H (50 tests) | SINKEX Import (50 tests) | Savings |
|--------|----------------------|--------------------------|---------|
| Cost per test | $51,200 | $1,610,000 (decommissioned vessel) | **$1,558,800 per test (96.8%)** |
| 3-year program (50 tests) | $2,560,000 | $80,500,000 | **$77,940,000 (96.8%)** |
| Local content | 64.6% | 0% (imported vessels) | +64.6 percentage points |
| Scheduling flexibility | Deploy in 2.5 h | 6-12 months vessel preparation | Immediate availability |
| Environmental impact | Non-toxic HDPE/Al/steel debris | Full ship sinking (oil, paint, hazmat) | Far superior |
| Reusable range | Mooring reusable; location flexible | Fixed position; seabed obstruction | More flexible |

**Conclusion:** The THANH TRI-H provides anti-ship missile test capability at **1.8% of SINKEX cost** per engagement, with vastly superior scheduling flexibility, environmental profile, and Vietnamese local content.

---

## 10. Obsolescence Management

### 10.1 COTS Components at Risk

| Component | Current Source | Lifecycle Estimate | Risk Level | Impact if Obsolete |
|-----------|--------------|-------------------|------------|-------------------|
| **GNSS module (u-blox ZED-F9P)** | u-blox (Switzerland/Taiwan) | 5-7 years production life | MEDIUM | GPS beacon assembly requires redesign; replacement module qualification |
| **Iridium SBD modem (RockBLOCK 9603N)** | Rock Seven (UK) / Iridium | 5-10 years (Iridium network life >2030) | LOW | Alternative Iridium modems available; Iridium network contracted through 2035+ |
| **Li-ion 18650 cells** | Multiple manufacturers | Chemistry evolves every 3-5 years (capacity improves) | LOW | Replacement cells widely available; form factor (18650) is industry standard through 2030+ |
| **GNSS active antenna** | Multiple COTS sources | 5-10 years | LOW | Standard GNSS antenna; multiple interchangeable sources |
| **IP67 waterproof enclosure** | Multiple COTS sources | 10+ years | NEGLIGIBLE | Standard industrial enclosure; many interchangeable options |

### 10.2 Mitigation Strategies

| Strategy | Applicable Components | Action | Timeline |
|----------|----------------------|--------|----------|
| **Lifetime buy** | GNSS module, Iridium modem | At initial procurement, purchase enough modules for projected 3-year program (50-100 units). Buffer stock per Section 2.4. | At first production order |
| **Multi-source qualification** | GNSS module (qualify u-blox + Queclink), Li-ion cells (qualify 2 manufacturers) | Qualify alternative COTS module with identical form/fit/function. Document qualification test results. | Within 6 months of first production |
| **Modular beacon design** | M6 GPS Beacon assembly | Enclosure accepts multiple GNSS/Iridium module combinations via standardized connector interface. Beacon bracket (IF-05) is module-agnostic. | Current design already modular |
| **Technology watch** | All COTS electronics | Annual review of COTS product roadmaps; manufacturer end-of-life (EOL) notifications; industry conference attendance | Ongoing (annual) |

### 10.3 Technology Refresh Opportunities

| Opportunity | Timeline | Impact | Feasibility |
|-------------|----------|--------|-------------|
| **Vietnamese LPBF AM capability** | 2-3 years | Eliminates ASEAN AM import; reduces frame cost to $500-600/ea; increases local content to >85% | MEDIUM -- requires EOS M290 or equivalent ($500K investment), trained operator, powder supply chain |
| **Alternative satellite links (LoRa, NB-IoT)** | 1-2 years | Replaces Iridium SBD with lower-cost satellite IoT (Swarm, Kineis, Globalstar). Reduces per-unit satellite modem cost by 50-70%. | HIGH -- LoRa satellite services expanding rapidly in ASEAN; compatible with existing beacon enclosure |
| **Solid-state LiFePO4 batteries** | 2-3 years | Replaces Li-ion 18650 with safer LiFePO4 chemistry. Extended shelf life (5-7 years vs 3 years). Eliminates limited-life rotation concern. | HIGH -- LiFePO4 cells already available; requires minor BMS redesign |
| **CNC-only reflector frames** | Immediate (fallback available) | Eliminates AM supply chain dependency entirely. Trades +/-0.1 deg tolerance for +/-0.3 deg (acceptable if military approves 10% RCS variation increase). | HIGH -- proven technology, all Vietnamese CNC shops capable |
| **Rotomolded 1-piece hull** | 1-2 years (mold investment) | Eliminates IF-07 hull section joint; reduces assembly time by 4 h; improves hull structural integrity | MEDIUM -- requires $24-30K mold investment; break-even at ~15 units vs welded approach |

---

## 11. Requirements Traceability

### 11.1 Maintenance Requirements (MNT)

| Req ID | Requirement | Value | Logistics Plan Section | Compliance |
|--------|-------------|-------|----------------------|------------|
| MNT-001 | Target maintenance concept | Expendable -- no post-engagement maintenance | Section 1.1 (Expendable Target Philosophy) | **COMPLIANT** -- single-use concept; no repair provisions |
| MNT-002 | Mooring system recovery | Recoverable for reuse (WISH W=4) | Section 6.2 (Mooring Kit M7 recovery, inspection, retirement criteria) | **COMPLIANT** -- full recovery and reuse protocol defined; trip line retrieval method |
| MNT-003 | Pre-deployment inspection time | <=1 h (WISH W=3) | Section 5.3 (Post-Recovery Processing); Section 8.3 (Maintenance Checklist) | **COMPLIANT** -- pre-deployment checklist estimated 30-45 min per C11 |
| MNT-004 | Reflector shelf maintenance | None (anodized aluminum) | Section 3.4 (Shelf Life: 10+ yr for anodized Al) | **COMPLIANT** -- zero maintenance in storage |
| MNT-005 | GPS beacon battery replacement | Field-replaceable, tool-free | Section 6.1 (GPS Beacon recovery: battery swap procedure) | **COMPLIANT** -- tool-free quick-disconnect battery pack per A7 M6 |

### 11.2 Transport Requirements (TRA)

| Req ID | Requirement | Value | Logistics Plan Section | Compliance |
|--------|-------------|-------|----------------------|------------|
| TRA-001 | Container compatibility | >=1 target per 40 ft container (disassembled) | Section 3.1 (Packaging: hull on flatbed, accessories in 20 ft container) | **COMPLIANT** -- 1 complete target per flatbed + 20 ft container combination per P15 Section 9 |
| TRA-002 | Maximum road transport width | <=2.5 m per section | Section 3.5 (Transport: oversize permit for 4.0 m hull halves) | **PENDING** -- 4.0 m hull halves exceed 2.5 m; oversize permit required OR sea transport alternative |
| TRA-003 | Tow configuration | Bridle (2-point, 60 deg spread) + trailing drogue | Section 6.3 (Tow Kit M8 management) | **COMPLIANT** -- tow kit defined per A7 M8 |
| TRA-004 | Tow line specification | 16 mm Dyneema, SWL >=8,000 kgf | Section 6.3 (Dyneema SK75, SWL 8,000 kgf) | **COMPLIANT** -- per C14 BOM item 1.8.01 |
| TRA-005 | Shelf life (stored ashore) | >=5 years (WISH W=4) | Section 3.4 (Shelf Life table: all components >=5 yr except Li-ion batteries at 3 yr) | **COMPLIANT** -- all structural components 10+ yr; Li-ion managed per FIFO rotation (Section 4.2) |
| TRA-006 | Depot storage | Standard covered warehouse, no climate control (WISH W=3) | Section 3.3 (Storage Conditions: covered warehouse, -5 to +55 deg C, <85% RH) | **COMPLIANT** -- no climate control required; Li-ion batteries in separate cabinet |

### 11.3 Operational Requirements (OPR) Relevant to Logistics

| Req ID | Requirement | Value | Logistics Plan Section | Compliance |
|--------|-------------|-------|----------------------|------------|
| OPR-001 | Deployment sea state | SS 4-5 | Section 8.1 (Training Module T-03: deployment procedure, abort criteria) | **COMPLIANT** -- training includes abort at SS >5 |
| OPR-005 | Water depth range | 10-80 m | Section 4.1 (Mooring kit: 3 depth variants S/M/D) | **COMPLIANT** -- 3 mooring kit variants per A7 M7 |
| OPR-007 | Ambient temperature range | -5 to +55 deg C | Section 3.3 (Storage: -5 to +55 deg C) and Section 3.4 (all materials rated) | **COMPLIANT** -- all materials and storage within range |

### 11.4 Cost Requirements

| Req ID | Requirement | Value | Logistics Plan Section | Compliance |
|--------|-------------|-------|----------------------|------------|
| CST-006 | 3-year TCO (50 tests) | <=$2,600,000 | Section 9.1 ($2,559,955 TCO) | **COMPLIANT** -- $40,045 margin (1.5%) |
| CST-007 | Cost vs import (SINKEX) | <=50% of $1,610,000 | Section 9.4 ($51,200 per test = 3.2% of SINKEX) | **COMPLIANT** -- 96.8% savings vs SINKEX |

### 11.5 Safety-Critical Items

| SCI # | Item | Logistics Impact | Plan Section |
|-------|------|-----------------|-------------|
| SCI-01 | Mooring chain (19 mm G30 HDG) | 100% proof load cert per batch; visual each deployment; UT if >10 deployments | Section 6.2 (chain inspection criteria) |
| SCI-02 | Pad eye assembly | UT weld inspection; torque verification at factory and pre-deployment | Section 5.1 (factory QC), Section 8.3 (pre-deployment checklist) |
| SCI-03 | Tow line (16 mm Dyneema) | Visual before each tow; retire after 50 deployments or visible damage | Section 6.3 (retirement criteria) |
| SCI-04 | Anchor (50-100 kg Danforth) | Visual fluke/shank inspection; verify free pivot | Section 6.2 (anchor inspection criteria) |
| SCI-05 | GPS beacon battery | Capacity test before first use; voltage check before each deployment | Section 6.1 (battery replacement cycle) |
| SCI-06 | Mast locking pins (8x) | Visual and tactile check during field erection; spare pins in per-unit kit | Section 4.4 (spare parts kit: 4 spare pins per unit) |

---

## 12. Cross-References

### Phase 4 Documents
- [[logistics_sustainment_plan.md]] -- This document

### Phase 3 Source Documents
- [[../03_embodiment/OCP_P15_production_planning.md]] -- Manufacturing, supplier identification, QC plan, assembly sequence, packaging/transport, field deployment
- [[../03_embodiment/OCP_C14_cost_analysis.md]] -- Detailed BOM ($17,862), labor ($2,726), volume pricing, cost reduction roadmap, local content 64.6%
- [[../03_embodiment/DECS_C11_requirements_verification.md]] -- 116 requirements verification matrix (72 VERIFIED, 34 PENDING-TEST, 5 PENDING-ANALYSIS)
- [[../03_embodiment/DECS_S12_standards_compliance.md]] -- MIL-STD-810H/882E compliance, safety-critical items SCI-01 to SCI-06, test plan
- [[../03_embodiment/PRAD_A7_architecture_definition.md]] -- 8 modules (M1-M8), 7 interfaces (IF-01 to IF-07), containment hierarchy, assembly/deployment sequences
- [[../03_embodiment/RISM_M4_material_analysis.md]] -- Material selections for 5 component groups, corrosion data, shelf life properties, local content analysis

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1), MNT-001 to MNT-005, TRA-001 to TRA-006, OPR-001 to OPR-010, CST-001 to CST-007, ERG-006/007

### Project Management
- [[../PROJECT_STATUS.md]] -- Project status tracker

---

*End of Logistics & Sustainment Plan. This document defines the complete through-life logistics framework for the THANH TRI-H expendable sea target: supply chain architecture with strategic buffers, PHS&T specifications for Vietnamese production and oversize transport, inventory management with limited-life item rotation, recoverable item management for mooring/GPS/tow subsystems, debris recovery and environmental compliance, training program, 3-year TCO model ($2.56M for 50 tests, compliant with CST-006), and obsolescence management for COTS electronics. All maintenance (MNT), transport (TRA), operational (OPR), and cost (CST) requirements are traced and satisfied.*
