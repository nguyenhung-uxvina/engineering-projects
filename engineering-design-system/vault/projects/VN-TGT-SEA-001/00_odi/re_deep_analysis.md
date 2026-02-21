---
project: VN-TGT-SEA-001
phase: 0
type: reverse_engineering_deep
version: 2.1
created: 2026-02-09
updated: 2026-02-10
revision: B.1
status: draft
---

# Deep Reverse Engineering: Competitor Subsystem Analysis

> **Rev B.1** — Platform 8.0m (was 6.0m), superstructure REMOVED, IR/propane REMOVED (radar-only), reflectors elevated to 3-4m on steel masts, 980 kg displacement, $35,640/unit. Competitor RE data unchanged.

**Scope:** Subsystem-level teardown of 5 competitor systems and 3 critical technology areas
**Purpose:** Extract quantitative design parameters for VN-TGT-SEA-001-H subsystem specification
**Sources:** Public specifications, patent databases, published research, manufacturer datasheets

---

## 1. Corner Reflector Subsystem — Deep Analysis

### 1.1 RCS Physics Baseline

**Trihedral corner reflector (square faces):**
```
sigma_max = (12 * pi * a^4) / lambda^2

Alternative formulation (from radar engineering):
sigma_max = (4 * pi * a^4) / (3 * lambda^2)

Note: The factor difference depends on whether 'a' refers to
face edge length (12*pi) or interior edge length (4*pi/3).
VN-TGT-SEA-001 uses face edge = a, so:

  sigma = (12 * pi * a^4) / lambda^2
```

**RCS scaling law:** RCS increases with the **4th power** of edge dimension. Doubling edge length increases RCS by 16x. This has critical cost implications — a slightly larger reflector dramatically reduces the number needed.

| Edge Length (a) | X-band RCS (9.4 GHz, lambda=32mm) | Weight (3mm Al) | Cost Est. |
|-----------------|-----------------------------------|-----------------|-----------|
| 0.2 m | 0.6 m² (-2.2 dBsm) | 0.5 kg | $50 |
| 0.3 m | 3.0 m² (4.8 dBsm) | 1.1 kg | $120 |
| 0.4 m | 9.5 m² (9.8 dBsm) | 2.0 kg | $250 |
| **0.5 m** | **23.2 m² (13.7 dBsm)** | **3.1 kg** | **$400** |
| 0.6 m | 48.2 m² (16.8 dBsm) | 4.5 kg | $600 |
| 0.8 m | 152.3 m² (21.8 dBsm) | 8.0 kg | $1,000 |

**Design decision for VN-TGT-SEA-001:** a = 0.5 m provides optimal balance. 8 reflectors at 0.5 m = 186 m² peak (23.2 x 8), with overlap yielding 250-350 m² effective 360 deg coverage.

> **Rev B.1:** Edge length upgraded to **a = 0.8 m** (152.3 m² per reflector). 8 reflectors at 0.8m = 1,218 m² peak, >1,000 m² average 360°. Hybrid CNC faces + AM frames. See [[phase0_final_revision.md]].

### 1.2 Array Configurations for 360 deg Coverage

| Configuration | Qty | Spacing | Min RCS (between peaks) | Coverage Quality | Used By |
|---------------|-----|---------|------------------------|-----------------|---------|
| Central mast, 4 reflectors | 4 | 90 deg | ~30% of peak (deep nulls) | Poor — 4 nulls at 45 deg | Small buoys |
| **Perimeter array, 8 reflectors** | **8** | **45 deg** | **~60% of peak** | **Good — shallow nulls** | **VN-TGT-SEA-001** |
| Octahedral (back-to-back) | 8 | Geometric | ~40% of peak | Moderate — designed for spherical | Navigation buoys |
| Dense array, 12 reflectors | 12 | 30 deg | ~80% of peak | Excellent — near-uniform | Military decoys |

**Key finding:** 8 reflectors at 45 deg spacing provides <= +/- 2 dB variation through 360 deg, meeting the requirement. Going to 12 reflectors improves to +/- 1 dB but adds 50% more cost/weight.

### 1.3 Effect of Sea Motion on RCS

**RCS scintillation in seaway:**
- Ship RCS varies dramatically with roll/pitch (echo strength changes by 10-20 dB in heavy seas)
- For VN-TGT-SEA-001: circular pontoon limits roll to +/- 5 deg in SS 3
- At +/- 5 deg roll, trihedral reflector RCS drops by < 1 dB (within tolerance)
- At +/- 15 deg roll (SS 4+), RCS drops by 3-5 dB — still above 150 m² minimum

