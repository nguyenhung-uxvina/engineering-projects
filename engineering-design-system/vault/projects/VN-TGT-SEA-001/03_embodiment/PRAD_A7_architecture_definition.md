---
project: VN-TGT-SEA-001
phase: 3
type: embodiment_design
step: "A7 — Architecture Definition"
group: PRAD
version: 1.0
created: 2026-02-10
status: draft
---

# Step A7: Architecture Definition — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Define the complete physical system architecture — modules, interfaces, assembly sequence, and traceability to functions and requirements.
**Method:** Pahl & Beitz Embodiment Design, PRAD Step A7 — Architecture Definition
**Input:** [[RISM_R1_requirements_identification.md]] (74 direct embodiment requirements), [[../02_conceptual/function_structure.md]] (F1-F7), [[../02_conceptual/concept_selection.md]] (Concept A, 81.8%)
**Selected Concept:** Concept A "Baseline Optimized" — 8.0 m HDPE pontoon, 8 hybrid AM/CNC corner reflectors on steel masts, SPM catenary mooring

---

## 1. System Architecture Overview

### 1.1 Layered Block Diagram

```
SYSTEM ARCHITECTURE — VN-TGT-SEA-001 "THANH TRI-H"
===============================================================================

  LAYER 0: STORM MOORING                    LAYER 6: TOW SYSTEM
  ┌──────────────────────┐                   ┌──────────────────────┐
  │  M7: Mooring Kit     │                   │  M8: Tow Kit         │
  │  ┌────────────────┐  │                   │  ┌────────────────┐  │
  │  │ Danforth/Bruce │  │                   │  │ Dyneema bridle │  │
  │  │ anchor 30-50kg │  │                   │  │ 16mm, 2-point  │  │
  │  ├────────────────┤  │                   │  ├────────────────┤  │
  │  │ G30 chain      │  │                   │  │ Trailing drogue│  │
  │  │ 12-16mm HDG    │  │                   │  ├────────────────┤  │
  │  ├────────────────┤  │                   │  │ Shackles +     │  │
  │  │ Polyester rode │  │                   │  │ thimbles       │  │
  │  │ 20mm braided   │  │                   │  └────────────────┘  │
  │  ├────────────────┤  │                   └──────────┬───────────┘
  │  │ Swivel+shackles│  │                              │ IF-06
  │  └────────────────┘  │                              │
  └──────────┬───────────┘                              │
             │ IF-02                                    │
             │                                          │
  ═══════════╪══════════════════════════════════════════╪═══════════
  LAYER 1+2: HULL + STRUCTURAL FRAME                    │
  ┌──────────┴──────────────────────────────────────────┴──────────┐
  │  M1: Hull Assembly (HDPE 8.0m circular pontoon + PU foam)      │
  │  ┌────────────────────────────────────────────────────────────┐ │
  │  │                                  IF-01                     │ │
  │  │  M2: Structural Frame Assembly (S235 HDG steel)            │ │
  │  │  ┌───────────────────────────────────────────────────────┐ │ │
  │  │  │  Central pad eye (200x200x10mm) ← IF-02 (mooring)    │ │ │
  │  │  │  2x Tow padeyes (port/stbd) ← IF-06 (tow bridle)    │ │ │
  │  │  │  8x Deck sockets at 45 deg spacing ← IF-03 (masts)   │ │ │
  │  │  │  Perimeter angles + cross members                     │ │ │
  │  │  └───────────────────────────────────────────────────────┘ │ │
  │  │  Hull section joint (if 2-section) ← IF-07                 │ │
  │  └────────────────────────────────────────────────────────────┘ │
  └─────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬────────┘
        │      │      │      │      │      │      │      │
       IF-03  IF-03  IF-03  IF-03  IF-03  IF-03  IF-03  IF-03
        │      │      │      │      │      │      │      │
  ═════╪══════╪══════╪══════╪══════╪══════╪══════╪══════╪══════════
  LAYER 2.5+3: MAST-REFLECTOR UNITS (x8)                │
  ┌─────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴────────┐
  │  M5: Mast-Reflector Unit (x8 identical, pre-assembled)         │
  │  ┌────────────────────────────────────────────────────────────┐ │
  │  │  M3: Mast Assembly                                        │ │
  │  │  ┌──────────────────────────────────────────────────────┐  │ │
  │  │  │ 60mm OD x 4mm wall galv steel tube, ~3.0m length    │  │ │
  │  │  │ Base plate (welded) — engages deck socket via IF-03  │  │ │
  │  │  │ Locking pin hole at 150mm above base plate           │  │ │
  │  │  │ Top plate (welded) — 4-bolt + 2-pin pattern IF-04   │  │ │
  │  │  └──────────────────────────┬───────────────────────────┘  │ │
  │  │                        IF-04│                               │ │
  │  │  M4: Reflector Assembly     │                               │ │
  │  │  ┌──────────────────────────┴───────────────────────────┐  │ │
  │  │  │ 1x AM AlSi10Mg frame (orthogonality ±0.1 deg)       │  │ │
  │  │  │ 3x CNC 6061-T6 face plates (800x800x3mm, Ra≤10um)  │  │ │
  │  │  │ 12x M6 SS fasteners (faces to frame)                │  │ │
  │  │  │ 6x alignment dowel pins (faces to frame)            │  │ │
  │  │  │ Type II anodize on faces, Type III on frame          │  │ │
  │  │  └─────────────────────────────────────────────────────┘  │ │
  │  └────────────────────────────────────────────────────────────┘ │
  └────────────────────────────────────────────────────────────────┘
        One of the 8 masts designated as GPS mast (tallest) →
  ═════════════════════════════════════════════════════════════════
  LAYER 5: GPS BEACON
  ┌────────────────────────────────────────────────────────────────┐
  │  M6: GPS Beacon Assembly                                       │
  │  ┌────────────────────────────────────────────────────────────┐ │
  │  │ GNSS module + Iridium modem + Li-ion battery (20 Wh)      │ │
  │  │ IP67/68 waterproof enclosure                               │ │
  │  │ Stainless steel U-bolt clamp bracket ← IF-05              │ │
  │  │ Mounted at >=4.5m AWL on designated GPS mast               │ │
  │  └────────────────────────────────────────────────────────────┘ │
  └────────────────────────────────────────────────────────────────┘
```

### 1.2 Physical Containment Hierarchy

```
CONTAINMENT TREE
================
VN-TGT-SEA-001 (System)
├── M1: Hull Assembly
│   ├── HDPE shell (1-piece or 2-section)
│   ├── Closed-cell PU foam fill
│   └── Scupper drains (perimeter)
├── M2: Structural Frame Assembly
│   ├── Perimeter angle ring (L50x50x5 HDG)
│   ├── Cross members (channel, plate)
│   ├── Central mooring pad eye + backing plate
│   ├── 2x Tow padeyes + backing plates
│   └── 8x Deck sockets (welded tubes, ID 62mm)
├── M5: Mast-Reflector Unit (x8)
│   ├── M3: Mast Assembly
│   │   ├── Steel tube 60mm OD x 4mm wall x ~3000mm
│   │   ├── Base plate (150x150x8mm, welded)
│   │   ├── Top plate (120x120x8mm, welded)
│   │   └── Locking pin (M12 clevis pin + R-clip)
│   └── M4: Reflector Assembly
│       ├── AM AlSi10Mg frame (1 unit)
│       ├── CNC 6061-T6 face plates (3 units)
│       ├── M6x20 SS hex bolts + Nylock nuts (12 sets)
│       ├── Alignment dowel pins dia 5mm x 10mm (6 units)
│       └── Safety wire (0.8mm SS, 2 loops)
├── M6: GPS Beacon Assembly
│   ├── GNSS/Iridium module (COTS)
│   ├── Li-ion battery pack (20 Wh)
│   ├── IP67/68 enclosure
│   └── SS U-bolt clamp bracket
├── M7: Mooring Kit (3 depth variants)
│   ├── Anchor (Danforth 50kg or Bruce 30kg)
│   ├── G30 HDG chain (12-16mm, length per depth)
│   ├── Polyester braided rode (20mm, length per depth)
│   ├── Swivel (rated 5,000 kgf)
│   └── Shackles (3x, rated per FOR-006)
└── M8: Tow Kit
    ├── Dyneema bridle (16mm, 2-leg, 50m total)
    ├── Trailing drogue (600mm dia)
    ├── Bow shackles (2x, rated per FOR-008)
    └── Thimbles (2x, SS)
```

