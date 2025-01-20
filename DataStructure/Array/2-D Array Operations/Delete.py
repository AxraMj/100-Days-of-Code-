import numpy as np

new_2darray=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(new_2darray)
delete_array=np.delete(new_2darray,0,axis=1) #axist 0 means row and 1 means column
print(delete_array)