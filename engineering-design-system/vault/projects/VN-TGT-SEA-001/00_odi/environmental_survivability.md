---
project: VN-TGT-SEA-001
phase: 0
type: environmental_survivability
version: 2.1
created: 2026-02-10
updated: 2026-02-10
revision: B.1
status: draft
---

# Phase 0 Revision: Environmental Survivability Analysis

> **Rev B.1** — Updated for 8.0m platform (was 6.0m), superstructure REMOVED, IR/propane REMOVED (radar-only), reflectors elevated to 3-4m on 8× steel masts (60mm×4mm galv tube). Displacement 980 kg (was 800 kg). Key calculations revised.

**Purpose:** Redefine "survivability" from ballistic (TPMS, 50+ hits) to environmental (SS 5-6, Bft 6-7, 2-3 days anchored), per user directive
**Scope:** Towing, mooring, structural, stability, subsystem endurance for harsh sea conditions
**Key change:** O-57 reinterpretation — target must survive WEATHER, not BULLETS

---

## 1. Redefining Survivability — Operational Concept

### 1.1 Previous Definition (Superseded)

> "Target survives 50+ hits (12.7mm AP) without sinking, enabled by PA12 TPMS flotation core with ~36,000 sealed cells. Requires ~7,200 hits to sink."

This definition optimized for POST-ENGAGEMENT survival (reusability after hits). The TPMS flotation core was the primary innovation, enabling 5-10 reuse cycles per target.

### 1.2 Revised Definition (Active)

> "Target can be TOWED to anchor position in Sea State 5-6, remain ANCHORED for 2-3 days in SS 5-6 with wind force Beaufort 6-7, and STILL meet all conditions for anti-ship missile live-fire acceptance testing at sea."

This definition optimizes for PRE-ENGAGEMENT READINESS in harsh weather. The key challenge shifts from "damage tolerance" to "seakeeping + station-keeping + operational availability."

### 1.3 Why This Change Matters

| Aspect | Old (Ballistic) | New (Environmental) |
|--------|-----------------|---------------------|
| **Core question** | Can it survive hits? | Can it survive weather? |
| **Scenario** | After missile hit, target reusable | Before missile fires, target still functional |
| **Duration** | Seconds (ballistic event) | Days (2-3 days at anchor) |
| **Loading** | Point impact (12.7mm AP) | Distributed cyclic (waves, wind, current) |
| **Key subsystem** | TPMS flotation core ($10-25K) | Mooring system + structural integrity |
| **Innovation driver** | AM cellular material science | Marine engineering fundamentals |
| **Operational reality** | Navy doesn't reuse missile targets | Navy deploys days before test window |

### 1.4 Revised Operational Concept

```
OPERATIONAL TIMELINE (Revised for SS 5-6)
═══════════════════════════════════════════════════════

Day -7 to -3:  Pre-deploy mooring (anchor + chain + pickup buoy)
               ► Done in fair weather (SS 2-3)
               ► Mooring system sized for SS 6 survival

Day -2 to -1:  Tow target to mooring point
               ► Acceptable in SS 4-5 (not SS 6)
               ► Connect to pre-deployed mooring pickup
               ► Activate GPS beacon (72h battery)
               ► Depart

Day -1 to 0:   Target anchored, awaiting test window
               ► Survives SS 5-6, wind Bft 6-7
               ► All subsystems maintain readiness
               ► GPS beacon confirms position and status

Day 0:          Test execution
               ► Weather window ≥ SS 4 (for firing ship ops)
               ► Activate IR system (timer or remote)
               ► Confirm RCS/IR active via measurement
               ► Fire missile → engagement
               ► Target destroyed (expendable after hit)

Day +1:         Cleanup
               ► Debris recovery
               ► Mooring recovery (if reusable)
```

**Key insight:** The mooring system is pre-deployed in fair weather. The target tow occurs in moderate-to-rough seas (SS 4-5). The target then endures 1-3 days at anchor in SS 5-6 waiting for the optimal test window. This is realistic Vietnamese Navy operations during the northeast monsoon season (October-March), when SS 5-6 is common in the Vietnam East Sea.

---

## 2. Environmental Conditions — Quantified

### 2.1 Sea State Parameters

| Parameter | SS 3 (Previous) | SS 5 (Design) | SS 6 (Survival) | Source |
|-----------|-----------------|---------------|-----------------|--------|
| **Significant wave height (Hs)** | 0.5-1.25 m | 2.5-4.0 m | 4.0-6.0 m | WMO Sea State Scale |
| **Peak wave period (Tp)** | 3-5 s | 6-8 s | 8-10 s | Deep-water correlation |
| **Wavelength (Lp)** | 14-39 m | 56-100 m | 100-156 m | Lp = 1.56 × Tp² |
| **Max wave height (Hmax)** | 2.0 m | 6.4 m | 9.6 m | Hmax ≈ 1.6 × Hs |
| **Wave orbital velocity (surface)** | 0.5 m/s | 1.1-1.6 m/s | 1.6-2.4 m/s | v = π × Hs / Tp |
| **Wave steepness (Hs/Lp)** | 1/30 | 1/22-1/25 | 1/25 | Moderate steepness |

### 2.2 Wind Parameters

| Parameter | Bft 5 (Previous) | Bft 6 (Design) | Bft 7 (Survival) | Source |
|-----------|------------------|----------------|------------------|--------|
| **Mean wind speed** | 17-21 kn (8.7-10.8 m/s) | 22-27 kn (11.3-13.9 m/s) | 28-33 kn (14.4-17.0 m/s) | Beaufort Scale |
| **Gust speed (1.4×)** | 24-29 kn | 31-38 kn | 39-46 kn | Gust factor 1.4 |
| **Dynamic pressure** | 46-72 Pa | 78-118 Pa | 127-177 Pa | q = 0.5 × ρ × V² |

### 2.3 Current (Vietnamese Coastal)

| Parameter | Value | Source |
|-----------|-------|--------|
| Typical tidal current | 0.5-1.5 kn (0.26-0.77 m/s) | Vietnamese coastal data |
| Storm-enhanced current | up to 2.0 kn (1.03 m/s) | Combined wind + tidal |
| Current direction | Variable (tidal reversal every ~6h) | Diurnal tidal pattern |

### 2.4 Platform vs Wavelength

```
PLATFORM-TO-WAVE RATIO
═══════════════════════════════════════════════════════

Platform diameter: D = 8.0 m

                    Wavelength (Lp)    D/Lp    Behavior
SS 3 (Tp=4s):      24 m              0.33     Some wave reflection
SS 5 (Tp=7s):      76 m              0.11     Wave follower (rides waves)
SS 6 (Tp=9s):      126 m             0.06     Wave follower (rides waves)

When D/Lp < 0.2, the platform follows the wave surface like a cork.
It heaves, pitches, and rolls WITH the waves, not AGAINST them.

This is GOOD for survivability (no wave impact forces on hull)
but means the platform motion is large (±Hs/2 heave).
```

---

## 3. Towing Analysis

### 3.1 Tow Resistance