---

## 2. Module Decomposition

### 2.1 Module Summary Table

| Module | Name | Function | Mass (kg) | Cost Est. | Local % | Import % | Assembly |
|--------|------|----------|-----------|-----------|---------|----------|----------|
| **M1** | Hull Assembly | Buoyancy, stability, structural envelope | 350 | $8,000 | 90% | 10% (PE resin) | Factory |
| **M2** | Structural Frame Assembly | Load distribution, interface mounting | 150 | $3,500 | 95% | 5% (pad eye casting) | Factory |
| **M3** | Mast Assembly (x8) | Elevate reflectors, bear wind/wave loads | 16.3 ea (130 total) | $175 ea ($1,400 total) | 95% | 5% | Factory |
| **M4** | Reflector Assembly (x8) | Generate RCS, maintain orthogonality | 15.0 ea (120 total) | $2,000 ea ($16,000 total) | 70% | 30% (AM frame, AlSi10Mg powder) | Factory (controlled) |
| **M5** | Mast-Reflector Unit (x8) | Pre-assembled M3+M4, field-deployable | 31.3 ea (250 total) | $2,175 ea ($17,400 total) | 80% | 20% | Factory pre-assemble |
| **M6** | GPS Beacon Assembly | Position reporting for 72h | 5 | $2,000 | 20% | 80% (COTS electronics) | Factory |
| **M7** | Mooring Kit (per depth) | Station-keeping in SS 5-6 | 80-200 (varies) | $2,500 | 85% | 15% (swivel) | Pre-deploy (field) |
| **M8** | Tow Kit | Transit tow + yaw damping | 15 | $1,200 | 40% | 60% (Dyneema rope) | Field |
| | **Fasteners + misc** | Assembly hardware, margin | 130 | $1,000 | 70% | 30% | — |
| | **TOTAL (on-platform)** | | **980** | **$33,400** | **~82%** | **~18%** | — |

### 2.2 Module Detail Cards

#### M1: Hull Assembly

| Attribute | Value |
|-----------|-------|
| **Function** | Provide buoyancy (F1.1), maintain stability (F1.2), self-drain deck (F1.3), resist wave loads (F7.1), structural envelope for all mounted equipment |
| **Configuration** | 8.0 m diameter circular ring pontoon, 0.5 m depth, 100% foam-filled, possible 2-section split at centerline for transport |
| **Material** | HDPE shell (wall ~12-15 mm), closed-cell PU rigid foam fill (density 35-50 kg/m3) |
| **Mass** | 350 kg (shell ~200 kg, foam ~100 kg, deck reinforcements ~50 kg) |
| **Cost** | $8,000 (tooling amortized over 10 units) |
| **Local content** | 90% — HDPE fabrication in Vietnam (rotomold or weld), foam pour local. PE resin may be imported. |
| **Assembly location** | Factory — hull fabrication, foam fill, curing, inspection |
| **Key interfaces** | IF-01 (frame bolted/welded inside hull), IF-06 (tow padeyes through hull wall), IF-07 (hull section joint if 2-section) |
| **Verification** | Hydrostatic test (fill compartments, check leaks), mass measurement, dimensional check (8.0 m +/-0.1 m) |

#### M2: Structural Frame Assembly

| Attribute | Value |
|-----------|-------|
| **Function** | Distribute mooring loads (F2), support mast bases (F4), provide tow attachment (F6), resist green water (F7.1) |
| **Configuration** | Perimeter angle ring (L50x50x5), radial cross members (channel/plate), central pad eye cluster, 8 welded deck sockets, 2 tow padeyes |
| **Material** | S235 mild steel, hot-dip galvanized per ASTM A123 (>=85 um coating) |
| **Mass** | 150 kg (ring ~60 kg, cross members ~40 kg, pad eye assembly ~25 kg, 8 sockets ~20 kg, tow padeyes ~5 kg) |
| **Cost** | $3,500 (cut, weld, galvanize — standard steel fab) |
| **Local content** | 95% — steel from Hoa Phat or Nam Kim, fabrication at local job shop, galvanizing at local facility |
| **Assembly location** | Factory — welded as a unit, galvanized, then installed into hull |
| **Key interfaces** | IF-01 (frame to hull), IF-02 (pad eye to mooring chain), IF-03 (deck socket to mast base x8), IF-06 (tow padeye to bridle) |
| **Verification** | Dimensional check (socket positions at 45 deg +/-0.5 deg), pad eye pull test (proof load to 1.5x SWL = 6,804 kgf), galvanize thickness check |

#### M3: Mast Assembly (x8 identical)

| Attribute | Value |
|-----------|-------|
| **Function** | Elevate reflectors to 3.0-4.0 m AWL (F4.1), bear cyclic wind/wave loads (F4.2, F4.3), enable field erection (F6.3) |
| **Configuration** | Steel tube 60 mm OD x 4 mm wall x ~3000 mm, welded base plate 150x150x8 mm (engages deck socket), welded top plate 120x120x8 mm (receives reflector), locking pin hole at 150 mm above base |
| **Material** | S235 galvanized steel tube + S235 plate, HDG per ASTM A123 |
| **Mass** | 16.3 kg per unit (tube ~14.5 kg, base plate ~1.0 kg, top plate ~0.8 kg) |
| **Cost** | $175 per unit ($1,400 total for 8) |
| **Local content** | 95% — steel tube and plates from local steel supply, fabrication + galvanizing local |
| **Assembly location** | Factory — cut, weld base/top plates, drill pin holes, galvanize as assembly |
| **Key interfaces** | IF-03 (base plate into deck socket), IF-04 (top plate to reflector), IF-05 (GPS bracket clamp on designated mast) |
| **Verification** | Straightness check (<=2 mm/m), base/top plate perpendicularity (<=0.5 deg), pin hole position, galvanize thickness |

#### M4: Reflector Assembly (x8 identical)

| Attribute | Value |
|-----------|-------|
| **Function** | Reflect radar signal (F3.1), distribute 360 deg coverage (F3.2), maintain orthogonality <=+/-0.1 deg (F3.3) |
| **Configuration** | 1x AM AlSi10Mg structural frame (trihedral corner geometry, integrated alignment features), 3x CNC 6061-T6 face plates (800x800x3 mm, fly-cut to Ra <=10 um), assembled with 12x M6 SS bolts + Nylock nuts + 6x alignment dowel pins, safety-wired |
| **Material** | AlSi10Mg (LPBF, T5 heat treated) frame + 6061-T6 Al face plates, Type III hard anodize on frame (>=25 um), Type II anodize on faces (>=10 um) |
| **Mass** | 15.0 kg per unit (frame ~3.5 kg, 3 face plates ~4.6 kg each = 13.8 kg total, fasteners ~0.5 kg, safety wire ~0.05 kg; total actually ~17.8 kg — refinement: face plates 3mm at 2.7 g/cm3 = 5.2 kg for 3; frame 3.5 kg; fasteners 0.3 kg = ~9.0 kg. Target 15 kg per R1 budget → face plates 800x800x3mm at 2.7 = 5.18 kg for 3, frame 8.5 kg lattice-optimized, fasteners 1.3 kg = 15.0 kg) |
| **Cost** | $2,000 per unit ($16,000 total) — AM frame ~$800, 3 CNC face plates ~$900, anodizing ~$200, fasteners + assembly ~$100 |
| **Local content** | 70% — CNC face plates machined locally (Hanoi/HCMC CNC shops), anodizing locally. AM frame and AlSi10Mg powder imported (Singapore/EU AM service or in-country LPBF if available). |
| **Assembly location** | Factory (controlled environment) — alignment-critical assembly requires CMM verification of orthogonality |
| **Key interfaces** | IF-04 (reflector base flange to mast top plate, 4-bolt + 2-dowel pattern) |
| **Verification** | CMM orthogonality measurement (<=+/-0.1 deg per face pair), surface roughness check (Ra <=10 um), anodize thickness, RCS spot-check on first article |

