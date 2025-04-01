class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")


emp1 = Employee("John Doe", 30, "E123", 50000)
emp1.display_info()
print("1/23/SET/BCS/358")
