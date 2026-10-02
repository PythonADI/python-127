# INTERACTIVE: a stripped input() used directly as a condition (truthiness).

name = input("რა გქვია?\n").strip()

if name:
    print(f"Hello, {name.title()}!")
else:
    print("You didn't type a name.")

# An empty string is falsy, so just pressing Enter lands in the else.
print(f"{bool(name) = }")

