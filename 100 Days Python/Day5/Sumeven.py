#Instructions You are going to write a program that calculates the sum of all the even numbers from 1 to 100, 
# including 1 and 100. eg.2+4+6+8+10...+98 +100 Important, 
# there should only be 1 print statement in your console output. 
# It should just print the final total and not every step of the calculation.
#  Hint 
# 1. There are quite a few ways of solving this problem, 
# but you will need to use the range() function in any of the solutions.

print("Sum of even numbers from 1 to 100")
sum=0
for n in range(2,101,2):
    sum += n
print(sum)
    
