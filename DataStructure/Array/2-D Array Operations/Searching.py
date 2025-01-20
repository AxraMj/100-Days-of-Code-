import numpy as np

new_2darray=np.array([[1,2,3], [4,5,6], [7,8,9]])
def SearchElement(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return f"{value} found at position ({i}, {j})"
    return "Not founf"

print(SearchElement(new_2darray,9))