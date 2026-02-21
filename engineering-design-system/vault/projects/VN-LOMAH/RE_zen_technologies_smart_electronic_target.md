---
project: VN-TRN-LOMAH
phase: 0
type: reverse-engineering
subject: Zen Technologies Smart Electronic Target (India)
version: 1.0
created: 2026-02-06
status: complete
---

# RE: Zen Technologies Smart Electronic Target (LOMAH) - India
## Reverse Engineering Analysis from Public Sources

---

## 1. SYSTEM OVERVIEW

| Item | Detail |
|------|--------|
| **Product** | Zen Smart Target System (ZEN STS) - LOMAH |
| **Manufacturer** | Zen Technologies Ltd., Hyderabad, India |
| **Type** | Electro-mechanical, software-driven, acoustical projectile detection and reporting system |
| **Application** | Outdoor live-fire small arms ranges |
| **Website** | https://www.zentechnologies.com |

**LOMAH** = **L**ocation **O**f **M**iss **A**nd **H**it

---

## 2. SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────┐
│                    SYSTEM TOPOLOGY                        │
│                                                           │
│  TARGET END (Per Lane)          FIRER'S END (Per Lane)   │
│  ┌──────────────────┐          ┌──────────────────┐      │
│  │  Pop-up Target    │          │  Firing Point     │      │
│  │  Mechanism (PT)   │◄────────►│  Equipment (FPE)  │      │
│  │                   │  Wired/  │  - Shot display   │      │
│  │  ┌─────────────┐ │  Ethernet│  - Score/rating   │      │
│  │  │ Acoustic    │ │          │  - Group size     │      │
│  │  │ Sensor Array│ │          │  - Lane status    │      │
│  │  │ (on frame)  │ │          └──────────────────┘      │
│  │  └─────────────┘ │                   │                 │
│  │  ┌─────────────┐ │                   │                 │
│  │  │ Temp Sensor │ │                   │                 │
│  │  └─────────────┘ │          ┌────────▼─────────┐      │
│  └──────────────────┘          │  Master Control   │      │
│                                │  Station (MCS)    │      │
│                                │  - Central monitor │      │
│                                │  - Results record  │      │
│                                │  - Exercise ctrl   │      │
│                                └──────────────────┘      │
└─────────────────────────────────────────────────────────┘
```

### Three Major Subsystems

| Subsystem | Location | Function |
|-----------|----------|----------|
| **Pop-up Target (PT)** | Target end | Acoustic sensor frame + pop-up mechanism |
| **Firing Point Equipment (FPE)** | Firer's end | Per-lane display, score, shot location |
| **Master Control Station (MCS)** | Central | Monitor all lanes, record results, exercise control |

**Communication:** Ethernet 100BaseT
**Power:** 12V DC / Power over Ethernet (PoE)

---

## 3. CORE DETECTION PRINCIPLE

### 3.1 Supersonic Shockwave (Mach Cone) Detection

```
         Bullet trajectory
         ══════════════════════════════►  V_bullet > V_sound
                   ╲
                    ╲  Mach cone angle: θ = arcsin(V_sound / V_bullet)
                     ╲
                      ╲
    ───────────────────╲──────────── Sensor plane (target frame)
    [Mic 1]   [Mic 2]  ╲  [Mic 3]   [Mic 4]
       │         │       ╲    │         │
       t₁        t₂      ╲   t₃        t₄
                           ╲
    TDOA = t_i - t_j  →  Triangulation  →  (X, Y) position
```

**Physics:** A supersonic bullet (>Mach 1) generates a conical shockwave. As this cone intersects the sensor plane, each microphone registers the shockwave at a slightly different time.

**Key equation:**
```
TDOA_ij = (d_i - d_j) / V_sound

Where:
  d_i = distance from bullet path to sensor i
  d_j = distance from sensor j
  V_sound = speed of sound (temperature-compensated)
```

### 3.2 Why Temperature Compensation is Critical

V_sound varies with temperature:
```
V_sound ≈ 331.3 + 0.606 × T(°C)  [m/s]

