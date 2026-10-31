names = ["Nia", "Marry", "George", "Nick", "George"]
x = "George"


# for i, name in enumerate(names):
#     print(f"{i} - {name}")

for i, name in enumerate(names):
    if name == x:
        print(f"Found it at {i} index")
        break

print(x in names)