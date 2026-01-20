from PaymentProcessor import StripeProcessor, PayPalProcessor
from Payment import OneTimePayment, SubscriptionPayment
if __name__ == '__main__':
    stripe = StripeProcessor()
    paypal = PayPalProcessor()

    oneTimePayment = OneTimePayment(stripe)
    subscriptionPayment = SubscriptionPayment(paypal)

    oneTimePayment.pay('$1000')
    subscriptionPayment.pay('$500')


