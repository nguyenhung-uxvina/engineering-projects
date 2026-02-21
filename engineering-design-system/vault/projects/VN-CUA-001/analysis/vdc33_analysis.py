#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════
VDC-33 PROTOTYPE DATA ANALYSIS
Vietnamese Drone Catcher - 1:3 Scale Prototype
═══════════════════════════════════════════════════════════════════════════

Project:    VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
Prototype:  VDC-33 (1:3 Scale Pneumatic Demonstrator)
Version:    1.0.0
Date:       2026-02-05

Description:
    Comprehensive data analysis toolkit for VDC-33 prototype experiments.
    Includes functions for all 6 experiments with visualization and
    scaling calculations to VDC-100.

Requirements:
    pip install numpy pandas matplotlib scipy

Usage:
    python vdc33_analysis.py

═══════════════════════════════════════════════════════════════════════════
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
from datetime import datetime
import os

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

# VDC-33 Parameters
VDC33_BORE_MM = 32
VDC33_PROJECTILE_MASS_G = 58
VDC33_BARREL_LENGTH_MM = 260

# VDC-100 Parameters (for scaling)
VDC100_BORE_MM = 100
VDC100_PROJECTILE_MASS_G = 450
VDC100_BARREL_LENGTH_MM = 800

# Scaling Factors
BORE_RATIO = VDC100_BORE_MM / VDC33_BORE_MM  # 3.125
AREA_RATIO = BORE_RATIO ** 2  # 9.77
MASS_RATIO = VDC100_PROJECTILE_MASS_G / VDC33_PROJECTILE_MASS_G  # 7.76

# Output directory
OUTPUT_DIR = "results"

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def ensure_output_dir():
    """Create output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def timestamp():
    """Return current timestamp string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def print_header(title):
    """Print formatted section header."""
    print("\n" + "═" * 70)
    print(f"  {title}")
    print("═" * 70 + "\n")

def calculate_statistics(data):
    """Calculate common statistics for a dataset."""
    return {
        'mean': np.mean(data),
        'std': np.std(data, ddof=1),
        'min': np.min(data),
        'max': np.max(data),
        'cv': np.std(data, ddof=1) / np.mean(data) * 100 if np.mean(data) != 0 else 0,
        'n': len(data)
    }

# ═══════════════════════════════════════════════════════════════════════════
# EXPERIMENT 1: VELOCITY VS PRESSURE
# ═══════════════════════════════════════════════════════════════════════════

def analyze_velocity_pressure(data_file=None):
    """
    Analyze velocity vs pressure data.

    Expected CSV format:
        pressure_bar, shot1, shot2, shot3, shot4, shot5
        40, 22.1, 21.8, 22.3, 22.0, 21.9
        50, 26.5, 26.8, 26.3, 26.7, 26.4
        ...

    Returns: dict with analysis results
    """
    print_header("EXPERIMENT 1: VELOCITY VS PRESSURE")

    # Load or create sample data
    if data_file and os.path.exists(data_file):
        df = pd.read_csv(data_file)
        print(f"Loaded data from: {data_file}")
    else:
        # Sample data for demonstration
        print("Using sample data (no file provided)")
        df = pd.DataFrame({
            'pressure_bar': [40, 50, 60, 70, 80, 90, 100],
            'shot1': [22.1, 26.5, 30.2, 33.8, 36.5, 38.9, 40.8],
            'shot2': [21.8, 26.8, 30.5, 33.5, 36.8, 39.2, 41.1],
            'shot3': [22.3, 26.3, 29.9, 33.9, 36.2, 38.7, 40.5],
            'shot4': [22.0, 26.7, 30.3, 33.6, 36.6, 39.0, 40.9],
            'shot5': [21.9, 26.4, 30.1, 33.7, 36.4, 38.8, 40.7]
        })

    # Calculate statistics for each pressure
    results = []
    for _, row in df.iterrows():
        pressure = row['pressure_bar']
        velocities = row[1:].values.astype(float)
        stats_dict = calculate_statistics(velocities)
        stats_dict['pressure_bar'] = pressure
        results.append(stats_dict)

    results_df = pd.DataFrame(results)

    # Print results table
    print("\nResults Summary:")
    print("-" * 70)
    print(f"{'Pressure':<12} {'Mean V':<12} {'Std Dev':<12} {'CV %':<10} {'Min':<10} {'Max':<10}")
    print("-" * 70)
    for _, row in results_df.iterrows():
        print(f"{row['pressure_bar']:<12.0f} {row['mean']:<12.2f} {row['std']:<12.2f} "
              f"{row['cv']:<10.1f} {row['min']:<10.1f} {row['max']:<10.1f}")

    # Curve fitting: V = a * P^b (power law)
    def power_law(P, a, b):
        return a * np.power(P, b)

    pressures = results_df['pressure_bar'].values
    velocities = results_df['mean'].values

    try:
        popt, pcov = curve_fit(power_law, pressures, velocities, p0=[1, 0.5])
        a, b = popt

        # Calculate R²
        v_pred = power_law(pressures, a, b)
        ss_res = np.sum((velocities - v_pred) ** 2)
        ss_tot = np.sum((velocities - np.mean(velocities)) ** 2)
        r_squared = 1 - (ss_res / ss_tot)

        print(f"\nCurve Fit: V = {a:.4f} × P^{b:.4f}")
        print(f"R² = {r_squared:.4f}")

        # Find pressure for target velocity (35-40 m/s)
        target_v = 37.5  # midpoint
        optimal_p = (target_v / a) ** (1/b)
        print(f"\nOptimal pressure for {target_v} m/s: {optimal_p:.1f} bar")

    except Exception as e:
        print(f"Curve fitting failed: {e}")
        a, b, r_squared = None, None, None

    # Scale to VDC-100
    print("\n" + "-" * 70)
    print("SCALING TO VDC-100:")
    print("-" * 70)
    print(f"Bore ratio: {BORE_RATIO:.2f}×")
    print(f"Mass ratio: {MASS_RATIO:.2f}×")
    print("At same pressure, VDC-100 should achieve similar velocity")
    print("(larger bore provides more force, but larger mass requires more)")

    # Plot
    ensure_output_dir()
    fig, ax = plt.subplots(figsize=(10, 6))

    # Error bars
    ax.errorbar(pressures, velocities,
                yerr=results_df['std'].values,
                fmt='o', markersize=8, capsize=5,
                label='Measured data')

    # Fit curve
    if a is not None:
        p_smooth = np.linspace(min(pressures), max(pressures), 100)
        v_smooth = power_law(p_smooth, a, b)
        ax.plot(p_smooth, v_smooth, 'r-',
                label=f'Fit: V = {a:.3f}×P^{b:.3f} (R²={r_squared:.3f})')

    # Target zone
    ax.axhspan(35, 40, alpha=0.2, color='green', label='Target velocity zone')

    ax.set_xlabel('Regulated Pressure (bar)', fontsize=12)
    ax.set_ylabel('Muzzle Velocity (m/s)', fontsize=12)
    ax.set_title('VDC-33 Experiment 1: Velocity vs Pressure', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)

    filename = f"{OUTPUT_DIR}/exp1_velocity_pressure_{timestamp()}.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"\nPlot saved: {filename}")
    plt.close()

    return {
        'results_df': results_df,
        'fit_params': {'a': a, 'b': b, 'r_squared': r_squared},
        'optimal_pressure': optimal_p if a else None
    }

