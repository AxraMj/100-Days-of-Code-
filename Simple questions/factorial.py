# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact * i #1*1=1 1*2=2 
#     return fact
# print(factorial(6))

def factorial(n):
    if n in [0,1]:
        return 1
    return n * factorial(n-1)

print(factorial(1))
