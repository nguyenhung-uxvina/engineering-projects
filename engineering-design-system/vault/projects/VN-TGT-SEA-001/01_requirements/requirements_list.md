---
project: VN-TGT-SEA-001
phase: 1
type: requirements_list
version: 2.1
created: 2026-02-10
updated: 2026-02-10
status: draft
---

# Requirements List: VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Phase:** 1 — Task Clarification
**Methodology:** Pahl & Beitz 16-category requirements list (VDI 2221)
**Source:** Phase 0 ODI analysis (73 outcomes), environmental survivability analysis, competitive RE, stakeholder analysis

---

## 1. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-10 | Engineering Team | Initial release — 125 requirements |
| 2.0 | 2026-02-10 | Engineering Team | Revision B: Platform 6.0→8.0m, superstructure removed, IR/propane removed (radar-only) |
| **2.1** | **2026-02-10** | **Engineering Team** | **Revision B.1: Reflector mounting height 1.5-2.0m → 3.0-4.0m, mast structures added, wind/mooring forces recalculated** |

### Version 2.1 Change Summary (Rev B.1)

| Change | From (Rev B) | To (Rev B.1) | Impact |
|--------|-------------|--------------|--------|
| **Reflector mounting height** | 1.5-2.0 m above waterline | **3.0-4.0 m above waterline** | Better radar visibility, reduced sea clutter interference |
| **Mast structure** | None (deck-mounted) | **8 steel masts, ~3m above deck** | New structural component, adds weight and windage |
| **Displacement** | ~850 kg | **~980 kg** | +130 kg from masts; still under 1,100 kg limit |
| **Windage area (effective)** | ~8 m² | **~10 m²** | Mast silhouettes + elevated reflectors catch faster wind |
| **Wind force (Bft 7 steady)** | 148 kgf | **185 kgf** | +25% due to larger effective windage |
| **Peak mooring load** | 1,366 kgf | **1,512 kgf** | +11% — mooring chain adequacy TBD Phase 2 |
| **Unit cost (@10)** | $34,210 | **~$35,000** | +$790 for mast system |
| **Requirements count** | 112 | **116** | 4 new requirements (GEO-010, MAT-010, FOR-011, ASM-006) |
| **GPS beacon height** | ≥2.5 m | **≥4.5 m** | Must be above reflectors (highest point on platform) |

### Previous Changes (Rev B, retained)

| Change | From | To | Impact |
|--------|------|-----|--------|
| Platform diameter | 6.0 m | **8.0 m** | Better reflector spacing, lower draft, more stability |
| Superstructure | Ship-like silhouette | **REMOVED** | Simpler, lighter, less windage |
| IR signature | 250°C MWIR propane system | **REMOVED** | Radar-only target |

---

## 2. Project Overview

| Field | Value |
|-------|-------|
| **Product Name** | Fixed Sea Target with Hyperganic Enhancement (THANH TRI-H) |
| **Project Code** | VN-TGT-SEA-001 |
| **Customer** | Vietnamese People's Navy — Weapons Test & Acceptance Directorate |
| **End Users** | Naval Test Director (S-01), Deployment Crew (S-02), Missile Operator (S-03) |
| **Development Period** | 2026 Q1 — 2027 Q3 (15-18 months) |
| **Target Unit Cost** | $33-36K (H variant) @ 10 units |
| **Core Function** | Anchored stationary radar-signature sea target for anti-ship missile acceptance testing |

---

## 3. Requirements Summary

| # | Category | MUST | WISH | Total | Quantified | % Quant. |
|---|----------|------|------|-------|------------|----------|
| 1 | Geometry | 8 | 2 | 10 | 10 | 100% |
| 2 | Kinematics | 3 | 2 | 5 | 5 | 100% |
| 3 | Forces | 8 | 3 | 11 | 10 | 91% |
| 4 | Energy | 2 | 0 | 2 | 2 | 100% |
| 5 | Material | 7 | 3 | 10 | 7 | 70% |
| 6 | Signals | 7 | 2 | 9 | 9 | 100% |
| 7 | Safety | 6 | 1 | 7 | 6 | 86% |
| 8 | Ergonomics | 5 | 2 | 7 | 7 | 100% |
| 9 | Production | 5 | 3 | 8 | 7 | 88% |
| 10 | Quality | 4 | 2 | 6 | 5 | 83% |
| 11 | Assembly | 5 | 1 | 6 | 6 | 100% |
| 12 | Transport | 4 | 2 | 6 | 6 | 100% |
| 13 | Operation | 7 | 3 | 10 | 10 | 100% |
| 14 | Maintenance | 3 | 2 | 5 | 4 | 80% |
| 15 | Costs | 5 | 2 | 7 | 7 | 100% |
| 16 | Schedule | 4 | 2 | 6 | 5 | 83% |
| | **TOTAL** | **83** | **33** | **116** | **106** | **91%** |

---

## 4. Detailed Requirements

