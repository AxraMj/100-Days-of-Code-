class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
class CircularDoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        newNode.next=newNode
        newNode.prev=None
    def insert(self,value):
        if self.head is None:
            self.create(value)
        else:
            newnode=Node(value)
            self.tail.next=newnode
            newnode.next=self.head
            newnode.prev=self.tail
            self.tail=newnode
    def traverse(self):
        if self.head is None:
            print("Empty!!!!")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.value)
                current_node=current_node.next
                if current_node == self.head:
                    break
obj=CircularDoublyLL()
obj.create(30)
obj.insert(59)
obj.insert(99)
obj.insert(991)
obj.traverse()