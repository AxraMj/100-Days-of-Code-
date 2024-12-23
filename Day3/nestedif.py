#Nested if statement
# if condition1: 
#     if Another condition:
#         statement(s)
#     else:
#       statement(s)
# else:
#   statement(s)


print("Welcome to rollercoaster ride!!")
height=int(input("What is your height in cm?"))


if height >= 120:
    age=int(input("What is your age?"))
    if age >= 18:     
        print("please pay $7")
    else:
        print("please pay $5")
else:
    print("Sorry, you have to grow taller before you can ride.")



