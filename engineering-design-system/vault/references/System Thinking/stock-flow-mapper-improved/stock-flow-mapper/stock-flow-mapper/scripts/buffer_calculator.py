#!/usr/bin/env python3
"""
Buffer Calculator
Analyzes stock-to-flow ratios to determine optimal buffer sizes.
"""

import argparse
import sys


def calculate_buffer(stock_level, avg_flow, flow_variation):
    """Calculate buffer metrics and recommendations."""
    
    # Stock-to-flow ratio (days of coverage)
    buffer_ratio = stock_level / avg_flow if avg_flow > 0 else 0
    
    # Variation range
    min_flow = avg_flow - flow_variation
    max_flow = avg_flow + flow_variation
    variation_range = max_flow - min_flow
    
    # Optimal buffer range (50-75% of variation)
    optimal_min = avg_flow * (variation_range * 0.5)
    optimal_max = avg_flow * (variation_range * 0.75)
    
    # Classification
    if stock_level < optimal_min:
        status = "UNDERSIZED"
        risk = "HIGH - Frequent stockouts expected"
    elif stock_level > optimal_max:
        status = "OVERSIZED"
        risk = "MEDIUM - Slow response, waste"
    else:
        status = "OPTIMAL"
        risk = "LOW - Absorbs normal variation"
    
    return {
        "buffer_ratio": buffer_ratio,
        "buffer_days": buffer_ratio,
        "min_flow": min_flow,
        "max_flow": max_flow,
        "variation_range": variation_range,
        "optimal_min": optimal_min,
        "optimal_max": optimal_max,
        "status": status,
        "risk": risk,
        "current_stock": stock_level,
        "avg_flow": avg_flow
    }


def print_report(results):
    """Print formatted buffer analysis report."""
    
    print("\n" + "="*60)
    print("BUFFER ANALYSIS REPORT")
    print("="*60)
    
    print(f"\nCurrent Stock Level: {results['current_stock']:.1f} units")
    print(f"Average Flow Rate: {results['avg_flow']:.1f} units/period")
    print(f"Flow Variation: ±{results['variation_range']/2:.1f} units/period")
    
    print(f"\nBuffer Ratio: {results['buffer_ratio']:.2f} periods")
    print(f"  (Stock can cover {results['buffer_days']:.1f} periods at avg flow)")
    
    print(f"\nFlow Range:")
    print(f"  Min: {results['min_flow']:.1f} units/period")
    print(f"  Max: {results['max_flow']:.1f} units/period")
    print(f"  Range: {results['variation_range']:.1f} units/period")
    
    print(f"\nOptimal Buffer Range:")
    print(f"  Minimum: {results['optimal_min']:.1f} units")
    print(f"  Maximum: {results['optimal_max']:.1f} units")
    
    print(f"\n" + "-"*60)
    print(f"BUFFER STATUS: {results['status']}")
    print(f"RISK LEVEL: {results['risk']}")
    print("-"*60)
    
    # Recommendations
    print("\nRECOMMENDATIONS:")
    if results['status'] == "UNDERSIZED":
        increase = results['optimal_min'] - results['current_stock']
        print(f"  • Increase buffer by {increase:.1f} units (to {results['optimal_min']:.1f})")
        print(f"  • OR reduce flow variation")
        print(f"  • Current risk: Frequent stockouts, system fragility")
        
    elif results['status'] == "OVERSIZED":
        decrease = results['current_stock'] - results['optimal_max']
        print(f"  • Reduce buffer by {decrease:.1f} units (to {results['optimal_max']:.1f})")
        print(f"  • OR accept slower response time for stability")
        print(f"  • Current risk: Waste, slow adaptation")
        
    else:
        print(f"  • Buffer is optimally sized")
        print(f"  • Continue monitoring flow variations")
        print(f"  • Adjust if patterns change")
    
    print("\n" + "="*60 + "\n")


def interactive_mode():
    """Run interactive buffer calculator."""
    print("\n" + "="*60)
    print("BUFFER CALCULATOR - Interactive Mode")
    print("="*60 + "\n")
    
    try:
        stock_level = float(input("Current stock level (units): "))
        avg_flow = float(input("Average flow rate (units/period): "))
        flow_variation = float(input("Flow variation (±units/period): "))
        
        results = calculate_buffer(stock_level, avg_flow, flow_variation)
        print_report(results)
        
    except ValueError:
        print("Error: Please enter numeric values")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nCalculation cancelled")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate optimal buffer sizes for stock-flow systems",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Inventory analysis
  python buffer_calculator.py --stock-level 1000 --avg-flow 50 --flow-variation 20
  
  # Interactive mode
  python buffer_calculator.py
  
Theory:
  Buffer = Stock Level / Average Flow Rate
  Optimal = 50-75% of variation range
  Too small = Fragility, oscillation
  Too large = Rigidity, waste
        """
    )
    
    parser.add_argument('--stock-level', type=float,
                       help='Current stock level (units)')
    parser.add_argument('--avg-flow', type=float,
                       help='Average flow rate (units/period)')
    parser.add_argument('--flow-variation', type=float,
                       help='Flow variation (±units/period)')
    
    args = parser.parse_args()
    
    # Interactive mode if no args
    if not any([args.stock_level, args.avg_flow, args.flow_variation]):
        interactive_mode()
        return
    
    # Validate all required args present
    if not all([args.stock_level, args.avg_flow, args.flow_variation]):
        print("Error: All three arguments required in non-interactive mode")
        parser.print_help()
        sys.exit(1)
    
    # Calculate and report
    results = calculate_buffer(args.stock_level, args.avg_flow, args.flow_variation)
    print_report(results)


if __name__ == "__main__":
    main()
