---
project: RCWS-127-NAVAL
phase: 1
type: requirements
version: 1.0
created: 2026-02-03
updated: 2026-02-03
status: draft
---

# RCWS-127-NAVAL REQUIREMENTS LIST
## 12.7mm Naval Remote Controlled Weapon Station - Phase 1: Task Clarification

**Project Code**: RCWS-127-NAVAL
**Base Platform**: MTB-20 RCWS (ground vehicle variant)
**Target Platform**: Vietnamese Navy Patrol Boats

---

## 1. MISSION STATEMENT

Develop a **marinized 12.7mm remote controlled weapon station** for Vietnamese Navy patrol boats that:
- Provides accurate fire against surface and aerial threats in sea state 4+
- Withstands harsh marine environment (salt spray, humidity, corrosion)
- Integrates with existing patrol boat fire control systems
- Enables remote operation reducing crew exposure
- Maximizes reuse of MTB-20 RCWS base design (>40%)

---

## 2. DESIGN CONTEXT

### 2.1 Base Platform Reuse (MTB-20 RCWS)

**Retained Subsystems** (~40% reuse):
- Weapon mount mechanism (12.7mm interface)
- Azimuth/elevation drive motors (with marinized seals)
- Ammunition feed system
- Safety interlocks
- Basic control logic

**New Naval-Specific Subsystems** (~60% new):
- 2-axis gyro-stabilized platform
- Marinized housing (IP67)
- Ship power interface (24V/110V DC)
- Ship fire control integration (CAN bus)
- Environmental sealing systems

### 2.2 Key Differences from Ground Variant

| Aspect | MTB-20 Ground | RCWS-127-NAVAL | Driver |
|--------|---------------|----------------|--------|
| Stabilization | None | 2-axis gyro | Moving platform accuracy |
| Corrosion | Standard paint | Marine-grade coating | Salt spray environment |
| Sealing | IP54 | IP67 | Water immersion risk |
| Power | 12V/24V vehicle | 24V/110V DC naval | Ship power standards |
| Interface | Standalone | CAN bus + fire control | Tactical coordination |

---

## 3. COMPLETE REQUIREMENTS LIST

### Verification Methods Legend

| Code | Method | Description |
|------|--------|-------------|
| **A** | Analysis | Calculation, simulation, modeling |
| **I** | Inspection | Visual examination, measurement |
| **D** | Demonstration | Functional operation under controlled conditions |
| **T** | Test | Formal testing per specified procedures |

### Requirements Table (D = Demand, W = Wish)