### 4.1 Geometry

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| GEO-001 | Platform outer diameter | **8.0 m ±0.1 m (circular)** | MUST | I | Rev B: increased from 6.0m for stability + reflector spacing | 2.0m clearance between reflectors (was 1.23m) |
| GEO-002 | Hull depth (pontoon ring) | 0.5 m ±0.05 m | MUST | I | Environmental survivability (freeboard) | Provides ~0.48 m freeboard at ~980 kg displacement |
| GEO-003 | Corner reflector edge length | 0.8 m ±0.005 m | MUST | I | Final revision §1.2 (>1,000 m² RCS) | sigma_max = 152.3 m² per reflector at X-band |
| GEO-004 | Number of corner reflectors | 8 (at 45° spacing around perimeter) | MUST | I | Final revision §1.5, O-31 (360° consistency) | ±2 dB variation through 360° |
| GEO-005 | Reflector mounting height above waterline | **3.0-4.0 m** | MUST | I | **Rev B.1: Elevated for improved radar visibility** | Sea-skimming missile approach at 5-15 m altitude; height reduces sea clutter |
| GEO-006 | GPS beacon mounting height above waterline | **≥4.5 m** | MUST | I | **Rev B.1: Must be highest point on platform, above reflectors** | Above green water and reflector array |
| GEO-007 | Total displacement | **≤1,100 kg** | MUST | I | **Rev B.1: ~980 kg (hull 850 + masts 130 kg)** | Reserve buoyancy >96% at hull depth 0.5 m |
| GEO-008 | Draft at design displacement | ≤3 cm | WISH (W=3) | A, I | Hydrostatics: T = 980/1025/50.27 = 1.9 cm | Extremely shallow draft on 8.0m platform |
| GEO-009 | Clearance between adjacent reflectors | ≥1.5 m | MUST | I | Rev B: 8.0m platform gives 2.01m at deck level | Prevents inter-reflector obstruction |
| **GEO-010** | **Reflector mast/pedestal structure** | **8 masts, ≥2.5 m above deck, 45° spacing** | **MUST** | **I** | **Rev B.1: Required to achieve 3-4m reflector height** | Self-standing or guyed; deck sockets for field erection |

### 4.2 Kinematics

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| KIN-001 | Maximum roll angle in SS 6 | ≤±7.5° | MUST | A, T | Environmental survivability §6.2 | Calculated ±7.2° from wave slope |
| KIN-002 | Natural roll period | <2 s | WISH (W=2) | A | Hydrostatics (GM very high, 8.0m platform) | Stiff roll response follows wave surface |
| KIN-003 | Weathervaning freedom | 360° unrestricted rotation on mooring | MUST | D | RE deep analysis §2.1 (SPM selected) | Single-point mooring allows free rotation |
| KIN-004 | Maximum heave amplitude in SS 6 | ≤±3.0 m (wave following) | WISH (W=2) | A, T | Environmental survivability §6.3 | Platform follows wave surface (D/Lp < 0.15 at 8.0m) |
| KIN-005 | Tow speed in SS 5 | ≥3.0 knots sustained | MUST | T | Environmental survivability §3.4 | Maximum safe tow speed in SS 5 |

### 4.3 Forces

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| FOR-001 | Wind force resistance (Bft 7 mean) | Withstand **1,814 N (185 kgf)** steady | MUST | A, T | **Rev B.1: ~10 m² effective windage (elevated reflectors + masts), 15.7 m/s** | Was 148 kgf (Rev B, 8 m²) |
| FOR-002 | Wind force resistance (Bft 7 gust) | Withstand **3,557 N (363 kgf)** peak | MUST | A | **Rev B.1: 10 m² effective, 22 m/s gust** | Was 290 kgf (Rev B) |
| FOR-003 | Wave drift force resistance (SS 6) | Withstand 3,765 N (384 kgf) | MUST | A | Rev B: 8.0m platform (D=8.0) | Drift force proportional to D, unchanged |
| FOR-004 | Total mooring load (steady-state, SS 6, Bft 7) | **≤578 kgf** | MUST | A | **Rev B.1: wind 185 + current 9 + drift 384 = 578 kgf** | Was 541 kgf (Rev B) |
| FOR-005 | Peak dynamic mooring load (SS 6, Bft 7 gust) | **≤1,512 kgf** | MUST | A | **Rev B.1: (363+9+384) × 2.0 = 1,512 kgf** | Was 1,366 kgf (Rev B) |
| FOR-006 | Mooring system SWL | **≥4,536 kgf** (3:1 safety on peak) | MUST | A, I | 3:1 safety factor per marine standards | Was 4,098 kgf — **chain size TBD Phase 2 catenary analysis** |
| FOR-007 | Anchor holding power | ≥1,500 kgf (set position) | MUST | A, T | Environmental survivability §4.3 | Danforth 50 kg in sand — unchanged |
| FOR-008 | Tow line breaking strength | ≥7,524 kgf (SWL) | MUST | I | Environmental survivability §3.2 | 3:1 on peak tow load |
| FOR-009 | Green water force on deck equipment | Withstand 1,538 N (157 kgf) | WISH (W=4) | A | Environmental survivability §5.1 | **Rev B.1: Forces on mast bases and deck sockets** |
| FOR-010 | Reflector mount + mast base cyclic endurance | ≥40,000 cycles at ±7° roll amplitude | MUST | A, T | Environmental survivability §5.1 | **Rev B.1: Includes mast base fatigue at 3-4m height** |
| **FOR-011** | **Mast structural capacity (bending at base)** | **≥1,100 N·m per mast (Bft 7 gust + dynamic)** | **MUST** | **A** | **Rev B.1: Wind on reflector (178 N) + mast drag (27 N) × arm (2.5m) × 2.0 dynamic** | 60mm × 4mm steel tube minimum; Phase 2 detailed design |

