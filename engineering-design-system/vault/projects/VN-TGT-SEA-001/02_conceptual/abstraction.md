---
project: VN-TGT-SEA-001
phase: 2
type: abstraction
version: 1.0
created: 2026-02-10
status: draft
step: 1 of 6
---

# Step 1: Abstraction — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Remove solution-specific constraints to explore the full design space before converging on working principles.
**Method:** Pahl & Beitz 5-step abstraction process

---

## 1. Original Problem Statement

> "Design an 8.0m anchored HDPE sea target platform with 8 hybrid AM/CNC corner reflectors on steel masts producing >1,000 m² RCS at X-band, surviving SS 5-6 for 72 hours, at $35.6K/unit, for Vietnamese Navy anti-ship missile acceptance testing."

This statement contains numerous embedded solutions:
- "HDPE" → specific hull material
- "8.0m" → specific platform diameter
- "hybrid AM/CNC corner reflectors" → specific RCS generation method
- "steel masts" → specific support structure material and form
- "$35.6K" → specific cost target
- "anchored" → specific station-keeping method

The abstraction process systematically strips these to reveal the **essential function**.

---

## 2. Five-Step Abstraction

### Step 1: Remove Personal Preferences

Preferences are choices driven by familiarity, aesthetics, or habit rather than functional necessity.

| Preference | Why It's a Preference | Abstracted Form |
|-----------|----------------------|-----------------|
| "HDPE hull" | Material choice — other materials could float | "buoyant hull" |
| "AM/CNC hybrid reflectors" | Manufacturing method — other methods exist | "precision radar reflectors" |
| "steel masts" | Material/form choice for supports | "elevated supports" |
| "Danforth anchor" | Specific anchor type | "seabed restraint" |
| "GPS beacon" | Specific tracking technology | "position reporting system" |
| "circular pontoon" | Specific hull geometry | "floating platform" |

**After Step 1:** "Provide an anchored buoyant platform with 8 precision radar reflectors on elevated supports producing >1,000 m² RCS at X-band, surviving SS 5-6 for 72 hours, with position reporting, for anti-ship missile testing."

### Step 2: Omit Non-Essential Requirements

Non-essential requirements are those that support the core function but are not the function itself.

| Requirement | Essential? | Reason |
|------------|-----------|--------|
| >1,000 m² RCS at X-band | YES | Core product function — missile seeker acquisition |
| SS 5-6 survival for 72h | YES | Core differentiator — operational capability |
| Stationary at designated location | YES | Test requires known target position |
| No personnel during engagement | YES | Safety — core differentiator |
| 8 reflectors at 45° spacing | NO | Implementation detail of 360° coverage |
| ≤4 crew for deployment | NO | Operational preference, not core function |
| ≤$36K unit cost | NO | Business constraint, not physical function |
| 85% local content | NO | Policy constraint, not physical function |
| GPS position reporting | NO | Support function, not core |
| Tow deployment | NO | One method of transport |

**After Step 2:** "Provide a stationary floating body with high radar cross-section from all directions, anchored at a designated position, surviving storm sea conditions for extended duration, with no personnel present during engagement."

### Step 3: Transform Quantitative to Qualitative

| Quantitative | Qualitative |
|-------------|-------------|
| >1,000 m² RCS | Frigate-class radar signature |
| ±2 dB variation, 360° | Omnidirectional radar signature |
| SS 5-6, Bft 6-7 | Rough to very rough open sea |
| 72 hours | Extended duration (multi-day) |
| ≥5 km clearance | Safe distance (well beyond weapon danger zone) |
| 8.0 m diameter | Large enough for stability and reflector spacing |
| 980 kg displacement | Within practical deployment weight |

**After Step 3:** "Provide a stationary floating body with frigate-class omnidirectional radar signature, anchored at a designated position in rough open sea for multi-day duration, requiring no personnel during weapon engagement."

