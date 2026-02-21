---
project: VN-TGT-SEA-001
phase: 4
type: detail_design
document: "Deployment & Operations Manual"
version: 1.0
created: 2026-02-11
status: draft
lang: EN/VN
---

# Deployment & Operations Manual — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Document:** DOM-001 Rev 1.0
**Classification:** RESTRICTED
**Target Audience:** Naval deployment crews, test range operators
**Training Prerequisite:** 4 h classroom + 2 h hands-on per ERG-006
**Input:** [[PRAD_A7_architecture_definition.md]], [[PRAD_D8_design_structure.md]], [[DECS_C11_requirements_verification.md]], [[DECS_S12_standards_compliance.md]], [[OCP_P15_production_planning.md]], [[OCP_C14_cost_analysis.md]], [[../PROJECT_STATUS.md]]

---

## Document Conventions

Throughout this manual the following callout types are used:

> **WARNING:** Indicates a hazard that could result in serious injury or death if not avoided. STOP and read before proceeding.

> **CAUTION:** Indicates a condition that could result in equipment damage or mission failure.

> **NOTE:** Provides supplementary information, tips, or reminders.

---

## 1. Introduction

### 1.1 Product Description

The THANH TRI-H is a fixed, anchored sea target designed for anti-ship missile acceptance testing. It is a **radar-only, passive, expendable** platform that presents a frigate-class radar cross section (>1,000 m^2) at X-band (9.4 GHz) to radar-guided missile seekers. The target contains no active electronics except a GPS tracking beacon. It requires no operator presence during engagement. The target is **destroyed by missile impact** -- this is the intended outcome.

**Recoverable items after engagement:** Mooring kit (M7), tow kit (M8), GPS beacon (M6) if target survives (miss scenario).

### 1.2 System Overview -- Five Layers

```
SYSTEM LAYERS -- THANH TRI-H
=============================================
Layer 0: MOORING    Anchor + chain + rode + swivel (M7)
Layer 1: HULL       8.0 m HDPE circular pontoon, foam-filled (M1)
Layer 2: FRAME      S235 HDG steel structural frame (M2)
Layer 3: MASTS      8x HDG steel mast tubes, 3.0 m (M3)
Layer 4: REFLECTORS 8x hybrid AM/CNC corner reflectors (M4)
Layer 5: GPS        GNSS/Iridium beacon (M6)
Layer 6: TOW        Dyneema bridle + drogue (M8)
```

### 1.3 Key Specifications

| Parameter | Value |
|-----------|-------|
| Platform diameter | 8.0 m |
| Total displacement (on-platform) | 986 kg |
| Maximum displacement limit | 1,100 kg |
| RCS (X-band, 360 deg peak combined) | >=1,000 m^2 (30 dBsm) |
| RCS (360 deg average) | >=1,000 m^2 |
| RCS (360 deg minimum) | >=700 m^2 |
| Reflector edge length | 0.8 m |
| Number of corner reflectors | 8 at 45 deg spacing |
| Reflector height above waterline | 3.0-4.0 m |
| GPS beacon height above waterline | >=4.5 m |
| Deployment sea state | SS <=5 |
| Survival sea state (anchored) | SS 5-6 (72 h) |
| Survival wind | Beaufort 6-7 (22-33 kn mean) |
| GPS beacon endurance | >=72 h continuous |
| Water depth range | 10-80 m |
| Mooring system SWL | 5,800 kgf (19 mm G30 chain) |
| Tow speed (SS 5) | >=3.0 kn |
| Crew required | 4 personnel + vessel crew |
| Field deployment time (excl. transit) | ~155 min (2.5 h) |

### 1.4 Target Audience

This manual is intended for:
- **Naval deployment crews** responsible for loading, transporting, deploying, and recovering the target.
- **Test range operators** responsible for position monitoring, engagement authorization, and post-engagement debris recovery.
- **Maintenance personnel** responsible for pre-deployment inspection and inter-deployment storage.

### 1.5 Related Documents

| Document | Reference |
|----------|-----------|
| Architecture Definition | [[PRAD_A7_architecture_definition.md]] |
| Structural Analysis | [[PRAD_D8_design_structure.md]] |
| Requirements Verification | [[DECS_C11_requirements_verification.md]] |
| Standards Compliance | [[DECS_S12_standards_compliance.md]] |
| Production Planning | [[OCP_P15_production_planning.md]] |
| Cost Analysis | [[OCP_C14_cost_analysis.md]] |

---

## 2. Safety

### 2.1 General Safety Warnings

> **WARNING:** This system weighs 986 kg fully assembled. All lifting operations require certified lifting straps rated >=2,000 kg. Never position personnel under suspended loads.

> **WARNING:** All marine deployment operations carry risk of drowning. All personnel must wear approved life jackets at all times when on deck or working near the water's edge.

> **WARNING:** Do not deploy, recover, or tow the target in sea states greater than SS 5 (Hs > 2.5 m). Survival rating of SS 5-6 applies only to the anchored, unmanned target -- not to deployment crews working on or alongside the target.

> **WARNING:** Mooring chain and rode under tension store significant energy. Never stand in the bight of a line or chain under load. Maintain a safe distance of at least 2 m from loaded mooring hardware at all times.

### 2.2 Personnel Requirements

| Role | Minimum | PPE Required |
|------|---------|-------------|
| Deployment crew | 4 personnel | Life jacket (SOLAS-approved), non-skid steel-toe boots, chain-handling gloves (leather or Kevlar), hard hat (during crane operations), safety glasses |
| Vessel crew | Per vessel manning | Per vessel SOPs |
| Shore station operator | 1 person | N/A (shore-based) |

### 2.3 Sea State Limits

| Operation | Maximum Sea State | Maximum Wind | Notes |
|-----------|-------------------|-------------|-------|
| Deployment | SS <=5 (Hs <=2.5 m) | Bft 6 (<=27 kn) | Abort if deteriorating |
| Towing | SS <=5 | Bft 6 | <=3 kn tow speed at SS 5 |
| Recovery | SS <=4 (Hs <=1.25 m) | Bft 5 (<=21 kn) | Crew safety critical |
| Survival (anchored, unmanned) | SS 5-6 (Hs <=6.0 m) | Bft 6-7 (<=33 kn) | 72 h rated |

> **CAUTION:** DO NOT attempt deployment in SS >5. The target is rated for SS 5-6 SURVIVAL while anchored and unmanned, but crew safety during on-target work requires calmer conditions.

### 2.4 Hazard Summary

The following hazards were identified per MIL-STD-882E (ref. [[DECS_S12_standards_compliance.md]] Section 2.2):

| Hazard ID | Description | Risk Level | Mitigation |
|-----------|-------------|------------|------------|
| H-01 | Mooring failure -- target drifts into shipping lane | LOW | 19 mm G30 chain (128% SWL margin); GPS tracking; NOTAM broadcast |
| H-02 | Personnel injury during tow in heavy seas | MEDIUM | Dyneema SWL 8,000 kgf; max tow SS 5 at 3 kn; PPE mandatory |
| H-03 | Reflector/mast falls from mount in heavy seas | LOW | Clevis pin + R-clip + safety wire triple retention |
| H-04 | GPS beacon failure -- position unknown | LOW | 72 h Li-ion battery; IP67 enclosure; 4.5 m AWL mount |
| H-05 | Target capsizes before engagement | LOW | GM = 207.9 m -- physically impossible to capsize |
| H-06 | Marine debris contamination post-engagement | LOW | HDPE + PU foam non-toxic; debris recovery plan (Section 9) |
| H-07 | Anchor drags -- target off station at firing | LOW | 75-100 kg Danforth; GPS monitors drift >50 m |
| H-08 | Tow line parts -- target adrift during transit | LOW | Dyneema SWL 8,000 kgf (5.3:1 SF); GPS active during tow |

### 2.5 Safety-Critical Items (SCI) -- Inspect Before Every Deployment

The following items are classified as safety-critical per [[DECS_S12_standards_compliance.md]] Section 2.3. Inspect ALL items before every deployment. Record inspection results in the Pre-Deployment Checklist (Appendix A).