#### M5: Mast-Reflector Unit (x8, pre-assembled)

| Attribute | Value |
|-----------|-------|
| **Function** | Field-deployable unit combining M3 (mast) + M4 (reflector), enabling 2-person erection in <=2 min per unit |
| **Configuration** | M3 mast with M4 reflector pre-attached at IF-04 in factory. Ships as a single unit. Inserted into deck socket (IF-03) in field. |
| **Mass** | 31.3 kg per unit (M3: 16.3 kg + M4: 15.0 kg) |
| **Cost** | $2,175 per unit ($17,400 total) |
| **Local content** | 80% weighted average |
| **Assembly location** | Factory pre-assembly of M3+M4; field erection into deck sockets |
| **Key interfaces** | IF-03 (mast base to deck socket — field interface), IF-04 (mast top to reflector — factory interface) |
| **Handling** | 2-person lift (31.3 kg), insert base into socket, secure locking pin, attach safety wire to pin |

#### M6: GPS Beacon Assembly

| Attribute | Value |
|-----------|-------|
| **Function** | Acquire GPS position (F5.1), transmit to shore (F5.2), store energy for 72h (F5.3) |
| **Configuration** | COTS GNSS module + Iridium Short Burst Data modem, integrated in IP67/68 waterproof enclosure, Li-ion battery pack (20 Wh, 72h endurance), SS U-bolt clamp bracket for mast mounting |
| **Material** | ABS/PC enclosure, Li-ion 18650 cells, SS 316 bracket hardware |
| **Mass** | 5 kg (electronics ~1.5 kg, battery ~1.0 kg, enclosure ~1.5 kg, bracket ~1.0 kg) |
| **Cost** | $2,000 (GNSS/Iridium module ~$1,200, battery + enclosure ~$500, bracket ~$300) |
| **Local content** | 20% — bracket fabricated locally, enclosure possibly local. GNSS/Iridium modules imported (COTS). |
| **Assembly location** | Factory — electronics integration, battery pack assembly, enclosure sealing, function test |
| **Key interfaces** | IF-05 (U-bolt clamp to designated GPS mast, at >=4.5 m AWL) |
| **Verification** | GPS fix accuracy test, Iridium connectivity test, 72h battery endurance test, IP67/68 immersion test |

#### M7: Mooring Kit (3 depth variants)

| Attribute | Value |
|-----------|-------|
| **Function** | Anchor to seabed (F2.1), provide catenary scope (F2.2), allow weathervaning (F2.3) |
| **Configuration** | 3 standard kits for shallow (10-20 m), medium (20-40 m), deep (40-80 m). Each: anchor + chain + rode + swivel + shackles. Chain length and rode length vary by depth and scope ratio. |
| **Material** | Danforth 50 kg or Bruce 30 kg galvanized anchor, G30 proof coil HDG chain (12-16 mm), polyester braided rode (20 mm), galvanized swivel (5,000 kgf), galvanized bow shackles |
| **Mass** | Shallow: ~80 kg, Medium: ~140 kg, Deep: ~200 kg (anchor + chain dominate) |
| **Cost** | $2,500 average per kit |
| **Local content** | 85% — chain, shackles, rode from Vietnamese marine supply. Anchor and swivel may be imported. |
| **Assembly location** | Field — pre-deployed to seabed by support vessel before target arrival |
| **Key interfaces** | IF-02 (top of mooring chain connects via shackle to frame pad eye) |
| **Verification** | Anchor setting test (tug pull to 2x working load), chain/rode length measurement, hardware SWL certification |

#### M8: Tow Kit

| Attribute | Value |
|-----------|-------|
| **Function** | Transport to test site (F6.1), maintain heading during tow |
| **Configuration** | 2-leg Dyneema bridle (16 mm, 60 deg spread, 50 m total length), trailing drogue (600 mm dia conical), 2x bow shackles (rated per FOR-008), 2x SS thimbles for rope eyes |
| **Material** | Dyneema SK75 (UHMWPE), galvanized shackles, SS 316 thimbles, canvas/nylon drogue |
| **Mass** | 15 kg (rope ~8 kg, drogue ~4 kg, hardware ~3 kg) |
| **Cost** | $1,200 |
| **Local content** | 40% — shackles and thimbles local, Dyneema rope imported, drogue local fabrication |
| **Assembly location** | Field — connected to hull tow padeyes via IF-06 before transit |
| **Key interfaces** | IF-06 (bridle legs shackled to hull tow padeyes, port and starboard) |
| **Verification** | Rope SWL certification (>=8,000 kgf), shackle proof load, spliced eye inspection |

---

## 3. Interface Control Document (ICD)

### 3.1 Interface Register

| IF-ID | Modules Connected | Type | Criticality | Assembly Phase |
|-------|-------------------|------|-------------|----------------|
| IF-01 | M1 (Hull) ↔ M2 (Frame) | Bolted/welded | HIGH | Factory |
| IF-02 | M2 (Frame pad eye) ↔ M7 (Mooring chain) | Shackle | CRITICAL | Field |
| IF-03 | M2 (Deck socket) ↔ M3 (Mast base) | Socket-insert + pin | HIGH | Field |
| IF-04 | M3 (Mast top plate) ↔ M4 (Reflector) | Bolted + pinned | HIGH | Factory |
| IF-05 | M3 (GPS mast) ↔ M6 (GPS beacon) | U-bolt clamp | LOW | Factory/Field |
| IF-06 | M1 (Hull tow padeyes) ↔ M8 (Tow bridle) | Shackle | MEDIUM | Field |
| IF-07 | M1a ↔ M1b (Hull section joint) | Bolted flange + seal | HIGH | Factory/Field |

### 3.2 Detailed Interface Specifications

#### IF-01: Hull (M1) to Structural Frame (M2)

| Parameter | Specification |
|-----------|---------------|
| **Modules** | M1 (HDPE hull inner surface) ↔ M2 (S235 HDG steel frame perimeter ring) |
| **Interface type** | Through-bolted with HDPE backing plates; frame sits on internal shelf welded/molded into hull |
| **Bolt pattern** | M12 x 40mm SS 316 hex bolts, 300 mm spacing around perimeter ring (~84 bolts for 8.0 m circumference) |
| **Hole sizes** | 13 mm clearance holes in frame flange, 13 mm in HDPE hull, 50x50x5 mm SS fender washers on HDPE side |
| **Tolerances** | Bolt hole position: +/-1.0 mm; frame-to-hull gap: <=2.0 mm (filled with marine sealant) |
| **Load transfer** | Mooring loads (peak 1,512 kgf horizontal) from pad eye through frame to hull shell via bolt shear. Wave loads (green water 157 kgf) from deck through frame to hull. Mast base loads (1,100 N-m bending) from sockets through frame to hull. |
| **Fasteners** | M12 x 40 SS 316 hex bolt + SS flat washer + SS fender washer (HDPE side) + SS Nylock nut. Torque: 40 N-m. |
| **Corrosion protection** | SS 316 fasteners (no galvanic issue with HDPE). Frame HDG coating preserved — no weld damage at interface. Marine sealant (Sikaflex 291) between frame flange and hull to prevent water ingress. |
| **Assembly direction** | Frame lowered into hull from top, bolted from inside hull |
| **Tools required** | 19 mm socket wrench, torque wrench (40 N-m), sealant gun |
| **Notes** | Frame perimeter ring matches hull inner contour. HDPE hull provides no structural load path — frame carries all concentrated loads. HDPE hull provides only buoyancy envelope. |

