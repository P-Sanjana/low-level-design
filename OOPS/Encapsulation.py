class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}.")
        else:
            print(f"Invalid amount.")

    def __can_withdraw(self, amount):
        return 0 < amount <= self.__balance

    def withdraw(self, amount):
        if self.__can_withdraw(amount):
            self.__balance -= amount
            print(f"Withdrawn {amount}.")
        else:
            print(f"Insufficient/Invalid amount.")

    def get_balance(self):
        print(f"Balance: {self.__balance}")

class Employee:
    def __init__(self):
        self.__name = ''
        self.__age = ''

    def get_name(self):
        return self.__name

    def set_name(self, name1):
        self.__name = name1

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


acc = BankAccount("Sanjana", 1000)
acc.get_balance()
acc.deposit(200)
acc.get_balance()
acc.withdraw(200)
acc.get_balance()

# emp = Employee()
# emp.set_name("Sanjana")
# emp.set_age(25)
# print(f"Name: {emp.get_name()}")
# print(f"Age: {emp.get_age()}")