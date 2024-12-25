#forloop
#Average height 
#instructions
#You are going to write a program that calculates the average student height from a List of heights.
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#e.g.
#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#There are a total of 7 heights in student_heights
#1146 ÷ 7 = 163.71428571428572
#Average height rounded to the nearest whole number = 164

print("Avg height of students")
height_student=input("Height of students: ").split()
for n in range(0,len(height_student)):
    height_student[n]=int(height_student[n])
print(height_student)

sum=0
for height in height_student:
    sum+=height
print(f"Sum of heights is {sum}")

length=0
for student in height_student:
    length+=1
print(f"Number of students is {length}")

avg_height=round(sum/length)
print(f"Average height of students is {avg_height}")

    