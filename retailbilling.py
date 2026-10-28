
def retail_billing():
    print("=" * 60)
    print("             RETAIL BILLING SYSTEM")
    print("=" * 60)

    # Category-specific tax rates (illustrative)
    tax_rates = {
        "food": 0.05,
        "clothing": 0.05,
        "electronics": 0.18,
        "other": 0.12
    }

    # Discount policy
    discount_threshold = 5000
    discount_rate = 0.10
    max_concession = 1000

    try:
        n = int(input("Enter number of products: "))

        if n <= 0:
            print("Error: Number of products must be positive.")
            return

        products = []
        subtotal = 0
        total_tax = 0

        for i in range(n):
            print(f"\nProduct {i + 1}")

            name = input("Enter product name: ")
            category = input(
                "Enter category (food/clothing/electronics/other): "
            ).strip().lower()

            if category not in tax_rates:
                print("Invalid category. Please try again.")
                return

            price = float(input("Enter unit price (Rs.): "))
            quantity = int(input("Enter quantity: "))

            if price < 0 or quantity <= 0:
                print("Error: Price cannot be negative and "
                      "quantity must be positive.")
                return

            amount = price * quantity
            tax = amount * tax_rates[category]

            products.append({
                "name": name,
                "category": category,
                "price": price,
                "quantity": quantity,
                "amount": amount,
                "tax_rate": tax_rates[category],
                "tax": tax
            })

            subtotal += amount
            total_tax += tax

        # Apply threshold discount to the subtotal
        if subtotal >= discount_threshold:
            discount = subtotal * discount_rate
            discount = min(discount, max_concession)
        else:
            discount = 0

        # Calculate final bill
        final_amount = subtotal - discount + total_tax

        # Display itemized invoice
        print("\n" + "=" * 85)
        print("                         ITEMIZED INVOICE")
        print("=" * 85)
        print(f"{'Product':<16}{'Category':<15}{'Qty':>5}"
              f"{'Price':>10}{'Amount':>12}{'Tax':>10}")
        print("-" * 85)

        for p in products:
            print(
                f"{p['name']:<16}"
                f"{p['category']:<15}"
                f"{p['quantity']:>5}"
                f"{p['price']:>10.2f}"
                f"{p['amount']:>12.2f}"
                f"{p['tax']:>10.2f}"
            )

        print("-" * 85)
        print(f"{'Subtotal:':>65} Rs. {subtotal:>10.2f}")
        print(f"{'Discount:':>65} Rs. {discount:>10.2f}")
        print(f"{'Total Tax:':>65} Rs. {total_tax:>10.2f}")
        print("-" * 85)
        print(f"{'FINAL AMOUNT:':>65} Rs. {final_amount:>10.2f}")
        print("=" * 85)

    except ValueError:
        print("Error: Please enter valid numeric values.")


retail_billing()
