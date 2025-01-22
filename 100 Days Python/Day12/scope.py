##################### Scope ##############################

a=10 #global scope: outside the function

def sum():
    b=10 #local scope : inside the function
    print(a+b)

sum()
print(a)
# print(b) # This will throw an error because b is not defined in the global scope

def functions():
    if a>=10:
        c=20 #global scope
        print(c)

functions()