At 20°C: V_sound = 343.4 m/s
At 50°C: V_sound = 361.6 m/s  (5.3% faster)
```

This is why the system includes a **temperature sensor** on the target frame - without compensation, accuracy degrades significantly in field conditions.

---

## 4. SENSOR SUBSYSTEM ANALYSIS

### 4.1 Acoustic Sensor Array

| Parameter | Estimated Specification |
|-----------|----------------------|
| **Sensor type** | MEMS microphones (high-SPL rated) |
| **Configuration** | 3-4 sensors on rectangular/H-frame |
| **Mounting** | On target frame, below target face |
| **Protection** | Ballistic enclosure (rubber/composite) |
| **Detection** | Supersonic shockwave (Mach cone) |
| **Min. bullet velocity** | ~450 m/s (1,476 fps) at sensor plane |
| **Max fire rate** | 1,200 rounds/minute |

### 4.2 Sensor Geometry Options

Two common configurations found in LOMAH-class systems:

```
DELTA Configuration          H-BAR Configuration

      [S1]                    [S1]─────────[S2]
      / \                         │
     /   \                        │
    /     \                       │
[S2]─────[S3]               [S3]─────────[S4]

3 sensors, equilateral       4 sensors, rectangular
Simpler, fewer channels      Better accuracy, redundancy
```

### 4.3 Signal Processing Chain

```
Shockwave → MEMS Mic → Analog Frontend → High-speed ADC → TDOA Engine → (X,Y) Calculator
                              │                  │                │
                        Bandpass filter     ≥1 MHz sample    Cross-correlation
                        Gain (AGC)         rate needed       or threshold
                        Anti-alias                           detection
```

**Critical timing requirement:** For 5mm accuracy over a ~1m sensor span, timing resolution must be:
```
Δt = 5mm / 343 m/s ≈ 14.6 μs