| SCI # | Item | Inspection Method | Accept Criteria | Reject If |
|-------|------|-------------------|-----------------|-----------|
| SCI-01 | Mooring chain (19 mm G30 HDG) | Visual inspection of every link | No visible corrosion penetrating base metal; no distorted links | Any link shows cracks, deep corrosion pitting, or deformation |
| SCI-02 | Pad eye assembly (eye + backing plate + bolts) | Visual + torque check (M16 at 200 N-m) | Full-penetration weld intact; all 4 bolts torqued | Visible weld cracking; loose bolts; ring distortion |
| SCI-03 | Tow line (16 mm Dyneema) | Visual inspection of full length + spliced eyes | No cut fibers; no UV degradation; tuck count >=24 per splice | Visible chafe >10% of diameter; any cut strands; splice slippage |
| SCI-04 | Anchor (75-100 kg Danforth) | Visual + pivot check | Flukes pivot freely; shank straight +/-2 deg; shackle pin secure | Bent flukes; cracked shank; frozen pivot |
| SCI-05 | GPS beacon battery | Voltage check before each deployment | Voltage above cutoff (per manufacturer spec); >=72 h remaining capacity | Voltage below minimum; battery swollen or damaged |
| SCI-06 | Mast locking pins (8x M12 clevis pins) | Visual and tactile during field erection | Pin fully inserted; R-clip engaged; cannot be pulled out by hand | Pin incomplete engagement; missing R-clip; bent pin |

### 2.6 Emergency Procedures

**Mooring failure (target breaks free):**
1. GPS beacon continues transmitting position for up to 72 h.
2. Shore station monitors drift direction and speed.
3. Notify range control and Coast Guard immediately.
4. Broadcast updated NOTAM with drift track.
5. Dispatch recovery vessel if conditions permit (SS <=4).
6. Target is unsinkable (foam buoyancy = 3.0x displacement) -- it will float until recovered.

**Tow line failure (target adrift during transit):**
1. GPS beacon is active -- shore station tracks position.
2. Tow vessel circles to maintain visual contact.
3. Reconnect tow using spare shackle and bridle leg if conditions permit.
4. If reconnection not possible, deploy marker buoy and standby until conditions improve.

**Man overboard:**
1. Execute vessel MOB procedure immediately.
2. Deploy life ring and recovery equipment.
3. All target operations cease until person is recovered.
4. Resume operations only after crew accountability confirmed.

---

## 3. System Description

### 3.1 Module Descriptions

#### M1: Hull Assembly

```
M1 HULL — 8.0 m HDPE RING PONTOON
=============================================

     TOP VIEW:                          CROSS-SECTION:

     ╭────────────────────╮             ┌═══════════════════┐
    ╱    central deck      ╲            │  10-12 mm HDPE    │
   │    (open / grating)    │           │ ┌───────────────┐ │
   │                        │           │ │  Closed-cell  │ │ 500 mm
   │    ╭──── 7.0 m ────╮  │           │ │  PU foam fill │ │ depth
   │    │  inner void    │  │           │ │  (80% fill)   │ │
   │    ╰────────────────╯  │           │ └───────────────┘ │
    ╲                      ╱            └═══════════════════┘
     ╰────────────────────╯                 ~500 mm width
           8.0 m OD
```

- **Configuration:** 8.0 m diameter circular ring pontoon, 0.5 m depth, 2-section (joined at IF-07 for transport).
- **Material:** PE100 carbon-black stabilized HDPE, 10-12 mm wall thickness.
- **Foam fill:** Closed-cell PU rigid foam, 35-50 kg/m^3, 80% fill factor. Provides 3.0:1 buoyancy ratio -- **unsinkable** even with total hull breach.
- **Mass:** ~350 kg (shell ~200 kg, foam ~100 kg, deck reinforcements ~50 kg).
- **Draft at 986 kg:** 19.1 mm (freeboard 481 mm).
- **Scuppers:** 8x flush-mount drains at inner hull edge for self-draining deck.

#### M2: Structural Frame Assembly

```
M2 FRAME — S235 HDG STEEL
=============================================

     TOP VIEW (inside hull):

          radial beam
     ╭────────┼────────╮
    ╱  [S]   [S]   [S] ╲      [S] = deck socket (8x)
   │   [S]  [PAD]  [S]  │     [PAD] = central mooring pad eye
   │        EYE          │     [T] = tow padeye (2x)
    ╲  [S]        [S]  ╱
     ╰──[T]────[T]──╯
         perimeter ring (L50x50x5)
```

- **Configuration:** Perimeter angle ring + radial cross members + 8 welded deck sockets + central mooring pad eye (200x200x14 mm backing plate, upgraded per D8) + 2 tow padeyes.
- **Material:** S235 mild steel, hot-dip galvanized >=85 um per ASTM A123.
- **Mass:** ~150 kg.
- **Deck sockets:** 8x at R=3,200 mm from center, 45 deg spacing. Socket ID 62 mm, depth 200 mm. Drain hole at bottom.
- **Pad eye:** Central, 200x200 mm base plate, 25 mm dia ring (80 mm ID), proof load tested to 1.5x SWL (6,804 kgf) before first deployment.

#### M3: Mast Assembly (x8 identical)

```
M3 MAST — HDG STEEL TUBE
=============================================

         ┌──────┐  Top plate: 120x120x8 mm
         │      │  (4x M10 bolt holes + 2x dowel holes for IF-04)
         └──┬───┘
            │     60 mm OD x 4 mm wall, S235 HDG tube
            │     3,000 mm length above deck
            │
            │     Locking pin hole at 150 mm above base plate
       ____│____
      / ___│___ \  4x base gussets (6 mm plate, 80x40 mm triangle)
     / /   │   \ \
    /_/____│____\_\
    ┌──────────────┐  Base plate: 150x150x8 mm
    │  4x M12 bolt │  (engages deck socket top flange)
    └──────────────┘
```

- **Mass:** 16.3 kg per unit (tube ~14.5 kg + plates ~1.8 kg).
- **Engagement:** Mast tube (60 mm OD) slides into socket (62 mm ID) with 1.0-1.5 mm radial clearance. Base plate seats on socket flange.
- **Locking:** M12 clevis pin + R-clip + safety wire.
- **Field erection time:** <2 min per mast by 2 persons.

#### M4: Reflector Assembly (x8 identical)

```
M4 REFLECTOR — HYBRID AM/CNC CORNER REFLECTOR
=============================================

          ╱│
         ╱ │ Face B (CNC 6061-T6, 800x800x3 mm)
        ╱  │
       ╱   │
      ╱  ╱─┘
     ╱  ╱  Face C
    ╱  ╱
   ╱__╱
    Face A

   AM AlSi10Mg frame holds 3 faces
   in orthogonal alignment <=+/-0.1 deg

   Individual RCS: >=152 m^2 per reflector
   Combined 8x: >=1,000 m^2 (360 deg)
```

- **Frame:** 1x LPBF AlSi10Mg monolithic frame, T5 heat treated, Type III hard anodize >=25 um.
- **Face plates:** 3x CNC 6061-T6 aluminum, 800x800x3 mm, fly-cut to Ra <=10 um, Type II anodize >=10 um.
- **Assembly:** 12x M6 SS bolts + Nylock nuts + 6x alignment dowel pins + safety wire.
- **Orthogonality:** <=+/-0.1 deg between faces (100% verified at factory).
- **Mass:** 15.0 kg per unit.

#### M5: Mast-Reflector Unit (x8 pre-assembled)

- **Configuration:** M3 mast + M4 reflector, pre-assembled at factory at IF-04 interface.
- **Mass:** 31.3 kg per unit.
- **Handling:** 2-person lift (31.3 kg). Insert into deck socket, secure locking pin, attach safety wire.
- **Galvanic isolation at IF-04:** Nylon bushings + nylon washers + Tef-Gel anti-seize between HDG steel mast and anodized aluminum reflector.

#### M6: GPS Beacon Assembly

