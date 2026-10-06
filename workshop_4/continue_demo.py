# continue skips the rest of THIS pass and carries on with the next.

for number in range(1, 6):
    if number == 3:
        continue
    print(number)   # 1, 2, 4, 5 - the 3 is skipped
