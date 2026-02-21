---
project: VN-TGT-SEA-001
phase: 2
type: function_structure
version: 1.0
created: 2026-02-10
status: draft
step: 2 of 6
---

# Step 2: Function Structure — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Decompose the overall function into sub-functions with defined energy, material, and signal flows.
**Method:** Pahl & Beitz function structure with E/M/S flow analysis
**Input:** [[abstraction.md]] — 8 abstract functions from essential problem

---

## 1. Overall Function

### 1.1 Statement

**Overall Function:** Present radar target at sea for weapon engagement

This is derived from the essential problem statement by selecting the primary action verb + object.

### 1.2 System Boundary

```
SYSTEM BOUNDARY: VN-TGT-SEA-001
═══════════════════════════════════════════════════════════════════

                    ENVIRONMENT
                    ┌─────────────────────────────────────────┐
                    │  Wind (Bft 6-7)                         │
                    │  Waves (SS 5-6, Hs 2.5-6.0 m)          │
                    │  Current (≤1.5 m/s)                     │
                    │  Salt spray / immersion                 │
                    │  Temperature (-5 to +55°C)              │
                    │  Radar illumination (X-band, 9.4 GHz)   │
                    └────────────────┬────────────────────────┘
                                     │
    INPUTS                           │                    OUTPUTS
    ═══════                     ╔════╧════╗               ════════
    E: Wave energy ────────────►║         ║──────────► E: Reflected radar (RCS)
    E: Wind energy ────────────►║  TARGET ║──────────► E: Dissipated energy
    E: Current energy ─────────►║  SYSTEM ║──────────► S: GPS position → shore
    S: Radar illumination ─────►║         ║──────────► S: Radar return → missile
    M: Seawater (contact) ─────►║         ║──────────► M: Debris (post-engagement)
                                ╚════╤════╝
                                     │
                              SEABED │ (anchor point)
                              ───────┘
```

### 1.3 Input/Output Classification

| Flow | Type | Description | Magnitude |
|------|------|-------------|-----------|
| **Inputs** | | | |
| E-in-1 | Energy | Wave loading (SS 6) | ~3,765 N wave drift |
| E-in-2 | Energy | Wind loading (Bft 7) | ~1,814 N steady, 3,557 N gust |
| E-in-3 | Energy | Current drag | ~87 N |
| S-in-1 | Signal | Radar illumination (X-band) | Incident power density varies with range |
| M-in-1 | Material | Seawater (hull contact + spray) | Continuous immersion + salt spray |
| **Outputs** | | | |
| E-out-1 | Energy | Reflected radar energy | >1,000 m² RCS (>30 dBsm) |
| E-out-2 | Energy | Dissipated energy (drag, motion) | = E-in-1 + E-in-2 + E-in-3 |
| S-out-1 | Signal | GPS position data | ±5m CEP, 1 Hz, 72h continuous |
| S-out-2 | Signal | Radar return to missile seeker | Same as E-out-1 (signal perspective) |
| M-out-1 | Material | Post-engagement debris | HDPE + foam + aluminum + steel fragments |

---

## 2. Sub-Function Decomposition

### 2.1 Function Tree

