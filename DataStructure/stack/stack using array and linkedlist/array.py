class Node:
    def __init__(self,data):
        self.data=data

class ArrayStack:
    def __init__(self):
        self.stack=[]

    def push(self,value):
            newnode=Node(value)
            self.stack.append(newnode)

    def display(self):
        if self.stack is None:
            return "Empty"
        return [i.data for i in self.stack]
    
    def pop(self):
        if not self.stack:
            return "Empty"
        return self.stack.pop()
    def peek(self):
        if self.stack:
            print(self.stack[-1].data)
          
obj=ArrayStack()
obj.push(20)
obj.push(10)
obj.push(30)
print(obj.display())
print()

obj.pop()
print(obj.display())

obj.peek()
