def factorial(n):
    if n==1 or n==0:
        return 1
    elif n<0 or n!=int(n):
        return "Invalid case"
    else:
        return n*factorial(n-1)


print(factorial(34.6))