---
project: VN-RNG-001
phase: 0
type: reverse_engineering
version: 1.0
created: 2026-02-08
status: draft
subject: Polytronic International AG - LOMAH & Range Systems
---

# REVERSE ENGINEERING ANALYSIS: Polytronic International AG - LOMAH System

## 1. SYSTEM IDENTIFICATION

| Field | Value |
|-------|-------|
| **Designation** | Polytronic LOMAH (H-Bar, T-Bar, I-Bar) + AROS Range Control |
| **Origin** | Polytronic International AG, Muri, Aargau, Switzerland |
| **Founded** | 1966 by Claude Thalmann (ETH physicist) |
| **Subsidiary** | Polytronic Training Systems LLC, Abu Dhabi, UAE (est. 2016) |
| **Employees** | ~320+ (50+ Switzerland, 270+ UAE) |
| **Global Footprint** | 1,000+ ranges in 80+ countries |
| **Analysis Date** | 2026-02-08 |
| **Analysis Type** | OSINT - no physical specimen |
| **Confidence** | Medium-High |

> **Note:** The designation "ST-400" was not found in any Polytronic catalog. Polytronic uses the **"TG" (Target/Trefferanlage)** naming convention. This analysis covers their complete LOMAH and range system portfolio.

### Historical Significance

Polytronic **invented the world's first electronic scoring system** (1966) and filed the **first automatic marking system patent** (1969). They are the original LOMAH innovator.

### System Boundaries

| Boundary | Definition |
|----------|-----------|
| **System** | LOMAH acoustic/radar precision scoring |
| **Supersystem** | Polytronic Range System (targets + AROS + LOMAH + robotic targets) |
| **Sibling systems** | InVeris LOMAH, Saab LOMAH, Kongsberg eScore, SIUS Ascor |
| **Operational context** | Military ranges, sport shooting, law enforcement training |

---

## 2. EXTERNAL CHARACTERIZATION

### 2.1 Product Portfolio Overview

```
POLYTRONIC RANGE ECOSYSTEM
│
├── SCORING TECHNOLOGY (LOMAH)
│   ├── H-Bar LOMAH ─── Acoustic, supersonic, open-air
│   ├── T-Bar LOMAH ─── Acoustic, alternative geometry
│   ├── I-Bar LOMAH ─── RADAR, subsonic (★ WORLD FIRST)
│   ├── TG 4002 Box Target ── Enclosed acoustic, ±3mm accuracy
│   └── IVDU Display ─── Firing point visual feedback
│
├── TARGET MECHANISMS (TG Series)
│   ├── TG 82 Infantry ── Pop-up/rotary, LOMAH-compatible
│   ├── TG 82 Armour ──── Medium & large armour targets
│   ├── TG 82-70 Sniper ─ Portable sniper pop-up
│   ├── TG 350 Moving ─── Rail-mounted moving infantry
│   ├── Moving Armour ──── Diesel/battery vehicle movers
│   ├── TG 94 Retrievable ─ Law enforcement
│   └── PITS ───────── Portable Infantry Target System
│
├── ROBOTIC TARGETS (★ UNIQUE)
│   ├── RT-CQB ────── Close Quarter Battle, semi-autonomous
│   ├── RT-M6 ─────── Open field, hit sensing + LOMAH
│   └── CnC Controller ─ Commands up to 4 robots
│
├── SPORT SHOOTING
│   ├── TG 6302 ──── Latest 300m scoring (2024)
│   ├── TG 6110 HS ─ 10m air gun scoring
│   └── TG 6000 ──── 300m scoring (2007)
│
└── SOFTWARE
    └── AROS ──────── Advanced Range Operating Software (2016)
```

### 2.2 LOMAH H-Bar Specifications

| Parameter | Value | Source |
|-----------|-------|--------|
| **Accuracy (Zone A - center)** | ≤10mm avg radial tolerance | Polytronic spec |
| **Accuracy (Zone B)** | ≤14mm | Polytronic spec |
| **Accuracy (Zone C - edges)** | ≤16mm | Polytronic spec |
| **Accuracy (reseller data)** | ±5mm in center scoring area | Militec partner spec |
| **Box Target accuracy** | ±3mm throughout scoring area (to 1,000m) | TG 4002 spec |
| **Min projectile velocity** | 350-450 m/s at target | Varies by config |
| **Calibers** | 5.56mm to 12.7mm (infantry); up to 120mm (armour) | Product catalog |
| **Detection zone** | Up to double Fig 11 (infantry); 4×3m (armour) | Product spec |
| **Detection rate** | Up to 2,000 RPM | Polytronic spec |
| **Shooting angle (azimuth)** | ±15 degrees | Confirmed |
| **Shooting angle (elevation)** | ±3 to ±5 degrees | Confirmed |
| **Z-offset compensation** | Yes | Confirmed |
| **Angle of incidence calc** | Yes | Confirmed |

