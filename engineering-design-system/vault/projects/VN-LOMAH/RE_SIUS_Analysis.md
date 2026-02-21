---
project: VN-LOMAN
type: reverse_engineering
version: 1.0
created: 2026-02-06
status: active
methodology: Reverse Engineering (4-Phase D-M-I-R)
foreign_system: Electronic Scoring Systems (LS10, HS10, S310)
manufacturer: SIUS AG
country: Switzerland
---

# REVERSE ENGINEERING ANALYSIS
## SIUS AG Electronic Target Systems (Switzerland)
## Phan tich Ky thuat Dao nguoc - He thong Bia dien tu SIUS

---

# SYSTEM IDENTIFICATION

| Field | Value |
|-------|-------|
| **Manufacturer** | SIUS AG |
| **Headquarters** | Effretikon, Switzerland |
| **Founded** | 1949 |
| **Specialization** | Electronic scoring systems for sport & military |
| **Market Position** | World leader, Official ISSF Results Provider |
| **Certification** | Only system with ISSF approval for ALL disciplines |
| **Olympic History** | Used since 1996 Atlanta, through 2024 Paris |
| **Technology** | Optical (Laser), Acoustic, and Hybrid systems |
| **Analysis Date** | 2026-02-06 |
| **Analysis Type** | Open Source (web, patents, specifications) |

---

# PART 1: PHASE 1 - DIAGNOSIS (RECONNAISSANCE)

## 1.1 Company Overview

SIUS AG is the undisputed world leader in electronic target systems for precision shooting sports. Key facts:

- **50+ years** of experience in shooting sports
- **Only manufacturer** with ISSF approval for all disciplines
- **Official ISSF Results Service Provider**
- Supplies all **Olympic Games** and **World Championships**
- Partnership with **CISM** (International Military Sports Council)
- Products used in **military and law enforcement** training worldwide

## 1.2 Product Portfolio

```
SIUS AG PRODUCT FAMILY
===============================================================================

OPTICAL SYSTEMS (Highest Precision)
+------------------------------------------------------------------+
| LS10 LASERSCORE                                                   |
| Distance: 10m (airguns)                                           |
| Technology: Triple infrared laser detection                       |
| Accuracy: 0.01-0.1mm (industry best)                             |
| Certification: ISSF Phase 1, 2, 3                                |
| Applications: Olympic-level 10m air rifle/pistol                 |
+------------------------------------------------------------------+
| LS25/50 LASERSCORE                                               |
| Distance: 25m/50m (small bore)                                   |
| Technology: Fully optical, 160,000 measurements/second           |
| Accuracy: Sub-millimeter                                          |
| Applications: Olympic 25m/50m rifle/pistol                       |
+------------------------------------------------------------------+

HYBRID SYSTEMS (Best Value)
+------------------------------------------------------------------+
| HS10 HYBRIDSCORE                                                 |
| Distance: 10-20m (airguns), 50m (small bore with adapter)        |
| Technology: Dual IR laser + acoustic detection                   |
| Accuracy: Sub-millimeter in center, few mm at edges              |
| Price: EUR 3,290 (single target)                                 |
| Certification: ISSF Phase 1                                      |
| Applications: Club/training level, outdoor capable               |
+------------------------------------------------------------------+

ACOUSTIC SYSTEMS (Long Range)
+------------------------------------------------------------------+
| S310 / S110                                                       |
| Distance: 100-600m (big bore rifles)                             |
| Technology: Acoustic TDOA (4-5 microphones)                      |
| Detection Surface: 1330 x 1500mm                                 |
| Power: 7.6W                                                       |
| Certification: ISSF Phase 1, 2, 3 (only 300m target approved)    |
| Applications: 300m ISSF, military qualification                  |
+------------------------------------------------------------------+

CONTROL SYSTEMS
+------------------------------------------------------------------+
| SA941 / SA951                                                     |
| Function: Multi-lane range control                               |
| Display: 10.5" touchscreen (SA951)                              |
| Disciplines: All ISSF from 10m to 300m preprogrammed            |
| Interface: Network, printer, results management                  |
+------------------------------------------------------------------+

===============================================================================
```

