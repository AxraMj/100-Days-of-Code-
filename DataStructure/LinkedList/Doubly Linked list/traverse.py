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
            newNode.prev=self.tail       
            self.tail.next=newNode
            self.tail=newNode
    def traverse(self):
        if self.head is None:
            print("empty!!")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.value)
                current_node=current_node.next

obj=DoublyLL()
obj.create(10)
obj.create(20)
obj.create(30)
obj.create(40)
obj.traverse()

        