### 2.3 Physical Dimensions & Construction

| Component | Dimensions | Mass | Construction |
|-----------|-----------|------|-------------|
| **H-Bar sensor unit** | ~1200 × 450 mm (L×W) | ~10 kg | Zinc-coated sheet steel, polyester powder paint, SS fixings |
| **Portable frame (AC120)** | 1055 × 450 × 215 mm | ~12 kg | Same construction |
| **Pop-up mechanism + LOMAH** | 470 × 400 × 380 mm | ~25 kg (no battery) | Military-grade |
| **Battery pack** | Standard form factor | ~4.5 kg | Quick-fit military bayonet connector |

### 2.4 Environmental & Power

| Parameter | Value |
|-----------|-------|
| **IP Rating** | IP67 |
| **Operating Temperature** | Military standard (designed for Swiss Alps -30C to UAE desert +55C) |
| **Construction standard** | Mil-Std compliant |
| **Power** | 12V DC / rechargeable battery (6+ hours) |
| **Mains option** | 110VAC / 230-240VAC via PSU |
| **Communication** | Ethernet 10/100Mb (XML protocol) |
| **Radio range** | Line of sight, 2,000m+ |
| **Lifetime** | "Built to last for decades" - some units 40+ years operational |
| **Certifications** | ISO 9001, ISO 14001, ISO 45001 |

---

## 3. FUNCTIONAL RECONSTRUCTION

### 3.1 Overall Function

> **"Detect projectile trajectory, compute impact position, and provide real-time scoring feedback for live-fire training across all weapon types (supersonic AND subsonic)"**

### 3.2 Function Structure

```
OVERALL: Detect and score live-fire shots for training feedback

├── F1: DETECT projectile passage
│   ├── F1.1: Sense supersonic shockwave (H-Bar/T-Bar)
│   │         → [WP: Acoustic pressure transducer array]
│   ├── F1.2: Sense subsonic projectile (I-Bar) ★ UNIQUE
│   │         → [WP: RADAR millimeter-wave detection]
│   ├── F1.3: Timestamp arrival at each sensor
│   │         → [WP: High-speed ADC + precision timer]
│   └── F1.4: Filter environmental noise
│             → [WP: Bandpass filter + signal conditioning]
│
├── F2: COMPUTE shot position
│   ├── F2.1: Calculate TDOA between sensor pairs
│   │         → [WP: Cross-correlation algorithm (proprietary)]
│   ├── F2.2: Triangulate X,Y coordinates
│   │         → [WP: Multilateration with least-squares]
│   ├── F2.3: Compensate for environment (temp, wind)
│   │         → [WP: Sensor-based correction + geometric self-cal]
│   ├── F2.4: Calculate angle of incidence
│   │         → [WP: Multi-sensor trajectory reconstruction]
│   └── F2.5: Apply Z-offset compensation
│             → [WP: Geometric correction for sensor-to-target offset]
│
├── F3: COMMUNICATE data
│   ├── F3.1: Encode shot data (X, Y, score, metadata)
│   │         → [WP: XML over Ethernet 10/100Mb]
│   ├── F3.2: Transmit to AROS range server
│   │         → [WP: Wired Ethernet backbone]
│   └── F3.3: Distribute to IVDU firing point displays
│             → [WP: Ethernet/WiFi to display units]
│
├── F4: DISPLAY and SCORE
│   ├── F4.1: Render shot on graphical target (IVDU)
│   │         → [WP: Non-glare LCD with target overlay]
│   ├── F4.2: Calculate MPI and group size
│   │         → [WP: Statistical computation]
│   ├── F4.3: Recommend sight adjustments
│   │         → [WP: MPI offset → MOA/MIL correction]
│   ├── F4.4: Score per exercise type (zones, qualification)
│   │         → [WP: Configurable scoring zones in AROS]
│   └── F4.5: Multi-lane instructor overview
│             → [WP: AROS server aggregation display]
│
├── F5: MANAGE range operations (AROS)
│   ├── F5.1: Program automated exercise scenarios
│   │         → [WP: Drag-and-drop scenario editor]
│   ├── F5.2: Control target mechanisms (expose/conceal/move)
│   │         → [WP: Networked actuator commands]
│   ├── F5.3: Control robotic targets (path programming)
│   │         → [WP: CnC controller + WiFi/UHF]
│   ├── F5.4: Record session data and generate reports
│   │         → [WP: Database + report engine]
│   ├── F5.5: After-action review with replay
│   │         → [WP: Timeline-based data replay]
│   └── F5.6: Manage range scheduling and maintenance
│             → [WP: Booking and maintenance modules in AROS]
│
├── F6: CONTROL targets (integrated)
│   ├── F6.1: Pop-up/down infantry targets (TG 82)
│   │         → [WP: Electric actuator, 12V DC]
│   ├── F6.2: Rotate/slice exposure targets
│   │         → [WP: Rotary module]
│   ├── F6.3: Move targets on rail (TG 350)
│   │         → [WP: Motorized rail carrier, variable speed]
│   ├── F6.4: Deploy robotic targets (RT-CQB/RT-M6)
│   │         → [WP: Semi-autonomous mobile robot platform]
│   └── F6.5: Trigger portable targets (PITS)
│             → [WP: WiFi/UHF trigger, IR/pressure mat detection]
│
└── F_AUX: SUPPORT functions
    ├── F_AUX.1: Self-calibrate sensors
    │            → [WP: Power-up calibration routine]
    ├── F_AUX.2: Built-In Test diagnostics
    │            → [WP: Firmware status, voltage, comms, hit count]
    ├── F_AUX.3: Power management (battery/mains)
    │            → [WP: 12V DC distribution, battery monitor]
    ├── F_AUX.4: Ballistic protection for sensors
    │            → [WP: Steel enclosure below target plane]
    └── F_AUX.5: Environmental protection
                 → [WP: IP67 sealing, corrosion-resistant construction]
```

