# VDC-33 Data Analysis Toolkit

## Overview

Python-based analysis toolkit for VDC-33 prototype experiment data with automatic scaling calculations to VDC-100.

## Requirements

```bash
pip install numpy pandas matplotlib scipy
```

## Directory Structure

```
analysis/
├── vdc33_analysis.py       # Main analysis script
├── templates/              # CSV templates for data entry
│   ├── exp1_velocity_pressure.csv
│   ├── exp2_valve_timing.csv
│   ├── exp3_safety.csv
│   ├── exp4_stability.csv
│   ├── exp5_recoil.csv
│   └── exp6_gas.csv
├── results/                # Output directory (auto-created)
└── README.md               # This file
```

## Usage

### Run with Sample Data (Demo)

```bash
python vdc33_analysis.py
```

### Run with Actual Data

1. Copy templates to a data directory
2. Fill in measured values
3. Run analysis:

```bash
python vdc33_analysis.py path/to/data/
```

### Individual Experiment Analysis

```python
from vdc33_analysis import *

# Experiment 1: Velocity vs Pressure
results = analyze_velocity_pressure("data/exp1_velocity_pressure.csv")

# Experiment 2: Valve Timing
results = analyze_valve_timing("data/exp2_valve_timing.csv")

# Experiment 3: Safety Validation
results = analyze_safety_validation("data/exp3_safety.csv")

# Experiment 4: Projectile Stability
results = analyze_projectile_stability("data/exp4_stability.csv")

# Experiment 5: Recoil
results = analyze_recoil("data/exp5_recoil.csv")

# Experiment 6: Gas Consumption
results = analyze_gas_consumption("data/exp6_gas.csv")
```

## Data Templates

### Exp 1: Velocity vs Pressure
```
pressure_bar,shot1,shot2,shot3,shot4,shot5
40,22.1,21.8,22.3,22.0,21.9
50,26.5,26.8,26.3,26.7,26.4
...
```

### Exp 2: Valve Timing
```
dwell_ms,shot1,shot2,shot3,shot4,shot5,p_start,p_end
5,28.1,27.8,28.3,28.0,27.9,200,195
8,33.5,33.8,33.3,33.7,33.4,195,189
...
```

### Exp 3: Safety Validation
```
test_id,test_type,arm,safety,trigger,expected,actual,pass
S1,state,OFF,SAFE,REL,NO_FIRE,NO_FIRE,1
S2,state,OFF,SAFE,PRESS,NO_FIRE,NO_FIRE,1
...
```

### Exp 4: Projectile Stability
```
fin_set,shot,frames_5m,rotations_5m,stability_score
A,1,42,3.5,3
A,2,41,3.4,3
...
```
Stability scores:
- 3 = STABLE
- 2 = SLIGHT WOBBLE
- 1 = MODERATE WOBBLE
- 0 = TUMBLE

### Exp 5: Recoil
```
pressure_bar,shot,peak_force_kg,duration_ms
60,1,3.2,35
60,2,3.1,36
...
```

### Exp 6: Gas Consumption
```
dwell_ms,p_start,p_end,shots
8,200,188,10
12,188,174,10
...
```

## Outputs

### Plots (saved to results/)
- `exp1_velocity_pressure_TIMESTAMP.png` - V vs P curve with fit
- `exp2_valve_timing_TIMESTAMP.png` - Velocity and efficiency vs dwell
- `exp4_stability_TIMESTAMP.png` - Fin set comparison
- `exp5_recoil_TIMESTAMP.png` - Force and impulse comparison
- `exp6_gas_consumption_TIMESTAMP.png` - Shots per fill comparison

### Data Files
- `exp3_safety_results_TIMESTAMP.csv` - Safety test results

## Scaling to VDC-100

The toolkit automatically calculates VDC-100 predictions using:

| Parameter | VDC-33 | VDC-100 | Ratio |
|-----------|--------|---------|-------|
| Bore diameter | 32mm | 100mm | 3.125× |
| Bore area | 804mm² | 7854mm² | 9.77× |
| Projectile mass | 58g | 450g | 7.76× |
| Barrel length | 260mm | 800mm | 3.08× |

Key scaling relationships:
- **Velocity**: Similar at same pressure (force scales with area, but so does mass resistance)
- **Dwell time**: ×1.5-2.0 (larger volume to fill)
- **Gas consumption**: ×9.77 (scales with bore area)
- **Recoil impulse**: ×7.76 (scales with projectile mass)

## Success Criteria

| Experiment | VDC-33 Target | VDC-100 Requirement |
|------------|---------------|---------------------|
| 1. Velocity | 30-40 m/s @ 70 bar | 35-45 m/s @ 100 bar |
| 2. Timing | Identify knee point | Dwell < 30 ms |
| 3. Safety | 100% pass rate | 100% pass rate |
| 4. Stability | Score ≥ 75% | Same fin geometry |
| 5. Recoil | Measure baseline | ≤ 15 Ns |
| 6. Gas | ≥30 shots/fill | ≥ 5 shots/fill |

## Troubleshooting

**Import error**: Install dependencies with `pip install numpy pandas matplotlib scipy`

**No plots showing**: Check `results/` directory for saved PNG files

**Data format error**: Ensure CSV files match template format exactly

---

*Analysis toolkit for VN-CUA-001 VDC-33 prototype validation.*
