#How to find maximum product of two integers in the array where all element are possitive
import numpy as np
myarray=np.array([1,2,45,66,23,12,1,34,78,9])


def function(array):
    maxProduct=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j]>maxProduct:
                maxProduct=array[i] *array[j]
                pairs=str(array[i]) + "," +str(array[j])
    print(pairs)
    print(maxProduct)
                


function(myarray)