```
┌─────────────────────────────────────────────────────────────────────┐
│         F0: PRESENT RADAR TARGET AT SEA FOR ENGAGEMENT              │
│              (Overall Function)                                      │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
  ┌─────────┬─────────┬────────┼────────┬─────────┬─────────┐
  │         │         │        │        │         │         │
  ▼         ▼         ▼        ▼        ▼         ▼         ▼
┌─────┐ ┌───────┐ ┌───────┐ ┌─────┐ ┌───────┐ ┌───────┐ ┌───────┐
│ F1  │ │  F2   │ │  F3   │ │ F4  │ │  F5   │ │  F6   │ │  F7   │
│Float│ │ Hold  │ │Genera-│ │Supp-│ │Report │ │Deploy/│ │With-  │
│stab-│ │posit- │ │te RCS │ │ort  │ │posit- │ │recov- │ │stand  │
│ly   │ │ion    │ │       │ │above│ │ion    │ │er     │ │envir. │
└──┬──┘ └──┬────┘ └──┬────┘ └──┬──┘ └──┬────┘ └──┬────┘ └──┬────┘
   │       │         │         │       │         │         │
   ▼       ▼         ▼         ▼       ▼         ▼         ▼
┌─────┐ ┌─────┐ ┌────────┐ ┌─────┐ ┌─────┐ ┌────────┐ ┌────────┐
│F1.1 │ │F2.1 │ │F3.1    │ │F4.1 │ │F5.1 │ │F6.1    │ │F7.1    │
│Buoy-│ │Anch-│ │Reflect │ │Elev-│ │Acqui│ │Trans-  │ │Resist  │
│ancy │ │or   │ │radar   │ │ate  │ │re   │ │port to │ │wave    │
│     │ │hold │ │signal  │ │refl.│ │GPS  │ │site    │ │loads   │
├─────┤ ├─────┤ ├────────┤ ├─────┤ ├─────┤ ├────────┤ ├────────┤
│F1.2 │ │F2.2 │ │F3.2    │ │F4.2 │ │F5.2 │ │F6.2    │ │F7.2    │
│Stab-│ │Cate-│ │Distri- │ │Bear │ │Trans│ │Connect │ │Resist  │
│ility│ │nary │ │bute    │ │loads│ │mit  │ │to moor-│ │wind    │
│     │ │scope│ │360°    │ │     │ │data │ │ing     │ │loads   │
├─────┤ ├─────┤ ├────────┤ ├─────┤ ├─────┤ ├────────┤ ├────────┤
│F1.3 │ │F2.3 │ │F3.3    │ │F4.3 │ │F5.3 │ │F6.3    │ │F7.3    │
│Self-│ │Weat-│ │Maintain│ │Resi-│ │Store│ │Erect   │ │Resist  │
│drain│ │herv-│ │orthog- │ │st   │ │ener-│ │struct- │ │corros- │
│deck │ │ane  │ │onality │ │wind │ │gy   │ │ures    │ │ion     │
└─────┘ └─────┘ └────────┘ └─────┘ └─────┘ └────────┘ └────────┘
```

### 2.2 Sub-Function Detail Table

