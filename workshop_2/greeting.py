# Ask for the user's name and age, clean up the input, and greet them.

name = input("What is your name?\n").strip()
age = int(input("რამდენი წლის ხარ?\n"))

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'> — because we cast it

print(f"Hello, {name.title()}!\nYou are {age} years old.")
print(f"In 5 years you will be {age + 5}.")
print(f"Your name has {len(name)} letters: {name.upper()}")
