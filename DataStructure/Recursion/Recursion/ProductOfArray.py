def ProductOfArray(array):
    if len(array)==0:
        return 1
    return array[0] * ProductOfArray(array[1:])



output=ProductOfArray([1,2,3])
print(output)