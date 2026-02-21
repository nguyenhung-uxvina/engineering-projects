---
project: VN-CUA-001
designation: VDC-100
type: morphological_matrix
phase: 2
step: 3-4
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz (VDI 2221) - Steps 3 & 4
---

# VN-CUA-001: MORPHOLOGICAL MATRIX
## Vietnamese Drone Catcher 100 (VDC-100)
## Ma trận Hình thái - Giai đoạn 2, Bước 3-4

**Project Code:** VN-CUA-001
**Phase:** 2 - Conceptual Design (Steps 3-4: Working Principles Search & Morphological Matrix)
**Date:** 2026-02-08
**Input:** [[02_conceptual/function_structure|Function Structure (18 Sub-Functions)]]

---

# 1. WORKING PRINCIPLES SEARCH

Systematic search for physical/technical principles that can realize each sub-function. Sources: literature, patents, competitive analysis (SkyWall, DroneCatcher, NetGun), brainstorming, and ODI-informed innovation.

---

## 1.1 F1: ACQUIRE TARGET — Working Principles

### F1.1 Detect Target

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P1.1a | **Visual (eyes)** | Operator visual detection | Simple, no electronics, zero latency | Limited range in haze, fatigue | 9 | $0 |
| P1.1b | Radar alert | RF detection of drone | All-weather, automatic detection | Complex, expensive ($5K+), ITAR | 8 | +$5,000 |
| P1.1c | Acoustic sensor | Microphone array detects drone noise | Low cost, passive | Short range (~50m), noisy environments | 6 | +$200 |
| P1.1d | Camera + AI | Video with ML-based drone detection | Auto-detect, record evidence | Processing power, cost, latency | 7 | +$500 |

**Selection rationale:** P1.1a (Visual) selected as primary — aligns with cost constraint and operator-centric design. External detection systems (radar, acoustic) can cue the operator but are not part of the VDC-100 system itself.

### F1.3 Measure Range

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P1.3a | **Laser rangefinder** | Time-of-flight laser pulse | Accurate ±1m, proven COTS | Cost $150-300, Class 1 eye-safe required | 9 | +$200 |
| P1.3b | Stadiametric reticle | Reticle marks vs. known drone size | No electronics, always works | Requires known target size, training | 9 | $0 |
| P1.3c | Radar ranging | RF echo ranging | Multi-target, all-weather | Complex, expensive, ITAR concern | 8 | +$3,000 |
| P1.3d | Estimated (operator) | Operator guesses range | Zero cost, zero electronics | Inaccurate ±30%, poor hit rate | 9 | $0 |

**Selection rationale:** P1.3a (LRF) provides the accuracy needed for O-48 (first-shot hit). The $200 cost is justified by the 15.0 ODI score. P1.3b (stadiametric) as backup for LRF failure.

### F1.4 Calculate Aim Point

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P1.4a | Manual reticle | Operator uses range marks + mental lead | Simple, robust, no electronics | Training intensive, slower | 9 | $0 |
| P1.4b | Ballistic computer | Auto-calculates elevation + lead | Fast, accurate, reduces training | Cost $300+, electronics dependency | 8 | +$400 |
| P1.4c | **Hybrid (LRF+reticle)** | LRF provides range, reticle shows marks | Best accuracy/cost balance | Integration effort | 8 | +$250 |

**Selection rationale:** P1.4c (Hybrid) addresses the #1 ODI outcome. LRF gives precise range, reticle with graduated marks gives the operator a physical reference for elevation and lead — no electronics in the fire control chain.

---

## 1.2 F2: PREPARE SYSTEM — Working Principles

### F2.1 Store Energy

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P2.1a | **HPA (compressed air)** | 0.5L aluminum cylinder @ 300 bar | Clean, refillable, ≥5 shots, proven | Cylinder weight ~1.2 kg, fill station needed | 9 | $80 |
| P2.1b | CO2 cartridge | Disposable 88g or 12g cartridges | Compact, no fill station | Single-use waste, temp sensitive ±20%, 1-2 shots | 9 | $5/shot |
| P2.1c | Blank cartridge | Smokeless powder charge | High energy density, compact | Loud (120+ dB), weapon regulation, Vietnam import | 9 | $3/shot |
| P2.1d | Bungee/spring | Mechanical energy storage | Simple, silent, no consumables | Low energy (~20 m/s max), cocking effort 50+ kg | 7 | $30 |