### 4.4 Energy

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| ENR-001 | GPS beacon battery life | ≥72 hours continuous operation | MUST | T | Environmental survivability §7.2, S-05 | Li-ion external battery pack |
| ENR-002 | GPS beacon transmit rate | ≥1 Hz position fix | MUST | T | S-05 (scoring), O-55 (GPS reliability) | 1 Hz minimum for position tracking |

> **Note:** IR/propane energy requirements (v1.0 ENR-003 to ENR-007) **REMOVED** per Rev B. Target is radar-only.

### 4.5 Material

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| MAT-001 | Hull material | HDPE (rotomolded or welded) | MUST | I | Environmental survivability §8.3 | UV/salt/waterproof, 20+ year marine life |
| MAT-002 | Flotation fill material | Closed-cell marine foam (PU or PE) | MUST | I | Environmental survivability §8.3 | >98% reserve buoyancy even if hull breaches |
| MAT-003 | Reflector face plate material | 6061-T6 aluminum, 3 mm thick | MUST | I | Final revision §1.4 (hybrid AM/CNC) | CNC fly-cut for flatness <0.1 mm |
| MAT-004 | Reflector mounting frame material | AlSi10Mg (LPBF, as-printed + T5) | MUST | I | Final revision §1.4 | AM frame ensures ±0.1° orthogonality |
| MAT-005 | Structural frame material | Mild steel (S235 or equivalent), hot-dip galvanized | MUST | I | Phase 0 synthesis, S-08 | Local VN supply (Hoa Phat, Nam Kim) |
| MAT-006 | Mooring chain material | G30 proof coil, hot-dip galvanized | MUST | I | Final revision §2.3 | **Rev B.1: 12-16mm pending Phase 2 catenary analysis (TBD-011)** |
| MAT-007 | Reflector surface finish (face plates) | Ra ≤10 um | WISH (W=3) | I | RE deep analysis §1.4 | Adequate for X-band (lambda=32 mm >> Ra) |
| MAT-008 | Face plate surface protection | Marine anodize Type II, ≥10 um | WISH (W=4) | I | Final revision §2.2 | 5+ year saltwater corrosion resistance |
| MAT-009 | AM frame surface protection | Type III hard anodize, ≥25 um | MUST | I | Final revision §2.2 | AlSi10Mg requires protection in marine environment |
| **MAT-010** | **Reflector mast material** | **Galvanized mild steel tube or marine-grade aluminum, corrosion protected** | **MUST** | **I** | **Rev B.1: 8 masts carrying 15 kg reflectors at 3-4m height** | Min 60mm OD × 4mm wall (steel) or equivalent aluminum; hot-dip galvanized |

### 4.6 Signals

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| SIG-001 | RCS at X-band (9.4 GHz), peak combined | ≥1,000 m² (30 dBsm) | MUST | T | Final revision §1.2, O-29 | 8 x 152.3 m² peak = 1,218 m² |
| SIG-002 | RCS at X-band, 360° average | ≥1,000 m² | MUST | T | Final revision §1.2, O-31 | ~1,050 m² calculated |
| SIG-003 | RCS at X-band, 360° minimum (worst angle) | ≥700 m² | MUST | T | Final revision §1.2 | ~770 m² calculated at deepest null |
| SIG-004 | RCS angular variation through 360° | ≤±2 dB | MUST | T | Final revision §1.2, O-31 | 8 reflectors at 45° spacing |
| SIG-005 | RCS at ±7° platform roll (SS 6) | ≤1 dB degradation from boresight | MUST | A, T | Final revision §1.6, RE deep §1.3 | Trihedral tolerance ±15° for <3 dB loss |
| SIG-006 | Missile seeker acquisition range | ≥20 km (probability ≥99%) | MUST | T | S-03, O-40 | >1,000 m² RCS exceeds 150 m² threshold by 7x |
| SIG-007 | GPS beacon position accuracy | ≤±5 m CEP | MUST | T | S-05, O-16 | Standard GNSS accuracy |
| SIG-008 | GPS beacon signal availability | ≥99% during 72h deployment | WISH (W=5) | T | S-05, O-55 | Waterproof mounting required |
| SIG-009 | Reflector orthogonality tolerance (per reflector) | ≤±0.1° between faces | MUST | I | Final revision §1.4, O-29 | AM frame controls alignment; <0.5 dB RCS loss |

