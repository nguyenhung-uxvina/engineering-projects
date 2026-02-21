---
project: VN-MGM-001A
designation: Naval HMG Mount 12.7mm
type: requirements
phase: 1
version: 2.0
created: 2026-01-31
updated: 2026-02-05
status: approved
---

# VN-MGM-001A REQUIREMENTS SPECIFICATION
## 12.7mm Naval Heavy Machine Gun Mount
## Giá Súng máy Nặng 12.7mm Hải quân

**Phase:** 1 - Task Clarification (Pahl & Beitz)
**Version:** 2.0 (Revised and expanded)

---

# EXECUTIVE SUMMARY

## Product Identity

| Field | Value |
|-------|-------|
| **Product Code** | VN-MGM-001A |
| **Name (EN)** | Naval Heavy Machine Gun Mount 12.7mm |
| **Name (VI)** | Giá Súng máy Nặng 12.7mm Hải quân |
| **Target Price** | $6,500 |
| **R&D Investment** | $45,000 |
| **Development Time** | 6 months |
| **Current Phase** | Phase 3 Complete (Embodiment Design) |

## Compatible Weapons

| Weapon | Caliber | Origin | Weight | ROF | Recoil | Priority |
|--------|---------|--------|--------|-----|--------|----------|
| **DShK** | 12.7×108mm | Russia | 34 kg | 600 rpm | 32 kN | Primary |
| **NSV** | 12.7×108mm | Russia | 25 kg | 700 rpm | 28 kN | Primary |
| **Type 54** | 12.7×108mm | China | 38 kg | 600 rpm | 32 kN | Primary |
| **KPVT** | 14.5×114mm | Russia | 52 kg | 600 rpm | 55 kN | Secondary* |

*KPVT requires adapter and reinforced recoil system

## ODI Opportunity Analysis

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    ODI OPPORTUNITY SCORES                                     ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  OUTCOME                                              IMP   SAT   OPP SCORE  ║
║  ─────────────────────────────────────────────────   ───   ───   ─────────  ║
║  Maximize stability during firing                    9.5   3.0   16.0 🔴    ║
║  Maximize confidence in weapon readiness             9.5   3.0   16.0 🔴    ║
║  Minimize tracking lag vs target motion              9.0   2.0   16.0 🔴    ║
║  Minimize likelihood of alignment loss               8.5   2.0   15.0 🔴    ║
║  Minimize time to mount weapon                       9.0   3.5   14.5 ⚠️    ║
║  Minimize effort to traverse weapon                  8.5   2.5   14.5 ⚠️    ║
║  Maximize hit probability at max range               9.0   3.5   14.5 ⚠️    ║
║  Minimize time to reload ammunition                  8.5   3.0   14.0 ⚠️    ║
║  Minimize operator fatigue                           8.0   2.5   13.5 ⚠️    ║
║                                                                               ║
║  🔴 HIGH Priority (≥15): Core design focus                                   ║
║  ⚠️ SIGNIFICANT (13-15): Include in solution                                 ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

# PART 1: REQUIREMENTS LIST (16 CATEGORIES)

## Category 1: GEOMETRY (Hình học)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| G-01 | D | Base footprint | Ø450mm max | Dimensional check |
| G-02 | D | Height (stowed) | ≤500mm from deck | Dimensional check |
| G-03 | D | Height (operational) | ≤1200mm to grip | Ergonomic test |
| G-04 | D | Mounting bolt pattern | 8× M16 on Ø400mm PCD | Fit test |
| G-05 | W | Deck penetration | None required | Installation review |
| G-06 | W | Clearance envelope | Ø1500mm traverse | Layout check |

