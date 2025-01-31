# Accept basic pay
basic_pay = float(input("Enter basic pay: "))

# Calculate HRA (10% of basic pay) & TA (5% of basic pay)
HRA = 0.10 * basic_pay
TA = 0.05 * basic_pay

# Calculate total salary
total_salary = basic_pay + HRA + TA

# Print result
print("Total Salary:", total_salary)
