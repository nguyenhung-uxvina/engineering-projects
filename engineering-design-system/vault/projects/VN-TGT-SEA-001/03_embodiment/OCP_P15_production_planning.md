---
project: VN-TGT-SEA-001
phase: 3
step: "P15 — Production Planning"
group: OCP
version: 1.0
created: 2026-02-10
status: draft
---

# Step P15: Production Planning — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Define the complete production plan for Vietnamese manufacturing -- process selection, supplier identification, make/buy analysis, quality control, assembly sequences, field deployment, scheduling, capacity analysis, and packaging/transport.
**Method:** Pahl & Beitz Embodiment Design, OCP Step P15 -- Production Planning
**Input:** [[PRAD_A7_architecture_definition.md]] (8 modules, 7 interfaces), [[RISM_M4_material_analysis.md]] (5 material selections), [[../01_requirements/requirements_list.md]] (116 requirements, Rev B.1)
**Targets:** Unit cost $35.6K @ 10 units, production rate >=6 units/month at steady state, local content >=60%

---

## 1. Manufacturing Process Selection

### 1.1 Process Overview by Module

| Module | Primary Process | Equipment | Capability Required | Vietnamese Availability | Fallback Process |
|--------|----------------|-----------|---------------------|------------------------|------------------|
| **M1: Hull Assembly** | HDPE rotomolding (preferred) | Biaxial rotomolding machine, 8m capable or 4m (2-section) | Large-diameter HDPE rotomolding, PE100 processing, 12-15mm wall | **MODERATE** -- 4m rotomolders exist; 8m single-piece requires tooling investment or 2-section approach | HDPE hot-plate welding from flat sheet (standard, widely available) |
| **M2: Structural Frame** | Steel fabrication (cut, drill, weld, HDG) | CNC plasma cutter, drill press, MIG/MAG welders, HDG bath | Standard mild steel fabrication, S235 welding per AWS D1.1, hot-dip galvanizing per ASTM A123 | **HIGH** -- Standard capability at any Vietnamese steel fabrication shop | Manual plasma cutting + manual welding (lower precision, higher labor) |
| **M3: Mast Assembly (x8)** | Tube cutting, plate welding, drilling, HDG | Tube cutter or bandsaw, MIG/MAG welder, drill press, HDG bath | Tube-to-plate welding, perpendicularity control <=0.5 deg, hole position <=0.5mm | **HIGH** -- Simple fabrication; any job shop | Same as primary (no fallback needed) |
| **M4: Reflector Assembly (x8)** | CNC milling (face plates) + LPBF AM (frames) + manual assembly | 3-axis CNC mill with vacuum fixture, LPBF metal printer (external), CMM or angle gauge | CNC fly-cutting 800x800mm Al to Ra<=10um, flatness <0.1mm; LPBF AlSi10Mg to +-0.1 deg orthogonality | **MODERATE** -- CNC locally available; LPBF from ASEAN bureaus | CNC-only multi-part frame assembly (6061-T6 CNC, +-0.3 deg, lower cost) |
| **M5: Mast-Reflector Unit (x8)** | Pre-assembly with alignment verification | Torque wrench, dowel pin press, digital angle gauge | Bolt + pin IF-04 joint, galvanic isolation insert, orthogonality verification <=0.5 deg system | **HIGH** -- Standard mechanical assembly; requires trained technician | Same (no fallback needed) |
| **M6: GPS Beacon** | Electronics integration + enclosure sealing | Soldering station, IP67/68 test rig, battery spot welder or tab welder | GNSS/Iridium module integration, Li-ion battery pack assembly, waterproof seal validation | **LOW-MODERATE** -- Electronics integration limited; COTS module simplifies | Procure fully assembled COTS GPS tracker + custom bracket only |
| **M7: Mooring Kit** | COTS procurement + rope splicing | Rope splicing tools, shackle tools | Marine hardware procurement, rope eye-splicing, assembly of chain-rode-anchor-swivel kit | **HIGH** -- Vietnamese marine chandlers stock all components; rope splicing is traditional skill | Direct import of assembled mooring kits (higher cost) |
| **M8: Tow Kit** | COTS procurement + Dyneema splicing | Dyneema splicing tools (fid, needles) | Dyneema SK75 splicing (specialized), drogue fabrication (canvas/nylon sewing) | **MODERATE** -- Dyneema splicing requires training; drogue sewing available at sail lofts | Import pre-spliced Dyneema bridle; local drogue fabrication |

### 1.2 Process Detail -- M1 Hull

**Option A: Rotomolding (Preferred)**

| Parameter | Value |
|-----------|-------|
| Process | Biaxial rotational molding, PE100 powder |
| Mold | Aluminum or steel, CNC-machined cavity, 2-section hull (each ~4.0m half-disc) |
| Mold cost | $12,000-15,000 per half-mold ($24,000-30,000 total for 2 molds) |
| Mold amortization | Over 50 units = $480-600/unit |
| Cycle time | 90-120 min per half (heat + cool + demold) |
| Wall thickness | 12-15mm, controlled by rotation speed and dwell time |
| Output | 2 half-hulls per day (1 mold set) |
| Post-process | Trim flash, drill bolt holes (IF-01, IF-06, IF-07), install scupper drains |
| Foam fill | Pour closed-cell PU rigid foam (32-48 kg/m3) into hull cavity, cure 24h |
| Suppliers capable | Binh Minh Plastics (HCMC), Tan Dai Hung (HCMC), Tien Phong Plastics (Hai Phong) |

**Option B: HDPE Hot-Plate Welding (Fallback)**

| Parameter | Value |
|-----------|-------|
| Process | Cut HDPE sheet (12-15mm) to patterns, hot-plate butt weld into hull sections |
| Equipment | HDPE sheet cutter (CNC router or manual), hot-plate welding machine (>=600mm platen) |
| Tooling cost | $3,000-5,000 (welding fixtures, cutting templates) |
| Cycle time | 3-5 days per hull (labor-intensive) |
| Output | 1 hull per week (1 welding station) |
| Post-process | Weld bead dressing, leak test (fill compartments), drill bolt holes |
| Foam fill | Same as Option A |
| Suppliers capable | Any HDPE tank/pipe fabricator in Vietnam (many available) |

**Decision:** Start with Option B (HDPE welding) for prototype and first 10 units. Transition to Option A (rotomolding) at unit 11+ when demand justifies mold investment. Break-even: mold investment recovers at ~15 units vs welding cost difference.

### 1.3 Process Detail -- M4 Reflector

| Sub-component | Process | Detail |
|---------------|---------|--------|
| **Face plates (24x)** | CNC fly-cutting | 6061-T6 sheet stock (25mm thick plate preferred for clamping, or 3mm sheet on vacuum fixture). Face 1: fly-cut to Ra<=10um on 3-axis VMC. Face 2: parallel face, thickness to 3.00 +-0.05mm. Edge: profile mill to 800x800 +-0.1mm. Drill 4x M6 clearance + 2x dia 5mm dowel holes per face plate. Deburr all edges. |
| **AM frames (8x)** | LPBF (laser powder bed fusion) | AlSi10Mg powder, EOS M290 or SLM 280 class machine. Build orientation: frame upright (Z-axis = vertical axis of reflector). Post-process: stress relief (300C/2h), T5 age (160C/6h), support removal, CNC post-machine datum surfaces (mounting flange, face plate mounting bosses, dowel pin holes), blast/tumble non-critical surfaces. |
| **Anodize** | Type II (face plates), Type III (frames) | Batch anodize: 24 face plates in Type II clear anodize bath (>=10um). 8 frames in Type III hard anodize bath (>=25um, sealed). Separate baths required. |
| **Assembly** | Manual assembly in controlled environment | Clean environment (no dust/grit). Mount 3 face plates to 1 frame using 12x M6 SS bolts + Nylock nuts, 6x alignment dowel pins. Torque to 8 N-m. Safety wire bolt heads in pairs. Verify orthogonality with digital angle gauge (3 face-pair measurements per reflector, all <=+-0.1 deg). |

---

## 2. Supplier Identification

### 2.1 Primary Suppliers

