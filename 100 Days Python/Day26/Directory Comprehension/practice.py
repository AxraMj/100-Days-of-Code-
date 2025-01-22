import random
students={
    "Alex":89,
    "Beth":98,
    "Akash":21,
    "Avinash":89
    }

student_score={student:random.randint(1,100) for student in students}
print(student_score)

#passed_students={new_key:new_value for (key,value) in dictionary.tems() }
passed_students={student:score for (student,score) in student_score.items() if score >= 60 }
print(passed_students)