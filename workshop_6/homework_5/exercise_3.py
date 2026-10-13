def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"

    return "F"
        

for score in range(60, 101, 10):
    print(f"{score}: {grade(score)}")