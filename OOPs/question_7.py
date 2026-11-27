# Understanding super()

class Animal:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal name:", self.name)


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display_details(self):
        print(self.name, self.breed)


dog1 = Dog("Tommy", "Labrador")

dog1.display_details()