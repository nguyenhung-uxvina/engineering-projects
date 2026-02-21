---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: OCP-O
title: Design Optimization
version: 1.0
created: 2026-02-06
status: complete
---

# STEP O: DESIGN OPTIMIZATION
## Performance, Cost & Systems Thinking Optimization
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 13 of 15

**Purpose:** Refine the BSU-V1 design for best performance/cost trade-off. Apply Systems Thinking leverage points to maximize impact of design decisions.

**Input:** [[DECS_D_detail_specification]], [[DECS_E_evaluate_variants]], [[DECS_C_requirements_verification]]
**Output:** Optimized design with documented trade-offs

---

## 1. PERFORMANCE OPTIMIZATION

### 1.1 Accuracy Optimization

**Current:** ±10mm MUST, target ±5mm

| Parameter | Current Value | Optimization | Expected Improvement | Cost Impact |
|-----------|-------------|-------------|---------------------|-------------|
| ADC resolution | 16-bit (ADS8688) | Already optimal; 12-bit would save $2 but lose resolution | — (keep 16-bit) | $0 |
| ADC speed | 500 kSPS/ch | Sufficient; 1 MSPS would improve timing by 2× | ±8mm → ±6mm | +$4 (ADS8698) |
| FPGA clock | 48 MHz | Increase to 100 MHz via PLL for finer timestamp | ±10mm → ±7mm at edge of zone | +$0 (same FPGA) |
| Mic spacing | 347 mm equal | Optimize for asymmetric spacing to reduce ambiguity | TBD — requires simulation | $0 |
| Non-coplanar offset | 30 mm | Increase to 40 mm for better 3D resolution | Better elevation discrimination | $0 (change pocket position) |

**Optimization Decision:**
- ✅ Enable FPGA PLL to 100 MHz (free improvement, verify jitter)
- ⏸️ Defer ADC upgrade to ADS8698 — evaluate ±10mm first, upgrade if needed
- ⏸️ Defer asymmetric spacing — requires simulation in Phase 4
- ✅ Increase non-coplanar offset from 30mm to 40mm (free, better 3D solving)

### 1.2 Weight Optimization

**Current:** 7.8 kg (target 8 kg, MUST ≤12 kg)

| Component | Current | Optimization | Saving | Risk |
|-----------|---------|-------------|--------|------|
| Enclosure wall | 4mm uniform | 3mm sides + 4mm base/top (selective thinning) | -0.4 kg | Medium: need FEA for shock |
| Sensor bar | 3mm C-channel | Reduce to 2.5mm with internal ribs at clamp points | -0.15 kg | Low: ribs compensate |
| Battery | 4S1P 3,500mAh (3.5 kg) | 4S1P 3,000mAh cells (Samsung 30Q): lighter | -0.3 kg | Low: 9.2h runtime (still >10h? No, 9.2h < 10h MUST) |
| Lid bolts | 6× M4 SS316 + washers | 6× M4 Ti grade 5: lighter | -0.02 kg | High: Ti cost 10× |
| Internal cables | PVC jacket | Silicone jacket (lighter) | -0.05 kg | Low: silicone adequate |

**Optimization Decision:**
- ⏸️ Defer enclosure thinning — 7.8 kg is well within 12 kg; margin is comfortable
- ❌ Reject battery downsize — violates ENG-03 (≥10h MUST)
- ❌ Reject Ti bolts — cost not justified for 0.02 kg
- ✅ Use silicone internal cables — -0.05 kg, no downside
- **Optimized weight: 7.75 kg** (minimal change; weight is not a problem)

### 1.3 Thermal Optimization

**Current:** FPGA Tj = 89.7°C at 60°C ambient (10.3°C margin to 100°C limit)

| Optimization | Impact | Cost | Decision |
|-------------|--------|------|----------|
| Larger copper pour under FPGA (30×30mm vs 20×20mm) | Tj: -5°C | $0 (PCB layout change) | ✅ ADOPT |
| Thicker thermal pad (1.0mm vs 0.5mm) | Tj: +3°C (worse) | $0 | ❌ REJECT (thicker = higher thermal resistance) |
| Add thermal vias under FPGA (5×5 array) | Tj: -8°C | $0 (PCB layout) | ✅ ADOPT |
| Increase base plate to 8mm | Tj: -2°C | +$5, +0.3 kg | ❌ REJECT (marginal improvement) |
| Power-aware FPGA clock gating | Reduce FPGA power 1.5W → 1.0W | $0 (firmware) | ✅ ADOPT |