- **Configuration:** COTS GNSS module + Iridium SBD modem in IP67/68 waterproof enclosure, Li-ion battery (20 Wh, 72 h endurance), SS316 U-bolt clamp bracket.
- **Mount position:** Designated GPS mast (M5-1) at >=4.5 m AWL.
- **Mass:** 5 kg.
- **Activation:** Power switch inside enclosure; verify GPS fix + Iridium SBD link to shore station before departure.
- **Battery:** Field-replaceable pack with waterproof quick-disconnect connector. Swap before each deployment.

> **NOTE:** Ship the GPS beacon with battery disconnected. Connect battery and activate only during pre-deployment preparation.

#### M7: Mooring Kit (3 depth variants)

| Kit | Water Depth | Chain | Rode | Anchor | Total Mass | Scope |
|-----|-------------|-------|------|--------|------------|-------|
| **Kit A** (Shallow) | 10-20 m | 30 m x 19 mm G30 HDG (all-chain) | None | 75 kg Danforth | ~330 kg | 5:1 to 6:1 |
| **Kit B** (Medium) | 20-40 m | 20 m x 19 mm G30 HDG | 60 m x 24 mm polyester | 75 kg Danforth | ~260 kg | Hybrid |
| **Kit C** (Deep) | 40-80 m | 15 m x 19 mm G30 HDG | 100 m x 24 mm polyester | 75 kg Danforth | ~270 kg | Hybrid |

**All kits include:** HDG jaw-jaw swivel (SWL 5,000 kgf), 3x HDG bow shackles (SWL 5,000 kgf), 2x SS316 thimbles, trip line (50 m, 10 mm polypropylene + orange surface buoy), mousing wire (1 mm galvanized).

> **CAUTION:** Select the correct mooring kit for the deployment site water depth. Using a shallow-water kit in deep water results in insufficient scope and anchor dragging.

#### M8: Tow Kit

- **Bridle:** 2-leg Dyneema SK75, 16 mm, 12-strand, 2x 25 m legs, spliced soft eyes with SS316 thimbles.
- **Drogue:** 600 mm dia conical, canvas/nylon, with SS ring + swivel.
- **Hardware:** 2x HDG bow shackles (16 mm pin, SWL 3,500 kgf), 1x drogue shackle (12 mm pin), mousing wire.
- **Mass:** 15 kg (rope ~8 kg, drogue ~4 kg, hardware ~3 kg).
- **Configuration:** 2-point attachment at IF-06 tow padeyes (port and starboard, 60 deg spread).

### 3.2 Interface Descriptions

| IF-ID | Connection | Type | Assembly Phase | Criticality |
|-------|------------|------|----------------|-------------|
| IF-01 | Frame (M2) to Hull (M1) | 84x M12 SS316 bolts, 300 mm spacing, torque 40 N-m | Factory | HIGH |
| IF-02 | Mooring chain (M7) to Frame pad eye (M2) | Bow shackle through pad eye ring, moused with SS wire | Field | CRITICAL |
| IF-03 | Mast base (M3) to Deck socket (M2) | Socket-insert + M12 clevis pin + R-clip + safety wire | Field | HIGH |
| IF-04 | Reflector (M4) to Mast top plate (M3) | 4x M10 bolts + Nordlock + Nylock + 2x dowel pins | Factory | HIGH |
| IF-05 | GPS beacon (M6) to GPS mast (M3) | 2x M8 SS316 U-bolts, torque 15 N-m | Factory/Field | LOW |
| IF-06 | Tow bridle (M8) to Hull tow padeyes (M1) | Bow shackle through padeye ring, moused with SS wire | Field | MEDIUM |
| IF-07 | Hull section 1 to Hull section 2 | 34x M12 SS316 bolts + EPDM gasket + Sikaflex seal | Factory/Field | HIGH |

---

## 4. Pre-Deployment Checklist

Perform all items below at the quayside or staging area BEFORE departing for the deployment site. Use the tear-out checklist in Appendix A for field recording.

### 4.1 Component Inventory Verification

- [ ] Hull assembly (M1) -- 2 sections or 1 piece, joined and leak-tested
- [ ] 8x Mast-reflector units (M5) -- count and serial number check
- [ ] GPS beacon (M6) -- with charged battery pack + spare battery
- [ ] Mooring kit (M7) -- correct depth variant selected (Kit A / B / C)
- [ ] Tow kit (M8) -- bridle + drogue + shackles
- [ ] Spare parts kit (Appendix C)
- [ ] Tool kit (Appendix D)
- [ ] This manual in waterproof pouch
- [ ] Pre-deployment checklist form (Appendix A)

### 4.2 Visual Inspection

- [ ] Hull: No cracks, punctures, or UV degradation; hull section joint (IF-07) gasket intact and bolts torqued
- [ ] Frame: No visible corrosion penetrating HDG zinc coating; all 8 deck sockets clear of debris
- [ ] Masts: Straight (no bowing >2 mm/m); base and top plates perpendicular; locking pin holes clear
- [ ] Reflectors: Face plate surfaces clean, no scratches deeper than anodize thickness; safety wire intact on all bolt pairs
- [ ] Locking pins: 8x M12 clevis pins present with R-clips; not bent or corroded
- [ ] Pad eye (SCI-02): Ring not distorted; weld intact; M16 bolts torqued to 200 N-m
- [ ] Tow padeyes: 2x rings intact; M12 bolts secure

### 4.3 Safety-Critical Item Inspection

Inspect all 6 SCIs per Section 2.5. Record results on checklist form.

> **WARNING:** Do NOT deploy if any SCI fails inspection. Replace or repair the failed item before proceeding.

### 4.4 GPS Beacon Activation

1. Open IP67 enclosure (4x screws or latch, per model).
2. Connect Li-ion battery pack to quick-disconnect connector.
3. Close and seal enclosure. Verify seal is seated.
4. Power on beacon (press and hold power button 3 seconds).
5. Wait for GPS fix (LED indicator or shore station confirmation) -- max 5 minutes.
6. Confirm Iridium SBD message received at shore station via radio.
7. If no fix after 5 minutes: check antenna orientation (must face skyward), check for obstructions.

### 4.5 Mooring Kit Selection

Select mooring kit based on deployment site water depth:

| Site Depth | Kit | Chain Length | Rode Length | Total Scope | Anchor |
|------------|-----|-------------|-------------|-------------|--------|
| 10-20 m | **Kit A** | 30 m x 19 mm G30 (all-chain) | None | 5:1 to 6:1 | 75 kg Danforth |
| 20-40 m | **Kit B** | 20 m x 19 mm G30 | 60 m x 24 mm polyester | Hybrid | 75 kg Danforth |
| 40-80 m | **Kit C** | 15 m x 19 mm G30 | 100 m x 24 mm polyester | Hybrid | 75 kg Danforth |

> **NOTE:** For mud or soft seabed, upgrade to 100 kg Danforth anchor. A 75 kg Danforth holds ~1,500 kgf in sand but only ~675 kgf in mud, which is insufficient. Verify seabed type from nautical charts or local knowledge before selecting anchor.

### 4.6 Weather Forecast Check

- [ ] Obtain 48 h marine weather forecast for deployment area.
- [ ] Confirm sea state <=SS 5 for deployment window.
- [ ] Confirm no tropical storm or typhoon warnings within 72 h.
- [ ] Record forecast on checklist: Wind ______ kn, Seas ______ m, Trend ______.

### 4.7 Support Vessel Requirements

| Requirement | Minimum Specification |
|-------------|----------------------|
| Deck space | Sufficient for hull sections (4.0 m x 4.0 m per half) |
| Lifting | Crane >=1 ton capacity OR ramp launch capability |
| Winch | For controlled anchor lowering and anchor setting |
| Echo sounder | Operational, for depth verification at site |
| Navigation | GPS chartplotter, VHF radio |
| Safety | Life rings, MOB equipment, first aid kit |

---

## 5. Loading Procedure

### Step D-01: Pre-Deployment Briefing (15 min)

**Crew:** All 4 crew + vessel crew.

