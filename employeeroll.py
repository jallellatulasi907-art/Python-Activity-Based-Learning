#algorithm

1. Start the program.
2. Input basic salary, allowances, overtime pay, and incentives.
3. Calculate gross salary.
4. Calculate progressive deductions based on salary slabs.
5. Calculate net salary by subtracting deductions from gross salary.
6. Display the formatted salary statement.
7. Stop the program.

#flow chart

             ( START )
                 |
                 v
       Input Basic Salary,
       Allowances, Overtime,
       and Incentives
                 |
                 v
       Calculate Gross Salary
       = Basic + Allowances
         + Overtime + Incentives
                 |
                 v
         < Gross <= 20000? >
             /          \
           Yes           No
            |             |
            v             v
      Deduction = 5%   < Gross <= 50000? >
                         /          \
                       Yes           No
                        |             |
                        v             v
                  Deduction =     Deduction =
                  5% of 20000     5% of 20000
                  + 10% of       + 10% of 30000
                  remaining      + 15% of remaining
                        \             /
                         v           v
                    Calculate Net Salary
                    = Gross - Deduction
                              |
                              v
                    Display Salary Statement
                              |
                              v
                           ( STOP )

#code


basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

# Progressive deduction slabs
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 50000:
    deduction = 20000 * 0.05 + (gross - 20000) * 0.10
else:
    deduction = (20000 * 0.05 +
                 30000 * 0.10 +
                 (gross - 50000) * 0.15)

net = gross - deduction

print("\n--- SALARY STATEMENT ---")
print(f"Basic Salary : Rs.{basic:.2f}")
print(f"Allowances   : Rs.{allowances:.2f}")
print(f"Overtime Pay : Rs.{overtime:.2f}")
print(f"Incentives   : Rs.{incentives:.2f}")
print(f"Gross Salary : Rs.{gross:.2f}")
print(f"Deduction    : Rs.{deduction:.2f}")
print(f"Net Salary   : Rs.{net:.2f}")

#sample output

Enter basic salary: 30000
Enter allowances: 5000
Enter overtime pay: 2000
Enter incentives: 3000

--- SALARY STATEMENT ---
Basic Salary : Rs.30000.00
Allowances   : Rs.5000.00
Overtime Pay : Rs.2000.00
Incentives   : Rs.3000.00
Gross Salary : Rs.40000.00
Deduction    : Rs.3000.00
Net Salary   : Rs.37000.00