| Component | Supplier | Location | Capability | Lead Time | MOQ | Backup Supplier |
|-----------|----------|----------|------------|-----------|-----|-----------------|
| **HDPE sheet/resin (PE100)** | Binh Minh Plastics (BMP) | Ho Chi Minh City | HDPE pipe/sheet extrusion, rotomolding; ISO 9001 | 2-3 weeks | 500 kg | Tien Phong Plastics (Hai Phong) |
| **PU rigid foam** | Dong A Chemical | Binh Duong Province | Closed-cell PU pour-in-place foam, 32-60 kg/m3 | 1-2 weeks | 200 kg | Dai Dong Tien (HCMC) |
| **S235 steel plate + angle** | Hoa Phat Group | Hai Duong / Dung Quat | S235JR equivalent (CT3), hot-rolled plate 5-20mm, angles L50-L100 | 1-2 weeks (stock) | 1 ton | Nam Kim Steel (Binh Duong) |
| **S235 steel tube (60mm OD)** | Hoa Phat Tube Division | Hai Duong | Welded/seamless structural tube, 48-114mm OD, 3-6mm wall | 1-2 weeks (stock) | 100m | SeAH Steel (Vietnam plant, Binh Duong) |
| **Steel fabrication (frame, masts)** | Truong Hai Mechanical (TBD) | Hanoi / Hai Phong | CNC plasma, MIG/MAG welding, AWS D1.1 capable, 5-ton capacity | 2-3 weeks per batch | 1 unit | Vietnam Precision Mechanical (Bac Ninh) |
| **Hot-dip galvanizing** | Vinh Thanh HDG | Hai Phong | HDG bath >=3m length, ASTM A123, >=85um zinc | 3-5 days | 500 kg | Hoa Phat Galvanizing (Hai Duong) |
| **6061-T6 Al sheet (3mm)** | Novelis (Korea) via VN distributor | Import (Korea/Japan) | ASTM B209, 6061-T6, 1250x2500mm sheets | 3-4 weeks (import) | 500 kg (10 sheets) | Hindalco (India) via HCMC trader |
| **CNC face plate machining** | Hai Phong CNC (TBD) | Hai Phong | 3-axis VMC >=1000mm X-travel, vacuum fixture, fly-cut experience | 1-2 weeks per batch of 24 | 8 plates | Minh Phuc CNC (Hanoi) |
| **AlSi10Mg AM frames** | Xometry Asia | Singapore | EOS M290 / SLM 280, AlSi10Mg LPBF, T5 heat treat, CNC post-machine | 2-3 weeks | 1 frame (batch pricing at 8) | Facfox (Shenzhen, China) |
| **AlSi10Mg AM frames (backup 2)** | JR Tech Solutions | Bangkok, Thailand | SLM 280, AlSi10Mg, post-processing, ISO 9001 | 3-4 weeks | 4 frames | Protolabs (Singapore) |
| **Type II anodize (Al face plates)** | Saigon Anodizing | Ho Chi Minh City | Clear Type II anodize >=10um per MIL-A-8625, batch capacity >=50 parts | 3-5 days | 10 parts | An Phat Surface Treatment (Binh Duong) |
| **Type III hard anodize (AM frames)** | Xometry Asia (bundled with AM) | Singapore | Type III hard anodize >=25um, sealed, on AlSi10Mg substrate | Included in AM lead time | Bundled | Saigon Anodizing (needs AlSi10Mg qualification) |
| **SS 316 fasteners** | Bulong Viet (TBD) | Hanoi / HCMC | M6, M10, M12 hex bolts, Nylock nuts, flat/fender washers, SS 316 | 1-2 weeks | 100 pcs per size | Import (China) via fastener distributor |
| **Danforth anchor (50 kg HDG)** | Vietnam Marine Equipment | Hai Phong | Cast steel anchor, HDG, marine grade, 30-80 kg range | 2-3 weeks | 5 units | Tan Thanh Marine (Da Nang) |
| **G30 HDG chain (16-19mm)** | Hai Phong Marine Chandler | Hai Phong | G30 proof coil chain, HDG, 10-22mm, sold by meter or 100m drum | 1 week (stock) | 100m | Vung Tau Marine Supply |
| **Polyester braided rode (20mm)** | Saigon Rope & Cordage | Ho Chi Minh City | 3-strand and double-braid polyester, 12-32mm, marine UV-stabilized | 1-2 weeks | 200m | Hai Phong Rope Factory |
| **Dyneema SK75 (16mm)** | Import via Marlow Ropes agent | Import (UK/Netherlands) | 12-strand Dyneema, 16mm, SWL >=8,000 kgf, pre-spliced eyes | 4-6 weeks (import) | 100m | Samson Rope (US) via Singapore distributor |
| **Swivel, shackles, thimbles** | Vietnam Marine Hardware | Hai Phong | HDG/SS bow shackles, swivels <=10,000 kgf, SS thimbles | 1-2 weeks (stock) | 10 pcs per type | Import (China) via marine hardware distributor |
| **GNSS/Iridium module (COTS)** | Import via Garmin / BW Technologies agent | Import (Taiwan / US) | Integrated GNSS + Iridium SBD tracker, IP67, battery >=20 Wh | 4-6 weeks (import) | 5 units | GT MarineTracker (China), Queclink (China) |
| **Li-ion battery pack (20 Wh)** | Bundled with GNSS module OR | Import (China) | 18650 cell pack, 20+ Wh, with protection circuit, IP67 housing | Included or 2-3 weeks | 10 packs | EVE Energy (China), BYD (China) |
| **Drogue (600mm)** | Local canvas/sail maker | Hai Phong / Da Nang | Conical drogue, 600mm diameter, nylon/canvas, SS ring + swivel | 1-2 weeks | 5 units | Thai Binh Sailmakers (HCMC) |

### 2.2 Supplier Risk Assessment

| Risk | Affected Supplier | Impact | Mitigation |
|------|-------------------|--------|------------|
| **LPBF capacity bottleneck** | Xometry, Facfox, JR Tech | AM frames delayed >3 weeks | Maintain 3 qualified AM suppliers; keep 1 batch buffer stock of frames |
| **6061-T6 Al import delay** | Korean/Japanese mills | Face plate production delayed | Maintain 2-month raw material buffer; qualify Indian backup source |
| **Dyneema import delay** | Marlow Ropes / Samson | Tow kit delayed | Pre-order 6-month Dyneema stock; alternative: 28mm polyester rope (per TRA-004) |
| **GPS module supply** | Garmin / BW Technologies | GPS beacon delayed | Qualify 2 COTS suppliers (Garmin + Queclink); maintain 5-unit buffer stock |
| **HDG bath size limit** | Vinh Thanh HDG | Frame too large for bath | Pre-qualify bath dimensions (>=3m for masts); frame can be galvanized in sub-assemblies if needed |
| **Single CNC shop bottleneck** | Hai Phong CNC | Face plate production delayed | Qualify 2 CNC shops; face plate machining is standard VMC work |

---

## 3. Make vs Buy Analysis

### 3.1 Decision Matrix