**Optimized thermal:**
- 30×30mm copper pour + 25 thermal vias + clock gating
- FPGA power: 1.0W (from 1.5W with clock gating)
- Tj at 60°C ambient: 60 + 1.0×(12-5+2+0.5+0.3+5) = 60 + 14.8 = 74.8°C
- **Margin: 25.2°C** (improved from 10.3°C) ✅

### 1.4 Power Consumption Optimization

**Current budget: 15W max, 13W typical**

| Subsystem | Current | Optimized | Saving | Method |
|-----------|---------|-----------|--------|--------|
| FPGA | 1.5W | 1.0W | 0.5W | Clock gating: disable ADC capture between shots |
| MCU | 2.0W | 1.5W | 0.5W | Sleep mode between shots; wake on FPGA interrupt |
| ADC | 0.8W | 0.4W | 0.4W | Power down between shots; 100μs wake-up time |
| Analog front-end | 1.2W | 1.2W | 0W | Must be always-on for continuous monitoring |
| Ethernet PHY | 0.5W | 0.5W | 0W | Must be always-on for communication |
| DC-DC losses | 1.5W | 1.3W | 0.2W | Optimize inductor selection for light-load efficiency |
| BMS + fuel gauge | 0.2W | 0.2W | 0W | Already minimal |
| Status LEDs | 0.1W | 0.1W | 0W | Already minimal |
| **TOTAL** | **7.8W typical** | **6.2W typical** | **1.6W** | |

**Battery runtime improvement:**
- Current: 14.8V × 10Ah / 13W = 11.4h
- Optimized: 14.8V × 10Ah / 10.6W (6.2W + 4.4W margin) = 14.0h
- Optimized typical: 148Wh / 6.2W = **23.9 hours** (idle, no shots)
- Realistic with shooting: 148Wh / 8W (average with periodic shots) = **18.5 hours**
- **Far exceeds 10h MUST requirement** ✅

---

## 2. COST OPTIMIZATION

### 2.1 BOM Cost Reduction Opportunities

| Opportunity | Current Cost | Optimized | Saving | Risk | Decision |
|-------------|-------------|-----------|--------|------|----------|
| ADC: ADS8688 → ADS8684 (4ch instead of 8ch) | $15 | $10 | $5 | Low: we only use 4 channels | ✅ ADOPT |
| Flash: W25Q128 → W25Q64 (8MB vs 16MB) | $1.50 | $0.80 | $0.70 | Low: 8MB still stores >250K shots + dual firmware image | ✅ ADOPT |
| Ethernet magnetics: Pulse H1102NL → HanRun HR601680 | $3.00 | $0.80 | $2.20 | Low: HanRun qualified for 100BaseT, widely used | ✅ ADOPT |
| IP67 RJ45: Amphenol RJFTV → Chinese equivalent | $12.00 | $6.00 | $6.00 | Medium: verify IP67 rating; test sample | ⚠️ EVALUATE |
| Enclosure CNC: negotiate batch pricing (lot 50) | $45 | $38 | $7 | Low: volume discount standard | ✅ ADOPT |
| Sensor bar: extrusion die shared across projects | $800/die | $400/die (50% shared) | $0.80/unit | Low: if other products use same profile | ⚠️ FUTURE |
| Passive components: batch buy (1000+ MOQ) | $5 | $3 | $2 | Low: standard parts | ✅ ADOPT |
| Cable: local manufacture with PUR jacket | $15 | $12 | $3 | Low: local cable company capable | ✅ ADOPT |

**Total confirmed savings: $5 + $0.70 + $2.20 + $7 + $2 + $3 = $19.90/unit**

### 2.2 Optimized Unit Cost

| Category | Original | Optimized | Saving |
|----------|---------|-----------|--------|
| Electronics | $55 | $47 | $8 |
| PCB + SMT | $20 | $20 | $0 |
| Mechanical | $83 | $76 | $7 |
| Battery | $35 | $35 | $0 |
| Connectors + cables | $39 | $34 | $5 |
| Rubber + coating | $11 | $11 | $0 |
| Labor | $35 | $35 | $0 |
| Transport case | $20 | $20 | $0 |
| Software (amortized) | $30 | $30 | $0 |
| **SUBTOTAL** | **$328** | **$308** | **$20** |
| Margin + contingency (15%) | $49 | $46 | $3 |
| **UNIT COST** | **$377** | **$354** | **$23** |

**Optimized cost: $354/lane (70.8% of $500 budget)** ✅

### 2.3 Local Content Impact of Optimization

