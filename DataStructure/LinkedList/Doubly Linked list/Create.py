class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def create(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.prev=None
            newNode.next=None
        else:
            newNode.prev=self.head
            self.head.next=newNode

obj=DoublyLL()
node1=Node(20)
node2=Node(30)

obj.head=node1
node1.next=node2
node2.prev=node1
obj.tail=node2
        