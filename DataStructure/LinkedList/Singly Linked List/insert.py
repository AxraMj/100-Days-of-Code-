class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert into the singly linked list
    def insertSSL(self, value, location):
        newNode = Node(value)
        if self.head is None:  # If the list is empty
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # Insert at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == -1:  # Insert at the end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:  # Insert at a specific location
                tempNode=self.head
                index=0
                while index < location -1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
    # Traverse and print the elements of the list
    def Traverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.value, end=" -> ")
                current_node = current_node.next
            print("None")

# Create a singly linked list and add nodes
SinglyLinkedList = SLList()
node1 = Node(20)
node2 = Node(22)
node3 = Node(25)
SinglyLinkedList.head = node1
node1.next = node2
node2.next = node3
SinglyLinkedList.tail = node3

# Insert a node with value 21 at position 2
SinglyLinkedList.insertSSL(21, 2)

# Traverse the list and print the elements
SinglyLinkedList.Traverse()
