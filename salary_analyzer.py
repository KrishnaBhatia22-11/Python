salaries = [30000, 45000, 25000, 50000, 40000]

highest = salaries[0]
lowest = salaries[0]
total = 0

for salary in salaries:
    if salary > highest:
        highest = salary
    if salary < lowest:
        lowest = salary
    total += salary

average = total / len(salaries)

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Krishna Bhatia 1/23/SET/BCS/358")
