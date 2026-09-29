# A tip calculator: input, casting, floats, round(), and a constant.

TIP_RATE = 0.1

bill = float(input("Bill total (GEL): "))
tip = bill * TIP_RATE
total = bill + tip



print(f"Tip:\t{round(tip, 2)} GEL")
print(f"Total:\t{round(total, 2)} GEL")