**Design implication:** Circular pontoon geometry is critical for RCS stability. A rectangular barge would roll more, causing greater RCS variation.

### 1.4 Corner Reflector Construction — Competitor Methods

| Method | Material | Tolerance | Cost | Durability | Used By |
|--------|----------|-----------|------|------------|---------|
| Hand-bent sheet | 1.3-3mm Al 6082 T651 | +/- 1-2 deg | $50-200 | 2-5 years | Most maritime |
| Welded fabrication | 3mm Al 5083 | +/- 0.5 deg | $200-500 | 5-10 years | Military targets |
| **AM LPBF monolith** | **AlSi10Mg** | **+/- 0.1 deg** | **$800-1,500** | **10+ years (anodized)** | **VN-TGT-SEA-001-H** |
| Mesh panels | Al or Cu mesh | +/- 2-5 deg | $20-50 | 1-2 years | Expendable |
| Foil construction | 0.14mm Al foil | +/- 5+ deg | $5-10 | Expendable | Emergency reflectors |

**AM advantage quantified:**
- +/- 0.1 deg error = < 0.5 dB RCS loss
- +/- 1.0 deg error (typical traditional) = 5-8 dB RCS loss
- **Net improvement: 5-8 dB** = 3-6x more consistent RCS
- This directly reduces missile acquisition failure rate from ~10-15% to ~2-3%

### 1.5 Reflector Mounting Height

**Maritime standard:** Minimum 4.6 m (15 ft) above sea level for navigation reflectors (provides ~8 km radar horizon).

**VN-TGT-SEA-001 design (Rev B.1):** Reflectors elevated to **3.0-4.0 m** above waterline on 8× galvanized steel masts (60mm×4mm tube, ~16 kg each). This provides:
- Improved radar horizon (~7 km at 3.5m height vs ~4.5 km at 1.5m)
- Better separation from sea clutter (reflectors above wave crests in SS 5-6)
- Anti-ship missile seekers approach at 5-15 m altitude — look-down angle to 3.5m reflector at 20 km range: < 0.01°
- Mast bending moment requirement: ≥1,100 N·m at base (wind + dynamic loading)
- Mast tube: 60mm OD × 4mm wall galvanized steel (allowable 1,303 N·m > 1,100 N·m required)

---

## 2. Mooring Subsystem — Deep Analysis

### 2.1 Single-Point vs Multi-Point Mooring

| Parameter | Single-Point (SPM) | 3-Point Spread | VN-TGT-SEA-001 Choice |
|-----------|--------------------|--------------|-----------------------|
| Deployment time | 15-30 min | 60-120 min | **SPM (faster)** |
| Position accuracy | +/- 50-100 m (swing circle) | +/- 5-20 m | SPM acceptable |
| Crew required | 3-4 | 6-8 | **SPM (fewer)** |
| Equipment | 1 anchor + chain | 3 anchors + 3 chains + bridle | **SPM (simpler)** |
| Cost | $950 | $3,500-5,000 | **SPM (cheaper)** |
| Recovery | Simple (1 line) | Complex (3 lines) | **SPM (easier)** |
| Weathervaning | Yes (rotates with wind/current) | No (fixed orientation) | SPM OK (360 deg signature) |

**Decision: Single-point mooring.** Because VN-TGT-SEA-001 has 360 deg signature coverage, weathervaning is acceptable — the target presents the same signature regardless of orientation. This eliminates the primary disadvantage of SPM and allows simpler, faster, cheaper deployment.

> **Rev B.1:** Decision unchanged. Single-point mooring confirmed for 8.0m platform. Storm-rated: Danforth/Bruce anchor (30-50 kg) + 12-16mm G30 chain + polyester rode. Peak mooring load 1,512 kgf, SWL 4,536 kgf. Concrete block REPLACED by proper marine anchor.

### 2.2 Scope Ratio and Chain Length

```
MOORING GEOMETRY
═══════════════════════════════════════════════════════

Water depth: D = 10 m (typical Vietnamese coastal test range)
Scope ratio: S = 5:1 (normal conditions)
Chain length: L = S x D = 50 m

Swing circle radius (catenary):
  R = sqrt(L^2 - D^2)
  R = sqrt(50^2 - 10^2)
  R = sqrt(2500 - 100)
  R = sqrt(2400)
  R = 49 m

With target platform radius (3 m):
  Total swing radius = 49 + 3 = 52 m → rounds to +/- 50 m

For storm conditions (scope 8:1):
  L = 80 m
  R = sqrt(80^2 - 10^2) = sqrt(6300) = 79 m
  Total = 79 + 3 = 82 m → +/- 80 m
```

