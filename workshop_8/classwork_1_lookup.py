# Classwork: looking things up
#
# 1. Create a dictionary `capitals` with three countries as keys and
#    their capitals as values (e.g. "Georgia": "Tbilisi").
# 2. Write capital_of(country) that returns the capital, or
#    "Unknown" if the country is not in the dictionary. Use .get().

capitals = {
    "Georgia": "Tbilisi",
    "Hungary": "Budapest",
    "Germany": "Berlin",
}

def capital_of(country):
    return capitals.get(country, "Unknown")
    # if country not in capitals:
    #     return "Unknown"
    # return capitals[country]

print(capital_of("Georgia"))  # should print Tbilisi
print(capital_of("Narnia"))   # should print Unknown