| ID | Sub-Function | Input Flows | Output Flows | Type | Critical Req. |
|----|--------------|-------------|--------------|------|---------------|
| **F1** | **Float stably at sea surface** | E: wave/wind loads; M: seawater | E: dissipated (drag); M: displaced water | **Main** | GEO-001, KIN-001, SAF-007 |
| F1.1 | Provide buoyancy | M: displaced water volume | E: upward buoyancy force | Auxiliary | GEO-007 (≤1,100 kg) |
| F1.2 | Maintain stability | E: wave excitation | E: restoring moment (GM × displacement × sin θ) | Auxiliary | KIN-001 (≤±7.5° roll) |
| F1.3 | Self-drain deck | M: green water (wave overtopping) | M: water returned to sea via scuppers | Auxiliary | FOR-009 |
| **F2** | **Hold position at designated location** | E: wind + current + wave drift | E: anchor holding → seabed | **Main** | FOR-004-007, OPR-005-006 |
| F2.1 | Anchor to seabed | E: horizontal mooring load | E: friction/holding force in seabed | Auxiliary | FOR-007 (≥1,500 kgf) |
| F2.2 | Provide catenary scope | E: tension in chain/rode | E: gravity (chain weight) absorbs shock | Auxiliary | FOR-005 (≤1,512 kgf peak) |
| F2.3 | Allow weathervaning | E: asymmetric wind/wave/current | E: rotation about mooring point | Auxiliary | KIN-003 (360° rotation) |
| **F3** | **Generate controlled radar signature** | S: incident radar (X-band) | S: reflected radar (>1,000 m², 360°) | **Main** | SIG-001-006, SIG-009 |
| F3.1 | Reflect radar signal | S: incident electromagnetic wave | S: retroreflected wave (3-bounce) | Core | SIG-001 (≥1,000 m²) |
| F3.2 | Distribute coverage 360° | S: reflections from multiple reflectors | S: omnidirectional RCS pattern | Core | SIG-004 (≤±2 dB) |
| F3.3 | Maintain orthogonality | E: structural loads, thermal expansion | S: stable RCS (tolerance ±0.1°) | Core | SIG-009 (±0.1°) |
| **F4** | **Support signature elements above water** | E: weight + wind + wave-induced loads | E: reaction forces → deck → hull | **Main** | GEO-005, GEO-010, FOR-011 |
| F4.1 | Elevate reflectors to 3-4m AGL | E: reflector weight (15 kg) + wind (178 N) | E: bending moment at base (≥1,100 N·m) | Auxiliary | GEO-005 (3-4m AGL) |
| F4.2 | Bear cyclic loads | E: wave-induced oscillation (40,000+ cycles) | E: fatigue resistance | Auxiliary | FOR-010 (≥40,000 cycles) |
| F4.3 | Resist wind on elevated elements | E: gust wind force (Bft 7, 22 m/s) | E: bending + shear at mast base | Auxiliary | FOR-011 (≥1,100 N·m) |
| **F5** | **Report position to shore** | E: battery energy | S: GPS coordinates (±5m, 1 Hz) | **Support** | ENR-001-002, SIG-007-008 |
| F5.1 | Acquire GPS position | S: satellite signals | S: computed position fix | Auxiliary | SIG-007 (±5m CEP) |
| F5.2 | Transmit position data | E: electrical power; S: position data | S: transmitted signal → satellite/shore | Auxiliary | SIG-008 (≥99% availability) |
| F5.3 | Store energy for 72h | E: chemical energy (battery) | E: electrical power (regulated) | Auxiliary | ENR-001 (≥72h) |
| **F6** | **Enable deployment and recovery** | E: tug propulsion; M: tow line | E: tow resistance; S: crew instructions | **Support** | ERG-001-007, TRA-001-006 |
| F6.1 | Transport to test site | E: tug power → tow line → target | E: drag resistance (tow) | Auxiliary | KIN-005 (≥3.0 kn in SS 5) |
| F6.2 | Connect to pre-deployed mooring | M: shackle/hook connection | E: mooring load path established | Auxiliary | ERG-005 (tool-free) |
| F6.3 | Erect field structures | M: mast + reflector units | E: structural connection (socket insert) | Auxiliary | ASM-006 (≤15 min, 2-person) |
| **F7** | **Withstand environmental loads** | E: wave, wind, current, thermal | E: structural resistance | **Support** | OPR-001-009 |
| F7.1 | Resist wave loads | E: hydrostatic + hydrodynamic forces | E: hull structural resistance | Auxiliary | OPR-002 (SS 5-6) |
| F7.2 | Resist wind loads | E: aerodynamic forces on exposed area | E: structural + mooring resistance | Auxiliary | OPR-003 (Bft 6-7) |
| F7.3 | Resist corrosion | M: saltwater, salt spray, UV | M: protective coatings maintain integrity | Auxiliary | OPR-009 (72h salt spray) |

---

## 3. Flow Diagrams

### 3.1 Energy Flow

