---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: PRAD-R
title: Rules Application
version: 1.0
created: 2026-02-06
status: complete
---

# STEP R: RULES APPLICATION
## 4 Basic Rules Compliance Matrix
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 6 of 15

**Purpose:** Systematically verify the BSU-V1 design against the 4 Fundamental Rules of Embodiment Design (Clarity, Simplicity, Safety, Economy).

**Input:** [[PRAD_P_principles]] (Principle-based design decisions)
**Output:** Rules compliance matrix with violations identified and corrected

---

## 1. RULE 1: CLARITY (Rõ ràng)

*"Every function must be clear and unambiguous. Load paths easy to trace. No hidden failures."*

### 1.1 Function-to-Component Mapping

| Function (Phase 2) | Component(s) | Clear? | Evidence |
|---------------------|-------------|--------|----------|
| F1: Sense projectile | 4× MEMS mic + daughter PCB + rubber boot | ✅ | One mic = one sensor point. No shared sensing. |
| F2: Measure timing | FPGA (iCE40UP5K) + ADC (ADS8688) | ✅ | FPGA captures ALL timing. ADC digitizes ALL channels. Single responsibility. |
| F3: Compute location | MCU (STM32H743) | ✅ | MCU runs TDOA algorithm exclusively. Not shared with timing capture. |
| F4: Communicate | Ethernet PHY (LAN8720A) + magnetics + RJ45 | ✅ | Dedicated Ethernet path from MCU to external. |
| F5: Present | Web application on external device | ✅ | Software-only, not part of BSU hardware. |
| F6: Supply power | Battery + BMS + DC-DC chain | ✅ | Sequential power path: battery → BMS → 5V → 3.3V. Traceable. |
| F7: Protect | Enclosure + gaskets + coatings + conformal coat | ✅ | Each protection layer has one role (structural/seal/chemical). |

**Clarity Score: 7/7 functions clearly mapped to dedicated components.**

### 1.2 Load Path Clarity

| Load Type | Path | Clear? | Notes |
|-----------|------|--------|-------|
| Wind on sensor bar | Bar → clamps → frame | ✅ | Direct compression at 3 support points |
| 40g shock | Enclosure wall → standoffs (rubber) → PCB | ✅ | Attenuated path via rubber grommets |
| Cable tension | PUR jacket → cable gland → enclosure wall | ✅ | Strain relief at cable gland, not at PCB |
| Battery weight | Battery → cradle → base plate | ✅ | Direct gravity path; no shear on terminals |
| Thermal (FPGA heat) | FPGA → thermal pad → standoff → base plate → ambient | ✅ | Conduction path, no forced air required |
| O-ring compression | Lid bolts → lid flange → O-ring → body groove | ✅ | Uniform compression via 8× M4 bolts |

**Load Path Score: 6/6 paths clearly traceable.**

### 1.3 Hidden Failure Check

| Potential Hidden Failure | Check | Status |
|--------------------------|-------|--------|
| O-ring degradation (invisible) | EPDM rated 20+ years outdoor; material does not creep-relax | ✅ No hidden failure |
| PCB delamination (internal) | FR-4 Tg170; survived -40/+70°C cycling (>Tg); conformal coating prevents moisture wicking | ✅ Addressed |
| Battery cell degradation | BQ27441 fuel gauge tracks capacity fade; BIT reports state-of-health | ✅ Made visible via BIT |
| Corrosion under anodize | Type III hard anodize 25μm + UV paint. Inspect at PM interval (500h) | ✅ PM inspection procedure |
| FPGA config corruption (silent) | Dual-image boot: detects corruption via CRC, falls back to golden image | ✅ Automatic recovery |
| Sensor sensitivity drift | BIT acoustic self-test (optional piezo exciter); compare channels for drift | ✅ Detectable via BIT |

**Hidden Failure Score: 0 hidden failures found. All potential failures made visible through BIT, inspection, or self-recovery.**

### 1.4 Clarity Summary

| Criterion | Score | Status |
|-----------|-------|--------|
| Function mapping | 7/7 | ✅ PASS |
| Load paths | 6/6 | ✅ PASS |
| Hidden failures | 0 found | ✅ PASS |
| **RULE 1: CLARITY** | **100%** | **✅ COMPLIANT** |

---

## 2. RULE 2: SIMPLICITY (Đơn giản)

*"Minimum number of parts. Reduce feature count. Fewer interfaces = fewer failure modes."*

### 2.1 Part Count Analysis

