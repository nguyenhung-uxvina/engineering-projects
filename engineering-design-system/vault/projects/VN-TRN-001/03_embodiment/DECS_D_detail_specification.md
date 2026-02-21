---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: DECS-D
title: Detail Specification
version: 1.0
created: 2026-02-06
status: complete
---

# STEP D: DETAIL SPECIFICATION
## Dimensions, Tolerances, Surfaces & Component Specifications
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 9 of 15

**Purpose:** Specify all critical dimensions with tolerances, surface finishes, fits, fastener specifications, and detailed component data for the BSU-V1 definitive layout.

**Input:** [[PRAD_D_structure]] (Structural design), [[DECS_E_evaluate_variants]] (Selected layout L1)
**Output:** Complete specification for production drawing generation (Phase 4)

---

## 1. CRITICAL DIMENSION SPECIFICATION

### 1.1 Sensor Bar Assembly

| Feature | Nominal | Tolerance | Basis |
|---------|---------|-----------|-------|
| **Overall length** | 1040 mm | ±1.0 mm | Mic spacing accuracy |
| **Cross-section (external)** | 60 × 40 mm | ±0.5 mm | Extrusion die tolerance |
| **Wall thickness** | 3.0 mm | ±0.3 mm | Structural minimum |
| **Mic pocket center-to-center (M1-M2)** | 347.0 mm | ±0.2 mm | TDOA accuracy critical |
| **Mic pocket center-to-center (M2-M3)** | 347.0 mm | ±0.2 mm | TDOA accuracy critical |
| **Mic pocket center-to-center (M3-M4)** | 347.0 mm | ±0.2 mm | TDOA accuracy critical |
| **Mic pocket diameter** | 10.0 mm | +0.05/-0.00 (H7) | Press-fit for rubber boot |
| **Mic pocket depth** | 15.0 mm | ±0.1 mm | Mic membrane flush with surface |
| **Non-coplanar offset (M2, M4)** | 30.0 mm | ±0.1 mm | Calibration-free geometry critical |
| **Clamp slot width** | 12.0 mm | +0.2/-0.0 mm | Clamp jaw clearance |
| **Clamp slot center positions** | 347 mm from each end | ±1.0 mm | Structural support points |
| **Cable exit hole diameter** | 12.0 mm | ±0.2 mm | IP67 cable gland thread |
| **Mounting V-groove angle** | 90° | ±2° | Frame rail alignment |

### 1.2 Processing Enclosure

| Feature | Nominal | Tolerance | Basis |
|---------|---------|-----------|-------|
| **External dimensions (L×W×H)** | 250 × 180 × 120 mm | ±0.5 mm | General machining |
| **Internal cavity (L×W×H)** | 238 × 168 × 108 mm | ±0.3 mm | Component clearance |
| **Wall thickness (sides/top)** | 4.0 mm | ±0.2 mm | Structural + EMC shielding |
| **Base plate thickness** | 6.0 mm | ±0.3 mm | Thermal mass + structural |
| **O-ring groove width** | 3.5 mm | ±0.1 mm | AS568A groove spec for 2.62mm cord |
| **O-ring groove depth** | 2.0 mm | ±0.05 mm | 15-25% compression ratio |
| **O-ring groove corner radius** | R0.3 mm | max | Prevent O-ring extrusion |
| **Lid bolt holes (M4 clearance)** | Ø4.5 mm × 6 | ±0.1 mm (position) | Hexagonal pattern, 6 bolts |
| **Lid bolt circle diameter** | Per pattern | ±0.2 mm | Sealing uniformity |
| **PCB standoff holes (M3 threaded)** | Ø2.5 mm tap × 8 | ±0.1 mm (position) | Main PCB (4) + Power PCB (4) |
| **Standoff height** | 8.0 mm | ±0.2 mm | PCB clearance from base |
| **Battery compartment (L×W×H)** | 80 × 80 × 25 mm | ±0.5 mm | 4S1P pack clearance |
| **Battery door opening** | 85 × 85 mm | ±0.5 mm | Pack extraction clearance |
| **Cable gland holes (M20×1.5)** | Ø20.5 mm × 3 | ±0.15 mm | IP67 cable gland thread |
| **VESA mount pattern** | 100 × 100 mm | ±0.3 mm | M6 threaded inserts ×4 |
| **Corner fillet radius (external)** | R5.0 mm | min | Stress concentration reduction |
| **Corner fillet radius (internal)** | R3.0 mm | min | CNC tool radius limitation |

