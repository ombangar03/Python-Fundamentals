# Lesson 3: Instance Variables vs Class Variables

class Employees:

    company = "Google"  #class variable

    def __init__(self, name, salary):
        self.name = name # instance varaible
        self.salary = salary 

    def display_details(self):
        print(self.name, self.salary)


emp1 = Employees("Rahul", 50000)
emp2 = Employees("Ravi", 60000)

print(emp1.company)
print(emp2.company)

print(emp1.name)
print(emp2.name)


# Instance variable	                       Class variable
# Belongs to an individual object	        Shared through the class
# Usually defined using self	             Defined directly inside the class
# Each object can have different value	     Common value for all objects



class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Rahul")
emp2 = Employee("Ravi")

emp1.company = "Microsoft"

print(emp1.company)
print(emp2.company)
print(Employee.company)




# Instance variable
# - Belongs to an individual object.
# - Usually created inside __init__() using self.
# - Each object can have its own value.

class Employee:
    def __init__(self, name): 
        self.name = name  # instance varaible 


# Class variable
# - Belongs to the class.
# - Defined directly inside the class, outside methods.
# - Shared by objects unless an instance overrides it.
class Employee:
    company = "Google"    # class varaible

    def __init__(self, name):
        self.name = name


class Bike:
    wheels = 2

    def __init__(self, brand):
        self.brand = brand

bike1 = Bike("KTM")
bike2 = Bike("Royal Enfield")