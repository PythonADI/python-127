text = "heello worldd"
letter_count = {}
result = []

for letter in text:
    letter_count[letter] = letter_count.get(letter, 0) + 1

for letter, repetition in letter_count.items():
    if repetition == 2:
        result.append(letter)

print(result)