1. Review deployment plan: target coordinates, water depth, mooring kit selected.
2. Confirm sea state forecast (SS <=5 for deployment window).
3. Assign roles:
   - **Crew 1 (Lead):** Mooring connection, pad eye shackling, final inspection.
   - **Crew 2:** Mast erection, locking pin verification.
   - **Crew 3:** Mast erection assistant, equipment passing from vessel.
   - **Crew 4:** GPS beacon monitoring, photography, safety watch.
4. Review abort criteria: SS >5, equipment failure, personnel injury.
5. Confirm communications plan: VHF channel to shore station.

### Step D-02: Load Hull onto Vessel (30 min)

**Crew:** 4 + crane operator.

> **WARNING:** Hull mass is ~490 kg per section (2-section) or ~980 kg assembled. Use certified lifting straps rated >=2,000 kg. Hard hats mandatory during crane operations.

1. Position hull sections on flatbed truck or quayside.
2. Attach lifting straps through scupper holes or dedicated lifting points (4-point lift).
3. Crane lift hull section onto vessel deck (or ramp launch into water alongside vessel).
4. If 2-section hull: load both sections and join on vessel deck or in water alongside.
5. Secure hull on deck with ratchet straps (8x, 2T WLL) to prevent shifting during transit.

> **NOTE:** For ramp launch, float hull in calm water alongside vessel. Secure to vessel cleats with spring lines.

### Step D-03: Load Mooring Kit (15 min)

**Crew:** 2.

> **CAUTION:** Chain handling gloves MANDATORY. 19 mm G30 chain weighs 7.9 kg/m -- finger pinch hazard at every link.

1. Load anchor onto vessel deck. Secure upright against bulkhead.
2. Flake chain on vessel deck in figure-eight pattern for tangle-free deployment.
3. Flake polyester rode (Kit B or C) on top of chain, coiled neatly.
4. Place swivel, shackles, thimbles, and mousing wire in accessible kit bag.
5. Attach trip line and surface buoy to anchor crown.

### Step D-04: Load Mast-Reflector Units and Tow Kit (15 min)

**Crew:** 2.

> **CAUTION:** Each M5 unit weighs 31.3 kg. Use 2-person lift. Do NOT drag reflector face plates across any surface -- scratches degrade RCS.

1. Transfer 8x M5 units from padded vertical rack to vessel deck rack.
2. Secure M5 units in padded vertical rack on vessel deck (foam spacers between reflectors).
3. Load tow kit bag (M8) on deck.
4. Load spare parts kit and tool kit.
5. Verify all 8 clevis pins and R-clips are in the tool kit or attached to their masts.

### Step D-05: Activate GPS Beacon (5 min)

**Crew:** 1.

1. If not already activated per Section 4.4, power on GPS beacon now.
2. Verify GPS fix acquired (shore station confirms position accuracy <=+/-5 m).
3. Confirm Iridium SBD message received at shore station.
4. Record beacon serial number and activation time on checklist.

> **WARNING:** Confirm shore station is receiving GPS position BEFORE departing quayside. Do not depart without confirmed GPS link.

---

## 6. Mooring Deployment Procedure

### Step D-06: Transit to Target Site (variable, 1-4 h)

**Crew:** Vessel crew.

1. Vessel transits to deployment coordinates.
2. Monitor weather en route. **Abort and return if sea state deteriorates above SS 5.**
3. On arrival, confirm water depth with echo sounder. Record: ______ m.
4. Verify depth matches selected mooring kit range (Kit A: 10-20 m, Kit B: 20-40 m, Kit C: 40-80 m).

> **CAUTION:** If actual depth differs from expected, switch to appropriate mooring kit or abort. Do NOT deploy with incorrect scope.

### Step D-07: Deploy Anchor (30 min)

**Crew:** 3 + vessel crew.

1. Position vessel at target coordinates, heading into wind/current.
2. Attach anchor to bottom of chain using bow shackle. Mouse shackle pin with SS wire.
3. Attach surface buoy and trip line to anchor crown ring.
4. Lower anchor over the side using vessel winch for controlled descent. **Keep hands clear of chain.**
5. Pay out chain and rode to full scope:

| Depth | Scope Ratio | Total Length (chain + rode) |
|-------|-------------|---------------------------|
| 15 m | 5:1 to 6:1 | 75-90 m chain (Kit A, all-chain) |
| 30 m | Hybrid | 20 m chain + 60 m rode = 80 m (Kit B) |
| 50 m | Hybrid | 15 m chain + 100 m rode = 115 m (Kit C) |

6. Attach pick-up buoy to top of rode/chain with 5 m pick-up line.

> **WARNING:** Keep all personnel clear of running chain. Do NOT attempt to grab or guide chain with hands during deployment. Use vessel winch brake to control pay-out speed.

### Step D-08: Set Anchor (15 min)

**Crew:** Vessel crew.

1. Once all chain/rode is deployed, vessel backs down slowly on mooring.
2. Increase engine load gradually to 2x working load (~1,160 kgf) for 5 minutes.
3. Monitor GPS position for anchor drag -- if position shifts >10 m, anchor is NOT set.
4. If anchor drags: haul up, reposition, and re-deploy. Consider heavier anchor (100 kg).
5. If anchor holds for 5 minutes with no position shift: anchor is SET.

> **CAUTION:** Do NOT exceed 2x working load during anchor setting. Monitor vessel tension gauge. Excessive force may damage the mooring system.

### Step D-09: Confirm Anchor Set (5 min)

**Crew:** 1.

1. Return vessel to neutral throttle.
2. Verify vessel drifts back to position directly above or near anchor (confirms anchor holding).
3. Label pick-up buoy: "MOORING -- DO NOT REMOVE -- [Project Code] -- [Date]".
4. Record anchor position on GPS: Lat ______ Lon _______.

---

## 7. Target Deployment Procedure

### Step D-10: Position Target Alongside Mooring Buoy (15 min)

**Crew:** 2 + vessel crew.

1. If target is on vessel deck: launch target into water alongside vessel using crane or ramp.
2. If target is being towed: maneuver target to mooring buoy position.
3. Hold target alongside pick-up buoy using vessel lines and fenders.

> **CAUTION:** Place fenders between target hull and vessel to prevent HDPE hull damage.

### Step D-11: Connect Mooring (IF-02) (10 min)

**Crew:** 2.

1. Pick up mooring pick-up buoy from water.
2. Haul pick-up line onto vessel or target deck to access top of mooring chain/rode.
3. Pass mooring top end through vessel fairlead to target central pad eye.
4. Insert bow shackle through pad eye ring (80 mm ID) and mooring chain/rode top eye.
5. Tighten shackle pin fully using shackle key.
6. Mouse shackle pin with SS wire (wrap 3 turns through pin hole and shackle body, twist tight).

> **WARNING:** Ensure shackle pin is FULLY SEATED and MOUSED before releasing target from vessel. An unmoused shackle can vibrate open under wave loading, resulting in mooring loss (H-01).

7. Verify connection visually: shackle closed, pin tight, mousing wire secure.

### Step D-12: Release Target from Vessel (5 min)

**Crew:** 2.

1. Cast off all vessel lines holding target.
2. Allow target to drift to mooring equilibrium position under current/wind.
3. Observe target for 2 minutes. Verify target weathervanes freely 360 deg on mooring swivel.

> **NOTE:** If target does NOT weathervane (hangs at fixed angle), swivel may be seized. Reconnect and inspect swivel before continuing.

### Step D-13: Erect 8x Mast-Reflector Units (IF-03) (20 min)

**Crew:** 2 on target deck + 1 passing units from vessel.

> **CAUTION:** Wear non-skid footwear on wet deck. Target deck may be slippery from wave wash. Work in bow-to-stern sequence (M5-1 through M5-8).

For EACH of the 8 mast-reflector units, perform the following steps:

