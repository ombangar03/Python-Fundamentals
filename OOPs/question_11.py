# Polymorphism
# This is the fourth major pillar of OOP.

# Polymorphism means one interface, multiple forms of behaviour.

class Dog:
    def sound(self):
        print("Dog braks")

class Cat:
    def sound(self):
        print("Cat meow")

class Cow:
    def sound(self):
        print("Cow moos")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

print("-----------------------------------------------------------")

class CreditCard:
    def pay(self):
        print("Payment made using Credit Card")

class UPI:
    def pay(self):
        print("Payment made using UPI")

class Cash:
    def pay(self):
        print("Payment made using Cash")

payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    payment.pay()


# One more important concept: Method Overriding
# Method overriding happens when a child class provides its own implementation of a 
# method already defined in its parent class.

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog bark")

class Cat(Animal):
    def sound(self):
        print("Cat meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()