## 1.3 Technical Specifications

### 1.3.1 LS10 Laserscore (Optical - Highest Precision)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Technology** | Triple infrared laser | 950nm wavelength |
| **Measurement Rate** | 100,000-200,000/second | Per patent documentation |
| **Accuracy** | 0.01-0.1mm | Industry-leading precision |
| **Detection Method** | Non-contact, in target plane | No parallax error |
| **Target Distance** | 10m | Air rifle/pistol |
| **Wear** | Zero | No contact with projectile |
| **ISSF Approval** | Phase 1, 2, 3 | Full certification |
| **Patent Protection** | Worldwide | Protected technology |

### 1.3.2 HS10 Hybridscore (Hybrid - Best Value)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Technology** | Dual IR laser + acoustic | Hybrid measurement |
| **Optical Zone** | Central target area | Highest precision |
| **Acoustic Zone** | Outer target area | Extended coverage |
| **Accuracy** | Sub-mm (center), ~few mm (edge) | Best of both |
| **Target Distance** | 10-20m (air), 50m (small bore) | Versatile |
| **Power** | 30W, 110-240VAC | Universal input |
| **Illumination** | Integrated LED | High-intensity |
| **Price** | EUR 3,290 | Including VAT |
| **ISSF Approval** | Phase 1 | Training/club level |

### 1.3.3 S310 (Acoustic - Long Range)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Technology** | Acoustic TDOA | 4-5 ultrasonic transducers |
| **Detection Surface** | 1330 x 1500mm | Large scoring area |
| **Target Distance** | 100-600m | Big bore rifles |
| **Power** | 7.6W | Low power |
| **Caliber** | Military/sporting rifle | No restrictions |
| **Velocity** | Supersonic required | >340 m/s |
| **Mounting** | Bottom (bullet-proof area) | High durability |
| **ISSF Approval** | Phase 1, 2, 3 | Only 300m target approved |

## 1.4 Pricing Summary

| Product | Price (EUR) | Price (USD) | Application |
|---------|-------------|-------------|-------------|
| **LS10 Laserscore** | ~5,000-8,000 | ~$5,500-8,800 | Olympic/competition |
| **HS10 Hybridscore** | 3,290 | ~$3,600 | Club/training |
| **HS10 + SIUSLANE** | ~1,800-2,000 | ~$2,000-2,200 | Basic setup |
| **HS10 Complete System** | ~3,000 | ~$3,300 | With lifter, cables, software |
| **S310 (300m)** | 8,000-15,000 | ~$8,800-16,500 | Military/ISSF ranges |
| **SA951 Control Unit** | ~2,000-4,000 | ~$2,200-4,400 | Range management |

---

# PART 2: PHASE 2 - MODELING (FUNCTIONAL RECONSTRUCTION)

## 2.1 Technology Comparison

### 2.1.1 Three Detection Technologies

```
SIUS DETECTION TECHNOLOGY COMPARISON
===============================================================================

                    OPTICAL              ACOUSTIC            HYBRID
                    (LS10/LS25)          (S310)              (HS10)
                    -----------          --------            ------

PRINCIPLE           IR laser barrier     Shock wave TDOA     Both combined

ACCURACY            0.01-0.1mm           ~1-5mm              Sub-mm (center)
                    (exceptional)        (good)              ~few mm (edge)

RANGE               10-50m               100-600m            10-50m
                    (limited)            (long range)        (versatile)

VELOCITY REQ        Any                  Supersonic only     Any (optical)
                                         >340 m/s            Supersonic (acoustic)

PROJECTILE          Air pellets,         Bullets only        Both
                    bullets

WEAR                Zero                 Low (front frame)   Very low

COST                High                 Moderate            Moderate

PARALLAX            None                 None                None

ISSF LEVEL          Full (1,2,3)        Full (1,2,3)        Phase 1

===============================================================================
```

