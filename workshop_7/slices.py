temperatures = [24, 25, 24, 27, 28, 30, 31, 32]

# this creates new list
print(temperatures[:], temperatures)
print(temperatures[:] == temperatures)
print(temperatures[:] is temperatures)
# print(temperatures[0:len(temperatures)])
print(temperatures[:5])
print(temperatures[5:])
print(temperatures[::2])

print(temperatures[:] is temperatures[:])

# print(id(temperatures), id(temperatures[:]))

# for temp in temperatures[0:3]:
#     print(temp)


first_days = temperatures[:3]

first_days[0] = 27

print(temperatures)
print(first_days)