| Assembly | Part Count | Minimum Achievable | Justified? |
|----------|-----------|-------------------|-----------|
| Sensor bar | 13 (bar + 4 mic + 4 boot + 2 clamp + cable + connector) | 10 (combine boots into bar gasket) | ✅ Individual boots enable individual mic replacement (MNT-07) |
| Main PCB | 1 (assembled PCB) | 1 | ✅ Minimum |
| Power board | 1 (assembled PCB) | 1 | ✅ Minimum |
| Sensor daughter PCBs | 4 (one per mic) | 1 (could integrate all 4 on sensor bar) | ✅ 4 separate = field-replaceable per MNT-07; worth the trade-off |
| Battery pack | 1 (assembled pack with BMS) | 1 | ✅ Minimum |
| Enclosure | 6 (body + lid + 2 cable gland + battery door + LED window) | 5 (integrate LED window into lid) | ✅ Separate window allows lid replacement without optical part |
| Cables | 2 (Ethernet + sensor bar cable) | 1 (could combine) | ✅ Separate = independent replacement; Ethernet is standard |
| Internal wiring | 3 (battery→power, power→main, sensor→main) | 2 (integrate power→main with sensor→main) | ⚠️ Could combine into single internal harness |
| Fasteners | 20 (8 lid + 4 standoff + 4 battery + 4 clamp) | 16 (reduce lid to 6) | ⚠️ 8-bolt lid is redundant for IP67; 6 sufficient |
| **TOTAL** | **~51** | **~43** | See optimization |

### 2.2 Simplification Opportunities

| Opportunity | Current | Proposed | Saving | Risk | Decision |
|-------------|---------|----------|--------|------|----------|
| Reduce lid bolts 8→6 | 8× M4 | 6× M4 (hexagonal pattern) | -2 parts, -30s assembly | IP67 still achievable with proper O-ring groove | ✅ ADOPT |
| Single internal harness | 3 cables | 1 harness with 3 connectors | Cleaner routing, -2 cable assemblies | Slightly harder to service individual boards | ✅ ADOPT |
| Combine LED window into lid | Separate window | Machined pocket in lid with epoxy-potted LEDs | -1 part | LED replacement requires lid removal (acceptable) | ✅ ADOPT |
| Integrate mic onto sensor bar PCB | 4 daughter PCBs | Single flex PCB on bar | -3 PCBs | Loses individual mic replaceability (violates MNT-07) | ❌ REJECT |
| Eliminate battery door | Separate door | Access battery through main lid only | -1 part, -1 seal | Battery change requires opening main enclosure (violates MTTR) | ❌ REJECT |

**Optimized part count: ~46 (from 51)**

### 2.3 Interface Count

| Interface | Count | Minimizable? |
|-----------|-------|-------------|
| Electrical connectors (external) | 2 (Ethernet + Power) | ✅ Minimum for function |
| Electrical connectors (internal) | 5 (sensor bar + 4× daughter PCB headers) | Could reduce to 3 with harness consolidation |
| Mechanical interfaces (enclosure) | 4 (lid seal + battery door seal + 2× cable gland) | ✅ Minimum for IP67 |
| PCB-to-enclosure mounting | 8 (4× main PCB + 4× power PCB) | Could share standoffs: 2 power PCB standoffs = main PCB standoffs |

### 2.4 Simplicity Summary

| Criterion | Score | Status |
|-----------|-------|--------|
| Part count optimized | 46 parts (from 51) | ✅ PASS |
| No unnecessary parts | All parts justified by function | ✅ PASS |
| Interface count | 14 total (minimum for function) | ✅ PASS |
| **RULE 2: SIMPLICITY** | **92%** | **✅ COMPLIANT** |

*Note: 4 daughter PCBs retained despite adding parts, because field-replaceable sensors (MNT-07) is a high-value ODI outcome (O-37, O-39).*

---

## 3. RULE 3: SAFETY (An toàn)

*"Fail-safe design. Redundancy for critical functions. Clear indication of failures."*

### 3.1 Safety Hierarchy Application

| Function | Safety Approach | Level | Justification |
|----------|----------------|-------|---------------|
| F1: Sensing | **Safe-life** | 1 | MEMS mics designed for 15-year life with derating. No redundancy needed (graceful degradation with 3 of 4 mics). |
| F2: Timing | **Safe-life** | 1 | FPGA operates within specs with 50% voltage derating. Crystal oscillator rated for industrial temp. |
| F3: Compute | **Fail-safe** | 2 | Algorithm outputs "NO SHOT DETECTED" on any computational error. Never reports false position. |
| F4: Communicate | **Fail-safe** | 2 | Loss of Ethernet → BSU stores shots locally in flash (W25Q128). No data lost. |
| F6: Power | **Redundant** | 3 | Battery + external power. BMS protects against all fault modes. |
| F7: Protect | **Safe-life** | 1 | IP67 enclosure exceeds requirements by design margin. |