1. **Pass:** Crew 3 passes M5 unit from vessel deck to Crew 1 on target deck (31.3 kg, 2-person handoff across gap). Use line assist if gap >1 m.
2. **Position:** Crew 1 and Crew 2 hold M5 unit vertically over the next deck socket.
3. **Insert:** Push mast tube (60 mm OD) down into deck socket (62 mm ID). Push firmly until base plate seats flush on socket flange.
4. **Align:** Rotate mast slightly until clevis pin holes in socket wall and mast tube align (visible through pin hole).
5. **Pin:** Insert M12 clevis pin through aligned holes. Push fully in until pin head is flush against socket wall.
6. **Clip:** Snap R-clip onto protruding end of clevis pin to prevent withdrawal.
7. **Wire:** Loop 0.8 mm SS safety wire from pin head to mast base plate eyelet. Twist tight (3 turns minimum).
8. **Verify:** Tug mast laterally -- it should be firmly fixed. Pin must not slide.
9. **Repeat** for all 8 units. Estimated time: 2.5 min per mast x 8 = 20 min total.

> **NOTE:** If a mast tube does not slide smoothly into socket, check socket for debris (sand, paint flakes). Clear with a rag or wire brush. Apply Tef-Gel lubricant to socket bore if stiff.

### Step D-14: Verify All Locking Pins (3 min)

**Crew:** 1.

1. Walk around entire target deck perimeter.
2. Visually confirm for each of 8 masts:
   - [ ] Clevis pin fully inserted
   - [ ] R-clip engaged on pin end
   - [ ] Safety wire attached from pin to base plate
3. Count: 8 pins, 8 R-clips, 8 safety wires. All present.
4. Record on checklist.

### Step D-15: Verify GPS Beacon (2 min)

**Crew:** 1.

1. Visually confirm GPS beacon (M6) is mounted on designated mast (M5-1) with antenna facing skyward.
2. Call shore station on VHF radio: "Shore station, this is [vessel call sign]. Confirm GPS beacon transmitting from target [serial number]."
3. Shore station confirms: position received, accuracy within +-5 m. Record time: _______.

### Step D-16: Disconnect Tow Bridle (5 min)

**Crew:** 2.

(If tow bridle was used for transit to deployment site.)

1. Unshackle bridle legs from hull tow padeyes (IF-06) -- 2 shackles.
2. Recover bridle and drogue onto vessel deck.
3. Coil and stow bridle in rope bag.

### Step D-17: Final Visual Inspection from Vessel (10 min)

**Crew:** 1 (observer) + vessel crew.

1. Vessel moves clear of target (50 m standoff).
2. Circle target at 50 m distance at slow speed.
3. Verify visually:
   - [ ] All 8 mast-reflector units vertical and intact
   - [ ] No visible damage to hull, frame, or reflectors
   - [ ] Mooring line taut (target on station)
   - [ ] Target floating level (no list or trim)
   - [ ] GPS beacon visible at top of designated mast
4. Photograph target from 4 cardinal directions (N, E, S, W) for QC records.
5. Record target condition as: SATISFACTORY / UNSATISFACTORY.

### Step D-18: Depart and Establish Exclusion Zone (5 min)

**Crew:** Vessel crew.

1. Vessel departs target area.
2. Shore station broadcasts NOTAM (Notice to Mariners):
   - Target position: Lat ______ Lon ______
   - Exclusion radius: **5 km**
   - Duration: until engagement complete and debris cleared
   - Contact: [range control frequency/phone]
3. Confirm NOTAM broadcast before leaving area.

> **WARNING:** Do NOT leave the deployment area until NOTAM has been confirmed as broadcast. Unannounced targets are a navigation hazard.

**TOTAL FIELD DEPLOYMENT TIME: ~155 min (2.5 h), excluding transit.**

---

## 8. Post-Deployment Monitoring

### 8.1 GPS Position Tracking Protocol

1. Shore station monitors GPS beacon position continuously via Iridium SBD.
2. Log position at 1 Hz (transmitted in periodic bursts per beacon configuration).
3. Display position on range control chart with exclusion zone overlay.

### 8.2 Position Drift Limits

| Condition | Action |
|-----------|--------|
| Drift <10 m from set position | NORMAL -- mooring scope allows swing with tide/current |
| Drift 10-50 m from set position | MONITOR -- may indicate current shift or scope elongation |
| Drift >50 m from set position | **INVESTIGATE** -- possible anchor drag. Notify range control. Dispatch vessel to check mooring if conditions permit. |

### 8.3 Weather Monitoring

1. Obtain updated marine weather forecast every 12 hours during anchored period.
2. If forecast SS >6 or wind >Bft 8: notify range control. Consider early engagement or recovery.
3. Target is rated for SS 5-6 (72 h). Conditions beyond SS 6 exceed design envelope.

### 8.4 Go/No-Go Decision for Engagement

| Criterion | GO | NO-GO |
|-----------|-----|-------|
| Target on station (drift <50 m) | YES | NO -- investigate mooring |
| GPS beacon transmitting | YES | NO -- cannot confirm position for safety |
| Sea state at engagement | SS <=6 | SS >6 -- reschedule |
| Exclusion zone clear (5 km) | YES | NO -- clear zone before firing |
| NOTAM in effect | YES | NO -- rebroadcast NOTAM |

---

## 9. Recovery Procedure (Post-Engagement)

### 9.1 Debris Recovery

> **CAUTION:** Approach debris field from upwind. Watch for floating sharp metal fragments (aluminum face plates, steel frame sections).

1. Wait minimum 30 minutes after impact before approaching debris field.
2. Support vessel approaches from upwind at slow speed.
3. Visual survey: identify large floating debris (HDPE hull sections, foam blocks).
4. Collect debris using boat hook, net, or grappling line.
5. Focus on recovering:
   - GPS beacon (M6) -- if still floating and transmitting
   - Large HDPE hull sections -- to prevent navigation hazard
   - Metal fragments >0.5 m -- to prevent fouling of fishing nets
6. Record debris field extent and photograph for post-engagement analysis.

### 9.2 Mooring Recovery

1. Locate mooring pick-up buoy (orange, labeled with project code).
2. Pick up buoy; haul pick-up line onto vessel.
3. Disconnect rode/chain from destroyed target pad eye (if target remnant attached, cut free).
4. Winch chain + rode onto vessel deck.
5. Retrieve anchor using trip line: pull trip line to flip anchor and break out.
6. If trip line is parted or anchor is deeply buried: use vessel winch to haul vertically on chain. If anchor does not break free at 2x anchor weight, mark position for later recovery with divers.
7. Inspect recovered mooring components for reuse:
   - Chain: check all links for damage. Replace if any link is stretched or cracked.
   - Rode: check for chafe. Cut and re-splice if surface damage >10% of diameter.
   - Anchor: check flukes and shank for bending.
   - Shackles/swivel: check for deformation. Replace mousing wire.

### 9.3 GPS Beacon Recovery

If target survives (miss scenario) or beacon is found floating in debris:

1. Retrieve beacon from water or from mast (if target intact).
2. Power off beacon (press and hold power button 3 seconds).
3. Open enclosure, disconnect battery.
4. Download position log data via USB (per manufacturer instructions).
5. Inspect enclosure seal for water ingress.
6. Replace battery pack. Reseal enclosure. Return to inventory for next deployment.

### 9.4 Tow Recovery (Miss Scenario -- Target Intact)

If the target survives engagement (missile miss or exercise cancellation):

1. Approach target from downwind at slow speed.
2. Connect tow bridle (M8) to hull tow padeyes (IF-06) -- 2x bow shackles, moused with SS wire.
3. Disconnect mooring: unshackle chain/rode from pad eye (IF-02).
4. Buoy mooring top end for separate recovery.
5. Deploy trailing drogue if sea state >SS 3.
6. Tow target to port at speed per Section 11.2.

---

## 10. Recovery Procedure (No-Engagement / Exercise)

Full target recovery when target is NOT engaged (exercise cancellation, weather abort, or training deployment).

### 10.1 Preparation

1. Confirm sea state <=SS 4 before beginning recovery operations.
2. Deploy support vessel to target location.

### 10.2 Remove Mast-Reflector Units (reverse of D-13)

**Crew:** 2 on target deck + 1 on vessel.

For EACH of the 8 mast-reflector units (work stern-to-bow, reverse of deployment):

1. Remove safety wire from pin-to-base plate connection (cut with wire cutters).
2. Remove R-clip from clevis pin.
3. Pull clevis pin out of socket wall and mast tube.
4. Lift M5 unit vertically out of deck socket (2-person lift, 31.3 kg).
5. Pass M5 unit to Crew 3 on vessel deck. Place in padded vertical rack.
6. Repeat for all 8 units. Estimated time: 3 min per mast x 8 = 24 min.

