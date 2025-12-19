# violates open-closed principle
class Payment:
    def ___init__(self, card_number, account_number):
        self.card_number = card_number
        self.account_number = account_number

    def pay(self, payment_mode):
        if payment_mode == 'Card':
            print("Payment done with card")
        elif payment_mode == 'Bank account':
            print("Payment done with bank account")

# satisfies OCP
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class Card(Payment):
    def pay(self):
        print("Payment done with card")

class BankAccount(Payment):
    def pay(self):
        print("Payment done with bank account")