### 3.3 Key Differentiating Functions (vs Saab/InVeris)

| Function | Polytronic Unique Capability | VN-RNG-001 Implication |
|----------|---------------------------|------------------------|
| **F1.2: Subsonic RADAR detection** | World's first I-Bar for 9mm pistol rounds | Future expansion opportunity; not needed for initial product |
| **F6.4: Robotic targets** | Semi-autonomous RT-CQB/RT-M6 with hit sensing | Advanced feature; Phase 2+ consideration |
| **F5.1: Drag-and-drop scenarios** | AROS scenario editor for CQB ranges | Good UX model for VN-RNG-001 software |
| **F2.4: Angle of incidence** | Calculates projectile approach angle | Nice-to-have; adds training data value |
| **F2.5: Z-offset compensation** | Corrects for sensor-to-target-face offset | Important for accuracy; should implement |

---

## 4. WORKING PRINCIPLE CATALOG

| ID | Subfunction | Physical Effect | Form Design | Working Principle |
|----|-------------|----------------|-------------|-------------------|
| WP-1 | Sense supersonic shockwave | Acoustic pressure wave | MEMS/piezo transducer array | **Acoustic pressure transducer** |
| WP-2 | Sense subsonic projectile | Electromagnetic reflection | mm-wave radar | **RADAR doppler/reflection** ★ |
| WP-3 | Timestamp arrival | Voltage → digital time | High-speed ADC + timer | **Sub-microsecond sampling** |
| WP-4 | Cross-correlate signals | Statistical correlation | DSP algorithm | **Proprietary cross-correlation** |
| WP-5 | Triangulate position | TDOA → intersection | Multilateration solver | **Least-squares multilateration** |
| WP-6 | Environmental compensation | Temp/wind correction | Sensor + algorithm | **Real-time c(T) correction** |
| WP-7 | Z-offset compensation | Geometric correction | Known sensor-target geometry | **Offset transform matrix** |
| WP-8 | Encode/transmit data | Electrical signaling | Ethernet + XML | **XML over 100BaseT** |
| WP-9 | Display shot location | Pixel rendering | LCD + software | **Non-glare IVDU display** |
| WP-10 | Score shots | Zone mapping | Software algorithm | **Configurable scoring zones** |
| WP-11 | Program scenarios | Drag-and-drop UI | AROS web/desktop | **Visual scenario editor** |
| WP-12 | Control robotic target | Autonomous navigation | Motor + sensors + AI | **Semi-autonomous mobile robot** |
| WP-13 | Ballistic protection | Kinetic absorption | Steel enclosure | **Hardened housing** |
| WP-14 | Environmental sealing | Gasket compression | IP67 enclosure | **Military-grade sealing** |

