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
    def search(self,element):
        if self.head is None:
            print("empty!!!")
        else:
            cureent_node=self.head
            while cureent_node is not None:
                if cureent_node.value == element:
                    return f"{element} is present"
                cureent_node=cureent_node.next
                if cureent_node == self.head:
                    break
            return f"{element} is not present"

obj=CircularDoublyLL()
obj.create(30)
obj.traverse()

print()
obj.insert(20,0)
obj.insert(5,0)
obj.insert(39,-1)
obj.insert(89,2)
obj.traverse()
print(obj.search(39))