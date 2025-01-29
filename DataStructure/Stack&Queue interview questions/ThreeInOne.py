# class Solution:
#     def __init__(self):
#         self.stack = []
#         self.stackTwo=[]
#         self.stackThree=[]
#         self.list = [11, 22, 33, 44, 55, 66, 77, 88, 99] 

#     def stack1(self):
#         for i in range(0, len(self.list) // 3):
#             self.stack.append(self.list[i])
#         print("Stack One:", self.stack)

#     def stack2(self):
#         for i in range(len(self.list) // 3, 2 * len(self.list) // 3):
#             self.stackTwo.append(self.list[i])
#         print("Stack Two:", self.stackTwo)

#     def stack3(self):
#         for i in range( 2 * len(self.list) // 3, len(self.list)):
#             self.stackThree.append(self.list[i])
#         print("Third stack:" ,self.stackThree)



# # Creating object of Solution class
# obj = Solution()
# obj.stack1()
# obj.stack2()
# obj.stack3()
class Thriplestack:
    def __init__(self, stack_size):
        self.stack_size = stack_size  # Size of each stack
        self.array = [None] * (3 * stack_size)  # The main array holding all three stacks
        self.top = [-1, -1, -1]  # Track the top of each stack

    # Push an element onto a specified stack
    def push(self, stack_num, value):
        if self.is_full(stack_num):  # Check if the stack is full
            raise Exception(f"Stack {stack_num} is full")
        
        # Calculate the correct index for the stack based on its stack number
        index = stack_num * self.stack_size + self.top[stack_num] + 1
        self.top[stack_num] += 1
        self.array[index] = value

    # Check if the stack is empty
    def is_empty(self, stack_num):
        return self.top[stack_num] == -1

    # Check if the stack is full
    def is_full(self, stack_num):
        return self.top[stack_num] == self.stack_size - 1

    # Display the contents of a stack
    def display(self, stack_num):
        if self.is_empty(stack_num):  # If the stack is empty, raise an exception
            raise Exception(f"Stack {stack_num} is empty")
        
        print(f"Stack {stack_num} contents:")
        start_index = stack_num * self.stack_size
        end_index = start_index + self.top[stack_num] + 1
        for i in range(start_index, end_index):
            if self.array[i] is not None:
                print(self.array[i])

# Example usage
obj = Thriplestack(3)  # Create a stack with each stack having space for 3 elements

# Pushing elements onto the stacks
obj.push(0, 11)  # Push to Stack 1
obj.push(1, 22)  # Push to Stack 2
obj.push(2, 33)  # Push to Stack 3
obj.push(0, 44)  # Push to Stack 1
obj.push(1, 55)  # Push to Stack 2
obj.push(2, 66)  # Push to Stack 3

# Display the contents of each stack
obj.display(0)  # Display Stack 1
obj.display(1)  # Display Stack 2
obj.display(2)  # Display Stack 3
