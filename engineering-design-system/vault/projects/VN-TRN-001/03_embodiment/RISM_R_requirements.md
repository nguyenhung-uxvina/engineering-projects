---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: RISM-R
title: Requirements Identification
version: 1.0
created: 2026-02-06
status: complete
---

# STEP R: REQUIREMENTS IDENTIFICATION
## Embodiment-Determining Requirements Extraction
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 1 of 15

**Purpose:** Extract and organize all requirements from Phase 1 that directly constrain the physical embodiment of the BSU-V1 design.

**Input:** [[requirements_list]] (107 requirements across 16 categories)
**Output:** Embodiment Requirements Matrix organized by physical constraint type

---

## 1. FILTERING CRITERIA

Requirements are classified as **embodiment-determining** if they directly constrain:
- Physical dimensions, shape, or spatial arrangement
- Motion, velocity, or positioning of components
- Structural loads, shock, vibration, or pressure
- Material properties, surface finish, or coatings
- Electrical power, thermal management, or energy storage
- Environmental resistance (temperature, humidity, salt, dust)
- Human interaction (ergonomics, setup, maintenance access)
- Manufacturing method or production capability

Requirements that are **NOT embodiment-determining** (addressed in firmware/software or project management):
- Software UI features (SIG-09, SIG-10 display/export)
- Protocol implementations (SIG-06 FASIT)
- Schedule targets (SCH-01 to SCH-04)
- Training time (ERG-01) -- process, not hardware
- NRE amortization (CST-04) -- financial, not physical

---

## 2. EMBODIMENT REQUIREMENTS MATRIX

### 2.1 Geometric Constraints (Size, Shape, Envelope)

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| GEO-01 | BSU length | ≤1,300mm | D | Sensor bar max length; mic spacing ≤347mm pitch |
| GEO-02 | BSU height | ≤200mm | W(4) | Enclosure + sensor bar profile |
| GEO-03 | BSU width/depth | ≤150mm | W(3) | Enclosure cross-section |
| GEO-04 | BSU weight | ≤12kg (target 8kg) | D | Material selection driver; Al vs polymer vs steel |
| GEO-05 | TPU enclosure | ≤300×200×150mm | W(3) | Processing enclosure envelope |
| GEO-06 | TPU weight | ≤5kg | D | Enclosure + battery weight budget |
| GEO-07 | Detection zone - infantry | ≥3.0m(H) × 2.5m(W) | D | Sensor geometry + sensitivity; bar length + mic placement |
| GEO-08 | Detection zone - armor | ≥4.0m(H) × 3.0m(W) | W(4) | Extended sensitivity requirement |
| GEO-09 | Mounting compatibility | NATO + Vietnamese frames | D | Mounting bracket design; clamp system adaptability |

**Geometric Summary:**
- Max sensor bar: 1,300 × 200mm cross-section, ≤12kg total system
- Processing enclosure: 300 × 200 × 150mm, ≤5kg
- Detection zone constrains mic placement geometry (minimum baseline for TDOA resolution)
- Mounting must be universal (NATO + local frames)

---

### 2.2 Kinematic Constraints (Motion, Velocity, Timing)

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| KIN-01 | Min projectile velocity | ≤Mach 1.3 (440 m/s) | D | Sensor sensitivity + algorithm; N-wave amplitude floor |
| KIN-02 | Max projectile velocity | ≥Mach 3.5 (~1,190 m/s) | D | ADC speed + anti-aliasing filter bandwidth |
| KIN-03 | Detection azimuth | ≥±20° from perpendicular | D | Sensor bar geometry; non-coplanar arrangement |
| KIN-04 | Detection elevation | ≥±5° from perpendicular | D | Non-coplanar mic offset (z-axis); 3D solving |
| KIN-05 | Shot-to-display latency | ≤500ms (target 200ms) | W(4) | Processing pipeline: ADC→FPGA→MCU→Ethernet |

**Kinematic Summary:**
- Mach 1.3-3.5 velocity range → bandpass filter 1-100 kHz, ADC ≥500 kSPS
- ±20° azimuth + ±5° elevation → non-coplanar sensor array geometry required
- ≤500ms latency → deterministic processing chain (FPGA timing + MCU algorithm + Ethernet)

---

