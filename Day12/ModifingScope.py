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

#global scope is maily used to modify the value of the variable in the global scope
#global scope is mainly used for constants like pi=3.14, 
#                                               url="www.google.com" , 
#                                               social security number , 
#                                               social media username etc