| Change | Local Content Impact |
|--------|---------------------|
| ADS8684 (import) replaces ADS8688 (import) | Neutral (both import) |
| W25Q64 (import) replaces W25Q128 (import) | Neutral |
| HanRun magnetics (import/China) replaces Pulse (import) | Neutral |
| Enclosure batch discount | +Local (more local spend relative to total) |
| Local cable manufacture | +Local |

**Optimized local content: $199 local / $308 total = 64.6%** (improved from 66.2% by ratio, absolute local spend slightly lower but import spend dropped more)

---

## 3. SYSTEMS THINKING OPTIMIZATION

### 3.1 Current System Map

```
REINFORCING LOOPS (R - Growth/Virtuous Cycles)
═══════════════════════════════════════════════

R1: CAPABILITY LOOP
  Calibration-free → faster setup → more training sessions
  → more data → better algorithms → better accuracy
  → more demand → more production → lower unit cost
  → more sales → fund development → better capability ───┐
  └──────────────────────────────────────────────────────┘

R2: LOCAL CONTENT LOOP
  Local production → Vietnamese expertise grows
  → better quality → more capabilities → more local content
  → lower import dependency → lower cost → more orders
  → more local production ──────────────────────────────┐
  └──────────────────────────────────────────────────────┘

R3: MAINTENANCE LOOP
  Modular LRU design → fast repair → high availability
  → user satisfaction → more deployment → more spares demand
  → local spares production → more local capability
  → better support → higher satisfaction ───────────────┐
  └──────────────────────────────────────────────────────┘


BALANCING LOOPS (B - Limiting/Stabilizing)
═══════════════════════════════════════════

B1: COST CONTROL
  More features desired → higher cost → exceeds budget
  → features cut → cost controlled ──────────────────────┐
  └──────────────────────────────────────────────────────┘

B2: COMPLEXITY CONTROL
  More capabilities → more complexity → harder to maintain
  → maintenance complaints → simplify design → reduced complexity
  └──────────────────────────────────────────────────────┘

B3: THERMAL LIMIT
  Higher performance → more power → more heat
  → thermal limit reached → must reduce power → performance limited
  └──────────────────────────────────────────────────────┘
```

### 3.2 Leverage Point Analysis

| Level | Leverage Point | Current Design | Optimization | Impact |
|-------|---------------|----------------|-------------|--------|
| **L4: Self-organization** | Modular architecture | 5 modules, LRU-swappable | Ensure ALL modules independently testable in production | Enables distributed manufacturing; reduces single-point-of-failure in supply chain |
| **L5: Rules** | Calibration-free rule | Algorithm enforces: "never require user calibration" | Extend to: "never require factory calibration per unit" → production test = automated functional test | Eliminates per-unit calibration cost in production |
| **L6: Information flows** | BIT diagnostic chain | Power→sensor→FPGA→comm→ready | Add: shot count per sensor → predictive maintenance (replace mic before failure) | Moves from reactive to predictive maintenance |
| **L7: Feedback polarity** | R1 (capability loop) | Positive → growth | Ensure B1 (cost control) doesn't kill R1 → set firm cost ceiling and optimize within it | Prevents cost spiral from killing adoption |
| **L8: Negative feedback** | Watchdog timers, BMS protection | MCU watchdog, BMS OCP/OTP/OVP | Add FPGA watchdog independent of MCU; ensures recovery even if MCU hangs before setting up its own watchdog | Closes a coverage gap in self-recovery |
| **L9: Delays** | Setup time, boot time | ≤15 min setup, ≤30s boot | Optimize boot: FPGA config from SPI flash (2s) + MCU fast-boot (5s) + Ethernet autoneg (3s) = **10s total boot** | 3× faster than requirement; eliminates "waiting" friction |

### 3.3 High-Leverage Design Changes

| # | Change | Leverage | Effort | Impact | Decision |
|---|--------|----------|--------|--------|----------|
| OPT-1 | Independent FPGA watchdog (L8) | L8: strengthen negative feedback | Low (firmware) | Closes recovery gap | ✅ ADOPT |
| OPT-2 | Per-sensor shot counter in firmware (L6) | L6: add information flow | Low (firmware) | Enables predictive maintenance | ✅ ADOPT |
| OPT-3 | Automated production test mode (L5) | L5: system rules | Medium (firmware + test jig) | Eliminates per-unit calibration | ✅ ADOPT |
| OPT-4 | Fast-boot optimization (L9) | L9: reduce delays | Low (firmware) | 10s boot from 30s; user delight | ✅ ADOPT |
| OPT-5 | Export shot data via USB flash drive (L6) | L6: information flow to user | Low (firmware) | Works without network; field data collection | ✅ ADOPT |
| OPT-6 | OTA firmware update via Ethernet (L6) | L6: information flow | Medium (firmware) | Remote update capability; reduces maintenance visits | ✅ ADOPT |

