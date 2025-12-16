# violates DRY
def calculate_food_tax(price):
    tax_rate = 0.05
    return price * (1 + tax_rate)

def calculate_clothing_tax(price):
    tax_rate = 0.1
    return price * (1 + tax_rate)

def calculate_electronics_tax(price):
    tax_rate = 0.12
    return price * (1 + tax_rate)

# satisfies DRY
def calculate_tax(price, tax_rate):
    return price * (1 + tax_rate)

print(calculate_tax(100, 0.05))
print(calculate_tax(100, 0.1))
print(calculate_tax(100, 0.12))

# Another example
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b, **kwargs):
    return a + b

@logger
def multiple(a, b):
    return a * b

add(1, 2, c=3)
multiple(3, 4)