## Category 2: KINEMATICS (Động học)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| K-01 | D | Traverse range | ±180° continuous (360°) | Rotation test |
| K-02 | D | Elevation range | -15° to +85° | Limit test |
| K-03 | D | Traverse rate (manual) | ≥30°/sec achievable | Timing test |
| K-04 | D | Elevation rate (manual) | ≥20°/sec achievable | Timing test |
| K-05 | D | Traverse lock | Positive engagement | Function test |
| K-06 | D | Elevation lock | Friction brake, adjustable | Function test |
| K-07 | W | Traverse smoothness | No stick-slip | Operator evaluation |
| K-08 | W | Elevation balance | Neutral at 0° | Balance test |

## Category 3: FORCES (Lực)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| F-01 | D | Recoil force capacity | 50 kN peak | Static load test |
| F-02 | D | Cyclic recoil | 600 rpm sustained | Fatigue test 10,000 cycles |
| F-03 | D | Traverse effort | <5 kg·m (49 N·m) | Force gauge |
| F-04 | D | Elevation effort | <3 kg·m (29 N·m) | Force gauge |
| F-05 | D | Base mounting load | 75 kN static, 100 kN dynamic | FEA + test |
| F-06 | W | Recoil absorption | ≥40% energy absorbed | Instrumented test |
| F-07 | W | Residual vibration | <2G at grips after shot | Accelerometer |

## Category 4: ENERGY (Năng lượng)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| E-01 | D | Power source | Manual only (no electrical) | Design review |
| E-02 | D | Operator input | Human muscle power only | Ergonomic review |
| E-03 | W | Recoil energy dissipation | Via elastomer/spring | Design review |
| E-04 | W | Heat dissipation | No heat buildup at grips | Thermal test |

## Category 5: MATERIAL (Vật liệu)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| M-01 | D | Base ring material | 316 Stainless Steel | Material cert |
| M-02 | D | Pedestal material | 5083-H116 Aluminum | Material cert |
| M-03 | D | Cradle material | 6061-T6 Aluminum | Material cert |
| M-04 | D | Bearing material | C93200 Bronze + PTFE | Material cert |
| M-05 | D | Trunnion material | 4140 Steel, 50-55 HRC | Hardness test |
| M-06 | D | Fasteners | A4-80 Stainless (ISO 3506) | Material cert |
| M-07 | D | Elastomer | Polyurethane 90A Shore | Material cert |
| M-08 | W | Local sourcing | 65%+ by value from Vietnam | BOM analysis |

## Category 6: SIGNALS (Tín hiệu)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| S-01 | D | Traverse position | Visual scale, 10° increments | Inspection |
| S-02 | D | Elevation position | Visual scale, 5° increments | Inspection |
| S-03 | D | Lock status | Tactile feedback | Operator test |
| S-04 | W | Sight mounting | Picatinny rail, MIL-STD-1913 | Fit test |
| S-05 | W | Night sight ready | Rail position for NVG | Layout check |

## Category 7: SAFETY (An toàn)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| SF-01 | D | Weapon retention | Positive lock, no accidental release | Drop test 1.5m |
| SF-02 | D | Elevation hard stops | Mechanical limits at -15°/+85° | Function test |
| SF-03 | D | Pinch point elimination | No exposed mechanisms | Design review |
| SF-04 | D | Sharp edge control | All edges <0.5mm radius | Inspection |
| SF-05 | D | Stability (unmounted) | No tip-over at 15° deck angle | Tilt test |
| SF-06 | W | Hot surface protection | Insulated grips | Thermal test |
| SF-07 | W | Emergency release | Weapon removable in <60 sec | Timed test |

## Category 8: ERGONOMICS (Công thái học)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| ER-01 | D | Operator height range | 1.55m - 1.85m (5th-95th %ile VN) | Mockup test |
| ER-02 | D | Grip diameter | 30-40mm | Dimensional check |
| ER-03 | D | Grip angle | Adjustable ±15° | Function test |
| ER-04 | D | Sustained operation | 30 min without undue fatigue | User trial |
| ER-05 | W | Gloved operation | Compatible with tactical gloves | User trial |
| ER-06 | W | Ambidextrous controls | Symmetric layout | Design review |
| ER-07 | W | Shoulder rest | Optional attachment point | Fit test |

