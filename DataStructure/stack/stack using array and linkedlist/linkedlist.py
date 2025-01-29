class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class StackLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    
    def display(self):
        if self.head is None:
            return "Empty"
        else:
            current_node=self.head
            while current_node:
                print(current_node.data)
                current_node=current_node.next

    def pop(self):
        if self.head is None:
            return "Stack is empty."
        poped_data=self.head
        self.head=self.head.next
        return poped_data
    def peek(self):
        return self.head.data

obj=StackLL()
obj.push(20)
obj.push(60)
obj.push(70)
obj.display()
print()
obj.pop()
obj.display()

print()
print(obj.peek())
