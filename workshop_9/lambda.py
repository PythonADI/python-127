students = [
    {
        "name": "Nika",
        "score": 78
    },
    {
        "name": "Nia",
        "score": 88
    },
    {
        "name": "Marry",
        "score": 92
    },
    {
        "name": "George",
        "score": 62
    },
]


def sudent_key(a):
    return a["score"]

students.sort(key=lambda a: a["score"], reverse=True)

for student in students:
    print(student["name"], student["score"])
