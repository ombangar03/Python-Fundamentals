# Types of Inheritance

# Type	                        Meaning
# Single	                  One parent → one child
# Multiple	                  One child → multiple parents
# Multilevel	                Grandparent → parent → child
# Hierarchical	                 One parent → multiple children
# Hybrid	                       Combination of inheritance types

#Single inheritance

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("barking")

dog1 = Dog()
dog1.eat()
dog1.bark()

# Multiple inheritance

class Father:
    def skills(self):
        print("driving")


class Mother:

    def talent(self):
        print("cooking")

class Child(Father, Mother):
    pass


child1 = Child()
child1.skills()
child1.talent()


# Hybrid inheritance
# Hybrid inheritance is a combination of two or more inheritance types.

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class SportsCar(Car, Bike):
    pass

# This combines hierarchical and multiple inheritance.




# Multiple inheritance: One child class inherits from multiple parent classes.
# Hierarchical inheritance: Multiple child classes inherit from one parent class.

#MRO (Method Resolution Order)
# Suppose two parent classes have a method with the same name.

class Father:
    def skills(self):
        print("Father's skills")

class Mother:
    def skills(self):
        print("Mother's skills")

class Child(Father, Mother):
    pass

child = Child()
child.skills()   # output: Father's skills

# Why?
# Because Python follows the order in which parent classes are mentioned:
# Python checks Father first, then Mother.
# This lookup order is called MRO (Method Resolution Order).

# print(child.__o__


