#for unlimited keyword arguments we use **kwargs
def calculate(n,**kwargs):
    print(type(kwargs)) #<class 'dict'>
    print(kwargs) #{'add': 1, 'mul': 2}
    print(kwargs["mul"]) #to get value #output 2
    n+=kwargs["add"]
    n+=kwargs["mul"]
    print(n) #5


calculate(2,add=1,mul=2)