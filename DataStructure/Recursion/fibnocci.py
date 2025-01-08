def fibnocci(n):
    assert n>=0 and int(n)==n,'Finocci cannot be neagtive or non integer'
    if n in [0,1]:
        return n

    else:
        return fibnocci(n-1)+fibnocci(n-2)

print(fibnocci(2.4))



#f(n)=f(n-1)+f(n-2)
#f(0)=0
#f(1)=1