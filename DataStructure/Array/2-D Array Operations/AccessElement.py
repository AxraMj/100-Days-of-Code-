import numpy as np

New2dArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(New2dArray)

def accessArray(array,row,column):
    if row>=len(array) and column>= len(array[0]):
        return "Incorrect index"
    return array[row][column]



print(accessArray(New2dArray,2,1))