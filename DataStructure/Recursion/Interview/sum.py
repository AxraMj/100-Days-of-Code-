#sum of digits

def sum_digits(n):
    assert n==int(n) or n>0 ,'Error'
    if n==0:
        return 0
    else:
        return int(n%10) + sum_digits(int(n/10))

print(sum_digits(83))
    