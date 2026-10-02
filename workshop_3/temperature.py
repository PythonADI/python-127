# Chained comparisons for a range, plus a one-line conditional expression.

temperature = 22

if 18 <= temperature <= 25:
    print("Comfortable.")       # Comfortable.
else:
    print("Not comfortable.")

# Exactly the same condition, written out in full:
print(18 <= temperature and temperature <= 25)   # True

# A conditional expression picks a value in one line.
advice = "take a jacket" if temperature < 18 else "go as you are"
print(f"Today: {advice}")       # Today: go as you are

label = "warm" if temperature >= 25 else "mild"
print(f"{temperature} degrees is {label}.")   # 22 degrees is mild.