### 10.3 Disconnect Mooring

1. Connect tow bridle (M8) to hull tow padeyes (IF-06) before disconnecting mooring.
2. Unshackle mooring chain/rode from pad eye (IF-02).
3. Buoy mooring top end for separate recovery.
4. Vessel holds target on tow while mooring is recovered separately (or left for later).

### 10.4 Tow to Shore

1. Tow target to port per Section 11.
2. Haul target onto ramp or crane-lift onto flatbed at quayside.

### 10.5 Disassemble for Storage

1. If hull is 2-section: unbolt IF-07 joint (34x M12 bolts), separate sections, stack on pallets.
2. Bundle 8x mast tubes in steel cradle (if M5 units were not already disassembled for transport).
3. Store reflectors in padded crates (foam separators between face plates).
4. Store mooring kit on pallet, shrink-wrapped, labeled with depth variant.
5. Store GPS beacon in Pelican case, battery disconnected.

---

## 11. Towing Procedure

### 11.1 Tow Configuration

```
TOW ARRANGEMENT (TOP VIEW)
=============================================

              Tow vessel
                 │
                 │  tow warp (vessel's line)
                 │
           ┌─────┴─────┐
           │  junction  │  shackle
           └─────┬─────┘
            ╱         ╲
           ╱  60 deg   ╲   Dyneema bridle legs (16 mm, 25 m each)
          ╱   spread    ╲
    [IF-06]             [IF-06]
      Port              Starboard
      tow padeye        tow padeye

           ╭────────────╮
          ╱   THANH TRI  ╲    8.0 m target hull
         │    -H TARGET   │
          ╲              ╱
           ╰──────┬─────╯
                  │
              [drogue]  600 mm trailing drogue (above SS 3)
```

### 11.2 Tow Speed Limits

| Sea State | Maximum Tow Speed | Drogue | Notes |
|-----------|-------------------|--------|-------|
| SS 1-2 (calm) | 8 kn | Not required | Normal transit speed |
| SS 3 (slight) | 5 kn | Deploy drogue | Yaw damping beneficial |
| SS 4 (moderate) | 4 kn | Deploy drogue | Reduce speed if surging |
| SS 5 (rough) | **3 kn** | Deploy drogue | Maximum rated tow condition |
| SS >5 | **DO NOT TOW** | -- | Shelter in port or anchor target |

> **CAUTION:** In SS 5, tow at no more than 3 kn. Higher speeds risk bridle overload and yaw instability.

### 11.3 Drogue Deployment

1. When sea state exceeds SS 3 or target yaws excessively (>30 deg off heading):
2. Attach 600 mm drogue to stern of target hull using drogue shackle (12 mm pin) at designated trailing point (aft cleat or padeye).
3. Deploy drogue over stern into water. Allow line to pay out until drogue is 10-15 m behind target.
4. Drogue provides yaw damping by creating directional drag at stern.

### 11.4 Tow Monitoring

1. Maintain continuous visual watch on towed target from tow vessel.
2. Monitor GPS beacon position (independent confirmation of tow track).
3. Check bridle tension periodically -- excessive surging (rhythmic jerking) indicates too much speed for conditions. Reduce speed.
4. If target starts surfing (overtaking tow vessel on wave crests), reduce speed further.

### 11.5 Emergency Tow Procedures

**Bridle failure (one leg parts):**
1. Immediately reduce speed to bare steerageway.
2. Remaining leg will pull target to one side -- watch for collision with tow vessel.
3. Recover parted bridle end if possible.
4. Rig emergency tow using vessel's own tow warp connected to one tow padeye (single-point tow).
5. Reduce speed to 2 kn maximum on single-point tow. Deploy drogue.

**Total tow line failure:**
1. Target will drift free. GPS beacon continues tracking.
2. Tow vessel circles to maintain visual contact.
3. If conditions permit, reconnect using spare shackle and remaining bridle hardware.
4. If reconnection not possible, deploy marker buoy near target and standby until conditions improve.

---

## 12. Storage Procedure

### 12.1 Short-Term Storage (Between Deployments, <6 Months)

| Component | Storage Location | Conditions | Notes |
|-----------|-----------------|------------|-------|
| Hull (M1) | Covered warehouse or outdoor under tarp | No climate control required; protect from direct UV exposure | Stack sections on pallets with foam spacers |
| Frame (M2) | Installed in hull (leave assembled) | Covered, dry preferred | Inspect HDG coating every 3 months |
| Mast-reflector units (M5) | Padded vertical rack in warehouse | Keep upright; foam between reflectors | Do NOT stack horizontally (reflector face damage) |
| GPS beacon (M6) | Pelican case in dry indoor storage | Room temperature | **Disconnect battery.** Charge battery to 50% for storage. |
| Mooring kit (M7) | Palletized, shrink-wrapped | Covered outdoor or warehouse | Hose off salt water after each use; dry before storage |
| Tow kit (M8) | Rope bag in warehouse | Dry, out of direct sunlight | Coil Dyneema loosely (do NOT kink). Inspect splices. |
| Spare parts | Parts bin in warehouse | Dry | Check inventory against Appendix C quarterly |

### 12.2 Long-Term Storage (>6 Months)

1. **HDG steel surfaces (frame, masts):** Inspect for zinc coating degradation (white rust). If zinc bloom (white powder) is present, brush off and apply cold galvanizing touch-up spray to bare areas.
2. **Anodized aluminum (reflectors):** Inspect face plate surfaces. If anodize is scratched to bare aluminum, apply clear marine lacquer to affected area. Do NOT sand or polish face plates.
3. **HDPE hull:** Inspect for UV degradation (chalking, cracking). If outdoor-stored, apply UV-protective marine coating.
4. **Li-ion batteries (M6):** Charge to 50% state of charge every 6 months. Store at room temperature (15-25 deg C). Do NOT store fully discharged or fully charged for extended periods.
5. **Dyneema (M8):** Inspect for UV degradation (fiber fuzz, discoloration). Dyneema degrades slowly under UV -- store in opaque bag. Replace after 5 years regardless of condition.
6. **Mooring chain:** Inspect every link. HDG chain in coastal storage may develop surface rust within 1-2 years. Acceptable if rust is surface-only (no pitting to base metal). Wire-brush and re-galvanize if needed.

### 12.3 Component-Level Storage Conditions

| Component | Temperature Range | Humidity | UV Exposure | Shelf Life |
|-----------|-------------------|----------|-------------|------------|
| HDPE hull | -5 to +55 deg C | Any | Avoid prolonged direct UV | >20 years (covered) |
| S235 HDG steel | -20 to +55 deg C | Any | OK (HDG protects) | 10-15 years (HDG coating life) |
| 6061-T6 anodized Al | -40 to +80 deg C | Any | OK (anodize protects) | >10 years |
| AlSi10Mg hard anodized | -40 to +80 deg C | Any | OK (anodize protects) | >10 years |
| PU closed-cell foam | -30 to +80 deg C | Any | Avoid prolonged UV | >20 years |
| Li-ion 18650 cells | 0 to +35 deg C (ideal) | <80% RH | N/A (enclosed) | 3-5 years (cycle-dependent) |
| Dyneema SK75 | -40 to +65 deg C | Any | Avoid UV | 5 years (UV-degradable) |
| Polyester rode | -20 to +65 deg C | Any | Moderate UV OK | 8-10 years |
| G30 HDG chain | Any | Any | OK | 10-15 years |

---

## 13. Troubleshooting Guide

