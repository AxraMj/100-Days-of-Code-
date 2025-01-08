def fibnocci(n):
    if n in [0,1]:
        return n
    elif n!=int(n) or n<0:
        return "Invalid case"
    else:
        return fibnocci(n-1)+fibnocci(n-2)

print(fibnocci(2.4))



#f(n)=f(n-1)+f(n-2)
#f(0)=0
#f(1)=1