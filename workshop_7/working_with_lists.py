# 24 25 24 27 28 30 31

temperatures = []

for i in range(int(input("How many days have you recorded: "))):
    temperatures.append(
        int(input(f"Day {i}: "))
    )

print(temperatures)

# temperatures.append(14)
# temperatures.append(13)
# temperatures.append(16)
# temperatures.append(15)
# temperatures.pop()
temperatures.pop(11)


if len(temperatures) % 2 != 0:
    temperatures.pop(len(temperatures) // 2)
else:
    # 8 // 2 -> 4
    mid = len(temperatures) // 2
    temperatures.pop(mid)
    temperatures.pop(mid - 1)
    

print(temperatures)

# print(temperatures[0])
# print(temperatures[1])
# print(temperatures[2])

s = 0
for temp in temperatures:
    print(temp)
    s += temp

print(len(temperatures))
print(s / len(temperatures))
