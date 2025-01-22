#Highest Score 
# Instructions 
# You are going to write a program that calculates the highest score from a List of scores. 
# e.g. student scores (78, 85, 85, 86, 55, 91, 54, 891 Important you are not allowed to use the max or min functions.
#  The output words must match the example. i.e The highest score in the class list x

print("Welcome to the Highest Score Calculator")
score=input("Enter the scores of the students separated by commas: ").split(", ")
for n in range(0,len(score)):
    score[n]=int(score[n])
print(score)

height_score=0
for maxscore in score:
    if maxscore > height_score:
        height_score=maxscore
print(height_score)