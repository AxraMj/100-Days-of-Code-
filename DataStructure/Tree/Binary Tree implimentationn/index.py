class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        newnode=Node(value)
        if self.root is None:
            self.root=newnode
        else:
            current_node=self.root
            if value < current_node:
                if current_node.left is None:
                    current_node.left=newnode
                    return
                current_node=current_node.left
            else:
                if value > current_node:
                    if current_node.right is None:
                        current_node.right=newnode
                        return
                    current_node=current_node.right
obj=BinaryTree()
obj.insert(10)