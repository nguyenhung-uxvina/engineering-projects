#!/usr/bin/env python3
"""
Stock Growth Projector
Projects stock levels over time based on inflow and outflow rates.
"""

import argparse
import sys


def project_stock(initial_stock, inflow_rate, outflow_rate, periods):
    """Project stock levels over time."""
    
    stock_history = [initial_stock]
    inflow_history = []
    outflow_history = []
    net_flow_history = []
    
    current_stock = initial_stock
    
    for period in range(periods):
        # Calculate flows
        inflow = inflow_rate
        outflow = outflow_rate
        net_flow = inflow - outflow
        
        # Update stock (prevent negative)
        current_stock = max(0, current_stock + net_flow)
        
        # Record
        stock_history.append(current_stock)
        inflow_history.append(inflow)
        outflow_history.append(outflow)
        net_flow_history.append(net_flow)
    
    # Analyze pattern
    final_stock = stock_history[-1]
    total_change = final_stock - initial_stock
    percent_change = (total_change / initial_stock * 100) if initial_stock > 0 else float('inf')
    
    # Determine pattern
    if net_flow_history[0] > 0:
        pattern = "GROWTH"
        risk = "Accumulation" if outflow_rate < inflow_rate else "Balanced"
    elif net_flow_history[0] < 0:
        pattern = "DEPLETION"
        # Calculate when stock hits zero
        periods_to_zero = initial_stock / abs(outflow_rate - inflow_rate) if (outflow_rate > inflow_rate) else float('inf')
        risk = f"Crisis in {periods_to_zero:.1f} periods" if periods_to_zero < float('inf') else "Stable"
    else:
        pattern = "EQUILIBRIUM"
        risk = "Stable"
    
    return {
        "initial_stock": initial_stock,
        "final_stock": final_stock,
        "total_change": total_change,
        "percent_change": percent_change,
        "inflow_rate": inflow_rate,
        "outflow_rate": outflow_rate,
        "net_flow": inflow_rate - outflow_rate,
        "periods": periods,
        "pattern": pattern,
        "risk": risk,
        "stock_history": stock_history,
        "inflow_history": inflow_history,
        "outflow_history": outflow_history,
        "net_flow_history": net_flow_history
    }


def print_report(results):
    """Print formatted projection report."""
    
    print("\n" + "="*60)
    print("STOCK PROJECTION ANALYSIS")
    print("="*60)
    
    print(f"\nInitial Conditions:")
    print(f"  Starting Stock: {results['initial_stock']:.1f} units")
    print(f"  Inflow Rate: {results['inflow_rate']:.1f} units/period")
    print(f"  Outflow Rate: {results['outflow_rate']:.1f} units/period")
    print(f"  Net Flow: {results['net_flow']:+.1f} units/period")
    print(f"  Projection: {results['periods']} periods")
    
    print(f"\nResults:")
    print(f"  Final Stock: {results['final_stock']:.1f} units")
    print(f"  Total Change: {results['total_change']:+.1f} units ({results['percent_change']:+.1f}%)")
    
    print(f"\n" + "-"*60)
    print(f"PATTERN: {results['pattern']}")
    print(f"RISK: {results['risk']}")
    print("-"*60)
    
    # Visualization
    print(f"\nStock Level Progression:")
    print(f"  Period    Stock    Inflow   Outflow   Net")
    print(f"  " + "-"*50)
    print(f"     0    {results['initial_stock']:6.1f}       -        -        -")
    
    for i in range(min(10, results['periods'])):
        period = i + 1
        stock = results['stock_history'][period]
        inflow = results['inflow_history'][i]
        outflow = results['outflow_history'][i]
        net = results['net_flow_history'][i]
        print(f"  {period:4d}    {stock:6.1f}    {inflow:6.1f}   {outflow:6.1f}   {net:+6.1f}")
    
    if results['periods'] > 10:
        print(f"  ...")
        period = results['periods']
        stock = results['stock_history'][period]
        inflow = results['inflow_history'][-1]
        outflow = results['outflow_history'][-1]
        net = results['net_flow_history'][-1]
        print(f"  {period:4d}    {stock:6.1f}    {inflow:6.1f}   {outflow:6.1f}   {net:+6.1f}")
    
    # Recommendations
    print("\nANALYSIS:")
    
    if results['pattern'] == "GROWTH":
        if results['net_flow'] > 0:
            print(f"  • Stock is accumulating at {results['net_flow']:.1f} units/period")
            if results['inflow_rate'] > results['outflow_rate'] * 2:
                print(f"  ⚠ Rapid accumulation - consider if this is desirable")
            else:
                print(f"  • Growth rate appears sustainable")
    
    elif results['pattern'] == "DEPLETION":
        if results['net_flow'] < 0:
            print(f"  ⚠ Stock is depleting at {abs(results['net_flow']):.1f} units/period")
            if "Crisis" in results['risk']:
                print(f"  ⚠️ {results['risk']} - URGENT ACTION REQUIRED")
            print(f"  • Options: Increase inflow OR decrease outflow")
    
    else:  # EQUILIBRIUM
        print(f"  ✓ System in equilibrium")
        print(f"  • Stock level stable at {results['final_stock']:.1f} units")
        print(f"  • Monitor for changes in flow rates")
    
    print("\nRECOMMENDATIONS:")
    
    if results['pattern'] == "GROWTH" and results['net_flow'] > results['inflow_rate'] * 0.5:
        print(f"  • Review if growth is intentional")
        print(f"  • Consider if increased outflow needed")
        print(f"  • Monitor for constraint formation")
    
    elif results['pattern'] == "DEPLETION" and "Crisis" in results['risk']:
        print(f"  • IMMEDIATE: Increase inflow rate")
        print(f"  • OR reduce outflow rate")
        print(f"  • Calculate minimum viable stock level")
        print(f"  • Set up early warning system")
    
    elif results['pattern'] == "EQUILIBRIUM":
        print(f"  • Maintain current flow balance")
        print(f"  • Monitor for external disruptions")
        print(f"  • Verify equilibrium at desired level")
    
    print("\nSTOCK-FLOW INSIGHTS:")
    print(f"  • This is a {results['pattern'].lower()} pattern")
    print(f"  • Net flow: {results['net_flow']:+.1f} units/period")
    print(f"  • Change rate: {results['percent_change']/results['periods']:.1f}% per period")
    
    print("\n" + "="*60 + "\n")