> **Note:** IR signature requirements (v1.0 SIG-006, SIG-007 for MWIR) **REMOVED** per Rev B. Target is radar-only.

### 4.7 Safety

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| SAF-001 | Minimum clearance distance (all personnel) | ≥5 km during engagement | MUST | D | S-04, O-35 | Passive operation, no C2 vessel required |
| SAF-002 | Operation mode during engagement | Fully passive (no operator, no C2 link) | MUST | D | Final revision §4.2, S-04 | Zero personnel in danger zone |
| SAF-003 | Mooring failure consequence | Target drifts downwind (no hazard to shipping for ≥24h) | MUST | A | S-04 | GPS beacon continues transmitting position |
| SAF-004 | Environmental debris plan | HDPE + foam debris is non-toxic, recoverable | MUST | A | S-04, O-66 | No hazardous materials in hull/flotation |
| SAF-005 | Tow safety | Bridle attachment point SWL ≥3x peak tow load | MUST | A, I | Environmental survivability §3.2 | SWL ≥7,524 kgf |
| SAF-006 | Reflector/mast retention in waves | Safety wire on all reflector mount bolts; mast locking pins | MUST | I | Final revision §2.2 | **Rev B.1: Prevent 15 kg reflector or mast falling; mast sockets include locking mechanism** |
| SAF-007 | Stability — no capsize condition | Positive GM in all loading conditions up to SS 6 | WISH (W=5) | A | Environmental survivability §6.1 | **Rev B.1: GM >210 m even with masts at 3-4m — inherently stable** |

> **Note:** Propane safety requirements (v1.0 SAF-003, SAF-004, SAF-009 for propane) **REMOVED** per Rev B. No propane system.

### 4.8 Ergonomics

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| ERG-001 | Maximum crew size for deployment | ≤4 personnel | MUST | D | S-02, O-18 | Standard tug crew complement |
| ERG-002 | Deployment time (mooring connect to ready) | ≤30 min | MUST | D | S-02, O-34 | From mooring pickup to target ready, **including mast erection** |
| ERG-003 | Maximum single-component weight (manual handling) | ≤150 kg (2-person lift with aids) | MUST | I | S-02, O-26 | Heaviest component during field ops; masts ~16 kg each |
| ERG-004 | Heaviest field-replaceable component | ≤25 kg (1-person lift) | WISH (W=4) | I | S-02 | Reflector = 15 kg, mast = 16 kg (meets this) |
| ERG-005 | Connections during deployment | Tool-free (shackles, snap hooks, quick-connect) | MUST | D | S-02, O-19 | Cold/wet hands, rough seas; **mast insertion = tool-free socket** |
| ERG-006 | Operator training time | ≤8 hours classroom + ≤4 hours hands-on | WISH (W=3) | D | S-02, O-21 | Low skill level required |
| ERG-007 | Deployment manual | Pictorial (step-by-step, multilingual VN/EN) | MUST | I | S-02 | Operational documentation deliverable |

### 4.9 Production

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| PRD-001 | Production rate capability | ≥6 units/month at steady state | MUST | A | S-08, O-64 | Supports 50-100 units/year demand |
| PRD-002 | Local content (by value) | ≥85% | MUST | A | S-06, O-73 | Vietnamese manufacturing, CNC local |
| PRD-003 | AM component supply chain | ≥2 qualified AM service bureaus | MUST | A | S-06, S-09 | ASEAN region (Xometry, Facfox, JR Tech) |
| PRD-004 | CNC face plate fabrication | Local Vietnamese CNC job shops | MUST | A | S-08, final revision §1.4 | 800x800x3 mm 6061-T6, fly-cut |
| PRD-005 | HDPE hull fabrication | Rotomolded or welded, Vietnamese supplier | MUST | A | S-08 | 8.0m diameter — may require 2-section hull |
| PRD-006 | Rejection rate target | <5% for finished units | WISH (W=4) | A | S-08 | Statistical process control |
| PRD-007 | AM frame lead time | ≤3 weeks per batch (8 frames) | WISH (W=4) | A | S-09 | From PO to delivery |
| PRD-008 | Production tooling investment | ≤$15,000 (jigs, fixtures, molds) | WISH (W=3) | A | Development budget Phase 4 | Amortized over production run |

### 4.10 Quality

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| QUA-001 | RCS compliance verification | Each unit measured 360° before delivery | MUST | T | S-01, O-30 | Portable RCS measurement or calibrated range |
| QUA-002 | Reflector orthogonality QC | 100% check with digital angle gauge (±0.1°) | MUST | I | Final revision §1.4 | Per reflector assembly |
| QUA-003 | GPS beacon functional test | 100% transmit/receive test before delivery | MUST | T | S-05, O-55 | Confirm position fix and battery capacity |
| QUA-004 | Mooring hardware inspection | 100% visual + load certificate per batch | MUST | I | S-04 (safety) | Chain, shackles, anchor per marine standard |
| QUA-005 | Unit-level acceptance test success rate | ≥95% first-pass | WISH (W=4) | A | S-08 | Indicates manufacturing maturity |
| QUA-006 | Mission success rate (seeker acquisition) | ≥98% per engagement | MUST | D | S-01, O-46 | At >1,000 m² RCS, failure rate <2% |

