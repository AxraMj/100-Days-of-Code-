#congratulations, you have got a job at python pizza. 
# Your first job is to build an automatic pizza order program. 
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

print("Welcome to Python Pizza!!")
print("Enter your choice:")
print("1. Small Pizza")
print("2. Medium Pizza")
print("3. Large Pizza")
choice=int(input())

bill=0
if choice==1:
    bill=15
    print("You have selected Small Pizza")
elif choice==2:
    bill=20
    print("You have selected Medium Pizza")
elif choice==3:
    bill=25
    print("You have selected Large Pizza")
else:
    print("Invalid choice")
    exit()

add_pepperoni=input("Do you want to add pepperoni? (yes/no)")
if add_pepperoni=="yes":
    if choice==1:
        bill=bill+2
    else:
        bill=bill+3
    print("Pepperoni added")

extra_cheese=input("Do you want to add extra cheese? (yes/no)")
if extra_cheese=="yes":
    bill=bill+1
    print("Extra cheese added")

print("Your final bill is:",bill)