```
TOW RESISTANCE — 8m CIRCULAR PONTOON (Rev B.1)
═══════════════════════════════════════════════════════

Calm water tow resistance:
  R = 0.5 × ρ_water × C_d × A_frontal × V_tow²

  ρ_water = 1,025 kg/m³
  C_d = 1.5 (flat circular face, no streamlining)
  A_frontal = D × draft = 8.0 × 0.5 m = 4.0 m²
  (using hull depth 0.5m, not waterline draft)

  At 3 kn (1.54 m/s): R = 0.5 × 1025 × 1.5 × 4.0 × 1.54² = 7,288 N = 743 kgf
  At 4 kn (2.06 m/s): R = 0.5 × 1025 × 1.5 × 4.0 × 2.06² = 12,968 N = 1,322 kgf
  At 5 kn (2.57 m/s): R = 0.5 × 1025 × 1.5 × 4.0 × 2.57² = 20,200 N = 2,061 kgf

Added wave resistance (SS 5, Hs=3m):
  Factor: 1.5-2.0× calm water resistance
  At 3 kn in SS 5: R_total = 743 × 1.8 = 1,337 kgf

Peak dynamic tow load (wave slam + surge):
  Factor: 2.5-3.0× mean resistance
  Peak at 3 kn in SS 5: R_peak = 1,337 × 2.5 = 3,343 kgf
```

### 3.2 Tow Line Specification

| Parameter | Requirement | Selection |
|-----------|-------------|-----------|
| Peak tow load | 3,343 kgf (SS 5, 3 kn) | Design load |
| Safety factor | 3:1 | Marine standard |
| Required SWL | 10,029 kgf | |
| **Recommendation** | **20mm Dyneema (HMPE)** | **SWL 12,000 kgf** |
| Alternative | 28mm polyester double-braid | SWL 6,000 kgf (insufficient for 3:1) |
| Length | 50-100 m | Wave damping in catenary |
| Cost | $300-500 (polyester) / $800-1,200 (Dyneema) | |

**Note (Rev B.1):** 8.0m platform increases peak tow load to 3,343 kgf. Required SWL at 3:1 is 10,029 kgf. 20mm Dyneema (SWL 12,000 kgf) is the only adequate option. Polyester lines do not meet the 3:1 safety factor.

### 3.3 Tow Stability

**Problem:** A circular pontoon has NO directional stability under tow. It will yaw wildly, loading the tow line asymmetrically and risking capsize or tow line failure.

> **Rev B.1:** 8.0m platform has even worse directional stability than 6.0m. Drogue + bridle tow remains essential. Consider towing alongside for short distances.

**Mitigation options:**

| Solution | Effectiveness | Cost | Complexity |
|----------|--------------|------|------------|
| **Drogue (sea anchor) astern** | HIGH — provides directional drag | $200-500 | LOW — deploy from stern cleat |
| Bridle tow (2-point attachment) | MEDIUM — reduces yaw | $100 | LOW — 2 attachment points |
| Skeg (fixed fin) on bottom | HIGH — passive directional stability | $500 | MEDIUM — permanent modification |
| Tow alongside (lashed to tug) | HIGH — eliminates towing issues | $0 | HIGH — weather-limited |

**Recommendation:** Use drogue + bridle tow combination. Drogue deploys from stern, bridle attaches to two points on leading edge of pontoon at 60° spread. This provides both directional stability and reduces yaw to ±10° in SS 5.

### 3.4 Tow Speed Limitations

| Sea State | Max Safe Tow Speed | Notes |
|-----------|-------------------|-------|
| SS 3 | 5-6 kn | Normal tow |
| SS 4 | 4-5 kn | Moderate wave resistance |
| SS 5 | **3 kn** | **Heavy loading, frequent spray** |
| SS 6 | **1-2 kn** | **DANGEROUS — avoid if possible** |

**Operational recommendation:** Tow target in SS 4-5 maximum. If SS 6 is forecast, either:
- Deploy earlier (before weather deteriorates)
- Pre-deploy mooring and wait for brief weather window to tow target to mooring point
- Tow from closer staging point (reduce tow distance)

### 3.5 Tow Distance and Time

| Scenario | Distance | Speed (SS 5) | Time | Fuel Cost |
|----------|----------|-------------|------|-----------|
| Near-shore range (15 km offshore) | 15 nm | 3 kn | 5 hr | $500 |
| Offshore range (30 km) | 16 nm | 3 kn | 5.3 hr | $700 |
| Far offshore (50 km) | 27 nm | 3 kn | 9 hr | $1,200 |

**Note:** Vietnamese Navy missile test ranges in the Vietnam East Sea are typically 20-50 km offshore, in water depths of 20-80 m. Tow time of 5-9 hours in SS 5 is feasible for a day operation.

---

## 4. Mooring System Redesign

### 4.1 Force Analysis — SS 5-6 Conditions

```
MOORING FORCE ANALYSIS
═══════════════════════════════════════════════════════

1. WIND FORCE (dominant force for shallow-draft platform)
   F_wind = 0.5 × ρ_air × C_d × A_windage × V²

   Windage area: superstructure + reflectors
     Platform with reflectors: ~6m wide × 2.5m high
     Average projected area (circular): ~9 m²
     With superstructure silhouette: 12 m² maximum
     Use: A = 12 m² (conservative, broadside)

   C_d = 1.2 (bluff body)
   ρ_air = 1.225 kg/m³

   Bft 6 (12.6 m/s):  F = 0.5 × 1.225 × 1.2 × 12 × 12.6² = 1,400 N = 143 kgf
   Bft 7 (15.7 m/s):  F = 0.5 × 1.225 × 1.2 × 12 × 15.7² = 2,176 N = 222 kgf
   Bft 7 gust (22 m/s): F = 0.5 × 1.225 × 1.2 × 12 × 22² = 4,267 N = 435 kgf

2. CURRENT FORCE
   F_current = 0.5 × ρ_water × C_d × A_underwater × V_current²

   A_underwater = D × draft ≈ 6.0 × 0.05 m = 0.3 m² (very small draft!)
   Plus pontoon bottom friction: negligible for circular flat shape
   C_d = 1.0
   V_current = 0.77 m/s (1.5 kn)

   F_current = 0.5 × 1025 × 1.0 × 0.3 × 0.77² = 91 N = 9 kgf
   → Negligible due to extremely shallow draft

3. WAVE DRIFT FORCE
   For D/Lp = 0.05-0.08 (platform much smaller than wavelength):
   The platform transmits most wave energy rather than reflecting it.
   Mean drift force is small for a shallow-draft body.

   Estimate: F_drift ≈ ρ × g × Hs² × D / 16
   SS 5 (Hs=3m): F = 1025 × 9.81 × 9 × 6 / 16 = 33,888 N

   BUT this formula is for a vertical wall spanning full water depth.
   For a surface-following pontoon with 5cm draft: correction factor ~0.01-0.05
   F_drift (SS 5) ≈ 33,888 × 0.03 = 1,017 N = 104 kgf
   F_drift (SS 6) ≈ (Hs=5): 33,888 × (25/9) × 0.03 = 2,824 N = 288 kgf

4. TOTAL STEADY-STATE MOORING LOAD

   ┌───────────────────────────────────────────────────┐
   │ Condition      │ Wind  │ Current │ Drift │ Total  │
   │────────────────│───────│─────────│───────│────────│
   │ SS 5, Bft 6    │ 143   │ 9       │ 104   │ 256 kgf│
   │ SS 5, Bft 7    │ 222   │ 9       │ 104   │ 335 kgf│
   │ SS 6, Bft 7    │ 222   │ 9       │ 288   │ 519 kgf│
   │ SS 6, Bft 7 gust│435   │ 9       │ 288   │ 732 kgf│
   └───────────────────────────────────────────────────┘

5. DYNAMIC PEAK LOAD
   Chain catenary absorbs most dynamic oscillation.
   Residual dynamic amplification factor: 1.5-2.0 (with chain catenary)
   Without chain (taut mooring): factor 3.0-5.0

   Design peak load (SS 6, Bft 7 gust, with catenary):
   F_peak = 732 × 2.0 = 1,464 kgf

   Safety factor: 3:1 → Required mooring system SWL: 4,392 kgf
```

