class Node:
    def __init__(self,value=None):
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
    def insert(self,value):
        if self.head is None:
            self.create(value)
        else:
            newnode=Node(value)
            self.tail.next=newnode
            newnode.next=self.head
            self.tail=newnode
    def delete(self,location):
        if self.head is None:
            print("Empty!!!!")
        else:
            if location == 0:
                self.head=self.head.next
                self.tail.next=self.head
            elif location == -1:
                current_node=self.head
                while current_node is not None:
                    if current_node.next == self.tail:
                        break
                    current_node=current_node.next
                current_node.next=self.head
            else:
                 temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index += 1
            temp_node.next = temp_node.next.next
            # Update the tail if the deleted node was the last node
            if temp_node.next == self.head:
                self.tail = temp_node

    def Traverse(self):
        if self.head is None:
            print("Empty!!!")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.value)
                current_node=current_node.next
                if current_node == self.head:
                    break

obj=CircularSLL()
obj.insert(20)
obj.insert(50)
obj.insert(70)
obj.insert(80)
obj.insert(150)
obj.insert(170)
obj.insert(180)
obj.Traverse()
print()
obj.delete(3)
obj.Traverse()