### 2.1.2 Optical Detection Principle (LS10)

```
OPTICAL DETECTION - TRIPLE IR LASER SYSTEM
===============================================================================

SIDE VIEW:
                    Projectile path
                         |
                         v
    +------------------+-+------------------+
    |    IR Emitters   | |   IR Receivers  |
    |                  | |                  |
    | LED1 ~~~~~~~~~~~>|*|<~~~~~~~~~~~ PT1 |
    |                  | |                  |
    | LED2 ~~~~~~~~~~~>|*|<~~~~~~~~~~~ PT2 |
    |                  | |                  |
    | LED3 ~~~~~~~~~~~>|*|<~~~~~~~~~~~ PT3 |
    |                  | |                  |
    +------------------+-+------------------+
                       | |
                       | | <- Pellet interrupts beams
                       v v

TOP VIEW (Detection Grid):
    +--------------------------------------------------+
    |  \  \  \  \  \  \  \  \  \  \  \  \  \  \  \    |
    |   \  \  \  \  \  \  \  \  \  \  \  \  \  \  \   |
    |    \  \  \  \  \  \  \  \  \  \  \  \  \  \  \  |
    |     \  \  \  \  \  *  \  \  \  \  \  \  \  \    |
    |      \  \  \  \  \ | \  \  \  \  \  \  \  \     |
    |       \  \  \  \  \|  \  \  \  \  \  \  \  \    |  Group A (diagonal)
    |        \  \  \  \  *  \  \  \  \  \  \  \  \    |
    +--------------------------------------------------+
    |        /  /  /  /  *  /  /  /  /  /  /  /  /    |
    |       /  /  /  /  /|  /  /  /  /  /  /  /  /    |
    |      /  /  /  /  / | /  /  /  /  /  /  /  /     |
    |     /  /  /  /  /  *  /  /  /  /  /  /  /       |  Group B (diagonal)
    |    /  /  /  /  /  /  /  /  /  /  /  /  /        |
    |   /  /  /  /  /  /  /  /  /  /  /  /  /         |
    |  /  /  /  /  /  /  /  /  /  /  /  /  /          |
    +--------------------------------------------------+

    * = Pellet passage point (intersection of interrupted beams)

SPECIFICATIONS (from patent):
- 36 IR phototransistors per array
- 950nm wavelength LEDs
- 2 crossing groups of optical paths
- Beam spacing < projectile diameter (typically <2mm)
- Sampling rate: 100,000-200,000 Hz
- Position from partial beam interruption analysis

===============================================================================
```

### 2.1.3 Acoustic Detection Principle (S310)

```
ACOUSTIC DETECTION - 5-SENSOR TDOA
===============================================================================

SENSOR ARRANGEMENT (S310 rear):
    +--------------------------------------------------+
    |                                                   |
    |        S1                           S2            |
    |         o                            o            |
    |                                                   |
    |                                                   |
    |                     S3                            |
    |                      o                            |
    |                                                   |
    |                                                   |
    |        S4                           S5            |
    |         o                            o            |
    |                                                   |
    +--------------------------------------------------+

    Detection surface: 1330 x 1500mm

WORKING PRINCIPLE:
    1. Supersonic bullet creates shock wave
    2. Shock wave reaches each sensor at different times
    3. Time differences (TDOA) calculated
    4. Position triangulated from 4+ time measurements
    5. Overdetermined system (5 sensors, 2 unknowns) improves accuracy

TDOA EQUATIONS:
    dt12 = t2 - t1 -> Hyperbola 1
    dt13 = t3 - t1 -> Hyperbola 2
    dt14 = t4 - t1 -> Hyperbola 3
    dt15 = t5 - t1 -> Hyperbola 4

    Position (x,y) = Intersection point (least-squares fit)

===============================================================================
```

### 2.1.4 Hybrid Detection Principle (HS10)

