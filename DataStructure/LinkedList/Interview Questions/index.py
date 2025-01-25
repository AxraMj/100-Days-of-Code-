from random import randint
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value) 
node1=Node(20)
print(node1)
# Here’s what this does:
# Purpose: Converts the Node object into a string representation by returning the string representation of its value attribute.
# Usage: If you have a Node object and call print() or str() on it, Python will call the __str__ method and return the value of the node as a string.
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        current_Node=self.head
        while current_Node:
            yield current_Node
            current_Node=current_Node.next
    def __str__(self):
        value=[str(x.value) for x in self]
        return '->'.join(value)
    
    #to find length of linkedlst
    def __len__(self):
        result = 0
        node=self.head
        while node:
            result+=1
            node=node.next
        return result
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self
# The __iter__ method is a special method in Python that allows an object to be used in a for loop or other contexts where iteration is required.
# How is yield different from return?
# return: Stops the function completely and sends back a single value.
# yield: Pauses the function and sends back a value, but the function can continue running after that.
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(len(customLL))