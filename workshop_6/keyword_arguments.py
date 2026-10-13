def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe("Nina", 25, "Tbilisi")
describe(city="Batumi", name="Luka", age=30)
describe("Nina", city="Kutaisi", age=25)

def make_tea(sugar=1, milk=False, lemon=False):
    print(f"sugar={sugar}, milk={milk}, lemon={lemon}")

make_tea(lemon=True)
