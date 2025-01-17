def add(*args):
    print(args[0])
    sum=0
    for n in args:
        sum+=n
    return sum
    

print(add(1,2,5,6,10,1))