# Encapsulation
# Encapsulation means bundling data and methods inside a class and controlling 
# how that data is accessed or modified.


"""
Type	           Syntax	               Meaning
Public	             name	                Accessible normally
Protected	        _name	                Intended for internal/subclass use
Private	            __name	                Name-mangled to discourage direct access
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   #__balance is a private-style attribute.

    def get_balance(self):
        return self.__balance


account = BankAccount(50000)

print(account.get_balance())


# One small Python detail: _age is a convention, not enforced protection. 
# Similarly, __marks uses name mangling.



# Getters and Setters
# Let's understand how we can access and modify private-style attributes through methods.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
    
    #getter
    def get_balance(self):
        return self.__balance

    #setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")


account = BankAccount(100000)
account.set_balance(150000)

print(account.get_balance())

account.set_balance(-500)

print(account.get_balance())
    

# Remember:
# - Getter → Retrieves a value.
# - Setter → Updates a value, optionally applying validation.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    #getter
    def get_balance(self):
        return self.__balance

    #setter
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid Balance")

    

account = BankAccount(500000)
account.set_balance(160000)
print(account.get_balance())

account.set_balance(-400)
print(account.get_balance())




