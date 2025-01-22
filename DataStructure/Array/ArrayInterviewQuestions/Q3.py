#How to check if an array contains a number in python(find weather a value presnt in array)

import numpy as np

myarray=np.array([1,2,3,4,5,6,7])

def findValue(array,value):
    for i in range(len(array)):
        if array[i] == value:
             return "Value is present in Array"
    return "No Such value Present"
    
print(findValue(myarray, 3))