---

## 5. DESIGN PHILOSOPHY ASSESSMENT

### 5.1 Paradigm Indicators

| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| **Safety margins** | Mil-Std, IP67, -30C to +55C range (Alps to desert) | 5 | Over-engineered for durability |
| **Modularity** | H-Bar/T-Bar/I-Bar interchangeable, targets modular | 5 | Exceptional modularity |
| **Material selection** | Zinc-coated steel, SS fixings, powder coat, aluminum (box) | 4 | Premium industrial-grade |
| **Redundancy** | 8 sensors (5 redundant beyond minimum 3) | 4 | Sensor redundancy for reliability |
| **Manufacturing precision** | Swiss-designed, dual Swiss/UAE manufacturing | 5 | Highest quality standards |
| **Innovation** | World's first LOMAH (1966), first subsonic RADAR LOMAH, robotic targets | 5 | Industry innovation leader |
| **Integration** | AROS controls static, moving, portable, AND robotic targets | 5 | Deepest multi-target integration |

### 5.2 Inferred Design Paradigm

> **"Engineer the most comprehensive, highest-quality live-fire training ecosystem in the world - from acoustic scoring to robotic adversaries - leveraging Swiss precision engineering with Middle Eastern manufacturing scale, at premium pricing justified by decades of reliability and innovation leadership."**

### 5.3 Trade-off Pattern

| Polytronic Prioritized | Over | Evidence |
|----------------------|------|----------|
| **Innovation leadership** | Cost competitiveness | First LOMAH (1966), first subsonic RADAR, first robotic targets |
| **Swiss precision** | Low price point | ±3mm box target accuracy; ISO 9001/14001/45001 |
| **Full ecosystem** | Simplicity | Static + moving + portable + robotic + sport + AROS |
| **Decades of reliability** | Fast iteration | "Built to last for decades"; 40-year old units operational |
| **Turnkey capability** | Component sales | Design → build → install → operate → maintain |
| **Dual climate design** | Single-market optimization | Swiss Alps (-30C) + UAE desert (+55C) in one product |

### 5.4 Paradigm Applicability to Vietnamese Context

| Assessment | Rationale |
|-----------|-----------|
| **Partial match - inspiration for features, not cost structure** | Polytronic's innovation (subsonic RADAR, robotic targets, AROS UX) provides aspirational features for VN-RNG-001 roadmap. However: (1) Swiss/UAE premium pricing is 4-8x Vietnamese target, (2) Robotic targets are beyond Phase 1 scope, (3) Subsonic RADAR is unique IP we cannot easily replicate, (4) AROS drag-and-drop UX is an excellent model for our web-based software |

---

## 6. TECHNOLOGY COMPARISON: Polytronic vs VN-RNG-001

### 6.1 Parallel Function Comparison

| Function | Polytronic Solution | VN-RNG-001 Option | Gap | Feasibility |
|----------|-------------------|---------------------|-----|-------------|
| **F1.1: Supersonic detection** | Acoustic transducer array (H-Bar) | COTS MEMS array (8x) | Small | HIGH |
| **F1.2: Subsonic detection** | **RADAR (I-Bar) - WORLD FIRST** | Not planned (Phase 1) | Large | LOW (radar IP) |
| **F2.1: TDOA computation** | Proprietary cross-correlation | GCC-PHAT (published) | None | HIGH |
| **F2.4: Angle of incidence** | Multi-sensor trajectory calc | Multi-sensor trajectory calc | None | MEDIUM |
| **F2.5: Z-offset compensation** | Geometric transform | Same approach | None | HIGH |
| **F4.1: Display (IVDU)** | Proprietary non-glare LCD | COTS Android tablet (sunlight-readable) | None | HIGH |
| **F5.1: Scenario programming** | AROS drag-and-drop editor | Web-based scenario editor (React) | Small | HIGH |
| **F5.3: Robotic target control** | CnC + RT-CQB/RT-M6 | Not planned (Phase 1) | Large | N/A (future) |
| **F5.6: Range booking/maintenance** | AROS integrated modules | Web-based admin panel | Small | HIGH |
| **F_AUX.5: Environmental** | IP67, Swiss Alps + UAE desert | IP67, tropical-optimized | Different focus | HIGH |