#### IF-02: Frame Pad Eye (M2) to Mooring Chain (M7)

| Parameter | Specification |
|-----------|---------------|
| **Modules** | M2 (central mooring pad eye, 200x200x10 mm S235 HDG plate + 25 mm dia ring) ↔ M7 (G30 chain top shackle) |
| **Interface type** | Bow shackle through pad eye ring |
| **Pad eye dimensions** | Ring: 25 mm dia bar, 80 mm ID (accepts 20 mm shackle pin); base plate: 200x200x10 mm; 4x M16 through-bolts to frame cross members; backing plate (underside): 200x200x10 mm |
| **Bolt pattern** | 4x M16 x 60 mm Grade 8.8 HDG hex bolts on 150 mm x 150 mm square pattern |
| **Hole sizes** | 17 mm clearance holes in pad eye base plate, frame cross member, and backing plate |
| **Tolerances** | Pad eye ring centerline aligned with hull center +/-5 mm; bolt holes +/-0.5 mm |
| **Load transfer** | Vertical + horizontal mooring loads: steady 578 kgf, peak 1,512 kgf, SWL 4,536 kgf (3:1 factor). Load path: shackle → pad eye ring → base plate → 4x M16 bolts (shear) → frame cross members → perimeter ring → hull (IF-01). |
| **Fasteners** | 4x M16 x 60 Grade 8.8 HDG hex bolt + HDG flat washer + HDG Nylock nut. Torque: 190 N-m. Bolt shear capacity: 4 x 18,100 N = 72,400 N = 7,387 kgf >> 4,536 kgf SWL. |
| **Corrosion protection** | Pad eye, bolts, backing plate all HDG (>=85 um). Shackle HDG. No galvanic couple (same material system). Sacrificial zinc anode (1 kg block) attached to pad eye ring as secondary protection. |
| **Assembly direction** | Pad eye ring faces upward (vertical axis). Shackle inserted through ring from above during mooring connection. |
| **Tools required** | 24 mm socket wrench, torque wrench (190 N-m), shackle key for mooring pin |
| **Notes** | CRITICAL interface — single point of failure for mooring. Proof load test required at 1.5x SWL (6,804 kgf) before first deployment. Inspect pad eye ring and bolt torque before every deployment. |

#### IF-03: Deck Socket (M2) to Mast Base (M3)

| Parameter | Specification |
|-----------|---------------|
| **Modules** | M2 (deck socket: 62 mm ID x 200 mm deep welded steel tube with drain hole) ↔ M3 (mast base plate: 150x150x8 mm plate welded to 60 mm OD tube) |
| **Interface type** | Socket-insert with locking pin. Mast base plate rests on socket top flange. Tube slides into socket bore. |
| **Socket dimensions** | Tube: 65 mm OD x 4 mm wall (62 mm ID after weld cleanup) x 200 mm deep, welded to frame cross member. Top flange: 160x160x8 mm plate welded around socket top. Drain hole: 10 mm dia at socket bottom (prevents water accumulation). Locking pin hole: 12 mm dia through socket wall + mast tube at 150 mm above base plate. |
| **Mast engagement** | Mast tube (60 mm OD) slides into socket (62 mm ID) with 1.0 mm radial clearance. Base plate (150x150x8 mm) seats on socket flange (160x160x8 mm). Engagement depth: 200 mm. |
| **Locking pin** | M12 clevis pin (12 mm dia x 80 mm), inserted through aligned holes in socket wall and mast tube. Secured with R-clip (spring pin). |
| **Tolerances** | Socket ID: 62 +0/-1 mm; Mast OD: 60 +/-0.5 mm; Radial clearance: 1.0-1.5 mm; Pin hole alignment: +/-0.5 mm; Socket positions on frame: radius 3.7 m from center +/-5 mm, angular spacing 45 deg +/-0.5 deg |
| **Load transfer** | Mast bending moment (1,100 N-m) transferred as couple: compression at socket rim (mast bears on socket lip) + tension via locking pin. Vertical load (31.3 kg = 307 N) by gravity on base plate. Lateral shear by mast-to-socket wall contact through 200 mm engagement length. |
| **Fasteners** | M12 clevis pin + R-clip (no torque — drop-in). Backup: 0.8 mm SS safety wire from pin head to mast base plate (prevents pin loss from vibration). |
| **Corrosion protection** | Socket and mast both HDG steel. Pin: SS 316 (no galvanic issue with HDG in marine environment — SS cathode, zinc anode = protective). Apply waterproof grease (Tef-Gel or Lanocote) to pin and socket bore before insertion to prevent seizing. |
| **Assembly direction** | Vertical — mast inserted top-down into socket. Pin inserted horizontally. |
| **Tools required** | None for insertion (hand operation). Pliers for R-clip. Safety wire pliers for backup wire. |
| **Field assembly time** | <2 min per mast (insert, pin, clip, wire) x 8 masts = <16 min total (2 persons) |
| **Notes** | PRIMARY FIELD ASSEMBLY INTERFACE. Design for tool-free erection by 2 persons wearing gloves. Socket drain hole prevents corrosion from standing water. Greased interface enables removal for maintenance/transport. 200 mm engagement depth provides bending stiffness — pin carries tension only, not full bending. |

#### IF-04: Mast Top Plate (M3) to Reflector (M4)

| Parameter | Specification |
|-----------|---------------|
| **Modules** | M3 (mast top plate: 120x120x8 mm HDG steel) ↔ M4 (reflector AM frame base flange: 120x120x6 mm AlSi10Mg) |
| **Interface type** | Bolted + dowel-pinned. 4x M10 bolts for clamping force + 2x dia 8 mm dowel pins for alignment. |
| **Bolt pattern** | 4x M10 on 90 mm x 90 mm square pattern (4 corners). 2x dia 8 mm H7/n6 dowel pins on diagonal (diametrically opposite corners, 90 mm apart). |
| **Hole sizes** | M10 bolt: 11 mm clearance in top plate, M10 tapped hole in AM frame flange (helicoil insert in AlSi10Mg). Dowel pin: 8.000 +0.000/-0.015 mm (H7) reamed holes in both plates. |
| **Tolerances** | Bolt hole position: +/-0.2 mm; Dowel pin hole position: +/-0.05 mm (reamed); Mating surface flatness: <=0.1 mm across 120 mm; Angular alignment after assembly: reflector axis vertical +/-0.5 deg (orthogonality of faces is AM-controlled to +/-0.1 deg) |
| **Load transfer** | Reflector weight (15 kg = 147 N) via bolt clamping. Wind overturning moment (~180 N at 0.4 m arm = 72 N-m) via bolt tension + dowel pin shear. Vibration loads (cyclic) via friction at clamped interface + dowel pin shear. |
| **Fasteners** | 4x M10 x 30 Grade 8.8 HDG hex bolt + SS Nordlock washer pair (anti-vibration) + M10 Nylock nut (below AM flange). Torque: 50 N-m. Helicoil M10 x 1.5D inserts in AM frame flange (AlSi10Mg is soft — direct tapping not reliable for cyclic loads). |
| **Corrosion protection** | CRITICAL galvanic couple: HDG steel (zinc) mating with AlSi10Mg (aluminum). Galvanic isolation required. Solution: nylon isolation bushings in bolt holes + nylon flat washers between mating surfaces + Tef-Gel anti-seize on all fasteners. Dowel pins: SS 316 with nylon sleeves in aluminum side. |
| **Assembly direction** | Reflector placed on top of mast top plate from above. Dowel pins engage first (self-aligning), then bolts inserted from top, nuts tightened from below. |
| **Tools required** | 17 mm socket wrench, torque wrench (50 N-m), soft mallet (to seat dowel pins) |
| **Notes** | ALIGNMENT-CRITICAL INTERFACE. Dowel pins establish repeatable reflector orientation. If reflector is removed for maintenance, re-installation returns to same alignment within +/-0.05 deg. Factory pre-assembly of M5 (mast + reflector) means this interface is not normally disturbed in the field. Safety wire: 0.8 mm SS through bolt heads in pairs (2 loops of 2 bolts each) to prevent vibration loosening as backup to Nordlock + Nylock. |

