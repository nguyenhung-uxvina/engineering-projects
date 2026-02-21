# Pahl & Beitz 16 Requirement Categories

Use this table when running `/requirements` to ensure all categories are covered.

| # | Category | Typical Questions | Defense-Specific |
|---|----------|-------------------|------------------|
| 1 | **Geometry** | Dimensions? Weight? | MIL-STD-1366 transport constraints |
| 2 | **Kinematics** | Motion? Speed? Range? | Tracking rates, slew speed |
| 3 | **Forces** | Loads? Shock? Vibration? | MIL-STD-810 vibration profiles |
| 4 | **Energy** | Power source? Efficiency? | Battery life, fuel consumption |
| 5 | **Material** | Material? Corrosion resistance? | Environmental exposure, salt fog |
| 6 | **Signals** | I/O? Interfaces? Data rates? | MIL-STD-1553, RS-232/422 |
| 7 | **Safety** | Fail-safe? Hazards? | MIL-STD-882 hazard analysis |
| 8 | **Ergonomics** | Operator interface? Training? | MIL-STD-1472 human factors |
| 9 | **Production** | Quantity? Rate? Tooling? | Local content 60-75% by value |
| 10 | **Quality** | Reliability? MTBF? | MIL-HDBK-217 reliability prediction |
| 11 | **Assembly** | Assembly sequence? Tools needed? | Field assembly capability? |
| 12 | **Transport** | Shipping? Packaging? | Tactical transport, air-droppable? |
| 13 | **Operation** | Environment? Temperature? Humidity? | MIL-STD-810H operational conditions |
| 14 | **Maintenance** | MTTR? Spares? Tools? | Field-level vs depot-level repair |
| 15 | **Costs** | Target cost? Life cycle cost? | <= 70% of import equivalent |
| 16 | **Schedule** | Deadlines? Milestones? | Contract delivery requirements |

## Category Completeness Check

A valid requirements list must address all 16 categories. Categories with no applicable requirements should be explicitly marked "N/A - [reason]" rather than left blank.
