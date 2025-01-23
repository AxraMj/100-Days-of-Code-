class Node:
    def __init__(self, values=None):
        self.values = values
        self.next = None

class HeadTailNode:
    def __init__(self):
        self.head = None
        self.tail = None

    def tarverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.values)
                current_node = current_node.next

    def deleteWhole(self):
        if self.head is None:
            print("Linked list is already empty")
        else:
            self.head = None  # Remove reference to head
            self.tail = None  # Remove reference to tail

# Create and populate the linked list
obj = HeadTailNode()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)
obj.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
obj.tail = node6

# Delete the whole linked list
obj.deleteWhole()

# Try traversing the now empty list
obj.tarverse()  # This should print "Linked list is empty"