### 4.11 Assembly

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| ASM-001 | Reflector assembly time (per unit, 8 reflectors) | ≤4 hours (30 min/reflector) | MUST | D | Final revision §1.4 | Bolt face plates to AM frames |
| ASM-002 | Platform assembly time (complete unit) | ≤2 working days (factory) | WISH (W=3) | D | Rev B: simpler (no superstructure, no propane) | Hull + frame + mast sockets + reflectors + GPS |
| ASM-003 | Field assembly tools | Standard hand tools only (wrenches, torque wrench) | MUST | I | S-02, O-19 | No specialized equipment in field |
| ASM-004 | Reflector-to-mast attachment | Bolted with Nylock + alignment pins + safety wire | MUST | I | Final revision §2.2 | **Rev B.1: Reflector bolted to mast top plate** |
| ASM-005 | Mooring attachment to platform | Through-bolted steel pad eye with backing plate (200x200x10 mm) | MUST | I | Environmental survivability §5.2 | Distributes mooring load across structure |
| **ASM-006** | **Field mast erection (8 masts)** | **≤15 min total (2-person, insert into deck sockets)** | **MUST** | **D** | **Rev B.1: Masts inserted into welded deck sockets, locked with pins** | Mast + reflector pre-assembled as unit (~31 kg each); no crane required |

### 4.12 Transport

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| TRA-001 | Container compatibility | ≥1 target per 40 ft container (disassembled) | MUST | A, I | S-07, O-22 | 8.0m hull may need 2-section; **masts 3m long — fits in container** |
| TRA-002 | Maximum road transport width | ≤2.5 m per section (standard truck) | MUST | A | S-07 | 8.0m hull requires disassembly or oversize permit |
| TRA-003 | Tow configuration | Bridle (2-point, 60° spread) + trailing drogue | MUST | D | Environmental survivability §3.3 | Reduces yaw to ±10° in SS 5 |
| TRA-004 | Tow line specification | 16 mm Dyneema (HMPE), SWL ≥8,000 kgf, 50-100 m | MUST | I | Environmental survivability §3.2 | Or 28 mm polyester (SWL ≥6,000 kgf) |
| TRA-005 | Shelf life (stored ashore) | ≥5 years (all components) | WISH (W=4) | A | S-07, O-23 | HDPE, aluminum, steel, foam all exceed 5 years |
| TRA-006 | Depot storage | Standard covered warehouse (no climate control) | WISH (W=3) | A | S-07 | No propane = no special storage requirements |

### 4.13 Operation

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| OPR-001 | Deployment sea state | SS 4-5 (Hs = 1.25-4.0 m) | MUST | D | Environmental survivability §1.4, S-02 | Target towed and connected to pre-deployed mooring |
| OPR-002 | Survival sea state (anchored) | SS 5-6 (Hs = 2.5-6.0 m) for 72 hours | MUST | T | Final revision §6.1, O-57 | Core differentiator — storm survival |
| OPR-003 | Survival wind (anchored) | Beaufort 6-7 (22-33 kn mean, gusts to 46 kn) | MUST | T | Environmental survivability §2.2 | Northeast monsoon conditions |
| OPR-004 | Survival duration at anchor | ≥72 hours (3 days) | MUST | T | Final revision §6.1, S-01 | Pre-engagement wait time |
| OPR-005 | Water depth range | 10-80 m (depth-dependent mooring) | MUST | A | Environmental survivability §4.2 | 3 mooring configurations (shallow/medium/deep) |
| OPR-006 | Position hold accuracy (at anchor) | ≤±240 m swing radius (depth-dependent) | MUST | T | Environmental survivability §4.2 | Acceptable for offshore test range |
| OPR-007 | Ambient temperature range | -5°C to +55°C | MUST | A | Vietnamese maritime conditions | Air temperature range |
| OPR-008 | Seawater temperature range | 20°C to 32°C | WISH (W=2) | A | Vietnam East Sea data | Affects material selection |
| OPR-009 | Salt spray exposure | Continuous immersion + spray for 72h | MUST | T | MIL-STD-810H Method 509.7 | All exposed components must withstand |
| OPR-010 | Missile compatibility | **Radar-guided anti-ship missiles (X-band active seeker)** | MUST | D | S-01, S-03, O-47 | **Rev B: Radar-only. C-802, Kh-35, Exocet radar mode.** IR seekers NOT supported. |

