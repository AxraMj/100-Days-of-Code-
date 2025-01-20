import numpy as np

new_2darray=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(new_2darray)
delete_array=np.delete(new_2darray,0,axis=0)
print(delete_array)