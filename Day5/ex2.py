print("Avg height of students")
height_student=input("Height of students: ").split()
for n in range(0,len(height_student)):
    height_student[n]=int(height_student[n])
print(height_student)

total_height=sum(height_student)
number_of_students=len(height_student)
avg_height=round(total_height/number_of_students)
print(f"Average height of students is {avg_height}")