### 4.14 Maintenance

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| MNT-001 | Target maintenance concept | Expendable — no post-engagement maintenance | MUST | — | User directive (TPMS removed) | Target destroyed by missile impact |
| MNT-002 | Mooring system recovery | Recoverable (anchor + chain/rode) for reuse | WISH (W=4) | D | S-06 (cost reduction) | Trip line on anchor for retrieval |
| MNT-003 | Pre-deployment inspection time | ≤1 hour (visual + functional check) | WISH (W=3) | D | S-02 | **Rev B.1: Includes mast socket and locking pin inspection** |
| MNT-004 | Reflector shelf maintenance | None (anodized aluminum, no corrosion maintenance) | MUST | A | MAT-008, MAT-009 | Zero maintenance during storage |
| MNT-005 | GPS beacon battery replacement | Field-replaceable, tool-free connector | MUST | I | S-02 | Swap battery pack before each deployment |

### 4.15 Costs

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| CST-001 | Unit cost (H variant, @ 10 units) | **≤$36,000** | MUST | A | **Rev B.1: ~$35,000 (add mast system ~$800)** | Including AM reflector frames + mast system |
| CST-002 | Unit cost (H variant, @ 50 units) | ≤$27,000 | WISH (W=4) | A | Volume pricing (AM frame cost reduction) | Target for series production |
| CST-003 | Unit cost (base variant, @ 10 units) | ≤$29,000 | WISH (W=3) | A | CNC-only reflectors (±0.3° tolerance) | Without AM frames |
| CST-004 | Total development budget | ≤$280,000 | MUST | A | Rev B: reduced from $292K (no propane dev, simpler prototype) | Phases 0-4 inclusive |
| CST-005 | Risk-adjusted cost per test | ≤$46,000 (including 1% missile loss) | MUST | A | $36K target + $5-10K missile loss risk | Lower target cost reduces per-test cost |
| CST-006 | 3-year TCO (50 tests) | ≤$2,600,000 | MUST | A | 50 x $36K + $280K dev + $250K ops + $250K missile loss | |
| CST-007 | Cost vs import equivalent | ≤50% of nearest comparable (SINKEX) | MUST | A | $36K vs $1,610K = 2.2% of SINKEX | Order-of-magnitude advantage |

### 4.16 Schedule

| ID | Requirement | Value/Range | Type | Verify | Source | Notes |
|----|-------------|-------------|------|--------|--------|-------|
| SCH-001 | Phase 1 completion (requirements) | ≤Q1 2026 | MUST | I | Development plan | Current phase |
| SCH-002 | Phase 2 completion (conceptual design) | ≤Q2 2026 | MUST | I | Development plan | Reflector + mast + platform design |
| SCH-003 | Phase 3 completion (prototype + validation) | ≤Q1 2027 | MUST | I | Development plan | Sea trial in SS 5 |
| SCH-004 | Phase 4 completion (production readiness) | ≤Q3 2027 | WISH (W=4) | I | Development plan | Including pilot batch (3 units) |
| SCH-005 | Total development timeline | ≤18 months | MUST | I | Final revision §6.1 | From Phase 1 start to pilot batch |
| SCH-006 | First live-fire demonstration | ≤Q2 2027 | WISH (W=5) | I | S-01, S-06 | Critical for military acceptance |

---

## 5. Standards Compliance Matrix (Summary)

| Standard | Sections | Requirements Mapped | Compliance Approach |
|----------|----------|---------------------|---------------------|
| **MIL-STD-810H** | 509.7 (salt fog), 514.8 (vibration), 507.6 (humidity) | OPR-009, FOR-010, OPR-007 | Analysis + sea trial testing |
| **MIL-STD-882E** | 4.1-4.5 (system safety) | SAF-001 to SAF-007 | Preliminary Hazard Analysis (PHA) |
| **TCVN** | Marine vessels (TBD-002) | GEO-001, MAT-005 | Compliance mapping required |
| **IALA** | Reflector mounting (advisory) | GEO-005, GEO-006 | Adapted for missile target application |
| **ASTM F3301** | AM PBF-LB/M process | MAT-004, SIG-009 | AM component qualification |

> **Note:** Propane/LPG standards (TCVN 7441, TCVN 6153, TCVN 7111) **REMOVED** per Rev B.
> Detailed standards mapping: [[standards_mapping.md]]

---

## 6. Verification Plan Summary

| Verification Type | Count | Estimated Cost | Duration | Phase |
|-------------------|-------|----------------|----------|-------|
| **Analysis (A)** | 40 | $7,000 | Phase 1-2 | Engineering calculations, FEA, RCS simulation, mast structural |
| **Inspection (I)** | 47 | $4,500 | Phase 3-4 | Dimensional, visual, material certification |
| **Test (T)** | 28 | $35,000 | Phase 3 | Sea trial (SS 5), RCS measurement, GPS endurance |
| **Demonstration (D)** | 17 | $20,000 | Phase 3-4 | Deployment exercise (incl. mast erection), live-fire demo |
| **TOTAL** | 132* | **$66,500** | | *Some requirements have multiple verification methods |