→ ADC sample rate: ≥ 100 kHz (practical: 500 kHz - 1 MHz)
→ Timer resolution: < 1 μs for high accuracy
```

---

## 5. SPECIFICATIONS SUMMARY (Benchmarked)

| Parameter | Zen STS (LOMAH) | Industry Reference (InVeris) |
|-----------|----------------|----------------------------|
| **Detection method** | Acoustic (shockwave) | Acoustic (shockwave) |
| **Caliber range** | Small arms (5.56-12.7mm) | .22 - .50 cal (standard) |
| **Accuracy** | ±5mm (estimated) | <5mm radial at center |
| **Detection zone** | ~3 × 2.5m | 3 × 2.5m (standard) |
| **Max fire rate** | Not published | 1,200 rpm |
| **Min velocity** | Supersonic at target | 450 m/s |
| **Operating temp** | MIL-STD-810 (est.) | -25°C to +70°C |
| **IP rating** | Not published | IP67 |
| **Power** | 12V DC | 12V DC / PoE |
| **Communication** | Ethernet | 100BaseT Ethernet |
| **Wind limit** | Not published | <1.5 m/s for rated accuracy |

---

## 6. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

```
┌─────────────────────────────────────────────────────────┐
│            OVERALL FUNCTION                              │
│  "Detect and report projectile location on target"       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  F1: Detect projectile     F2: Compute position          │
│  ┌──────────────────┐     ┌──────────────────┐          │
│  │ F1.1 Sense shock-│     │ F2.1 Measure TDOA│          │
│  │      wave        │     │ F2.2 Compensate  │          │
│  │ F1.2 Filter noise│     │      temperature │          │
│  │ F1.3 Amplify     │     │ F2.3 Triangulate │          │
│  │ F1.4 Digitize    │     │      (X,Y)       │          │
│  └──────────────────┘     └──────────────────┘          │
│                                                          │
│  F3: Present target       F4: Control system             │
│  ┌──────────────────┐     ┌──────────────────┐          │
│  │ F3.1 Raise/lower │     │ F4.1 Exercise    │          │
│  │      target      │     │      programming │          │
│  │ F3.2 Rotate/move │     │ F4.2 Multi-lane  │          │
│  │ F3.3 Illuminate  │     │      management  │          │
│  └──────────────────┘     └──────────────────┘          │
│                                                          │
│  F5: Report results       F6: Withstand environment      │
│  ┌──────────────────┐     ┌──────────────────┐          │
│  │ F5.1 Display at  │     │ F6.1 Ballistic   │          │
│  │      firer pos   │     │      protection  │          │
│  │ F5.2 Record/log  │     │ F6.2 Weather     │          │
│  │ F5.3 Score/rate  │     │      sealing     │          │
│  └──────────────────┘     │ F6.3 EMC/ESD     │          │
│                           └──────────────────┘          │
└─────────────────────────────────────────────────────────┘
```

---

## 7. BILL OF MATERIALS ESTIMATE (For Indigenous Development)

### 7.1 Per-Lane Target Unit

| Component | Description | Sourcing (VN) | Est. Cost |
|-----------|-------------|---------------|-----------|
| MEMS microphones (×4) | High-SPL, wide bandwidth | Import (TDK/Knowles) | $8-20 |
| Temperature sensor | Digital (DS18B20 or similar) | Import (commodity) | $1-2 |
| MCU/DSP | STM32H7 or similar w/ high-speed ADC | Import | $10-25 |
| Analog frontend | Op-amp, bandpass filter, AGC | Mixed | $5-10 |
| Ethernet PHY + connector | 100BaseT, IP67 connector | Import | $5-10 |
| PoE module | 802.3af/at | Import | $5-10 |
| Sensor frame | Aluminum extrusion + rubber damping | **Local** (Hoa Phat) | $20-40 |
| Ballistic protection | AR500 steel or composite | Local/import | $15-30 |
| Pop-up mechanism | 12V actuator + linkage | **Local** machining | $30-60 |
| PCB + enclosure | IP67 enclosure, custom PCB | **Local** PCB fab | $15-25 |
| Cabling | Ethernet + power | **Local** | $5-10 |
| **Subtotal per lane** | | | **$120-240** |

### 7.2 Local Content Estimate

| Category | Local | Import | Local % |
|----------|-------|--------|---------|
| Mechanical (frame, actuator, enclosure) | $65-130 | $0 | **100%** |
| Electronics (PCB, passive) | $15-25 | $30-65 | ~30% |
| Software | $0 (labor) | $0 | **100%** |
| **Overall by value** | | | **~55-65%** |

---

## 8. KEY ENGINEERING CHALLENGES

| Challenge | Difficulty | Mitigation |
|-----------|-----------|------------|
| **TDOA timing accuracy** (<1 μs) | HIGH | Use STM32H7 timer capture, dedicated analog frontend |
| **Environmental noise rejection** | MEDIUM | Bandpass filter (20-100 kHz), adaptive threshold |
| **Temperature compensation** | LOW | Digital temp sensor, real-time V_sound update |
| **Ballistic protection of sensors** | MEDIUM | Rubber-backed steel baffles, sensor recessing |
| **Wind interference** | MEDIUM | Wind screens, statistical outlier rejection |
| **Multi-shot discrimination** | HIGH | Time-gating, pattern matching for burst fire |
| **Subsonic ammunition** | HIGH | Requires different approach (rubber belt + impact sound) |
| **Weatherproofing (IP67)** | MEDIUM | Potted electronics, sealed connectors |

---

## 9. COMPETITORS & BENCHMARKS

| Manufacturer | Country | Product | Notable Feature |
|-------------|---------|---------|-----------------|
| **Zen Technologies** | India | ZEN STS (LOMAH) | Integrated pop-up + MCS |
| **InVeris (Meggitt)** | USA | LOMAH | MIL-SPEC, .22-120mm range |
| **Theissen Training** | Germany | LOMAH systems | Rubber-frame zero-wind design |
| **Oakwood Controls** | UK | H-Bar LOMAH | Portable, battery-powered |
| **ShotMarker** | USA | Wireless LOMAH | LoRa RF, MEMS, consumer-grade |
| **INTARSO** | Germany | Various | Acoustic + optical + piezo |
| **BEL (ABHIAS)** | India | ABHIAS LOMAH | Indian defense competitor |
| **Steinert** | USA | TrueZeroTarget | Hunting/civilian focus |

---

## 10. ASSESSMENT SUMMARY

### Strengths
- Integrated system (target mechanism + scoring + MCS)
- Proven in Indian military service
- Cost-competitive vs Western alternatives
- Good software ecosystem (exercise programming, recording)

### Weaknesses
- Supersonic only (no subsonic capability)
- No FASIT compliance (limits NATO/US market)
- No published IP rating
- Wind-sensitive (open-air only)
- Proprietary ecosystem (no retrofit to other lifters)

### Relevance to Vietnamese Development
- Demonstrates feasibility of indigenous LOMAH development
- Similar cost structure and supply chain challenges to Vietnam
- Architecture is straightforward and reproducible
- Key differentiator opportunity: add subsonic capability + tropical hardening

---

*Analysis based entirely on publicly available information (product brochures, published specifications, academic papers, competitor datasheets).*
*The detection principle (TDOA-based acoustic shockwave triangulation) is well-established physics, not proprietary.*