```
ENERGY FLOW DIAGRAM
═══════════════════════════════════════════════════════════════════

                Wave Energy          Wind Energy        Current
                (SS 5-6)            (Bft 6-7)          (≤1.5 m/s)
                    │                    │                  │
                    ▼                    ▼                  ▼
              ┌──────────┐       ┌──────────┐       ┌──────────┐
              │  F7.1    │       │  F7.2    │       │  F7.1    │
              │  Resist  │       │  Resist  │       │  Resist  │
              │  wave    │       │  wind    │       │  current │
              └────┬─────┘       └────┬─────┘       └────┬─────┘
                   │                  │                   │
                   ▼                  ▼                   ▼
              ┌──────────────────────────────────────────────┐
              │         F1: FLOAT STABLY                      │
              │  F1.1 Buoyancy ← displaced water              │
              │  F1.2 Stability ← GM restoring moment         │
              │  F1.3 Self-drain ← scuppers                   │
              └──────────────────────┬───────────────────────┘
                                     │ Mooring load
                                     ▼
              ┌──────────────────────────────────────────────┐
              │         F2: HOLD POSITION                     │
              │  F2.1 Anchor hold ← seabed friction           │
              │  F2.2 Catenary ← chain weight absorbs shock   │
              │  F2.3 Weathervane ← free rotation on SPM      │
              └──────────────────────┬───────────────────────┘
                                     │ Reaction force
                                     ▼
                                  SEABED
```

### 3.2 Signal Flow

```
SIGNAL FLOW DIAGRAM
═══════════════════════════════════════════════════════════════════

Missile Radar                                          GPS Satellites
(X-band, 9.4 GHz)                                    (L-band)
      │                                                    │
      ▼                                                    ▼
┌──────────┐                                        ┌──────────┐
│  F3.1    │                                        │  F5.1    │
│  Reflect │                                        │  Acquire │
│  radar   │                                        │  GPS fix │
│  signal  │                                        └────┬─────┘
└────┬─────┘                                             │
     │                                                   ▼
     ▼                                             ┌──────────┐
┌──────────┐                                       │  F5.2    │
│  F3.2    │                                       │  Transmit│
│  Distri- │                                       │  position│
│  bute    │                                       └────┬─────┘
│  360°    │                                            │
└────┬─────┘                                            ▼
     │                                          Shore Station
     ▼                                          (test control)
Missile Seeker
(acquires target at >20 km)
```

### 3.3 Material Flow

```
MATERIAL FLOW DIAGRAM
═══════════════════════════════════════════════════════════════════

       Seawater                     Air (ambient)
          │                              │
          ▼                              ▼
    ┌──────────┐                  ┌──────────┐
    │ Hull     │                  │ Above-   │
    │ contact  │                  │ water    │
    │ (immersn)│                  │ (salt    │
    │          │                  │  spray)  │
    └────┬─────┘                  └────┬─────┘
         │                             │
         ▼                             ▼
    F7.3: Resist corrosion       F7.3: Resist corrosion
    (HDPE inherent,              (galvanize, anodize,
     foam fill)                   marine coatings)

    POST-ENGAGEMENT:
    M-out: HDPE + foam + aluminum + steel debris
           (non-toxic, recoverable per SAF-004)
```

---

## 4. Interface Definitions

### 4.1 Internal Interfaces

| ID | Interface | Between | Flow Type | Critical Parameter | Requirement |
|----|-----------|---------|-----------|-------------------|-------------|
| **I-1** | Hull ↔ Mooring | F1 ↔ F2 | Energy | Pad eye SWL ≥4,536 kgf; cyclic fatigue | FOR-006, ASM-005 |
| **I-2** | Deck ↔ Mast base | F1 ↔ F4 | Energy | Mast socket bending ≥1,100 N·m; 40,000+ cycles | FOR-011, FOR-010 |
| **I-3** | Mast top ↔ Reflector | F4 ↔ F3 | Energy + Signal | 15 kg weight + wind load; must not affect orthogonality | GEO-005, SIG-009 |
| **I-4** | Mast ↔ GPS beacon | F4 ↔ F5 | Energy + Signal | <5 kg at ≥4.5m AGL; unobstructed sky view | GEO-006, SIG-008 |
| **I-5** | Hull ↔ Tow bridle | F1 ↔ F6 | Energy | Tow SWL ≥7,524 kgf; 2-point attachment | FOR-008, TRA-003 |
| **I-6** | Hull ↔ Mooring chain | F1 ↔ F2 | Energy + Material | Chain connects through fairlead to pad eye | FOR-006, I-1 |

