print("Welcome to wonderla!!")
print("Enter your choice:")
print("1. Roller coaster")
print("2. Water rides")
print("3. Kids rides")
choice=int(input())
bill=0
if choice==1:
    age=int(input("Enter your age:"))
    if age>=18:
        print("You are eligible for the ride")
        if age < 25:
            bill=500
            print("You need to pay 500")
        else:
            bill=1000
            print("You need to pay 1000")
    elif age<18:
        print("You are not eligible for the ride")

    print("Photo session is available for 100")
    photo=input("Do you want to take photo? (yes/no)")
    if photo=="yes":
        print("Photo is taken")
        bill=bill+100
        print("Your total bill is",bill)




    