**Selection rationale:** P2.1a (HPA) is optimal — refillable (low TCO), consistent velocity across shots, silent operation, no weapon regulation, proven in existing C-UAS systems.

### F2.2 Load Projectile

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P2.2a | **Breech loading** | Rear chamber access, drop-in projectile | Fast reload (≤8 sec), simple, robust | Exposes breech mechanism | 9 | $20 |
| P2.2b | Muzzle loading | Front-loading into barrel | Traditional, simple | Slower (15+ sec), must lower weapon | 9 | $10 |
| P2.2c | Magazine feed | Auto-feed from rotary/box magazine | Multi-shot ready, no manual reload | Complexity, weight +1.5 kg, jamming risk | 7 | +$300 |

**Selection rationale:** P2.2a (Breech loading) meets O-55 (reload ≤8 sec) while keeping the system simple and lightweight.

### F2.3 Regulate Energy

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P2.3a | **Mechanical regulator** | Spring-loaded piston pressure reducer (300→100 bar) | Reliable, no electronics, consistent ±3% | Adds weight ~200g, maintenance item | 9 | $60 |
| P2.3b | Fixed orifice | Calibrated restriction in gas line | Simple, cheap, no moving parts | Less precise ±10%, varies with cylinder pressure | 8 | $10 |
| P2.3c | Electronic valve | Solenoid-controlled proportional valve | Precise, can adjust for temp/pressure | Electronics dependency, power needed, cost | 8 | +$150 |

**Selection rationale:** P2.3a (Mechanical regulator) delivers the consistency O-23 demands (14.6 score) without electronic dependency.

---

## 1.3 F3: PROPEL PROJECTILE — Working Principles

### F3.2 Accelerate Projectile

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P3.2a | **Pneumatic tube** | Gas expansion accelerates projectile in barrel | Clean, variable velocity via regulator, quiet | Barrel length determines efficiency | 9 | $40 |
| P3.2b | Pyrotechnic | Powder charge deflagration | High velocity (70+ m/s), compact | Loud (120 dB), regulation, single-use | 9 | $3/shot |
| P3.2c | Spring launcher | Compressed spring release | Silent, no consumables | Low velocity (≤25 m/s), limited range | 7 | $50 |
| P3.2d | Electromagnetic | Rail gun / coil gun | Very high velocity, adjustable | Massive power requirement, TRL 3-4, $10K+ | 4 | +$10,000 |

### F3.3 Guide Projectile (Barrel Type)

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P3.3a | Smoothbore | No rifling, plain tube | Simple manufacturing, lower friction | No spin stabilization | 9 | $0 |
| P3.3b | Rifled barrel | Helical grooves impart spin | Spin stabilization, accuracy | Complex machining, sabot needed, drag | 9 | +$100 |
| P3.3c | **Fin stabilization** | Projectile-mounted fins deploy after muzzle exit | Good stability without barrel complexity | Projectile more complex, fin reliability | 8 | +$15/proj |

**Selection rationale:** P3.3c (Fin stabilization) provides accuracy benefit without requiring an expensive rifled barrel — complexity moves to the projectile which is a consumable anyway.

---

## 1.4 F4: CAPTURE TARGET — Working Principles

### F4.1 Deploy Capture Mechanism

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P4.1a | **Net (projected)** | Net deployed from projectile at target vicinity | Large capture area (3m×3m), proven concept | Timing critical, drag after deploy | 8 | $15/proj |
| P4.1b | Entanglement lines | Weighted cords thrown by spin | Simple, low drag in flight | Smaller capture area (~1.5m) | 7 | $8/proj |
| P4.1c | Bola | Spinning weights on cords | Ancient, proven concept | Limited capture area, tangling | 8 | $5/proj |
| P4.1d | Sticky projectile | Adhesive impact projectile | Direct impact attachment | Requires precise hit (no area effect) | 6 | $10/proj |

### F4.1t Deploy Timing

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P4.1t1 | **Timer** | Pre-set time-delay fuse | Simple, reliable, no electronics needed | Fixed timing — doesn't adapt to range | 9 | $2/proj |
| P4.1t2 | **Barometric** | Altitude/pressure change trigger | Auto-adapts to flight arc apex | Moderate complexity, altitude sensitivity | 7 | $8/proj |
| P4.1t3 | RF command | Radio-triggered deploy | Precise operator control | RF link adds cost/complexity, jamming risk | 8 | +$200 |
| P4.1t4 | Proximity sensor | Sensor detects target proximity | Optimal timing automatically | Complex, expensive ($50+ per projectile) | 6 | +$50/proj |

