# Nested loops: the inner loop runs fully for every pass of the outer one.

for row in range(1, 5):
    for col in range(1, 3):
        print("🟩", end="")   # 1 x 1 = 1, 1 x 2 = 2, ...
    print()                            # after each row
