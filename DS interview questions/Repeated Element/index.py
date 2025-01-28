#a=[1,2,3,1,4,5,2]
#return 1

#b=[2,1,3,4,5,6,2,1,2]
#return 2

def RepeatedElement(array):
    seen=set()
    for i in array:
        if i in seen:
            return i
        seen.add(i)
array=[3,3,2,1,1,3,4,5,6,2,1,2]
print(RepeatedElement(array))
