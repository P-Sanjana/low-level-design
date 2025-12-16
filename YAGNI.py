# violates YAGNI
def process_payment(amount, payment_method):
    if payment_method == 'Card':
        print("Processed through card")
    elif payment_method == 'Bitcoin':
        print('Processed through bitcoin')
    elif payment_method == 'PayPal':
        print('Processes through paypal')

# satisfies YAGNI by only implementing the necessary functionality based on the current need
def process_payment(amount, payment_method):
    if payment_method == 'Card':
        print("Processed through card")