### Step 4: Generalize

| Specific | Generalized |
|---------|-------------|
| Anti-ship missile acceptance testing | Radar-guided weapon evaluation |
| Vietnamese Navy | Any naval force |
| C-802, Kh-35, Exocet | Any active radar seeker |
| Frigate-class | High-magnitude (appropriate to seeker design) |
| Anchored at designated position | Holds station at defined location |

**After Step 4:** "Provide a stationary floating body with controlled, high-magnitude radar cross-section from all horizontal approach directions, holding station at a defined location in rough sea conditions for extended duration, with no personnel during engagement."

### Step 5: Formulate Solution-Neutral Problem Statement

Remove all remaining technology references. Express as pure function.

---

## 3. Essential Problem Statement

> **"Provide a stationary, anchored floating body that presents a controlled, high-magnitude radar cross-section from all horizontal approach directions, surviving rough open-sea conditions for extended duration, requiring no personnel during engagement, at minimum lifecycle cost."**

### 3.1 Decomposition of Essential Problem

| Element | Function | Implies |
|---------|----------|---------|
| "stationary, anchored floating body" | **Float + Hold position** | Buoyancy + Station-keeping |
| "controlled, high-magnitude radar cross-section" | **Generate signature** | Precision RCS generation |
| "from all horizontal approach directions" | **Omnidirectional** | 360° coverage requirement |
| "surviving rough open-sea conditions" | **Withstand environment** | Structural + stability design |
| "for extended duration" | **Endure** | Material durability, energy storage |
| "requiring no personnel during engagement" | **Passive operation** | No active systems, no C2 |
| "at minimum lifecycle cost" | **Cost-effective** | Design for manufacture, simplicity |

---

## 4. Abstract Functions Identified

From the essential problem statement, 8 abstract functions are derived. These become the basis for the function structure (Step 2).

| # | Abstract Function | What It Must Do | Key Requirements Mapped |
|---|-------------------|-----------------|-------------------------|
| **AF-1** | Float stably at sea surface | Provide buoyancy, maintain stability in waves, achieve required draft/freeboard | GEO-001 to GEO-010, KIN-001 to KIN-004, SAF-007 |
| **AF-2** | Hold position at designated location | Resist wind, current, wave drift forces; stay within acceptable swing radius | FOR-001 to FOR-011, OPR-005, OPR-006 |
| **AF-3** | Generate controlled radar signature | Produce >1,000 m² RCS at X-band, 360° omnidirectional, ≤±2 dB variation | SIG-001 to SIG-009 |
| **AF-4** | Support signature elements above water | Elevate radar reflectors above sea clutter, above green water | GEO-005, GEO-010, FOR-011 |
| **AF-5** | Report position to shore | Transmit location data for test coordination and safety | ENR-001, ENR-002, SIG-007, SIG-008 |
| **AF-6** | Enable transport and deployment | Allow movement to test site, connection to mooring, crew operations | TRA-001 to TRA-006, ERG-001 to ERG-007, KIN-005 |
| **AF-7** | Withstand environmental loads | Survive wave, wind, current, salt spray for ≥72h without structural failure | OPR-001 to OPR-009, FOR-009, FOR-010 |
| **AF-8** | Be producible at target cost | Manufacturable with local content, at volume, within cost target | PRD-001 to PRD-008, CST-001 to CST-007 |

### 4.1 Function Hierarchy

```
ESSENTIAL PROBLEM (Solution-Neutral)
│
├── AF-1: FLOAT STABLY ──────────── Physical domain (buoyancy, hydrostatics)
├── AF-2: HOLD POSITION ─────────── Mechanical domain (mooring, anchor)
├── AF-3: GENERATE SIGNATURE ────── Electromagnetic domain (RCS, reflection)
├── AF-4: SUPPORT ELEMENTS ──────── Structural domain (mast, loads)
├── AF-5: REPORT POSITION ──────── Information domain (GPS, telemetry)
├── AF-6: ENABLE DEPLOYMENT ─────── Operational domain (tow, crew, logistics)
├── AF-7: WITHSTAND ENVIRONMENT ─── Environmental domain (waves, wind, corrosion)
└── AF-8: BE PRODUCIBLE ─────────── Manufacturing domain (DFM, cost, supply chain)
```