**Verification:** +/- 50 m position hold in SS 3 confirmed by calculation. Matches project brief specification.

### 2.3 Anchor Selection

| Anchor Type | Holding Power Ratio | Weight Needed (for 800 kg target, SS 3) | Seabed | Recovery |
|-------------|--------------------|-----------------------------------------|--------|----------|
| Danforth (fluke) | 20:1 (sand), 9:1 (mud) | 40-90 kg | Sand/mud only | Difficult |
| Mushroom | 10:1 (buried) | 80 kg (after burial) | Mud/silt only | Very difficult |
| **Concrete block** | **1:2 (weight:holding)** | **300 kg** | **Any bottom** | **Not recovered** |

**Decision: Concrete block (300 kg).**
- Rationale: Expendable target = expendable anchor. No recovery needed.
- Concrete block works on ANY seabed (sand, mud, rock, coral) — critical for Vietnamese coastal variety
- Simplest to fabricate: pour concrete into a mold with embedded chain eye
- Cost: $200 (materials + labor) — cheapest option
- Holding force: 300 kg x 0.55 (underwater weight factor) x 2 (friction + suction) = ~330 kg holding
- Required holding: 800 kg target x wind/current force coefficient (~0.3 in SS 3) = ~240 kg
- Safety factor: 330/240 = 1.4 — acceptable for expendable target

> **Rev B.1:** Concrete block (300 kg) REPLACED by Danforth/Bruce anchor (30-50 kg). Holding power 600-1,000 kgf (vs 250 kgf for concrete). Required for SS 5-6 survival. See [[environmental_survivability.md]] Section 4.

### 2.4 Chain Specification

| Parameter | Specification | Rationale |
|-----------|--------------|-----------|
| Grade | G30 (proof coil) | Lowest cost, adequate strength |
| Size | 12 mm (1/2 inch) | Working load ~1,800 kg (4:1 safety factor) |
| Length | 50 m | Scope 5:1 at 10 m depth |
| Galvanization | Hot-dip (144 um zinc) | Saltwater immersion, 5+ year life |
| End fittings | Shackle (bow) + swivel + shackle (anchor) | Prevents chain twist |
| Weight | ~2.5 kg/m x 50 m = 125 kg | Contributes to catenary damping |
| Cost | $8-10/m x 50 m = $400-500 | Including fittings |

> **Rev B.1:** Chain upgraded to **12-16mm G30** (TBD Phase 2). Peak mooring load increased to 1,512 kgf due to elevated reflectors (+25% windage at height). SWL requirement: 4,536 kgf.

**Catenary benefit:** The 125 kg chain weight creates a catenary curve that:
1. Keeps the pull angle on the anchor near-horizontal (< 11 deg at 5:1 scope)
2. Absorbs shock loads from wave action (elastic curve stretching)
3. Provides damping (chain weight resists sudden displacement)

---

## 3. QinetiQ Hammerhead MkII — Subsystem Teardown

### 3.1 Hull System

| Parameter | Hammerhead Spec | VN-TGT-SEA-001 Comparison |
|-----------|----------------|---------------------------|
| Material | GRP (glass reinforced plastic) | HDPE pontoon (simpler) |
| Construction | Molded fiberglass speedboat hull | Rotomolded or welded |
| LOA | 5.2 m | **8.0 m** diameter (circular) — Rev B |
| Beam | 1.4 m | 6.0 m (circular = omnidirectional) |
| Displacement | 900 kg | **980 kg** — Rev B.1 |
| Hull type | Planing (V-hull) | Flat pontoon (displacement) |

**RE insight:** Hammerhead's GRP V-hull is optimized for **speed** (40 knots planing). VN-TGT-SEA-001 doesn't need speed — circular flat pontoon optimizes for **stability** and **360 deg symmetry**. Completely different design paradigm.

### 3.2 Propulsion System

| Parameter | Hammerhead | VN-TGT-SEA-001 |
|-----------|-----------|-----------------|
| Engine | MerCruiser 3.0L gasoline | **NONE** (stationary) |
| Power | 135 HP | 0 HP |
| Drive | Alpha1 sterndrive | N/A |
| Fuel | 161 L (43 gal) | **None** (radar-only, no propane) — Rev B |
| Speed | 40 kn (SS 2), 35 kn (SS 3) | 0 kn (anchored) |
| Endurance | 5 hr @ 30 kn, 12 hr @ 10 kn | 8+ hr (GPS beacon battery) |
| Cost allocation | ~$15,000 (engine + drive) | $0 |