### F4.2 Entangle Target

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P4.2a | **Net mesh + corner weights** | Woven UHMWPE net with steel weights | Reliable spread, proven, simple | Weight 120g for net alone | 9 | $12/proj |
| P4.2b | Self-tightening net | Drawstring closure activated on contact | Better capture, harder to escape | Complexity, reliability concern | 7 | +$8/proj |
| P4.2c | Simple net (no weights) | Unweighted mesh | Lightest option | Poor spread, unreliable | 8 | $5/proj |

---

## 1.5 F5: RECOVER TARGET — Working Principles

### F5.1 Slow Descent

| Principle ID | Principle | Description | Pros | Cons | TRL | Cost Impact |
|-------------|-----------|-------------|------|------|-----|-------------|
| P5.1a | **Parachute** | Fabric canopy (0.8m diameter) | Proven, gentle descent (3-5 m/s) | Deployment mechanism needed, packing | 9 | $8/proj |
| P5.1b | **Streamer/drogue** | Ribbon or small drogue chute | Simple, reliable deployment, backup role | Less deceleration than full chute | 8 | $3/proj |
| P5.1c | Autorotation | Rotor blades on projectile spin to slow descent | No deployment mechanism | Complex projectile, unreliable | 6 | +$15/proj |
| P5.1d | None (ballistic) | No recovery — free fall | Simplest, lightest | Drone damage on impact (evidence lost), safety risk | 9 | $0 |

**Selection rationale:** P5.1a (Parachute) as primary, P5.1b (Drogue) as backup — dual redundancy addresses O-63 evidence preservation concern.

---

# 2. MORPHOLOGICAL MATRIX

## 2.1 Matrix Structure

The morphological matrix combines all sub-functions (rows) with their working principles (columns). Concept paths are traced through the matrix.

| Sub-Function | Solution 1 | Solution 2 | Solution 3 | Solution 4 |
|--------------|------------|------------|------------|------------|
| **F1.1 Detect target** | **Visual (eyes)** | Acoustic sensor | Radar alert | Camera + AI |
| **F1.3 Measure range** | **Laser rangefinder** | Stadiametric reticle | Radar ranging | Estimated |
| **F1.4 Calculate aim** | Manual reticle | Ballistic computer | **Hybrid (LRF+reticle)** | — |
| **F2.1 Store energy** | **HPA cylinder** | CO2 cartridge | **Blank cartridge** | Bungee/spring |
| **F2.2 Load projectile** | **Breech loading** | Muzzle loading | Magazine feed | — |
| **F2.3 Regulate energy** | **Mechanical regulator** | Fixed orifice | Electronic valve | — |
| **F3.2 Accelerate** | **Pneumatic tube** | **Pyrotechnic** | Spring launcher | EM launcher |
| **F3.3 Guide** | Smoothbore | Rifled barrel | **Fin-stabilized** | — |
| **F4.1 Deploy capture** | **Projected net** | Entanglement lines | Bola | Sticky |
| **F4.1t Deploy timing** | **Timer** | **Barometric** | RF command | Proximity |
| **F4.2 Entangle** | **Mesh + weights** | Self-tightening | Simple net | — |
| **F5.1 Slow descent** | **Parachute** | **Drogue/streamer** | Autorotation | None |

**Total theoretical combinations:** 4 × 4 × 3 × 4 × 3 × 3 × 4 × 3 × 4 × 4 × 3 × 4 = **2,654,208 possible concepts**

**Practical concepts after compatibility screening:** 4 (see Section 3)

---

## 2.2 Compatibility Check

Not all principle combinations are physically compatible. Key incompatibilities:

| Combination | Issue | Resolution |
|-------------|-------|------------|
| Pyrotechnic + Electronic valve | No gas to regulate | Use fixed charge — no regulator needed |
| Magazine feed + Muzzle loading | Contradictory loading methods | Choose one |
| RF command deploy + Jam-proof | RF is jammable | Timer or barometric for jam-proof designs |
| Spring launcher + 80m range | Insufficient velocity (<25 m/s) | Eliminate from long-range concepts |
| Bola + Parachute | Bola has no projectile body for chute | Separate recovery needed |
| EM launcher + Man-portable | Power supply too heavy | Eliminate |

---

# 3. CONCEPT GENERATION

Four viable concepts generated by tracing compatible paths through the morphological matrix:

