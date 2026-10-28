
def employee_payroll():
    print("=" * 45)
    print("       EMPLOYEE PAYROLL SYSTEM")
    print("=" * 45)

    # Employee details
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")

    # Salary inputs
    basic_pay = float(input("Enter Basic Pay (Rs.): "))
    allowances = float(input("Enter Allowances (Rs.): "))
    overtime_hours = float(input("Enter Overtime Hours: "))
    overtime_rate = float(input("Enter Overtime Rate per Hour (Rs.): "))
    incentives = float(input("Enter Incentives (Rs.): "))

    # Validate inputs
    if min(basic_pay, allowances, overtime_hours,
           overtime_rate, incentives) < 0:
        print("Error: Salary components cannot be negative.")
        return

    # Calculate salary components
    overtime_pay = overtime_hours * overtime_rate
    gross_salary = basic_pay + allowances + overtime_pay + incentives

    # Progressive deductions (illustrative policy)
    if gross_salary <= 20000:
        tax = gross_salary * 0.05
    elif gross_salary <= 50000:
        tax = 20000 * 0.05 + (gross_salary - 20000) * 0.10
    else:
        tax = (20000 * 0.05
               + 30000 * 0.10
               + (gross_salary - 50000) * 0.20)

    # Other deduction: 5% of basic pay
    other_deduction = basic_pay * 0.05

    total_deductions = tax + other_deduction
    net_salary = gross_salary - total_deductions

    # Formatted salary statement
    print("\n" + "=" * 45)
    print("           SALARY STATEMENT")
    print("=" * 45)
    print(f"Employee ID       : {emp_id}")
    print(f"Employee Name     : {emp_name}")
    print("-" * 45)
    print(f"Basic Pay         : Rs. {basic_pay:,.2f}")
    print(f"Allowances        : Rs. {allowances:,.2f}")
    print(f"Overtime Pay      : Rs. {overtime_pay:,.2f}")
    print(f"Incentives        : Rs. {incentives:,.2f}")
    print("-" * 45)
    print(f"Gross Salary      : Rs. {gross_salary:,.2f}")
    print(f"Progressive Tax   : Rs. {tax:,.2f}")
    print(f"Other Deduction   : Rs. {other_deduction:,.2f}")
    print(f"Total Deductions  : Rs. {total_deductions:,.2f}")
    print("-" * 45)
    print(f"NET SALARY        : Rs. {net_salary:,.2f}")
    print("=" * 45)


employee_payroll()