**RE insight:** Eliminating propulsion saves ~$15,000/unit and removes the most complex, maintenance-intensive subsystem. This is the core cost advantage of the anchored concept.

### 3.3 UTCS Command & Control

| Parameter | Hammerhead UTCS | VN-TGT-SEA-001 |
|-----------|----------------|-----------------|
| Standard | STANAG 4856 | N/A (passive) |
| Range | 5 nm (subject to antenna height) | N/A |
| Protocol | Single data half-duplex | N/A |
| Capacity | Up to 16 vehicles concurrent | N/A |
| Features | Remote start, waypoint, speed | GPS beacon only |
| Cost | ~$50,000-80,000 (system) | $1,500 (COTS GPS beacon) |
| Operator skill | Specialist trained | None (passive) |

**RE insight:** UTCS is the second-largest cost driver in USV targets (~$50-80K). VN-TGT-SEA-001 eliminates this entirely — the target is passive (deploy, activate timer, withdraw). This removes:
- C2 system cost ($50-80K)
- Control vessel requirement (vessel must remain at 2-3 km during firing)
- Specialist operator training
- Signal interference risk

### 3.4 Hammerhead Market Data

- **Total orders:** >425 units worldwide (highest production surface target)
- **Major customers:** Canada (>40), UK, USA, South Africa, Germany
- **Unit cost:** ~$300,000 (including C2 share)
- **Primary use:** FIAC/FAC simulation, swarm training (up to 40 vehicles)
- **NOT designed for:** Missile acceptance testing (RCS only 10-50 m²)

**Strategic takeaway:** Hammerhead dominates the **moving target / gunnery training** market. VN-TGT-SEA-001 targets a **different market** (missile acceptance). No direct competition — complementary products for different jobs.

---

## 4. Metal Shark HSMST — Subsystem Teardown

### 4.1 Hull System

| Parameter | HSMST Spec | VN-TGT-SEA-001 Comparison |
|-----------|-----------|---------------------------|
| Base platform | 26 ft Relentless center console | Custom circular pontoon |
| Designer | Michael Peters (naval architect) | In-house |
| Material | 5086 Aluminum, welded | HDPE or steel |
| Yield strength | 210 MPa (H116 temper) | N/A (structural not critical) |
| Density | 2.66 g/cm³ | HDPE: 0.95 g/cm³ |
| Construction | Heavy welded plates | Rotomolded or fabricated |
| LOA | 7.9 m (26 ft) | 6.0 m diameter |
| Configuration | Collared center console | Flat circular pontoon |

**RE insight:** HSMST uses premium 5086 aluminum (not 5083) because it needs to withstand 46-knot dynamic loads. VN-TGT-SEA-001's static loading allows much simpler materials — HDPE rotomolding or mild steel.

### 4.2 Propulsion

| Parameter | HSMST | VN-TGT-SEA-001 |
|-----------|-------|-----------------|
| Configuration | Twin outboards | NONE |
| Max power | 600 HP (combined) | 0 HP |
| Speed | 46 knots | 0 knots |
| Engine cost | ~$40,000-60,000 (twin) | $0 |

### 4.3 US Navy Contract Analysis

| Metric | Value | Implication |
|--------|-------|-------------|
| Initial contract | $14M for 350 units | **$40,000/unit** (production cost) |
| Extended value | ~$42M total | ~$48,250/unit (average with options) |
| Delivery rate | Up to 3 units/week | High-rate production capability |
| Total delivered | >400 units | Massive installed base |
| Export status | **ITAR restricted** | **NOT available to Vietnam** |

**Key RE insight:** At $40-48K/unit in volume production, HSMST is surprisingly cheap for a USV — but this is WITHOUT C2 system (government-furnished equipment). True system cost including C2 is $150-200K. Still, the $40K production cost demonstrates what's achievable with welded aluminum + twin outboard at scale.

### 4.4 ITAR Implication

Metal Shark HSMST is **ITAR-controlled** (US International Traffic in Arms Regulations). This means:
- Cannot be exported to Vietnam without State Department license
- License extremely unlikely for autonomous weapons-associated platform
- **Confirms the need for indigenous solution** — VN-TGT-SEA-001 fills a procurement gap that cannot be filled by import

---

## 5. QinetiQ L-CATT — Subsystem Teardown

### 5.1 Hull System

| Parameter | L-CATT Spec | VN-TGT-SEA-001 Comparison |
|-----------|-----------|---------------------------|
| Material | Roto-molded polyethylene | Similar (HDPE pontoon) |
| Construction | Single-piece rotomold | Rotomold or fabricated |
| LOA | 4.8 m | 6.0 m diameter |
| Beam | 2.4 m | 6.0 m (circular) |
| Weight | ~500 kg | 800 kg |
| Buoyancy | Foam-filled compartments | TPMS AM core (H variant) |

