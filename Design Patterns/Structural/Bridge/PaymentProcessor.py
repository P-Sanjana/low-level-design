from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class StripeProcessor(PaymentProcessor):
    def process(self, amount):
        print(f'Processing {amount} through Stripe')

class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        print(f'Processing {amount} through PayPal')
