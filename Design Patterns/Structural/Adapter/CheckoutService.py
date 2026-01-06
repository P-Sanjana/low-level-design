class CheckoutService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def checkout(self, amount, currency):
        print(f'Checking out...')
        self.payment_processor.process_payment(amount, currency)
        if self.payment_processor.is_payment_successful():
            print(f'Payment successful, transaction id: {self.payment_processor.get_transaction_id()}')
        else:
            print(f'Payment unsuccessful')