### 6.2 Technology Insertion Candidates from Polytronic

| Technology | Adoption Priority | Rationale |
|-----------|-------------------|-----------|
| **Z-offset compensation (F2.5)** | P1 - Implement | Improves accuracy for real-world mounting; simple geometry |
| **Zonal accuracy specification (A/B/C zones)** | P1 - Adopt approach | Honest accuracy reporting by zone; better than single spec |
| **AROS UX patterns (drag-and-drop)** | P2 - Inspire software | Excellent UX model for exercise configuration |
| **Box target concept (TG 4002)** | P2 - Future variant | Enclosed target for ±3mm sniper training |
| **Angle of incidence calculation** | P2 - Nice-to-have | Added training data; helps identify shooter technique |
| **Subsonic RADAR (I-Bar)** | P3+ - Long-term research | Unique capability but complex IP; consider for pistol ranges |
| **Robotic targets** | P3+ - Future expansion | Semi-autonomous adversary training; advanced feature |

### 6.3 What NOT to Copy

| Polytronic Feature | Why Skip | VN-RNG-001 Alternative |
|-------------------|----------|----------------------|
| **Dual Swiss/UAE manufacturing** | We ARE the local manufacturer | Vietnamese-only production |
| **Turnkey range construction** | Beyond initial scope | Focus on LOMAH scoring system; partner for range construction |
| **Robotic targets (Phase 1)** | Too complex for initial product | Add in future product roadmap |
| **Subsonic RADAR** | Proprietary IP, complex development | Acoustic-only for supersonic; acoustic box for subsonic future |
| **ISSF sport scoring** | Different market segment | Focus on military training first |
| **Premium pricing model** | Conflicts with cost target | Target 50-60% of import price |

---

## 7. COMPARATIVE ANALYSIS: Polytronic vs Saab vs VN-RNG-001

| Feature | Polytronic | Saab | VN-RNG-001 Target |
|---------|-----------|------|--------------------|
| **Heritage** | Inventor (1966) | 60+ years training | New entrant |
| **Accuracy (open)** | ±5mm center, zone-graded | ±5mm | ±5mm center |
| **Accuracy (enclosed)** | ±3mm (TG 4002) | N/A | Future variant |
| **Subsonic detection** | RADAR (I-Bar) ★ | No | No (Phase 1) |
| **Detection rate** | 2,000 RPM | 1,200 RPM | 1,200 RPM target |
| **Robotic targets** | Yes (RT-CQB/M6) ★ | No | No (Phase 1) |
| **Range software** | AROS | Exercise Mgmt | Web-based |
| **Ecosystem depth** | Very deep | Deepest (GAMER TESS) | Focused (LOMAH only) |
| **Tropical optimization** | Yes (UAE design) | No (Nordic heritage) | YES (native) |
| **Cost** | $$$$$ (Swiss premium) | $$$$$ (Swedish premium) | $$ (Vietnamese) |
| **Local content** | 0% | 0% | 60-75% |
| **Vendor independence** | Import-dependent | Import-dependent | 100% self-sustaining |
| **Manufacturing** | Switzerland + UAE | Sweden + Czech Rep | Vietnam |
| **Patent portfolio** | 30+ patents | Multiple | None (clean-sheet) |

---

## 8. KEY INSIGHTS FOR VN-RNG-001

### 8.1 What Polytronic Teaches Us

1. **Zone-graded accuracy specification is honest and useful.** Don't claim "±5mm" uniformly - specify Zone A (center ≤10mm), Zone B (≤14mm), Zone C (≤16mm). This sets realistic expectations and enables meaningful validation.

2. **Z-offset compensation is essential.** The sensor bar is physically below the target face. Without geometric correction for this offset, accuracy degrades at edges. Simple trigonometry, but must implement.

3. **Subsonic is a real market gap.** Polytronic's RADAR I-Bar is a world-first. If VN-RNG-001 can eventually solve subsonic detection (even with different technology like enclosed acoustic box), it opens pistol/CQB training markets.