| Component | Make In-House | Buy (COTS/Outsource) | Decision | Rationale |
|-----------|--------------|----------------------|----------|-----------|
| **M1: HDPE hull shell** | -- | **BUY** (outsource to VN rotomolder/welder) | BUY | HDPE processing requires specialized equipment (rotomold oven or hot-plate welder). Outsource to Binh Minh Plastics or equivalent. |
| **M1: PU foam fill** | **MAKE** | -- | MAKE | Pour-in-place foam fill is simple, done at assembly facility. Procure 2-component PU foam kit. |
| **M2: Structural frame** | -- | **BUY** (outsource to VN steel fab shop) | BUY | Steel fabrication (cut, weld, drill) is standard job-shop work. Outsource to local fabricator. |
| **M2: Hot-dip galvanizing** | -- | **BUY** (outsource to HDG plant) | BUY | HDG requires dedicated bath facility. Outsource to Vinh Thanh or Hoa Phat HDG. |
| **M3: Mast fabrication (8x)** | -- | **BUY** (same steel fab shop as M2) | BUY | Bundle with M2 frame fabrication at same shop for efficiency. |
| **M4: CNC face plates (24x)** | -- | **BUY** (outsource to VN CNC shop) | BUY | CNC fly-cutting requires 3-axis VMC. Outsource to qualified CNC shop. |
| **M4: AM frames (8x)** | -- | **BUY** (outsource to ASEAN AM bureau) | BUY | No Vietnamese LPBF capability for AlSi10Mg. Outsource to Xometry/Facfox/JR Tech. |
| **M4: Anodize (face plates + frames)** | -- | **BUY** (outsource to anodizer) | BUY | Type II and Type III anodize requires chemical process lines. Outsource. |
| **M4: Reflector assembly** | **MAKE** | -- | MAKE | Alignment-critical assembly done in-house at controlled assembly facility. Core competency. |
| **M5: Mast-reflector pre-assembly** | **MAKE** | -- | MAKE | In-house pre-assembly of M3+M4 at IF-04 interface. Alignment verification in-house. |
| **M6: GPS beacon** | -- | **BUY** (COTS module + custom bracket) | BUY | Electronics module is COTS. Bracket fabrication outsource to SS fab shop. In-house integration. |
| **M6: GPS bracket** | **MAKE** | -- | MAKE | Simple SS 316 L-bracket, U-bolt clamp. Fabricate in-house or bundle with M2 fab shop. |
| **M7: Mooring kit** | -- | **BUY** (COTS procurement, all components) | BUY | All mooring hardware (anchor, chain, rode, swivel, shackles) is standard marine COTS. Procure from marine chandler. |
| **M7: Rode splicing** | **MAKE** | -- | MAKE | Eye-splicing polyester rode is done in-house by trained rigger. |
| **M8: Tow bridle** | -- | **BUY** (pre-spliced Dyneema) or MAKE | BUY | Dyneema splicing requires specialized skill. Order pre-spliced bridle from rope supplier. |
| **M8: Drogue** | -- | **BUY** (outsource to sail maker) | BUY | Canvas/nylon drogue sewing outsource to local sail loft. |
| **Final assembly** | **MAKE** | -- | MAKE | System integration, QC, functional test performed in-house at assembly facility. |
| **RCS measurement** | **MAKE** | -- | MAKE | Portable RCS test setup (or outdoor range) operated by engineering team. |

### 3.2 Make vs Buy Summary

| Category | Make (In-House) | Buy (Outsource / COTS) |
|----------|-----------------|------------------------|
| **Number of items** | 8 | 15 |
| **Value (in-house labor)** | ~$8,500/unit | ~$27,100/unit |
| **Core competencies retained** | Reflector assembly (alignment), system integration, QC/test, foam fill | Hull fabrication, steel fab, CNC machining, AM printing, anodize, HDG, COTS procurement |

**Rationale:** The make/buy split concentrates in-house effort on the value-critical activities -- reflector assembly (where orthogonality control is the key differentiator) and system integration/test. All material processing (HDPE, steel, CNC, AM, anodize, HDG) is outsourced to specialists who have dedicated equipment and established quality systems.

---

## 4. Quality Control Plan

### 4.1 Incoming Material Inspection

| Component | Inspection Point | Method | Accept/Reject Criteria | Frequency | Equipment |
|-----------|-----------------|--------|----------------------|-----------|-----------|
| HDPE hull shell (from supplier) | Wall thickness, diameter, section weight | Ultrasonic thickness gauge, tape measure, scale | Wall 12-15mm +-1mm; diameter 4.0m +-5mm (per half); mass +-5% of target | 100% of hulls | UT gauge (Elcometer), 10m tape, floor scale |
| PU foam (raw material) | Density of cured sample | Pour test coupon, weigh + measure | 32-48 kg/m3 | Per batch | Scale, calipers |
| Steel frame (from fab shop) | Weld quality, dimensions, socket positions | Visual weld inspection per AWS D1.1, dimensional check with tape + level + angle gauge | No cracks, undercut, porosity; socket positions at R=3.7m +-5mm, 45 deg +-0.5 deg | 100% of frames | Welding gauge set, 10m tape, digital protractor, spirit level |
| Steel frame -- critical welds | Pad eye weld, tow padeye welds | Ultrasonic testing (UT) per AWS D1.1 | No indications >3mm; full penetration confirmed | 100% on pad eye; 50% on tow padeyes | UT flaw detector (Olympus Epoch 650) |
| HDG coating (frame + masts) | Zinc thickness | Magnetic coating thickness gauge | >=85 um per ASTM A123 (3 readings per part, all pass) | 100% of galvanized parts | Elcometer 456 or equivalent |
| 6061-T6 Al sheet (incoming) | Material certificate, thickness | Review mill cert (alloy, temper, lot), micrometer check | 6061-T6 per ASTM B209; thickness 3.0 +-0.1mm (or 25mm plate if fly-cutting from block) | Per shipment | Micrometer, filing cabinet for certs |
| AM frames (from ASEAN bureau) | Dimensional, orthogonality, material cert | CMM measurement of datum surfaces + face mounting planes; review AM build report + heat treat cert | All datum dimensions +-0.1mm; orthogonality of 3 face planes <=+-0.1 deg; tensile test cert (sigma_y >=230 MPa) | 100% of frames | CMM (outsource to metrology lab if needed), digital angle gauge |
| CNC face plates (from CNC shop) | Flatness, surface roughness, dimensions | Surface plate + feeler gauge or CMM; surface roughness tester; calipers | Flatness <0.1mm over 800x800mm; Ra <=10um; dimensions +-0.1mm | 100% of face plates | Granite surface plate (1000x1000mm), feeler gauge set, Mitutoyo SJ-210 roughness tester |
| Anodize (face plates) | Coating thickness, adhesion | Eddy-current thickness gauge; tape adhesion test per ASTM D3359 | Type II >=10um; adhesion rating 4B or 5B | 10% of plates per batch + first article | Eddy-current gauge (Fischer Dualscope), cross-hatch tape kit |
| Anodize (AM frames) | Coating thickness | Eddy-current thickness gauge | Type III >=25um | 100% of frames | Eddy-current gauge |
| G30 chain (incoming) | Load certificate, visual | Review chain cert (grade, WLL, test load); visual for rust, damage | Grade 30, WLL >=4,200 kgf (16mm) or >=5,800 kgf (19mm); no visible defects | Per lot | Filing cabinet for certs, visual |
| Dyneema bridle (incoming) | Rope cert, splice inspection | Review rope cert (SWL); visual inspection of spliced eyes | SWL >=8,000 kgf; tuck count >=24 per splice | 100% of bridles | Visual, calipers for tuck count |
| GPS module (COTS) | Power-on test, GPS fix, Iridium link | Power on, acquire GPS fix, send test SBD message | Fix acquired <5 min; position accurate +-5m (compare to known reference); SBD received | 100% of modules | Known reference position marker, Iridium SBD account |

### 4.2 In-Process Quality Control

| Component | Inspection Point | Method | Accept/Reject Criteria | Frequency | Equipment |
|-----------|-----------------|--------|----------------------|-----------|-----------|
| Hull foam fill | Foam cure + fill completeness | Tap test (hollow = void), weigh hull after fill | No voids >200mm diameter (tap test); filled mass within +-5% of calculated | 100% of hulls | Rubber mallet (tap test), floor scale |
| Frame-to-hull install (IF-01) | Bolt torque, sealant application | Torque wrench check; visual sealant bead | All 84x M12 bolts at 40 N-m +-5%; continuous sealant bead, no gaps | 100% | Torque wrench (10-100 N-m range) |
| Pad eye proof load (IF-02 mechanical) | Proof load test | Hydraulic jack or tensile test to 1.5x SWL = 6,804 kgf | No permanent deformation; no bolt loosening; no weld cracking | 100% (first article + every 10th unit) | Hydraulic jack + load cell + calibrated gauge |
| Reflector assembly (M4) | Orthogonality measurement | Digital angle gauge between each face pair (3 measurements per reflector: AB, BC, AC) | All 3 face-pair angles 90.0 +-0.1 deg | **100% of reflectors (24 measurements per unit)** | Digital angle gauge (Wixey WR300 Type 2, resolution 0.05 deg) or CMM |
| Reflector assembly (M4) | Face plate flatness in-situ | Straight edge + feeler gauge across face diagonal | <0.15mm across 800mm diagonal (relaxed from incoming 0.1mm to account for bolt distortion) | 100% of face plates after assembly | 1000mm straight edge, feeler gauge set |
| Reflector assembly (M4) | Fastener torque + safety wire | Torque wrench check; visual safety wire | All 12x M6 bolts at 8 N-m +-1; safety wire present on all bolt pairs (6 wire loops) | 100% of reflectors | Torque wrench (1-20 N-m), safety wire pliers |
| Mast-reflector pre-assembly (M5, IF-04) | Bolt torque, dowel pin engagement, galvanic isolation | Torque wrench; pin engagement depth; visual check nylon isolation bushings + washers | 4x M10 bolts at 50 N-m +-5%; dowel pins fully seated; nylon isolators present on all 4 bolts + 2 pins | 100% of M5 units | Torque wrench (20-100 N-m), visual |
| GPS beacon (M6) | 72h battery endurance test | Power on at 1 Hz transmit rate, monitor until battery depletion | >=72h continuous operation | First article + every 5th unit | Timer, Iridium SBD monitoring |