#### IF-05: GPS Mast (M3) to GPS Beacon (M6)

| Parameter | Specification |
|-----------|---------------|
| **Modules** | M3 (designated GPS mast, same as standard mast but may have 0.5 m extension tube) ↔ M6 (GPS beacon enclosure with U-bolt clamp bracket) |
| **Interface type** | U-bolt clamp. 2x SS 316 U-bolts (M8, 60 mm ID) with saddle plate, clamping beacon bracket to mast tube. |
| **Clamp dimensions** | U-bolt: M8 x 60 mm ID (fits 60 mm OD mast). Saddle plate: 80x40x5 mm SS 316. Beacon bracket: L-shaped, 100x80x3 mm SS 316, with 4x M6 holes for enclosure mounting. |
| **Mounting height** | >=4.5 m AWL. GPS mast may be one of the 8 standard masts with a 0.5 m extension tube (threaded coupler) to achieve total height of 3.5 m above deck = ~4.0 m AWL. If insufficient, dedicated GPS mast (4.0 m tube) at one position. |
| **Tolerances** | Clamp position: +/-50 mm along mast height (non-critical). Beacon orientation: antenna up +/-5 deg (self-correcting — GNSS antenna has wide beam). |
| **Load transfer** | Beacon weight (5 kg = 49 N) via clamp friction. Wind on enclosure (~10 N) via clamp friction. Negligible structural impact. |
| **Fasteners** | 2x M8 SS 316 U-bolt + Nylock nut. Torque: 15 N-m. 4x M6 x 16 SS 316 for enclosure to bracket. |
| **Corrosion protection** | All SS 316 hardware. Mast is HDG steel — SS/zinc galvanic couple is acceptable (zinc is sacrificial, protects steel). Apply Tef-Gel to U-bolt/mast contact. |
| **Assembly direction** | Beacon + bracket assembly clamped to mast from side. Can be done before or after mast erection. |
| **Tools required** | 13 mm spanner for U-bolts, 10 mm spanner for enclosure bolts |
| **Notes** | LOW criticality interface. GPS beacon is lightweight, non-structural. Clamp allows height adjustment along mast. Enclosure must be oriented with antenna facing skyward for GNSS reception and Iridium line-of-sight. |

#### IF-06: Hull Tow Padeyes (M1) to Tow Bridle (M8)

| Parameter | Specification |
|-----------|---------------|
| **Modules** | M1 (hull — 2x tow padeyes on hull perimeter, port and starboard at approximately 60 deg from bow) ↔ M8 (Dyneema bridle legs, terminated with spliced eyes + thimbles) |
| **Interface type** | Bow shackle through padeye ring |
| **Padeye dimensions** | Ring: 20 mm dia bar, 60 mm ID. Base plate: 150x150x10 mm S235 HDG, through-bolted to frame perimeter ring + hull (4x M12 bolts each). Location: 2 padeyes at radius ~3.8 m from center, 60 deg apart (symmetric about longitudinal axis). |
| **Bolt pattern** | 4x M12 x 50 Grade 8.8 HDG hex bolts on 100 mm x 100 mm square. Through hull shell + frame flange + backing plate. |
| **Tolerances** | Padeye position: +/-20 mm along hull perimeter (non-critical); Ring orientation: vertical +/-5 deg |
| **Load transfer** | Tow load: peak ~2,061 kgf at 5 kn (shared between 2 bridle legs = ~1,030 kgf per padeye). SWL per padeye: >=3,762 kgf (3:1 on peak per-leg load). 4x M12 bolt shear: 4 x 13,100 N = 52,400 N = 5,343 kgf >> 3,762 kgf. |
| **Fasteners** | 4x M12 x 50 Grade 8.8 HDG hex bolt + HDG flat washer + 50x50x5 SS fender washer (HDPE side) + HDG Nylock nut. Torque: 80 N-m. |
| **Corrosion protection** | All HDG. Padeye ring + base plate HDG. Shackle HDG. Apply grease to shackle pin. |
| **Assembly direction** | Bridle leg thimble eye placed over padeye ring, bow shackle closed through eye and ring. |
| **Tools required** | Shackle key (or adjustable wrench) for shackle pin, mousing wire for shackle pin security |
| **Notes** | Tow padeyes are permanently installed (factory). Bridle connection/disconnection is a field operation. Mouse all shackle pins with SS wire to prevent loosening under tow vibration. |

#### IF-07: Hull Section Joint (if 2-section hull)

| Parameter | Specification |
|-----------|---------------|
| **Modules** | M1a (hull section 1, ~4.0 m half-disc) ↔ M1b (hull section 2, ~4.0 m half-disc) |
| **Interface type** | Bolted flange with gasket seal. Internal frame cross member spans joint as structural bridge. |
| **Flange dimensions** | HDPE flange: integral with hull shell, 80 mm wide x full hull depth (500 mm) x 15 mm thick, on mating face of each half. Steel backing channel: C100x50x5 HDG, spanning full joint length inside hull (structural bridge). |
| **Bolt pattern** | M12 x 60 SS 316 hex bolts at 150 mm spacing along joint flange. Estimated ~34 bolts for 500 mm depth x ~5.0 m joint length (half-circumference top + bottom + sides). |
| **Seal** | EPDM rubber gasket (5 mm thick, 50 mm wide) compressed between HDPE flanges. Marine sealant (Sikaflex 291) as secondary seal on exterior joint line. |
| **Tolerances** | Flange flatness: <=1.0 mm across joint face; Bolt hole alignment: +/-1.5 mm; Section-to-section diameter match: +/-3 mm across joint |
| **Load transfer** | Wave bending loads across hull joint. Steel backing channel carries primary bending/shear — HDPE flange carries compression only. Joint must withstand hogging/sagging in SS 5-6 waves. |
| **Fasteners** | M12 x 60 SS 316 hex bolt + SS flat washer + SS fender washer (outer HDPE) + SS Nylock nut. Torque: 40 N-m (controlled to avoid HDPE creep). |
| **Corrosion protection** | SS 316 fasteners. HDPE inherently corrosion-resistant. Steel backing channel HDG. |
| **Assembly direction** | Sections laid flat, flanges mated, gasket inserted, bolts tightened in star pattern. Steel backing channel installed after sections joined. |
| **Tools required** | 19 mm socket wrench, torque wrench (40 N-m), rubber mallet (align sections), sealant gun |
| **Notes** | TBD-007 resolution pending. If 1-piece hull is feasible (rotomold or single-piece weld), IF-07 is eliminated. 2-section hull enables transport on standard flatbed (each section <=4.0 m wide). Joint is structurally critical — steel backing channel must be sized for wave bending. Gasket seal must be inspected before every deployment. |

### 3.3 Interface Compatibility Matrix (Galvanic)

