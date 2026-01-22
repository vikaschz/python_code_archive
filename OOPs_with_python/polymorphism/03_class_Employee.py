"""Create a base class Employee with calculate_salary(). Derive FullTimeEmployee, PartTimeEmployee, and ContractEmployee. Demonstrate runtime polymorphism."""
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclass must implement calculate_salary()")

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class ContractEmployee(Employee):
    def __init__(self, name, contract_amount):
        super().__init__(name)
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount

def show_salary(emp: Employee):
    print(emp.name, "salary:", emp.calculate_salary())

employees = [
    FullTimeEmployee("Aman", 50000),
    PartTimeEmployee("Rohit", 400, 80),
    ContractEmployee("Neha", 70000)
]

for e in employees:
    show_salary(e)