## Category 9: PRODUCTION (Sản xuất)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| P-01 | D | Manufacturing processes | CNC machining, welding, coating | Process review |
| P-02 | D | Special tooling | None required for assembly | Assembly trial |
| P-03 | D | Production rate target | 10 units/month achievable | Capacity study |
| P-04 | W | Local manufacturing | 90%+ processes in Vietnam | Supplier audit |
| P-05 | W | Batch size flexibility | Economic at 5-50 units | Cost analysis |

## Category 10: QUALITY CONTROL (Kiểm soát chất lượng)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| Q-01 | D | Critical dimensions | Cpk ≥1.33 | SPC data |
| Q-02 | D | Function test | 100% units tested | Test records |
| Q-03 | D | Material traceability | Full lot traceability | Documentation |
| Q-04 | W | Defect rate | ≤2% at final assembly | Quality records |
| Q-05 | W | First-pass yield | ≥95% | Production data |

## Category 11: ASSEMBLY (Lắp ráp)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| A-01 | D | Assembly time (factory) | ≤4 hours | Time study |
| A-02 | D | Field installation | ≤15 min with 2 persons | Timed trial |
| A-03 | D | Tools required | Standard metric hand tools | Tool list |
| A-04 | D | Alignment requirement | Self-aligning design | Assembly trial |
| A-05 | W | Modular subassemblies | 6 main assemblies | Design review |
| A-06 | W | Error-proofing | Keyed connections where possible | Design review |

## Category 12: TRANSPORT (Vận chuyển)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| T-01 | D | Shipping weight | ≤80 kg (with crate) | Weighing |
| T-02 | D | Shipping dimensions | ≤600×600×600mm | Dimensional check |
| T-03 | D | Handling | 2-person lift, no equipment | Handling trial |
| T-04 | W | Forklift compatible | Pallet base option | Design review |
| T-05 | W | Stackable | 3-high in storage | Stack test |

## Category 13: OPERATION (Vận hành)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| O-01 | D | Weapon mounting time | <5 min from storage | Timed trial |
| O-02 | D | Ammunition loading | 200-round belt supported | Function test |
| O-03 | D | Continuous firing | 200 rounds without adjustment | Firing trial |
| O-04 | D | Operating temperature | -10°C to +55°C | Environmental test |
| O-05 | D | Operating humidity | 0-100% RH | Environmental test |
| O-06 | W | Night operation | No light emission | Inspection |
| O-07 | W | Silent operation | No rattles or squeaks | Operator eval |

## Category 14: MAINTENANCE (Bảo trì)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| MT-01 | D | Lubrication interval | ≥1000 rounds or 1 month | Field trial |
| MT-02 | D | Lubrication type | Marine grease, single type | Specification |
| MT-03 | D | Bearing access | Without major disassembly | Maintenance trial |
| MT-04 | D | Replacement parts | Bearings, elastomers, fasteners | Parts list |
| MT-05 | W | MTBF | ≥10,000 rounds | Reliability test |
| MT-06 | W | MTTR | ≤30 min for routine service | Maintenance trial |
| MT-07 | W | Tool-free inspection | Daily checks without tools | Procedure review |

## Category 15: ENVIRONMENT (Môi trường)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| EN-01 | D | Salt fog resistance | 1000 hours per MIL-STD-810H | Chamber test |
| EN-02 | D | UV resistance | 5 years outdoor exposure | Accelerated test |
| EN-03 | D | Temperature cycling | -10°C to +55°C, 100 cycles | Chamber test |
| EN-04 | D | Humidity resistance | 95% RH, 40°C, 30 days | Chamber test |
| EN-05 | D | Vibration | 3G, 10-500 Hz, 3 axes | Shaker test |
| EN-06 | D | Shock | 40G, 11ms half-sine | Shock test |
| EN-07 | W | IP rating | IP65 for bearings/pivots | IP test |
| EN-08 | W | Fungus resistance | Non-nutrient materials | Material review |

## Category 16: COST (Chi phí)

