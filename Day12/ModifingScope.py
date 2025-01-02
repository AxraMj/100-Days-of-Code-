#modifing scope of variable

values=5

def scope():
    global values
    values +=1
    print(values)


scope()