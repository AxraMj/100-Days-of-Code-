import numpy as np
New2dArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
            
traverse(New2dArray)