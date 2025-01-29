class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, item):
        if self.head is None:
            newnode = ListNode(item)
            self.head = newnode
            self.tail = newnode
        else:
            newnode = ListNode(item)
            self.tail.next = newnode
            self.tail = newnode

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")

    def addTwoNumbers(self, list1, list2):
        carry = 0
        a = list1.head
        b = list2.head
        result = Solution()  # This will store the sum linked list
        
        while a or b or carry:
            sum = carry
            if a:
                sum += a.val  
                a = a.next
            if b:
                sum += b.val  
                b = b.next

            carry = sum // 10
            result.insert(sum % 10)  # Insert the digit at the correct place

        return result.head  # Return only the head of the result linked list (ListNode)

# Example usage:

print("List One is:")
list1 = Solution()
list1.insert(2)
list1.insert(4)
list1.insert(3)

print("List Two is:")
list2 = Solution()
list2.insert(5)
list2.insert(6)
list2.insert(4)

print("List Sum is:")
result = list1.addTwoNumbers(list1, list2)

# Traverse the result (now result is the head of the new linked list)
current_node = result
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
