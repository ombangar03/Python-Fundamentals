"""Create a class called Employee.

Requirements:
1. Class variable: company = "TCS".
2. Constructor accepts name and salary.
3. Instance method display() prints employee details.
4. Class method change_company() changes the company name.
5. Static method is_valid_salary() checks whether salary is greater than zero.
Create two employee objects and test all three methods."""


class Employee:
    company = "TCS"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(self.name, self.salary)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

emp1 = Employee("Ravi", 40000)
emp1.display()
emp2 = Employee("Rahul", 30000)
emp2.display()


Employee.change_company("Google")
print(Employee.company)

print(Employee.is_valid_salary(40000))