| ID | Type | Requirement | Specification | Verification |
|----|------|-------------|---------------|--------------|
| C-01 | D | Unit manufacturing cost | ≤$4,400 | Cost analysis |
| C-02 | D | Target selling price | ≤$6,500 | Pricing review |
| C-03 | D | vs Import alternative | ≤50% of Russian equivalent | Market comparison |
| C-04 | W | Lifecycle cost | ≤$1,000/year maintenance | TCO analysis |
| C-05 | W | Spare parts cost | ≤$400/year average | Parts analysis |

---

# PART 2: ENVIRONMENT ANALYSIS

## 2.1 Operating Environments

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    OPERATING ENVIRONMENT MATRIX                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ENV 1: PATROL BOAT (Tàu tuần tra) - 240 mount positions                    ║
║  ═══════════════════════════════════════════════════════                     ║
║  Platform:     300-1000 ton vessels, fore/aft positions                      ║
║  Motion:       Roll ±15°, Pitch ±10°, Yaw ±5°                               ║
║  Vibration:    3-5 G peak during high speed                                  ║
║  Salt spray:   Continuous during operation                                   ║
║  Temperature:  25-45°C (deck up to 60°C)                                    ║
║  Humidity:     75-95% RH                                                     ║
║  Crew:         Trained naval personnel                                       ║
║                                                                               ║
║  ENV 2: COAST GUARD (Cảnh sát biển) - 130 mount positions                   ║
║  ═══════════════════════════════════════════════════════                     ║
║  Platform:     100-500 ton vessels                                           ║
║  Motion:       Roll ±18°, Pitch ±12°                                        ║
║  Patrol:       Extended duration (weeks)                                     ║
║  Maintenance:  Limited at sea                                                ║
║  Crew:         Mixed training levels                                         ║
║                                                                               ║
║  ENV 3: DK1 OFFSHORE PLATFORM (Nhà giàn) - 84 mount positions               ║
║  ═══════════════════════════════════════════════════════                     ║
║  Platform:     Fixed steel structure                                         ║
║  Motion:       None (static)                                                 ║
║  Salt:         EXTREME (elevated, constant spray)                            ║
║  Humidity:     85-98% RH (worst case)                                       ║
║  Wind:         Up to 150 km/h storms                                         ║
║  Resupply:     Quarterly only                                                ║
║  Requirement:  6-month autonomous operation                                  ║
║                                                                               ║
║  ENV 4: FISHING MILITIA (Dân quân biển) - 300+ mount positions              ║
║  ═══════════════════════════════════════════════════════                     ║
║  Platform:     Fishing vessels, 50-200 tons                                  ║
║  Motion:       Roll ±20° (smaller, less stable)                             ║
║  Maintenance:  Minimal expertise                                             ║
║  Storage:      Limited protected space                                       ║
║  Power:        No ship power (manual only)                                   ║
║  Training:     Basic only                                                    ║
║                                                                               ║
║  DESIGN DRIVER: DK1 PLATFORM (Most severe environment)                       ║
║  ══════════════════════════════════════════════════════                      ║
║  If it survives DK1 for 10 years, it survives anywhere.                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

## 2.2 Environmental Severity Comparison

| Factor | Patrol Boat | Coast Guard | DK1 Platform | Militia |
|--------|-------------|-------------|--------------|---------|
| Salt exposure | HIGH | HIGH | EXTREME | HIGH |
| Platform motion | MEDIUM | MEDIUM | NONE | HIGH |
| Maintenance access | GOOD | FAIR | POOR | POOR |
| Operator training | GOOD | FAIR | GOOD | BASIC |
| Power availability | YES | YES | YES | NO |
| Resupply frequency | Weekly | Biweekly | Quarterly | Variable |
| **Design criticality** | 2 | 3 | 1 (worst) | 4 |

---

# PART 3: WEAPON INTERFACE SPECIFICATIONS

## 3.1 DShK Interface (Primary)

