from array import *

arr1=array("i",[10,20,30,40,50])
print(arr1[3])

#to avoid this error IndexError: array index out of range
def accessElement(array,index):
    if index>=len(array):
        return "Element not in array"
    return array[index]

print(accessElement(arr1,10)) #Element not in array
print(accessElement(arr1,1)) #Element not in array