# ═══════════════════════════════════════════════════════════════════════════
# EXPERIMENT 2: VALVE TIMING OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════

def analyze_valve_timing(data_file=None):
    """
    Analyze valve dwell time optimization data.

    Expected CSV format:
        dwell_ms, shot1, shot2, shot3, shot4, shot5, tank_pressure_start, tank_pressure_end
        5, 28.1, 27.8, 28.3, 28.0, 27.9, 200, 195
        8, 33.5, 33.8, 33.3, 33.7, 33.4, 195, 189
        ...
    """
    print_header("EXPERIMENT 2: VALVE TIMING OPTIMIZATION")

    if data_file and os.path.exists(data_file):
        df = pd.read_csv(data_file)
        print(f"Loaded data from: {data_file}")
    else:
        print("Using sample data")
        df = pd.DataFrame({
            'dwell_ms': [5, 8, 10, 12, 15, 20, 25],
            'shot1': [28.1, 33.5, 35.8, 37.2, 37.8, 38.1, 38.2],
            'shot2': [27.8, 33.8, 36.1, 37.0, 37.9, 38.0, 38.3],
            'shot3': [28.3, 33.3, 35.5, 37.3, 37.7, 38.2, 38.1],
            'shot4': [28.0, 33.7, 35.9, 37.1, 37.8, 38.0, 38.2],
            'shot5': [27.9, 33.4, 35.7, 37.2, 37.9, 38.1, 38.1],
            'p_start': [200, 195, 189, 182, 174, 164, 152],
            'p_end': [195, 189, 182, 174, 164, 152, 138]
        })

    # Calculate statistics
    results = []
    for _, row in df.iterrows():
        dwell = row['dwell_ms']
        velocities = row[['shot1', 'shot2', 'shot3', 'shot4', 'shot5']].values.astype(float)
        stats_dict = calculate_statistics(velocities)
        stats_dict['dwell_ms'] = dwell
        stats_dict['gas_per_shot'] = (row['p_start'] - row['p_end']) / 5
        stats_dict['efficiency'] = stats_dict['mean'] / stats_dict['gas_per_shot']
        results.append(stats_dict)

    results_df = pd.DataFrame(results)

    # Print results
    print("\nResults Summary:")
    print("-" * 80)
    print(f"{'Dwell(ms)':<12} {'Mean V':<10} {'Std':<8} {'Gas/shot':<12} {'Efficiency':<12}")
    print("-" * 80)
    for _, row in results_df.iterrows():
        print(f"{row['dwell_ms']:<12.0f} {row['mean']:<10.2f} {row['std']:<8.2f} "
              f"{row['gas_per_shot']:<12.2f} {row['efficiency']:<12.3f}")

    # Find optimal dwell (knee point)
    # Use velocity plateau criterion: where delta V < 0.5 m/s per ms increase
    dwell_vals = results_df['dwell_ms'].values
    vel_vals = results_df['mean'].values

    # Calculate velocity gain per ms
    vel_gain = np.diff(vel_vals) / np.diff(dwell_vals)

    # Knee point: where gain drops below 0.3 m/s per ms
    knee_idx = np.where(vel_gain < 0.3)[0]
    if len(knee_idx) > 0:
        optimal_dwell = dwell_vals[knee_idx[0] + 1]
        optimal_velocity = vel_vals[knee_idx[0] + 1]
    else:
        optimal_dwell = dwell_vals[-1]
        optimal_velocity = vel_vals[-1]

    print(f"\nOptimal dwell time: {optimal_dwell:.0f} ms")
    print(f"Velocity at optimal: {optimal_velocity:.1f} m/s")

    # Best efficiency point
    best_eff_idx = results_df['efficiency'].idxmax()
    print(f"Best efficiency at: {results_df.loc[best_eff_idx, 'dwell_ms']:.0f} ms")

    # VDC-100 scaling
    print("\n" + "-" * 70)
    print("SCALING TO VDC-100:")
    print("-" * 70)
    vdc100_dwell = optimal_dwell * 1.5  # Larger volume needs more time
    print(f"Estimated VDC-100 dwell: {vdc100_dwell:.0f} ms (×1.5 for larger volume)")

    # Plot
    ensure_output_dir()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Velocity vs Dwell
    ax1.errorbar(results_df['dwell_ms'], results_df['mean'],
                yerr=results_df['std'], fmt='o-', markersize=8, capsize=5)
    ax1.axvline(optimal_dwell, color='r', linestyle='--',
                label=f'Optimal: {optimal_dwell:.0f}ms')
    ax1.axhspan(35, 40, alpha=0.2, color='green')
    ax1.set_xlabel('Dwell Time (ms)', fontsize=12)
    ax1.set_ylabel('Muzzle Velocity (m/s)', fontsize=12)
    ax1.set_title('Velocity vs Dwell Time', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Efficiency vs Dwell
    ax2.bar(results_df['dwell_ms'], results_df['efficiency'], width=2, alpha=0.7)
    ax2.set_xlabel('Dwell Time (ms)', fontsize=12)
    ax2.set_ylabel('Efficiency (m/s per bar)', fontsize=12)
    ax2.set_title('Gas Efficiency vs Dwell Time', fontsize=14)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    filename = f"{OUTPUT_DIR}/exp2_valve_timing_{timestamp()}.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"\nPlot saved: {filename}")
    plt.close()

    return {
        'results_df': results_df,
        'optimal_dwell_ms': optimal_dwell,
        'optimal_velocity': optimal_velocity,
        'vdc100_estimated_dwell': vdc100_dwell
    }

# ═══════════════════════════════════════════════════════════════════════════
# EXPERIMENT 3: SAFETY INTERLOCK VALIDATION
# ═══════════════════════════════════════════════════════════════════════════

def analyze_safety_validation(data_file=None):
    """
    Analyze safety interlock validation results.

    Expected CSV format:
        test_id, test_type, arm, safety, trigger, expected, actual, pass
        S1, state, OFF, SAFE, REL, NO_FIRE, NO_FIRE, 1
        S2, state, OFF, SAFE, PRESS, NO_FIRE, NO_FIRE, 1
        ...
    """
    print_header("EXPERIMENT 3: SAFETY INTERLOCK VALIDATION")

    if data_file and os.path.exists(data_file):
        df = pd.read_csv(data_file)
        print(f"Loaded data from: {data_file}")
    else:
        print("Using sample data (all pass)")
        # Create complete test matrix
        tests = []
        # State permutation tests
        states = [
            ('S1', 'state', 'OFF', 'SAFE', 'REL', 'NO_FIRE'),
            ('S2', 'state', 'OFF', 'SAFE', 'PRESS', 'NO_FIRE'),
            ('S3', 'state', 'OFF', 'FIRE', 'REL', 'NO_FIRE'),
            ('S4', 'state', 'OFF', 'FIRE', 'PRESS', 'NO_FIRE'),
            ('S5', 'state', 'ON', 'SAFE', 'REL', 'NO_FIRE'),
            ('S6', 'state', 'ON', 'SAFE', 'PRESS', 'NO_FIRE'),
            ('S7', 'state', 'ON', 'FIRE', 'REL', 'NO_FIRE'),
            ('S8', 'state', 'ON', 'FIRE', 'PRESS', 'FIRE'),
        ]
        for s in states:
            tests.append({
                'test_id': s[0], 'test_type': s[1],
                'arm': s[2], 'safety': s[3], 'trigger': s[4],
                'expected': s[5], 'actual': s[5], 'pass': 1
            })

        # Failure mode tests
        failures = [
            ('F1', 'failure', 'Battery disconnected', 'NO_FIRE'),
            ('F2', 'failure', 'Low battery', 'NO_FIRE'),
            ('F3', 'failure', 'ARM stuck ON', 'NO_FIRE'),
            ('F4', 'failure', 'Solenoid disconnected', 'NO_FIRE'),
            ('F5', 'failure', 'Arduino reset', 'NO_FIRE'),
        ]
        for f in failures:
            tests.append({
                'test_id': f[0], 'test_type': f[1],
                'arm': '-', 'safety': '-', 'trigger': f[2],
                'expected': f[3], 'actual': f[3], 'pass': 1
            })

        # Indication tests
        indications = [
            ('I1', 'indication', 'Power OFF', 'LED_OFF'),
            ('I2', 'indication', 'Power ON, SAFE', 'LED_GREEN'),
            ('I3', 'indication', 'Power ON, ARMED', 'LED_RED'),
            ('I4', 'indication', 'Low battery', 'LED_FLASH'),
        ]
        for i in indications:
            tests.append({
                'test_id': i[0], 'test_type': i[1],
                'arm': '-', 'safety': '-', 'trigger': i[2],
                'expected': i[3], 'actual': i[3], 'pass': 1
            })

        # Live fire tests
        live = [
            ('L1', 'live', 'ON', 'FIRE', 'PRESS', 'FIRE'),
            ('L2', 'live', 'ON', 'FIRE', 'PRESS', 'FIRE'),
            ('L3', 'live', 'ON', 'FIRE', 'PRESS', 'FIRE'),
            ('L4', 'live', 'ON', 'SAFE', 'PRESS', 'NO_FIRE'),
            ('L5', 'live', 'ON', 'SAFE', 'PRESS', 'NO_FIRE'),
            ('L6', 'live', 'ON', 'SAFE', 'PRESS', 'NO_FIRE'),
        ]
        for l in live:
            tests.append({
                'test_id': l[0], 'test_type': l[1],
                'arm': l[2], 'safety': l[3], 'trigger': l[4],
                'expected': l[5], 'actual': l[5], 'pass': 1
            })

        df = pd.DataFrame(tests)

    # Analyze results
    total_tests = len(df)
    passed_tests = df['pass'].sum()
    failed_tests = total_tests - passed_tests
    pass_rate = passed_tests / total_tests * 100

    print("\nTest Results Summary:")
    print("-" * 70)
    print(f"Total tests:    {total_tests}")
    print(f"Passed:         {passed_tests}")
    print(f"Failed:         {failed_tests}")
    print(f"Pass rate:      {pass_rate:.1f}%")

    # Results by category
    print("\nResults by Category:")
    print("-" * 70)
    for test_type in df['test_type'].unique():
        subset = df[df['test_type'] == test_type]
        cat_pass = subset['pass'].sum()
        cat_total = len(subset)
        print(f"  {test_type.capitalize():<15} {cat_pass}/{cat_total} "
              f"({'PASS' if cat_pass == cat_total else 'FAIL'})")

    # List any failures
    failures = df[df['pass'] == 0]
    if len(failures) > 0:
        print("\n⚠️  FAILED TESTS:")
        print("-" * 70)
        for _, row in failures.iterrows():
            print(f"  {row['test_id']}: Expected {row['expected']}, "
                  f"Got {row['actual']}")
    else:
        print("\n✓ ALL TESTS PASSED")

    # Overall verdict
    print("\n" + "=" * 70)
    if pass_rate == 100:
        print("  SAFETY INTERLOCK VALIDATION: ✓ PASSED")
        print("  System is safe to proceed with prototype testing")
    else:
        print("  SAFETY INTERLOCK VALIDATION: ✗ FAILED")
        print("  DO NOT PROCEED - Fix failures before testing")
    print("=" * 70)

    # Save results
    ensure_output_dir()
    results_file = f"{OUTPUT_DIR}/exp3_safety_results_{timestamp()}.csv"
    df.to_csv(results_file, index=False)
    print(f"\nResults saved: {results_file}")

    return {
        'results_df': df,
        'total_tests': total_tests,
        'passed': passed_tests,
        'failed': failed_tests,
        'pass_rate': pass_rate,
        'validated': pass_rate == 100
    }

# ═══════════════════════════════════════════════════════════════════════════
# EXPERIMENT 4: PROJECTILE STABILITY
# ═══════════════════════════════════════════════════════════════════════════

def analyze_projectile_stability(data_file=None):
    """
    Analyze projectile stability test results.

    Expected CSV format:
        fin_set, shot, frames_5m, rotations_5m, stability_score
        A, 1, 42, 3.5, 3
        A, 2, 41, 3.4, 3
        ...
    """
    print_header("EXPERIMENT 4: PROJECTILE STABILITY")

    if data_file and os.path.exists(data_file):
        df = pd.read_csv(data_file)
        print(f"Loaded data from: {data_file}")
    else:
        print("Using sample data")
        # Sample data: 3 fin sets, 4 shots each
        data = []
        # Fin Set A: 15° cant - high spin, good stability
        for i in range(1, 5):
            data.append({'fin_set': 'A', 'shot': i, 'frames_5m': 40 + np.random.randint(-2, 3),
                        'rotations_5m': 3.5 + np.random.uniform(-0.3, 0.3), 'stability_score': 3})
        # Fin Set B: 10° cant - medium spin, good stability
        for i in range(1, 5):
            data.append({'fin_set': 'B', 'shot': i, 'frames_5m': 41 + np.random.randint(-2, 3),
                        'rotations_5m': 2.3 + np.random.uniform(-0.2, 0.2), 'stability_score': 3})
        # Fin Set C: 0° straight - no spin, some wobble
        for i in range(1, 5):
            score = np.random.choice([2, 2, 2, 3])  # Mostly slight wobble
            data.append({'fin_set': 'C', 'shot': i, 'frames_5m': 42 + np.random.randint(-2, 3),
                        'rotations_5m': 0.1 + np.random.uniform(-0.1, 0.1), 'stability_score': score})
        df = pd.DataFrame(data)

    # Camera settings (assumed)
    FPS = 240

    # Calculate derived values
    df['velocity_ms'] = 5.0 / (df['frames_5m'] / FPS)
    df['spin_rpm'] = df['rotations_5m'] * FPS * 60 / df['frames_5m']

    # Aggregate by fin set
    results = []
    for fin_set in df['fin_set'].unique():
        subset = df[df['fin_set'] == fin_set]
        results.append({
            'fin_set': fin_set,
            'n_shots': len(subset),
            'avg_velocity': subset['velocity_ms'].mean(),
            'std_velocity': subset['velocity_ms'].std(),
            'avg_spin_rpm': subset['spin_rpm'].mean(),
            'std_spin_rpm': subset['spin_rpm'].std(),
            'stability_score': subset['stability_score'].sum(),
            'max_score': len(subset) * 3,
            'score_pct': subset['stability_score'].sum() / (len(subset) * 3) * 100
        })

    results_df = pd.DataFrame(results)

    # Print results
    print("\nResults by Fin Set:")
    print("-" * 80)
    print(f"{'Fin Set':<10} {'Velocity':<15} {'Spin (RPM)':<15} {'Score':<12} {'%':<8}")
    print("-" * 80)
    for _, row in results_df.iterrows():
        print(f"{row['fin_set']:<10} {row['avg_velocity']:.1f}±{row['std_velocity']:.1f} m/s   "
              f"{row['avg_spin_rpm']:.0f}±{row['std_spin_rpm']:.0f}        "
              f"{row['stability_score']:.0f}/{row['max_score']:.0f}      {row['score_pct']:.0f}%")

    # Determine best fin set
    best_idx = results_df['score_pct'].idxmax()
    best_fin = results_df.loc[best_idx, 'fin_set']

    print(f"\nRecommended fin set: {best_fin}")
    print(f"  Stability score: {results_df.loc[best_idx, 'score_pct']:.0f}%")
    print(f"  Spin rate: {results_df.loc[best_idx, 'avg_spin_rpm']:.0f} RPM")

    # Stability criteria
    print("\nStability Scoring:")
    print("  3 = STABLE (no visible wobble)")
    print("  2 = SLIGHT WOBBLE (<10° deviation)")
    print("  1 = MODERATE WOBBLE (10-30°)")
    print("  0 = TUMBLE (>30° or flip)")

    # VDC-100 scaling
    print("\n" + "-" * 70)
    print("SCALING TO VDC-100:")
    print("-" * 70)
    print(f"Selected fin configuration: {best_fin}")
    print("Scale fin dimensions by 3.1× for VDC-100")
    print("Maintain same cant angle for similar spin characteristics")

    # Plot
    ensure_output_dir()
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Velocity comparison
    fin_sets = results_df['fin_set'].values
    ax1 = axes[0]
    ax1.bar(fin_sets, results_df['avg_velocity'],
            yerr=results_df['std_velocity'], capsize=5, alpha=0.7)
    ax1.set_xlabel('Fin Set', fontsize=12)
    ax1.set_ylabel('Velocity (m/s)', fontsize=12)
    ax1.set_title('Velocity by Fin Set', fontsize=14)
    ax1.grid(True, alpha=0.3)

    # Spin rate comparison
    ax2 = axes[1]
    ax2.bar(fin_sets, results_df['avg_spin_rpm'],
            yerr=results_df['std_spin_rpm'], capsize=5, alpha=0.7, color='orange')
    ax2.set_xlabel('Fin Set', fontsize=12)
    ax2.set_ylabel('Spin Rate (RPM)', fontsize=12)
    ax2.set_title('Spin Rate by Fin Set', fontsize=14)
    ax2.grid(True, alpha=0.3)

    # Stability score
    ax3 = axes[2]
    colors = ['green' if s >= 90 else 'yellow' if s >= 75 else 'red'
              for s in results_df['score_pct']]
    ax3.bar(fin_sets, results_df['score_pct'], color=colors, alpha=0.7)
    ax3.axhline(75, color='orange', linestyle='--', label='Minimum acceptable')
    ax3.set_xlabel('Fin Set', fontsize=12)
    ax3.set_ylabel('Stability Score (%)', fontsize=12)
    ax3.set_title('Stability Score by Fin Set', fontsize=14)
    ax3.set_ylim(0, 105)
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    filename = f"{OUTPUT_DIR}/exp4_stability_{timestamp()}.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"\nPlot saved: {filename}")
    plt.close()

    return {
        'results_df': results_df,
        'raw_data': df,
        'best_fin_set': best_fin,
        'best_score_pct': results_df.loc[best_idx, 'score_pct']
    }

# ═══════════════════════════════════════════════════════════════════════════
# EXPERIMENT 5: RECOIL CHARACTERIZATION
# ═══════════════════════════════════════════════════════════════════════════

def analyze_recoil(data_file=None):
    """
    Analyze recoil measurement data.

    Expected CSV format:
        pressure_bar, shot, peak_force_kg, duration_ms
        60, 1, 3.2, 35
        60, 2, 3.1, 36
        ...
    """
    print_header("EXPERIMENT 5: RECOIL CHARACTERIZATION")

    if data_file and os.path.exists(data_file):
        df = pd.read_csv(data_file)
        print(f"Loaded data from: {data_file}")
    else:
        print("Using sample data")
        data = []
        for pressure in [60, 80, 100]:
            for shot in range(1, 6):
                # Approximate physics-based values
                base_force = 2.5 + (pressure - 60) * 0.03
                force = base_force + np.random.uniform(-0.2, 0.2)
                duration = 30 + np.random.randint(-3, 4)
                data.append({
                    'pressure_bar': pressure,
                    'shot': shot,
                    'peak_force_kg': force,
                    'duration_ms': duration
                })
        df = pd.DataFrame(data)

    # Calculate derived values
    df['peak_force_n'] = df['peak_force_kg'] * 9.81
    df['impulse_ns'] = 0.5 * df['peak_force_n'] * (df['duration_ms'] / 1000)  # Triangular pulse

    # Aggregate by pressure
    results = []
    for pressure in df['pressure_bar'].unique():
        subset = df[df['pressure_bar'] == pressure]
        results.append({
            'pressure_bar': pressure,
            'avg_force_n': subset['peak_force_n'].mean(),
            'std_force_n': subset['peak_force_n'].std(),
            'avg_duration_ms': subset['duration_ms'].mean(),
            'avg_impulse_ns': subset['impulse_ns'].mean(),
            'std_impulse_ns': subset['impulse_ns'].std()
        })

    results_df = pd.DataFrame(results)

    # Print results
    print("\nResults by Pressure:")
    print("-" * 70)
    print(f"{'Pressure':<12} {'Peak Force':<18} {'Duration':<12} {'Impulse':<15}")
    print("-" * 70)
    for _, row in results_df.iterrows():
        print(f"{row['pressure_bar']:<12.0f} {row['avg_force_n']:.1f}±{row['std_force_n']:.1f} N      "
              f"{row['avg_duration_ms']:.0f} ms       {row['avg_impulse_ns']:.2f}±{row['std_impulse_ns']:.2f} Ns")

    # VDC-100 scaling
    print("\n" + "-" * 70)
    print("SCALING TO VDC-100:")
    print("-" * 70)

    # At 100 bar (operating pressure)
    vdc33_impulse = results_df[results_df['pressure_bar'] == 100]['avg_impulse_ns'].values[0]
    vdc100_impulse = vdc33_impulse * MASS_RATIO  # Scales with projectile mass

    print(f"VDC-33 impulse at 100 bar: {vdc33_impulse:.2f} Ns")
    print(f"VDC-100 predicted impulse: {vdc100_impulse:.2f} Ns")
    print(f"VDC-100 requirement: ≤15 Ns")

    if vdc100_impulse <= 15:
        print(f"\n✓ PASS: Predicted impulse {vdc100_impulse:.1f} Ns ≤ 15 Ns")
        margin = (15 - vdc100_impulse) / 15 * 100
        print(f"  Margin: {margin:.0f}%")
    else:
        print(f"\n✗ FAIL: Predicted impulse {vdc100_impulse:.1f} Ns > 15 Ns")
        print("  Action: Add recoil buffer or reduce operating pressure")

    # Plot
    ensure_output_dir()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Force vs Pressure
    ax1.errorbar(results_df['pressure_bar'], results_df['avg_force_n'],
                yerr=results_df['std_force_n'], fmt='o-', markersize=8, capsize=5)
    ax1.set_xlabel('Pressure (bar)', fontsize=12)
    ax1.set_ylabel('Peak Force (N)', fontsize=12)
    ax1.set_title('Peak Recoil Force vs Pressure', fontsize=14)
    ax1.grid(True, alpha=0.3)

    # Impulse with VDC-100 scaling
    ax2.bar(results_df['pressure_bar'] - 2, results_df['avg_impulse_ns'],
            width=4, label='VDC-33', alpha=0.7)
    ax2.bar(results_df['pressure_bar'] + 2, results_df['avg_impulse_ns'] * MASS_RATIO,
            width=4, label='VDC-100 (scaled)', alpha=0.7, color='orange')
    ax2.axhline(15, color='r', linestyle='--', label='VDC-100 limit (15 Ns)')
    ax2.set_xlabel('Pressure (bar)', fontsize=12)
    ax2.set_ylabel('Impulse (Ns)', fontsize=12)
    ax2.set_title('Recoil Impulse Comparison', fontsize=14)
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    filename = f"{OUTPUT_DIR}/exp5_recoil_{timestamp()}.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"\nPlot saved: {filename}")
    plt.close()

    return {
        'results_df': results_df,
        'raw_data': df,
        'vdc33_impulse_100bar': vdc33_impulse,
        'vdc100_predicted_impulse': vdc100_impulse,
        'requirement_met': vdc100_impulse <= 15
    }

# ═══════════════════════════════════════════════════════════════════════════
# EXPERIMENT 6: GAS CONSUMPTION
# ═══════════════════════════════════════════════════════════════════════════

def analyze_gas_consumption(data_file=None):
    """
    Analyze gas consumption data.

    Expected CSV format:
        dwell_ms, p_start, p_end, shots
        8, 200, 188, 10
        12, 188, 174, 10
        ...
    """
    print_header("EXPERIMENT 6: GAS CONSUMPTION")

    if data_file and os.path.exists(data_file):
        df = pd.read_csv(data_file)
        print(f"Loaded data from: {data_file}")
    else:
        print("Using sample data")
        df = pd.DataFrame({
            'dwell_ms': [8, 12, 15],
            'p_start': [200, 188, 174],
            'p_end': [188, 174, 158],
            'shots': [10, 10, 10]
        })

    # Calculate gas consumption
    df['delta_p'] = df['p_start'] - df['p_end']
    df['gas_per_shot'] = df['delta_p'] / df['shots']

    # Print results
    print("\nResults:")
    print("-" * 60)
    print(f"{'Dwell(ms)':<12} {'ΔP (bar)':<12} {'Gas/shot':<15}")
    print("-" * 60)
    for _, row in df.iterrows():
        print(f"{row['dwell_ms']:<12.0f} {row['delta_p']:<12.0f} {row['gas_per_shot']:.2f} bar/shot")

    # Calculate shots per fill for VDC-33
    vdc33_tank_volume = 0.8  # L (48ci)
    vdc33_full_pressure = 200  # bar (typical fill)
    vdc33_min_pressure = 80  # bar (regulator cutoff)
    vdc33_usable_range = vdc33_full_pressure - vdc33_min_pressure  # 120 bar

    # Use optimal dwell (12ms from Exp 2)
    optimal_gas_per_shot = df[df['dwell_ms'] == 12]['gas_per_shot'].values[0]
    vdc33_shots_per_fill = vdc33_usable_range / optimal_gas_per_shot

    print(f"\nVDC-33 Performance:")
    print(f"  Tank: {vdc33_tank_volume}L @ {vdc33_full_pressure} bar")
    print(f"  Usable range: {vdc33_usable_range} bar")
    print(f"  Gas per shot (12ms dwell): {optimal_gas_per_shot:.2f} bar")
    print(f"  Shots per fill: {vdc33_shots_per_fill:.0f}")

    # VDC-100 scaling
    print("\n" + "-" * 70)
    print("SCALING TO VDC-100:")
    print("-" * 70)

    vdc100_tank_volume = 0.5  # L
    vdc100_full_pressure = 300  # bar
    vdc100_min_pressure = 120  # bar
    vdc100_usable_range = vdc100_full_pressure - vdc100_min_pressure  # 180 bar

    # Gas consumption scales with bore area (more volume to fill)
    vdc100_gas_per_shot = optimal_gas_per_shot * AREA_RATIO
    vdc100_shots_per_fill = vdc100_usable_range / vdc100_gas_per_shot

    print(f"  Tank: {vdc100_tank_volume}L @ {vdc100_full_pressure} bar")
    print(f"  Usable range: {vdc100_usable_range} bar")
    print(f"  Predicted gas per shot: {vdc100_gas_per_shot:.1f} bar")
    print(f"  Predicted shots per fill: {vdc100_shots_per_fill:.1f}")
    print(f"  Requirement: ≥5 shots per fill")

    if vdc100_shots_per_fill >= 5:
        print(f"\n✓ PASS: {vdc100_shots_per_fill:.0f} shots ≥ 5 shots")
    else:
        print(f"\n✗ FAIL: {vdc100_shots_per_fill:.1f} shots < 5 shots")
        print("  Action: Increase tank size or optimize dwell time")

    # Plot
    ensure_output_dir()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Gas per shot vs dwell
    ax1.bar(df['dwell_ms'], df['gas_per_shot'], width=2, alpha=0.7)
    ax1.set_xlabel('Dwell Time (ms)', fontsize=12)
    ax1.set_ylabel('Gas per Shot (bar)', fontsize=12)
    ax1.set_title('Gas Consumption vs Dwell Time', fontsize=14)
    ax1.grid(True, alpha=0.3)

    # Shots per fill comparison
    categories = ['VDC-33', 'VDC-100\n(predicted)']
    shots = [vdc33_shots_per_fill, vdc100_shots_per_fill]
    colors = ['blue', 'orange']
    ax2.bar(categories, shots, color=colors, alpha=0.7)
    ax2.axhline(5, color='r', linestyle='--', label='VDC-100 minimum (5)')
    ax2.set_ylabel('Shots per Fill', fontsize=12)
    ax2.set_title('Shots per Fill Comparison', fontsize=14)
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    filename = f"{OUTPUT_DIR}/exp6_gas_consumption_{timestamp()}.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"\nPlot saved: {filename}")
    plt.close()

    return {
        'results_df': df,
        'vdc33_shots_per_fill': vdc33_shots_per_fill,
        'vdc100_predicted_shots': vdc100_shots_per_fill,
        'requirement_met': vdc100_shots_per_fill >= 5
    }

# ═══════════════════════════════════════════════════════════════════════════
# MAIN ANALYSIS RUNNER
# ═══════════════════════════════════════════════════════════════════════════

def run_all_analyses(data_dir=None):
    """Run all experiment analyses."""
    print("\n" + "═" * 70)
    print("       VDC-33 PROTOTYPE - COMPLETE DATA ANALYSIS")
    print("═" * 70)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    results = {}

    # Run each experiment analysis
    if data_dir:
        results['exp1'] = analyze_velocity_pressure(f"{data_dir}/exp1_velocity_pressure.csv")
        results['exp2'] = analyze_valve_timing(f"{data_dir}/exp2_valve_timing.csv")
        results['exp3'] = analyze_safety_validation(f"{data_dir}/exp3_safety.csv")
        results['exp4'] = analyze_projectile_stability(f"{data_dir}/exp4_stability.csv")
        results['exp5'] = analyze_recoil(f"{data_dir}/exp5_recoil.csv")
        results['exp6'] = analyze_gas_consumption(f"{data_dir}/exp6_gas.csv")
    else:
        # Run with sample data
        results['exp1'] = analyze_velocity_pressure()
        results['exp2'] = analyze_valve_timing()
        results['exp3'] = analyze_safety_validation()
        results['exp4'] = analyze_projectile_stability()
        results['exp5'] = analyze_recoil()
        results['exp6'] = analyze_gas_consumption()

    # Summary
    print_header("ANALYSIS SUMMARY")

    print("Experiment Results:")
    print("-" * 70)

    if results['exp1']['fit_params']['a']:
        print(f"  1. Velocity: Optimal pressure = {results['exp1']['optimal_pressure']:.0f} bar")

    print(f"  2. Timing: Optimal dwell = {results['exp2']['optimal_dwell_ms']:.0f} ms")
    print(f"            VDC-100 estimated = {results['exp2']['vdc100_estimated_dwell']:.0f} ms")

    print(f"  3. Safety: {'✓ VALIDATED' if results['exp3']['validated'] else '✗ FAILED'} "
          f"({results['exp3']['pass_rate']:.0f}%)")

    print(f"  4. Stability: Best fin set = {results['exp4']['best_fin_set']} "
          f"({results['exp4']['best_score_pct']:.0f}%)")

    print(f"  5. Recoil: VDC-100 = {results['exp5']['vdc100_predicted_impulse']:.1f} Ns "
          f"({'✓ PASS' if results['exp5']['requirement_met'] else '✗ FAIL'})")

    print(f"  6. Gas: VDC-100 = {results['exp6']['vdc100_predicted_shots']:.0f} shots/fill "
          f"({'✓ PASS' if results['exp6']['requirement_met'] else '✗ FAIL'})")

    # Overall readiness
    print("\n" + "=" * 70)
    all_pass = (results['exp3']['validated'] and
                results['exp5']['requirement_met'] and
                results['exp6']['requirement_met'])

    if all_pass:
        print("  VDC-33 PROTOTYPE VALIDATION: ✓ READY FOR PHASE 4")
        print("  All critical requirements met")
    else:
        print("  VDC-33 PROTOTYPE VALIDATION: ✗ ISSUES FOUND")
        print("  Review failed experiments before proceeding")
    print("=" * 70 + "\n")

    return results

# ═══════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        # Run with data directory
        run_all_analyses(sys.argv[1])
    else:
        # Run with sample data
        run_all_analyses()