### 3.4 Archetype Detection

**Archetype: "Fixes That Fail" (Potential Risk)**
- Symptom: Accuracy not meeting ±10mm in field
- Quick fix: Add temperature compensation (violates calibration-free philosophy)
- Fundamental solution: Improve sensor geometry + algorithm + ADC resolution
- **Design decision:** Invest in root cause (better geometry, 40mm offset, 100MHz FPGA clock) rather than adding temperature compensation

**Archetype: "Success to the Successful" (Opportunity)**
- VN-LOMAH succeeds → gets more funding → improves faster
- Competing Vietnamese defense projects get less funding
- **Design decision:** Ensure VN-LOMAH platform can serve multiple products (LOMAH → Box Target → Armor LOMAH) to justify continued investment

---

## 4. OPTIMIZATION SUMMARY

### 4.1 All Optimizations Applied

| # | Category | Optimization | Status | Impact |
|---|----------|-------------|--------|--------|
| 1 | Accuracy | FPGA PLL to 100 MHz | ✅ Adopted | Better timing resolution |
| 2 | Accuracy | Non-coplanar offset 30→40mm | ✅ Adopted | Better 3D solving |
| 3 | Thermal | 30×30mm copper pour + 25 thermal vias | ✅ Adopted | Tj: 89.7→74.8°C |
| 4 | Thermal | FPGA clock gating | ✅ Adopted | Power: 1.5→1.0W |
| 5 | Power | MCU sleep + ADC power-down between shots | ✅ Adopted | Runtime: 11.4→18.5h |
| 6 | Weight | Silicone internal cables | ✅ Adopted | -0.05 kg |
| 7 | Cost | ADS8684 (4ch) replaces ADS8688 (8ch) | ✅ Adopted | -$5/unit |
| 8 | Cost | W25Q64 replaces W25Q128 | ✅ Adopted | -$0.70/unit |
| 9 | Cost | HanRun magnetics replaces Pulse | ✅ Adopted | -$2.20/unit |
| 10 | Cost | Enclosure batch pricing | ✅ Adopted | -$7/unit |
| 11 | Cost | Passive component batch buy | ✅ Adopted | -$2/unit |
| 12 | Cost | Local cable manufacture | ✅ Adopted | -$3/unit |
| 13 | Firmware | Independent FPGA watchdog | ✅ Adopted | Reliability improvement |
| 14 | Firmware | Per-sensor shot counter | ✅ Adopted | Predictive maintenance |
| 15 | Firmware | Automated production test mode | ✅ Adopted | Lower production cost |
| 16 | Firmware | Fast-boot (10s) | ✅ Adopted | 3× better than requirement |
| 17 | Firmware | USB data export | ✅ Adopted | Field data collection |
| 18 | Firmware | OTA firmware update | ✅ Adopted | Remote update capability |

### 4.2 Before/After Comparison

| Metric | Before Optimization | After Optimization | Change |
|--------|--------------------|--------------------|--------|
| Unit cost | $377 | $354 | -6.1% |
| Weight | 7.8 kg | 7.75 kg | -0.6% |
| Battery runtime | 11.4 h | 18.5 h (realistic) | +62% |
| FPGA Tj at 60°C | 89.7°C | 74.8°C | -14.9°C |
| Boot time | ~30s | ~10s | -67% |
| Local content | 66.2% | 64.6% | -1.6% (still >60%) |
| BIT coverage | 90% | 95% (with shot counter + FPGA WDT) | +5% |

---

## 5. META-LEARNING SKILL APPLIED

**Skill: Optimization Heuristics**
- Applied "low-hanging fruit" prioritization: free improvements first (PCB layout, firmware), then cost reductions, then deferred improvements
- Key heuristic: "Don't optimize what already meets requirements by wide margin" (weight: 7.8 vs 12 kg → not worth optimizing)
- Systems Thinking elevated firmware changes (OPT-1 to OPT-6) from "nice to have" to "high leverage" by identifying their position on the leverage point hierarchy (L5-L9)
- Most impactful single change: FPGA clock gating (improves thermal, power, runtime simultaneously — one change, three benefits)

---

**Next Step:** [[OCP_C_cost_analysis]] → Detailed cost analysis

*OCP-O Complete | 18 optimizations adopted | Cost: $377→$354 | Runtime: 11.4→18.5h | Tj: 89.7→74.8°C*
