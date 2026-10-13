

def count_vowels(word):
    total = 0
    for letter in word.lower():
        if letter in "aeiou":
            total += 1
    return total
    

word = "Titan"
print(count_vowels(word))

word = "Lexo"
print(count_vowels(word))
print(count_vowels("Hurricane"))