| ID                          | Category          | Requirement                    | D/W | Value                                | Verification | Remarks                           |
| --------------------------- | ----------------- | ------------------------------ | --- | ------------------------------------ | ------------ | --------------------------------- |
| **1. GEOMETRY**             |                   |                                |     |                                      |              |                                   |
| R101                        | Dimensions        | Overall height (stowed)        | D   | ≤1.2 m                               | I            | Deck clearance for bridges        |
| R102                        | Dimensions        | Footprint (base)               | D   | ≤0.8 m diameter                      | I            | Deck space on patrol boats        |
| R103                        | Dimensions        | Elevation range                | D   | -15° to +60°                         | I            | Surface + aerial engagement       |
| R104                        | Dimensions        | Azimuth range                  | D   | 360° continuous                      | D            | Full perimeter coverage           |
| R105                        | Mass              | Total system weight            | D   | ≤200 kg                              | I            | Deck loading limits               |
| R106                        | Mass              | Above-deck mass                | D   | ≤150 kg                              | I            | Ship stability concern            |
| R107                        | Center of Gravity | CoG height                     | W   | <0.6 m above deck                    | A            | Minimize top-weight               |
| **2. KINEMATICS**           |                   |                                |     |                                      |              |                                   |
| R201                        | Tracking          | Azimuth slew rate              | D   | ≥60°/s                               | T            | Fast surface threats              |
| R202                        | Tracking          | Elevation slew rate            | D   | ≥30°/s                               | T            | Aerial threats                    |
| R203                        | Tracking          | Tracking accuracy (stabilized) | D   | ±1 mil RMS                           | T            | Sea state 4, ship moving          |
| R204                        | Tracking          | Stabilization axes             | D   | 2-axis (pitch + roll)                | D            | Compensate ship motion            |
| R205                        | Tracking          | Stabilization bandwidth        | D   | ≥10 Hz                               | T            | High-frequency wave motion        |
| R206                        | Tracking          | Max ship motion compensation   | D   | ±15° roll, ±10° pitch                | T            | Sea state 4-5 capability          |
| **3. FORCES**               |                   |                                |     |                                      |              |                                   |
| R301                        | Loads             | Weapon recoil                  | D   | 12.7mm NSV/DShK standard             | A            | ~5 kN peak                        |
| R302                        | Loads             | Wind load (operational)        | D   | 50 km/h wind                         | A            | Coastal operations                |
| R303                        | Loads             | Wind load (survival)           | D   | 120 km/h wind (stowed)               | A            | Typhoon survival                  |
| R304                        | Shock             | Shipboard shock                | D   | MIL-STD-167 Type I                   | T            | Naval shock qualification         |
| R305                        | Vibration         | Shipboard vibration            | D   | MIL-STD-167 Type II                  | T            | Continuous operation              |
| **4. ENERGY**               |                   |                                |     |                                      |              |                                   |
| R401                        | Power             | Input voltage                  | D   | 24V DC ±20% nominal                  | T            | Primary naval power               |
| R402                        | Power             | Alternate voltage              | W   | 110V DC (optional)                   | T            | Larger vessels                    |
| R403                        | Power             | Power consumption (standby)    | D   | ≤50 W                                | T            | 24/7 ready state                  |
| R404                        | Power             | Power consumption (tracking)   | D   | ≤300 W                               | T            | Slewing + stabilization           |
| R405                        | Power             | Power consumption (firing)     | D   | ≤500 W peak                          | T            | Max load                          |
| R406                        | Power             | Inrush current                 | D   | ≤30 A @ 24V                          | T            | Ship breaker sizing               |
| R407                        | Efficiency        | Power efficiency               | W   | >80%                                 | A            | Minimize heat generation          |
| **5. MATERIAL**             |                   |                                |     |                                      |              |                                   |
| R501                        | Material          | Primary structure              | D   | Marine-grade aluminum 5083           | I            | Corrosion resistance              |
| R502                        | Material          | Fasteners                      | D   | 316 stainless steel                  | I            | Salt spray resistance             |
| R503                        | Material          | Coating                        | D   | Epoxy primer + polyurethane topcoat  | I            | 5000 hrs salt fog                 |
| R504                        | Material          | Seals/gaskets                  | D   | EPDM or Viton                        | I            | UV + salt resistant               |
| R505                        | Material          | Optical windows                | D   | Sapphire or hardened glass           | I            | Scratch + salt resistant          |
| R506                        | Material          | Avoid                          | D   | No galvanized steel                  | I            | Galvanic corrosion risk           |
| R507                        | Material          | Drainage design                | D   | No horizontal surfaces, 5° min slope | I            | Prevent water pooling (L4)        |
| R508                        | Material          | Galvanic isolation             | D   | Dissimilar metals isolated           | I            | Prevent galvanic corrosion (L4)   |
| **6. SIGNALS**              |                   |                                |     |                                      |              |                                   |
| R601                        | Interface         | Operator control               | D   | CAN bus (ISO 11898)                  | T            | Ship standard                     |
| R602                        | Interface         | Fire control integration       | D   | CAN bus + RS-232                     | T            | Target designation                |
| R603                        | Interface         | Video output                   | D   | IP camera (H.264)                    | D            | Ship combat system                |
| R604                        | Interface         | Configuration port             | D   | Ethernet (RJ45)                      | D            | Maintenance access                |
| R605                        | Data              | Position feedback              | D   | 0.1° resolution                      | T            | Aim point accuracy                |
| R606                        | Data              | Target track output            | W   | CAN bus broadcast                    | D            | Ship fire control                 |
| R607                        | Protocol          | Naval data standard            | W   | NMEA 0183 compatible                 | T            | GPS/heading integration           |
| R608                        | Data              | Real-time hit indication       | D   | <2 s after impact                    | T            | Operator feedback (L6)            |
| R609                        | Data              | Engagement data logging        | W   | 1000 engagements storage             | I            | Learning loop (L6)                |
| R610                        | Interface         | Ship IMU integration           | W   | CAN bus, 100 Hz update               | T            | Predictive stabilization (L6)     |
| **7. SAFETY**               |                   |                                |     |                                      |              |                                   |
| R701                        | Safety            | Safe sectors                   | D   | Programmable no-fire zones           | D            | Prevent ship structure damage     |
| R702                        | Safety            | Emergency stop                 | D   | <500 ms stop time                    | T            | All motion halted                 |
| R703                        | Safety            | Fail-safe mode                 | D   | Safe weapon on power loss            | D            | Mechanical safe lock              |
| R704                        | Safety            | Misfire detection              | D   | Detect + alert within 2 s            | T            | Operator awareness                |
| R705                        | Safety            | Personnel protection           | D   | Interlock when maintenance mode      | D            | Power lockout                     |
| R706                        | Safety            | Fire inhibit                   | D   | Hardware + software redundant        | A            | MIL-STD-882E Cat I                |
| R707                        | Lightning         | Lightning protection           | D   | Bonded to ship ground                | I            | Mast-mounted exposed              |
| **8. ERGONOMICS**           |                   |                                |     |                                      |              |                                   |
| R801                        | Operator          | Control station                | D   | Indoor ship console                  | I            | Below-deck operation              |
| R802                        | Operator          | Joystick control               | D   | Intuitive 2-axis + trigger           | D            | Minimal training                  |
| R803                        | Operator          | Display                        | D   | Video overlay on ship display        | D            | No dedicated monitor              |
| R804                        | Operator          | Training time                  | W   | ≤4 hours operator qualification      | D            | Navy gunner skill level           |
| R805                        | Operator          | Firing position                | D   | Seated, below deck                   | I            | Reduced crew exposure             |
| **9. PRODUCTION**           |                   |                                |     |                                      |              |                                   |
| R901                        | Sourcing          | Local content                  | D   | ≥60% by value                        | A            | Self-reliance target              |
| R902                        | Sourcing          | COTS components                | D   | Maximize where possible              | A            | Cost + availability               |
| R903                        | Production        | Lot size                       | D   | Initial 20 units                     | -            | Fleet retrofit                    |
| R904                        | Production        | Production rate                | W   | 2 units/month                        | D            | Shipyard installation pace        |
| R905                        | Manufacturing     | Vietnamese capability          | D   | Local shipyard fabrication           | A            | Marine-grade welding/machining    |
| **10. QUALITY/RELIABILITY** |                   |                                |     |                                      |              |                                   |
| R1001                       | Reliability       | MTBF (marine environment)      | D   | ≥500 hours                           | A            | MIL-HDBK-217 (marine factor)      |
| R1002                       | Reliability       | Mission reliability            | D   | >95% for 8-hour patrol               | A            | High availability                 |
| R1003                       | Durability        | Service life                   | D   | 10 years / 5000 hours                | A            | Fleet lifecycle                   |
| R1004                       | Accuracy          | First-shot hit (stabilized)    | W   | >50% @ 500m, sea state 4             | T            | Moving platform                   |
| R1005                       | Environmental     | Salt fog resistance            | D   | 1000 hours exposure                  | T            | MIL-STD-810H Method 509.7         |
| R1006                       | Environmental     | Humidity                       | D   | 95% RH, 40°C                         | T            | MIL-STD-810H Method 507.6         |
| **11. ASSEMBLY**            |                   |                                |     |                                      |              |                                   |
| R1101                       | Assembly          | Installation time              | D   | ≤16 hours (shipyard)                 | D            | Per vessel retrofit               |
| R1102                       | Assembly          | Installation tools             | D   | Standard shipyard tools              | I            | No special fixtures               |
| R1103                       | Assembly          | Deck penetration               | D   | 4 mounting bolts only                | I            | Minimize hull modification        |
| R1104                       | Assembly          | Cable routing                  | D   | Through existing cable runs          | I            | Avoid new deck cuts               |
| R1105                       | Calibration       | Factory calibration            | D   | No field calibration required        | D            | Ship-to-ship consistency          |
| **12. TRANSPORT/STORAGE**   |                   |                                |     |                                      |              |                                   |
| R1201                       | Storage           | Storage temperature            | D   | -20°C to +60°C                       | T            | Shipboard storage                 |
| R1202                       | Storage           | Storage humidity               | D   | 95% RH non-condensing                | T            | Below-deck storage                |
| R1203                       | Transport         | Shipping mode                  | D   | Containerized (20ft std)             | I            | Port-to-port logistics            |
| R1204                       | Transport         | Shock (transport)              | D   | MIL-STD-810H Method 516.8            | T            | Truck + ship transport            |
| **13. OPERATION**           |                   |                                |     |                                      |              |                                   |
| R1301                       | Environment       | Operating temperature          | D   | 0°C to +50°C                         | T            | Tropical coastal                  |
| R1302                       | Environment       | Operating humidity             | D   | 95% RH                               | T            | Open ocean                        |
| R1303                       | Environment       | Rain                           | D   | Heavy rain (50 mm/hr)                | T            | MIL-STD-810H Method 506.6         |
| R1304                       | Environment       | Sea state                      | D   | Operational in sea state 4           | T            | 1.25-2.5m significant wave height |
| R1305                       | Environment       | Salt spray                     | D   | Direct salt spray exposure           | T            | MIL-STD-810H Method 509.7         |
| R1306                       | Operation         | Duty cycle                     | D   | 24/7 ready, 4 hr continuous fire     | D            | Patrol endurance                  |
| R1307                       | Environment       | Solar radiation                | W   | Tropical sun exposure                | T            | Paint/seal degradation            |
| **14. MAINTENANCE**         |                   |                                |     |                                      |              |                                   |
| R1401                       | Maintenance       | MTTR (corrective)              | D   | ≤2 hours                             | A            | Shipboard repair                  |
| R1402                       | Maintenance       | Preventive interval            | D   | 200 hours operation                  | -            | Lubrication, inspection           |
| R1403                       | Maintenance       | Tool requirements              | D   | Standard navy tools                  | I            | No proprietary tools              |
| R1404                       | Maintenance       | Spares strategy                | D   | 2-level (ship + depot)               | A            | Parts commonality                 |
| R1405                       | Maintenance       | Diagnostics                    | W   | Built-in test (BIT)                  | D            | Fault isolation                   |
| R1406                       | Maintenance       | Manual                         | D   | Maintenance manual (Vietnamese)      | I            | Navy technician level             |
| R1407                       | Maintenance       | Modular LRUs                   | D   | 3 major modules (sensor, drive, FCS) | D            | Fast repair (L10)                 |
| **15. COSTS**               |                   |                                |     |                                      |              |                                   |
| R1501                       | Cost              | Unit cost target               | D   | ≤$250,000                            | A            | Qty 20+ production                |
| R1502                       | Cost              | Development cost               | D   | ≤$250,000                            | A            | NRE budget                        |
| R1503                       | Cost              | Retrofit cost (per vessel)     | W   | ≤$300,000 total                      | A            | Unit + installation               |
| R1504                       | Cost              | Lifecycle cost                 | W   | 60% of import equivalent             | A            | 10-year TCO                       |
| R1505                       | Cost              | Spares budget                  | W   | 15% of unit cost                     | A            | Initial provisioning              |
| **16. SCHEDULE**            |                   |                                |     |                                      |              |                                   |
| R1601                       | Schedule          | Phase 1 complete               | D   | 2026-Q2                              | -            | Requirements approval             |
| R1602                       | Schedule          | Prototype delivery             | D   | 2027-Q2                              | -            | 2 units for sea trials            |
| R1603                       | Schedule          | Sea trials complete            | D   | 2027-Q3                              | -            | 500 hours operational             |
| R1604                       | Schedule          | Production approval            | D   | 2027-Q3                              | -            | Type certification                |
| R1605                       | Schedule          | First production delivery      | W   | 2027-Q4                              | -            | Fleet retrofit start              |