## 3.1 Concept A: "VDC-100 BASIC" (Simplified SkyWall)

```
MORPHOLOGICAL PATH — CONCEPT A
═══════════════════════════════════════════════════════════════════════════════

F1.1  [ Visual ●]  Acoustic    Radar      Camera
F1.3  [ LRF ●]     Stadiametric  Radar    Estimated
F1.4    Manual    [ Ballistic   [ Hybrid ●]
F2.1  [ HPA ●]     CO2         Blank      Bungee
F2.2  [ Breech ●]  Muzzle      Magazine
F2.3  [ Mech Reg ●]  Fixed     Electronic
F3.2  [ Pneumatic ●]  Pyro     Spring     EM
F3.3  [ Smoothbore ●]  Rifled  Fin-stab
F4.1  [ Net ●]     Lines       Bola       Sticky
F4.1t [ Timer ●]   Barometric  RF         Proximity
F4.2  [ Mesh+wt ●] Self-tight  Simple
F5.1  [ Parachute ●] Drogue   Autorot    None

═══════════════════════════════════════════════════════════════════════════════
```

| Attribute | Value |
|-----------|-------|
| **Name** | VDC-100 BASIC |
| **Philosophy** | Maximum simplicity — fewest components, lowest risk |
| **Detection** | Operator visual + LRF for range |
| **Targeting** | Ballistic reticle with range marks (manual lead calculation) |
| **Propulsion** | HPA pneumatic (300→100 bar regulated) |
| **Barrel** | Smoothbore aluminum, 800mm |
| **Projectile** | Net with corner weights, timer deploy, parachute |
| **Key Advantages** | Simple, proven technology (TRL 8-9), no RF (jam-proof), low cost (~$1,600 production), high reliability |
| **Key Limitations** | Manual lead calculation (training intensive), fixed timer deploy (less adaptive), basic accuracy (~60% first-shot at 50m moving) |
| **Estimated Production Cost** | ~$1,600 |
| **Estimated Weight** | ~7.5 kg |
| **Risk Level** | LOW |

---

## 3.2 Concept B: "VDC-100 ENHANCED" (ODI-Optimized)

```
MORPHOLOGICAL PATH — CONCEPT B
═══════════════════════════════════════════════════════════════════════════════

F1.1  [ Visual ●]  Acoustic    Radar      Camera
F1.3  [ LRF ●]     Stadiametric  Radar    Estimated
F1.4    Manual      Ballistic  [ Hybrid ●]
F2.1  [ HPA ●]     CO2         Blank      Bungee
F2.2  [ Breech ●]  Muzzle      Magazine
F2.3  [ Mech Reg ●]  Fixed     Electronic
F3.2  [ Pneumatic ●]  Pyro     Spring     EM
F3.3    Smoothbore  Rifled     [ Fin-stab ●]
F4.1  [ Net ●]     Lines       Bola       Sticky
F4.1t [ Timer ●] + [ Barometric ●]  RF    Proximity
F4.2  [ Mesh+wt ●] Self-tight  Simple
F5.1  [ Parachute ●] + [ Drogue ●] Autorot  None

═══════════════════════════════════════════════════════════════════════════════
```

| Attribute | Value |
|-----------|-------|
| **Name** | VDC-100 ENHANCED |
| **Philosophy** | ODI-optimized — best balance of top outcomes vs. cost/complexity |
| **Detection** | Operator visual + LRF with digital range display |
| **Targeting** | Ballistic reticle with range marks + lead angle marks (LRF-fed) |
| **Propulsion** | HPA pneumatic with fast-acting valve |
| **Barrel** | Smoothbore aluminum, 800mm |
| **Projectile** | Fin-stabilized, net with corner weights, timer + barometric backup |
| **Recovery** | Parachute with drogue backup (dual redundancy) |
| **Key Advantages** | Optimized for top ODI outcomes, better first-shot hit (fins + calibrated reticle), dual deploy redundancy (timer + barometric), improved accuracy (~70% at 50m moving), still no RF (jam-proof) |
| **Key Limitations** | Slightly higher cost (~$1,800 production), fin-stabilized projectile more complex |
| **Estimated Production Cost** | ~$1,800 |
| **Estimated Weight** | ~7.8 kg |
| **Risk Level** | LOW-MEDIUM |

**ODI Optimization Details:**

