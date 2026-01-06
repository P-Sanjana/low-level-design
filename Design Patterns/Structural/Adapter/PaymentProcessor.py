from abc import ABC, abstractmethod
import uuid
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount, currency):
        pass

    @abstractmethod
    def is_payment_successful(self):
        pass

    @abstractmethod
    def get_transaction_id(self):
        pass

class InHousePaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.transaction_id = None
        self.is_payment_successful_flag = False

    def process_payment(self, amount, currency):
        print(f'InHouse Payment Processor: Processing payment of {amount} {currency}')
        self.is_payment_successful_flag = True
        self.transaction_id = str(uuid.uuid4())[:8]

    def is_payment_successful(self):
        return self.is_payment_successful_flag

    def get_transaction_id(self):
        return self.transaction_id
