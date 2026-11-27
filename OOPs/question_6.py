# Inheritance: allows one class to reuse properties and methods from another class.abs
# e.g parent class Vehicle: child class: Bike, Car

class Vehicle:

    def start(self):
        print("Vehicle Started")

    def stop(self):
        print("Vehicle Stopped")


class Bike(Vehicle):

    def ride(self):
        print("bike is running")


bike1 = Bike()

bike1.start()
bike1.ride()
bike1.stop()


# Your first inheritance exercise
# Create a parent class called Animal.

# Requirements:
# 1. Create a method eat() that prints "Animal is eating".
# 2. Create a method sleep() that prints "Animal is sleeping".
# Now create a child class called Dog that inherits from Animal.
# 3. Add a method bark() that prints "Dog is barking".
# 4. Create an object of Dog.
# 5. Call all three methods.


class Animal:

    def eat(self):
        print("Animal is eating")
    
    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.bark()
dog1.sleep()