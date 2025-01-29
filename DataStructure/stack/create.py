class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
    def treverse(self):
        if not self.stack:
            print("Empty")
        else:
            print(self.stack)
    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            print("Empty!!")
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "empty"


obj=Stack()
obj.push(20)
obj.push(10)
obj.push(50)
obj.push(60)
obj.treverse()
print()
obj.pop()
obj.pop()
obj.treverse()
print(obj.peek())