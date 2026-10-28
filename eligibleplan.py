
def telecom_cost_optimization():
    print("=" * 55)
    print("   MOBILE PLAN COST OPTIMIZATION SYSTEM")
    print("=" * 55)

    # User requirements
    try:
        data_needed = float(input("Enter required data (GB): "))
        calls_needed = int(input("Enter required call minutes: "))
        validity_needed = int(input("Enter required validity (days): "))
        budget = float(input("Enter your budget (Rs.): "))

        if (data_needed < 0 or calls_needed < 0
                or validity_needed <= 0 or budget < 0):
            print("Error: Enter valid non-negative requirements.")
            return
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    # Plan details:
    # name, price, data GB, call minutes, validity days,
    # extra data charge per GB, extra call charge per minute
    plans = [
        ("Basic", 199, 2, 300, 28, 50, 0.50),
        ("Smart", 299, 10, 600, 28, 30, 0.40),
        ("Premium", 399, 20, 1000, 56, 20, 0.30),
        ("Unlimited", 599, 40, 2000, 84, 10, 0.20)
    ]

    results = []

    print("\nPLAN COMPARISON")
    print("-" * 90)
    print(f"{'Plan':<12}{'Base Price':>12}{'Extra Cost':>13}"
          f"{'Total Cost':>13}{'Eligible':>12}")
    print("-" * 90)

    for plan in plans:
        name, price, data, calls, validity, data_rate, call_rate = plan

        # Calculate excess usage charges
        excess_data = max(0, data_needed - data)
        excess_calls = max(0, calls_needed - calls)

        extra_cost = excess_data * data_rate
        extra_cost += excess_calls * call_rate

        total_cost = price + extra_cost

        # Check usage, validity, and budget constraints
        usage_ok = data >= data_needed and calls >= calls_needed
        validity_ok = validity >= validity_needed
        budget_ok = total_cost <= budget

        eligible = usage_ok and validity_ok and budget_ok

        print(f"{name:<12}{price:>12.2f}{extra_cost:>13.2f}"
              f"{total_cost:>13.2f}{str(eligible):>12}")

        results.append({
            "name": name,
            "price": price,
            "extra_cost": extra_cost,
            "total_cost": total_cost,
            "usage_ok": usage_ok,
            "validity_ok": validity_ok,
            "budget_ok": budget_ok,
            "eligible": eligible
        })

    # Find the cheapest eligible plan
    eligible_plans = [p for p in results if p["eligible"]]

    print("-" * 90)

    if eligible_plans:
        best_plan = min(eligible_plans, key=lambda p: p["total_cost"])

        print("\nMOST ECONOMICAL ELIGIBLE PLAN")
        print("-" * 40)
        print("Plan Name       :", best_plan["name"])
        print(f"Base Price      : Rs. {best_plan['price']:.2f}")
        print(f"Excess Charges  : Rs. {best_plan['extra_cost']:.2f}")
        print(f"Total Cost      : Rs. {best_plan['total_cost']:.2f}")
        print(f"Budget Remaining: Rs. {budget - best_plan['total_cost']:.2f}")
    else:
        print("\nNo plan satisfies all requirements.")
        print("Consider increasing your budget or reducing usage "
              "or validity requirements.")


telecom_cost_optimization()
