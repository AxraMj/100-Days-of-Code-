#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder. e.g. 86 is even because 86 + 2 = 43 with no remainder.
# 43 does not have any decimal places. 
# Therefore the division is clean. e.g. 59 is odd because 59 + 2 = 36.875 36.875 is not a whole number, 
# it has decimal places. Therefore there is a remainder of 0.875, so the division is not clean. 
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.


print("Welcome to the odd or even number checker!")
number=int(input("Enter a number: "))

if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")