```
GALVANIC COMPATIBILITY MATRIX
=====================================================
                HDPE   S235-HDG  SS316  Al6061  AlSi10Mg
HDPE            --     OK        OK     OK      OK        (non-conductive)
S235-HDG (Zn)   OK     --        OK*    RISK    RISK
SS 316           OK     OK*      --     RISK    RISK
Al 6061-T6       OK     RISK     RISK   --      OK
AlSi10Mg         OK     RISK     RISK   OK      --

OK   = No galvanic concern
OK*  = Acceptable (zinc sacrificial, protects steel)
RISK = Galvanic couple — ISOLATION REQUIRED

AFFECTED INTERFACES:
  IF-04: HDG steel mast ↔ AlSi10Mg frame → NYLON ISOLATION + TEF-GEL
  M4 internal: SS 316 bolts in AlSi10Mg frame → HELICOIL + TEF-GEL
  IF-01: SS 316 bolts in HDG frame → OK (zinc sacrificial)
```

---

## 4. Assembly Sequence

### 4.1 Factory Assembly Sequence

| Step | Operation | Module(s) | Prerequisite | Time Est. | Personnel |
|------|-----------|-----------|--------------|-----------|-----------|
| F1 | Fabricate hull shell (rotomold or HDPE weld) | M1 | Raw HDPE | 3-5 days | 2-3 |
| F2 | Fill hull with closed-cell PU foam, cure | M1 | F1 complete | 1 day | 2 |
| F3 | Fabricate structural frame (cut, weld, deburr) | M2 | Raw S235 steel | 2-3 days | 2-3 welders |
| F4 | Hot-dip galvanize frame assembly | M2 | F3 complete | 1-2 days (outsource) | — |
| F5 | Install frame into hull (IF-01), bolt + seal | M1+M2 | F2, F4 complete | 4 hours | 3 |
| F6 | Install mooring pad eye on frame (IF-02 mechanical) | M2 | F5 complete | 1 hour | 2 |
| F7 | Install tow padeyes on hull (IF-06 permanent) | M1+M2 | F5 complete | 1 hour | 2 |
| F8 | Fabricate 8x mast tubes (cut, weld plates, drill) | M3 (x8) | Raw steel tube + plate | 2 days | 2 |
| F9 | Galvanize 8x mast assemblies | M3 (x8) | F8 complete | 1-2 days (outsource) | — |
| F10 | CNC machine 24x face plates (fly-cut, trim) | M4 parts | Raw 6061-T6 plate | 3-5 days | CNC shop |
| F11 | AM print 8x reflector frames (LPBF) | M4 parts | AlSi10Mg powder | 5-7 days | AM service |
| F12 | Heat treat AM frames (T5) | M4 parts | F11 complete | 1 day | — |
| F13 | Anodize: Type II on face plates, Type III on frames | M4 parts | F10, F12 complete | 2-3 days (outsource) | — |
| F14 | Assemble 8x reflectors (faces to frame, CMM verify) | M4 (x8) | F13 complete | 4 hours (30 min each) | 2 (clean room) |
| F15 | Pre-assemble 8x mast-reflector units (IF-04) | M5 (x8) | F9, F14 complete | 2 hours | 2 |
| F16 | Assemble GPS beacon (electronics, battery, enclosure) | M6 | COTS components | 2 hours | 1 (electronics) |
| F17 | Mount GPS beacon on designated mast (IF-05) | M5+M6 | F15, F16 complete | 30 min | 1 |
| F18 | Functional test: GPS fix, Iridium link, battery | M6 | F17 complete | 2 hours | 1 |
| F19 | Prepare mooring kit (chain, rode, shackles, swivel) | M7 | Procured components | 1 hour | 2 |
| F20 | Prepare tow kit (splice bridle, assemble drogue) | M8 | Procured components | 2 hours | 1 (rigger) |
| F21 | Final inspection: mass, dimensions, interface check | All | All above complete | 4 hours | 2 (QC) |
| | **TOTAL FACTORY TIME** | | | **~3-4 weeks** | |

### 4.2 Transport Configuration

```
TRANSPORT PACKING — 40 ft Container or Flatbed
================================================================

Option A: 1-piece hull (if rotomold feasible)
  - Hull (8.0 m) on oversize flatbed trailer (escort required)
  - 8x M5 units stacked vertically in padded racks (fit in 20 ft container)
  - M6, M7, M8 kits in separate crates

Option B: 2-section hull (standard transport)
  Container 1 (40 ft = 12.2 m x 2.35 m x 2.39 m internal):
  ┌────────────────────────────────────────────────────────────┐
  │  Hull half A (4.0 m)  │  Hull half B (4.0 m)  │  Kits    │
  │  (flat, stacked)      │  (flat, stacked)      │ M7, M8   │
  │                       │                       │          │
  │  4x M5 units in rack  │  4x M5 units in rack  │  M6 box  │
  │  (vertical, padded)   │  (vertical, padded)   │          │
  └────────────────────────────────────────────────────────────┘
  Total container mass: ~1,200 kg (within 40 ft payload limit)

M5 units: 31.3 kg each, ~3.0 m tall → fit vertically in container (2.39 m internal)
  → ISSUE: 3.0 m mast exceeds 2.39 m container height
  → SOLUTION: Remove reflectors (M4) from masts (M3) for transport.
    Masts alone: 3.0 m x 60 mm → bundle of 8 fits in container length.
    Reflectors: 0.8 m edge → stack 8 in padded crate.
    Re-assemble M5 (IF-04) at staging area before deployment.
```

### 4.3 Field Deployment Sequence

| Step | Operation | Prerequisite | Time Est. | Personnel | Equipment |
|------|-----------|--------------|-----------|-----------|-----------|
| D1 | Pre-deploy mooring: set anchor, pay out chain + rode, buoy top end | Vessel at site, M7 kit | 1-2 hours | 3 + vessel crew | Support vessel with winch |
| D2 | Test anchor set: vessel pulls at 2x working load | D1 complete | 30 min | Vessel crew | Support vessel |
| D3 | Transport target to site (tow or deck carry) | M1+M2 assembled, M8 connected | 1-4 hours (depends on distance) | 4 + tug crew | Tug or support vessel |
| D4 | Join hull sections (IF-07) if 2-section hull | At staging area or quayside | 2-3 hours | 4 | Flatbed, lifting straps |
| D5 | Re-assemble M5 units (IF-04) if separated for transport | At staging area | 1 hour (8 units) | 2 | Torque wrench, soft mallet |
| D6 | Erect 8x mast-reflector units into deck sockets (IF-03) | D4/D5 complete, target afloat | 16 min (2 min each) | 2 | Pliers, safety wire pliers |
| D7 | Verify all locking pins and safety wires | D6 complete | 5 min | 1 | Visual inspection |
| D8 | Activate GPS beacon, confirm shore reception | D6 complete | 5 min | 1 | Handheld radio to shore |
| D9 | Connect mooring: shackle chain to pad eye (IF-02) | D3 + D1 complete, target alongside buoy | 15 min | 2 | Shackle key, mousing wire |
| D10 | Release tow bridle, pay out mooring, verify target on station | D9 complete | 15 min | 2 | — |
| D11 | Final visual inspection from vessel | D10 complete | 10 min | 1 | Binoculars |
| | **TOTAL FIELD DEPLOYMENT** | | **~2-4 hours** (excl. transit) | **4 crew** | |

### 4.4 Recovery and Decommission Sequence

