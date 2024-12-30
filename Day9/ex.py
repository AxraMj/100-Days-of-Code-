student_score={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

grade_student={}

for i in student_score:
    if student_score[i]>90:
        grade_student[i]="Excellent"
    elif student_score[i]>80:
        grade_student[i]="Exceeed expectation"
    elif student_score[i]>70:
        grade_student[i]="Acceptable"
    elif student_score[i]<70:
        grade_student[i]="Fail"


for key in grade_student:
    print(key +":"+grade_student[key])