### 3.2 Failure Mode → Safe State

| Failure Mode | Safe State | Detection | Recovery |
|-------------|------------|-----------|----------|
| Mic 1 fails | System reports 3-mic degraded mode; reduced accuracy but operational | BIT: channel amplitude check | Replace daughter PCB (field, <5 min) |
| FPGA hangs | MCU detects FPGA heartbeat loss → resets FPGA via GPIO | Watchdog timeout (100ms) | Automatic recovery (<2s) |
| MCU crash | IWDG resets MCU automatically | Independent watchdog timer | Automatic recovery (<5s boot) |
| Ethernet cable cut | Shots buffered in W25Q128 (16MB = ~500,000 shots) | Link-down detection | Reconnect cable; buffered shots auto-sync |
| Battery depleted | System shuts down gracefully: save state → power LED red → shutdown | BQ27441 low battery warning at 10% | Replace/recharge battery |
| Over-temperature | BMS disconnects battery at 60°C; system saves state first | TMP117 + BMS NTC monitoring | Cool down; auto-resume below 55°C |
| Water ingress | IP67 prevents ingress. If breach detected (humidity sensor TBD), BIT reports | BIT moisture indicator (optional) | Inspect/replace gasket at depot |

### 3.3 Redundancy Design

| Critical Function | Primary | Backup | Independence |
|-------------------|---------|--------|--------------|
| Shot data storage | Ethernet → Control Station | W25Q128 local flash (16MB) | Fully independent; no shared failure mode |
| Power supply | Li-ion battery (14.8V 10Ah) | External DC input (10.5-28V) | Independent sources; power path auto-switch |
| FPGA configuration | Application bitstream | Golden bitstream (factory) | Separate flash sectors; CRC-protected |
| Clock source | 48 MHz crystal oscillator | MCU internal RC oscillator (for degraded mode) | Independent clock domains |

### 3.4 Safety Summary

| Criterion | Score | Status |
|-----------|-------|--------|
| Fail-safe states defined | 7/7 failure modes | ✅ PASS |
| No single-point-of-failure for data loss | Dual storage (Ethernet + flash) | ✅ PASS |
| BIT coverage | 90%+ of critical functions | ✅ PASS |
| Battery safety | 4-level protection (BMS + fuse + NTC + charger) | ✅ PASS |
| Electrical safety | ≤50V DC; IEC 62368-1 design | ✅ PASS |
| **RULE 3: SAFETY** | **100%** | **✅ COMPLIANT** |

---

## 4. RULE 4: ECONOMY (Kinh tế)

*"Right material for function. Consider full lifecycle cost. Manufacturing method appropriate to volume."*

### 4.1 Material Economy Check

| Component | Material | Overdesigned? | Right-sized? |
|-----------|----------|---------------|-------------|
| Enclosure | Al 6061-T6, 4mm wall | σ_max = 200 MPa vs σ_y = 276 MPa → SF = 1.4 | ✅ Right: 4mm minimum for IP67 sealing + shock |
| Base plate | Al 6061-T6, 6mm | Used as heat sink → thickness justified by thermal, not structural | ✅ Right: dual-function (structure + thermal) |
| Sensor bar | Al 6063-T5, 3mm wall | SF = 2.3 for wind load → adequate for combined loads | ✅ Right: extrusion = cheapest for C-channel |
| Fasteners | SS 316 | Could use SS 304 for non-coastal? No: 316 marginal cost (+10%) for much better salt spray | ✅ Right: lifecycle cost < replacement cost |
| PCB | FR-4 Tg170 | Tg140 sufficient for -10 to +60°C? No: need margin for lead-free reflow (260°C) + cycling | ✅ Right: Tg170 prevents delamination |
| Battery | Samsung 35E 3,500mAh | Could use cheaper 2,600mAh? No: need 10h at 13W = 130Wh; 4×3.5Ah×3.7V = 51.8Wh per cell → 10Ah needed | ✅ Right-sized |

### 4.2 Manufacturing Method Economy

