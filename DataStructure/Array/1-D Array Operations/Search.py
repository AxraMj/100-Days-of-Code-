from array import *

arr1=array("i",[10,20,30,40,60])
def searcharray(array,value):
    for i in array:
        if i==value:
            return array.index(value)
    return "Not found"
print(searcharray(arr1,40))
    