4. **AROS UX is the gold standard.** Drag-and-drop scenario programming, unified control across target types, range booking, maintenance scheduling. Our web-based software should aspire to this level of UX.

5. **Swiss quality is achievable with Vietnamese labor.** Polytronic's UAE subsidiary proves that non-Swiss manufacturing can meet Swiss standards with proper quality systems (ISO 9001/14001/45001).

6. **Detection rate of 2,000 RPM vs 1,200 RPM.** Polytronic claims 2,000 RPM - higher than InVeris/Saab (1,200 RPM). This is a processing speed advantage, likely from faster ADC + algorithm. Target 1,200 RPM minimum, stretch to 2,000 RPM.

### 8.2 Risk Assessment

| Risk | Impact on VN-RNG-001 |
|------|---------------------|
| **Patent infringement** | Polytronic has 30+ patents. Must do freedom-to-operate analysis before production. GCC-PHAT algorithm is published/public. Sensor array geometry is common. Key risk is specific scoring computation methods. |
| **Accuracy shortfall vs Polytronic Box Target** | ±3mm is achievable with enclosed acoustic design (ShotMarker achieves 1-3mm with COTS MEMS). Open-air ±5mm is realistic target. |
| **Feature gap (subsonic, robotic)** | Not needed for initial market entry. Vietnamese military trains primarily with supersonic 7.62mm/5.56mm. |

---

## 9. POLYTRONIC DEPLOYMENT MAP (Confirmed)

| Region | Customer/Installation | Products | Date |
|--------|----------------------|----------|------|
| **Switzerland** | Swiss Armed Forces | Largest contract (TLES), sport ranges | 1966-present |
| **South Korea** | National ranges | TG 3000 sport scoring (42nd World Cup) | 1978 |
| **Norway** | Norwegian Armed Forces | Large live-fire range project | 2006 |
| **Australia** | ADI IP acquisition, Australian military | Target systems | 2002-present |
| **UAE** | Undisclosed customer | "World's largest live-fire range project" | 2016 |
| **Middle East** | Sniper training | Electronic scoring | 1993-present |
| **80+ countries** | Various | 1,000+ ranges | 1966-present |

### Contract Values (Known)

| Contract | Value | Year |
|---------|-------|------|
| Swiss Armed Forces (TLES) | "Largest sales contract" (undisclosed) | 1990 |
| "World's largest live-fire project" (Middle East) | Estimated $50-200M+ | 2016 |
| Typical complete lane | Estimated $20,000-50,000 per lane | Market rate |

---

## 10. PATENTS & IP LANDSCAPE

| Patent | Description | Relevance to VN-RNG-001 |
|--------|-------------|------------------------|
| **1969 Original** | World's first automatic marking system | Expired - no barrier |
| **WO2017137084A1** | Method and device for detecting a hit field | Review for TDOA computation approach |
| **30+ patents** | Various scoring, target apparatus, position determination | Freedom-to-operate analysis needed |
| **Subsonic RADAR** | I-Bar technology | Not relevant for Phase 1 (acoustic only) |
| **AROS software** | Range management platform | Software is independently developed |

### Freedom-to-Operate Assessment

| Area | Risk Level | Mitigation |
|------|-----------|------------|
| **Acoustic TDOA concept** | LOW | Fundamental physics; prior art from 1960s |
| **GCC-PHAT algorithm** | NONE | Published academic algorithm, not patentable |
| **Sensor array geometry** | LOW | Delta/H-bar patterns widely used, multiple prior art |
| **Specific scoring computation** | MEDIUM | Avoid copying Polytronic's exact algorithms; develop own |
| **Subsonic RADAR** | HIGH | Do not attempt without license; avoid entirely in Phase 1 |
| **Software UX patterns** | NONE | UX patterns not patentable |

---

## References

- Polytronic International AG: [polytronic.ch](https://www.polytronic.ch)
- Polytronic UAE: [polytronic.ae](https://www.polytronic.ae)
- Militec Ltd: H-Bar specifications (reseller datasheet)
- Koza Construction: H-Bar detailed technical specifications
- Patent WO2017137084A1: Polytronic International Ltd
- [[re_saab_lomah|RE: Saab LOMAH System]] - Companion analysis
- [[00_odi/odi_analysis|Phase 0 ODI Analysis]] - Customer outcome mapping

---

*Reverse engineering analysis per SKILL_reverse_engineering methodology. OSINT-based - no physical specimen.*