> **Rev B.1: +$1,500 vs Rev B ($65K). Additional mast structural analysis and field deployment demonstration.**

---

## 7. Open Issues & TBDs

| Issue ID | Description | Category | Owner | Target Date | Status |
|----------|-------------|----------|-------|-------------|--------|
| TBD-001 | ODI field survey validation (30-50 respondents) | All | Survey team | Q2 2026 | Open |
| TBD-002 | TCVN standards mapping for sea targets | Standards | Regulatory (S-10) | Phase 1 | Open |
| TBD-003 | AM reflector RCS measurement validation (prototype) | Signals | Engineering | Phase 2 | Open |
| TBD-004 | Software requirements specification (GPS beacon firmware) | Signals | Engineering | Phase 2 | Open |
| TBD-005 | AM service bureau qualification (min. 2 suppliers) | Production | Procurement (S-06) | Phase 2 | Open |
| TBD-006 | Mooring sea trial protocol (SS 5 anchor test) | Forces | Engineering | Phase 3 | Open |
| TBD-007 | 8.0m hull fabrication method (1-piece vs 2-section) | Production | S-08 Manufacturing | Phase 2 | Open |
| TBD-008 | Platform transport — oversize permit or disassembly for 8.0m hull | Transport | Engineering | Phase 2 | Open |
| TBD-009 | Exact CNC flatness specification for face plates (<0.1 mm TBV) | Quality | Engineering | Phase 2 | Open |
| TBD-010 | Depth-dependent mooring kit specification (3 variants) | Operation | Engineering | Phase 2 | Open |
| **TBD-011** | **Mast structural design: free-standing vs guyed, material (steel vs Al), chain size (12 vs 16mm catenary)** | **Forces/Structure** | **Engineering** | **Phase 2** | **NEW** |

---

## 8. Requirements Traceability — ODI Outcome Mapping

| ODI Outcome | Opp Score | Category | Requirement IDs |
|-------------|-----------|----------|-----------------|
| **O-57** (environmental survivability) | **18.0 EXTREME** | Operation | OPR-002, OPR-003, OPR-004 |
| **O-37** (anchor holds in SS 6) | **15.0 EXTREME** | Forces | FOR-004, FOR-005, FOR-006, FOR-007 |
| **O-71** (total cost of ownership) | **15.0 EXTREME** | Costs | CST-005, CST-006, CST-007 |
| O-29 (seeker acquisition) | 13.8 HIGH | Signals | SIG-001, SIG-002, SIG-006, SIG-009 |
| O-31 (360° RCS consistency) | 14.0 HIGH | Signals | SIG-004, GEO-004 |
| O-62 (cost per test) | 14.9 HIGH | Costs | CST-001, CST-005 |
| O-36 (capsize/instability) | 14.0 HIGH | Safety | SAF-007, KIN-001 |
| O-33 (position drift) | 14.0 HIGH | Operation | OPR-006 |
| O-40 (seeker max range) | 13.5 HIGH | Signals | SIG-006 |
| O-42 (RCS fades) | 12.5 HIGH | Signals | SIG-003, SIG-005 |
| O-73 (indigenous content) | 14.0 HIGH | Production | PRD-002, PRD-004, PRD-005 |
| O-46 (test failures from signature) | 13.5 HIGH | Quality | QUA-006 |
| O-55 (GPS reliability) | 11.5 MOD | Energy | ENR-001, ENR-002 |
| O-34 (anchor to ready time) | 12.5 HIGH | Ergonomics | ERG-002 |
| O-26 (component weight) | 10.5 MOD | Ergonomics | ERG-003, ERG-004 |
| O-35 (safe distance) | 12.0 MOD | Safety | SAF-001, SAF-002 |
| O-66 (environmental impact) | 11.0 MOD | Safety | SAF-004 |
| O-22 (storage space) | 10.0 MOD | Transport | TRA-001, TRA-006 |
| O-23 (shelf life) | 10.0 MOD | Transport | TRA-005 |

> **Note:** O-32 (360° IR visibility) and O-05 (IR uncertainty) **NOT ADDRESSED** per Rev B. Target is radar-only.

---

## 9. Stakeholder Sign-Off Mapping

| Stakeholder | Role | Requirements Responsible | Sign-Off |
|-------------|------|--------------------------|----------|
| S-01 Test Director | Accountable for all | SIG-001 to SIG-009, OPR-001 to OPR-010 | Final approval |
| S-02 Deployment Crew | Responsible: seakeeping, mooring, **mast erection** | ERG-001 to ERG-007, KIN-003, KIN-005, **ASM-006** | Operational review |
| S-03 Missile Operator | Responsible: RCS specs | SIG-001 to SIG-006, OPR-010 | Technical review (radar-only) |
| S-04 Safety Officer | Responsible: safety | SAF-001 to SAF-007 | Safety review (no propane) |
| S-05 Scoring Officer | Consulted: GPS, scoring | ENR-001, ENR-002, SIG-007, SIG-008 | Technical review |
| S-06 Procurement | Accountable: cost targets | CST-001 to CST-007, PRD-002 | Budget review |
| S-07 Depot/Logistics | Accountable: transport/storage | TRA-001 to TRA-006 | Logistics review |
| S-08 Manufacturing | Accountable: production | PRD-001 to PRD-008, ASM-001 to ASM-006 | DFM review |
| S-09 AM Bureau | Responsible: AM components | MAT-004, PRD-003, PRD-007, SIG-009 | Feasibility review |
| S-10 Regulatory | Accountable: standards | OPR-007, OPR-009 | Compliance review |

