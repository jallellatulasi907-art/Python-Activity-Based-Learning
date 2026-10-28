#algorithm

1. Start the program.
2. Input the number of products.
3. For each product, enter its name, price, quantity, and category.
4. Calculate the subtotal for each product.
5. Apply category-specific tax rates.
6. Calculate the total bill before discounts.
7. Apply threshold discounts and maximum concession limits.
8. Calculate the final payable amount.
9. Display the itemized invoice with taxes and discounts.
10. Stop the program.

#flow chart

              ( START )
                  |
                  v
          Input Number of Products
                  |
                  v
          Enter Product Details
       (Name, Price, Quantity, Category)
                  |
                  v
             < Details Valid? >
               /          \
             No            Yes
             |              |
             v              v
        Print Error    Calculate Subtotal
             |         and Category Tax
             v              |
          ( STOP )          v
                     Process All Products
                             |
                             v
                     Calculate Total Bill
                             |
                             v
                     < Bill >= 5000? >
                       /          \
                     Yes           No
                      |             |
                      v             v
                 Apply 10%     < Bill >= 2000? >
                                /          \
                              Yes           No
                               |             |
                               v             v
                           Apply 5%     No Discount
                               \             /
                                v           v
                         Apply Maximum Discount
                                  |
                                  v
                         Calculate Final Bill
                                  |
                                  v
                         Display Itemized Invoice
                                  |
                                  v
                               ( STOP )    
#code


n = int(input("Enter number of products: "))

subtotal = 0
tax_total = 0
items = []

if n <= 0:
    print("Invalid number of products")
else:
    for i in range(n):
        print(f"\nProduct {i+1}")
        name = input("Enter product name: ")
        price = float(input("Enter unit price: "))
        qty = int(input("Enter quantity: "))
        category = input("Category (food/electronics): ").lower()

        if price < 0 or qty <= 0 or category not in ["food", "electronics"]:
            print("Invalid product details")
            break

        amount = price * qty
        tax_rate = 5 if category == "food" else 18
        tax = amount * tax_rate / 100

        subtotal += amount
        tax_total += tax
        items.append((name, qty, amount, tax))

    if len(items) == n:
        total = subtotal + tax_total

        if total >= 5000:
            discount = total * 0.10
        elif total >= 2000:
            discount = total * 0.05
        else:
            discount = 0

        discount = min(discount, 1000)
        final = total - discount

        print("\n--- ITEMIZED INVOICE ---")
        for name, qty, amount, tax in items:
            print(f"{name}: Qty={qty}, Amount=Rs.{amount:.2f}, Tax=Rs.{tax:.2f}")

        print(f"Subtotal: Rs.{subtotal:.2f}")
        print(f"Total Tax: Rs.{tax_total:.2f}")
        print(f"Discount: Rs.{discount:.2f}")
        print(f"Final Bill: Rs.{final:.2f}")

#sample output

Enter number of products: 2

Product 1
Enter product name: Rice
Enter unit price: 1000
Enter quantity: 2
Category (food/electronics): food

Product 2
Enter product name: Headphones
Enter unit price: 2000
Enter quantity: 2
Category (food/electronics): electronics

--- ITEMIZED INVOICE ---
Rice: Qty=2, Amount=Rs.2000.00, Tax=Rs.100.00
Headphones: Qty=2, Amount=Rs.4000.00, Tax=Rs.720.00
Subtotal: Rs.6000.00
Total Tax: Rs.820.00
Discount: Rs.682.00
Final Bill: Rs.6138.00