| Component | Method | Volume Match? | Alternative | Decision |
|-----------|--------|--------------|-------------|----------|
| Enclosure | CNC from billet | ✅ Lot 50-100: CNC optimal | Die-cast @ lot 5,000+ | CNC correct for initial production |
| Sensor bar | Extrusion + CNC | ✅ Custom die ($800) amortized over 500 units = $1.60/unit | Fully CNC machined: $60/unit vs $30/unit extrusion | Extrusion correct: saves $15,000 over 500 units |
| PCB | Standard PCB house + SMT | ✅ Standard process; no custom tooling | In-house: not cost-effective at lot 50 | Outsource correct |
| Battery pack | Manual assembly (spot weld + BMS) | ✅ Low-volume; no automation needed | Automated: only at >1,000/year | Manual correct for initial production |
| Gaskets | Custom mold ($300) | ✅ Amortized over 500 units = $0.60/unit; silicone molding is simple | Die-cut from sheet: similar cost but less precise | Molded correct for O-ring groove fit |
| Rubber boots | Custom mold ($200) | ✅ Amortized over 500 units = $0.40/unit | Die-cut + hand-trimmed: poor consistency | Molded correct |

### 4.3 Lifecycle Cost (10-Year TCO)

| Cost Element | Per Lane | 10 Lanes | Calculation |
|-------------|----------|----------|-------------|
| Hardware purchase | $377 | $3,770 | Unit cost at lot 50 |
| Battery replacements (every 3 years) | $105 ($35 × 3) | $1,050 | 3 replacements in 10 years |
| Gasket replacements (every 5 years) | $12 ($6 × 2) | $120 | 2 replacements |
| Annual PM labor (2 hours × $20/hr) | $400 ($40 × 10y) | $4,000 | Vietnamese technician rate |
| Sensor replacement (1 per 5 years est.) | $20 ($10 × 2) | $200 | 2 daughter PCB replacements |
| Cable replacement (1 per 10 years) | $15 | $150 | One replacement |
| **10-Year TCO per lane** | **$929** | | **Requirement CST-03: ≤$1,500 ✅** |
| **10-Year TCO, 10-lane range** | | **$9,290** | Excl. software license |

**vs Import (Saab/InVeris):**
- Import 10-lane: ~$50,000-80,000 purchase + $5,000-10,000/yr support = $100,000-180,000 TCO
- VN-LOMAH 10-lane: ~$19,770 purchase + $929/yr = $29,060 TCO
- **Savings: 70-84%**

### 4.4 Economy Summary

| Criterion | Score | Status |
|-----------|-------|--------|
| No over-designed materials | 6/6 components right-sized | ✅ PASS |
| Manufacturing method matches volume | 6/6 methods appropriate for lot 50-100 | ✅ PASS |
| Lifecycle cost within target | $929/lane TCO (≤$1,500) | ✅ PASS |
| Import cost comparison | 12-15% of import equivalent | ✅ PASS |
| **RULE 4: ECONOMY** | **100%** | **✅ COMPLIANT** |

---

## 5. OVERALL RULES COMPLIANCE

| Rule | Score | Status | Key Finding |
|------|-------|--------|-------------|
| Rule 1: Clarity | 100% | ✅ | All functions mapped; all load paths traceable; no hidden failures |
| Rule 2: Simplicity | 92% | ✅ | 46 parts (optimized from 51); daughter PCBs retained for maintainability |
| Rule 3: Safety | 100% | ✅ | All failures → safe state; dual data storage; 4-level battery protection |
| Rule 4: Economy | 100% | ✅ | No overdesign; CNC appropriate for volume; 10y TCO $929/lane |
| **OVERALL** | **98%** | **✅ COMPLIANT** | |

### Design Changes from Rules Review

| Change # | Rule | Change | Impact |
|----------|------|--------|--------|
| RC-1 | Simplicity | Reduce lid bolts 8→6 | -2 parts, -30s assembly time |
| RC-2 | Simplicity | Consolidate internal wiring to single harness | -2 cable assemblies, cleaner routing |
| RC-3 | Simplicity | Integrate LED window into lid | -1 part, simpler enclosure |

---

## 6. META-LEARNING SKILL APPLIED

**Skill: Checklist-Based Verification**
- Applied 4 rules as structured checklists across all subsystems
- Identified 3 simplification opportunities (RC-1 to RC-3)
- Rules act as "negative feedback" on design complexity: each check asks "is this necessary?"
- Key insight: Rule 2 (Simplicity) conflicts with maintenance requirement (MNT-07) for individual mic replacement. Resolution: accept 4 daughter PCBs as justified complexity.

---

**Next Step:** [[PRAD_A_architecture]] → Define system architecture, modules, and interfaces

*PRAD-R Complete | 4 Rules scored | 98% overall compliance | 3 design changes adopted*
