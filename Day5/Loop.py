#loop

#defintion: A loop is a sequence of instruction s that is continually repeated until a certain condition is reached.
#-------------------------------------
#for loop : A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#syntax:
# for item in list_of_items:
#     #Do this
#example:
# for number in range(1,11):
#     print(number)
#output: 1 2 3 4 5 6 7 8 9 10

#-------------------------------------
#nested loop: A nested loop is a loop inside a loop.
#syntax:
# for item in list_of_items:
#     for item in list_of_items:
#         #Do this
#example:
# for number in range(1,11):
#     for i in range(1,11):
#         print(f"{number} X {i} = {number*i}")
#output: 1 X 1 = 1
#        1 X 2 = 2
#        1 X 3 = 3
#        1 X 4 = 4
#        1 X 5 = 5
#        1 X 6 = 6
#        1 X 7 = 7
#        1 X 8 = 8
#        1 X 9 = 9
#        1 X 10 = 10

#-------------------------------------
#while loop: With the while loop we can execute a set of statements as long as a condition is true.
#syntax:
# while condition:
#     #Do this
#example:
# number=1
# while number<=10:
#     print(number)
#     number+=1
#output: 1 2 3 4 5 6 7 8 9 10

#do while loop: Python does not have a do while loop like other programming languages.