```
DShK 12.7mm RECEIVER INTERFACE
═══════════════════════════════════════════════════════════════════

                    ┌────────────────────────────────────┐
                    │          DShK RECEIVER             │
                    │                                    │
              ●━━━━━┼━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┼━━━━━●
              ↑     │                                    │     ↑
           Trunnion │        Weapon body                 │  Trunnion
           Ø12mm    │        (34 kg)                     │  Ø12mm
              │     │                                    │     │
              │     └────────────────────────────────────┘     │
              │                                                │
              └──────────────────────────────────────────────┘
                              120mm spacing

Key Dimensions:
• Trunnion pin diameter: 12mm
• Trunnion spacing: 120mm (center to center)
• Receiver width: 140mm max
• Receiver height: 100mm
• Weight: 34 kg (weapon only), 55 kg (with barrel + feed)
```

## 3.2 NSV Interface

```
NSV 12.7mm RECEIVER INTERFACE
═══════════════════════════════════════════════════════════════════

                    ┌────────────────────────────────────┐
                    │          NSV RECEIVER              │
                    │                                    │
              ●━━━━━┼━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┼━━━━━●
              ↑     │                                    │     ↑
           Trunnion │        Weapon body                 │  Trunnion
           Ø10mm    │        (25 kg)                     │  Ø10mm
              │     │                                    │     │
              │     └────────────────────────────────────┘     │
              │                                                │
              └──────────────────────────────────────────────┘
                              115mm spacing

Key Dimensions:
• Trunnion pin diameter: 10mm
• Trunnion spacing: 115mm (center to center)
• Receiver width: 130mm max
• Weight: 25 kg (weapon only)

ADAPTER REQUIRED: Bushing Ø12→Ø10mm for DShK cradle
```

## 3.3 Recoil Force Analysis

| Weapon | Bullet | Velocity | Impulse | Peak Force | Duration |
|--------|--------|----------|---------|------------|----------|
| DShK | 48g | 820 m/s | 63 N·s | 32 kN | 2 ms |
| NSV | 48g | 845 m/s | 65 N·s | 28 kN | 2.3 ms |
| Type 54 | 48g | 820 m/s | 63 N·s | 32 kN | 2 ms |
| **Design** | - | - | - | **50 kN** | - |

Design force = 32 kN × 1.5 (safety factor) = **48 kN → 50 kN**

---

# PART 4: STAKEHOLDER ANALYSIS

## 4.1 Stakeholder Requirements Matrix

| Stakeholder | Primary Need | Requirements Impact | Priority |
|-------------|--------------|---------------------|----------|
| **Operators** | Easy aiming, low fatigue | K-03, K-04, ER-04 | HIGH |
| **Gunners** | Accurate fire, quick target acquisition | F-06, S-04 | HIGH |
| **Maintainers** | Easy service, common tools | MT-03, MT-06, A-03 | MEDIUM |
| **Logistics** | Standard spares, low cost | M-08, C-05, MT-04 | MEDIUM |
| **Training** | Simple operation | ER-01 through ER-06 | MEDIUM |
| **Command** | Reliability, readiness | MT-05, Q-01 | HIGH |
| **Procurement** | Cost, delivery, local content | C-01, C-02, P-04 | HIGH |
| **Safety** | No accidents | SF-01 through SF-07 | CRITICAL |

## 4.2 Conflicting Requirements Resolution

| Conflict | Requirement A | Requirement B | Resolution |
|----------|---------------|---------------|------------|
| Weight vs Strength | G-09 (≤75 kg) | F-01 (50 kN) | Use 5083 Al + optimize |
| Cost vs Corrosion | C-01 (≤$4,400) | EN-01 (1000 hrs) | 316 SS base, Al upper |
| Simplicity vs Features | A-03 (std tools) | S-04 (Picatinny) | Integrated rail |
| Speed vs Safety | O-01 (<5 min) | SF-01 (positive lock) | Quick-release with detent |

---

# PART 5: ABSTRACTION & ESSENTIAL PROBLEM