```
HYBRID DETECTION - COMBINED OPTICAL + ACOUSTIC
===============================================================================

CROSS-SECTION VIEW:

    +--------------------------------------------------+
    |                                                   |
    |     OUTER ZONE (Acoustic)                        |
    |     +------------------------------------+       |
    |     |                                    |       |
    |     |    INNER ZONE (Optical)           |       |
    |     |    +------------------------+     |       |
    |     |    |                        |     |       |
    |     |    |    TARGET CENTER      |     |       |
    |     |    |         *             |     |       |
    |     |    |    (0.01-0.1mm)       |     |       |
    |     |    |                        |     |       |
    |     |    +------------------------+     |       |
    |     |         (~1-5mm)                  |       |
    |     +------------------------------------+       |
    |                                                   |
    +--------------------------------------------------+

ADVANTAGES:
    1. Best accuracy in center where it matters most (10-ring)
    2. Extended coverage at edges (misses detected)
    3. Lower cost than full optical coverage
    4. Works with both air pellets and bullets
    5. No parallax error (both measure in target plane)

PATENT CLAIM (US8570499B2):
    "The shooting position is determined exclusively in an
    opto-electronic manner in a first impact area [center] and
    exclusively in an acousto-electronic manner in a second
    impact area [outer zone]."

===============================================================================
```

## 2.2 Function Structure

```
FUNCTION STRUCTURE: SIUS ELECTRONIC TARGET SYSTEMS
===============================================================================

OVERALL FUNCTION: Detect projectile passage through target plane
                  and display precise impact position in real-time

F1: DETECT PROJECTILE (Optical - LS10/HS10 center)
+-- F1.1: Generate IR light -------------------- LED emitters (950nm)
+-- F1.2: Create detection grid ---------------- 2 crossing beam groups
+-- F1.3: Detect beam interruption ------------- Phototransistors (36+)
+-- F1.4: Sample at high rate ------------------ 100,000-200,000 Hz
+-- F1.5: Measure partial coverage ------------- Analog signal analysis
+-- F1.6: Self-calibrate brightness ------------ Max/min reference

F2: DETECT PROJECTILE (Acoustic - S310/HS10 edge)
+-- F2.1: Capture shock wave ------------------- Ultrasonic transducers (4-5)
+-- F2.2: Convert acoustic to electrical ------- Piezoelectric conversion
+-- F2.3: Timestamp arrival -------------------- High-speed ADC
+-- F2.4: Compensate temperature --------------- Speed of sound adjustment
+-- F2.5: Calculate time differences ----------- TDOA algorithm

F3: CALCULATE POSITION
+-- F3.1: Identify interrupted beams (optical) - Digital logic
+-- F3.2: Calculate intersection (optical) ----- Geometric algorithm
+-- F3.3: Triangulate position (acoustic) ------ Hyperbolic intersection
+-- F3.4: Apply least-squares fit -------------- Error minimization
+-- F3.5: Convert to target coordinates -------- X, Y in mm
+-- F3.6: Calculate score ---------------------- Ring/decimal value

F4: COMMUNICATE RESULTS
+-- F4.1: Format data packet ------------------- Protocol encoding
+-- F4.2: Transmit via network ----------------- Ethernet/RS-485
+-- F4.3: Support multi-lane ------------------- Synchronized timing
+-- F4.4: Interface with SIUSDATA -------------- Range management

F5: DISPLAY & RECORD
+-- F5.1: Show impact on target image ---------- Graphics rendering
+-- F5.2: Display score ------------------------ Decimal scoring
+-- F5.3: Calculate group statistics ----------- Mean, SD, group size
+-- F5.4: Store session data ------------------- Results database
+-- F5.5: Print results ------------------------ Thermal/laser printer
+-- F5.6: Export to ISSF format ---------------- Competition reporting

F_AUX: SUPPORT FUNCTIONS
+-- F_AUX.1: Illuminate target ----------------- LED lighting (HS10)
+-- F_AUX.2: Power electronics ----------------- 24V/30W systems
+-- F_AUX.3: Protect from projectiles ---------- Bullet trap/frame
+-- F_AUX.4: Mount target face ----------------- Replaceable paper/carrier
+-- F_AUX.5: Lift/lower target ----------------- Motorized mechanism

===============================================================================
TOTAL: 5 Main Functions + 1 Auxiliary = 6 Function Groups, 33 Subfunctions
===============================================================================
```

