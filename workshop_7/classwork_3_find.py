# Classwork: finding an element
#
# Write these yourself with a loop and an early return. Do not use
# `in`, .index() or .count() for this exercise.
#
# 1. contains(items, target) returns True if target is in the list,
#    otherwise False.
# 2. position(items, target) returns the index of the first match, or
#    None if there is none. Loop over range(len(items)).

def contains(items, target):
    # TODO: return True the moment an item == target; False after the loop
    pass

def position(items, target):
    # TODO: return i the moment items[i] == target; None after the loop
    pass

fruits = ["apple", "pear", "plum", "pear"]

print(contains(fruits, "plum"))   # should print True
print(contains(fruits, "kiwi"))   # should print False
print(position(fruits, "pear"))   # should print 1
print(position(fruits, "kiwi"))   # should print None