### 4.2 Solution Space Width

The abstraction reveals that the design space is wider than the current Rev B.1 architecture suggests:

| Abstract Function | Current Solution (Rev B.1) | Alternative Solution Space |
|-------------------|---------------------------|---------------------------|
| AF-1: Float | HDPE circular pontoon | Spar buoy, catamaran, inflatable, steel barge, foam block |
| AF-2: Hold position | Single-point mooring | Multi-point, dynamic positioning, deadweight, sea anchor |
| AF-3: Generate signature | Trihedral corner reflectors | Luneburg lens, active transponder, flat plates, dielectric lens |
| AF-4: Support elements | Fixed steel masts | Guyed masts, A-frames, pedestals, cables, inflatable columns |
| AF-5: Report position | GPS beacon (satellite) | AIS, RACON, Iridium, radio beacon, passive radar reflector |
| AF-6: Deploy | Surface tow by tug | Self-propelled, helicopter, ship crane, air-drop, swim-in |
| AF-7: Withstand environment | Robust structure (over-engineer) | Breakaway/sacrificial, submersible, wave-conforming |
| AF-8: Be producible | HDPE + steel + CNC + AM | All-steel, all-plastic, inflatable, modular kit |

**Key insight:** The abstraction confirms that the current architecture addresses only ONE path through a wide solution space. Phase 2 Steps 3-5 will systematically explore alternatives and validate that the current path is optimal.

---

## 5. Constraints vs. Requirements

A critical output of abstraction is distinguishing true requirements (non-negotiable) from constraints (negotiable or implementation-dependent):

### 5.1 True Requirements (Cannot Be Relaxed)

| # | Requirement | Source | Why Non-Negotiable |
|---|-------------|--------|-------------------|
| 1 | RCS >1,000 m² at X-band | Missile seeker physics | Below this, seeker acquisition degrades significantly |
| 2 | 360° coverage (≤±2 dB) | Unknown missile approach angle | Target must work from any direction |
| 3 | Survive SS 5-6 for 72h | Northeast monsoon conditions | Core differentiator; deployment window |
| 4 | No personnel during engagement | Safety (missile impact) | Non-negotiable safety requirement |
| 5 | Hold position at designated location | Test range requirements | Missile must know where target is |
| 6 | Expendable | User directive | Target destroyed by missile impact |

### 5.2 Soft Constraints (Can Be Traded Off)

| # | Constraint | Current Value | Trade-Off Space |
|---|-----------|---------------|-----------------|
| 1 | Unit cost | $35.6K | Could accept $40-45K if performance improves |
| 2 | Local content | 85-90% | Could accept 70-80% if cost/performance justified |
| 3 | Platform diameter | 8.0 m | Could be 6-10m depending on concept |
| 4 | Displacement | 980 kg | Could be 500-2,500 kg depending on concept |
| 5 | Deployment crew | ≤4 | Could be 5-6 if concept requires |
| 6 | Deployment time | ≤30 min | Could be 1-2 hours if concept is simpler overall |

---

## Cross-References

- [[function_structure.md]] — Step 2: Function structure (next)
- [[working_principles.md]] — Step 3: Working principles search
- [[morphological_matrix.md]] — Step 4: Concept generation
- [[concept_evaluation.md]] — Step 5: VDI 2225 evaluation
- [[concept_selection.md]] — Step 6: Selection decision
- [[../01_requirements/requirements_list.md]] — 116 requirements (input)
- [[../00_odi/phase0_final_revision.md]] — Phase 0 final specs
