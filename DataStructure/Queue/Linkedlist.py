class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class QueueLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
            self.tail=newnode
        else:
            newnode=Node(data)
            self.tail.next=newnode
            self.tail=newnode

    def display(self):
        if self.head is None:
            print("Empty!!")
        else:
            curent_node=self.head
            while curent_node:
                print(curent_node.data)
                curent_node=curent_node.next
    def dequeue(self):
        if self.head is None:
            print("Empty!!!")
        else:
            deu_elemnt=self.head
            self.head=self.head.next
            return deu_elemnt


obj=QueueLL()
obj.enqueue(20)
obj.enqueue(10)
obj.enqueue(90)
obj.display()

print()
obj.dequeue()
obj.display()