### 4.2 External Interfaces

| ID | Interface | Between | Flow Type | Critical Parameter |
|----|-----------|---------|-----------|-------------------|
| **E-1** | Anchor ↔ Seabed | F2 ↔ Environment | Energy | Holding ≥1,500 kgf in sand/mud |
| **E-2** | Hull ↔ Seawater | F1 ↔ Environment | Energy + Material | Hydrostatic pressure, corrosion |
| **E-3** | Reflectors ↔ Radar | F3 ↔ Missile | Signal | >1,000 m² RCS return |
| **E-4** | GPS antenna ↔ Satellites | F5 ↔ GPS constellation | Signal | ±5m CEP, 1 Hz |
| **E-5** | Target ↔ Tug | F6 ↔ Deployment vessel | Energy | Tow force ≤2,061 kgf at 5 kn |

### 4.3 Interface Criticality Matrix

```
INTERFACE CRITICALITY
═══════════════════════════════════════════════════════════════════

                    CONSEQUENCE OF FAILURE
                    Low         Medium        High
                 ┌───────────┬─────────────┬─────────────┐
           High  │           │   I-2       │   I-1       │
LIKELIHOOD       │           │  (mast base)│  (pad eye)  │
OF FAILURE       │           │             │             │
                 ├───────────┼─────────────┼─────────────┤
           Med   │   I-4     │   I-3       │   E-1       │
                 │ (GPS mnt) │  (refl mnt) │  (anchor)   │
                 ├───────────┼─────────────┼─────────────┤
           Low   │   I-5     │   I-6       │   E-3       │
                 │ (tow brid)│  (chain)    │  (RCS perf) │
                 └───────────┴─────────────┴─────────────┘

CRITICAL INTERFACES (require detailed Phase 3 design):
  I-1: Pad eye → hull frame (SWL 4,536 kgf, fatigue)
  I-2: Mast socket → deck (1,100 N·m bending, 40,000 cycles)
  E-1: Anchor → seabed (1,500 kgf holding in SS 6)
```

---

## 5. Requirements Coverage Verification

All 116 requirements from [[../01_requirements/requirements_list.md]] mapped to sub-functions:

| Category | Count | Functions Covered | Coverage |
|----------|-------|-------------------|----------|
| 1. Geometry (GEO) | 10 | F1, F3, F4, F5 | 100% |
| 2. Kinematics (KIN) | 5 | F1, F2, F6 | 100% |
| 3. Forces (FOR) | 11 | F1, F2, F4, F7 | 100% |
| 4. Energy (ENR) | 2 | F5 | 100% |
| 5. Material (MAT) | 10 | F1, F2, F3, F4, F7 | 100% |
| 6. Signals (SIG) | 9 | F3, F5 | 100% |
| 7. Safety (SAF) | 7 | F1, F2, F4, F6 | 100% |
| 8. Ergonomics (ERG) | 7 | F6 | 100% |
| 9. Production (PRD) | 8 | F1, F3 (DFM) | 100% |
| 10. Quality (QUA) | 6 | F3, F5 | 100% |
| 11. Assembly (ASM) | 6 | F3, F4, F6 | 100% |
| 12. Transport (TRA) | 6 | F6 | 100% |
| 13. Operation (OPR) | 10 | F1, F2, F7 | 100% |
| 14. Maintenance (MNT) | 5 | F3, F5, F6 | 100% |
| 15. Costs (CST) | 7 | All (system level) | 100% |
| 16. Schedule (SCH) | 6 | All (system level) | 100% |
| **TOTAL** | **116** | **F1-F7** | **100%** |

---

## Cross-References

- [[abstraction.md]] — Step 1: Abstraction (input)
- [[working_principles.md]] — Step 3: Working principles (next)
- [[morphological_matrix.md]] — Step 4: Concept generation
- [[concept_evaluation.md]] — Step 5: VDI 2225 evaluation
- [[concept_selection.md]] — Step 6: Selection decision
- [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1)
