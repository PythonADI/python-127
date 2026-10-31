phones = {"Nina": "555-1234", "Luka": "555-9876"}
print(phones["Luka"])
print(len(phones))

ages = {"Nina": 19, "Luka": 22}
print(ages.get("Ana"))
print(ages.get("Ana", 0))
print("Nina" in ages)

ages["Ana"] = 21     # add
ages["Nina"] = 20    # change
print(ages)

removed = ages.pop("Luka")
print(removed, ages)