**RE insight:** L-CATT's roto-molded PE construction is the closest analog to VN-TGT-SEA-001's base hull concept. Key differences:
- L-CATT is **towed** (streamlined bow shape) vs VN-TGT-SEA-001 **anchored** (circular)
- L-CATT foam-fill provides basic buoyancy (3-10 hits before sinking) vs TPMS core (50+ hits)
- L-CATT RCS: 20-50 m² (insufficient) vs VN-TGT-SEA-001: 250-350 m²

### 5.2 Tow System (What VN-TGT-SEA-001 Eliminates)

| Component | L-CATT Spec | Cost | Risk |
|-----------|-----------|------|------|
| Tow cable | 750 m Dyneema (HMPE) | $2,250 | Cable failure during tow |
| Tow bridle | Y-configuration + swivel | $500 | Alignment affects RCS |
| Tow vessel | Must remain at 500-1000 m | $10,000/day (vessel ops) | **SAFETY: vessel in engagement zone** |
| Recovery | Winch + crane on tow vessel | $5,000 (equipment) | Sea state dependent |

**Total tow system cost per engagement:** ~$12,750 (cable wear + vessel ops)
**VN-TGT-SEA-001 saves:** All of this — anchor system costs only $950

### 5.3 Safety Analysis — Why L-CATT Fails for Missiles

```
L-CATT SAFETY GEOMETRY (MISSILE TEST)
═══════════════════════════════════════════════════════

                    ENGAGEMENT ZONE (5 km radius)
              ┌─────────────────────────────────────┐
              │                                     │
              │         ┌─────┐                     │
              │         │L-CATT│ ← Target            │
              │         └──┬──┘                     │
              │            │ 750m Dyneema           │
              │            │                        │
              │         ┌──┴──┐                     │
              │         │ TOW  │ ← Tow vessel       │
              │         │VESSEL│    IN DANGER ZONE!  │
              │         └─────┘                     │
              │                                     │
              └─────────────────────────────────────┘

Anti-ship missile warhead: 165 kg (C-802)
Kill radius: 50-100 m
Fragment radius: 500-1000 m

Tow vessel at 750 m = WITHIN FRAGMENT RADIUS

UNACCEPTABLE FOR MISSILE TESTING.
```

**VN-TGT-SEA-001 eliminates this risk entirely.** Tug deploys target, withdraws 5+ km, all personnel are outside the engagement zone. This is the single most important safety advantage.

---

## 6. IR Signature Subsystem — Deep Analysis

> **REMOVED (Rev B):** Entire IR signature subsystem eliminated. VN-TGT-SEA-001 is now radar-only. No propane burner, no Schwarz P panels, no IR emission. This section retained as reference for future IR variant if needed.

### 6.1 Emitter Technology Comparison

| Technology | Temperature | MWIR Output | Duration | Cost | Reusable | VN-TGT-SEA-001 |
|-----------|------------|-------------|----------|------|----------|-----------------|
| **Propane burner** | **1,135 deg C** | **Strong** | **30-60 min** | **$2,000** | **Yes** | **SELECTED** |
| Electric hot plate | 200-400 deg C | 6-40 W/sr | Unlimited (powered) | $5,000+ | Yes | Backup option |
| Pyrotechnic flare | 1,500+ deg C | Very strong | 5-30 sec | $50-200/each | No | Not suitable |
| Catalytic emitter | 300-600 deg C | Moderate | 1-4 hr | $3,000+ | Yes | Future option |

### 6.2 Propane Burner — Detailed Design

**Reference system:** Meggitt TIX infrared augmented target (1,135 deg C propane burner)

```
PROPANE BURNER CALCULATION FOR VN-TGT-SEA-001
═══════════════════════════════════════════════════════

Requirement: 250 deg C apparent temperature, 360 deg coverage, 30 min

Propane properties:
  Heating value: 46 MJ/kg (19,768 BTU/lb)
  Density: 0.493 kg/L (liquid)
  Combustion temp: 1,135 deg C (in air)

Burner thermal output estimate:
  Target surface area (visible): ~0.5 m^2 (burner + diffuser)
  Required radiance at 250 deg C: ~2 kW/m^2 (Stefan-Boltzmann)
  Total output needed: ~1 kW (accounting for 360 deg coverage)

But actual burner operates at 1,135 deg C (much hotter than
required 250 deg C apparent). The 250 deg C is the APPARENT
temperature as seen by IR seeker at range — due to atmospheric
attenuation and angular distribution.

Estimated fuel consumption:
  Conservative: 1.5 kg/hr (10 kW burner at 50% efficiency)
  For 30 min: 0.75 kg propane
  For 60 min: 1.5 kg propane

2 kg propane tank provides: 40-80 min duration
  (well within 30 min requirement, with 2x margin)

Propane tank specs:
  Capacity: 2 kg (4.4 lb) — standard camping size
  Tank weight: 3 kg (empty)
  Total loaded weight: 5 kg
  Cost: $50-100 (COTS)
```