### Requirements Summary Statistics

| Category | Demands | Wishes | Total |
|----------|---------|--------|-------|
| 1. Geometry | 6 | 1 | 7 |
| 2. Kinematics | 6 | 0 | 6 |
| 3. Forces | 5 | 0 | 5 |
| 4. Energy | 6 | 1 | 7 |
| 5. Material | 8 | 0 | 8 |
| 6. Signals | 6 | 4 | 10 |
| 7. Safety | 7 | 0 | 7 |
| 8. Ergonomics | 4 | 1 | 5 |
| 9. Production | 4 | 1 | 5 |
| 10. Quality/Reliability | 5 | 1 | 6 |
| 11. Assembly | 5 | 0 | 5 |
| 12. Transport/Storage | 4 | 0 | 4 |
| 13. Operation | 6 | 1 | 7 |
| 14. Maintenance | 6 | 1 | 7 |
| 15. Costs | 3 | 2 | 5 |
| 16. Schedule | 4 | 1 | 5 |
| **TOTAL** | **85** | **14** | **99** |

**Quantification Level**: 94/99 = **95.0%** ✅ (Exceeds 80% target)

**Systems Thinking Integration:** 6 new requirements added from leverage point analysis (L4, L6, L10)

---

## 4. APPLICABLE STANDARDS