### 1.3 Critical Sensor Geometry (TDOA Accuracy)

```
SENSOR POSITION SPECIFICATION (Top View)
══════════════════════════════════════════

Reference: M1 center = origin (0, 0, 0)

        X-axis (along bar)
        ─────────────────────────────────→

M1 ●────────────── M2 ●────────────── M3 ●────────────── M4 ●
(0,0,0)          (347,0,30)        (694,0,0)         (1041,0,30)

Position Tolerances (all relative to M1):
┌────────┬───────────────────┬─────────────┐
│ Sensor │ Position (X,Y,Z)  │ Tolerance   │
├────────┼───────────────────┼─────────────┤
│ M1     │ 0, 0, 0 (datum)   │ — (origin)  │
│ M2     │ 347, 0, 30        │ ±0.2, ±0.5, ±0.1 mm │
│ M3     │ 694, 0, 0         │ ±0.3, ±0.5, ±0.1 mm │
│ M4     │ 1041, 0, 30       │ ±0.4, ±0.5, ±0.1 mm │
└────────┴───────────────────┴─────────────┘

CRITICAL: Z-axis tolerance ±0.1 mm
  The non-coplanar offset (30mm) must be accurate to ±0.1mm
  because the calibration-free algorithm derives speed-of-sound
  from the z-offset. A 0.1mm error in z causes ~0.3% velocity
  error → ~0.3mm position error at 1m miss distance. Acceptable.

X-axis tolerance ±0.2-0.4 mm
  Mic spacing enters TDOA equation directly. At 347mm spacing,
  ±0.4mm = 0.12% error → ~0.12mm position error. Acceptable.
```

**Tolerance justification:** Vietnamese CNC job shops routinely achieve ±0.05mm on single-setup features and ±0.2mm on multi-setup features. The specified ±0.1-0.4mm tolerances are well within local capability.

---

## 2. SURFACE SPECIFICATIONS

### 2.1 External Surfaces

| Surface | Finish | Roughness | Treatment | Standard |
|---------|--------|-----------|-----------|----------|
| Enclosure body (external) | Machined | Ra 3.2 μm | Hard anodize Type III (25μm min) + paint | MIL-A-8625F + RAL 6031 |
| Enclosure body (internal) | Machined | Ra 6.3 μm | Clear anodize Type II (10μm) | MIL-A-8625F |
| Base plate (external bottom) | Machined flat | Ra 3.2 μm | Hard anodize Type III (25μm) | Heat dissipation surface |
| O-ring groove | Machined | Ra 0.8 μm | Clear anodize Type II | Seal surface must be smooth |
| Sensor bar (external) | Extrusion finish | Ra 1.6 μm (as-extruded) | Hard anodize + paint | MIL-A-8625F + RAL 6031 |
| Sensor bar mic pockets | CNC machined | Ra 1.6 μm | Clear anodize Type II | Acoustic coupling surface |
| Battery door | Machined | Ra 3.2 μm | Hard anodize + paint | Match enclosure |
| Lid | Machined | Ra 3.2 μm | Hard anodize + paint | Match enclosure |

### 2.2 PCB Surfaces