### 6.3 360 deg IR Coverage

**Design challenge:** Propane burner is directional (flame points upward). Must provide IR signature visible from all horizontal approach angles.

**Solution: Central elevated burner with heat diffuser**

```
SIDE VIEW                           TOP VIEW

     ╔═══╗ ← Heat diffuser (Al cone)     ┌─────────────┐
     ║🔥 ║ ← Propane flame              / ◢    ╔═╗    ◣ \
     ╠═══╣ ← Burner assembly           │ ◢   ║🔥 ║   ◣  │
     ║   ║                             │      ╚═╝      │
     ║   ║ ← 2.5m steel mast          │ ◣            ◢ │
     ║   ║                              \ ◣          ◢ /
  ───╨═══╨───  Platform deck              └─────────────┘
  ▓▓▓▓▓▓▓▓▓▓▓                           8 corner reflectors
                                         around perimeter

Diffuser cone redirects heat 360 deg horizontally.
Missile approaches at ~5 m altitude → looks UP at burner.
Burner visible from all approach angles at any distance > 500m.
```

### 6.4 QinetiQ IR Hot Nose — Reference Design

| Parameter | Hot Nose Spec | VN-TGT-SEA-001 Adaptation |
|-----------|-------------|--------------------------|
| Fuel | Propane | Propane (same) |
| Heated element | 8.5 inch (216mm) hemisphere | Heat diffuser cone (~300mm) |
| Ignition | Remote from ground control | Timer-based (preset) |
| Reusability | Fully reusable nose cone | N/A (target destroyed) |
| Transport | No pyrotechnic restrictions | Same (propane = non-pyro) |
| Compatibility | Banshee drone interface | Custom mount on mast |

**Key adoption:** Timer-based ignition (not remote control) simplifies the system. Timer set at deployment to ignite T + transit time + safety margin. No radio link needed.

### 6.5 Schwarz P Enhancement (Phase H1 — Deferred)

The base propane burner provides a **point source** IR signature. A real ship has a **distributed** thermal pattern (hot funnel, warm hull, cool waterline). The Schwarz P thermal panel enhancement would distribute heat through internal channels to create this gradient pattern.

**Current assessment:** Base burner is sufficient for acceptance testing (missile seeker locks on any IR source above threshold). Schwarz P enhancement improves **realism** for advanced seekers but is not required for initial capability. Deferred to Phase H1/H2.

---

## 7. C-Target 3 — Design Philosophy Extraction

### 7.1 Principles Adopted for VN-TGT-SEA-001

The C-Target 3 Pahl-Beitz analysis revealed a core design philosophy: **"Deployable, repairable, producible"** with priorities:

```
C-Target 3 priority:     Deployability (5) > Cost (4) > Repairability (4) > Speed (3)
VN-TGT-SEA-001 priority: Safety (5) > Cost (4) > Signature (4) > Deployability (4)
```

| C-Target 3 Principle | Adopted for VN-TGT-SEA-001? | Adaptation |
|----------------------|------------------------------|------------|
| Modular bolt-together hull | **YES** | 5 x 3m sections (not centerline split) |
| Container-compatible dimensions | **YES** | 8m circular — requires sectional transport or flat-rack |
| Off-the-shelf engine | **N/A** | No engine (stationary target) |
| COTS electronics | **YES** | GPS beacon = $1,500 COTS |
| Low tooling investment | **YES** | HDPE rotomold or simple steel fab |
| >70% COTS components | **YES** | >80% COTS (reflectors + anchor = simple) |
| Field-repairable | **PARTIAL** | Expendable after missile hit; AM modules replaceable before engagement |
| 4 units per container | **TARGET** | Sections pack efficiently; 2-3 targets per container |

### 7.2 DFM Metrics Comparison