| ODI Outcome | How Concept B Addresses It |
|-------------|---------------------------|
| O-48: First-shot hit (15.0) | LRF + graduated reticle + fin stabilization |
| O-23: Reliability (14.6) | Mechanical regulator, no electronics in fire chain |
| O-46: Range (13.5) | Fin stabilization maintains accuracy at 80m |
| O-43: Net deploy (13.5) | Timer + barometric dual-redundancy |
| O-55: Reload (12.5) | Fast breech loading ≤8 sec |
| O-63: Evidence (13.0) | Parachute + drogue dual-redundancy |

---

## 3.3 Concept C: "VDC-100 PRO" (Maximum Capability)

```
MORPHOLOGICAL PATH — CONCEPT C
═══════════════════════════════════════════════════════════════════════════════

F1.1    Visual      Acoustic    Radar     [ Camera ●]
F1.3  [ LRF ●]     Stadiametric  Radar    Estimated
F1.4    Manual    [ Ballistic ●]  Hybrid
F2.1  [ HPA ●]     CO2         Blank      Bungee
F2.2    Breech      Muzzle    [ Magazine ●]
F2.3    Mech Reg    Fixed     [ Electronic ●]
F3.2  [ Pneumatic ●]  Pyro     Spring     EM
F3.3    Smoothbore  Rifled    [ Fin-stab ●]
F4.1  [ Net ●]     Lines       Bola       Sticky
F4.1t   Timer       Barometric [ RF ●]    Proximity
F4.2    Mesh+wt   [ Self-tight ●] Simple
F5.1  [ Parachute ●] Drogue   Autorot    None

═══════════════════════════════════════════════════════════════════════════════
```

| Attribute | Value |
|-----------|-------|
| **Name** | VDC-100 PRO |
| **Philosophy** | Maximum performance — technology-forward, highest capability |
| **Detection** | Operator visual + camera-assisted display |
| **Targeting** | Ballistic computer with auto-lead calculation |
| **Propulsion** | HPA pneumatic with electronic valve control |
| **Loading** | 3-round rotary magazine for rapid follow-up |
| **Projectile** | Fin-stabilized, smart net with RF-triggered deploy |
| **Capture** | Self-tightening net mechanism |
| **Recovery** | Parachute |
| **Key Advantages** | Highest accuracy (~85% at 50m), multi-shot without reload, computer-assisted reduces training, optimal capture timing (RF trigger) |
| **Key Limitations** | High cost (~$3,500 production → $9,000 selling), RF vulnerable to jamming, complex electronics = lower reliability, heavier (~10 kg), lower local content (~50%) |
| **Estimated Production Cost** | ~$3,500 |
| **Estimated Weight** | ~10 kg |
| **Risk Level** | HIGH |

---

## 3.4 Concept D: "VDC-100 PYRO" (Blank Cartridge Alternative)

```
MORPHOLOGICAL PATH — CONCEPT D
═══════════════════════════════════════════════════════════════════════════════

F1.1  [ Visual ●]  Acoustic    Radar      Camera
F1.3  [ LRF ●]     Stadiametric  Radar    Estimated
F1.4    Manual      Ballistic  [ Hybrid ●]
F2.1    HPA         CO2       [ Blank ●]   Bungee
F2.2  [ Breech ●]  Muzzle      Magazine
F2.3    (N/A — fixed charge, no regulation needed)
F3.2    Pneumatic [ Pyro ●]    Spring     EM
F3.3  [ Smoothbore ●]  Rifled  Fin-stab
F4.1  [ Net ●]     Lines       Bola       Sticky
F4.1t [ Timer ●]   Barometric  RF         Proximity
F4.2  [ Mesh+wt ●] Self-tight  Simple
F5.1  [ Parachute ●] Drogue   Autorot    None

═══════════════════════════════════════════════════════════════════════════════
```

| Attribute | Value |
|-----------|-------|
| **Name** | VDC-100 PYRO |
| **Philosophy** | Alternative energy source — compact, high velocity, no gas system |
| **Detection** | Operator visual + LRF |
| **Targeting** | Ballistic reticle (same as Concept A) |
| **Propulsion** | Blank cartridge (smokeless powder) |
| **Barrel** | Smoothbore steel, 600mm (shorter due to higher pressure) |
| **Projectile** | Net with timer deploy, standard parachute |
| **Key Advantages** | Higher muzzle velocity (50+ m/s), compact system (no gas cylinder), lighter (~6 kg), simpler logistics (cartridges vs gas refill) |
| **Key Limitations** | Loud report (120+ dB tactical signature), weapon regulation in Vietnam, temperature sensitivity ±15%, single-use cartridges (higher per-shot cost), less precise velocity control |
| **Estimated Production Cost** | ~$1,400 |
| **Estimated Weight** | ~6 kg |
| **Risk Level** | MEDIUM (regulatory risk) |

