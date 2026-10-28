#algorithm

1. Start the program.
2. Input the number of subjects and maximum marks per subject.
3. Enter the marks obtained in each subject.
4. Check whether the marks are valid.
5. Apply the subject-wise pass criteria.
6. If a student fails by a small margin, apply the specified grace marks.
7. Ensure that final marks do not exceed maximum marks.
8. Calculate total marks and percentage.
9. Display the final result and classification.
10. Stop the program.

#flow chart

              ( START )
                  |
                  v
        Input Number of Subjects
                  |
                  v
          Input Subject Marks
                  |
                  v
             < Marks Valid? >
              /          \
            No            Yes
            |              |
            v              v
       Print Error    < Marks < Pass Mark? >
            |             /          \
            v           Yes           No
         ( STOP )        |             |
                         v             |
                 < Within Grace Limit? >
                    /          \
                  Yes           No
                   |             |
                   v             v
             Add Grace Marks  Keep Marks
                   \             /
                    v           v
              Check All Subjects
                    |
                    v
              Calculate Total
              and Percentage
                    |
                    v
              < Any Subject Fail? >
                  /          \
                Yes           No
                 |             |
                 v             v
             Print FAIL   Determine Class
                 \             /
                  v           v
                Display Result
                     |
                     v
                  ( STOP )

#code


n = int(input("Enter number of subjects: "))
maximum = 100
pass_mark = 35
grace_limit = 5

marks = []
final_marks = []
failed = 0

if n <= 0:
    print("Invalid number of subjects")
else:
    for i in range(n):
        m = int(input(f"Enter marks in subject {i+1}: "))

        if m < 0 or m > maximum:
            print("Invalid marks")
            break

        if m < pass_mark and pass_mark - m <= grace_limit:
            m = pass_mark
            print("Grace marks applied")

        final_marks.append(m)

        if m < pass_mark:
            failed += 1

    if len(final_marks) == n:
        total = sum(final_marks)
        percentage = total / (n * maximum) * 100

        print("\n--- EXAM RESULT ---")
        print("Final Marks:", final_marks)
        print("Total Marks:", total)
        print(f"Percentage: {percentage:.2f}%")

        if failed > 0:
            print("Result: FAIL")
        elif percentage >= 75:
            print("Classification: Distinction")
        elif percentage >= 60:
            print("Classification: First Class")
        elif percentage >= 50:
            print("Classification: Second Class")
        else:
            print("Classification: Pass")

#sample output

Enter number of subjects: 4
Enter marks in subject 1: 80
Enter marks in subject 2: 33
Grace marks applied
Enter marks in subject 3: 65
Enter marks in subject 4: 72

--- EXAM RESULT ---
Final Marks: [80, 35, 65, 72]
Total Marks: 252
Percentage: 63.00%
Classification: First Class
