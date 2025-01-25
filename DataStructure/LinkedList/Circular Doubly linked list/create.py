class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class CircularDoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None

obj=CircularDoublyLL()
nod1=Node(20)
node2=Node(30)
node3=Node(40)

obj.head=nod1
nod1.next=node2
nod1.prev=None
node2.next=node3
node2.prev=nod1
node3.next=nod1
node3.prev=node2
obj.tail=node3