### 2.3 Force & Load Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| FRC-01 | Shockwave overpressure | ≥164 dB SPL without damage | D | Mic selection (max SPL rating); AGC circuit |
| FRC-02 | Ballistic impact survival | Indirect 5.56mm fragments at 300m | D | Enclosure wall thickness; material strength |
| FRC-03 | Mechanical shock (transport) | 40g, 11ms MIL-STD-810H 516.8 | D | PCB retention, battery strap, rubber isolators |
| FRC-04 | Vibration (transport) | MIL-STD-810H 514.8 Cat 4 | D | Natural frequency analysis; mounting isolation |
| FRC-05 | Wind load on BSU | Operational at 72 km/h (20 m/s) | W(4) | Aerodynamic profile; mounting clamp strength |
| FRC-06 | Drop height (packed) | 1.0m onto concrete | W(3) | Transport case design; internal foam |

**Force Summary:**
- 164 dB SPL → mic + front-end must handle extreme acoustic input
- 40g shock → all internal components secured; no unsupported PCB spans >80mm
- Cat 4 vibration → rubber isolator mounts; resonance >200 Hz
- 20 m/s wind → clamp system must resist ~15N lateral force on bar
- Fragment impact → 4mm aluminum wall minimum

---

### 2.4 Energy & Power Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| ENG-01 | Primary power input | 12 VDC (10.5-15V) | D | DC-DC converter input range; connector rating |
| ENG-02 | Mains power input | 110/230 VAC auto-switching | D | External AC-DC adapter; not built into BSU |
| ENG-03 | Battery runtime | ≥10 hours at 25°C | D | Battery capacity: ≥150Wh (at 15W); cell count |
| ENG-04 | Battery type | Li-ion, field-replaceable | D | Battery door access; BMS board; UN 38.3 cells |
| ENG-05 | System power consumption | ≤15W average per lane | D | Component selection power budget; thermal mgmt |
| ENG-06 | Solar charging input | 18-36 VDC compatible | W(4) | Charger IC input range; connector type |
| ENG-07 | Power-on to operational | ≤60s (target 30s) | W(4) | Boot sequence; FPGA configuration time |
| ENG-08 | Brownout/surge protection | Survive 50V, 100ms | D | TVS diode; input protection circuit |

**Energy Summary:**
- Battery: Li-ion 4S1P (14.8V), ≥10Ah for 10h at 15W; field-replaceable door
- Input range: 10.5-28V DC (12V vehicle + 24V military + 18-36V solar)
- Power budget: 15W max average → drives component power selection
- Surge protection: TVS + reverse polarity MOSFET on power input
- Boot: FPGA config <5s (iCE40 from SPI flash), MCU init <25s

---

### 2.5 Material & Surface Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| MAT-01 | BSU housing material | Al 6061-T6 or marine polymer | D | Enclosure material selection; machining method |
| MAT-02 | Fasteners | SS 316 or equivalent | D | All external fasteners; dissimilar metal isolation |
| MAT-03 | PCB conformal coating | IPC-CC-830C Class 3 | D | Coating material + process; rework access |
| MAT-04 | Sealing gaskets | EPDM or silicone, Vietnamese-sourced | D | Gasket groove design; compression ratio |
| MAT-05 | Cable assemblies | UV-resistant, oil-resistant | W(4) | PUR jacket selection; cable diameter |
| MAT-06 | RoHS compliance | RoHS 3 all materials | D | Lead-free solder; component screening |
| MAT-07 | Acoustic coupling | Vietnamese natural rubber | W(3) | Mic mount boot design; shore hardness |
| OPR-07 | IP rating | IP67 minimum | D | O-ring grooves; connector sealing; test method |

**Material Summary:**
- Enclosure: Al 6061-T6 (anodized Type III, 25μm min per MIL-A-8625F)
- Fasteners: SS 316 throughout; nylon washers at Al-SS interfaces
- Sealing: EPDM O-rings per AS568A; IP67 verified per IEC 60529
- Coating: Acrylic conformal (HumiSeal 1B31), IPC-CC-830C Class 3
- All RoHS 3 compliant; SAC305 lead-free solder

---

### 2.6 Environmental Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| OPR-01 | Operating temperature | -10°C to +60°C | D | Component grade (industrial min); thermal design |
| OPR-02 | Storage temperature | -40°C to +70°C | D | Material selection (no brittle fracture at -40°C) |
| OPR-03 | Humidity | 95% RH at 40°C | D | IP67 + conformal coating; no bare copper |
| OPR-04 | Rain operation | 100mm/hr | D | IP67 enclosure; drainage design |
| OPR-05 | Dust/sand | MIL-STD-810H 510.7 | D | IP67 sealing; no ventilation openings |
| OPR-06 | Salt fog | MIL-STD-810H 509.7, 48h | D | SS316 fasteners; hard anodize; no bare aluminum |
| OPR-08 | Calibration-free | Zero calibration shots | D | Non-coplanar sensor geometry; algorithm design |
| OPR-09 | Ammunition compatibility | 5.56, 7.62×39, 7.62×51, 12.7mm | D | Velocity range → sensor bandwidth + ADC speed |

