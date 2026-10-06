# Accumulating a total: a variable that survives across iterations.

total = 0
for number in range(1, 5):
    total += number
    print(f"added {number}, total is now {total}")

print(f"Final total: {total}")   # Final total: 10
