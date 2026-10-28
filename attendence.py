
import math

def attendance_recovery():
    print("=" * 60)
    print("          ATTENDANCE RECOVERY COMPUTATION")
    print("=" * 60)

    try:
        total_classes = int(input("Enter total classes conducted: "))
        attended_classes = int(input("Enter classes attended: "))
        threshold = float(input("Enter required attendance percentage: "))

        if total_classes <= 0:
            print("Error: Total classes must be positive.")
            return

        if not 0 <= attended_classes <= total_classes:
            print("Error: Attended classes must be between 0 and total classes.")
            return

        if not 0 < threshold <= 100:
            print("Error: Threshold must be greater than 0 and at most 100.")
            return

        # Calculate current attendance
        current_percentage = attended_classes / total_classes * 100

        print("\nCURRENT ATTENDANCE")
        print("-" * 40)
        print(f"Classes Conducted : {total_classes}")
        print(f"Classes Attended  : {attended_classes}")
        print(f"Classes Missed    : {total_classes - attended_classes}")
        print(f"Attendance        : {current_percentage:.2f}%")
        print(f"Eligibility Limit : {threshold:.2f}%")

        if current_percentage >= threshold:
            print("Status            : ELIGIBLE")
        else:
            print("Status            : NOT YET ELIGIBLE")

        # Future attendance scenarios:
        # Each scenario assumes every future class is attended.
        scenarios = {
            "Best case": 1.00,
            "Regular attendance": 0.90,
            "Occasional absence": 0.75
        }

        print("\nFUTURE ATTENDANCE SCENARIOS")
        print("-" * 70)
        print(f"{'Scenario':<25}{'Future Rate':>15}"
              f"{'Classes Needed':>20}")
        print("-" * 70)

        for scenario, future_rate in scenarios.items():
            # Find minimum n such that:
            # (attended + future_rate*n) /
            # (total_classes + n) >= threshold / 100
            #
            # Integer class counts are used. A future attendance rate
            # below 100% is modeled as a long-run proportion.

            t = threshold / 100

            if attended_classes / total_classes >= t:
                needed = 0
            elif future_rate <= t:
                needed = None
            else:
                needed = math.ceil(
                    (t * total_classes - attended_classes)
                    / (future_rate - t)
                )

                # Correct possible floating-point boundary errors
                while (
                    (attended_classes + future_rate * needed)
                    / (total_classes + needed) < t - 1e-12
                ):
                    needed += 1

            if needed is None:
                result = "Not achievable"
            else:
                result = str(needed)

            print(f"{scenario:<25}{future_rate * 100:>14.0f}%"
                  f"{result:>20}")

        # Exact minimum if every future class is attended
        if current_percentage < threshold:
            minimum = math.ceil(
                (threshold * total_classes / 100 - attended_classes)
                / (1 - threshold / 100)
            )

            while (
                (attended_classes + minimum)
                / (total_classes + minimum) * 100
                < threshold - 1e-10
            ):
                minimum += 1

            print("\nMINIMUM CONSECUTIVE CLASSES")
            print("-" * 40)
            print(f"Attend the next {minimum} classes "
                  "without missing any.")

            future_total = total_classes + minimum
            future_attended = attended_classes + minimum
            future_percentage = future_attended / future_total * 100

            print(f"Projected Attendance: {future_percentage:.2f}%")
        else:
            print("\nNo additional classes are needed to meet "
                  "the current threshold.")

        print("=" * 60)

    except ValueError:
        print("Error: Please enter valid numeric values.")


attendance_recovery()
