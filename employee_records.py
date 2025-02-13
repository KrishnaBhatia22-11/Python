emp1 = (101, "Amit", 25, "HR", 50000)
emp2 = (102, "Ravi", 30, "IT", 70000)
emp3 = (103, "Priya", 28, "Finance", 65000)
emp4 = (104, "Vikram", 35, "IT", 80000)
emp5 = (105, "Neha", 27, "HR", 55000)

employees = (emp1, emp2, emp3, emp4, emp5)
print("All Employees:", employees)

print("Details of Employee 2:", employees[1])

print("Subset of first 3 employees:", employees[:3])


updated_emp2 = (102, "Ravi", 30, "IT", 75000)  
employees = (emp1, updated_emp2, emp3, emp4, emp5)  
print("Updated Employees:", employees)

new_emp1 = (106, "Sameer", 29, "Marketing", 60000)
new_emp2 = (107, "Geeta", 32, "Finance", 70000)
new_employees = (new_emp1, new_emp2)
merged_employees = employees + new_employees
print("Merged Employee Records:", merged_employees)

contract_extension = (emp3,) * 2
print("Duplicated Employee Record:", contract_extension)

departments = tuple(emp[3] for emp in employees)
print("HR department count:", departments.count("HR"))

emp_ids = tuple(emp[0] for emp in employees)
print("Index of Employee with ID 104:", emp_ids.index(104))

employees_list = list(employees)  
modified_emp5 = list(employees_list[4]) 
modified_emp5[3] = "Operations" 
employees_list[4] = tuple(modified_emp5) 
employees = tuple(employees_list)  
print("Modified Employees after Department Change:", employees)

print("Krishna Bhatia 1/23/SET/BCS/358")
