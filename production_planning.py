"""
Production Fixed Horizon Planning - Wagner-Whitin Algorithm

This script implements the Wagner-Whitin algorithm for optimal
production planning to minimize setup and holding costs.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def wagner_whitin(demand, setup_cost, holding_cost):
    """
    Implement Wagner-Whitin algorithm for production planning.

    Parameters:
    - demand: list of demand values for each period
    - setup_cost: fixed cost per production setup
    - holding_cost: cost to hold one unit for one period

    Returns:
    - optimal_cost: minimum total cost
    - production_plan: list of production quantities per period
    """
    n = len(demand)

    # Initialize cost matrix
    # cost[i][j] = cost of producing in period i to satisfy demand from i to j
    cost = np.full((n, n), np.inf)

    for i in range(n):
        cumulative_holding = 0
        for j in range(i, n):
            if i == j:
                cost[i][j] = setup_cost
            else:
                # Holding cost for demand[j] stored from period i to j
                periods_held = j - i
                cumulative_holding += demand[j] * periods_held * holding_cost
                cost[i][j] = setup_cost + cumulative_holding

    # Dynamic programming to find optimal solution
    # f[j] = minimum cost to satisfy demand from period 0 to j
    f = np.zeros(n)
    last_production = np.zeros(n, dtype=int)  # Track where production occurs

    for j in range(n):
        f[j] = cost[0][j]
        last_production[j] = 0

        for i in range(1, j + 1):
            candidate_cost = f[i - 1] + cost[i][j]
            if candidate_cost < f[j]:
                f[j] = candidate_cost
                last_production[j] = i

    # Backtrack to find production plan
    production_plan = np.zeros(n, dtype=int)
    j = n - 1
    while j >= 0:
        prod_period = last_production[j]
        # Production in period prod_period covers demand from prod_period to j
        production_plan[prod_period] = sum(demand[prod_period:j + 1])
        j = prod_period - 1

    return f[n - 1], production_plan


def lot_for_lot(demand, setup_cost, holding_cost):
    """
    Lot-for-Lot policy: produce exactly what's needed each period.
    """
    n = len(demand)
    total_cost = 0
    production_plan = np.zeros(n, dtype=int)

    for i in range(n):
        if demand[i] > 0:
            total_cost += setup_cost
            production_plan[i] = demand[i]

    return total_cost, production_plan


def fixed_order_quantity(demand, setup_cost, holding_cost, eoq=None):
    """
    Fixed Order Quantity policy using EOQ.
    """
    n = len(demand)
    total_demand = sum(demand)

    if eoq is None:
        # Calculate EOQ
        avg_demand = total_demand / n
        eoq = int(np.sqrt(2 * avg_demand * setup_cost / holding_cost))
        eoq = max(eoq, max(demand))  # At least cover largest demand

    production_plan = np.zeros(n, dtype=int)
    inventory = 0
    total_cost = 0
    total_holding = 0

    for i in range(n):
        if inventory < demand[i]:
            # Need to produce
            production_plan[i] = eoq
            inventory += eoq
            total_cost += setup_cost

        inventory -= demand[i]
        total_holding += inventory * holding_cost

    total_cost += total_holding
    return total_cost, production_plan


def display_results(demand, plans, costs, method_names):
    """Display comparison of production planning methods."""
    n = len(demand)
    periods = [f"M{i+1}" for i in range(n)]

    print("=" * 70)
    print("PRODUCTION PLANNING COMPARISON")
    print("=" * 70)

    # Demand
    print(f"\n{'Period':<10}", end="")
    for p in periods:
        print(f"{p:<8}", end="")
    print(f"{'Total':<10}")

    print(f"{'Demand':<10}", end="")
    for d in demand:
        print(f"{d:<8}", end="")
    print(f"{sum(demand):<10}")

    print("-" * 70)

    # Each method
    for name, plan, cost in zip(method_names, plans, costs):
        print(f"\n{name}")
        print(f"{'Production':<10}", end="")
        for p in plan:
            print(f"{p:<8}", end="")
        print(f"{sum(plan):<10}")
        print(f"Total Cost: ${cost:,.2f}")


def plot_production_plan(demand, production_plan, title="Production Plan"):
    """Visualize production plan vs demand."""
    n = len(demand)
    periods = range(1, n + 1)

    fig, ax = plt.subplots(figsize=(12, 6))

    width = 0.35
    x = np.arange(n)

    ax.bar(x - width/2, demand, width, label='Demand', color='steelblue')
    ax.bar(x + width/2, production_plan, width, label='Production', color='orange')

    ax.set_xlabel('Period')
    ax.set_ylabel('Units')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels([f'M{i+1}' for i in range(n)])
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('production_plan.png', dpi=150)
    plt.close()
    print(f"\nVisualization saved to: production_plan.png")


def load_demand(filepath='data/demand_forecasts.csv'):
    """Load demand data from CSV file."""
    df = pd.read_csv(filepath, sep=';')
    return df['forecast'].tolist()


def main():
    """Main function demonstrating production planning."""
    print("=" * 70)
    print("PRODUCTION FIXED HORIZON PLANNING")
    print("Wagner-Whitin Algorithm Implementation")
    print("=" * 70)

    # Load demand from CSV
    demand = load_demand('./data/demand_forecasts.csv')
    # Costs
    setup_cost = 500  # Fixed cost per production run
    holding_cost = 1  # Cost per unit per period

    print(f"\nSetup Cost: ${setup_cost}")
    print(f"Holding Cost: ${holding_cost}/unit/period")

    # Run different methods
    ww_cost, ww_plan = wagner_whitin(demand, setup_cost, holding_cost)
    lfl_cost, lfl_plan = lot_for_lot(demand, setup_cost, holding_cost)
    foq_cost, foq_plan = fixed_order_quantity(demand, setup_cost, holding_cost)

    # Display results
    display_results(
        demand,
        [ww_plan, lfl_plan, foq_plan],
        [ww_cost, lfl_cost, foq_cost],
        ["Wagner-Whitin", "Lot-for-Lot", "Fixed Order Qty"]
    )

    # Cost comparison
    print("\n" + "=" * 70)
    print("COST COMPARISON")
    print("=" * 70)
    print(f"Wagner-Whitin:     ${ww_cost:>10,.2f} (Optimal)")
    print(f"Lot-for-Lot:       ${lfl_cost:>10,.2f} ({(lfl_cost/ww_cost-1)*100:+.1f}%)")
    print(f"Fixed Order Qty:   ${foq_cost:>10,.2f} ({(foq_cost/ww_cost-1)*100:+.1f}%)")

    # Plot Wagner-Whitin solution
    plot_production_plan(demand, ww_plan, "Wagner-Whitin Optimal Production Plan")


if __name__ == "__main__":
    main()
