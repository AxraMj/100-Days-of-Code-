class Solution:
    def __init__(self,max_size):
        self.stack=[]
        self.max_size=max_size


    def is_empty(self):
        return len(self.stack)==0
    def is_full(self):
        return len(self.stack)>= self.max_size
    
    def push(self,item):
        if self.is_full():
            return f"Stack is full cannot insert {item}"
        else:
            self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty!! Nothing to Pop"
        else:
            poped_item=self.stack.pop()
            return poped_item
        
    def Traverse(self):
        if self.is_empty():
            return "Stack is empty!!!"
        else:
            for i in self.stack:
                print(i)
        
    def peek(self):
        return self.stack[-1]
obj=Solution(5)
obj.push(10)
obj.push(20)
obj.push(30)
obj.Traverse()
print()
obj.pop()
obj.Traverse()
print()
print(obj.peek())
    