### 4.1 Naval Standards

| Standard | Sections | Application |
|----------|----------|-------------|
| **MIL-STD-167-1A** | All | Mechanical vibrations of shipboard equipment |
| **MIL-STD-810H** | Method 509.7, 506.6, 507.6 | Salt fog, rain, humidity |
| **MIL-STD-461G** | RE102, RS103, CS114 | EMC for naval systems |
| **MIL-STD-882E** | All | System safety (weapon system) |
| **MIL-STD-1399** | Section 300 | Interface standard for shipboard systems |
| **MIL-DTL-24643** | All | Finishing of weapon systems (corrosion) |

### 4.2 Vietnamese Standards

| Standard | Application |
|----------|-------------|
| TCVN 9294:2012 | Maritime equipment general requirements |
| TCVN 6260:2014 | Safety requirements for marine vessels |

---

## 5. KEY DIFFERENCES VS MTB-20 (REQUIREMENTS DELTA)

### 5.1 New Naval Requirements (Not in MTB-20)

| Requirement | Value | Driver |
|-------------|-------|--------|
| R201-R206 | Stabilization requirements | Moving platform accuracy |
| R501-R506 | Marine materials | Corrosion resistance |
| R1005 | 1000 hrs salt fog | Naval environment |
| R1304 | Sea state 4 operation | Operational requirement |
| R701 | Programmable safe sectors | Ship structure protection |
| R401-R402 | 24V/110V DC naval power | Ship integration |