| Symptom | Probable Cause | Action |
|---------|---------------|--------|
| **GPS no fix** (LED not solid, shore station no data) | Antenna obstructed or facing wrong direction; low battery; module fault | Verify antenna orientation (face skyward); check battery voltage; power cycle beacon; if no fix after 10 min with clear sky, replace beacon |
| **Mast tube won't insert into socket** | Debris in socket (sand, paint); misaligned pin holes; corrosion buildup | Clear socket with rag or wire brush; apply Tef-Gel to socket bore; rotate mast slightly during insertion; check socket drain hole is not blocked |
| **Clevis pin won't align** | Mast tube rotated slightly; socket/mast hole tolerance | Rotate mast +-5 deg while pressing down; tap base plate lightly with rubber mallet to seat fully; if holes still misalign, remove mast and inspect pin hole for burr |
| **Anchor dragging** (GPS shows >10 m drift under load) | Insufficient scope; wrong anchor for seabed type; anchor not properly set | Increase scope (pay out more rode); verify seabed type (sand vs mud); re-set anchor with higher backing force; upgrade to 100 kg anchor for mud |
| **Mooring line chafing** (visible wear on rode at chafe point) | Rode rubbing on hull edge or fairlead without chafe guard | Install chafe guard (split rubber hose) over rode at contact point; rotate rode 180 deg at fairlead to present unworn section; replace if damage >10% of diameter |
| **Target listing to one side** | Water accumulation in hull (leak at IF-07 joint or hull puncture); asymmetric weight (missing mast) | Check hull section joint gasket; check scupper drains not blocked; verify all 8 masts installed; if hull is breached, foam fill maintains buoyancy but list may persist |
| **Reflector face plate loose** | Nylock nut loosened; safety wire broken; vibration-induced loosening | Re-torque M6 bolts to 8 N-m; replace safety wire; check all bolt pairs on affected reflector. If recurring, inspect Nordlock washers at IF-04 |
| **Shore station loses GPS signal** | Battery depleted; beacon submersed by wave (temporary); antenna cable damage | Wait 15 min (may be temporary submersion recovery); if no signal after 30 min, beacon battery may be depleted -- note time since activation; dispatch vessel to investigate if within 72 h window |
| **Swivel seized (target not weathervaning)** | Corrosion in swivel bearings; overload damage | Recover target; replace swivel; apply marine grease to new swivel before deployment |
| **Hull section joint leaking** | EPDM gasket displaced; bolt torque lost; sealant cracked | Haul target; inspect joint; re-torque all 34x M12 bolts to 40 N-m in star pattern; replace gasket if compressed flat; re-apply Sikaflex 291 sealant |

---

## 14. Technical Specifications Summary

### 14.1 Quick Reference -- Key Specifications

| Category | Parameter | Value |
|----------|-----------|-------|
| **Geometry** | Platform diameter | 8.0 m +/-0.1 m |
| | Hull depth | 0.5 m |
| | Draft (at 986 kg) | 19.1 mm |
| | Freeboard | 481 mm |
| | Mast height above deck | 3.0 m |
| | Reflector center AWL | ~4.0 m |
| | GPS beacon AWL | >=4.5 m |
| **Mass** | Total displacement (on-platform) | 986 kg |
| | Hull (M1) | 350 kg |
| | Frame (M2) | 150 kg |
| | Masts (M3 x8) | 130 kg total |
| | Reflectors (M4 x8) | 120 kg total |
| | GPS beacon (M6) | 5 kg |
| | Mast-reflector unit (M5) | 31.3 kg each |
| **Radar** | Peak combined RCS (X-band) | >=1,000 m^2 |
| | 360 deg average RCS | >=1,000 m^2 |
| | 360 deg minimum RCS | >=700 m^2 |
| | Angular variation | <=+/-2 dB |
| | Reflector edge length | 0.8 m |
| | Single reflector RCS | ~152 m^2 |
| **Mooring** | Chain | 19 mm G30 HDG |
| | Chain SWL | 5,800 kgf |
| | Required SWL | 4,536 kgf (3:1 on 1,512 kgf peak) |
| | Anchor (sand/hard) | 75 kg Danforth (holding ~1,500 kgf) |
| | Anchor (mud/soft) | 100 kg Danforth recommended |
| | Swivel SWL | 5,000 kgf |
| **Tow** | Bridle | 16 mm Dyneema SK75, 2-leg |
| | Bridle SWL | >=8,000 kgf |
| | Max tow speed (SS 5) | 3 kn |
| | Max tow speed (SS 1-2) | 8 kn |
| **GPS** | Battery endurance | >=72 h |
| | Position accuracy | <=+/-5 m CEP |
| | Transmit rate | 1 Hz |
| **Environment** | Survival sea state | SS 5-6 |
| | Survival wind | Bft 6-7 |
| | Temperature range | -5 to +55 deg C |
| | Seawater temp range | 20-32 deg C |

### 14.2 Mooring Load Table by Sea State

| Sea State | Hs (m) | Wind (kn) | Steady Load (kgf) | Peak Load (kgf) | Required SWL (3:1) |
|-----------|--------|-----------|-------------------|-----------------|---------------------|
| SS 2 | 0.1-0.5 | 4-6 | ~28 | ~42 | 126 |
| SS 3 | 0.5-1.25 | 7-10 | ~120 | ~180 | 540 |
| SS 4 | 1.25-2.5 | 11-16 | ~290 | ~435 | 1,305 |
| SS 5 | 2.5-4.0 | 17-21 | ~430 | ~860 | 2,580 |
| SS 6 (Design) | 4.0-6.0 | 22-27 | **578** | **1,512** | **4,536** |
| SS 6 + Gust (LC4) | 4.0-6.0 | gust 43 | 756 | **1,512** | **4,536** |

### 14.3 Weight and Dimensions by Module

| Module | Description | Mass (kg) | Dimensions (L x W x H) | Package |
|--------|-------------|-----------|------------------------|---------|
| M1 | Hull (2 sections) | 350 | 4.0 m dia x 0.5 m per half | Flatbed or 40 ft container |
| M2 | Frame (installed in hull) | 150 | 8.0 m dia x 0.15 m | Integrated with M1 |
| M3 x8 | Mast tubes (bundled) | 130 total | 3.1 m x 0.3 m x 0.3 m (bundle) | Steel cradle |
| M4 x8 | Reflectors (in crate) | 120 total | 0.9 m x 0.9 m x 0.5 m per crate | Padded plywood crate |
| M5 x8 | Mast-reflector (pre-assembled) | 250 total | 3.3 m x 0.9 m x 0.9 m each | Padded vertical rack |
| M6 | GPS beacon | 5 | 0.4 m x 0.3 m x 0.3 m | Pelican case |
| M7 | Mooring kit (medium) | ~260 | 1.2 m x 1.0 m x 0.8 m (pallet) | Palletized, shrink-wrap |
| M8 | Tow kit | 15 | 0.8 m x 0.5 m x 0.3 m | Canvas rope bag |

---

## 15. Appendices

### Appendix A: Pre-Deployment Checklist (Tear-Out Format)

```
═══════════════════════════════════════════════════════════════
  PRE-DEPLOYMENT CHECKLIST — VN-TGT-SEA-001 "THANH TRI-H"
  Date: ____________  Target S/N: ______________
  Site: ____________  Depth: _______ m  Kit: A / B / C
  Crew Lead: ___________________  Weather: SS ___ Wind ___ kn
═══════════════════════════════════════════════════════════════

COMPONENT INVENTORY
[ ] Hull (M1) — 2 sections joined / 1 piece     Condition: OK / DEFECT
[ ] 8x M5 mast-reflector units (count: __/8)     Condition: OK / DEFECT
[ ] GPS beacon (M6) S/N: ____________            Condition: OK / DEFECT
[ ] Mooring kit (M7) — Kit A / B / C             Condition: OK / DEFECT
[ ] Tow kit (M8) — bridle + drogue               Condition: OK / DEFECT
[ ] Spare parts kit                               Present:  YES / NO
[ ] Tool kit                                      Present:  YES / NO
[ ] Deployment manual                             Present:  YES / NO

SAFETY-CRITICAL ITEMS (SCI)
[ ] SCI-01  Mooring chain — links inspected       PASS / FAIL
[ ] SCI-02  Pad eye — weld + bolt torque check    PASS / FAIL
[ ] SCI-03  Tow line — visual + splice check      PASS / FAIL
[ ] SCI-04  Anchor — flukes + pivot check         PASS / FAIL
[ ] SCI-05  GPS battery — voltage check           PASS / FAIL  V=___
[ ] SCI-06  Locking pins (8x) — all present       PASS / FAIL

VISUAL INSPECTION
[ ] Hull — no cracks, no UV damage                PASS / FAIL
[ ] Hull joint (IF-07) — gasket + bolts           PASS / FAIL
[ ] Frame — HDG coating intact                    PASS / FAIL
[ ] 8x Deck sockets — clear, no debris           PASS / FAIL
[ ] 8x Masts — straight, plates perpendicular    PASS / FAIL
[ ] 8x Reflectors — faces clean, wire intact     PASS / FAIL
[ ] Pad eye ring — not distorted                  PASS / FAIL
[ ] Tow padeyes — rings intact                    PASS / FAIL

GPS BEACON ACTIVATION
[ ] Battery connected                Time: _________
[ ] GPS fix acquired                 Time: _________
[ ] Iridium SBD confirmed           Time: _________  Shore ACK: YES / NO

WEATHER CHECK
[ ] 48h forecast obtained
[ ] Sea state <=SS 5 confirmed       SS forecast: ___
[ ] No storm warnings within 72h     Forecast source: ____________

AUTHORIZATION
Crew Lead signature: ___________________  Date: __________
Vessel Master signature: _______________  Date: __________

RESULT:  [ ] PROCEED TO DEPLOYMENT   [ ] HOLD — Resolve defects
═══════════════════════════════════════════════════════════════
```

