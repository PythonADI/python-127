# Counting with a condition inside the loop.
# მომხმარებელი გეტყვით სიტყვას - (input -ით უნდა კითხოთ)
# თქვენ უნდა უთხრათ რამდენი თანხმოვანია ამ სიტყვაში

word = input("enter a word").lower()
consonants = 0
for letter in word:
    if letter not in "aeiou":
        consonants += 1

print(f"onsonants: {consonants}")