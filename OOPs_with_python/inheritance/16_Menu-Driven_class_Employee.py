"""
1. Menu-Driven Employee System
Create a base class Employee.
Derived classes: FullTimeEmployee, PartTimeEmployee.
Use method overriding for salary calculation.
Menu options:
1. Enter employee details
2. Calculate salary
3. Exit
"""


class Employee:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


emp = None

while True:
    print("\n1. Enter employee details")
    print("2. Calculate salary")
    print("3. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        t = input("Type (full/part): ")
        if t == "full":
            emp = FullTimeEmployee(float(input("Salary: ")))
        elif t == "part":
            emp = PartTimeEmployee(int(input("Hours: ")), float(input("Rate: ")))
    elif ch == 2:
        if emp:
            print("Salary:", emp.calculate_salary())
        else:
            print("No employee")
    elif ch == 3:
        break
