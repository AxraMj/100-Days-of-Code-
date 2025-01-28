#array=[1,2,3,4] target=10
#array-[1,2,3,5,5] target =10

#brute force approach
# def TwoSum(array,target):
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#             if array[i] + array[j] == target:
#                 return f"{array[i]}, {array[j]}"
#     return False

# array=[1,2,3,5,5]
# print(sumelement(array,5)) time is O(n ^ 2)

#better solution

# def TwoSum(array, target):
#     seen = set()
#     for i in range(len(array)):
#         value = target - array[i]  
#         if value in seen:
#             return f"{value},{array[i]}" 
#         seen.add(array[i])  

# array = [1, 2, 4, 3, 5]
# print(sumelement(array, 7))  

#write it using class
class TwoSum:
     def TwoSum(self,array, target):
        seen = set()
        for i in range(len(array)):
            value = target - array[i]  
            if value in seen:
                return [array.index(value), i] 
            seen.add(array[i])  
        
obj=TwoSum()
array = [2,7,11,15]
print(obj.TwoSum(array,9))
