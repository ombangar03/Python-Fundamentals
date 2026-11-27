# Your next exercise
# Create these two classes:

# Parent class: Person
# - Constructor accepts name and age.
# - Method display_person() prints name and age.
# Child class: Employee
# - Inherits from Person.
# - Constructor accepts name, age, and salary.
# - Use super() to initialize name and age.
# - Store salary using self.
# - Method display_employee() prints all three details.
# Create one employee object:


class Person:

    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def display_person(self):
        print(self.name, self.age)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_employee(self):
        print(self.name, self.age, self.salary)


emp1 = Employee("Om", 24, 45000)

emp1.display_employee()