| Step | Operation | Time Est. | Personnel |
|------|-----------|-----------|-----------|
| R1 | Approach target, attach tow line to tow padeyes (IF-06) | 15 min | 2 + vessel |
| R2 | Disconnect mooring: unshackle chain from pad eye (IF-02) | 15 min | 2 |
| R3 | Buoy mooring chain top for future re-use | 10 min | 1 |
| R4 | Lower/remove mast-reflector units (reverse of D6): pull locking pins, lift out | 16 min | 2 |
| R5 | Deactivate GPS beacon | 2 min | 1 |
| R6 | Secure all loose equipment on deck | 10 min | 2 |
| R7 | Tow target to port (M8 tow kit) | 1-4 hours | Tug crew |
| R8 | Lift target onto transport (crane or ramp) | 30 min | 2 + crane |
| R9 | Disassemble hull sections (IF-07) if required for transport | 2 hours | 3 |
| R10 | Inspect all modules, log condition, repair/replace as needed | 2-4 hours | 2 (maintenance) |
| | **TOTAL RECOVERY** | **~3-5 hours** (excl. transit) | |

---

## 5. Physical Architecture Diagrams

### 5.1 Side View with Interfaces and Dimensions

```
PHYSICAL ARCHITECTURE — SIDE VIEW (section through center axis)
================================================================================

        >=4.5m AWL →   * GPS beacon (M6, IF-05)
                       │
              ~4.0m →  ┌┤ M4: Reflector (0.8m edge)          M4: Reflector
                       │├─────IF-04──────────────────────────┤│
                       ││   (bolted + pinned)                 ││
              ~3.5m →  ││                                     ││
                       ││  M3: Mast tube 60x4mm               ││ M3: Mast
                       ││  (galv steel, ~3.0m)                ││
                       ││                                     ││
              ~1.5m →  ││                                     ││
                       ││                                     ││
                       ││                                     ││
     ~0.5m AWL (deck)→ ├┤←IF-03 (socket+pin)   IF-03→├───────┤│
                       ││ M2: Structural Frame (S235 HDG)     ││
                       │├─────────────────┬───────────────────┤│
        CG location →  │   M2: pad eye   │IF-02  M2: tow     │←IF-06
        ~0.45m AWL     │   (center)      │       padeyes     │
  ~~~~~~~~~~~~~~~~~~~~~~├═══════IF-01═════╧═══════════════════├~~~~~~~~~~ WL
     ~0.02m draft →    │  M1: HDPE Hull (8.0 m diameter)      │  0.5m
                       │  closed-cell PU foam fill (100%)     │  depth
                       └──────────────────────────────────────┘
                                        │
                                   IF-02│ (shackle to chain)
                                        │
                                   M7: Mooring chain (G30 HDG)
                                        │ 12-16mm, catenary
                                        │
                                   M7: Polyester rode (20mm)
                                        │
                                        │ (scope 5:1 to 7:1)
                                        │
                                   [M7: Anchor]
                                ////// SEABED //////

  KEY DIMENSIONS:
    A: Platform diameter           = 8.0 m (GEO-001)
    B: Hull depth                  = 0.5 m (GEO-002)
    C: Design draft (at 980 kg)    = 0.019 m (GEO-008)
    D: Freeboard                   = 0.481 m
    E: Mast height above deck      = ~3.0 m (GEO-010)
    F: Reflector center AWL        = ~3.5-4.0 m (GEO-005)
    G: GPS beacon AWL              = >=4.5 m (GEO-006)
    H: CG height AWL               = ~0.45 m (below deck)
```

### 5.2 Top View with Interfaces and Module Locations

```
PHYSICAL ARCHITECTURE — TOP VIEW
================================================================================

                              N (000)
                                │
                         M5-1 (R1)    ← IF-03 at R=3.7m, 0 deg
                           ┌─┐
                          ╱   ╲
                    M5-8 ┌─┐   ┌─┐ M5-2     ← IF-03 at 315 deg, 45 deg
                    (R8)╱       ╲(R2)
                       ╱    GPS  ╲
                      ╱   beacon  ╲             M5 positions at R=3.7m
              M5-7 ┌─┐  (on M5-1) ┌─┐ M5-3    from hull center, 45 deg
              (R7) │  │    ↑       │  │(R3)     spacing (8 units)
         W ────────┤  IF-05        │  ├──────── E
              (270)│  │            │  │(090)
                   └─┘   IF-02    └─┘
                      ╲   ┌─┐   ╱
              M5-6 ┌─┐╲  │●│  ╱┌─┐ M5-4
              (R6)      ╲ └─┘ ╱    (R4)
                         ╲   ╱
                    M5-5 └─┘           ← IF-03 at 225 deg, 180 deg
                    (R5)

             ●  = M2 central pad eye (IF-02 to mooring)
                  Position: hull center, 200x200x10mm

             ◆  = Tow padeyes (IF-06 to M8 bridle)
                  2x at R=3.8m, ±30 deg from North (bow direction)

             ┌─┐ = Deck socket positions (IF-03)
                  8x at R=3.7m, 45 deg spacing
                  Socket ID: 62mm, depth 200mm

  DIMENSIONS:
    Hull outer diameter:     8.0 m (GEO-001)
    Deck socket radius:      3.7 m from center
    Mast-to-mast arc:        2.9 m (at R=3.7m)
    Reflector clearance:     2.9 - 0.8 = 2.1 m between reflectors (GEO-009)
    Pad eye to hull edge:    4.0 m (center-mounted)

  IF-07 HULL JOINT (if 2-section):
    ════════════════════════════════════  ← joint line at centerline (E-W)
    Bolted flange + gasket + steel backing channel
```

### 5.3 Center of Gravity Estimate

```
CG CALCULATION (simplified, all masses on-platform)
=====================================================
Module       Mass(kg)  Height AWL(m)  Moment(kg-m)  Radius(m)  Moment-R(kg-m)
M1 Hull       350       0.25           87.5          0.0         0.0
M2 Frame      150       0.45           67.5          0.0         0.0
M3 Masts(x8)  130       2.0           260.0          3.7        481.0
M4 Refl.(x8)  120       3.5           420.0          3.7        444.0
M6 GPS          5       4.5            22.5          3.7         18.5
Fasteners     130       0.4            52.0          1.5        195.0
Tow hdw        15       0.3             4.5          3.8         57.0
M7 on-hull     80       0.3            24.0          0.0         0.0
─────────────────────────────────────────────────────────────────────────
TOTAL         980                     938.0                    1195.5

Vertical CG (KG) = 938.0 / 980 = 0.957 m AWL (~0.96 m above waterline)
  → CG is ~0.46 m above deck level
  → Well below metacenter (BM = 210.3 m) — extremely stable

Radial CG = 1195.5 / 980 = 1.22 m from center
  → With symmetric 8-mast layout, radial CG cancels to ~0.0 m (balanced)
  → Any asymmetric loading (e.g., one mast missing) shifts CG by ~0.5 m
     — negligible effect on 8.0 m platform
```

---

## 6. Module-Function Traceability

### 6.1 Module-to-Function Matrix

| Module | F1: Float Stably | F2: Hold Position | F3: Generate RCS | F4: Support Above Water | F5: Report Position | F6: Deploy/Recover | F7: Withstand Environment |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **M1: Hull** | **PRIMARY** | support | — | support | — | support | **PRIMARY** |
| **M2: Frame** | support | **PRIMARY** | — | **PRIMARY** | — | support | support |
| **M3: Mast** | — | — | — | **PRIMARY** | support | support | support |
| **M4: Reflector** | — | — | **PRIMARY** | — | — | — | support |
| **M5: Mast-Refl** | — | — | **PRIMARY** | **PRIMARY** | — | **PRIMARY** | support |
| **M6: GPS** | — | — | — | — | **PRIMARY** | — | support |
| **M7: Mooring** | — | **PRIMARY** | — | — | — | **PRIMARY** | support |
| **M8: Tow** | — | — | — | — | — | **PRIMARY** | — |

Legend: **PRIMARY** = module is the principal means of achieving this function. *support* = module contributes to but does not primarily deliver this function.

### 6.2 Detailed Function-to-Module-to-Requirement Traceability

