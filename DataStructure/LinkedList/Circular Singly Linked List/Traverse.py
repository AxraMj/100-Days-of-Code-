class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularSLL:
    def __init__(self):
        self.head=None
        self.tail=None
    # Create the circular linked list with a single node
    def create(self, value):
        newNode = Node(value)
        newNode.next = newNode  # Points to itself, making it circular
        self.head = newNode
        self.tail = newNode
        print(f"{value} Node created successfully as the first node.")

    # Add a new node to the circular linked list
    def insert(self, value):
        if self.head is None:  # If the list is empty, create it first
            self.create(value)
        else:
            newNode = Node(value)
            newNode.next = self.head  # New node points to the current head
            self.tail.next = newNode  # Old tail points to the new node
            self.tail = newNode       # Update the tail to the new node
            print(f"{value} Node added successfully.")
    def traverse(self):
        if self.head is None:
            print("empty!!")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.value)
                current_node=current_node.next
                if current_node == self.head:  # Stop when we come back to the head
                    break
            print("(Back to head)")

    
obj=CircularSLL()
obj.create(20)
obj.insert(50)
obj.insert(60)
obj.traverse()


        