"""
# Abstraction
# This is the fourth major pillar of OOP, 
# along with inheritance, encapsulation and polymorphism.


# abstraction means hiding the implementation details and exposing only
# the essentials functionality

You interact with the essential functionality without dealing with the internal complexity.
That's abstraction."""

# Python provides the abc module (Abstract Base Classes)
# We mainly use:
# - ABC — Creates an abstract base class.
# - @abstractmethod — Defines a method that child classes must implement.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Bike:

    def start(self):
        print("Bike Started")

class Car:

    def start(self):
        print("Car Started")

bike = Bike()
car = Car()
# vehicle = Vehicle()  TypeError

bike.start()
car.start()

# @abstractmethod
# def start(self):
#     pass

# This declares that every concrete child class must implement start().

# Both Bike and Car provide their own implementation of start()



"""
Inheritance:	                                 
Reuses parent class functionality	          
Uses parent-child relationships	                
Helps code reusability	                       

Abstraction:
Defines required functionality while hiding implementation details.
Uses abstract classes and methods
Helps enforce a common interface

"""
from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class Credit(Payment):
    def pay(self):
        print("Payment processed through Credit Card")

class UPI(Payment):
    def pay(self):
        print("Payment processed through UPI")

credit = Credit()
upi = UPI()

credit.pay()
upi.pay()


"""Remember this interview point
An abstract class cannot be instantiated while it has unimplemented abstract methods. 
A concrete child class must implement all inherited abstract methods."""