
def travel_budget_analysis():
    print("=" * 60)
    print("       MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
    print("=" * 60)

    try:
        home_currency = input(
            "Enter home currency (e.g., INR): "
        ).strip().upper()

        budget = float(input("Enter total travel budget: Rs. "))
        fee_percent = float(input("Enter conversion fee (%): "))
        n = int(input("Enter number of expense categories: "))

        if budget < 0 or not 0 <= fee_percent <= 100 or n <= 0:
            print("Error: Invalid budget, fee, or category count.")
            return

        expenses = []
        total_before_fees = 0
        total_fees = 0

        # Collect expenses and exchange rates
        for i in range(n):
            print(f"\nExpense Category {i + 1}")

            category = input("Enter category name: ").strip()
            currency = input(
                "Enter expense currency (e.g., USD): "
            ).strip().upper()

            amount = float(input("Enter expense amount: "))
            rate = float(input(
                f"Enter exchange rate (1 {currency} = ? "
                f"{home_currency}): "
            ))

            if not category or amount < 0 or rate <= 0:
                print("Error: Invalid category, amount, or exchange rate.")
                return

            # Convert expense to home currency
            converted_amount = amount * rate

            # Calculate conversion fee
            fee = converted_amount * fee_percent / 100
            total_amount = converted_amount + fee

            expenses.append({
                "category": category,
                "currency": currency,
                "amount": amount,
                "rate": rate,
                "converted": converted_amount,
                "fee": fee,
                "total": total_amount
            })

            total_before_fees += converted_amount
            total_fees += fee

        # Total expenditure including conversion fees
        total_spending = total_before_fees + total_fees
        remaining_budget = budget - total_spending

        # Identify the largest expense category
        largest_expense = max(expenses, key=lambda x: x["total"])

        # Display report
        print("\n" + "=" * 90)
        print("                    TRAVEL EXPENSE REPORT")
        print("=" * 90)

        print(f"{'Category':<16}{'Currency':<10}{'Original':>12}"
              f"{'Converted':>15}{'Fee':>12}{'Total':>15}")
        print("-" * 90)

        for e in expenses:
            print(
                f"{e['category']:<16}"
                f"{e['currency']:<10}"
                f"{e['amount']:>12.2f}"
                f"{e['converted']:>15.2f}"
                f"{e['fee']:>12.2f}"
                f"{e['total']:>15.2f}"
            )

        print("-" * 90)
        print(f"Total Before Fees ({home_currency}): "
              f"{total_before_fees:,.2f}")
        print(f"Total Conversion Fees ({home_currency}): "
              f"{total_fees:,.2f}")
        print(f"Total Spending ({home_currency}): "
              f"{total_spending:,.2f}")
        print(f"Travel Budget ({home_currency}): {budget:,.2f}")

        print("-" * 60)

        if remaining_budget >= 0:
            print(f"Budget Remaining: {remaining_budget:,.2f} "
                  f"{home_currency}")
            print("Status: WITHIN BUDGET")
        else:
            print(f"Budget Exceeded By: {-remaining_budget:,.2f} "
                  f"{home_currency}")
            print("Status: OVER BUDGET")

        print(
            f"Largest Expense Category: "
            f"{largest_expense['category']} "
            f"({largest_expense['total']:,.2f} {home_currency})"
        )

        print("=" * 90)

    except ValueError:
        print("Error: Please enter valid numeric values.")


travel_budget_analysis()