> **Rev B.1 REVISED FORCES (8.0m platform, no superstructure, mast-mounted reflectors):**
> - Windage area: 10 m² (8× elevated reflectors + masts, NO superstructure — was 12 m² with superstructure)
> - Wind Bft 7 steady: **185 kgf** (was 222 kgf — reduced windage area)
> - Wind Bft 7 gust: **363 kgf** (was 435 kgf)
> - Wave drift SS 5: **138 kgf** (was 104 kgf — larger 8.0m platform)
> - Wave drift SS 6: **384 kgf** (was 288 kgf)
> - Current: ~10 kgf (unchanged)
> - **Total steady SS 6, Bft 7: 578 kgf** (was 519 kgf)
> - **Total gust SS 6, Bft 7: 757 kgf** (was 732 kgf)
> - **Peak dynamic (×2.0): 1,512 kgf** (was 1,464 kgf)
> - **Required SWL (×3): 4,536 kgf** (was 4,392 kgf)
> - Chain: 12-16mm G30 (TBD Phase 2). 16mm WLL 3,000 kgf adequate for steady-state.

### 4.2 Mooring Configurations by Water Depth

```
MOORING DESIGN: DEPTH-DEPENDENT
═══════════════════════════════════════════════════════

Configuration A: SHALLOW WATER (10-20 m depth)
─────────────────────────────────────────────────
  Scope: 7:1 (storm)
  Chain: 12mm G30, 70-140 m long
  Weight: 175-350 kg chain
  Anchor: Danforth 30 kg (sand/mud, holding 600 kgf)
         or Bruce 20 kg (any bottom, holding 400 kgf)
  Total mooring weight: 200-380 kg
  Cost: $1,500-2,500

  ┌─Surface─────────────────────────────────────────┐
  │  ⛵ Target                                       │
  │   │                                              │
  │   │ Scope 7:1                                    │
  │   │ (chain catenary curve)                       │
  │───┘                                              │
  │   ⌇⌇⌇⌇ chain on seabed ⌇⌇⌇⌇ ⚓ Danforth       │
  └─Seabed──────────────────────────────────────────┘
  Depth: 10-20 m
  Swing radius: 67-137 m

Configuration B: MEDIUM DEPTH (20-50 m)
─────────────────────────────────────────────────
  Scope: 5:1 (with rope section, effective catenary scope)
  Chain: 12mm G30, 30 m (ground tackle near anchor)
  Rode: 20mm polyester double-braid, 80-220 m
  Anchor: Danforth 50 kg (holding 1,000 kgf)
  Total mooring weight: 130-180 kg (+ 50 kg anchor)
  Cost: $2,000-3,500

  Benefit: Polyester stretch (15-20%) absorbs dynamic loads.
  Chain at bottom keeps pull angle low at anchor.

Configuration C: DEEP WATER (50-80 m)
─────────────────────────────────────────────────
  Scope: 3:1 (semi-taut polyester)
  Chain: 16mm G30, 20 m (ground tackle)
  Rode: 24mm polyester double-braid, 130-220 m
  Anchor: Danforth 50 kg or Bruce 30 kg
  Total mooring weight: 120-150 kg (+ 50 kg anchor)
  Cost: $2,500-4,000

  Note: Semi-taut mooring with elastic polyester provides
  shock absorption through rope stretch rather than chain weight.
  Swing radius: 150-240 m (acceptable for open sea test range)
```

### 4.3 Anchor Selection — Revised

| Anchor Type | Holding Ratio (Sand) | Holding Ratio (Mud) | Weight Needed | Any Bottom? | Recovery? | Recommendation |
|-------------|---------------------|--------------------|--------------|-----------|-----------|----|
| **Danforth (fluke)** | **20:1** | **9:1** | **30-50 kg** | No (sand/mud only) | Yes (trip line) | **PRIMARY for known sand/mud** |
| **Bruce/Claw** | **15:1** | **8:1** | **20-30 kg** | **YES** | Yes | **PRIMARY for unknown bottom** |
| Mushroom | 10:1 (buried) | 10:1 | 80-100 kg | Mud/silt only | Difficult | Permanent moorings |
| Concrete block | 0.5:1 | 0.3:1 | **1,500+ kg** | Yes | No | **IMPRACTICAL for SS 6** |
| Screw anchor | 20-30:1 | 15:1 | 10-20 kg | No (soft bottom) | Yes (unscrew) | Future option |

**Decision change:** Replace 300 kg concrete block with 30-50 kg Danforth or Bruce anchor.

| Parameter | Old (SS 3) | New (SS 5-6) | Change |
|-----------|-----------|-------------|--------|
| Anchor | 300 kg concrete block | 30-50 kg Danforth/Bruce | 250 kg lighter, 5× more holding |
| Chain length | 50 m (12mm G30) | 30-140 m (depth dependent) | Up to 3× longer |
| Rode | None | 0-220 m polyester | New component |
| Scope | 5:1 | 5-7:1 (effective) | Increased |
| Holding force | ~250 kgf | 600-1,000 kgf | 2.5-4× stronger |
| Cost | $950 | $1,500-4,000 | +$550-3,050 |
| Swing radius | ±50 m | ±70-240 m | Larger (acceptable at sea) |

### 4.4 Pre-deployment of Mooring

**Recommended operational procedure for SS 5-6 operations:**

```
MOORING PRE-DEPLOYMENT PROCEDURE
═══════════════════════════════════════════════════════

Step 1: Deploy mooring in fair weather (SS 2-3)
  - Tug positions at target coordinates (GPS)
  - Lower anchor to seabed
  - Pay out chain/rode
  - Attach pickup buoy (radar-reflective, with light)
  - Mark position on chart
  - DONE: mooring system sitting on seabed ready

Step 2: Deploy target (SS 4-5 acceptable)
  - Tow target to mooring pickup buoy
  - Pick up mooring line from buoy
  - Connect to target's bow cleat/fairlead
  - Release tow line
  - Target swings to mooring → anchored
  - Activate GPS beacon (72h battery)
  - Deploy drogue if needed for stability
  - Tug withdraws

Step 3: Wait for test window (1-3 days)
  - Target holds position in SS 5-6
  - GPS beacon confirms position ±swing radius
  - No personnel at target

Step 4: Execute test
  - Weather window SS ≤ 4 (for firing ship operations)
  - Activate IR system (timer set at deployment)
  - Confirm RCS/IR signatures via ship radar/camera
  - Fire missile
  - Engage

BENEFIT: Mooring deployment happens in calm weather (low risk).
Target attachment is a brief operation (30 min in SS 4-5).
Longest exposure (2-3 days) is unmanned and passive.
```

