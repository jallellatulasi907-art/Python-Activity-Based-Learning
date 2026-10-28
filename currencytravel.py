#algorithm

1. Start the program.
2. Input the travel budget in Indian Rupees (INR).
3. Enter travel expense categories and their amounts in foreign currency.
4. Input the exchange rate and conversion fee percentage.
5. Convert each expense into INR and calculate the conversion fee.
6. Calculate the total travel expenses, including fees.
7. Compare total expenses with the budget.
8. Identify the largest expense category.
9. Display the expense summary, budget status, and largest expense.
10. Stop the program.

#flow chart

               ( START )
                  |
                  v
       Input Travel Budget (INR)
       Input Conversion Fee (%)
                  |
                  v
       Enter Expense Amounts,
       Currencies and Exchange Rates
                  |
                  v
       Convert Expenses into INR
                  |
                  v
       Calculate Conversion Fees
                  |
                  v
       Calculate Total Expenses
                  |
                  v
       Find Largest Expense Category
                  |
                  v
         < Total > Budget? >
             /        \
           Yes         No
            |           |
            v           v
      Print Budget   Print Remaining
       Exceeded        Budget
            \           /
             v         v
        Display Expense Summary
                  |
                  v
               ( STOP )
#code


budget = float(input("Enter travel budget in INR: "))
fee_rate = float(input("Enter conversion fee percentage: "))

expenses = {
    "Hotel": ("USD", 200, 85),
    "Food": ("EUR", 100, 90),
    "Shopping": ("USD", 80, 85)
}

total = 0
category_totals = {}

print("\n--- Travel Expense Summary ---")

for category, (currency, amount, rate) in expenses.items():
    converted = amount * rate
    fee = converted * fee_rate / 100
    final_amount = converted + fee

    category_totals[category] = final_amount
    total += final_amount

    print(f"{category}: {currency} {amount}")
    print(f"Converted with fee: Rs.{final_amount:.2f}")

largest = max(category_totals, key=category_totals.get)

print(f"\nTotal Expenses: Rs.{total:.2f}")
print(f"Travel Budget: Rs.{budget:.2f}")
print("Largest Expense:", largest)

if total > budget:
    print("Budget Exceeded")
else:
    print(f"Budget Remaining: Rs.{budget-total:.2f}")

#sample output

Enter travel budget in INR: 30000
Enter conversion fee percentage: 2

--- Travel Expense Summary ---
Hotel: USD 200
Converted with fee: Rs.17340.00
Food: EUR 100
Converted with fee: Rs.9180.00
Shopping: USD 80
Converted with fee: Rs.6936.00

Total Expenses: Rs.33456.00
Travel Budget: Rs.30000.00
Largest Expense: Hotel
Budget Exceeded
