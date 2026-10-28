#algorithm

1. Start the program.
2. Input material cost, labour charges, wastage cost, machine cost, quantity produced, selling price per unit, and target profit percentage.
3. Calculate total production cost.
4. Calculate total sales revenue.
5. Calculate profit and profit percentage.
6. Compare actual profit percentage with the target profit percentage.
7. Display total cost, revenue, profit, and target status.
8. Stop the program.

#flow chart

              ( START )
                  |
                  v
       Input Material, Labour,
       Wastage and Machine Costs
                  |
                  v
       Input Quantity, Selling Price
       and Target Profit Percentage
                  |
                  v
           < Inputs valid? >
             /          \
           No            Yes
           |              |
           v              v
     Print Invalid    Calculate Total Cost
         Input        = Material + Labour
           |          + Wastage + Machine
           v              |
        ( STOP )          v
                    Calculate Revenue
                    = Quantity x Price
                          |
                          v
                    Calculate Profit
                    = Revenue - Cost
                          |
                          v
                    Calculate Profit %
                          |
                          v
                    < Profit % >= Target? >
                        /          \
                      Yes           No
                       |             |
                       v             v
                 Target Achieved  Target Not
                                  Achieved
                       \             /
                        v           v
                    Display Report
                          |
                          v
                       ( STOP )

#code


material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
quantity = int(input("Enter quantity produced: "))
price = float(input("Enter selling price per unit: "))
target = float(input("Enter target profit percentage: "))

if material < 0 or labour < 0 or wastage < 0 or machine < 0:
    print("Invalid cost")
elif quantity <= 0 or price < 0 or target < 0:
    print("Invalid quantity, price or target")
else:
    cost = material + labour + wastage + machine
    revenue = quantity * price
    profit = revenue - cost
    profit_percent = profit / cost * 100 if cost > 0 else 0

    print("\n--- Manufacturing Report ---")
    print(f"Total Production Cost: Rs.{cost:.2f}")
    print(f"Sales Revenue: Rs.{revenue:.2f}")
    print(f"Profit/Loss: Rs.{profit:.2f}")
    print(f"Profit Percentage: {profit_percent:.2f}%")

    if profit_percent >= target:
        print("Target Profit Achieved")
    else:
        print("Target Profit Not Achieved")

#sample output

Enter material cost: 10000
Enter labour charges: 4000
Enter wastage cost: 1000
Enter machine cost: 2000
Enter quantity produced: 100
Enter selling price per unit: 250
Enter target profit percentage: 50

--- Manufacturing Report ---
Total Production Cost: Rs.17000.00
Sales Revenue: Rs.25000.00
Profit/Loss: Rs.8000.00
Profit Percentage: 47.06%
Target Profit Not Achieved