---

# PART 3: DESIGN PARADIGM ANALYSIS

## 3.1 Observed Indicators

| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| **Accuracy** | 0.01-0.1mm optical (world-leading) | 5 | Uncompromising precision |
| **Certification** | Only full ISSF approval | 5 | Regulatory excellence |
| **Technology** | Patented optical system | 5 | Innovation leader |
| **Quality** | Swiss manufacturing | 5 | Premium quality |
| **Range coverage** | 10m to 600m products | 5 | Complete portfolio |
| **Integration** | Full ecosystem (targets, control, software) | 5 | System approach |
| **Price** | Premium segment | 3 | Not cost-competitive |
| **Military focus** | Secondary to sport | 3 | Sport-first strategy |

**Overall Paradigm Score: 4.5/5** (Precision-first, Swiss quality, sport shooting focus)

## 3.2 Designer's Paradigm Statement

> "Deliver uncompromising measurement accuracy for Olympic-level shooting sports through continuous innovation in optical and acoustic sensing technology, maintaining ISSF certification leadership and Swiss manufacturing quality."

## 3.3 Trade-off Analysis

| Trade-off | Choice Made | Alternative Forgone | Rationale |
|-----------|-------------|---------------------|-----------|
| **Accuracy vs. Cost** | Maximum accuracy | Lower price | Competition requires best precision |
| **Optical vs. Acoustic** | Optical for 10m | Acoustic (cheaper) | 0.1mm vs 1mm accuracy |
| **Sport vs. Military** | Sport focus | Military scale | ISSF certification priority |
| **Swiss vs. Offshore** | Swiss manufacturing | Lower cost production | Quality reputation |
| **Proprietary vs. Open** | Patented technology | Open standards | Protect innovation |
| **Full system vs. Components** | Integrated ecosystem | Component sales | Control user experience |

## 3.4 Strengths and Limitations

### Strengths
1. **World-leading accuracy** - 0.01-0.1mm with optical systems
2. **Only full ISSF certification** - Required for Olympic/World Championships
3. **Complete ecosystem** - Targets, control units, software, printers
4. **50+ years experience** - Proven reliability and support
5. **Swiss quality** - Premium manufacturing standards
6. **Hybrid innovation** - Best-value HS10 combines technologies
7. **Long-range capability** - S310 covers 100-600m big bore

### Limitations
1. **Premium pricing** - EUR 3,290-15,000+ per target
2. **Sport-focused** - Not optimized for military LOMAH applications
3. **Fixed installation** - Not designed for rapid tactical deployment
4. **Proprietary** - Locked into SIUS ecosystem
5. **Complex infrastructure** - Requires network, power, control systems
6. **No portable option** - Unlike H-Bar or TrueZeroTarget

---

# PART 4: PHASE 3 - INTERVENTION (APPLICATION STRATEGY)

## 4.1 Relevance to VN-LOMAN

SIUS targets a **different market segment** than VN-LOMAN:

| Aspect | SIUS | VN-LOMAN Target |
|--------|------|-----------------|
| **Primary Market** | Sport shooting (Olympic) | Military training |
| **Form Factor** | Fixed installation | Portable |
| **Accuracy Need** | 0.1mm (10-ring scoring) | 5mm (hit/miss) |
| **Price Point** | EUR 3,000-15,000 | $1,500-2,000 |
| **Communication** | Wired network | Wireless (Wi-Fi/LoRa) |
| **Deployment** | Permanent range | Rapid tactical |

## 4.2 Technology Lessons for VN-LOMAN

### 4.2.1 Adopt from SIUS

