
class Node:
    queue=[0]
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
        Node.queue.append(self.data)
    
    def getval():
        print(Node.queue)
    def parent(self):
        for i in range (len(Node.queue)):

            if  Node.queue[i]==self.data:
                return i//2
    def leftChild(self):
        if self.left:

            for i in range (1,(len(Node.queue))):
                if  Node.queue[i]==self.data:
                    return 2*i
        else:
            return False
        
    def rightChild(self):
        if self.right:

            for i in range (1,(len(Node.queue))):
                if Node.queue[i]==self.data:
                    child=(2*i)+1
                    return child
        else:
            return False

    def shiftUp(self):
        prt=self.parent()
        for i in range (1,(len(Node.queue))):
            if Node.queue[i]==self.data:
                idx=i

        while idx>1 and Node.queue[prt] < Node.queue[idx]:
            Node.queue[prt],Node.queue[idx]=Node.queue[idx],Node.queue[prt]
            i=self.parent()

        

    def shifDown(self):


        for i in range (1,(len(Node.queue))):
            if Node.queue[i]==self.data:
                maxindex=i          #index of elemt
                size=len(Node.queue)
                l=self.leftChild()  #index of left child
                print("max index is maxindex"+str(maxindex))
                print("left child index is "+str(l))
                if l<=size and Node.queue[l]>Node.queue[maxindex]:
                    maxindex = l
                r=self.rightChild()
                if r <=size and Node.queue[r]>Node.queue[maxindex]:
                    maxindex=r
                
                if i !=maxindex:
                    Node.queue[i],Node.queue[maxindex]=Node.queue[maxindex],Node.queue[i]
                    
    def insert(self,data):

        Node.queue.append(data)
        self.shifUp(data)

        
def leveltraversal(root):
    traversed=[]
    traversed.append(root)

    if root is None:
        return traversed
    
    while traversed!=[]:
        print(traversed[0].data)
        x=traversed.pop(0)

        if x.left:
            traversed.append(x.left)
        if x.right:
            traversed.append(x.right)

root=Node(42)

root.left=Node(10)
root.right=Node(15)   #down 
root.left.left=Node(20)
root.left.left.shiftUp()
child=Node(50)

Node.getval()