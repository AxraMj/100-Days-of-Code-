import numpy as np

New2DArray=np.array([[1,2,3], [5,6,7], [8,9,10]])
print(New2DArray)
inseted_array=np.insert(New2DArray,0,[12,34,56], axis=1)
print(inseted_array)