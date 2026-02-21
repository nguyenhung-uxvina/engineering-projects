#!/usr/bin/env python3
"""
Delay Impact Calculator
Quantifies the impact of delays on system oscillation and stability.
"""

import argparse
import sys
import math


def calculate_delay_impact(current_delay, proposed_delay, flow_rate, cycle_time=None):
    """Calculate impact of delay changes on system behavior."""
    
    # If no cycle time provided, estimate from flow rate
    if cycle_time is None:
        cycle_time = max(current_delay * 2, 30)  # Assume cycle is 2x delay or 30 min
    
    # Delay as percentage of cycle
    current_ratio = (current_delay / cycle_time) * 100
    proposed_ratio = (proposed_delay / cycle_time) * 100
    
    # Oscillation risk (simple heuristic)
    def oscillation_risk(ratio):
        if ratio > 75:
            return "CRITICAL"
        elif ratio > 50:
            return "HIGH"
        elif ratio > 25:
            return "MEDIUM"
        else:
            return "LOW"
    
    current_risk = oscillation_risk(current_ratio)
    proposed_risk = oscillation_risk(proposed_ratio)
    
    # Response time improvement
    response_improvement = ((current_delay - proposed_delay) / current_delay) * 100
    
    # Stability improvement (inverse of delay ratio)
    stability_improvement = current_ratio - proposed_ratio
    
    # Estimated throughput impact (simplified)
    # Shorter delays allow faster iteration
    throughput_gain = (1 - (proposed_delay / current_delay)) * 100 if current_delay > 0 else 0
    
    return {
        "current_delay": current_delay,
        "proposed_delay": proposed_delay,
        "delay_reduction": current_delay - proposed_delay,
        "delay_reduction_pct": response_improvement,
        "flow_rate": flow_rate,
        "cycle_time": cycle_time,
        "current_ratio": current_ratio,
        "proposed_ratio": proposed_ratio,
        "current_risk": current_risk,
        "proposed_risk": proposed_risk,
        "stability_improvement": stability_improvement,
        "throughput_gain": throughput_gain
    }


def print_report(results):
    """Print formatted delay impact report."""
    
    print("\n" + "="*60)
    print("DELAY IMPACT ANALYSIS")
    print("="*60)
    
    print(f"\nCurrent System:")
    print(f"  Delay: {results['current_delay']:.1f} periods")
    print(f"  Cycle Time: {results['cycle_time']:.1f} periods")
    print(f"  Delay/Cycle Ratio: {results['current_ratio']:.1f}%")
    print(f"  Oscillation Risk: {results['current_risk']}")
    
    print(f"\nProposed System:")
    print(f"  Delay: {results['proposed_delay']:.1f} periods")
    print(f"  Delay/Cycle Ratio: {results['proposed_ratio']:.1f}%")
    print(f"  Oscillation Risk: {results['proposed_risk']}")
    
    print(f"\nImprovements:")
    print(f"  Delay Reduction: {results['delay_reduction']:.1f} periods ({results['delay_reduction_pct']:.1f}%)")
    print(f"  Stability Gain: {results['stability_improvement']:.1f} percentage points")
    print(f"  Throughput Gain: ~{results['throughput_gain']:.1f}%")
    
    print(f"\n" + "-"*60)
    print(f"RISK CHANGE: {results['current_risk']} → {results['proposed_risk']}")
    print("-"*60)
    
    # Recommendations
    print("\nANALYSIS:")
    
    if results['proposed_risk'] == "LOW":
        print(f"  ✓ Proposed delay is optimal for system stability")
        print(f"  ✓ Minimal oscillation expected")
    elif results['proposed_risk'] == "MEDIUM":
        print(f"  • Proposed delay is acceptable")
        print(f"  • Some oscillation may occur under stress")
    elif results['proposed_risk'] == "HIGH":
        print(f"  ⚠ Proposed delay still problematic")
        print(f"  ⚠ Consider further reduction or add buffers")
    else:
        print(f"  ⚠️ CRITICAL: Delay dominates cycle time")
        print(f"  ⚠️ System will oscillate wildly")
    
    if results['delay_reduction_pct'] > 50:
        print(f"  ✓ Significant improvement ({results['delay_reduction_pct']:.0f}%)")
    elif results['delay_reduction_pct'] > 25:
        print(f"  • Moderate improvement ({results['delay_reduction_pct']:.0f}%)")
    else:
        print(f"  • Minor improvement - consider larger reduction")
    
    print("\nRECOMMENDATIONS:")
    if results['proposed_ratio'] > 50:
        target_delay = results['cycle_time'] * 0.25
        print(f"  • Target delay: {target_delay:.1f} periods (25% of cycle)")
        print(f"  • This requires {current_delay - target_delay:.1f} period reduction")
    else:
        print(f"  • Proposed delay meets < 50% of cycle guideline")
        print(f"  • Implement and monitor for oscillation")
    
    print(f"\nLEVERAGE POINT: L9 (Delays)")
    print(f"  • Intervention type: Shorten feedback delay")
    print(f"  • Priority: HIGH (delays cause oscillation)")
    print(f"  • Cost: Typically LOW-MEDIUM")
    print(f"  • Impact: HIGH (stability + throughput)")
    
    print("\n" + "="*60 + "\n")