## 5.1 Problem Statement Evolution

```
Level 0 (Too Specific):
"Design a pedestal-type gun mount with slewing ring bearing for DShK"
↓ Too solution-biased

Level 1 (Solution Biased):
"Design a naval gun mount for 12.7mm machine gun"
↓ Still implies specific solution

Level 2 (Solution Neutral - TARGET):
"Enable accurate engagement of surface and low-air targets from
a moving naval platform, operable by personnel with minimal
training, without modification to existing platform structure,
surviving 10 years in extreme marine environment"
↓ Correct level

Level 3 (Too Abstract):
"Transfer kinetic energy to targets"
↓ Too vague for design
```

## 5.2 Essential Functions

| # | Function (EN) | Function (VI) | Critical? |
|---|---------------|---------------|-----------|
| F1 | ACCEPT weapon assembly | Tiếp nhận cụm vũ khí | Yes |
| F2 | SUPPORT static load | Đỡ tải tĩnh | Yes |
| F3 | ROTATE in azimuth | Xoay theo phương vị | Yes |
| F4 | ROTATE in elevation | Xoay theo góc tà | Yes |
| F5 | ABSORB recoil energy | Hấp thụ năng lượng giật | Yes |
| F6 | TRANSFER loads to platform | Truyền tải xuống nền tảng | Yes |
| F7 | INDICATE position | Chỉ thị vị trí | No |
| F8 | PROTECT from environment | Bảo vệ khỏi môi trường | Yes |
| F9 | ENABLE operator control | Cho phép điều khiển | Yes |

---

# PART 6: VERIFICATION MATRIX

## 6.1 Verification Methods

| Method | Code | Description | When Used |
|--------|------|-------------|-----------|
| Analysis | A | Engineering calculation/FEA | Design phase |
| Inspection | I | Visual/dimensional check | Production |
| Demonstration | D | Functional operation | Assembly |
| Test | T | Measured performance | Qualification |

## 6.2 Requirements Verification Matrix (Summary)

| Category | Total Req | Analysis | Inspection | Demo | Test |
|----------|-----------|----------|------------|------|------|
| Geometry | 6 | 2 | 4 | 0 | 0 |
| Kinematics | 8 | 1 | 0 | 2 | 5 |
| Forces | 7 | 3 | 0 | 0 | 4 |
| Energy | 4 | 2 | 0 | 0 | 2 |
| Material | 8 | 1 | 0 | 0 | 7 |
| Signals | 5 | 0 | 3 | 0 | 2 |
| Safety | 7 | 1 | 2 | 0 | 4 |
| Ergonomics | 7 | 0 | 2 | 2 | 3 |
| Production | 5 | 2 | 0 | 2 | 1 |
| Quality | 5 | 0 | 0 | 0 | 5 |
| Assembly | 6 | 0 | 0 | 3 | 3 |
| Transport | 5 | 0 | 2 | 2 | 1 |
| Operation | 7 | 0 | 1 | 1 | 5 |
| Maintenance | 7 | 1 | 0 | 2 | 4 |
| Environment | 8 | 1 | 0 | 0 | 7 |
| Cost | 5 | 5 | 0 | 0 | 0 |
| **TOTAL** | **100** | **19** | **14** | **14** | **53** |

---

# PART 7: COMPLIANCE MATRIX

## 7.1 Standards Compliance

| Standard | Title | Applicable Requirements |
|----------|-------|------------------------|
| MIL-STD-810H | Environmental Engineering | EN-01 through EN-08 |
| MIL-STD-1472H | Human Engineering | ER-01 through ER-07 |
| MIL-STD-1913 | Accessory Mounting Rail | S-04 |
| STANAG 4568 | Naval Gun Mount Interface | G-04 |
| ISO 3506 | Mechanical Properties of Fasteners | M-06 |
| TCVN 7699 | Vietnamese Safety Standards | SF-01 through SF-07 |

## 7.2 Local Content Requirement

