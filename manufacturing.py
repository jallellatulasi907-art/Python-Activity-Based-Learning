
def manufacturing_analysis():
    print("=" * 55)
    print("   MANUFACTURING COST AND PROFITABILITY ANALYSIS")
    print("=" * 55)

    try:
        # Input details
        product_name = input("Enter product name: ")
        quantity = int(input("Enter production quantity: "))

        material_cost = float(input("Enter material cost per unit (Rs.): "))
        labour_cost = float(input("Enter labour cost per unit (Rs.): "))
        wastage_percent = float(input("Enter wastage percentage: "))
        machine_cost = float(input("Enter total machine cost (Rs.): "))
        selling_price = float(input("Enter selling price per unit (Rs.): "))
        profit_target = float(input("Enter target profit percentage: "))

        # Validate inputs
        if quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            return

        if min(material_cost, labour_cost, machine_cost,
               selling_price, profit_target, wastage_percent) < 0:
            print("Error: Values cannot be negative.")
            return

        if wastage_percent > 100:
            print("Error: Wastage percentage cannot exceed 100.")
            return

        # Calculate costs
        total_material = material_cost * quantity

        # Wastage cost is calculated as a percentage of material cost
        wastage_cost = total_material * wastage_percent / 100

        total_labour = labour_cost * quantity
        total_production_cost = (
            total_material + wastage_cost + total_labour + machine_cost
        )

        # Calculate revenue and profit
        total_revenue = selling_price * quantity
        profit = total_revenue - total_production_cost

        # Calculate profit margin and target profit
        profit_margin = (
            profit / total_revenue * 100
            if total_revenue > 0 else 0
        )

        target_profit_amount = total_production_cost * profit_target / 100

        # Check profitability target
        if profit >= target_profit_amount:
            status = "TARGET ACHIEVED"
        else:
            status = "TARGET NOT ACHIEVED"

        # Calculate break-even selling price per unit
        break_even_price = total_production_cost / quantity

        # Display report
        print("\n" + "=" * 55)
        print("          MANUFACTURING COST REPORT")
        print("=" * 55)
        print(f"Product Name             : {product_name}")
        print(f"Production Quantity      : {quantity}")
        print("-" * 55)
        print(f"Material Cost            : Rs. {total_material:,.2f}")
        print(f"Wastage Cost             : Rs. {wastage_cost:,.2f}")
        print(f"Labour Cost              : Rs. {total_labour:,.2f}")
        print(f"Machine Cost             : Rs. {machine_cost:,.2f}")
        print("-" * 55)
        print(f"Total Production Cost    : Rs. {total_production_cost:,.2f}")
        print(f"Cost Per Unit            : Rs. {break_even_price:,.2f}")
        print(f"Selling Price Per Unit   : Rs. {selling_price:,.2f}")
        print(f"Total Revenue            : Rs. {total_revenue:,.2f}")
        print(f"Total Profit/Loss        : Rs. {profit:,.2f}")
        print(f"Profit Margin            : {profit_margin:.2f}%")
        print(f"Target Profit Amount     : Rs. {target_profit_amount:,.2f}")
        print("-" * 55)
        print(f"Profitability Status     : {status}")
        print("=" * 55)

    except ValueError:
        print("Error: Please enter valid numeric values.")


manufacturing_analysis()
