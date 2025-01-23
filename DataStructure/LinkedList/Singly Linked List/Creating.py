#This class is used to create a node in the linked list.
class Node:
    def __init__(self,value=None):
        self.value=value #value: Stores the data of the node.
        self.next=None #next: Points to the next node in the list (or None if it's the last node).

#for head and tail node (This is the container for the linked list)
class SLinkedList:
    def __init__(self):
        self.head=None  #head: Points to the first node in the list (or None if the list is empty).
        self.tail=None  #tail: Points to the last node in the list (or None if the list is empty).

#link Node with head and tail node
singlylinedlist=SLinkedList()
node1=Node(3)
node2=Node(5)
singlylinedlist.head=node1
node1.next=node2 # First node points to the second node.
singlylinedlist.tail=node2

# Head -> [3] -> [5] -> None


#This how we create a singly linked list