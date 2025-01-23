#Work on a empty list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class HeadTail:
    def __init__(self):
        self.head=None
        self.tail=None
    #insert
    def insertValues(self,values,location):
        NewNode=Node(values)
        if self.head is None:
            self.head=NewNode
            self.tail=NewNode
        else:
            if location==0:
                NewNode.next=self.head
                self.head=NewNode
            elif location==-1:
                NewNode.next=None
                self.tail.next=NewNode
                self.tail=NewNode
            else:
                temp_node=self.head
                index=0
                while index < location -1:
                    temp_node=temp_node.next
                    index+=1
                nextNode=temp_node.next
                NewNode.next=nextNode
                temp_node.next=NewNode

    #Traverse
    def Traverseelement(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.value)
                current_node=current_node.next
obj=HeadTail()
obj.insertValues(30,None)
obj.insertValues(10,0)
obj.insertValues(50,-1)
obj.insertValues(100,-1)
obj.insertValues(3,2)
obj.Traverseelement()