student_score={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

for i in student_score:
    if student_score[i]>90:
        print(f"Otstanding performance {i}")
    elif student_score[i]>80:
        print(f"Exceeed expectation {i}")
    elif student_score[i]>70:
        print(f"Acceptable {i}")
    elif student_score[i]<70:
        print(f"Fail {i}")