| DFM Metric | C-Target 3 | VN-TGT-SEA-001 (Base) | VN-TGT-SEA-001-H (AM) |
|-----------|-----------|----------------------|----------------------|
| Tooling cost | $30-50K | $20-30K | $20-30K + nTop license ($2K) |
| Assembly time | 4 hr (first), 2 hr (trained) | 2 hr (first), 1 hr (trained) | Same |
| Skills required | Aluminum welding, marine | HDPE fabrication, basic assembly | + AM service bureau (outsourced) |
| Unit cost | $50-80K | $32,000 | $40-45,000 |
| Production rate | 4-8/month | 8-10/month | 6-8/month (AM lead time) |
| Local content | ~40% (imported design) | 90% (base) | 85% (AM outsourced ASEAN) |

---

## 8. Technology Gap Matrix — VN-TGT-SEA-001 vs All Competitors

### 8.1 Subsystem-Level Comparison

| Subsystem | SINKEX | Hammerhead | HSMST | L-CATT | **VN-TGT-SEA-001-H** |
|-----------|--------|-----------|-------|--------|----------------------|
| **RCS system** | Ship hull (uncontrolled) | Optional add-on (10-50 m²) | Optional add-on (20-100 m²) | Patch panels (20-50 m²) | **8x AM reflectors (250-350 m², +/- 2dB 360 deg)** |
| **IR system** | Engine heat (variable) | Optional Hot Nose | Optional | Not standard | **Central propane burner (250 deg C, 360 deg, 30 min)** |
| **Flotation** | Ship hull | GRP hull (sinks if holed) | 5086 Al hull (sinks if holed) | Foam-fill PE (3-10 hits) | **TPMS core (50+ hits, "unsinkable")** |
| **Propulsion** | Ship engines | 135 HP MerCruiser | Twin 600 HP outboard | Towed (no propulsion) | **None (anchored)** |
| **C2 system** | Ship bridge | UTCS ($50-80K) | Proprietary (ITAR) | Passive (towed) | **Passive (GPS beacon, $1,500)** |
| **Mooring** | Drift or tow | Self-propelled | Self-propelled | Tow cable 750m | **Single anchor + 50m chain ($950)** |
| **Cost/unit** | $1-5M/test | ~$300,000 | ~$200,000 | $20-30,000 | **$32-45,000** |
| **Safety (missile test)** | HIGH (withdraw) | MEDIUM (C2 at 2-3 km) | MEDIUM (C2 at 2-3 km) | **LOW (tow at 500m)** | **HIGH (withdraw 5+ km)** |

### 8.2 Unique Capabilities (No Competitor Has)

1. **TPMS "unsinkable" flotation** — Survives 50+ hits. No competitor offers this. Enables target REUSE (5-10 engagements per unit).
2. **AM precision reflectors** — +/- 0.1 deg tolerance. 5-8 dB improvement over traditional. Reduces missile test failure rate.
3. **Fully passive operation** — No C2 system, no operator during engagement. Lowest operational complexity.
4. **Indigenous production** — 85-90% local content. Not dependent on ITAR/EAR export controls.

---

## 9. Design Parameter Extraction — VN-TGT-SEA-001 Specification Basis

### 9.1 Parameters Derived from RE Analysis

| Parameter | Value | Source |
|-----------|-------|--------|
| Reflector edge length | **0.8 m** — Rev B.1 | RCS formula: 8 x 23.2 m² = 186 m² peak, 250-350 m² effective |
| Reflector count | 8 | 45 deg spacing provides <= +/- 2 dB variation |
| Reflector material | AlSi10Mg (LPBF) | +/- 0.1 deg tolerance achievable |
| Reflector weight (each) | ~3 kg (AM with lattice backing) (now ~15 kg hybrid CNC/AM) | 40% lighter than solid 5mm Al |
| Anchor type | **Danforth/Bruce 30-50 kg** — Rev B | Universal seabed compatibility, $200 |
| Anchor weight | 300 kg | Holding force > SS 3 loads on 800 kg target |
| Chain | **12-16mm G30** — Rev B.1 hot-dip galvanized, 50 m | Scope 5:1 at 10 m depth |
| Swing circle | +/- 50 m | Catenary calculation verified |
| Hull form | Circular pontoon, **8.0 m** diameter — Rev B | Omnidirectional stability + RCS symmetry |
| Hull material | HDPE rotomold (base) | L-CATT demonstrates PE feasibility |
| Flotation | TPMS Gyroid PA12 core (H variant) | 36,000+ cells, <1% buoyancy loss after 50 hits |
| IR source | **REMOVED** (radar-only) — Rev B | 2 kg tank, 30-60 min, 250 deg C MWIR |
| IR coverage | **REMOVED** — Rev B | Missile approaches horizontal, sees heated cone |
| GPS beacon | COTS waterproof, 1 Hz, 8 hr battery | $1,500 import |
| Deployment | Tow by tug, anchor drop, withdraw | 30 min, 3-4 crew |

