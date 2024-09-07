# import proper_divisor
from proper_divisor import proper_divisor
from random import random

# result = proper_divisor.proper_divisor(6)
# print(result)

# print(proper_divisor.__name__)

def is_perfect_number(number):
    divisors = proper_divisor(number)
    # _sum = sum(divisors)
    _sum = 0
    for div in divisors:
        _sum += div
        
    if _sum == number:
        return True
    return False


# if is_perfect_number(29):
#     print('Perfect number!')
# else:
#     print('Not perfect number!')

def main():
    for num in range(1, 10001):
        if is_perfect_number(num):
            print(num)
            
main()