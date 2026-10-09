secret = "27g"  # hard coded
while True:
    password = input("Enter Password: ")

    if password == secret:
        print("Welcome")
        break
    else:
        print("Password is incorrect")

print("Loop ended!")
print("Loading Dashboard...")