---

## 5. Platform Structural Analysis

### 5.1 Wave Loading on Flat Pontoon

```
WAVE LOADING ANALYSIS
═══════════════════════════════════════════════════════

Because D/Lp < 0.2, the pontoon follows the wave surface.
It does NOT experience wave impact like a fixed structure.

Primary loads:
1. Wave slope → pitch/roll of platform → load on reflector mounts
2. Green water → wave wash over low-freeboard deck
3. Mooring chain pull → tension at fairlead/cleat
4. Cyclic fatigue → 2-3 days × ~10 cycles/min = 30,000-40,000 cycles

1. WAVE SLOPE LOAD (on superstructure):
   Wave slope at SS 5: θ = π × Hs / Lp = π × 3 / 76 = ±7.1°
   Wave slope at SS 6: θ = π × 5 / 126 = ±7.2°

   Lateral force on reflector (3 kg at 2m height):
   F = m × g × sin(θ) = 3 × 9.81 × sin(7.2°) = 3.7 N
   → Negligible for structural bolts (fatigue not a concern)

2. GREEN WATER LOAD:
   Platform follows wave surface, so green water is limited to:
   - Wave steepness causing water to flow across tilted deck
   - Breaking wave crests (random, infrequent in SS 5-6)

   Green water depth estimate:
   d_green = Hs × (D / Lp) × π / 2 ≈ 3.0 × 0.11 × 1.57 = 0.52 m
   → ~38 cm of water flowing across deck in SS 5 (peak events)
   → ~50 cm in SS 6

   Green water force on superstructure (1m wide × 2m high face):
   F = 0.5 × ρ × C_d × A × v²
   v ≈ 2 m/s (relative water velocity across deck)
   F = 0.5 × 1025 × 1.5 × (1 × 0.5) × 4 = 1,538 N = 157 kgf
   → Significant! Superstructure must be designed for green water loads

3. MOORING CHAIN PULL:
   Peak load: 1,464 kgf (see Section 4.1)
   Applied at fairlead/bow cleat
   → Need reinforced attachment point (steel pad eye, through-bolted)
   → Distribute load across platform structure

4. FATIGUE CYCLING:
   Wave period SS 5: 7 s → 8.6 cycles/min
   Duration: 3 days × 24 hr × 60 min = 4,320 min
   Total cycles: 4,320 × 8.6 = 37,152 cycles

   → Low-cycle fatigue regime (< 10⁵)
   → HDPE and steel both handle this easily
   → Bolted connections may loosen → use Loctite or Nylock nuts
   → Welded connections: no concern at these load levels
```

> **Rev B.1:** Platform diameter 8.0m. D/Lp = 0.11 (SS 5) — still a wave follower. Green water depth estimate increases slightly due to larger deck area exposed to wave run-up.

### 5.2 Structural Design Requirements

| Requirement | SS 3 (Old) | SS 5-6 (New) | Design Response |
|-------------|-----------|-------------|-----------------|
| Mooring attachment | Simple cleat | Reinforced pad eye, through-bolted, load spread plate | Steel backing plate 200×200×10mm |
| Deck drainage | Optional | **Mandatory** — self-draining deck (scuppers) | 4× 100mm scupper holes at cardinal points |
| Superstructure | Lightweight frame | Wave-resistant frame, drainage holes in panels | Perforated panels, angled deflectors |
| Reflector mounts | Bolted | Bolted with Nylock + backup retention (safety wire) | Prevent reflectors falling off in waves |
| Propane system | Protected | **REMOVED** (Rev B — radar-only). No propane, no watertight enclosure needed. | N/A |
| GPS beacon | Surface mount | **Elevated mount + watertight** | Top of mast, ≥4.5m above waterline (on tallest mast) |
| Mast structures | N/A | 8× steel masts (60mm×4mm galv), deck sockets, guy wires if needed | Mast bending ≥1,100 N·m at base |

### 5.3 Structural Reinforcement Cost

| Item | Description | Cost |
|------|-------------|------|
| Reinforced mooring attachment | Steel pad eye + backing plate, through-bolted | $200 |
| Self-draining scuppers | 4× 100mm drainage holes + non-return flaps | $100 |
| Superstructure wave screening | Perforated panels, angled deflectors | $300 |
| Nylock nuts + safety wire (all bolts) | Vibration-resistant fasteners | $50 |
| Propane watertight enclosure | Marine-grade sealed box, 400×300×200mm | $150 |
| GPS beacon elevated mount | Stainless steel bracket, 2.5m height | $100 |
| **Total structural upgrade** | | **$900** |

---

## 6. Platform Stability & Seakeeping

### 6.1 Hydrostatic Properties

```
PLATFORM HYDROSTATICS
═══════════════════════════════════════════════════════

Platform: 6.0 m diameter circular pontoon
Hull depth: 0.5 m (HDPE rotomolded tub)
Total mass: 800 kg (as specified)

Waterplane area: A_wp = π × 3² = 28.27 m²

Displacement volume: V = 800 / 1025 = 0.780 m³

Draft: T = V / A_wp = 0.780 / 28.27 = 0.028 m ≈ 3 cm

Freeboard: f = hull_depth - T = 0.50 - 0.03 = 0.47 m

Reserve buoyancy:
  Total buoyancy at deck edge: V_max = 28.27 × 0.50 × 1025 = 14,488 kg
  Displacement: 800 kg
  Reserve: (14,488 - 800) / 14,488 = 94.5%
  → EXCELLENT reserve buoyancy

Metacentric radius:
  BM = I / V = (π × D⁴ / 64) / V
  I = π × 6⁴ / 64 = 63.62 m⁴
  BM = 63.62 / 0.780 = 81.6 m
  → EXTREMELY high stability (will not capsize)

KB (center of buoyancy above keel): T/2 = 0.014 m
KG (center of gravity above keel): estimated 0.8 m (weight concentrated at deck level)
GM = KB + BM - KG = 0.014 + 81.6 - 0.8 = 80.8 m
  → GM > 0 means stable. GM = 80.8 m is exceptionally stable.
```

> **Rev B.1 REVISED HYDROSTATICS (8.0m platform, 980 kg):**
> - Waterplane area: A_wp = π × 4² = **50.27 m²** (was 28.27)
> - Draft: T = 980 / (1025 × 50.27) = **0.019 m ≈ 2 cm** (was 3 cm)
> - Freeboard: 0.50 - 0.02 = **0.48 m**
> - Reserve buoyancy at deck edge: 50.27 × 0.50 × 1025 = **25,763 kg** → reserve **(980/25,763) = 96.2%**
> - BM = I / V = (π × 8⁴ / 64) / (980/1025) = 201.06 / 0.956 = **210.3 m** (was 81.6 m)
> - GM = 0.01 + 210.3 - 0.8 = **209.5 m** (extremely stable, no capsize risk)
> - 8.0m platform is even MORE stable than 6.0m (BM scales with D⁴/V)

