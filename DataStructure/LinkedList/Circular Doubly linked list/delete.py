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
    def insert(self,value,loaction):
        if self.head is None:
            self.create(value)
        else:
            newnode=Node(value)
            if loaction == 0:
                newnode.next=self.head
                newnode.prev=self.tail
                self.head.prev=newnode
                self.tail.next=newnode
                self.head=newnode
            elif loaction == -1:
                self.tail.next=newnode
                newnode.prev=self.tail
                newnode.next=self.head
                self.tail=newnode
            else:
                temp_node=self.head
                index=0
                while index < loaction-1:
                    temp_node=temp_node.next
                    index+=1
                nextnode=temp_node.next
                newnode.next=nextnode
                nextnode.prev=newnode
                temp_node.next=newnode
            
                
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
    def delete(self,location):
        if self.head is None:
            print("empty!!!")
        else:
            if location == 0:
                self.head=self.head.next
                self.tail.next=self.head
            if location == -1:
                self.tail=self.tail.prev
                self.tail.next=self.head
            else:
                temp_node=self.head
                index=0
                if index < location-1:
                    temp_node=temp_node.next
                    index+=1
                nextnode=temp_node.next.next
                temp_node.next = nextnode
                nextnode.prev = temp_node
obj=CircularDoublyLL()
obj.create(30)
obj.traverse()

print()
obj.insert(20,0)
obj.insert(5,0)
obj.insert(39,-1)
obj.insert(89,2)
obj.traverse()

print()

obj.delete(1)
obj.traverse()