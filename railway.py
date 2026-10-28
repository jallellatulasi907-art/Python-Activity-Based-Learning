#algorithm

1. Start the program.
2. Input the number of passengers, distance, travel class, age, and cancellation status.
3. Calculate the base fare according to distance slabs.
4. Apply the travel class multiplier.
5. Apply age-based concessions for eligible passengers.
6. Add the reservation fee.
7. If the ticket is cancelled, calculate the cancellation penalty.
8. Display the final fare and reservation details.
9. Stop the program.

#flow chart

               ( START )
                  |
                  v
       Input Passenger Count,
       Distance and Travel Class
                  |
                  v
             < Valid Input? >
              /          \
            No            Yes
            |              |
            v              v
       Print Error    Input Passenger Ages
            |              |
            v              v
         ( STOP )    Calculate Base Fare
                           |
                           v
                    Apply Class Multiplier
                           |
                           v
                    Apply Age Concession
                           |
                           v
                    Add Reservation Fee
                           |
                           v
                    Calculate Total Fare
                           |
                           v
                      < Cancel? >
                       /       \
                     Yes        No
                      |          |
                      v          v
                Calculate     Confirm
                Penalty       Reservation
                and Refund       |
                      \         /
                       v       v
                   Display Fare
                   and Final Details
                           |
                           v
                        ( STOP )

#code


n = int(input("Enter number of passengers: "))
distance = float(input("Enter distance in km: "))

print("1. Sleeper  2. AC 3-Tier  3. AC 2-Tier")
choice = int(input("Choose travel class: "))

if choice == 1:
    rate = 1.0
elif choice == 2:
    rate = 2.0
elif choice == 3:
    rate = 3.0
else:
    rate = 0

if n <= 0 or distance <= 0 or rate == 0:
    print("Invalid input")
else:
    total = 0

    for i in range(n):
        age = int(input(f"Enter age of passenger {i+1}: "))

        if distance <= 100:
            base = distance * 1
        elif distance <= 500:
            base = 100 + (distance - 100) * 1.5
        else:
            base = 700 + (distance - 500) * 2

        fare = base * rate

        if age >= 60:
            fare *= 0.90

        fare += 50  # Reservation fee
        total += fare

    print(f"Total reservation fare: Rs.{total:.2f}")

    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = total * 0.25
        refund = total - penalty
        print(f"Cancellation penalty: Rs.{penalty:.2f}")
        print(f"Refund amount: Rs.{refund:.2f}")
    else:
        print("Reservation confirmed")

#sample output

Enter number of passengers: 2
Enter distance in km: 200
1. Sleeper  2. AC 3-Tier  3. AC 2-Tier
Choose travel class: 1
Enter age of passenger 1: 65
Enter age of passenger 2: 30

Total reservation fare: Rs.510.00
Cancel ticket? (yes/no): yes
Cancellation penalty: Rs.127.50
Refund amount: Rs.382.50