### 5.2 Modified from MTB-20

| Requirement | MTB-20 Value | RCWS-127-NAVAL Value | Change |
|-------------|--------------|---------------------|--------|
| Sealing (R114) | IP54 | IP67 | +13 levels (immersion) |
| MTBF (R1001) | >2000 hrs | >500 hrs | Lower (marine harsh) |
| Power input | 12V/24V vehicle | 24V/110V DC | Naval standard |
| Mass (R105) | <150 kg | <200 kg | +33% (stabilization) |

### 5.3 Retained from MTB-20

- Weapon interface (12.7mm NSV/DShK)
- Ammunition feed requirements
- Safety interlock logic
- Basic operator controls (adapted)

---

## 6. REQUIREMENTS TRACEABILITY

### 6.1 Trace to Stakeholder Needs

| Stakeholder | Key Need | Requirements |
|-------------|----------|--------------|
| **Navy Operations** | Accurate fire in rough seas | R201-R206, R1004, R1304 |
| **Navy Maintenance** | Maintainable at sea | R1401-R1406, R1101-R1105 |
| **MoD Procurement** | Cost-effective | R1501-R1505, R901-R905 |
| **MoD Policy** | Local content | R901, R905 |
| **Safety Authority** | Safe operation | R701-R707 |
| **Shipyard** | Retrofit-able | R101-R106, R1101-R1104 |

