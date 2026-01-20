class Payment:
    def __init__(self, paymentProcessor):
        self.paymentProcessor = paymentProcessor

    def pay(self, amount):
        self.paymentProcessor.process(amount)

class OneTimePayment(Payment):
    def pay(self, amount):
        super().pay(amount)

class SubscriptionPayment(Payment):
    def pay(self, amount):
        super().pay(amount)
