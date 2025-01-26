from index import *

# Function to find the n-th element from the end of the linked list
def nthelement(obj, n):
    pointer1 = obj.head  # Start both pointers at the head
    pointer2 = obj.head  # Start the second pointer at the head

    # Move pointer2 ahead by 'n' steps
    for i in range(n):
        if pointer2 is None:  # If n is greater than the length of the list
            return None
        pointer2 = pointer2.next

    # Move both pointers until pointer2 reaches the end
    while pointer2 is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1.value  # Return the value of the n-th element from the end


# Create and print the linked list
obj = RemoveDuplictaeLL()
obj.generate(10, 0, 20)
print("Generated Linked List:")
obj.print_values()

# Find the 5th element from the end
print("5th element from the end:")
print(nthelement(obj, 5))