| Surface | Specification | Standard |
|---------|--------------|----------|
| Main PCB solder finish | ENIG (Electroless Nickel Immersion Gold) | IPC-4552 |
| Power PCB solder finish | HASL lead-free (SAC305) | J-STD-006 |
| Daughter PCB solder finish | ENIG | IPC-4552 |
| Conformal coating (all PCBs) | Acrylic, HumiSeal 1B31, 25-75 μm | IPC-CC-830C Class 3 |
| Solder mask color | Green | Standard |
| Silkscreen | White, component designators + polarity marks | IPC-7351 |

### 2.3 Paint Specification

| Parameter | Specification |
|-----------|--------------|
| Color | RAL 6031 (Bronze Green) - Vietnamese military standard |
| Type | 2-component polyurethane, UV-resistant |
| Thickness | 40-60 μm dry film |
| Adhesion | ASTM D3359 Method B: 5B (no removal) |
| Application | Spray after anodize, before assembly |
| Salt spray | ASTM B117: no blistering after 500 hours |

---

## 3. INTERFACE SPECIFICATIONS

### 3.1 Fastener Schedule

| Location | Fastener | Size | Material | Qty | Torque | Standard |
|----------|----------|------|----------|-----|--------|----------|
| Lid to body | Socket head cap screw | M4 × 12mm | SS 316 | 6 | 2.5 Nm | DIN 912 |
| Lid bolt washer | Split lock washer | M4 | SS 316 | 6 | — | DIN 7980 |
| PCB standoff (main) | Male-female hex standoff | M3 × 8mm | Brass, nickel-plated | 4 | 0.5 Nm | — |
| PCB standoff (power) | Male-female hex standoff | M3 × 8mm | Brass, nickel-plated | 4 | 0.5 Nm | — |
| PCB screw (main) | Pan head Phillips | M3 × 6mm | SS 304 | 4 | 0.4 Nm | DIN 7985 |
| PCB screw (power) | Pan head Phillips | M3 × 6mm | SS 304 | 4 | 0.4 Nm | DIN 7985 |
| Battery strap bolt | Hex flange bolt | M4 × 8mm | SS 316 | 2 | 1.5 Nm | DIN 6921 |
| VESA mount insert | Threaded insert (Helicoil) | M6 × 12mm | SS 304 | 4 | — (installed) | — |
| VESA mount bolt (user) | Hex head bolt | M6 × 16mm | SS 316 | 4 | 5.0 Nm | DIN 933 |
| Sensor bar clamp pivot | Shoulder bolt | M5 × 15mm | SS 316 | 2 | 3.0 Nm | DIN 7379 |
| Cable gland nut | Cable gland | M20 × 1.5 | Nickel-plated brass | 3 | Hand-tight + 1/4 turn | — |
| Battery door latch | Cam latch (quarter-turn) | — | SS 316 | 1 | Hand-operated | — |

**Dissimilar Metal Isolation:**
- All SS-to-Al interfaces: nylon flat washer (1mm thick) between metals
- Prevents galvanic corrosion (SS is cathodic to Al; ΔV ≈ 0.5V in saltwater)
- Nylon washer also provides electrical isolation

### 3.2 Sealing Specifications

| Seal Location | O-ring Size | Material | Cross-section | Compression | Groove Depth |
|---------------|-------------|----------|---------------|-------------|-------------|
| Lid to body | Custom (perimeter) | EPDM, Shore A 70 | 2.62 mm (AS568A) | 18-22% | 2.10 mm |
| Battery door | Ø60 mm | EPDM, Shore A 70 | 2.62 mm | 18-22% | 2.10 mm |
| Cable gland (Ethernet) | Integral to gland | Neoprene | — | Per gland spec | — |
| Cable gland (Power) | Integral to gland | Neoprene | — | Per gland spec | — |
| Cable gland (Sensor) | Integral to gland | Neoprene | — | Per gland spec | — |
| Mic rubber boot | Custom molded | Natural rubber (NR), Shore A 45 | Press-fit, no groove | Interference fit | — |

### 3.3 Connector Specifications

