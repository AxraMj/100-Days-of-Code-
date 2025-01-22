#prime number
#A number that only divisible by 1 and and itself
#eg 2 is divisible only by 1 and 2
#eg 3 is divisible by only 1 and 3
#eg 4 is not prime because it can be divisble by 1,2,4

def check_prime():
    is_prime=True
    num=int(input("Enter a number:"))
    for i in range(2,num):
        if num % i == 0:
            is_prime=False
    if is_prime:
        print("Its a prime number")
    else:
        print("Not a prime")

check_prime()