class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertatbeg(self,data):
        newnode=Node(data)
        if self.head == None:
            self.head=newnode

        else:
            newnode.prev=None
            newnode.next=self.head
            