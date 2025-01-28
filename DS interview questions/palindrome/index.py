class Solution:
    def isPalindrome(self,x):
        rev = 0
        original_n = x  
        while x > 0:
            lastdigit = x % 10
            rev = rev * 10 + lastdigit
            x = x // 10  
        
        if original_n == rev:
            return True
        else:
            return False

obj=Solution()
value=obj.isPalindrome(121)
print(value)
