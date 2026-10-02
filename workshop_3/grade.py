# Turn a score into a grade with an elif ladder — and why the order matters.

score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
# Grade: C  — Python stops at the first True condition

# The same ladder written the wrong way round: every passing score gets a C.
score = 95

if score >= 70:
    print("Grade: C")      # Grade: C  — 95 >= 70 is already True
elif score >= 90:
    print("Grade: A")      # never reached
