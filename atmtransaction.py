#algorithm

1.Start the program.
2.Initialize the ATM balance to ₹5000.
3.Set the maximum withdrawal limit to ₹2000 per transaction.
4.Enter the number of transactions.
5.For each transaction, choose Deposit or Withdrawal.
6.If Deposit is selected, enter the amount and add it to the balance if the amount is valid.
7.If Withdrawal is selected, check whether the amount is valid, within the withdrawal limit, and less than or equal to the available balance.
8.Reject invalid transactions and display an appropriate message.
9.Display the transaction summary and final balance.
10.Stop the program.
#flowchart
          ( START )
               |
               v
   Initialize Balance = 5000
      Withdrawal Limit = 2000
               |
               v
   Enter Transaction Type & Amount
               |
               v
       < Amount Valid? >
          /          \
        No            Yes
        |              |
        v              v
 Reject Transaction  < Transaction Type? >
                      /             \
                  Deposit         Withdraw
                     |                |
                     v                v
               Add Amount       Check Limit
               to Balance       and Balance
                     |                |
                     v                v
                     |         < Valid Withdrawal? >
                     |             /         \
                     |           No           Yes
                     |            |             |
                     |            v             v
                     |       Reject         Deduct Amount
                     |      Withdrawal      from Balance
                     |            |             |
                     v            v             v
                 Display Transaction Summary
                    and Final Balance
                           |
                           v
                         ( STOP )
#code

balance = 5000
limit = 2000
transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\n1. Deposit")
    print("2. Withdraw")
    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        transactions.append("Rejected: Invalid amount")

    elif choice == 1:
        balance += amount
        print("Deposit successful")
        transactions.append(f"Deposit: Rs.{amount}")

    elif choice == 2:
        if amount > limit:
            print("Withdrawal limit exceeded")
            transactions.append("Rejected: Limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
            transactions.append("Rejected: Insufficient balance")
        else:
            balance -= amount
            print("Withdrawal successful")
            transactions.append(f"Withdrawal: Rs.{amount}")

    else:
        print("Invalid choice")
        transactions.append("Rejected: Invalid choice")

print("\n--- Transaction Summary ---")
for t in transactions:
    print(t)

print("Final Balance: Rs.", balance)
#sample output
Enter number of transactions: 3

1. Deposit
2. Withdraw
Enter choice: 1
Enter amount: 1000
Deposit successful

1. Deposit
2. Withdraw
Enter choice: 2
Enter amount: 2000
Withdrawal successful

1. Deposit
2. Withdraw
Enter choice: 2
Enter amount: 3000
Withdrawal limit exceeded

--- Transaction Summary ---
Deposit: Rs.1000.0
Withdrawal: Rs.2000.0
Rejected: Limit exceeded
Final Balance: Rs. 4000.0