### 4.3 Final Acceptance Quality Control

| Test | Method | Accept/Reject Criteria | Frequency | Equipment | QC Hold Point? |
|------|--------|----------------------|-----------|-----------|----------------|
| **System mass** | Weigh complete unit (hull + frame + 8x M5 units + GPS + fasteners) | <=1,100 kg (GEO-007); target ~980 kg +-5% | 100% | Floor scale or crane scale (rated 2,000 kg) | YES -- reject if >1,100 kg |
| **Hull dimensional** | Measure outer diameter, hull depth, deck flatness | Diameter 8.0m +-0.1m; depth 0.5m +-0.05m | 100% | 10m tape measure, spirit level | No |
| **Hydrostatic leak test** | Float hull in test tank or harbor, inspect for leaks over 4h | No visible water ingress into foam-filled compartments; hull section joint (IF-07) dry | 100% | Test tank or harbor access; visual | YES -- reject if leak detected |
| **Mast socket verification** | Insert all 8 masts into sockets, check fit, pin engagement | All 8 masts insert smoothly with 1.0-1.5mm radial clearance; locking pin engages; base plate seats on flange | 100% | 8x mast assemblies, M12 clevis pins | No |
| **360 deg RCS measurement** | Rotate target on turntable (or tow in circle) with X-band radar at known range | Peak RCS >=1,000 m2; 360 deg average >=1,000 m2; minimum >=700 m2; variation <=+-2 dB (QUA-001, SIG-001 to SIG-004) | **100% of units** | Portable X-band radar (9.4 GHz), turntable or tow arrangement, data logger | **YES -- reject if any SIG requirement fails** |
| **GPS beacon function** | Power on, verify GPS fix, Iridium SBD transmission received at shore | Fix <5 min; accuracy <=+-5m; SBD received at monitoring station | 100% | GPS reference position, Iridium SBD account | YES -- reject if no fix or no SBD |
| **Visual inspection** | Complete surface inspection: hull, frame, welds, galvanize, anodize, safety wires, markings | No visible damage, corrosion, missing components, loose fasteners, missing safety wire, illegible markings | 100% | Visual, magnifying glass for weld inspection, checklist | No |
| **Documentation package** | Verify all certs, test reports, inspection records compiled | Material certs (steel, Al, AM, chain), HDG/anodize certs, weld inspection reports, RCS test data, GPS test data, orthogonality measurements | 100% | Filing system | YES -- unit not released without complete documentation |

---

## 5. Assembly Sequence (Factory)

### 5.1 Step-by-Step Factory Assembly

| Step | Description | Tools | Personnel | Time (hrs) | QC Hold? |
|------|-------------|-------|-----------|------------|----------|
| **F01** | **Receive and inspect hull shell** (2 half-sections from HDPE fabricator). Incoming inspection: wall thickness, dimensions, surface quality. | UT gauge, tape, scale | 2 (QC + handler) | 2.0 | No |
| **F02** | **Join hull sections** (IF-07): Align 2 half-hulls on flat assembly floor. Insert EPDM gasket. Mate flanges. Bolt 34x M12 SS in star pattern to 40 N-m. Apply Sikaflex 291 exterior seal. Install steel backing channel inside joint. | Torque wrench, sealant gun, rubber mallet, lifting straps | 3 (2 fitters + 1 helper) | 4.0 | No |
| **F03** | **Fill hull with PU foam**: Mix and pour 2-component rigid PU foam into hull cavity through fill ports. Allow 24h cure at ambient (>=20C). | Foam dispensing equipment, PPE (respirator, gloves) | 2 (foam tech + helper) | 2.0 (pour) + 24h (cure) | No |
| **F04** | **Trim and finish hull**: Trim flash from rotomold/weld seams. Drill bolt holes for IF-01 (84x M12, 300mm spacing around perimeter). Drill holes for IF-06 tow padeyes (8x M12). Install scupper drains. Apply deck non-skid texture (optional). Mark identification (project code, serial, mass). | Drill press or hand drill, jig for hole spacing, non-skid paint | 2 (fitter + helper) | 4.0 | No |
| **F05** | **Receive and inspect steel frame** (from fab shop, galvanized). Incoming inspection: weld quality (visual + UT on pad eye), dimensions, socket positions, HDG thickness. | Weld gauge, UT flaw detector, tape, protractor, coating gauge | 2 (QC + welder/inspector) | 3.0 | **YES** -- critical weld inspection |
| **F06** | **Install frame into hull** (IF-01): Lower frame into hull from top using overhead crane or chain hoist. Align frame bolt holes with hull bolt holes using drift pins. Install 84x M12 SS 316 bolts with fender washers (HDPE side), Nylock nuts. Torque to 40 N-m in 3 passes (finger tight, 20 N-m, 40 N-m). Apply Sikaflex 291 sealant between frame flange and hull. | Overhead crane or chain hoist (500 kg), 19mm socket wrench, torque wrench, sealant gun, drift pins | 3 (2 fitters + 1 crane operator) | 4.0 | No |
| **F07** | **Install tow padeyes** (IF-06): Bolt 2x tow padeyes to hull perimeter through frame flange. 4x M12 Grade 8.8 HDG bolts each, fender washers on HDPE side. Torque to 80 N-m. | 19mm socket wrench, torque wrench | 2 (fitters) | 1.0 | No |
| **F08** | **Pad eye proof load test** (IF-02): Apply 1.5x SWL (6,804 kgf) to central mooring pad eye using hydraulic jack bearing against hull. Hold 60 seconds. Inspect for deformation, bolt loosening, weld cracking. | Hydraulic jack (10-ton), load cell, dial indicator for deformation, torque wrench for bolt recheck | 2 (test tech + QC) | 1.5 | **YES** -- critical safety test |
| **F09** | **Hydrostatic leak test**: Float hull in test tank or harbor slip. Observe for 4 hours. Inspect hull section joint (IF-07), foam fill ports, bolt penetrations for leaks. Mark any leak locations. | Test tank or harbor access, marking pen, stopwatch | 2 (QC + handler) | 4.0 (observe) | **YES** -- reject if leak found |
| **F10** | **Receive and inspect CNC face plates** (24x from CNC shop, anodized). Incoming inspection: flatness, roughness, dimensions, anodize thickness. | Surface plate, feeler gauge, roughness tester, calipers, eddy-current gauge | 1 (QC) | 3.0 | No |
| **F11** | **Receive and inspect AM frames** (8x from ASEAN bureau, hard anodized). Incoming inspection: orthogonality of face planes (CMM or angle gauge), dimensions, material cert, anodize thickness. | CMM (outsource) or digital angle gauge, calipers, eddy-current gauge | 1 (QC) | 4.0 | **YES** -- orthogonality critical |
| **F12** | **Assemble 8x reflectors** (M4): For each reflector: clean frame datum surfaces, insert 6x alignment dowel pins, position 3 face plates, install 12x M6 SS bolts + Nylock nuts, torque to 8 N-m, safety wire bolt pairs. Measure 3 face-pair orthogonality angles. Record. | Clean bench, torque wrench (1-20 N-m), Allen keys, safety wire pliers, digital angle gauge | 2 (assembly tech + QC) | 4.0 (30 min each x 8) | **YES** -- 100% orthogonality check |
| **F13** | **Receive and inspect masts** (8x from fab shop, galvanized). Incoming inspection: straightness, base/top plate perpendicularity, pin hole position, HDG thickness. | Straight edge, protractor, calipers, coating gauge | 1 (QC) | 1.5 | No |
| **F14** | **Pre-assemble 8x mast-reflector units** (M5, IF-04): For each unit: install nylon isolation bushings in mast top plate bolt holes, place nylon isolation washers on mating surface, apply Tef-Gel to dowel pins, seat reflector on mast top plate (dowels engage first), insert 4x M10 bolts through isolators, install Nordlock washers + Nylock nuts, torque to 50 N-m, safety wire bolt pairs. | Soft mallet, torque wrench (20-100 N-m), safety wire pliers, Tef-Gel tube | 2 (assembly techs) | 3.0 (22 min each x 8) | No |
| **F15** | **Assemble GPS beacon** (M6): Mount GNSS/Iridium module in IP67 enclosure. Connect Li-ion battery pack. Seal enclosure. Mount SS U-bolt bracket. Functional test: power on, GPS fix, Iridium SBD send/receive. | Soldering iron (if needed), screwdriver set, IP67 seal test rig | 1 (electronics tech) | 2.0 | No |
| **F16** | **Mount GPS beacon on designated mast** (IF-05): Attach beacon bracket to GPS mast (M5-1, with 0.5m extension tube if needed) using 2x M8 SS U-bolts. Tighten to 15 N-m. Orient antenna skyward. | 13mm spanner, torque wrench | 1 (assembly tech) | 0.5 | No |
| **F17** | **GPS 72h endurance test** (first article + every 5th unit): Power on beacon, transmit at 1 Hz for 72h. Monitor SBD messages at shore station. Record battery voltage profile. | Timer, Iridium monitoring dashboard, battery voltage logger | 1 (test tech, monitoring) | 72h (background) | **YES** (first article) |
| **F18** | **Prepare mooring kit** (M7): Receive all COTS components. Splice eyes in polyester rode (2 eyes). Assemble kit: anchor + chain + shackle + swivel + rode + shackle. Verify all shackle pins moused with SS wire. Label kit with depth variant (S/M/D) and SWL. | Rope splicing tools (fid, whipping twine), shackle key, SS mousing wire | 1 (rigger) | 2.0 | No |
| **F19** | **Prepare tow kit** (M8): Receive Dyneema bridle (pre-spliced) and drogue. Inspect splice quality (tuck count >=24). Assemble: 2x bridle legs + 2x bow shackles + 2x thimbles + trailing drogue on swivel. Pack in kit bag. | Shackle key, inspection | 1 (rigger) | 1.0 | No |
| **F20** | **Final assembly verification**: Insert all 8 mast-reflector units into deck sockets (dry run). Verify all locking pins engage. Remove units and package. Weigh complete system (hull + frame + all components). | Pliers, floor scale or crane scale | 3 (2 assembly + 1 QC) | 2.0 | **YES** -- mass check |
| **F21** | **360 deg RCS measurement**: Set up target on turntable or tow slowly in circle at test range. Measure RCS at 1-degree increments over 360 deg at X-band (9.4 GHz). Compare to SIG-001 through SIG-004 requirements. | Portable X-band radar, turntable or tow boat, data acquisition laptop | 3 (2 test engineers + 1 operator) | 4.0 | **YES** -- release gate |
| **F22** | **Documentation and packaging**: Compile all material certs, inspection reports, test data into unit documentation package. Package unit for transport (see Section 9). Apply shipping labels. | Filing system, packing materials | 2 (QC + handler) | 3.0 | **YES** -- doc review |
| | **FACTORY TOTAL** | | **Peak: 3 persons** | **~52 hrs active labor** (~7 working days) | |

