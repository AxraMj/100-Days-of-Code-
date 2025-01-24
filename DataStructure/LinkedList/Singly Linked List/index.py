class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class HeadTailNode:
    def __init__(self):
        self.head=None
        self.tail=None
    #insertion
    def insertItem(self,value,location):
        newNode=Node(value,)
        if self.head is None:
            print("Empty list!!!")
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location==-1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index < location - 1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                newNode.next=nextNode
                tempNode.next=newNode


    def traverse(self):
        if self.head is None:
            print("Empty list!!")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.value)
                current_node=current_node.next
    
    def searchelement(self,element):
        if self.head is None:
            print("empty!!")
        else:
            Current_node = self.head
            while Current_node is not None:
                if Current_node.value == element:
                    return f"{element} is in the list"
                Current_node=Current_node.next
            return "Elemt not found"
    def DeleteElemt(self,location):
        if self.head is None:
            print("Nothing to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None  
                else:
                    self.head=self.head.next
            elif location == -1:
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
                temp_node= self.head
                index=0
                while index < location -1:
                    temp_node=temp_node.next
                    index+=1
                nextnode=temp_node.next
                temp_node.next=nextnode.next
                




obj=HeadTailNode()
node1=Node(20)
obj.head=node1
obj.tail=node1


obj.insertItem(10,0)
obj.insertItem(60,-1)
obj.insertItem(50,-1)
obj.insertItem(150,-1)
obj.insertItem(300,3)
obj.traverse()
print(obj.searchelement(150))

obj.DeleteElemt(0)
obj.DeleteElemt(-1)
obj.DeleteElemt(3)
obj.traverse()