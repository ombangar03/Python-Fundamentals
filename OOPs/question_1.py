"""Object-Oriented Programming (OOP)
1. What is OOP?
OOP is a programming approach where we organize code using classes and objects."""

# A motorcycle has:
# - Properties: brand, model, color, speed.
# - Behaviours: start, stop, accelerate, brake.

# What is a class and an object?
# Class: A blueprint or template used to create objects.

# Object: An actual instance created from a class.

class Bike:
    def start(self):
        print("Bike started")

bike1 = Bike()

bike1.start()

# class Bike: defines a class.
# def start(self): defines a method (a function inside a class).
# bike1.start() calls that method using an object.

# Requirements:
# 1. Create a method called start().
# 2. Print "Car started".
# 3. Create an object called car1.
# 4. Call the start() method using that object.

# understanding __init__() and self

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print(self.brand, self.model)

car1 = Car("BMW", "M4")
car2 = Car("Tata", "Nexon")

car1.display()
car2.display()

"""1. __init__()
- It is a special method called a constructor.
- Python automatically calls it when you create an object.
- It initializes the object's attributes.
2. self
- It refers to the current object.
- self.brand stores the brand belonging to that particular object.
- self.model stores its model.

"""
