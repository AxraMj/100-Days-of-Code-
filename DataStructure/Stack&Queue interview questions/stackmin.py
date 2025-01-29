class Solution:
    def __init__(self, max_size):
        self.stack = []  # The primary stack
        self.top = -1  # top is -1 when the stack is empty
        self.max_size = max_size  # maximum allowed size for the stack

    def is_empty(self):
        return self.top == -1  # True if the stack is empty

    def is_full(self):
        return self.top == self.max_size - 1  # True if the stack is full
    
    def push(self, value):
        if self.is_full():
            return "Stack is full!"
        
        self.stack.append(value)  # Add element to primary stack
        self.top += 1  # Update the top index
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"  # Handle case when trying to pop from an empty stack
        
        popped_element = self.stack.pop()  # Remove the element from the stack
        self.top -= 1  # Update the top index
        return popped_element  # Return the popped element

    def display(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            for element in self.stack:
                print(element)

# Example usage:
obj = Solution(max_size=5)

# Pushing elements to the stack
obj.push(10)  # Stack: [10]
obj.push(20)  # Stack: [10, 20]
obj.push(5)   # Stack: [10, 20, 5]
obj.push(8)   # Stack: [10, 20, 5, 8]
obj.push(2)   # Stack: [10, 20, 5, 8, 2]

# Display stack content
obj.display()

print()

# Popping an element and displaying the result
print(f"Popped element: {obj.pop()}")  # Popped: 2

# Display stack content after popping
obj.display()
