
def atm_simulation():
    print("=" * 55)
    print("          ATM TRANSACTION SIMULATION")
    print("=" * 55)

    try:
        balance = float(input("Enter initial account balance (Rs.): "))
        withdrawal_limit = float(
            input("Enter maximum withdrawal per transaction (Rs.): ")
        )
        daily_limit = float(
            input("Enter daily withdrawal limit (Rs.): ")
        )
        n = int(input("Enter number of transactions: "))

        if balance < 0 or withdrawal_limit <= 0 or daily_limit <= 0:
            print("Error: Invalid balance or withdrawal limits.")
            return

        if n <= 0:
            print("Error: Number of transactions must be positive.")
            return

        initial_balance = balance
        total_deposits = 0
        total_withdrawals = 0
        daily_withdrawals = 0
        successful = 0
        rejected = 0
        transactions = []

        for i in range(n):
            print(f"\nTransaction {i + 1}")
            transaction_type = input(
                "Enter transaction type (deposit/withdraw): "
            ).strip().lower()

            try:
                amount = float(input("Enter amount (Rs.): "))
            except ValueError:
                print("Invalid amount. Transaction rejected.")
                rejected += 1
                transactions.append(
                    ("Invalid amount", 0, "Rejected", balance)
                )
                continue

            # Validate transaction amount
            if amount <= 0:
                print("Rejected: Amount must be greater than zero.")
                rejected += 1
                transactions.append(
                    (transaction_type, amount, "Rejected", balance)
                )
                continue

            if transaction_type == "deposit":
                balance += amount
                total_deposits += amount
                successful += 1
                status = "Successful"

            elif transaction_type == "withdraw":
                if amount > withdrawal_limit:
                    print("Rejected: Per-transaction withdrawal limit exceeded.")
                    rejected += 1
                    status = "Rejected"

                elif daily_withdrawals + amount > daily_limit:
                    print("Rejected: Daily withdrawal limit exceeded.")
                    rejected += 1
                    status = "Rejected"

                elif amount > balance:
                    print("Rejected: Insufficient account balance.")
                    rejected += 1
                    status = "Rejected"

                else:
                    balance -= amount
                    total_withdrawals += amount
                    daily_withdrawals += amount
                    successful += 1
                    status = "Successful"

            else:
                print("Rejected: Invalid transaction type.")
                rejected += 1
                status = "Rejected"

            transactions.append(
                (transaction_type, amount, status, balance)
            )

            print(f"Transaction Status: {status}")
            print(f"Current Balance: Rs. {balance:.2f}")

        # Transaction summary
        print("\n" + "=" * 75)
        print("                  ATM TRANSACTION SUMMARY")
        print("=" * 75)
        print(f"{'Type':<18}{'Amount':>14}{'Status':>16}{'Balance':>20}")
        print("-" * 75)

        for transaction_type, amount, status, current_balance in transactions:
            print(
                f"{transaction_type:<18}"
                f"{amount:>14.2f}"
                f"{status:>16}"
                f"{current_balance:>20.2f}"
            )

        print("-" * 75)
        print(f"Initial Balance     : Rs. {initial_balance:.2f}")
        print(f"Total Deposits      : Rs. {total_deposits:.2f}")
        print(f"Total Withdrawals   : Rs. {total_withdrawals:.2f}")
        print(f"Successful          : {successful}")
        print(f"Rejected            : {rejected}")
        print(f"Final Balance       : Rs. {balance:.2f}")
        print("=" * 75)

    except ValueError:
        print("Error: Please enter valid numeric values.")


atm_simulation()