### 6.2 Roll/Pitch Behavior in SS 5-6

| Parameter | Value | Impact |
|-----------|-------|--------|
| GM | 80.8 m | Extremely stiff — platform follows wave slope exactly |
| Natural roll period | T_roll = 2π × sqrt(k²/g/GM) ≈ 0.7 s | Much shorter than wave period |
| Wave slope (SS 5) | ±7.1° | Platform tilts ±7.1° following waves |
| Wave slope (SS 6) | ±7.2° | Platform tilts ±7.2° following waves |
| RCS impact at ±7° | < 1 dB loss (trihedral tolerance ±15°) | **ACCEPTABLE** |
| IR impact at ±7° | None (central burner, elevated) | **ACCEPTABLE** |

**Conclusion:** The circular flat pontoon is inherently stable in any sea state. It follows the wave surface like a cork, tilting ±7° maximum. This tilt is well within the RCS tolerance of trihedral corner reflectors (maintain >90% RCS up to ±15° tilt). No capsize risk.

### 6.3 Heave and Green Water

```
HEAVE AND GREEN WATER IN SS 5-6
═══════════════════════════════════════════════════════

Platform heave amplitude: ≈ Hs/2
  SS 5: ±1.5 m (platform rides up and down 3 m total)
  SS 6: ±2.5 m (platform rides up and down 5 m total)

Green water occurrence:
  With 0.47 m freeboard on a wave-following platform,
  green water occurs when wave crests steepen locally.

  Probability of green water event:
    P = exp(-2 × (freeboard / Hs)²)
    SS 5 (Hs=3m): P = exp(-2 × (0.47/3)²) = exp(-0.049) = 95%
    SS 6 (Hs=5m): P = exp(-2 × (0.47/5)²) = exp(-0.018) = 98%

  → Green water events are FREQUENT in SS 5-6
  → Deck will be awash regularly
  → ALL equipment must be waterproof or above wave height

DESIGN RESPONSE:
  1. Waterproof all deck-mounted equipment
  2. Self-draining deck (scuppers, open grating sections)
  3. Elevate GPS beacon on mast (2.5 m above deck = 3.0 m above waterline)
  4. Propane system in sealed enclosure with drain
  5. Reflectors: AlSi10Mg with anodize → inherently waterproof
  6. Superstructure: designed to shed water (perforated panels, drainage)
```

### 6.4 Stability Summary

| Criterion | SS 3 | SS 5-6 | Assessment |
|-----------|------|--------|------------|
| Capsize risk | None | **None** | GM = 80.8 m (impossible to capsize) |
| Roll angle | ±2° | ±7° | Within RCS tolerance |
| Heave | ±0.5 m | ±2.5 m | Acceptable (platform rides waves) |
| Green water | Rare | **Frequent** | Must waterproof all equipment |
| Structural fatigue | Not a concern | ~37,000 cycles | Within HDPE/steel endurance |
| Position drift | ±50 m | ±70-240 m | Acceptable at sea (off-shore range) |

---

## 7. Subsystem Endurance — 2-3 Days at Sea

### 7.1 Subsystem-by-Subsystem Assessment

| Subsystem | 8h Exposure (Old) | 72h Exposure (New) | Risk | Mitigation |
|-----------|-------------------|-------------------|------|------------|
| **Corner reflectors (AM AlSi10Mg)** | No concern | Minor salt spray deposits on reflective surfaces | LOW | Type III anodize inherently marine-resistant. Salt deposits have negligible RCS impact at X-band (lambda=32mm >> salt crystal size). Self-washing in wave action. |
| **Corner reflectors (traditional Al)** | No concern | Salt corrosion starts | MEDIUM | Requires paint or coating. AM anodized version is superior for multi-day exposure. |
| **~~Propane IR system~~** | **REMOVED** (Rev B — radar-only) | N/A | N/A | N/A |
| **Steel masts (8×)** | N/A | Salt corrosion on galvanized surface | LOW | Hot-dip galvanized (144 μm zinc) provides 10+ year marine life. Inspect sockets for fatigue cracking. |
| **GPS beacon** | 8h battery OK | **8h battery INSUFFICIENT for 72h** | **HIGH** | Upgrade to 72h+ battery. Options: larger Li-ion pack ($200-400), or solar+battery ($300-500), or Iridium beacon with 30-day battery ($800). |
| **Superstructure (foam + steel)** | OK | Foam waterlogging, steel corrosion | LOW | Marine-grade closed-cell foam (not open-cell). Hot-dip galvanized steel or aluminum frame. |
| **Mooring attachment** | OK | Fatigue at chain fairlead | LOW | Reinforced pad eye with wear plate (see Section 5.2) |
| **Platform hull (HDPE)** | OK | OK | NONE | HDPE is inherently UV/salt/waterproof. 20+ year marine life. |
| **Bolted connections** | OK | Bolt loosening from vibration | LOW | Nylock nuts or Loctite on all structural bolts. Safety wire on critical reflector mounts. |

### 7.2 GPS Beacon Upgrade

The GPS beacon battery is the **single most critical subsystem upgrade** for 72h operations.

| Option | Battery Life | Cost | Weight | Size | Recommendation |
|--------|------------|------|--------|------|----------------|
| Current COTS GPS beacon | 8 hr | $1,500 | 0.5 kg | Handheld | **INADEQUATE** |
| **External Li-ion battery pack** | **72-96 hr** | **$200-400** | **2 kg** | **15×10×5 cm** | **RECOMMENDED** |
| Solar panel + battery | Unlimited (daylight) | $300-500 | 3 kg | 30×30 cm panel | Backup option (weather dependent) |
| Iridium satellite beacon | 30 days (AAA batteries) | $800-1,200 | 0.3 kg | Palm-sized | Premium option (satellite coverage) |

**Recommendation:** External Li-ion battery pack ($300) with waterproof connector. Provides 72-96 hours. Simple, reliable, low cost. Mount battery in waterproof enclosure below deck with cable to beacon on mast.

### 7.3 Propane System for Extended Deployment

> **REMOVED (Rev B):** Entire propane IR system eliminated. VN-TGT-SEA-001 is radar-only. No fuel management, no ignition timing, no watertight enclosure needed. This section retained as reference.

**Challenge:** IR activation timing must account for 1-3 day delay between deployment and test.

| Approach | Description | Pros | Cons |
|----------|-------------|------|------|
| **Timer (preset at deployment)** | Set ignition timer for T + estimated wait | Simple, no radio | Must estimate test time accurately |
| **Radio command** | Remote ignition from firing ship at 20+ km | Precise timing | Requires UHF radio link ($2,000+) |
| **Timed with manual override** | Timer set for latest expected test, with option to fire early via radio | Best of both | Moderate complexity |

