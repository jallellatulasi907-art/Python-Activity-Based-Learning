
def examination_result():
    print("=" * 60)
    print("       EXAMINATION RESULT AND GRACE-MARK SYSTEM")
    print("=" * 60)

    try:
        student_name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        n = int(input("Enter number of subjects: "))

        if n <= 0:
            print("Error: Number of subjects must be positive.")
            return

        max_marks = float(input("Enter maximum marks per subject: "))
        pass_marks = float(input("Enter minimum passing marks: "))
        grace_limit = int(input("Enter maximum grace marks per subject: "))
        total_grace_limit = int(input("Enter total grace marks allowed: "))

        if (max_marks <= 0 or pass_marks < 0
                or pass_marks > max_marks
                or grace_limit < 0 or total_grace_limit < 0):
            print("Error: Invalid examination policy.")
            return

        subjects = []
        total_marks = 0
        total_maximum = n * max_marks
        grace_used = 0

        for i in range(n):
            print(f"\nSubject {i + 1}")
            subject_name = input("Enter subject name: ")
            marks = float(input("Enter marks obtained: "))

            if marks < 0 or marks > max_marks:
                print(
                    f"Error: Marks must be between 0 and {max_marks}."
                )
                return

            # Calculate grace marks needed to pass this subject
            shortage = max(0, pass_marks - marks)

            # Apply grace only if shortage is within the subject limit
            remaining_grace = max(0, total_grace_limit - grace_used)

            if shortage > 0 and shortage <= grace_limit:
                grace = min(shortage, remaining_grace)
            else:
                grace = 0

            # Do not award more than the marks needed to pass
            grace = min(grace, max_marks - marks)

            final_marks = marks + grace
            grace_used += grace

            passed = final_marks >= pass_marks

            subjects.append({
                "name": subject_name,
                "original": marks,
                "grace": grace,
                "final": final_marks,
                "passed": passed
            })

            total_marks += final_marks

        # Determine overall result
        all_passed = all(subject["passed"] for subject in subjects)
        percentage = (total_marks / total_maximum) * 100

        if not all_passed:
            classification = "FAIL"
        elif percentage >= 75:
            classification = "DISTINCTION"
        elif percentage >= 60:
            classification = "FIRST CLASS"
        elif percentage >= 50:
            classification = "SECOND CLASS"
        else:
            classification = "PASS"

        # Display result
        print("\n" + "=" * 75)
        print("                    EXAMINATION RESULT")
        print("=" * 75)
        print(f"Student Name: {student_name}")
        print(f"Roll Number : {roll_no}")
        print("-" * 75)

        print(f"{'Subject':<20}{'Original':>12}{'Grace':>10}"
              f"{'Final':>12}{'Result':>12}")
        print("-" * 75)

        for subject in subjects:
            status = "PASS" if subject["passed"] else "FAIL"
            print(
                f"{subject['name']:<20}"
                f"{subject['original']:>12.2f}"
                f"{subject['grace']:>10.2f}"
                f"{subject['final']:>12.2f}"
                f"{status:>12}"
            )

        print("-" * 75)
        print(f"Total Marks       : {total_marks:.2f} / {total_maximum:.2f}")
        print(f"Percentage        : {percentage:.2f}%")
        print(f"Grace Marks Used  : {grace_used}")
        print(f"Overall Result    : {classification}")
        print("=" * 75)

    except ValueError:
        print("Error: Please enter valid numeric values.")


examination_result()
