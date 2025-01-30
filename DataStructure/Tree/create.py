class TreeNode:
    def __init__(self,value):
        self.value=value
        self.tree=[]

    def add(self,value):
        self.tree.append(value)

    def display(self):
        for i in self.tree:
            print(i.value)
        


root=TreeNode('A')
nodeB=TreeNode('B')
nodeC=TreeNode('c')
nodeD=TreeNode('D')
nodeE=TreeNode('E')

root.add(nodeB)
root.add(nodeC)

nodeB.add(nodeD)
nodeB.add(nodeE)

print("Root node A has:")
root.display()
print("Parent B has 2 child:")
nodeB.display()