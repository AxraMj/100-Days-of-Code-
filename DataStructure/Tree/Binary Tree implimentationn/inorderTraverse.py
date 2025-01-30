class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
            return

        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = newnode
                    return
                current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = newnode
                    return
                current_node = current_node.right
            else:
                # Ignore duplicate values
                return  

    def inorder_traverse(self, root):
        if root is not None:
            self.inorder_traverse(root.left)  # Left subtree
            print(root.value, end=" ")        # Root node
            self.inorder_traverse(root.right) # Right subtree

# Testing the BinaryTree class
obj = BinaryTree()
obj.insert(10)
obj.insert(20)
obj.insert(6)
obj.insert(15)
obj.insert(3)

print("Inorder Traversal: ")
obj.inorder_traverse(obj.root)  # Expected Output: 3 6 10 15 20
