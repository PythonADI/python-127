# Cinema entry: if, if/else, and/or/not, and nesting vs a single 'and'.

AGE_LIMIT = 18

age = 25
has_ticket = True

if age >= AGE_LIMIT:
    print("Old enough.")             # Old enough.

if age >= AGE_LIMIT and has_ticket:
    print("Enjoy the film.")
else:
    print("You can't come in.")      # You can't come in.

if age < AGE_LIMIT or not has_ticket:
    print("Check your age and your ticket.")   # Check your age and your ticket.

# Nesting costs an extra level, but it can say *which* part failed.
if age >= AGE_LIMIT:
    if has_ticket:
        print("Enjoy the film.")
    else:
        print("Please buy a ticket first.")    # Please buy a ticket first.
else:
    print("This film is 18+.")
