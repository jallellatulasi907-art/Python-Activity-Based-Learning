#algorithm

1.Start the program.
2.Input total classes conducted, classes attended, and eligibility percentage.
3.Check whether the input values are valid.
4.Calculate current attendance percentage.
5.If attendance meets the eligibility threshold, display “Eligible”.
6.Otherwise, calculate the minimum consecutive classes required under different future attendance scenarios.
7.Display the results.
8.Stop the program.
#flow chart

             ( START )
                 |
                 v
       Input Total Classes (T)
       Input Attended Classes (A)
       Input Eligibility (P)
                 |
                 v
           < Inputs valid? >
             /         \
           No           Yes
           |             |
           v             v
    Print Invalid    Calculate Current
        Input        Attendance = A/T * 100
           |             |
           v             v
        ( STOP )   < Current >= Target? >
                      /          \
                    Yes           No
                     |             |
                     v             v
               Print Eligible  Check Future Rates
                                    |
                                    v
                              Calculate Minimum
                              Classes Required
                                    |
                                    v
                              Display Results
                                    |
                                    v
                                  ( STOP )
#code


import math

total = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))
target = float(input("Enter eligibility percentage: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid input")
elif not 0 < target <= 100:
    print("Invalid eligibility percentage")
else:
    current = attended / total * 100
    print(f"Current Attendance: {current:.2f}%")

    if current >= target:
        print("Eligible")
    elif target == 100:
        print("Attend all future classes to reach 100%")
    else:
        for rate in [100, 90, 80, 75]:
            if rate <= target:
                print(f"{rate}% future attendance: "
                      "Target cannot be reached")
            else:
                n = math.ceil(
                    (target * total - 100 * attended)
                    / (rate - target)
                )
                print(f"{rate}% future attendance: "
                      f"{n} classes required")
#sample output

Enter total classes: 40
Enter classes attended: 28
Enter eligibility percentage: 75

Current Attendance: 70.00%
100% future attendance: 8 classes required
90% future attendance: 24 classes required
80% future attendance: 40 classes required
75% future attendance: Target cannot be reached        
        
             
    
