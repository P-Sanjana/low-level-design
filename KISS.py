def factorial(n):
    if n < 0:
        print('undefined for negative numbers')
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

import math
def factorial(n):
    if n < 0:
        print('undefined for negative numbers')
    return math.factorial(n)