class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class SLikedlist():
    def __init__(self):
        self.head=None
        self.tail=None

    #Traverse 
    def TraversingElemnt(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            current_node=self.head 
            while current_node is not None:
                print(current_node.value)
              


singlylinkedlist=SLikedlist()
node1=Node(10)
node2=Node(20)
node3=Node(30)

singlylinkedlist.head=node1
node1.next=node2
node2.next=node3
singlylinkedlist.tail=node3

singlylinkedlist.TraversingElemnt()