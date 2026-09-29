# Booleans, comparisons, and truthiness.

age = 20
print(f"{age >= 18 = }")     # age >= 18 = True
print(type(age >= 18))       # <class 'bool'>

# Numbers: zero is False, everything else is True
print(f"{bool(0) = }")
print(f"{bool(-5) = }")
print(f"{bool(0.001) = }")

# Strings: empty is False, anything else is True
print(f"{bool('') = }")
print(f"{bool(' ') = }")
print(f"{bool('0') = }")
print(f"{bool('False') = }")

# Floats aren't exact
print(0.1 + 0.2)               # 0.30000000000000004
print(0.1 + 0.2 == 0.3)        # False
print(round(0.1 + 0.2, 2) == 0.3)  # True

print((10 + 20) / 100)
