#array1=[1,2,3,4]
#array2=[9,5,4,6]
#same value return true
#else return false

#brute force approach
        # def function(array1,array2):
        #     for i in array1:
        #         for j in array2:
        #             if i==j:
        #                 return True
        #     return False

        # array1=[12,22,25,27]
        # array2=[13,77,55,22]
        # print(function(array1,array2)) #time is O(n ^ 2)

#better case
def function(array1,array2):
    seen=set(array1)
    for i in array2:
        if i in seen:
            return True
    return False

array1=[12,22,25,27]
array2=[13,77,55,22]
print(function(array1,array2)) #time is O(n)
