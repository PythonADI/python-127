# Classwork: building a list in a loop
#
# 1. evens(limit) returns a list of the even numbers from 1 to limit.
# 2. long_words(words, min_length=5) returns a new list with only the
#    words that have at least min_length letters.

def evens(limit):
    # TODO: start with [], append every even n in range(1, limit + 1)
    pass

def long_words(words, min_length=5):
    # TODO: start with [], append each word with len(word) >= min_length
    pass

words = ["sun", "apple", "kiwi", "banana", "fig"]

print(evens(10))                         # should print [2, 4, 6, 8, 10]
print(evens(1))                          # should print []
print(long_words(words))                 # should print ['apple', 'banana']
print(long_words(words, min_length=4))   # should print ['apple', 'kiwi', 'banana']
