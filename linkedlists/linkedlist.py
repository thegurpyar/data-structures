class Node:
    
    def __init__ (self,data=None,next=None):
        self.data=data
        self.next=next


class Linkedlist:

    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):              
        node=Node(data,self.head)           #next = address of previous node as we r inserting ar beg
        self.head=node                      #head pointer to newley inserted node
        return self.head

        
    def print(self):
        itr=self.head
        llstr=""
        
        while itr:
            suffix=""
            if itr.next:
                suffix="-->"

            llstr+=str(itr.data)+suffix

            itr=itr.next
        print(llstr)
    
    def get_length(self):
        count=0
        itr=self.head
        
        while itr:
            count+=1

            itr=itr.next

        return count

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:

            itr=self.head
            while itr.next:
                itr=itr.next

            itr.next=Node(data)

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            print("invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
        
        else:
            itr=self.head
            pos=0
            while itr:
                if pos == index-1:
                    node=Node(data,itr.next)
                    itr.next=node
                    break

                itr=itr.next
                pos+=1

            
root=Linkedlist()


root.insert_at_end(100)
root.insert_at_begining(10)
root.insert_at(-1,200)
root.print()