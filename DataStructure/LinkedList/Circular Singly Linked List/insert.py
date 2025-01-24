class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CircularSLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self,value):
        newNode=Node(value)
        self.head=newNode
        newNode.next=newNode
        self.tail=newNode
        print(f"{value} Node created successfully as the first node.")
    def insert(self,value,loctaion):
        if self.head is None:
            self.create(value)
        else:
            newNode=Node(value)
            if loctaion == 0:
                self.tail.next=newNode
                newNode.next=self.head
                self.head=newNode
                print(f"{value} Node inserted at the beginning.")
            elif loctaion == -1:
                self.tail.next=newNode
                newNode.next=self.head
                self.tail=newNode
            else:
                temp_node=self.head
                index=0
                while index < loctaion -1:
                    temp_node=temp_node.next
                    index+=1
                nextnode=temp_node.next
                temp_node.next=newNode
                newNode.next=nextnode


    def Traverse(self):
        if self.head is None:
            print("List is empty!!!")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.value)
                current_node=current_node.next
                if current_node == self.head:
                    break

obj=CircularSLL()
obj.create(10)
obj.Traverse()
print()
obj.insert(30,0)
obj.insert(130,0)
obj.insert(1,-1)
obj.insert(11,2)
obj.Traverse()