### 5.2 Factory Flow Diagram

```
FACTORY PRODUCTION FLOW — VN-TGT-SEA-001
═══════════════════════════════════════════════════════════════

   TRACK A: HULL                   TRACK B: STEEL            TRACK C: REFLECTORS
   ──────────────────              ──────────────────         ─────────────────────
   Receive hull halves (F01)       Receive frame (F05)       Receive face plates (F10)
        │                               │                    Receive AM frames (F11)
   Join sections (F02)             QC: weld UT, dims              │
        │                          HDG thickness              Assemble 8x M4 (F12)
   Pour PU foam (F03)                  │                     QC: orthogonality
   [24h cure]                          │                          │
        │                              │                     Receive masts (F13)
   Trim + drill (F04)                  │                          │
        │                              │                     Pre-assemble 8x M5 (F14)
        │                              │                          │
        ╰──────────────────┬───────────╯                     Assemble GPS beacon (F15)
                           │                                 Mount GPS on mast (F16)
                  Install frame (F06)                             │
                  Install tow padeyes (F07)                       │
                  Pad eye proof load (F08)                        │
                  Hydrostatic leak test (F09)                     │
                           │                                      │
                           ╰──────────────────┬───────────────────╯
                                              │
                                    Final dry-fit (F20)
                                    RCS measurement (F21)
                                    Documentation (F22)
                                              │
                                         ┌────┴────┐
                                         │ RELEASE │
                                         └─────────┘

  Critical Path: Track C (AM frame lead time) → F12 → F14 → F20 → F21
  Parallel: Tracks A, B, C can proceed simultaneously
```

---

## 6. Field Deployment Procedure

### 6.1 Pre-Deployment Preparation (Shore/Quayside)

| Step | Description | Crew | Time (min) | Safety Note |
|------|-------------|------|------------|-------------|
| D-01 | **Pre-deployment briefing**: Review deployment plan, sea state forecast, mooring depth, target position, communications plan. Assign roles. | 4 (all crew) | 15 | Abort criteria: SS >5 for deployment operations |
| D-02 | **Load target onto support vessel** (or tow from quayside): If deck-carry, lift hull with crane onto vessel deck (or flatbed to ramp launch). If tow, connect M8 tow bridle to hull tow padeyes (IF-06). | 4 + crane operator | 30 | Max lift mass ~980 kg; use certified lifting straps rated >=2,000 kg |
| D-03 | **Load mooring kit (M7)**: Load anchor, chain, rode, shackles onto support vessel deck. Flake chain and rode on deck for deployment. | 2 | 15 | Chain handling gloves required; watch for finger pinch |
| D-04 | **Load mast-reflector units (M5 x8)** and tow kit (M8): Secure M5 units in padded vertical rack on vessel deck. Load tow kit bag. | 2 | 15 | Each M5 unit is 31.3 kg; 2-person lift |
| D-05 | **Activate GPS beacon**: Power on M6 GPS beacon (already mounted on M5-1 designated GPS mast). Verify GPS fix and Iridium SBD received at shore station. | 1 | 5 | Confirm shore station receiving before departure |

### 6.2 Mooring Pre-Deployment (At Target Site)

| Step | Description | Crew | Time (min) | Safety Note |
|------|-------------|------|------------|-------------|
| D-06 | **Transit to target site**: Support vessel transits to deployment coordinates. Confirm water depth with echo sounder. | Vessel crew | Variable (1-4 hrs) | Monitor weather en route; abort if deteriorating |
| D-07 | **Deploy anchor**: Lower Danforth/Bruce anchor over side with chain leader. Pay out chain + rode to scope 5:1 (shallow) to 7:1 (deep). Attach surface buoy to top of rode with 5m pick-up line. | 3 + vessel crew | 30 | Use vessel winch for controlled lowering; keep hands clear of chain |
| D-08 | **Set anchor**: Vessel backs down on mooring at 2x working load (~1,160 kgf) for 5 minutes. Monitor GPS for anchor drag (position shift >10m = reset). | Vessel crew | 15 | Do not exceed 2x working load; monitor vessel tension gauge |
| D-09 | **Confirm anchor set**: Verify vessel returns to anchor position after engines neutral. Mark buoy with "MOORING - DO NOT REMOVE" label. | 1 | 5 | -- |

