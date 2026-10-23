"""
x - secret number (0, 100)

user will tell number and our program should them higher or lower
"""
import random

x = random.randint(0, 100)
count = 0


while True:
    count += 1
    user_guess = int(input("Guess: "))
    if user_guess > x:
        print("Lower")
    elif user_guess < x:
        print("Higher")
    else:
        print(f"Correct ({count} guesses)")
        break