| Connector | Type | Mfr/Part | Rating | Mating Cycles | Pinout |
|-----------|------|----------|--------|---------------|--------|
| Ethernet (external) | RJ45 IP67 | Amphenol RJFTV-2S-S1 | IP67 mated, Cat 5e | 500 | Standard T568B |
| Power (external) | 4-pin circular | Amphenol C091A | IP67 mated, 10A/contact | 500 | Pin 1: V+, Pin 2: V-, Pin 3: Shield, Pin 4: NC |
| Sensor cable (external) | 7-pin circular | Binder 770 series | IP67 mated | 500 | Pin 1-4: Mic 1-4 signal, Pin 5-6: Shield/GND, Pin 7: NC |
| Sensor cable (to bar) | Matching 7-pin | Binder 770 series | IP67 mated | 500 | Matching |
| Internal: Main↔Power | 6-pin header | Molex Micro-Fit 3.0 | 3A/contact | 30 | Pin 1: 5V, 2: 3.3V, 3-4: GND, 5: SDA, 6: SCL |
| Internal: Sensor→Main | 10-pin header | Molex Micro-Fit 3.0 | 3A/contact | 30 | Pin 1-4: Mic 1-4, 5-8: GND, 9: Shield, 10: NC |
| Debug (internal) | SWD 10-pin | Samtec FTSH-105 | — | 25 | ARM SWD standard |

### 3.4 Thermal Interface Specifications

| Interface | TIM | Thickness | Conductivity | Pressure | Component |
|-----------|-----|-----------|-------------|----------|-----------|
| FPGA to standoff | Bergquist GP5000S35 | 0.5 mm | 5.0 W/mK | 50 kPa | iCE40UP5K QFN-48 exposed pad |
| MCU to standoff | Bergquist GP5000S35 | 0.5 mm | 5.0 W/mK | 50 kPa | STM32H743 LQFP-100 via copper pour |
| Standoff to base plate | Metal-to-metal | — | ~200 W/mK (Al) | Bolt preload | Brass standoff to Al base |
| DC-DC inductor to base | Kapton tape (isolation) | 0.05 mm | 0.2 W/mK | — | TPS54331 inductor (minor heat) |

**Thermal budget at 60°C ambient, 15W dissipation:**

```
THERMAL PATH: FPGA → Ambient
═══════════════════════════════

FPGA junction (Tj)
  │  θ_jc = 25°C/W (QFN-48 exposed pad)
  ▼
FPGA case
  │  θ_TIM = 2°C/W (GP5000S35, 5mm² area, 0.5mm thick)
  ▼
Brass standoff top
  │  θ_standoff = 0.5°C/W (brass, Ø6mm × 8mm)
  ▼
Al base plate (internal surface)
  │  θ_base = 0.3°C/W (6mm Al, spreading)
  ▼
Al base plate (external surface)
  │  θ_conv = 5°C/W (natural convection, 250×180mm, horizontal)
  ▼
Ambient (60°C)

Total θ_ja = 25 + 2 + 0.5 + 0.3 + 5 = 32.8°C/W
FPGA power: ~1.5W → ΔT = 1.5 × 32.8 = 49.2°C
Tj_max = 60 + 49.2 = 109.2°C

⚠️ ISSUE: Exceeds 85°C industrial limit!
✅ RESOLUTION: FPGA exposed pad soldered directly to large copper
  pour (20×20mm) → θ_jc reduces to 12°C/W
  Revised: Tj = 60 + 1.5×(12+2+0.5+0.3+5) = 60 + 29.7 = 89.7°C

  Additional: At 60°C ambient, derate FPGA clock to reduce power.
  At typical 40°C: Tj = 40 + 29.7 = 69.7°C ✅

  iCE40UP5K max junction: 100°C. Operating at 89.7°C gives 10.3°C margin.
  Acceptable for short-duration 60°C ambient (MIL-STD-810H high temp test).
```

---

## 4. ELECTRONIC COMPONENT SPECIFICATIONS

### 4.1 Key Components

