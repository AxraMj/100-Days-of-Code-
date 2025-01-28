class Solution:
    def containsDuplicate(self, array):
        seen=set()
        for i in array:
            if i in seen:
                return True
            seen.add(i)
        return False

obj=Solution()
array=[1,2,3]
print(obj.containsDuplicate(array))
        