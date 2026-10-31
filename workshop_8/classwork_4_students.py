# Classwork: a list of dictionaries
#
# 1. average(students) returns the average score.
# 2. passed_names(students, pass_mark=70) returns a list of the names
#    of students whose score is at least pass_mark.

students = [
    {"name": "Nina", "score": 82},
    {"name": "Luka", "score": 78},
    {"name": "Ana", "score": 95},
]

def average(students):
    s = 0
    
    for student in students:
        s += student["score"]
    
    return s / len(students)

def passed_names(students, pass_mark=70):
    names = []
    for student in students:
        if student["score"] >= pass_mark:
            names.append(student["name"])
        
    return names
    

print(average(students))                    # 81.33333333333333
print(passed_names(students))               # ['Nina', 'Luka']
print(passed_names(students, pass_mark=90)) # ['Luka']