---

## 10. Conflict Register

| # | Conflict | Requirements | Resolution | Status |
|---|---------|-------------|------------|--------|
| C-01 | 0.8m reflectors on 3-4m masts vs mooring | SIG-001, GEO-005 vs FOR-004 | **Rev B.1: Wind force +25% but mooring still adequate; SWL 4,536 kgf achievable** | RESOLVED |
| C-02 | SS 5 deployment vs crew safety | OPR-001 vs SAF-001 | Pre-deploy mooring in fair weather; connect target in SS 4-5 only | RESOLVED |
| C-03 | AM precision vs local content (85%) | SIG-009 vs PRD-002 | Hybrid: CNC faces local (VN), AM frames ASEAN. 85-90% local overall | RESOLVED |
| C-04 | Storm mooring cost vs unit cost | FOR-006 vs CST-001 | +$800-3,000 per unit justified by 40-60% expanded test window | RESOLVED |
| C-05 | 8.0m platform exceeds road transport | GEO-001 vs TRA-002 | Oversize permit or 2-section hull. TBD-007 + TBD-008 | OPEN |
| C-06 | 72h GPS battery vs weight | ENR-001 vs ERG-004 | Li-ion pack (2 kg, $300) acceptable on elevated mast | RESOLVED |
| C-07 | Expendable vs unit cost | MNT-001 vs CST-001 | $36K justified by ROI vs baseline ($108K/test risk-adjusted) | RESOLVED |
| C-08 | Radar-only limits missile compatibility | OPR-010 vs O-32 | All target missiles have radar primary seeker. IR is secondary/optional. | RESOLVED |
| **C-09** | **3-4m mast height vs weight/windage** | **GEO-005 vs GEO-007, FOR-001** | **Rev B.1: Masts add 130 kg (within 1,100 kg limit) and +25% wind force (manageable). Structural design TBD-011** | **RESOLVED** |

---

## 11. Revised Unit Cost Estimate (Rev B.1)

```
UNIT COST: VN-TGT-SEA-001-H (Rev B.1 — RADAR-ONLY, 8.0m, 3-4m MASTS)
═══════════════════════════════════════════════════════

                           @ 10 units   @ 50 units   @ 100 units
COMPONENT                  ─────────    ─────────    ──────────
HDPE pontoon (8.0m circular) $7,000      $5,500       $4,800
Closed-cell foam fill        $1,200      $900         $750
Steel frame (+ mast sockets) $1,800     $1,400       $1,200
Reflector masts (8x galv.)   $800       $600         $500
Hybrid reflectors (8x 0.8m)
  CNC face plates (24x)      $4,000      $3,000       $2,400
  AM mounting frames (8x)     $8,000      $5,500       $4,000
  Assembly + QC               $1,000      $700         $500
  Subtotal reflectors        $13,000     $9,200       $6,900
Storm mooring system          $1,700      $1,400       $1,150
GPS beacon (72h battery)      $1,800      $1,500       $1,300
Tow equipment (bridle+drogue) $400       $300         $250
Assembly + QC                 $4,700      $3,400       $2,700
Margin (10%)                  $3,240      $2,470       $1,955
─────────────────────────────────────────────────────
TOTAL (H variant)            $35,640     $26,670      $21,505
─────────────────────────────────────────────────────

CHANGES vs Rev B:
  Steel frame +$300 (mast deck sockets)
  Masts       +$800 (8x galvanized steel tubes + bases)
  Assembly    +$200 (mast integration)
  Margin      +$130
  NET: +$1,430 per unit @ 10

Base variant (CNC-only reflectors, no AM frames):
  Base unit cost @ 10:       $28,640
  Base unit cost @ 50:       $21,670
```

---

## Cross-References

- [[stakeholder_analysis.md]] — Stakeholder registry, RACI matrix, needs mapping
- [[standards_mapping.md]] — Detailed MIL-STD and TCVN compliance
- [[requirements_validation.md]] — Completeness check and gate criteria
- [[../00_odi/odi_analysis.md]] — 73 ODI outcomes, opportunity scores
- [[../00_odi/phase0_final_revision.md]] — Final specifications (>1,000 m² RCS, SS 5-6, hybrid reflectors)
- [[../00_odi/environmental_survivability.md]] — Environmental survivability analysis
- [[../00_odi/re_deep_analysis.md]] — Competitor RE (reflector physics, mooring, subsystems)
- [[../PROJECT_STATUS.md]] — Project status tracker
