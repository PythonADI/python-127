# while vs for: use for when you know the number of repeats,
# while when you repeat until something becomes true.


# if -> break


password = ""
tries = 0
is_correct = False
while not is_correct and tries < 3:
    password = input("Password: ").strip()
    is_correct = password == "python"
    tries += 1


if is_correct:  
    print("Welcome!")   # only once the user types python
else:
    print("Too many tries")