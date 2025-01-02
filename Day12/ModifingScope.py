#modifing scope of variable

values=5
def scope():
    global values
    values +=1
    print(values)
scope()

#simple ways to do the above code
values=20
def scope():
    return values+1
output=scope()
print(output)