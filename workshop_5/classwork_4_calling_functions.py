# Classwork: one function calling another
#
# Write is_even(number), which returns True if number is even.
# Then write count_evens(limit), which loops over range(1, limit + 1)
# and uses is_even to count how many of those numbers are even.

def is_even(number):
    return number % 2 == 0

def count_evens(limit):
    # TODO: loop over range(1, limit + 1), use is_even to count the
    # even ones, and return that count
    count = 0
    for number in range(1, limit + 1):
        if is_even(number):
            count += 1
            print(f"{number = }")
    return count

print(count_evens(6))    # should print 3  (2, 4, 6)
print("---")
print(count_evens(11))   # should print 5  (2, 4, 6, 8, 10)