---

# 4. CONCEPT COMPARISON OVERVIEW

## 4.1 Side-by-Side Comparison

| Parameter | A: Basic | B: Enhanced | C: Pro | D: Pyro |
|-----------|----------|-------------|--------|---------|
| **Production cost** | $1,600 | $1,800 | $3,500 | $1,400 |
| **Selling price** | ~$4,800 | ~$5,400 | ~$9,000 | ~$4,200 |
| **Weight** | 7.5 kg | 7.8 kg | 10 kg | 6 kg |
| **Muzzle velocity** | 60 m/s | 60 m/s | 60 m/s | 70 m/s |
| **Effective range** | 80m | 80m | 100m | 90m |
| **1st shot hit (50m)** | ~60% | ~70% | ~85% | ~60% |
| **Reload time** | 10 sec | 8 sec | 2 sec (mag) | 12 sec |
| **Net deploy** | Timer | Timer+Baro | RF command | Timer |
| **Recovery** | Parachute | Chute+Drogue | Parachute | Parachute |
| **Noise** | Silent | Silent | Silent | LOUD |
| **Jam-proof** | Yes | Yes | No (RF) | Yes |
| **Local content** | ~75% | ~72% | ~50% | ~70% |
| **Component count** | ~60 | ~75 | ~120 | ~55 |
| **TRL (system)** | 8 | 7-8 | 6-7 | 8 |
| **Development risk** | Low | Low-Med | High | Med |

## 4.2 Concept Positioning Map

```
CONCEPT POSITIONING — COST vs. CAPABILITY
═══════════════════════════════════════════════════════════════════════════════

HIGH   │                                        ┌───────────┐
       │                                        │  C: PRO   │
       │                                        │  $9,000   │
       │                                        │  85% hit  │
  C    │                                        └───────────┘
  A    │
  P    │              ┌───────────┐
  A    │              │ B: ENHANCED│  ◄── SWEET SPOT (ODI optimized)
  B    │              │  $5,400   │
  I    │              │  70% hit  │
  L    │              └───────────┘
  I    │
  T    │  ┌───────────┐           ┌───────────┐
  Y    │  │ A: BASIC  │           │ D: PYRO   │
       │  │  $4,800   │           │  $4,200   │
       │  │  60% hit  │           │  60% hit  │
LOW    │  └───────────┘           └───────────┘
       │
       └──────────────────────────────────────────────────────
       LOW                                               HIGH
                              COST

═══════════════════════════════════════════════════════════════════════════════
```

---

# 5. CONCEPT SCREENING (Go / No-Go)

Pre-filter concepts before VDI 2225 evaluation:

| Screening Criterion | Threshold | A: Basic | B: Enhanced | C: Pro | D: Pyro |
|--------------------|-----------|----------|-------------|--------|---------|
| Price ≤ $6,000 | MUST | ✅ $4,800 | ✅ $5,400 | ❌ $9,000 | ✅ $4,200 |
| Weight ≤ 8 kg | MUST | ✅ 7.5 | ✅ 7.8 | ❌ 10 | ✅ 6 |
| Local content ≥ 60% | MUST | ✅ 75% | ✅ 72% | ⚠️ 50% | ✅ 70% |
| No weapon regulation issues | SHOULD | ✅ | ✅ | ✅ | ⚠️ Pyrotechnic |
| **SCREENING RESULT** | | **PASS** | **PASS** | **FAIL** | **CONDITIONAL** |

**Note:** Concept C fails two MUST requirements (price, weight) — it will still be evaluated by VDI 2225 for completeness but cannot be selected. Concept D has a regulatory risk that may be mitigatable.

---

# DOCUMENT LINKS

- [[02_conceptual/function_structure|Function Structure (Step 2)]]
- [[02_conceptual/concept_evaluation|Concept Evaluation (Step 5)]] ← NEXT
- [[01_requirements/requirements_list|Requirements List]]
- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery]]

---

*This morphological matrix follows Pahl & Beitz Steps 3-4, systematically searching working principles for 18 sub-functions and combining them into 4 viable concepts through the morphological matrix method.*
