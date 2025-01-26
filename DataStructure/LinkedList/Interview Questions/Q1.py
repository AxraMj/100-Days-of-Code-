from index import *

# Function to remove duplicates from a linked list
def remove(obj):
    if obj.head is None:
        print("Empty Linked List!")
        return obj
    else:
        current_node = obj.head
        temp_nodes = set([current_node.value])  # Set to store seen values

        # Traverse the linked list
        while current_node.next:  # Stop before the last node
            if current_node.next.value in temp_nodes:  # Duplicate found
                current_node.next = current_node.next.next  # Skip the duplicate node
            else:
                temp_nodes.add(current_node.next.value)  # Add value to set
                current_node = current_node.next  # Move to the next node

        return obj

# Create and test the linked list
obj = RemoveDuplictaeLL()
obj.generate(10, 0, 20)

# Print the generated values
print("Generated values in the linked list:")
obj.print_values()

# Remove duplicates and print the updated list
remove(obj)
print("Linked list after removing duplicates:")
obj.print_values()
