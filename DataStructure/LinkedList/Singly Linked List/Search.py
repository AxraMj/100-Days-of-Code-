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
    
    def search(self,Searchvalue):
        if self.head is None:
            print("Lnked lst is empty no va;ue to search!!")
        else:
            currentnode=self.head
            while currentnode is not None:
                if currentnode.values==Searchvalue:
                    return f"Value {currentnode.values} present"
                currentnode = currentnode.next
            return "No such value is present in the list"
                

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
print(obj.search(20))