def interactive_mode():
    """Run interactive delay calculator."""
    print("\n" + "="*60)
    print("DELAY IMPACT CALCULATOR - Interactive Mode")
    print("="*60 + "\n")
    
    try:
        current_delay = float(input("Current delay (days/weeks/periods): "))
        proposed_delay = float(input("Proposed delay (same units): "))
        flow_rate = float(input("Flow rate (units/period): "))
        
        cycle_input = input("System cycle time (press Enter to estimate): ").strip()
        cycle_time = float(cycle_input) if cycle_input else None
        
        results = calculate_delay_impact(current_delay, proposed_delay, flow_rate, cycle_time)
        print_report(results)
        
    except ValueError:
        print("Error: Please enter numeric values")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nCalculation cancelled")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate impact of delay reductions on system stability",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze 30-day delay reduced to 5 days
  python delay_impact_calculator.py --current-delay 30 --proposed-delay 5 --flow-rate 10
  
  # With explicit cycle time
  python delay_impact_calculator.py --current-delay 30 --proposed-delay 5 --flow-rate 10 --cycle-time 60
  
  # Interactive mode
  python delay_impact_calculator.py
  
Theory:
  Delay/Cycle Ratio < 25% = Stable (LOW risk)
  Delay/Cycle Ratio < 50% = Acceptable (MEDIUM risk)
  Delay/Cycle Ratio > 50% = Oscillation (HIGH risk)
  Delay/Cycle Ratio > 75% = Wild oscillation (CRITICAL)
  
Leverage Point L9: Shorten delays to improve stability
        """
    )
    
    parser.add_argument('--current-delay', type=float,
                       help='Current delay (days/weeks/periods)')
    parser.add_argument('--proposed-delay', type=float,
                       help='Proposed delay (same units)')
    parser.add_argument('--flow-rate', type=float,
                       help='Flow rate (units/period)')
    parser.add_argument('--cycle-time', type=float,
                       help='System cycle time (optional, will estimate if not provided)')
    
    args = parser.parse_args()
    
    # Interactive mode if no args
    if not any([args.current_delay, args.proposed_delay, args.flow_rate]):
        interactive_mode()
        return
    
    # Validate required args
    if not all([args.current_delay, args.proposed_delay, args.flow_rate]):
        print("Error: --current-delay, --proposed-delay, and --flow-rate required")
        parser.print_help()
        sys.exit(1)
    
    # Calculate and report
    results = calculate_delay_impact(
        args.current_delay,
        args.proposed_delay,
        args.flow_rate,
        args.cycle_time
    )
    print_report(results)


if __name__ == "__main__":
    main()
