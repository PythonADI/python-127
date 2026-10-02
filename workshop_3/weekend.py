# The 'or' trap: each side of 'or' needs a complete condition of its own.

day = "monday"

# WRONG — Python reads this as (day == "saturday") or ("sunday"),
# and "sunday" is a non-empty string, so it is always truthy.
if day == "saturday" or "sunday":
    print("Weekend! (wrong - prints on monday too)")
    # Weekend! (wrong - prints on monday too)

# Correct: spell out both comparisons.
if day == "saturday" or day == "sunday":
    print("Weekend!")
else:
    print("A work day.")        # A work day.

day = "sunday"
if day == "saturday" or day == "sunday":
    print("Weekend!")           # Weekend!

# 'not' flips a condition.
print(not (day == "sunday"))    # False
