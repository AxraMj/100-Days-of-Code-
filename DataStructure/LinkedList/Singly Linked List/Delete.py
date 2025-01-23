#Searching elemnt in singly linked list
class Node:
    def __init__(self,values=None):
        self.values=values
        self.next=None
class HeadTailNode:
    def __init__(self):
        self.head=None
        self.tail=None
    def tarverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.values)
                current_node=current_node.next
    def deleteNode(self,loction):
        if self.head is None:
            print("Empty!!")
        else:
            if loction==0:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif loction == -1:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    current_node=self.head
                    while current_node is not None:
                        if current_node.next==self.tail:
                            break
                        current_node=current_node.next
                    current_node.next=None
                    self.tail=current_node     
            else:
                tempnode=self.head
                index=0
                while index <loction-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next          

obj=HeadTailNode()
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)
obj.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
obj.tail=node6

obj.tarverse()
obj.deleteNode(-1)
print()
obj.tarverse()

