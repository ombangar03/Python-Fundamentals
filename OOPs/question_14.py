# Project: Bank Management System

"""1. What are we building?
Our system will support:
1. Creating a bank account.
2. Checking account balance.
3. Depositing money.
4. Withdrawing money.
5. Displaying account details."""


# Step 1 — Create the BankAccount class
# Requirements
# Create a class called BankAccount.

# The constructor should accept:
# - account_holder
# - account_number
# - balance

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.__account_number = account_number
        self.__balance = balance


    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.__account_number)
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                return self.__balance
            else:
                print("Insufficient Balance.")
        
        else:
            print("Invalid withdrawal amount.")


account = BankAccount("Om", 123456, 50000)

account.deposit(10000)
account.withdraw(15000)
account.withdraw(60000)

account.display_details()



# Step 2 — Deposit and Withdraw money