| Technology | SIUS Implementation | VN-LOMAN Application |
|------------|---------------------|----------------------|
| **Hybrid approach** | Optical center + acoustic edge | Consider for premium variant |
| **Temperature compensation** | Critical for acoustic accuracy | Must implement |
| **5-sensor TDOA** | Overdetermined system | Consider 5-6 sensors |
| **Self-calibration** | Automatic brightness adjustment | Implement for acoustic |
| **Decimal scoring** | 10.9, 10.8, etc. | Not needed (hit/miss) |

### 4.2.2 NOT Applicable to VN-LOMAN

| Technology | Reason Not Applicable |
|------------|----------------------|
| **Optical detection** | Too expensive, unnecessary for training |
| **0.1mm accuracy** | Overkill for military hit/miss |
| **Wired network** | Requires infrastructure |
| **Fixed installation** | Not portable |
| **ISSF certification** | Different market |

## 4.3 Competitive Positioning

```
ELECTRONIC TARGET MARKET SEGMENTATION
===============================================================================

                        ACCURACY
           HIGH (0.1mm)                    LOW (5mm)
              |                               |
    +---------+-------------------------------+
    |         |                               |
    |  SIUS   |                               |
    |  LS10   |                               |  PREMIUM
    |         |                               |  (>$5,000)
    |         |                               |
    +---------+-------------------------------+
    |         |                               |
    |  SIUS   |      KONGSBERG               |
    |  HS10   |      (Military)               |  MID-RANGE
    |         |                               |  ($2,000-5,000)
    |         |                               |
    +---------+-------------------------------+
    |         |                               |
    | MEGALINK|   TRUEZERO    H-BAR          |
    |         |                               |  VALUE
    |         |      VN-LOMAN (Target)       |  ($1,000-2,000)
    |         |                               |
    +---------+-------------------------------+
              |                               |
           SPORT                          MILITARY
                    APPLICATION

VN-LOMAN POSITIONING:
- VALUE segment ($1,500-2,000)
- MILITARY application (training, not competition)
- MODERATE accuracy (+/-5mm, sufficient for training)
- PORTABLE form factor (unlike SIUS)

===============================================================================
```

## 4.4 Updated VN-LOMAN Requirements

Based on SIUS analysis, confirm VN-LOMAN does NOT need:
- 0.1mm accuracy (5mm is sufficient)
- Optical detection (acoustic is appropriate)
- ISSF certification (military standards instead)
- Fixed installation design (portable required)
- Decimal scoring (hit/miss is sufficient)

VN-LOMAN SHOULD implement:
- Temperature compensation (critical for Vietnam climate)
- 5-6 sensor option (overdetermined TDOA)
- Self-calibration capability
- Robust outdoor enclosure (tropical conditions)

---

# PART 5: PHASE 4 - REFLECTION

## 5.1 Key Insights from SIUS Analysis

1. **Different market segments require different solutions** - SIUS optimizes for 0.1mm accuracy at high cost; VN-LOMAN needs 5mm at low cost.

2. **Optical is superior for precision but expensive** - LS10's 0.1mm accuracy requires complex IR laser arrays. Not justified for military training.

3. **Hybrid approach has merit** - HS10's combination provides good value. VN-LOMAN could offer hybrid variant for competition use.

4. **Temperature compensation is critical** - Even SIUS emphasizes this for acoustic systems. Essential for Vietnam's climate.

5. **5-sensor TDOA improves accuracy** - Overdetermined system reduces errors. VN-LOMAN should support 5-6 sensors.

6. **SIUS prices validate VN-LOMAN opportunity** - At EUR 3,290 for HS10, there's room for $1,500-2,000 military-focused alternative.

## 5.2 Four-System Comparison