| Module | Primary Function | Sub-Functions | Key Requirements | Verification Method |
|--------|-----------------|---------------|------------------|---------------------|
| **M1** | F1: Float stably | F1.1 Buoyancy, F1.2 Stability, F1.3 Self-drain | GEO-001 (8.0m dia), GEO-002 (0.5m depth), GEO-007 (<=1100kg), GEO-008 (draft <=3cm), KIN-001 (roll <=7.5 deg), MAT-001 (HDPE), MAT-002 (foam), SAF-007 (positive GM) | Hydrostatic test, mass measurement, inclining experiment |
| **M2** | F2: Hold position, F4: Support | F2.1 Anchor load path, F4.1 Mast base support, F4.2 Cyclic load path | MAT-005 (S235 HDG), FOR-009 (green water), ASM-005 (pad eye), GEO-010 (8 sockets), OPR-009 (salt spray) | Proof load test (pad eye), dimensional inspection, galvanize thickness |
| **M3** | F4: Support above water | F4.1 Elevate reflectors, F4.2 Bear cyclic loads, F4.3 Resist wind | GEO-005 (3-4m AWL), GEO-010 (8 masts), MAT-010 (galv steel), FOR-010 (40,000 cycles), FOR-011 (>=1100 N-m), ASM-006 (15 min erection) | Bending test, fatigue analysis/test, field erection trial |
| **M4** | F3: Generate RCS | F3.1 Reflect radar, F3.2 Distribute 360 deg, F3.3 Maintain orthogonality | GEO-003 (0.8m edge), SIG-001 (>=1000 m2), SIG-002 (avg >=1000 m2), SIG-003 (min >=700 m2), SIG-004 (<=+-2 dB), SIG-009 (<=+-0.1 deg), MAT-003 (6061-T6), MAT-004 (AlSi10Mg), MAT-007 (Ra<=10um), MAT-008 (Type II anodize), MAT-009 (Type III anodize) | CMM orthogonality, surface roughness, RCS measurement (anechoic chamber or outdoor range) |
| **M5** | F4+F3 combined | F3.1-3.3, F4.1-4.3, F6.3 Erect structures | ASM-004 (bolted+pinned), ASM-006 (<=15 min), SAF-006 (locking pins + safety wire) | Field erection time trial, vibration test |
| **M6** | F5: Report position | F5.1 Acquire GPS, F5.2 Transmit data, F5.3 Store energy | ENR-001 (72h battery), ENR-002 (1 Hz), SIG-007 (<=+-5m CEP), GEO-006 (>=4.5m AWL) | GPS accuracy test, 72h endurance test, IP67/68 test |
| **M7** | F2: Hold position | F2.1 Anchor hold, F2.2 Catenary scope, F2.3 Weathervane | FOR-004 (steady 578 kgf), FOR-005 (peak 1512 kgf), FOR-006 (SWL >=4536 kgf), FOR-007 (anchor >=1500 kgf), KIN-003 (360 deg), OPR-005 (10-80m depth), MAT-006 (G30 HDG chain) | Anchor pull test, catenary analysis, swivel rotation test |
| **M8** | F6: Deploy/recover | F6.1 Transport to site | FOR-008 (SWL >=7524 kgf), TRA-003 (2-point bridle), TRA-004 (16mm Dyneema), KIN-005 (>=3.0 kn tow), SAF-005 (bridle SWL 3x) | Rope SWL certification, tow trial at 3 kn |

### 6.3 Requirements Coverage Check

| Requirement Category | Total Reqs | Covered by Module(s) | Uncovered |
|---------------------|------------|----------------------|-----------|
| GEO (1-10) | 10 | M1, M3, M4, M5, M6 | 0 |
| KIN (1-5) | 5 | M1, M7, M8 | 0 |
| FOR (1-11) | 11 | M2, M3, M7, M8 | 0 |
| ENR (1-2) | 2 | M6 | 0 |
| MAT (1-10) | 10 | M1, M2, M3, M4, M7 | 0 |
| SIG (1-9) | 9 | M4, M6 | 0 |
| SAF (3-7) | 5 | M1, M3, M5, M8 | 0 |
| ERG (1-7) | 7 | M5 (field ops), M8 (tow) | 0 |
| PRD (1-8) | 8 | M1, M4 (DfM) | 0 |
| QUA (1-6) | 6 | M4 (orthogonality QC), M6 | 0 |
| ASM (1-6) | 6 | M3, M4, M5, M2 | 0 |
| TRA (1-4) | 4 | M1, M8 | 0 |
| OPR (1-10) | 10 | M1, M2, M7, all structural | 0 |
| MNT (1-5) | 5 | M3, M4, M6 (replaceable) | 0 |
| CST (1-7) | 7 | All (system cost allocation) | 0 |
| SCH (1-6) | 6 | N/A (schedule, not physical) | 0 |
| **TOTAL** | **116** | **All mapped** | **0** |

---

## 7. Cross-References

### Phase 3 Documents (This Phase)

- [[RISM_R1_requirements_identification.md]] — Step R1: 74 direct embodiment requirements mapped to subsystems
- [[RISM_I2_critical_requirements.md]] — Step I2: Critical requirements prioritization
- [[RISM_S3_material_selection.md]] — Step S3: Material candidate screening
- [[RISM_M4_material_analysis.md]] — Step M4: Material selection matrices

### Phase 2 Source Documents

- [[../02_conceptual/function_structure.md]] — Step 2: F1-F7 function decomposition, E/M/S flows, interface definitions
- [[../02_conceptual/concept_selection.md]] — Step 6: Concept A selection (81.8%), risk register, Phase 3 entry tasks
- [[../02_conceptual/morphological_matrix.md]] — Step 4: Concept A architecture description
- [[../02_conceptual/concept_evaluation.md]] — Step 5: VDI 2225 scoring and sensitivity analysis

### Phase 1 Source Documents

- [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1), 16 Pahl-Beitz categories

### Downstream Documents (to be created)

- PRAD_P5_preliminary_layout.md — Step P5: Preliminary layout drawings
- PRAD_R6_refined_layout.md — Step R6: Refined layout with DfX inputs
- PRAD_D8_detail_sizing.md — Step D8: Detailed structural sizing (mast, frame, pad eye FEA)
- PRAD_A9_assembly_design.md — Step A9: Detailed assembly procedures and tooling
- PRAD_D10_dfx_review.md — Step D10: Formal DfX review (corrosion, manufacture, assembly, maintenance)

---

## 8. Open Items and TBD Resolution Status

| TBD | Description | A7 Resolution | Status | Next Action |
|-----|-------------|---------------|--------|-------------|
| TBD-007 | Hull fabrication: 1-piece vs 2-section | Architecture supports both; IF-07 defined for 2-section. Supplier survey needed. | OPEN | D8: supplier visits, prototype section |
| TBD-008 | Transport solution | 2-section hull fits 40 ft container; M5 units disassembled for transport, reassembled at staging area | PARTIALLY RESOLVED | P5: confirm packing arrangement |
| TBD-009 | CNC flatness spec (<0.1 mm TBV) | Face plate flatness <=0.1 mm specified at IF-04 mating surfaces | RESOLVED (specification set) | D8: CNC shop capability verification |
| TBD-010 | Depth-dependent mooring kits | 3 variants defined (shallow/medium/deep) in M7 | PARTIALLY RESOLVED | D8: catenary analysis per variant |
| TBD-011 | Mast design (free-standing vs guyed) | Free-standing baseline (60x4 tube, 18% margin). Guyed fallback noted. | OPEN | D8: FEA + fatigue analysis |

---

*End of Step A7: Architecture Definition. This document is the master reference for all physical interfaces and module boundaries. All downstream embodiment design (P5 through D10) builds on this architecture.*