| Component | Part Number | Package | Key Specs | Alternates | Qty |
|-----------|------------|---------|-----------|-----------|-----|
| MEMS microphone | TDK ICS-40730 | LGA 3.5×2.65mm | SNR 65dB, 164dB SPL, analog out | Knowles SPH0641LU4H | 4 |
| Pre-amplifier | TI OPA1612 | SOIC-8 | 1.1 nV/√Hz, 80MHz GBW | AD8656 | 4 |
| AGC amplifier | ADI AD8338 | LFCSP-16 | 0-80dB gain, 18MHz BW | — | 4 |
| ADC | TI ADS8688 | TSSOP-38 | 8ch, 500kSPS, 16-bit, SPI | ADS8684 (4ch) | 1 |
| FPGA | Lattice iCE40UP5K | QFN-48 | 5,280 LUT, 1Mbit RAM, 48 I/O | iCE40UP3K | 1 |
| MCU | ST STM32H743VIT6 | LQFP-100 | Cortex-M7, 480MHz, 1MB RAM | STM32H753 | 1 |
| Ethernet PHY | Microchip LAN8720A | QFN-24 | 10/100 Mbps, RMII, 3.3V | DP83848 | 1 |
| Ethernet magnetics | Pulse H1102NL | SMD | 100BaseT, 350μH OCL | HanRun HR601680 | 1 |
| SPI Flash | Winbond W25Q128JVSIQ | SOIC-8 | 128Mbit, 104MHz SPI | GD25Q128E | 1 |
| Temperature sensor | TI TMP117 | SOT-563 | ±0.1°C, I2C, -55 to +150°C | MCP9808 | 1 |
| Accelerometer | ST LIS2DH12 | LGA-12 | ±2/4/8/16g, I2C/SPI | ADXL345 | 1 |
| Crystal oscillator | Abracon ASFL1-48.000MHZ | SMD 7×5mm | 48MHz, ±20ppm, -40 to +85°C | Epson SG-210STF | 1 |
| BMS IC | TI BQ76940 | TSSOP-44 | 4-10 cell, integrated protection | — | 1 |
| Charger IC | TI BQ25700A | QFN-32 | 1-4 cell, 12-28V in, NVDC | BQ25713 | 1 |
| Fuel gauge | TI BQ27441 | DSBGA-12 | Impedance track, I2C | MAX17048 | 1 |
| 5V DC-DC | TI TPS54331 | SOIC-8 | 3A, 28V max, 570kHz | LM2596 | 1 |
| 3.3V DC-DC | TI TPS62160 | SOT-23-6 | 1A, ultra-low noise | TPS62162 | 1 |
| TVS (power input) | Littelfuse SMAJ58A | SMA | 58V standoff, 400W | — | 1 |
| Reverse polarity FET | Vishay SI2301CDS | SOT-23 | P-MOSFET, -20V, 2.8A | — | 1 |

### 4.2 Component Temperature Ratings

| Component | Min Temp | Max Temp | Grade | Margin at -10/+60°C |
|-----------|----------|----------|-------|---------------------|
| ICS-40730 | -40°C | +100°C | Automotive | +30°C / +40°C |
| STM32H743 | -40°C | +85°C | Industrial | +30°C / +25°C |
| iCE40UP5K | -40°C | +100°C | Industrial+ | +30°C / +40°C |
| ADS8688 | -40°C | +125°C | Industrial | +30°C / +65°C |
| LAN8720A | -40°C | +85°C | Industrial | +30°C / +25°C |
| Samsung 35E | -20°C | +60°C (charge), +75°C (discharge) | Consumer | +10°C / 0°C ⚠️ |
| BQ76940 | -40°C | +85°C | Industrial | +30°C / +25°C |
| TMP117 | -55°C | +150°C | Industrial | +45°C / +90°C |

**⚠️ Battery thermal limitation:** Samsung 35E charging limited to +60°C. At 60°C ambient, charging should be disabled (BMS programmed accordingly). Discharging OK up to 75°C. This is acceptable: charging typically occurs in shade/shelter, not at peak temperature.