```
LOMAH/ELECTRONIC TARGET COMPARISON
===============================================================================

                | TrueZero   | H-Bar      | SIUS HS10  | VN-LOMAN
                | (Norway)   | (USA)      | (Swiss)    | (Vietnam)
----------------|------------|------------|------------|------------
MARKET          | Consumer   | Military   | Sport      | Military
ACCURACY        | +/-3mm     | +/-5mm     | <1mm       | +/-5mm
TECHNOLOGY      | Acoustic   | Acoustic   | Hybrid     | Acoustic
SENSORS         | 4+         | 6          | IR+4       | 4-6
COMM RANGE      | 300m WiFi  | 5km Radio  | Wired      | 1km LoRa
PORTABLE        | Yes        | Yes        | No         | Yes
PRICE           | EUR 3,490  | High       | EUR 3,290  | $1,500-2,000
LOCAL CONTENT   | 0%         | 0%         | 0%         | 70%+

===============================================================================
```

## 5.3 Final VN-LOMAN Specification Confirmation

| Parameter | Specification | Rationale |
|-----------|---------------|-----------|
| **Technology** | Acoustic TDOA | Cost-effective, proven |
| **Accuracy** | +/-5mm | Sufficient for training |
| **Sensors** | 4 standard, 6 optional | Balance cost/redundancy |
| **Min Velocity** | 380 m/s | Military calibers |
| **Communication** | Wi-Fi + LoRa (1km) | Portable + range |
| **Display** | Android tablet | Cost-effective |
| **Power** | LiFePO4 battery | 12+ hours |
| **Enclosure** | IP65 aluminum | Tropical durability |
| **Price** | $1,500-2,000 | 50% of imports |
| **Local Content** | 70%+ | Self-reliance |

---

# APPENDIX A: SOURCES

## Web Sources
- [SIUS AG Official Website](https://www.sius.com/en)
- [SIUS HS10 Hybridscore Product Page](https://www.sius.com/en/product-page/hs10-hybridscore)
- [SIUS S310 Product Page](https://www.sius.com/en/product-page/s310-schweiz)
- [SIUS Support - S310 Ammunition](https://support.sius.com/knowledge-base/approved-ammunition-for-the-s310-300m-rifle-target/)
- [Euroshooting - HS10 Pricing](https://www.euroshooting.eu/en/index.php?detail=HS1050)
- [CISM Partnership Announcement](https://www.milsport.one/news/cism-partners/aiming-for-excellence-cism-announces-partnership-with-sius-ag)

## Patent Sources
- [US8570499B2 - Method for electronically determining shooting position](https://patents.google.com/patent/US8570499B2/en)

## Related Documents
- [[RE_TrueZeroTarget_Analysis|TrueZeroTarget RE Analysis]]
- [[RE_OakwoodHBar_Analysis|Oakwood H-Bar RE Analysis]]

---

# APPENDIX B: COMPANY PROFILE

## SIUS AG

| Field | Value |
|-------|-------|
| **Founded** | 1949 |
| **Headquarters** | Effretikon, Switzerland |
| **Employees** | ~50-100 (estimated) |
| **Specialization** | Electronic scoring systems |
| **Market Position** | World leader, ISSF official provider |
| **Olympic Games** | 1996 Atlanta through 2024 Paris |
| **Certifications** | Only full ISSF approval (Phase 1, 2, 3) |
| **Partners** | CISM, national federations worldwide |
| **US Subsidiary** | SIUS USA, Inc. |

## Key Products by Application

| Distance | Product | Technology | Price Range |
|----------|---------|------------|-------------|
| 10m | LS10 | Optical | $5,000-8,000 |
| 10m | HS10 | Hybrid | $3,600 |
| 25m | LS25 | Optical | $6,000+ |
| 50m | LS50 | Optical | $8,000+ |
| 300m | S310 | Acoustic | $10,000-15,000 |

---

# REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-06** | **Initial RE analysis. SIUS AG (Switzerland) fully documented. Three technology types analyzed: optical (0.1mm), acoustic (1-5mm), hybrid. Patent US8570499B2 reviewed. Market positioning confirms VN-LOMAN opportunity in value/military segment.** |

---

*This reverse engineering analysis follows the 4-Phase D-M-I-R methodology for systematic extraction of design knowledge from foreign military/commercial systems.*

**Analysis Status:** COMPLETE
