

from logging import exception


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertatbegin(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp
    
    def insertatend(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:

            k=self.head
            while k.next!=None:
                k=k.next
            k.next=temp
    
    def insertatpos(self,data,pos):  #doubt
        temp=Node(data)
        count=1
        k=self.head
        while count < pos-1 and k!=None:
            k=k.next
            count+=1
        temp.next=k.next
        k.next=temp
        
    
    def traverse(self):
        while self.head!=None:
            print(self.head.data)
            self.head=self.head.next

    def deleteatbeg(self):
        if self.head==None:
            raise Exception("empty linked list")
        else:
            self.head=self.head.next
        
    def deleteatend(self):
        if self.head==None:
            raise Exception("Empty Linked List")
        else:
            curr=self.head
            prev=None
            while curr.next!=None:
                prev=curr
                curr=curr.next
            prev.next=None
            del curr
    
    def deleteatpos(self,pos):
        if self.head==None:
            raise Exception("Empty Linked List")
        else:
            curr=self.head
            prev=None
            count=1
            while curr!=None and count<pos:

                prev=curr
                curr=curr.next
                count+=1
            prev.next=curr.next
            del curr
            

LinkedList=LinkedList()
nums=[4,15,7,40]
for i in nums:
    LinkedList.insertatend(i)
LinkedList.deleteatpos(3)
LinkedList.traverse()
