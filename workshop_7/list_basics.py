scores = [90, 75, 82]
print(scores)
print(len(scores))

names = ["Nina", "Luka", "Ana"]
print(names[0])
print(names[2])
print(names[-1])

names[1] = "Giorgi"
print(names)

cart = ["bread", "milk"]
cart.append("cheese")
cart.insert(0, "water")
print(cart)

cart.remove("milk")
last = cart.pop()
print(last)
print(cart)
