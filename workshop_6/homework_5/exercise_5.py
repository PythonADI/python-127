"""

17


n % 2 != 0
n % 3 != 0
n % 4 != 0
n % 5 != 0
n % 6 != 0


"""
import math
n = 1273245

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


print(is_prime(n))