### 9.2 Cost Architecture (from RE)

| Subsystem | VN-TGT-SEA-001 Base | VN-TGT-SEA-001-H (AM) | Hammerhead Equivalent |
|-----------|---------------------|----------------------|---------------------|
| Hull/platform | $8,300 | $8,300 | ~$50,000 (GRP mold) |
| Propulsion | $0 | $0 | ~$15,000 (MerCruiser) |
| C2 system | $1,500 (GPS only) | $1,500 | ~$60,000 (UTCS) |
| RCS system | $9,100 (traditional) | $12,000-15,000 (AM) | ~$5,000 (optional) |
| IR system | $2,600 | $2,600 | ~$8,000 (Hot Nose) |
| Mooring | $950 | $950 | N/A (self-propelled) |
| Flotation (TPMS) | N/A | $3,000-10,000 | N/A |
| Assembly/QC | $6,500 | $6,500 | ~$30,000 |
| **TOTAL** | **$29,000-32,000** | **$35,000-45,000** | **~$168,000+** |

> **Rev B.1:** Unit cost revised to $35,640 @ 10 units. IR system removed ($0). Reflectors: hybrid CNC/AM at $13,000 for 8×. Mast system adds $1,430 (8 masts + sockets + assembly). Platform increased to 8.0m ($6,000-7,000). Total development budget: $292K.

---

## 10. Conclusions and Design Directives

### 10.1 Key RE Findings

1. **No competitor addresses the missile acceptance job.** All existing products are designed for gunnery training (moving targets, low RCS). VN-TGT-SEA-001 creates a new product category.

2. **Eliminating propulsion and C2 saves $75-140K per unit.** This is the anchored target's fundamental cost advantage over USV targets.

3. **360 deg signature is mandatory for anchored targets** (weathervaning on single-point mooring). This drives the 8-reflector perimeter array and central elevated IR burner design.

4. **AM provides quantifiable performance improvements:**
   - Reflectors: 5-8 dB RCS improvement (reduces missile test failure)
   - Flotation: 50x survivability improvement (enables reuse, $32-45K saved per reuse)
   - Combined ROI: AM investment ($8-13K per unit) recovered in single reuse

5. **L-CATT is the closest analog** (roto-molded PE, low cost, towed) but fails on RCS, safety, and survivability. VN-TGT-SEA-001 addresses all three failures.

6. **ITAR/EAR restrictions validate indigenous development.** HSMST (best USV target) cannot be exported to Vietnam. Hammerhead available but overpriced and wrong product category.

### 10.2 Design Directives for Phase 1

| Directive | Source | Priority |
|-----------|--------|----------|
| Use circular pontoon platform 8.0 m — Rev B (not rectangular) | Hammerhead RE: V-hull unnecessary; stability analysis | CRITICAL |
| Use 8 × 0.8m hybrid CNC/AM at 3-4m on masts — Rev B.1 | RCS formula + coverage analysis | CRITICAL |
| Use single-point concrete anchor + chain | Mooring analysis: simplest, cheapest, universal | HIGH |
| **REMOVED** — Rev B (radar-only) | IR analysis: 360 deg coverage at lowest cost | HIGH |
| Adopt TPMS PA12 flotation core (Phase H0 gate) | Survivability math: 50+ hits vs 3 for foam-fill | HIGH |
| Use AM LPBF for reflectors (Phase H1 gate) | Tolerance analysis: +/- 0.1 deg = 5-8 dB improvement | MEDIUM |
| Adopt C-Target 3 DFM philosophy | RE analysis: "deployable, repairable, producible" | HIGH |
| Design for 2-3 targets per 20ft container | C-Target 3 logistics concept | MEDIUM |

---

## Cross-References

- [[odi_analysis.md]] - ODI analysis (opportunity scores driving requirements)
- [[re_competitive_analysis.md]] - High-level competitive positioning
- [[hyperganic_feasibility.md]] - AM/TPMS technical feasibility
- [[../00_project_brief.md]] - Project brief with full specifications
- [[../../../references/Bia TL/VN_AST_MSL_001_Anchored_Target_Analysis.md]] - UIEF anchored target analysis
- [[../../../references/Bia TL/VN_AST_MSL_001_Competitive_Comparison.md]] - Competitive comparison
- [[../../../references/Target Drone/C-Target_3_PB_Reverse_Engineering_Worksheet.md]] - C-Target 3 RE