---

## 5. TOLERANCE STACK-UP ANALYSIS

### 5.1 Critical Chain: Mic Position Accuracy

```
TOLERANCE STACK-UP: M1 to M4 total spacing
═══════════════════════════════════════════

Nominal: 3 × 347.0 = 1041.0 mm

Contributing tolerances:
  Extrusion length tolerance:     ±1.0 mm (GEO-01)
  Pocket machining (X):           ±0.2 mm per pocket
  Pocket machining (Z-offset):    ±0.1 mm per offset pocket
  Thermal expansion at ΔT=70°C:   Al CTE 23 ppm × 1041mm × 70°C = 1.68 mm

RSS (Root Sum Square) analysis:
  Static: √(1.0² + 4×0.2² + 2×0.1²) = √(1.0+0.16+0.02) = √1.18 = 1.09 mm
  With thermal: ±1.09 mm static + 1.68 mm thermal shift (systematic)

Impact on TDOA accuracy:
  At 1041mm baseline, ±1.09mm = 0.10% spacing error
  → Position error contribution: ~0.1mm at 1m miss distance
  Thermal expansion: compensated by calibration-free algorithm
  (algorithm uses time-only; does NOT assume fixed geometry)
  The non-coplanar offset RATIO is what matters, not absolute dimensions.

CONCLUSION: Tolerance stack acceptable. ✅
```

### 5.2 Critical Chain: O-ring Compression

```
TOLERANCE STACK-UP: O-ring compression ratio
═════════════════════════════════════════════

O-ring cross-section (AS568A):    2.62 mm ± 0.08 mm
Groove depth:                     2.10 mm ± 0.05 mm
Lid flatness:                     0.05 mm max (machined surface)

Compression = (cord dia - groove depth) / cord dia × 100%

Worst case (max compression): (2.70 - 2.05) / 2.70 = 24.1%
Nominal:                       (2.62 - 2.10) / 2.62 = 19.8%
Worst case (min compression): (2.54 - 2.15) / 2.54 = 15.4%

Required range for IP67: 15-25% compression (EPDM)

Min: 15.4% ≥ 15% ✅
Max: 24.1% ≤ 25% ✅

CONCLUSION: O-ring compression within spec at all tolerance extremes. ✅
```

---

## 6. WORKMANSHIP STANDARDS

| Assembly Type | Standard | Class | Notes |
|---------------|----------|-------|-------|
| PCB assembly (SMT) | IPC-A-610 | Class 2 (Dedicated Service) | Standard for military support equipment |
| PCB assembly (through-hole) | IPC-A-610 | Class 2 | Hand solder where needed |
| Wire harness | IPC/WHMA-A-620 | Class 2 | Internal harness assembly |
| Conformal coating | IPC-CC-830C | Class 3 | Higher class for humidity protection |
| CNC machining | ISO 2768-mK | Medium (m) / Coarse (c) | General tolerances; tighter per drawing |
| Anodizing | MIL-A-8625F | Type III, Class 1 | 25μm minimum for hard anodize |
| Painting | MIL-DTL-53039 | — | 2K polyurethane CARC equivalent |

---

## 7. META-LEARNING SKILL APPLIED

**Skill: Precision Specification**
- Applied "as loose as function allows" principle: general tolerances ±0.5mm, critical TDOA features ±0.1-0.2mm
- Tolerance stack-up analysis on 2 critical chains (mic spacing, O-ring compression)
- Key insight: The calibration-free algorithm compensates for thermal expansion, making absolute spacing tolerance less critical than the non-coplanar Z-offset tolerance
- Vietnamese CNC capability (±0.05mm single-setup) provides comfortable margin on all specified tolerances

---

**Next Step:** [[DECS_E_evaluate_variants]] → Layout variant evaluation

*DECS-D Complete | All critical dimensions specified | 2 tolerance stack-ups analyzed | Thermal budget verified*
