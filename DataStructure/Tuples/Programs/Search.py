#  How to search for an element in Tuple?

t=(1,2,3,4,5)

def searchelemnt(tuple,value):
    for i in tuple:
        if i==value:
            return "Vlaue is present"
    return "Value is not found"

print(searchelemnt(t,4))