def countdown(start, step=1):
    current = start
    while current >= 1:
        print(current)
        current -= step

countdown(3)
print("---")
countdown(10, 3)