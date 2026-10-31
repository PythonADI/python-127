sentence = "banana is in the deep stash of dark forest"

"""
b: 1
a: 3
n: 2
 : 1
i: 1
s: 1

"""

letter_counts = {}

for letter in sentence:
    if letter == " ":
        continue
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)

letters = list(letter_counts.keys())
letters.sort()

for letter in letters:
    print(f"{letter}: {letter_counts[letter]}")