**Recommendation:** Timer-based with conservative fuel load. Set timer for T + 48h (expected test time). Load 4 kg propane (80-120 min burn time) instead of 2 kg. If test delays beyond 48h, a small support boat can approach to reset timer (target is passive, safe to approach). Cost: +$50 for extra propane tank.

---

## 8. TPMS Role Revision

### 8.1 Original TPMS Value Proposition (Superseded)

> **Rev B.1 CONFIRMED:** TPMS removed per user directive. HDPE hull with closed-cell foam fill provides adequate environmental buoyancy for 8.0m platform at 980 kg displacement.

```
TPMS FLOTATION CORE — ORIGINAL JUSTIFICATION
═══════════════════════════════════════════════════════

Primary value:    Ballistic survivability (50+ hits → reusable target)
ROI driver:       Each reuse saves $32-45K (avoided replacement)
Technology risk:  Phase H0 test ($6.2K) to validate
Development cost: $33,000 (Phase 3: full-size flotation section)
Production cost:  $3,500-10,000 per unit
Innovation claim: "Unsinkable" — 7,200 hits required to sink

STATUS: USER DIRECTIVE — NOT REQUIRED
"no need Target survivability 7,200 hits to sink"
```

### 8.2 Could TPMS Still Add Environmental Value?

| Scenario | TPMS Benefit | Alternative | Verdict |
|----------|-------------|-------------|---------|
| Hull cracks from wave slamming | TPMS cells prevent progressive flooding | Closed-cell foam fill achieves same result at 1/10th cost | TPMS NOT NEEDED |
| Hull puncture from debris (floating log, collision) | TPMS localizes damage | Foam fill or multi-compartment hull | TPMS NOT NEEDED |
| Extended deployment (>3 days) | TPMS provides extreme buoyancy reserve | Not required — 3 day max per user | TPMS NOT NEEDED |
| Post-engagement reuse | Target survives missile hit | **User explicitly does NOT want this** | TPMS NOT NEEDED |

**Conclusion: TPMS flotation core is NOT justified for the revised survivability definition.** Traditional marine construction (HDPE hull with closed-cell foam, or sealed compartments) provides adequate environmental survivability. The TPMS was specifically designed for ballistic damage tolerance, which is no longer a requirement.

### 8.3 Simplified Flotation Design

| Approach | Buoyancy Reserve | Cost | Complexity | Durability |
|----------|-----------------|------|------------|------------|
| **HDPE hull, empty** | 94.5% (hull alone) | $0 extra | Lowest | Good — HDPE doesn't corrode |
| **HDPE hull + closed-cell foam fill** | >98% (even if hull breaches) | $500-1,000 | Low | Excellent — 20+ year foam life |
| **HDPE hull + sealed compartments** | ~96% | $300 (internal dividers) | Low | Good |
| TPMS PA12 core (superseded) | >99.9% | $3,500-10,000 | High (AM outsource) | Unknown in marine env. |

**Recommendation: HDPE hull with closed-cell marine foam fill** in critical areas (pontoon ring). This provides:
- 98%+ reserve buoyancy (will float even with major hull damage)
- $500-1,000 cost (vs $3,500-10,000 for TPMS)
- Zero supply chain risk (foam is local, not AM outsourced)
- Proven marine technology (used in all life rafts, buoys, boat hulls)

---

## 9. Impact on Hyperganic Enhancement

### 9.1 Budget Reallocation

| Component | Original Budget | Revised Budget | Change | Justification |
|-----------|----------------|---------------|--------|---------------|
| **TPMS flotation core** | $33,000 (Phase 3) | **$0** | **-$33,000** | User directive: not required |
| **Phase H0 ballistic test** | $6,200 (Phase 0) | **$0** | **-$6,200** | No TPMS = no ballistic test needed |
| **AM corner reflectors** | $15,000 (Phase 2) | **$15,000** | No change | Still critical for RCS accuracy |
| **Schwarz P IR panels** | $4,000 (Phase 2) | $4,000 (deferred) | No change | Still deferred to Phase H1 |
| **Topology-optimized joints** | $5,000 (Phase 3) | **$5,000** | No change | Useful for wave-loaded connections |
| **Storm mooring system** | $0 | **+$2,500** | +$2,500 | New: anchor + chain/rode for SS 5-6 |
| **Mast system (8× steel masts + sockets)** | $0 | **+$1,430** | +$1,430 | New: Rev B.1 — elevated reflectors |
| **GPS 72h battery** | $0 | **+$300** | +$300 | New: extended battery pack |
| **Structural reinforcement** | $0 | **+$900** | +$900 | New: pad eye, scuppers, waterproofing |
| **nTop software license** | $2,000 | $2,000 | No change | Still needed for reflector design |

> **Rev B.1:** Total mast system adds $1,430/unit (8× masts $800, sockets $300, assembly/margin $330). Unit cost: $35,640.

### 9.2 Revised Hyperganic Budget

```
HYPERGANIC ENHANCEMENT BUDGET — REVISED
═══════════════════════════════════════════════════════

ORIGINAL:                              $68,000
  TPMS development + testing:  $39,200
  AM reflectors + IR panels:   $19,000
  Joints + nTop:               $7,000
  Contingency:                 $2,800

REVISED:                               $30,200
  AM reflectors (8x AlSi10Mg):        $15,000
  Schwarz P IR panel (1x demo):        $4,000
  Topology-optimized joints:           $5,000
  nTop software license:               $2,000
  Storm mooring upgrade:               $3,000
  GPS 72h battery:                     $300
  Structural reinforcement:            $900
                                       ────────
                                       $30,200

SAVINGS vs ORIGINAL:                   $37,800 (56% reduction)
```

### 9.3 Impact on Project Economics

| Metric | Original | Revised | Change |
|--------|----------|---------|--------|
| **Hyperganic budget** | $68,000 | $30,200 | -56% |
| **Total development budget** | $332,700 | ~$295,000 | -11% |
| **Unit cost (base)** | $32,000 | $33,000 (+mooring upgrade) | +3% |
| **Unit cost (H variant)** | $40-45,000 | $35-38,000 (no TPMS) | -12 to -18% |
| **Reusability (hits)** | 5-10 reuses (TPMS) | **1 use (expendable)** | Reduced |
| **TCO per test (50 tests)** | $20,020 (reusable) | $38,000 (expendable) | +90% |
| **ROI (3-year)** | 625% (from reuse savings) | ~200% (from cost reduction vs import) | Reduced |

### 9.4 TCO Impact — Honest Assessment

