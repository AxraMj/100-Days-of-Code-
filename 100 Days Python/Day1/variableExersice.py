# Instructions Write a program that switches the values stored in the variables a and b 
# Warning. 
# Do not change the code on lines 1-4 and 15-18. Your program should work for different inputs, 
# e.g. any value of a and b.

a=input("a:")
b=input("b:")

print("After swap")

temp=a
a=b
b=temp

print("a= " +a)
print("b= " +b)