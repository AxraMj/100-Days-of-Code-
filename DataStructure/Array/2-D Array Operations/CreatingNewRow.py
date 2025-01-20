import numpy as np

new_2darray=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(new_2darray)
row_updated_array=np.insert(new_2darray,2,[10,20,30],axis=0)
print(row_updated_array)