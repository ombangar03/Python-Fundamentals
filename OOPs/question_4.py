# Lesson 4: Instance Methods, Class Methods and Static Methods

# Instance methods
# Class methods
# Static methods

#instance methods within class

class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


emp1 = Employee("Rahul")
emp1.display()


# class method: works within class-level data. it takes cls as first 
#parameter and uses @classmethod

class Employees:
    company = "Google"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


Employees.change_company("Microsoft")
print(Employees.company)

#Static method: doesn't automatically receive self or cls. it is useful for
# utility operations related to the class

class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))  