PASS_BOUNDARY = 51

student = {
    "name": "Nika",
    "test": False,
    "subjects": [
        {
            "name": "Math 101",
            "score": 78
        },
        {
            "name": "CS 401",
            "score": 41
        },
        {
            "name": "English 1",
            "score": 98
        },
        {
            "name": "CS 402",
            "score": 60
        }
    ]
}

for subject in student["subjects"]:
    subject["pass"] = subject["score"] >= PASS_BOUNDARY


student["name"] = "Nikoloz"
print(student["name"])
print(student)
student.pop("test")
print(student)

print(len(student["subjects"]))
passed_subjects = []
for subject in student["subjects"]:
    if subject["pass"]:
        passed_subjects.append(subject)
        

for subject in passed_subjects:
    print(subject["name"], subject["score"])