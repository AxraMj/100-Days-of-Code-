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
    def insert(self,value,location):
        if self.head is None:
            self.create(value)
        else:
            newNode=Node(value)
            if location==0:
                self.head.prev=newNode
                newNode.next=self.head
                self.head=newNode
                newNode.prev=None
            elif location==-1:
                self.tail.next=newNode
                newNode.prev=self.tail
                newNode.next=None
                self.tail=newNode
            else:
                temp_node=self.head
                index=0
                while index < location -1:
                    temp_node=temp_node.next
                    index+=1
                nextnode=temp_node.next
                temp_node.next=newNode
                newNode.prev=temp_node
                newNode.next=nextnode
                nextnode.prev=newNode


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

print()
obj.insert(1,0)
obj.insert(2,0)
obj.insert(3,-1)
obj.insert(11,4)
obj.insert(12,2)
obj.traverse()
        