### 6.3 Target Deployment

| Step | Description | Crew | Time (min) | Safety Note |
|------|-------------|------|------------|-------------|
| D-10 | **Position target alongside mooring buoy**: Tow or maneuver target hull to mooring buoy position. Hold target alongside buoy with vessel. | 2 + vessel crew | 15 | Fender between target and vessel to prevent hull damage |
| D-11 | **Connect mooring** (IF-02): Pick up mooring buoy. Pass mooring line/chain through vessel, shackle top of mooring chain to hull central pad eye (200x200mm, IF-02). Tighten shackle pin. Mouse pin with SS wire. | 2 | 10 | Ensure shackle pin fully seated and moused; hands clear during connection |
| D-12 | **Release target from vessel**: Cast off tow line / vessel lines. Allow target to drift to mooring equilibrium position. Verify target weathervanes freely 360 deg. | 2 | 5 | Ensure all vessel lines clear before release |
| D-13 | **Erect mast-reflector units** (IF-03 x8): Transfer 8x M5 units from vessel to target deck (pass by hand, 31.3 kg each). For each mast: insert tube into deck socket, push down until base plate seats on flange, insert M12 clevis pin through aligned holes, clip R-clip, attach safety wire from pin to base plate. | 2 (on target deck) + 1 (passing from vessel) | 20 (2.5 min each) | 2-person lift per mast; wear non-skid footwear on wet deck; work bow-to-stern |
| D-14 | **Verify all locking pins**: Walk around deck, visually confirm 8x clevis pins inserted, 8x R-clips engaged, 8x safety wires attached. | 1 | 3 | -- |
| D-15 | **Verify GPS beacon**: Confirm GPS beacon (on M5-1 at >=4.5m AWL) transmitting position. Shore station confirms reception. | 1 | 2 | Call shore station by radio to confirm |
| D-16 | **Disconnect tow bridle** (if used for transit): Unshackle tow bridle legs from hull tow padeyes (IF-06). Recover tow bridle and drogue onto vessel. | 2 | 5 | -- |
| D-17 | **Final visual inspection from vessel**: Circle target at 50m. Verify all 8 mast-reflector units vertical, no visible damage, mooring line taut, target floating level. Photograph target from 4 cardinal directions for records. | 1 (observer) + vessel crew | 10 | Take photographs for QC records |
| D-18 | **Depart and establish exclusion zone**: Vessel departs. Shore station broadcasts NOTAM (Notice to Mariners) with target position and 5 km exclusion radius. | Vessel crew | 5 | Confirm NOTAM issued before leaving area |
| | **TOTAL FIELD DEPLOYMENT** | **4 crew + vessel** | **~155 min** (2.5 hrs, excl. transit) | |

---

## 7. Production Schedule -- First Lot of 10 Units

### 7.1 Material Procurement Lead Times

| Material / Component | Order Date | Lead Time | Delivery Date | Qty for 10 Units | Notes |
|---------------------|-----------|-----------|---------------|-------------------|-------|
| HDPE sheet/resin | Week 0 | 3 weeks | Week 3 | 4,000 kg | Or rotomold resin if Option A |
| S235 steel (plate + tube + angle) | Week 0 | 2 weeks | Week 2 | 3,000 kg | Stock items from Hoa Phat |
| 6061-T6 Al sheet (3mm or 25mm plate) | Week 0 | 4 weeks | Week 4 | 600 kg (10 sheets) | Import from Korea |
| AlSi10Mg AM frames (80x) | Week 0 | 3 weeks | Week 3 | 80 frames | 8 per unit x 10; order in 2 batches of 40 |
| SS 316 fasteners (all sizes) | Week 0 | 2 weeks | Week 2 | Bulk (per BOM x10) | Stock from fastener distributor |
| G30 HDG chain (19mm) | Week 0 | 1 week | Week 1 | 500m (50m/unit avg) | Stock from marine chandler |
| Polyester rode (20mm) | Week 0 | 2 weeks | Week 2 | 800m (80m/unit avg) | Stock from rope supplier |
| Danforth anchors (50 kg) | Week 0 | 3 weeks | Week 3 | 10 units | May need special order |
| Swivels, shackles, hardware | Week 0 | 2 weeks | Week 2 | Per BOM x10 | Marine chandler stock |
| Dyneema SK75 (16mm) | Week -2 | 6 weeks | Week 4 | 600m (60m/unit) | Import -- order 2 weeks early |
| GPS/Iridium modules | Week -2 | 6 weeks | Week 4 | 10 units | Import -- order 2 weeks early |
| PU foam (2-component) | Week 1 | 2 weeks | Week 3 | 2,500 kg | Local supply |
| Nylon isolation bushings, washers | Week 0 | 2 weeks | Week 2 | Per BOM x10 | Specialty plastics distributor |
| Sikaflex 291 marine sealant | Week 0 | 1 week | Week 1 | 30 cartridges | Building supply store |
| Tef-Gel anti-seize | Week 0 | 2 weeks | Week 2 | 10 tubes | Marine supply import |

**Critical path procurement:** 6061-T6 Al (4 weeks), AM frames (3 weeks), Dyneema (6 weeks), GPS modules (6 weeks). Order Dyneema and GPS modules 2 weeks before other materials.

### 7.2 Fabrication Schedule (Parallel Tracks)

```
PRODUCTION SCHEDULE — LOT 1 (10 UNITS)
Week:  -2  -1   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
═══════════════════════════════════════════════════════════════════════════════

PROCUREMENT
  Long-lead (Dyneema, GPS)
  ├──ORDER──┤          ├──RECEIVE──┤
  Standard materials
              ├──ORDER──┤   ├────RECEIVE (rolling)────┤

TRACK A: HULL FABRICATION (outsourced)
  Hull welding/rotomolding                    ├──── 10 hulls ────┤
  (10 hulls, 1/week)                  Wk3─────────────────────Wk12

TRACK B: STEEL FABRICATION (outsourced)
  Frame + mast fab                 ├──── 10 frames + 80 masts ────┤
  (starts Wk 2, steel delivered)   Wk2──────────────────────────Wk9
  Hot-dip galvanizing                    ├── HDG (rolling, 3-5 day per batch) ──┤
                                         Wk4───────────────────────────────Wk10

TRACK C: REFLECTOR PRODUCTION
  AM frames batch 1 (40x)    ├─── LPBF + HT + CNC + anodize ───┤
  (ordered Wk 0)              Wk0────────────────────────────Wk4
  AM frames batch 2 (40x)         ├─── LPBF + HT + CNC + anodize ───┤
  (ordered Wk 1)                   Wk1────────────────────────────Wk5
  CNC face plates (240x)                    ├── 240 plates, 48/week ──┤
  (Al delivered Wk 4)                        Wk4─────────────────Wk9
  Type II anodize (face plates)                   ├── rolling batches ──┤
                                                   Wk5────────────Wk10

TRACK D: ASSEMBLY (in-house)
  Unit 1 assembly                                        ├──U1──┤
  Unit 2 assembly                                           ├──U2──┤
  Unit 3 assembly                                              ├──U3──┤
  ...                                                             ...
  Unit 10 assembly                                                       ├U10┤
  (1 unit per 3-4 days after materials converge)          Wk7──────────Wk14

TRACK E: QC / TEST
  RCS measurement (per unit, 4 hrs each)                    ├─ rolling ─┤
                                                             Wk8─────Wk14
  GPS endurance test (first article: 72h)                   ├72h┤
                                                             Wk7
  Documentation + packaging                                 ├─ rolling ─┤
                                                             Wk8─────Wk14

DELIVERY
  First unit ready                                               ▼ Wk 9
  Last unit (10th) ready                                              ▼ Wk 14
  ═══════════════════════════════════════════════════════════════════════════
  Total program: 16 weeks (Wk -2 to Wk 14) = 4 months from PO to lot complete
```

### 7.3 Key Schedule Milestones