**Environmental Summary:**
- Full tropical exposure: -10 to +60°C operating, 95% RH, monsoon rain, salt fog
- IP67 mandatory: sealed enclosure, no ventilation holes, immersion-proof connectors
- Calibration-free: non-coplanar mic array + time-only TDOA algorithm
- Multi-caliber: Mach 1.3 (5.56mm at 300m) to Mach 3.5 (12.7mm at muzzle)

---

### 2.7 Safety Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| SAF-01 | Electrical safety | IEC 62368-1 | D | Creepage distances; insulation; grounding |
| SAF-02 | No projectile deflection | BSU shall not redirect projectiles | D | Sensor bar profile; mounting below target |
| SAF-03 | Low-voltage field operation | ≤50V DC accessible | D | All voltages internal ≤50V; battery 14.8V max |
| SAF-04 | Battery safety | UN 38.3; BMS protection | D | BMS IC selection; fuse; cell protection |
| SAF-05 | EMC emissions | MIL-STD-461G RE102, CE102 | D | Aluminum Faraday cage; filtered connectors |
| SAF-06 | Fault indication | Audible/visual alarm | W(3) | LED window in enclosure; optional buzzer |

**Safety Summary:**
- All user-accessible voltages ≤50V DC (battery = 14.8V max)
- Battery: BMS with over-charge, over-discharge, short-circuit, over-temperature
- EMC: aluminum enclosure acts as Faraday cage; pi-filter on power input
- Sensor bar below target frame → no projectile deflection risk
- Status LEDs visible through enclosure window; BIT self-diagnostic

---

### 2.8 Ergonomics & Operational Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| ERG-02 | Display readability | 500 nits or anti-glare | D | Control station display (COTS); not BSU hardware |
| ERG-04 | Setup without special tools | Max 1 multi-tool | W(4) | Tool-less clamps; hand-tightened connectors |
| ERG-05 | Single-person setup | One person per lane | W(3) | All components <5kg individual |
| ERG-06 | Color-coded connectors | Unique per cable type | W(3) | Connector body color selection |
| ASM-01 | Field assembly time | ≤15 min per lane | D | 3-step setup: clamp → connect → power-on |
| ASM-02 | Connector type | Quick-connect mil-spec IP67 | D | Amphenol RJFTV or equivalent |
| ASM-03 | Sensor bar mounting | Tool-less quick-mount clamp | D | Cam-lever clamp design |
| ASM-04 | Cable count per lane | ≤3 cables | W(4) | 1× Ethernet + 1× power (optional) |
| ASM-05 | Modular LRU design | BSU, TPU, VDU separable | W(3) | Module boundaries; connector interfaces |

**Ergonomics Summary:**
- Tool-less sensor bar mounting (cam-lever clamps)
- All connectors IP67 quick-connect; color-coded (Blue=Ethernet, Green=Power)
- ≤15 min setup: clamp bar → connect cable → power on
- All components <5 kg individual for single-person handling
- Modular LRU: sensor bar, main PCB, battery independently replaceable

---

### 2.9 Production & Cost Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| PRD-01 | Local content by value | ≥60% (target 70%) | D | Material sourcing; machining location |
| PRD-02 | Initial production lot | 50 lane-sets | D | Design for batch 50-100 (no mass-prod tooling) |
| PRD-03 | Production capability | Vietnamese machining + PCB | D | 3-axis CNC max; 4-layer PCB; 0402 min SMT |
| PRD-04 | Dual-sourcing | ≥2 suppliers per critical part | D | Component selection with alternates |
| PRD-05 | PCB assembly | Local SMT (0402 min, TQFP max) | W(4) | No BGA; max QFN-48 (reflow-solderable) |
| CST-01 | Unit hardware cost | ≤$500/lane at lot 50 | D | BOM target; margin budget |
| CST-02 | 10-lane range system | ≤$25,000 complete | D | System-level cost target |
| CST-05 | Import content cost | ≤40% of unit cost | W(4) | Import component selection |

