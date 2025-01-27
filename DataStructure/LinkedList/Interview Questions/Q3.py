from index import *

def questionthree(obj, x):
    # Start from the head of the list
    current_node = obj.head
    obj.tail = current_node

    while current_node is not None:
        # Store the next node before detaching
        next_node = current_node.next
        current_node.next = None

        if current_node.value < x:
            # Insert the node at the beginning (update head)
            current_node.next = obj.head
            obj.head = current_node
        else:
            # Append the node at the tail (update tail)
            obj.tail.next = current_node
            obj.tail = current_node

        # Move to the next node
        current_node = next_node

    # Ensure the tail's next pointer is None
    obj.tail.next = None


# Assuming RemoveDuplictaeLL is a valid linked list class
obj = RemoveDuplictaeLL()
obj.generate(10, 0, 20)

# Print the generated values
print("Generated values in the linked list:")
obj.print_values()

# Apply questionthree with x = 30
questionthree(obj, 5)

# Print the modified list
print("Modified linked list after applying questionthree:")
obj.print_values()
