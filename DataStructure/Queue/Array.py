class Node:
    def __init__(self,data):
        self.data=data

class QueueArray:
    def __init__(self):
        self.Queue=[]

    def enqueue(self,value):
        self.Queue.append(value)
    def display(self):
        for i in self.Queue:
            print(i)
    def dequeue(self):
        self.Queue.pop(0)
    
obj=QueueArray()
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(10)
obj.enqueue(70)
obj.display()
print()
obj.dequeue()
obj.dequeue()
obj.display()
        