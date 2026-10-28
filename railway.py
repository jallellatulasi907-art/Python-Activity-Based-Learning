
def railway_fare_calculator():
    print("=" * 55)
    print("      RAILWAY FARE AND RESERVATION SYSTEM")
    print("=" * 55)

    # Distance-based fare per km
    distance_slabs = [
        (100, 1.00),
        (300, 0.80),
        (500, 0.60),
        (float("inf"), 0.50)
    ]

    # Travel class multipliers
    class_rates = {
        "sleeper": 1.0,
        "3ac": 2.0,
        "2ac": 3.0,
        "1ac": 4.0
    }

    reservation_fees = {
        "sleeper": 20,
        "3ac": 40,
        "2ac": 50,
        "1ac": 60
    }

    try:
        distance = float(input("Enter travel distance (km): "))
        if distance <= 0:
            print("Error: Distance must be positive.")
            return

        print("\nAvailable classes: Sleeper, 3AC, 2AC, 1AC")
        travel_class = input("Enter travel class: ").strip().lower()

        if travel_class not in class_rates:
            print("Error: Invalid travel class.")
            return

        passenger_count = int(input("Enter number of passengers: "))
        if passenger_count <= 0:
            print("Error: Passenger count must be positive.")
            return

        passengers = []

        for i in range(passenger_count):
            print(f"\nPassenger {i + 1}")
            name = input("Enter passenger name: ")
            age = int(input("Enter age: "))

            if age < 0 or age > 120:
                print("Error: Invalid age.")
                return

            passengers.append({"name": name, "age": age})

        # Calculate base fare using progressive distance slabs
        remaining_distance = distance
        base_fare = 0
        previous_limit = 0

        for limit, rate in distance_slabs:
            slab_distance = min(
                remaining_distance, limit - previous_limit
            )
            if slab_distance <= 0:
                break

            base_fare += slab_distance * rate
            remaining_distance -= slab_distance
            previous_limit = limit

            if remaining_distance <= 0:
                break

        # Apply travel class multiplier
        class_fare = base_fare * class_rates[travel_class]
        reservation_fee = reservation_fees[travel_class]

        total_fare = 0
        passenger_details = []

        for passenger in passengers:
            age = passenger["age"]

            # Illustrative age-based concessions
            if age < 5:
                concession_rate = 1.0
            elif age >= 60:
                concession_rate = 0.40
            else:
                concession_rate = 0.0

            concession = class_fare * concession_rate
            fare_after_concession = class_fare - concession

            # Children under 5 pay no base fare in this example.
            # Reservation fee still applies.
            passenger_total = fare_after_concession + reservation_fee

            passenger_details.append({
                "name": passenger["name"],
                "age": age,
                "base_fare": class_fare,
                "concession": concession,
                "reservation_fee": reservation_fee,
                "total": passenger_total
            })

            total_fare += passenger_total

        # Display reservation details
        print("\n" + "=" * 70)
        print("                 RESERVATION FARE STATEMENT")
        print("=" * 70)
        print(f"Distance       : {distance:.0f} km")
        print(f"Travel Class   : {travel_class.upper()}")
        print(f"Passenger Count: {passenger_count}")
        print("-" * 70)

        for p in passenger_details:
            print(f"\nPassenger: {p['name']} (Age: {p['age']})")
            print(f"Base Fare       : Rs. {p['base_fare']:.2f}")
            print(f"Age Concession  : Rs. {p['concession']:.2f}")
            print(f"Reservation Fee : Rs. {p['reservation_fee']:.2f}")
            print(f"Passenger Total : Rs. {p['total']:.2f}")

        print("\n" + "-" * 70)
        print(f"TOTAL RESERVATION FARE: Rs. {total_fare:.2f}")

        # Cancellation calculation
        cancel = input(
            "\nDo you want to calculate cancellation charges? (yes/no): "
        ).strip().lower()

        if cancel == "yes":
            cancellation_percent = float(input(
                "Enter cancellation penalty percentage (0-100): "
            ))

            if not 0 <= cancellation_percent <= 100:
                print("Error: Penalty must be between 0 and 100.")
                return

            penalty = total_fare * cancellation_percent / 100
            refund = total_fare - penalty

            print("\nCANCELLATION STATEMENT")
            print("-" * 40)
            print(f"Original Fare : Rs. {total_fare:.2f}")
            print(f"Penalty       : Rs. {penalty:.2f}")
            print(f"Refund Amount : Rs. {refund:.2f}")

        print("=" * 70)

    except ValueError:
        print("Error: Please enter valid numeric values.")


railway_fare_calculator()
