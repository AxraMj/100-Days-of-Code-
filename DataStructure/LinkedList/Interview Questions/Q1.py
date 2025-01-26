from index import *

# Function to remove duplicates from a linked list
def remove(obj):
    if obj.head is None:
        print("Empty Linked List!")
        return obj
    else:
        current_node = obj.head
        temp_nodes = set()  # Set to store seen values
        prev_node = None  # Keep track of the previous node

        # Traverse the linked list
        while current_node:
            if current_node.value in temp_nodes:  # Duplicate found
                prev_node.next = current_node.next  # Remove duplicate
            else:
                temp_nodes.add(current_node.value)  # Add value to set
                prev_node = current_node  # Update previous node
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
