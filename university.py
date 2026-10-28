#algorithm

1. Start the program.
2. Input the number of applicants.
3. Enter each applicant’s name, aggregate marks, minimum subject marks, attendance percentage, and family income.
4. Check eligibility based on marks, subject scores, attendance, and income.
5. Add eligible applicants to the list.
6. Rank eligible applicants by aggregate marks in descending order.
7. Resolve ties using higher attendance, then lower family income.
8. Display the eligible students and their ranks.
9. Stop the program.

#flow chart

              ( START )
                  |
                  v
          Input Number of Applicants
                  |
                  v
          Enter Applicant Details
       (Marks, Subject Score, Attendance,
               and Family Income)
                  |
                  v
            < Meets All Criteria? >
                /          \
              No            Yes
              |              |
              v              v
       Mark Ineligible   Add to Eligible List
              |              |
              +------+-------+
                     |
                     v
              More Applicants?
                /          \
              Yes           No
               |             |
               +----> Input Details
                             |
                             v
                    Sort Eligible Students
                    by Marks, Attendance,
                    and Lower Income
                             |
                             v
                    Assign Merit Ranks
                             |
                             v
                    Display Merit List
                             |
                             v
                          ( STOP )
#code


applicants = []
n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nApplicant {i+1}")
    name = input("Enter name: ")
    aggregate = float(input("Enter aggregate marks (%): "))
    subject = float(input("Enter minimum subject marks (%): "))
    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income: "))

    if (aggregate >= 75 and subject >= 40
            and attendance >= 75 and income <= 300000):
        applicants.append(
            (name, aggregate, attendance, income)
        )
        print("Eligible")
    else:
        print("Not Eligible")

# Rank by marks, then attendance, then lower income
applicants.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- SCHOLARSHIP MERIT LIST ---")

if not applicants:
    print("No eligible applicants")
else:
    for rank, student in enumerate(applicants, start=1):
        name, marks, attendance, income = student
        print(f"Rank {rank}: {name} | Marks: {marks}% | "
              f"Attendance: {attendance}% | Income: Rs.{income:.0f}")

#sample output

Enter number of applicants: 3

Applicant 1
Enter name: Ravi
Enter aggregate marks (%): 85
Enter minimum subject marks (%): 70
Enter attendance (%): 90
Enter annual family income: 200000
Eligible

Applicant 2
Enter name: Sita
Enter aggregate marks (%): 90
Enter minimum subject marks (%): 65
Enter attendance (%): 85
Enter annual family income: 250000
Eligible

Applicant 3
Enter name: Kumar
Enter aggregate marks (%): 70
Enter minimum subject marks (%): 60
Enter attendance (%): 80
Enter annual family income: 150000
Not Eligible

--- SCHOLARSHIP MERIT LIST ---
Rank 1: Sita | Marks: 90.0% | Attendance: 85.0% | Income: Rs.250000
Rank 2: Ravi | Marks: 85.0% | Attendance: 90.0% | Income: Rs.200000
