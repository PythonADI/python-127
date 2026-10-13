# Classwork: return early
#
# 1. divide(a, b) returns a / b, or None when b is 0.
# 2. first_multiple(number, limit) loops over range(1, limit + 1) and
#    returns the first n that divides evenly by number, or None if
#    there is none.

def divide(a, b):
    # TODO: return None if b is 0, otherwise a / b
    pass

def first_multiple(number, limit):
    # TODO: return the first n in range(1, limit + 1) with n % number == 0
    pass

print(divide(10, 4))           # should print 2.5
print(divide(10, 0))           # should print None
print(first_multiple(7, 30))   # should print 7
print(first_multiple(40, 30))  # should print None