```
TCO COMPARISON: TPMS REUSABLE vs EXPENDABLE
═══════════════════════════════════════════════════════

SCENARIO: 50 missile acceptance tests over 3 years

A) WITH TPMS (Original — 5 reuses per target):
   Development: $332,700
   Targets: 10 units × $45,000 = $450,000
   Operations: 50 tests × $5,000 = $250,000
   Repair/replacement: $38,000
   TOTAL: $1,070,700 → $21,414/test

B) WITHOUT TPMS (Revised — expendable):
   Development: $295,000
   Targets: 50 units × $35,000 = $1,750,000
   Operations: 50 tests × $5,000 = $250,000
   TOTAL: $2,295,000 → $45,900/test

C) CURRENT BASELINE (ad-hoc barges):
   No development
   50 targets × $50,000 (estimated) = $2,500,000
   Operations: 50 × $8,000 = $400,000
   TOTAL: $2,900,000 → $58,000/test

VERDICT:
  Expendable VN-TGT-SEA-001 ($45,900/test) still beats
  current baseline ($58,000/test) by 21%.

  TPMS reusable variant ($21,414/test) would beat both by 63%,
  BUT user has explicitly deprioritized this capability.

  The expendable variant's value proposition is:
  ► Standardized (consistent RCS/IR every test)
  ► Safe (no personnel in danger zone)
  ► Storm-capable (deploys/survives in SS 5-6)
  ► Indigenous (85-90% local content)
  ► 21% cheaper than current ad-hoc approach
```

### 9.5 Decision Gate Revision

| Gate | Original | Revised |
|------|----------|---------|
| **H0: TPMS ballistic test** | PA12 SLS block survives 10+ hits AND floats ($6.2K) | **ELIMINATED** — TPMS not required |
| **H1: AM reflector RCS validation** | RCS within ±1 dBsm of target ($15K) | **UNCHANGED** — still critical path |
| **H2: Full-size flotation integration** | Full TPMS section survives live-fire ($25K) | **REPLACED** — Storm mooring sea trial ($5K) |
| **H3: Production readiness** | Modular library + digital twin ($20K) | **SIMPLIFIED** — AM reflector library only |

---

## 10. Revised Specifications

### 10.1 Updated Target Specifications

| Parameter | Old Value | **New Value** | Rationale |
|-----------|-----------|---------------|-----------|
| Platform diameter | 6.0 m | **8.0 m** | Rev B — improved stability |
| Reflector height above waterline | 1.5-2.0 m | **3.0-4.0 m** | Rev B.1 — steel masts |
| Displacement | 800 kg | **980 kg** (Rev B.1, includes masts) | Rev B.1 — 8.0m platform + mast system |
| Sea state (deploy/tow) | SS 0-3 | **SS 4-5** | Tow in moderate-rough seas |
| Sea state (survive anchored) | SS 4 | **SS 5-6** | 2-3 days anchored in rough seas |
| Wind (survive) | Not specified | **Bft 6-7 (22-33 kn)** | Northeast monsoon conditions |
| Duration at anchor | Not specified | **72 hours (3 days)** | Pre-engagement wait time |
| Position hold | ±50 m (SS 3) | **±70-240 m (depth dependent, SS 6)** | Larger swing circle with longer rode |
| Anchor | 300 kg concrete block | **30-50 kg Danforth or Bruce** | Higher holding power, any seabed |
| Chain/rode | 50 m, 12mm G30 | **30-140 m chain + 0-220 m polyester rode** | Depth-dependent design |
| Survivability (ballistic) | >99% after 50 hits (TPMS) | **NOT SPECIFIED** (expendable after hit) | User directive |
| GPS beacon battery | 8 hr | **72 hr minimum** | Extended deployment duration |
| Deck drainage | Not specified | **Self-draining (4× scuppers)** | Green water in SS 5-6 |
| Equipment waterproofing | Not specified | **IP67 minimum for all electronics** | Frequent wave wash-over |
| Propane endurance | 30 min burn | **60-120 min burn (4 kg tank)** | Margin for test timing uncertainty |
| Mooring cost | $950 | **$1,500-4,000 (depth dependent)** | Storm-rated system |
| Flotation | TPMS PA12 core | **Closed-cell marine foam fill** | Simpler, cheaper, adequate |
| Unit cost (H variant) | $40-45K | **$35-38K** | Reduced (no TPMS) |

### 10.2 Unchanged Specifications

| Parameter | Value | Status |
|-----------|-------|--------|
| RCS (X-band) | 250-350 m², 360° | Unchanged (AM reflectors still critical) |
| RCS variation | ≤ ±2 dB through 360° | Unchanged |
| ~~IR signature~~ | ~~250°C MWIR, 360°, 30 min+~~ | **REMOVED** (Rev B — radar-only) |
| Deployment time | 30 min from mooring pickup | Unchanged (pre-deployed mooring) |
| Crew required | 3-4 personnel | Unchanged |
| Missile compatibility | C-802, Kh-35, Exocet | Unchanged |
| Indigenous content | 85-90% | Unchanged (improved: no AM TPMS import) |
| Mast structures | 8× galvanized steel, 60mm×4mm, 3-4m height | NEW (Rev B.1) |

---

## 11. Revised Risk Matrix

| Risk | Probability | Impact | Mitigation | Change from Original |
|------|-------------|--------|------------|---------------------|
| ~~PA12 TPMS fails ballistic test~~ | ~~25%~~ | ~~HIGH~~ | ~~Phase H0 test~~ | **ELIMINATED** — TPMS removed |
| ~~Water wicks through damaged cells~~ | ~~35%~~ | ~~MEDIUM~~ | ~~Hydrophobic coating~~ | **ELIMINATED** — TPMS removed |
| AM reflector RCS mismatch | 15% | MEDIUM | Published RCS formula + AM tolerance data | Unchanged |
| Military rejects 3D-printed hardware | 50% | HIGH | Live-fire demo; cite GE Aviation | Unchanged |
| **Mooring fails in SS 6** | **20%** | **HIGH** | **Proper marine anchor + adequate scope; pre-deploy in fair weather** | **NEW** |
| **GPS beacon battery fails before test** | **10%** | **MEDIUM** | **72h Li-ion pack; redundant Iridium beacon option** | **NEW** |
| **Tow line parts in SS 5** | **15%** | **MEDIUM** | **Dyneema tow line (SWL 8,000 kgf); bridle + drogue for stability** | **NEW** |
| **Superstructure fails from green water** | **10%** | **LOW** | **Perforated panels; wave-shedding design; drainage** | **NEW** |
| **Target drifts off station (anchor drags)** | **15%** | **MEDIUM** | **Danforth with proper set; scope 7:1; pre-deploy and verify** | **NEW** |
| AM cost exceeds budget | 15% | LOW | Chinese bureaus; reduced AM scope | Reduced risk (smaller AM scope) |
| No local AM service bureau | 10% | LOW | Multiple ASEAN options | Unchanged |

**Overall risk assessment: MODERATE (reduced from MODERATE-HIGH).**

Eliminating TPMS removes the highest technical risk (PA12 ballistic performance unknown). New environmental risks (mooring, towing) are well-understood marine engineering problems with proven solutions. The risk profile shifts from "novel material science" to "conventional naval architecture," which is a significant de-risking.

---

## 12. O-57 Reinterpretation

### 12.1 Outcome Statement (Unchanged)

> **O-57:** Maximize the number of engagements a single target can survive

### 12.2 Interpretation Change

| Aspect | Old Interpretation | New Interpretation |
|--------|-------------------|-------------------|
| "Survive" means | Survive missile hits (ballistic damage) | Survive environmental conditions (weather) |
| Metric | Number of hits before sinking | Number of days maintaining operational readiness |
| Satisfaction driver | TPMS cellular flotation | Robust mooring + waterproof subsystems |
| Score change | Opp = 18.0 | **Opp = 18.0 (unchanged)** — current targets still fail this |