### Appendix B: Recovery Checklist

```
═══════════════════════════════════════════════════════════════
  RECOVERY CHECKLIST — VN-TGT-SEA-001 "THANH TRI-H"
  Date: ____________  Target S/N: ______________
  Recovery Type:  [ ] Post-Engagement  [ ] No-Engagement  [ ] Exercise
  Crew Lead: ___________________  Weather: SS ___ Wind ___ kn
═══════════════════════════════════════════════════════════════

POST-ENGAGEMENT RECOVERY
[ ] Wait 30 min after impact before approach
[ ] Visual survey of debris field — extent: ______ m
[ ] GPS beacon located?  YES / NO — recovered?  YES / NO
[ ] Large debris collected  (items: ___________________)
[ ] Mooring buoy located?  YES / NO
[ ] Mooring chain/rode recovered   Condition: ____________
[ ] Anchor recovered (trip line)   Condition: ____________
[ ] Debris field cleared of hazards

NO-ENGAGEMENT / EXERCISE RECOVERY
[ ] Confirm SS <=4 before starting
[ ] Tow bridle connected (IF-06)
[ ] 8x Mast-reflector units removed   Count: __/8
[ ] GPS beacon recovered and powered off
[ ] Mooring disconnected (IF-02)
[ ] Mooring buoyed for later recovery
[ ] Target under tow at <=3 kn (SS) / <=8 kn (calm)
[ ] Target hauled out at port

RECOVERED ITEMS CONDITION
[ ] Mooring chain — reusable?  YES / NO  (Notes: ___________)
[ ] Rode — reusable?  YES / NO  (Notes: ___________)
[ ] Anchor — reusable?  YES / NO  (Notes: ___________)
[ ] Shackles/swivel — reusable?  YES / NO
[ ] GPS beacon — functional?  YES / NO
[ ] Tow bridle — reusable?  YES / NO

Crew Lead signature: ___________________  Date: __________
═══════════════════════════════════════════════════════════════
```

### Appendix C: Spare Parts List

| Item | Qty | Purpose |
|------|-----|---------|
| M12 clevis pin + R-clip set | 4 | Spare mast locking pins |
| R-clip (spring pin) only | 8 | Replace lost clips |
| Safety wire, 0.8 mm SS, 10 m coil | 2 | Mast pins + reflector bolts |
| M12 x 40 SS316 hex bolt + nut + washer | 10 | IF-01 frame-to-hull spares |
| M6 x 20 SS316 hex bolt + Nylock nut + washer | 12 | Reflector face plate spares |
| Bow shackle, 20 mm pin, HDG (SWL 5,000 kgf) | 2 | Mooring spares |
| Mousing wire, 1 mm galvanized, 5 m | 2 | Shackle mousing |
| Tef-Gel anti-seize compound, 1 tube | 1 | Socket lubrication |
| EPDM gasket strip, 5 mm x 50 mm, 3 m | 1 | Hull joint gasket spare |
| Sikaflex 291 sealant, 1 cartridge | 1 | Hull joint sealant spare |
| Li-ion battery pack (GPS beacon spare) | 1 | GPS beacon battery replacement |
| Chafe guard (split rubber hose), 0.5 m | 2 | Mooring rode chafe protection |

### Appendix D: Tool List

| Tool | Qty | Purpose |
|------|-----|---------|
| Shackle key (adjustable) | 1 | Tighten/loosen shackle pins |
| 19 mm socket wrench + ratchet | 1 | M12 bolts (IF-01, IF-07) |
| 13 mm spanner | 1 | M8 U-bolts (GPS bracket) |
| Torque wrench, 10-100 N-m range | 1 | Bolt torque verification |
| Torque wrench, 100-250 N-m range | 1 | M16 pad eye bolt verification |
| Safety wire pliers | 1 | Safety wire installation |
| Wire cutters (diagonal) | 1 | Safety wire removal |
| Pliers (combination) | 1 | R-clip installation/removal |
| Rubber mallet | 1 | Seating mast base plates |
| Wire brush (stainless) | 1 | Socket cleaning |
| Tape measure, 10 m | 1 | Depth verification, scope measurement |
| Sealant gun (for Sikaflex cartridge) | 1 | Hull joint sealant |
| VHF handheld radio | 1 | Shore station communication |
| Camera (waterproof or in case) | 1 | Documentation photography |
| Multimeter (for GPS battery voltage) | 1 | SCI-05 battery check |
| Marker pen (waterproof) | 2 | Labeling buoys |

### Appendix E: Contact Information

| Role | Organization | Contact | Notes |
|------|-------------|---------|-------|
| Shore Station Operator | [Range Control Center] | VHF Ch. ___, Tel: ___________ | GPS monitoring 24/7 during deployment |
| Range Safety Officer | [Naval Test Range] | Tel: ___________ | Go/No-Go authority |
| Coast Guard (SAR) | [Regional Coast Guard] | VHF Ch. 16, Tel: ___________ | Emergency/MOB |
| NOTAM Broadcast | [Maritime Safety Center] | Tel: ___________ | Exclusion zone notification |
| Manufacturer (Engineering) | [Project Office VN-TGT-SEA-001] | Tel: ___________, Email: __________ | Technical support |
| Weather Service | [National Met Center] | Tel: ___________, Web: __________ | Marine forecast updates |
| Iridium SBD Service | [Service Provider] | Account: ___________ | GPS data monitoring |

> **NOTE:** Fill in contact details before issuing this manual to deployment crews. Keep a laminated copy of this page in the deployment kit.

---

## Cross-References

### Phase 3 Source Documents
- [[PRAD_A7_architecture_definition.md]] -- Module decomposition (M1-M8), interface specifications (IF-01 to IF-07)
- [[PRAD_D8_design_structure.md]] -- Structural analysis: masts, frame, mooring, hull (load cases, catenary profiles)
- [[DECS_C11_requirements_verification.md]] -- 116 requirements verification (ERG, OPR, SAF, MNT, ASM)
- [[DECS_S12_standards_compliance.md]] -- Safety-critical items (SCI-01 to SCI-06), hazard mitigations (H-01 to H-08)
- [[OCP_P15_production_planning.md]] -- Field deployment procedure (steps D-01 to D-18), factory assembly
- [[OCP_C14_cost_analysis.md]] -- Mooring kit variants, tow kit BOM

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1), ERG-006 training requirement

### Project Management
- [[../PROJECT_STATUS.md]] -- Project status tracker

---

*End of Deployment & Operations Manual, DOM-001 Rev 1.0. This document defines all field procedures for deployment, operation, recovery, towing, and storage of the THANH TRI-H fixed sea target. All crew members must complete the training program (4 h classroom + 2 h hands-on per ERG-006) before participating in deployment operations.*