| Component | Origin | % Value | Target |
|-----------|--------|---------|--------|
| Base ring (316 SS) | Import | 15% | - |
| Pedestal (5083 Al) | Hòa Phát | 12% | Local |
| Cradle (6061 Al) | Hòa Phát | 18% | Local |
| Machining | Local shops | 25% | Local |
| Bearings | Import | 8% | - |
| Fasteners | Import | 5% | - |
| Assembly/coating | Local | 17% | Local |
| **TOTAL LOCAL** | | **72%** | ≥65% ✓ |

---

# PART 8: COST BREAKDOWN

## 8.1 Target Cost Structure

| Category | Target | % of Total |
|----------|--------|------------|
| Raw materials | $1,620 | 37% |
| Direct labor | $1,200 | 27% |
| Machining (outsource) | $750 | 17% |
| Overhead | $830 | 19% |
| **Manufacturing cost** | **$4,400** | **100%** |
| Margin (30%) | $1,320 | - |
| **Selling price** | **$5,720** | - |
| Contingency | $780 | - |
| **Target price** | **$6,500** | - |

## 8.2 Cost Comparison

| Solution | Unit Price | 10-Year TCO | Source |
|----------|------------|-------------|--------|
| Russian NPU | $25,000 | $35,000 | Import quote |
| Chinese mount | $12,000 | $20,000 | Market data |
| Local fabrication | $4,000 | $15,000 | Poor quality |
| **VN-MGM-001A** | **$6,500** | **$12,000** | **Target** |

---

# APPENDICES

## Appendix A: Acronyms

| Acronym | Meaning |
|---------|---------|
| DShK | Degtyaryov-Shpagin Krupnokaliberny (12.7mm) |
| FEA | Finite Element Analysis |
| HMG | Heavy Machine Gun |
| HRC | Hardness Rockwell C |
| MTBF | Mean Time Between Failures |
| MTTR | Mean Time To Repair |
| NSV | Nikitin-Sokolov-Volkov (12.7mm) |
| ODI | Outcome-Driven Innovation |
| PCD | Pitch Circle Diameter |
| SPC | Statistical Process Control |
| TCO | Total Cost of Ownership |

## Appendix B: Reference Documents

| Document | Description |
|----------|-------------|
| VN_NAVAL_12.7mm_GUN_MOUNT_SYSTEM_Deep_Dive_Analysis.md | Parent system analysis |
| VN_MGM_001A_Gun_Mount_Assembly_Deep_Dive.md | Full deep-dive (Phase 1-3) |
| VN_MGM_Portfolio_Strategy.md | Product family strategy |
| VN_MGM_Bundled_Packages.md | Sales packages |

## Appendix C: Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-31 | Initial requirements (10D + 10W) |
| **2.0** | **2026-02-05** | **Expanded to 16 categories (100 requirements), added ODI scores, verification matrix, compliance matrix, cost breakdown** |

---

# DOCUMENT APPROVAL

## Gate 1 Review Checklist (Version 2.0)

| Criterion | V1.0 | V2.0 | Status |
|-----------|------|------|--------|
| Requirements categories | 2 | 16 | ✅ Complete |
| Total requirements | 20 | 100 | ✅ Expanded |
| Quantified (%) | 60% | 85% | ✅ Improved |
| Environment analysis | Basic | Comprehensive | ✅ Enhanced |
| Stakeholder analysis | None | Complete | ✅ Added |
| Verification matrix | None | Complete | ✅ Added |
| Cost breakdown | Basic | Detailed | ✅ Enhanced |
| Standards compliance | Partial | Complete | ✅ Enhanced |

## Approval Status

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Engineering | | | |
| Quality | | | |
| Production | | | |
| Program Manager | | | |

---

**Phase Status:** Phase 3 (Embodiment Design) COMPLETE
**Next Phase:** Phase 4 (Detail Design) - Ready to proceed

---

*This requirements specification supersedes all previous versions and serves as the baseline for VN-MGM-001A development.*