def interactive_mode():
    """Run interactive stock projector."""
    print("\n" + "="*60)
    print("STOCK PROJECTOR - Interactive Mode")
    print("="*60 + "\n")
    
    try:
        initial_stock = float(input("Initial stock level (units): "))
        inflow_rate = float(input("Inflow rate (units/period): "))
        outflow_rate = float(input("Outflow rate (units/period): "))
        periods = int(input("Number of periods to project: "))
        
        results = project_stock(initial_stock, inflow_rate, outflow_rate, periods)
        print_report(results)
        
    except ValueError:
        print("Error: Please enter numeric values")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nProjection cancelled")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Project stock levels over time based on flow rates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Project technical debt growth
  python stock_projector.py --initial-stock 100 --inflow-rate 20 --outflow-rate 15 --periods 12
  
  # Project inventory depletion
  python stock_projector.py --initial-stock 1000 --inflow-rate 30 --outflow-rate 50 --periods 24
  
  # Interactive mode
  python stock_projector.py
  
Theory:
  Inflow > Outflow = Growth
  Outflow > Inflow = Depletion  
  Inflow = Outflow = Equilibrium
  
Stock = Accumulation of (Inflows - Outflows) over time
        """
    )
    
    parser.add_argument('--initial-stock', type=float,
                       help='Initial stock level (units)')
    parser.add_argument('--inflow-rate', type=float,
                       help='Inflow rate (units/period)')
    parser.add_argument('--outflow-rate', type=float,
                       help='Outflow rate (units/period)')
    parser.add_argument('--periods', type=int,
                       help='Number of periods to project')
    
    args = parser.parse_args()
    
    # Interactive mode if no args
    if not any([args.initial_stock, args.inflow_rate, args.outflow_rate, args.periods]):
        interactive_mode()
        return
    
    # Validate required args
    if not all([args.initial_stock, args.inflow_rate, args.outflow_rate, args.periods]):
        print("Error: All four arguments required in non-interactive mode")
        parser.print_help()
        sys.exit(1)
    
    # Calculate and report
    results = project_stock(
        args.initial_stock,
        args.inflow_rate,
        args.outflow_rate,
        args.periods
    )
    print_report(results)


if __name__ == "__main__":
    main()