**Production Summary:**
- Vietnamese manufacturing: 3-axis CNC, 4-layer PCB, standard SMT (0402 min, QFN-48 max)
- No BGA packages → simplifies local assembly
- Lot size 50-100 → CNC machining (not tooling-intensive)
- ≤$500/lane → BOM budget ~$330 (15% margin)
- Local content ≥60% → maximize local mechanical, cables, assembly

---

### 2.10 Maintenance Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| QUA-01 | MTBF | ≥5,000h (target 8,000h) | D | Component derating; reliability analysis |
| QUA-02 | MTTR (field) | ≤30 min LRU replacement | D | Access design; LRU swap procedure |
| QUA-06 | Design life | ≥15 years | W(4) | Corrosion protection; component derating 50% |
| MNT-01 | PM interval | ≥500 operating hours | D | Sealed design; minimal wear items |
| MNT-02 | Built-In Test | Auto BIT at power-on | D | BIT circuits: voltage, temp, sensor, comm |
| MNT-03 | LRU replacement | Basic tools (Phillips + flat) | D | Screw access; no special tools |
| MNT-04 | Spare parts domestic | ≥80% within Vietnam | D | Sourcing strategy; local alternates |
| MNT-06 | No special test equipment | Standard multimeter only | W(3) | Test points accessible; BIT covers 90%+ |
| MNT-07 | Individual sensor replacement | Without full BSU disassembly | W(3) | Daughter PCB design; screw-mount sensors |

**Maintenance Summary:**
- MTTR ≤30 min → quick-release battery door; LRU access with Phillips screwdriver
- BIT: power, sensors (4ch), FPGA, MCU, Ethernet, temperature, battery
- Individual MEMS mic replacement via daughter PCB (screw-mount)
- 15-year design life → conservative derating (50% voltage, 75% current)
- ≥80% domestic spares → mechanical parts, cables, gaskets, battery all local

---

### 2.11 Transport Constraints

| Req ID | Requirement | Value | D/W | Impact on Embodiment |
|--------|-------------|-------|-----|----------------------|
| TRN-01 | Lane set packed weight | ≤25kg total | D | System weight budget allocation |
| TRN-02 | Transport case | IP67 ruggedized, stackable | D | Case internal dimensions; foam cutouts |
| TRN-03 | Vehicle transport | Fit 10 sets in truck bed | D | Case external dimensions; stacking |
| TRN-04 | Airline transport | UN 38.3 battery certified | W(4) | Battery removability; labeling |
| TRN-05 | Pack-up time | ≤10 min per lane | W(3) | Quick-disconnect design |

**Transport Summary:**
- Total packed: ≤25kg (BSU 7.8kg + cable 1.8kg + case 4kg + padding = ~15kg, within budget)
- Case: rotomolded PE, IP67, stackable, custom foam inserts
- 10 cases fit in standard military truck bed (~500×400×300mm per case)
- Battery removable for air transport

---

## 3. SUMMARY STATISTICS

| Category | Requirements Extracted | MUST | WISH | % of Total 107 |
|----------|----------------------|------|------|-----------------|
| Geometric | 9 | 5 | 4 | 8.4% |
| Kinematic | 5 | 4 | 1 | 4.7% |
| Force & Load | 6 | 4 | 2 | 5.6% |
| Energy & Power | 8 | 5 | 3 | 7.5% |
| Material & Surface | 8 | 6 | 2 | 7.5% |
| Environmental | 8 | 7 | 1 | 7.5% |
| Safety | 6 | 5 | 1 | 5.6% |
| Ergonomics & Operation | 9 | 4 | 5 | 8.4% |
| Production & Cost | 8 | 6 | 2 | 7.5% |
| Maintenance | 9 | 5 | 4 | 8.4% |
| Transport | 5 | 3 | 2 | 4.7% |
| **TOTAL EMBODIMENT** | **81** | **54** | **27** | **75.7%** |

**Non-embodiment requirements** (26): Software features, protocol specs, schedule, training, financial
These are addressed in firmware/software design and project management.

---

## 4. META-LEARNING SKILL APPLIED

**Skill: Categorization**
- Organized 107 flat requirements into 11 physical constraint categories
- Mental model: hierarchical organization by physical domain
- Benefit: Each category maps directly to a design decision area in subsequent RISM-PRAD steps

---

**Next Step:** [[RISM_I_critical_requirements]] → Prioritize by constraint strength, identify conflicts

*RISM-R Complete | 81 embodiment requirements extracted from 107 total | 54 MUST + 27 WISH*
