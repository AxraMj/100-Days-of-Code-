class Node:
    def __init__(self,value=None):
        self.value=value 
        self.next=None
class circularSLL:
    def __init__(self):
        self.head=None
        self.tail=None


obj=circularSLL()
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
obj.head=node1
obj.tail=node4

# Connect the nodes in a circular manner
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node1

 # Last node points back to the head.
 # Circular Linked List structure:
# Head -> [3] -> [5] -> [7] -> points back to Head (circular loop)