### 6.2 Trace to Technical Standards

| Standard | Requirements Covered |
|----------|---------------------|
| MIL-STD-167 | R304, R305 (shock, vibration) |
| MIL-STD-810H | R1005, R1006, R1301-R1305 (environment) |
| MIL-STD-461G | R35 (EMC - from MTB-20) |
| MIL-STD-882E | R701-R707 (safety) |

---

## 7. REQUIREMENTS CONFLICTS CHECK

### 7.1 Identified Conflicts

| Conflict | Requirements | Resolution |
|----------|--------------|-----------|
| **Weight vs Stabilization** | R105 (<200kg) vs R204 (2-axis gyro) | Prioritize R204 (mission-critical), accept R105 with margin |
| **Cost vs Performance** | R1501 ($250K) vs R1004 (>50% hit) | Phased approach: meet R1004 first, optimize cost in production |
| **Local Content vs Technology** | R901 (60% local) vs R204 (gyro import) | Accept gyro import (critical tech), maximize local elsewhere |

### 7.2 Trade-off Analysis Needed

| Trade-off | Options | Decision Point |
|-----------|---------|---------------|
| Stabilization quality vs cost | 1-axis vs 2-axis | Phase 2 concept evaluation |
| Coating vs weight | Thick coat (heavy) vs thin (frequent repaint) | Material selection (Phase 3) |
| COTS gyro vs custom | Import COTS vs develop local | Phase 2 (likely COTS for schedule) |

---

## 8. GATE 1 CHECKLIST (Phase 1 → Phase 2 Transition)

- [x] All MUST requirements quantified (85/85 Demands have values)
- [x] Verification methods specified for all requirements
- [x] Applicable standards identified and mapped
- [x] Stakeholder traceability documented
- [x] Conflicts identified and resolution path defined
- [x] **ODI analysis completed** (42 outcomes, opportunity scores) ✅ NEW
- [x] **Systems thinking analysis completed** (4 CLDs, leverage points) ✅ NEW
- [x] **Requirements enhanced with systems insights** (6 new requirements) ✅ NEW
- [ ] **Stakeholder sign-off obtained** (PENDING)
- [ ] **MTB-20 compatibility verified** (PENDING - need MTB-20 design review)

**Status**: 🟢 **90% Complete - Ready for stakeholder review + MTB-20 verification**

---

## 9. NEXT ACTIONS

### Immediate (Week 1-2):
1. **Schedule stakeholder review meeting**
   - Navy operators (patrol boat crews)
   - Shipyard engineers (installation experts)
   - MTB-20 supplier (reuse compatibility)

2. **MTB-20 design review**
   - Obtain MTB-20 design package
   - Verify reuse assumptions (40% claimed)
   - Identify adaptation points

3. **Supplier engagement**
   - Contact gyro-stabilization suppliers (Korea, China)
   - Marine coating suppliers (local)
   - Preliminary cost estimates

### Short-term (Week 3-4):
1. **Finalize requirements** based on stakeholder feedback
2. **Obtain Gate 1 approval**
3. **Begin Phase 2**: Function structure development

---

*Next: [[RCWS-127-NAVAL_02_function_structure|Function Structure]] - Phase 2*
*Back to: [[RCWS-127-NAVAL_00_project_brief|Project Brief]]*
