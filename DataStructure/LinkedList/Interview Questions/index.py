from random import randint
#Remove duplicate from linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class RemoveDuplictaeLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def create(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for i in range(n):
            self.create(randint(min_value,max_value))
        return self
     # Traverse the list and print all node values
    def print_values(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")  # End of the linked list

# obj = RemoveDuplictaeLL()
# obj.generate(10, 0, 20)

# # Print the generated values
# print("Generated values in the linked list:")
# obj.print_values()