| Milestone | Target Date | Dependency |
|-----------|-------------|------------|
| Purchase orders issued (all) | Week 0 (Dyneema/GPS at Week -2) | Budget approval |
| All raw materials received | Week 4 | Supplier delivery |
| First hull complete | Week 4 | HDPE fabricator |
| First frame + masts galvanized | Week 5 | Steel fab + HDG |
| All 80 AM frames received + inspected | Week 5 | ASEAN AM bureaus |
| First 24 CNC face plates anodized | Week 6 | CNC shop + anodizer |
| First unit assembly starts | Week 7 | All materials for Unit 1 converged |
| First unit RCS tested + released | Week 9 | Assembly + test |
| Lot complete (10/10 released) | Week 14 | Rolling assembly + test |

---

## 8. Production Capacity Analysis

### 8.1 Bottleneck Identification

| Process Step | Capacity (units/month) | Bottleneck? | Limiting Factor |
|--------------|----------------------|-------------|-----------------|
| HDPE hull fabrication | 4-6 hulls/month (1-section welding) or 8-10 (rotomold) | **POTENTIAL** (welding) | Welding labor (1 hull/week); resolved by rotomolding at scale |
| Steel frame + mast fabrication | 8-10 sets/month | No | Standard fab shop capacity; can use 2 shops in parallel |
| Hot-dip galvanizing | 20+ sets/month | No | Batch process, high throughput |
| CNC face plates (24/unit) | 6-8 units/month (144-192 plates) | No | 1 VMC can produce ~48 plates/week; 2 VMCs for redundancy |
| AM frames (8/unit) | **2-3 units/month per AM bureau** | **YES -- PRIMARY BOTTLENECK** | LPBF build time + post-processing; 2-3 week lead per batch of 8 |
| Anodize (Type II + Type III) | 10+ units/month | No | Batch process, high throughput |
| Reflector assembly (in-house) | 8-10 units/month | No | 2 techs x 4 hrs/unit = 40 hrs/month = 10 units |
| Final assembly + integration | 6-8 units/month | No | 2-3 days per unit; 2 assembly stations |
| RCS measurement | 6-8 units/month | No | 4 hrs/unit; can test 2/week with 1 radar setup |

**Primary bottleneck: AM frame production.** A single AM bureau can deliver approximately 2-3 batches of 8 frames per month (16-24 frames/month = 2-3 units/month worth). This is insufficient for the 6 units/month target.

### 8.2 Bottleneck Resolution Strategy

| Strategy | Effect | Implementation |
|----------|--------|----------------|
| **Qualify 3 AM bureaus** (Xometry, Facfox, JR Tech) | 3 x 2 batches/month = 6 batches = 48 frames = **6 units/month** | Pre-qualify all 3 bureaus with first-article inspection; distribute orders evenly |
| **Buffer stock of AM frames** | Absorb lead time variability | Maintain 16-frame (2-unit) buffer stock at all times; reorder when buffer drops to 8 frames |
| **CNC fallback frames** | Eliminate AM bottleneck entirely | If military accepts +-0.3 deg tolerance (Concept A-CNC), produce all frames locally by CNC; capacity unlimited |
| **Future: Vietnamese LPBF investment** | Domestic AM capacity | 2-3 year timeline; EOS M290 investment ~$500K; requires trained operator and powder supply chain |

### 8.3 Steady-State Capacity (6 Units/Month)

| Resource | Required for 6 units/month | Available | Margin |
|----------|---------------------------|-----------|--------|
| HDPE hulls | 6/month | 4-6 (welding) or 8-10 (rotomold) | TIGHT (welding) / OK (rotomold) |
| Steel frames + masts | 6 sets/month | 8-10 from 1 shop | +33% margin |
| AM frames | 48/month | 48 from 3 bureaus | **0% margin -- at capacity** |
| CNC face plates | 144/month | 192 from 1 VMC | +33% margin |
| Assembly labor | 36 person-days/month | 44 (2 techs x 22 days) | +22% margin |
| RCS test slots | 24 hrs/month | 88 hrs (22 days x 4 hrs) | >>100% margin |

### 8.4 Scaling Plan to 100 Units/Year

| Production Level | Rate | AM Strategy | Hull Strategy | Assembly | Investment Required |
|-----------------|------|-------------|---------------|----------|---------------------|
| **Pilot batch** | 3 units (lot) | 1 AM bureau, 1 batch | HDPE welding | 1 assembly station | $0 (existing capability) |
| **Low rate** (current) | 10 units / 4 months | 2 AM bureaus | HDPE welding | 1 assembly station | $0 |
| **Medium rate** | 6 units/month (72/year) | 3 AM bureaus | Rotomolding (invest in mold) | 2 assembly stations | $30K (mold) + $10K (2nd assembly station) |
| **Full rate** | 10 units/month (100+/year) | 3 AM bureaus + VN LPBF or CNC fallback | Rotomolding (2 mold sets) | 3 assembly stations | $60K (2nd mold) + $500K (VN LPBF) or $0 (CNC fallback) |

---

## 9. Packaging and Transport

### 9.1 Packaging Configuration

| Component | Package Type | Dimensions (L x W x H) | Mass | Transport Mode | Notes |
|-----------|-------------|------------------------|------|----------------|-------|
| **Hull (2 sections)** | Open flatbed or in 40 ft container | Each half: 4.0m x 4.0m x 0.6m | ~175 kg each (350 total) | **Option A:** 2 halves stacked flat on standard flatbed truck (width 4.0m = oversize, requires permit). **Option B:** 2 halves in 40 ft container (12.2m internal), laid flat end-to-end. | Wrap in PE shrink wrap or blanket for surface protection. Foam blocks between halves if stacked. |
| **Mast assemblies (8x)** | Bundled in steel or wood cradle | Bundle: 3.1m x 0.3m x 0.3m | ~130 kg (16.3 kg each x 8) | Container or flatbed | Bundle 8 masts with ratchet straps; pad base/top plates with foam to prevent HDG damage. Fits easily in container lengthwise. |
| **Reflector assemblies (8x)** | Individual padded crates | Crate: 0.9m x 0.9m x 0.5m each; or palletized 4-stack | ~15 kg each (120 kg total + crate) | **Custom plywood crate with closed-cell foam lining.** Stack max 4 high on pallet (2 pallets for 8 reflectors). | CRITICAL: Face plates must not contact each other (foam separators between reflectors). Handle with care -- anodize surface sensitive to scratching. |
| **GPS beacon (1x)** | Pelican case or padded box | 0.4m x 0.3m x 0.3m | ~5 kg + case | Inside reflector crate or separate small box | Ship battery disconnected. Include spare battery pack. |
| **Mooring kit (M7)** | Palletized | Pallet: 1.2m x 1.0m x 0.8m | 80-200 kg (depth dependent) | Pallet on flatbed or in container | Anchor on base, chain coiled, rode flaked on top. Shrink-wrap entire pallet. Mark depth variant (S/M/D). |
| **Tow kit (M8)** | Duffle bag or crate | 0.8m x 0.5m x 0.3m | ~15 kg | Inside container with other kits | Dyneema bridle coiled, drogue folded, hardware in mesh bag. |
| **Fastener kit + spares** | Parts bin or toolbox | 0.5m x 0.3m x 0.2m | ~10 kg | Inside container | Spare locking pins (4x), spare R-clips (8x), spare safety wire (2 rolls), Tef-Gel (1 tube), grease (1 tube), spare shackles (2x). |
| **Documentation package** | Waterproof document tube or folder | -- | ~1 kg | With unit | Certs, inspection reports, deployment manual, RCS test data. |

### 9.2 Container Packing Plan (40 ft Standard Container)

