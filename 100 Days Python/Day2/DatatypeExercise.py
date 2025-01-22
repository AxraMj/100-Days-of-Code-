# Instructions Write a program that adds the digits in a 2 digit number, 
# e.g. if the input was 35, then the output should be 3 + 5 = 8 Warning. 
# Do not change the code on lines 1-3. Your program should work for different inputs, e.g. any two-digit number.

num=input("Enter any 2 digit numbers:")
print(type(num))

print(int(num[0])+int(num[1]))