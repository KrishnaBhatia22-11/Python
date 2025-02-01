grades = input("Enter grades (comma separated): ").split(", ")
grades = [int(grade) for grade in grades]

highest = grades[0]
lowest = grades[0]
total = 0

for grade in grades:
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade
    total += grade

average = total / len(grades)

print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Average Grade:", average)
print("Krishna Bhatia 1/23/SET/BCS/358")