```
40 ft CONTAINER PACKING PLAN — 1 COMPLETE TARGET SYSTEM
════════════════════════════════════════════════════════════════════
Container internal: 12.03m (L) x 2.35m (W) x 2.39m (H)
Max payload: 26,680 kg (far exceeds our ~700 kg)

PLAN VIEW:
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  Hull half A (4.0m x 4.0m x 0.6m)      Hull half B              │
│  ┌────────────────────┐                 ┌────────────────────┐   │
│  │                    │                 │                    │   │← 2.35m
│  │   Laid flat, may   │                 │   Laid flat        │   │  wide
│  │   overhang or      │  Mast bundle    │                    │   │
│  │   angle to fit     │  (3.1m long)    │                    │   │
│  │   2.35m width      │  ┌──────────┐   │                    │   │
│  │                    │  │ 8 masts  │   │                    │   │
│  └────────────────────┘  └──────────┘   └────────────────────┘   │
│  ←──── 4.0m ────→       ←─ 0.5m ─→     ←──── 4.0m ────→         │
│                                                                  │
│                          ┌──────┐  ┌──────┐  ┌──────┐           │
│                          │Refl. │  │Refl. │  │Moor. │           │
│                          │crate │  │crate │  │pallet│           │
│                          │(4x)  │  │(4x)  │  │      │           │
│                          └──────┘  └──────┘  └──────┘           │
│                          ←0.9m→    ←0.9m→    ←1.2m→             │
│                                                                  │
│  ← ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ 12.03m ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ → │
└──────────────────────────────────────────────────────────────────┘

NOTE: 4.0m hull half-disc exceeds 2.35m container width.
RESOLUTION OPTIONS:
  (a) Transport hull halves on flatbed truck (oversize permit), container
      for everything else.
  (b) Cut hull into 4 quarter-sections (4x 2.0m arcs) — fits in container
      width but adds 2 more IF-07 joints.
  (c) Use open-top container (hull halves protrude above container sides).

RECOMMENDED: Option (a) — Hull on flatbed, all other components in 20 ft container.

20 ft CONTAINER (6.06m x 2.35m x 2.39m):
┌──────────────────────────────────────┐
│ Mast bundle (3.1m)                    │
│ Reflector crates x2 (0.9m x 0.9m)    │
│ Mooring pallet (1.2m x 1.0m)         │
│ Tow kit bag                           │
│ GPS case + fastener kit + docs        │
│ Total mass: ~350 kg                   │
└──────────────────────────────────────┘
```

### 9.3 Oversize Load Transport (Hull Sections)

| Parameter | Value |
|-----------|-------|
| Hull half dimensions | 4.0m dia half-disc x 0.6m deep |
| Transport width | 4.0m (exceeds 2.5m standard) |
| Transport height | 0.6m + flatbed height (~1.2m) = ~1.8m total (within 4.0m legal height) |
| Transport length | 4.0m (fits standard flatbed) |
| Permit required | **Yes -- oversize width permit** (Vietnam: "Giay phep van chuyen hang sieu truong, sieu trong") |
| Escort vehicle | Required for >3.0m width loads per Vietnamese road transport regulations |
| Route restrictions | Avoid narrow bridges, urban centers; prefer highway/port access roads |
| Stacking | 2 hull halves can stack (total height ~2.4m) to use 1 flatbed trip |
| Alternative | Barge/coastal vessel transport from factory (Hai Phong / HCMC) to deployment port -- avoids road width restrictions |

---

## 10. Cost Summary -- Production

### 10.1 Per-Unit Production Cost Breakdown (at 10 units)

| Cost Category | Value ($) | % of Unit Cost |
|---------------|-----------|----------------|
| **Raw materials (procured)** | $12,800 | 35.9% |
| **Outsourced processing** (CNC, AM, HDG, anodize, hull fab) | $9,400 | 26.4% |
| **In-house labor** (assembly, QC, test, packaging) | $5,200 | 14.6% |
| **Overhead** (facility, utilities, tooling amortization) | $1,800 | 5.1% |
| **Logistics** (shipping AM frames from ASEAN, transport to port) | $1,200 | 3.4% |
| **QC/test consumables** (test equipment amortization, calibration) | $800 | 2.2% |
| **Margin** (10%) | $3,240 | 9.1% |
| **Documentation + packaging** | $1,160 | 3.3% |
| **TOTAL** | **$35,600** | **100%** |

### 10.2 Local Content Achieved

| Category | Value ($) | Local ($) | Local % |
|----------|-----------|-----------|---------|
| Vietnamese materials + processing | $18,600 | $18,600 | 100% |
| ASEAN imports (AM frames, anodize) | $9,800 | $0 | 0% |
| Other imports (Al sheet, GPS, Dyneema) | $3,960 | $0 | 0% |
| In-house value-add (labor, QC, margin) | $12,240 | $12,240 | 100% |
| **TOTAL** | **$35,600** | **$22,240** | **62.5%** |

Meets >=60% local content target per CLAUDE.md success metric. Path to higher local content per M4 Section 5.4.

---

## 11. Cross-References

### Phase 3 Documents
- [[PRAD_A7_architecture_definition.md]] -- Module decomposition, interfaces, assembly sequence
- [[RISM_M4_material_analysis.md]] -- Material selections, cost analysis, local content assessment
- [[RISM_R1_requirements_identification.md]] -- 74 embodiment requirements
- [[RISM_I2_critical_requirements.md]] -- Critical requirements prioritization
- [[RISM_S3_material_selection.md]] -- Material screening
- [[PRAD_D8_design_structure.md]] -- Structural sizing

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1), PRD-001 to PRD-008, QUA-001 to QUA-006, ASM-001 to ASM-006

### Key Requirements Traced
| Requirement | Description | How Addressed |
|-------------|-------------|---------------|
| PRD-001 | Production rate >=6 units/month | Section 8: 6 units/month achievable with 3 AM bureaus |
| PRD-002 | Local content >=85% | Section 10.2: 62.5% achieved; 85% requires CNC fallback or ASEAN reclassification |
| PRD-003 | >=2 qualified AM bureaus | Section 2: 3 identified (Xometry, Facfox, JR Tech) |
| PRD-004 | CNC face plates from VN shops | Section 2: Hai Phong CNC + Minh Phuc CNC identified |
| PRD-005 | HDPE hull from VN supplier | Section 2: Binh Minh Plastics + Tien Phong Plastics |
| PRD-006 | Rejection rate <5% | Section 4: 100% inspection on critical dimensions |
| PRD-007 | AM lead time <=3 weeks | Section 2: 2-3 weeks from ASEAN bureaus (meets) |
| PRD-008 | Tooling investment <=15K | Section 1.2: $24-30K for rotomold (exceeds; $3-5K for welding approach) |
| QUA-001 | 360 deg RCS measurement per unit | Section 4.3: 100% RCS test at final acceptance |
| QUA-002 | 100% orthogonality check | Section 4.2: 100% digital angle gauge, 3 face-pairs per reflector |
| ASM-006 | Field mast erection <=15 min | Section 6.3 step D-13: 20 min allocated (marginal; optimize with practice) |
| CST-001 | Unit cost <=$36,000 | Section 10.1: $35,600 (meets) |
| ERG-002 | Deployment <=30 min | Section 6.3: ~40 min on-target (mooring pre-deployed); optimize with crew training |

---

## 12. Open Items

| Item | Description | Owner | Target | Status |
|------|-------------|-------|--------|--------|
| OCP-P15-001 | Qualify 3 ASEAN AM bureaus with first-article inspection | Procurement | Before pilot batch | OPEN |
| OCP-P15-002 | Qualify 2 Vietnamese CNC shops for face plate machining | Procurement | Before pilot batch | OPEN |
| OCP-P15-003 | Resolve hull fabrication method: welding vs rotomolding (TBD-007) | Manufacturing | Before Lot 1 | OPEN |
| OCP-P15-004 | Procure/fabricate RCS test equipment (portable X-band radar + turntable) | Engineering | Before Unit 1 test | OPEN |
| OCP-P15-005 | Develop field deployment SOP with crew training program | Operations | Before first deployment | OPEN |
| OCP-P15-006 | Resolve ASM-006 margin: 20 min actual vs 15 min requirement for mast erection | Engineering | Phase 3 sea trial | OPEN |
| OCP-P15-007 | Resolve PRD-008: rotomold tooling $24-30K exceeds $15K limit; use welding for early lots | Manufacturing | Lot 1 | OPEN |
| OCP-P15-008 | Verify oversize transport permit process for 4.0m hull halves | Logistics | Before Lot 1 shipment | OPEN |

---

*End of Step P15: Production Planning. This document defines the manufacturing approach, supply chain, quality system, and production schedule for Vietnamese manufacture of the THANH TRI-H fixed sea target. All downstream Phase 4 detail design builds on this production plan.*