### 12.3 Why O-57 Score Remains 18.0

Current targets (ad-hoc barges) fail the revised O-57 even more clearly:
- **Importance** remains 10.0 — the ability to deploy and wait for optimal test conditions is critical for operational success
- **Satisfaction** remains 2.0 — current ad-hoc targets:
  - Cannot survive SS 5-6 (capsize, break free, flood)
  - Cannot wait 2-3 days at anchor (no extended GPS, no waterproofing)
  - Force the Navy to deploy ONLY in fair weather (SS 2-3), severely limiting test windows
  - This is arguably a WORSE satisfaction than the ballistic interpretation

**Revised O-57 is more operationally relevant:** Vietnam's Navy conducts tests year-round, including during the northeast monsoon (Oct-Mar) when SS 5-6 is common. A target that can only deploy in SS 2-3 loses 40-60% of available test days. A storm-capable target expands the operational window dramatically.

### 12.4 Updated O-36 and O-37

Two CONFIRM-phase outcomes become more important with the environmental survivability focus:

| ID | Outcome | Old Opp | New Opp | Change |
|----|---------|---------|---------|--------|
| O-36 | Minimize likelihood of capsize/instability before firing | 11.0 (MOD) | **14.0 (HIGH)** | Imp 9.0→9.5, Sat 5.0→4.0 (SS 5-6 is harder) |
| O-37 | Maximize confidence anchor holds during engagement | 11.0 (MOD) | **15.0 (EXTREME)** | Imp 9.0→10.0, Sat 5.0→3.0 (SS 6 holding is critical) |

This brings the EXTREME count from 5 to **6 outcomes** (adding O-37), further validating the project.

---

## 13. Conclusions & Design Directives

### 13.1 Summary of Changes

```
SURVIVABILITY PIVOT SUMMARY
═══════════════════════════════════════════════════════

FROM:                          TO:
Ballistic survivability        Environmental survivability
TPMS PA12 cellular core       Robust mooring + marine construction
7,200 hits to sink            72 hours at anchor in SS 5-6
$10-25K per unit (TPMS)       $500-1,000 per unit (foam fill)
AM-intensive (TPMS + reflectors) AM-focused (reflectors only)
$68K Hyperganic budget        $30.2K Hyperganic budget (-56%)
5-10 reuses per target        Expendable (1 use)
$21K/test TCO (reusable)      $46K/test TCO (expendable)
Novel material science risk    Conventional naval engineering

NET EFFECT:
  ✓ Lower development cost (-$37.8K)
  ✓ Lower unit cost (-$5-10K per target)
  ✓ Lower technical risk (proven marine engineering)
  ✓ Higher operational capability (SS 5-6 deployment)
  ✗ No reusability (expendable after hit)
  ✗ Higher per-test cost (no reuse savings)
  ≡ AM reflectors remain as key differentiator (RCS accuracy)
```

### 13.2 Revised Design Directives for Phase 1

| # | Directive | Priority | Source |
|---|-----------|----------|--------|
| 1 | Design platform for SS 5-6 survival (72h anchored, Bft 6-7 wind) | **CRITICAL** | User directive |
| 2 | Use pre-deployed mooring concept (deploy mooring in fair weather, attach target later) | **CRITICAL** | Operational analysis |
| 3 | Use proper marine anchor (Danforth/Bruce) + chain/rode combo, depth-dependent sizing | **CRITICAL** | Force analysis |
| 4 | GPS beacon with 72h+ battery (Li-ion external pack) | **HIGH** | Subsystem endurance |
| 5 | Self-draining deck with scuppers, all equipment IP67 waterproof | **HIGH** | Green water analysis |
| 6 | Use 8 × 0.5m AM corner reflectors at 45° spacing (unchanged) | **CRITICAL** | RCS requirement unchanged |
| 7 | Circular pontoon platform (unchanged) | **CRITICAL** | Stability + 360° symmetry |
| 8 | HDPE hull with closed-cell foam fill (replaces TPMS) | **HIGH** | Simplified flotation |
| 9 | Central elevated propane burner with watertight enclosure, 4 kg tank | **HIGH** | Extended deployment IR |
| 10 | Tow system: bridle attachment + trailing drogue for stability in SS 5 | **HIGH** | Towing analysis |
| 11 | Reinforced mooring attachment (steel pad eye, through-bolted, load spread plate) | **HIGH** | Structural analysis |
| 12 | Adopt C-Target 3 DFM philosophy (unchanged) | **HIGH** | RE analysis |

### 13.3 What STAYS from the Hyperganic Enhancement

| Component | Status | Justification |
|-----------|--------|---------------|
| **AM corner reflectors (AlSi10Mg LPBF)** | **KEEP — CORE INNOVATION** | ±0.1° tolerance → 5-8 dB RCS improvement. This IS the product differentiator. |
| **Schwarz P IR panels** | **KEEP — DEFERRED** | Low priority but still unique. Phase H1 opportunity. |
| **Topology-optimized joints** | **KEEP** | Useful for mooring attachment and reflector mounts. Weight reduction at connection points. |
| **nTop software license** | **KEEP** | Required for reflector and joint design. |

### 13.4 What is REMOVED from the Hyperganic Enhancement

| Component | Status | Reason |
|-----------|--------|--------|
| **TPMS PA12 flotation core** | **REMOVED** | User directive: "no need Target survivability 7,200 hits to sink" |
| **Phase H0 ballistic test** | **REMOVED** | No TPMS = no ballistic test needed |
| **Phase H2 full-size flotation** | **REMOVED** | No TPMS production development |
| **Phase H3 modular TPMS library** | **SIMPLIFIED** | Reduced to AM reflector library only |

### 13.5 Future Option — TPMS as Add-On

The TPMS flotation core can be added as a future enhancement IF operational experience demonstrates that target reusability is valuable. The technology remains feasible (Phase 0 analysis still valid). It is simply not prioritized for the initial product.

```
TPMS RE-INTRODUCTION PATH (IF NEEDED LATER)
═══════════════════════════════════════════════════════

Phase N+1:  Conduct Phase H0 ballistic test ($6.2K)
Phase N+2:  If H0 passes, develop full-size TPMS section ($33K)
Phase N+3:  Integrate into production pontoon
Phase N+4:  Reusable variant available (5-10 uses per target)

Total additional cost to reintroduce: $39-42K
Timeline: 6-12 months from decision

This option remains available at any time after initial production.
```

---

## Cross-References

- [[odi_analysis.md]] — ODI analysis (O-57 survivability outcome, O-36 stability, O-37 anchor)
- [[re_deep_analysis.md]] — Deep RE: mooring subsystem, competitor flotation designs
- [[hyperganic_feasibility.md]] — TPMS feasibility (retained as reference for future option)
- [[re_competitive_analysis.md]] — Competitive positioning
- [[phase0_synthesis.md]] — Phase 0 synthesis (cost model, TCO — partially revised by this document)
- [[../00_project_brief.md]] — Project brief (specifications updated by this document)
- [[../PROJECT_STATUS.md]] — Status tracker
