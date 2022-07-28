class Node:
    def __init__(self,n):
        self.parent=[x for x in range(n)]
        self.rank=[0]*n

    def find(self,root):
        if self.parent[root]==root:
            return root
        else:
            return self.find(self.parent[root])
    def union(self,x,y):
        xroot=self.find(x)
        yroot=self.find(y)
        if xroot==yroot:
            return

        #below are based on rank not parent
        if self.rank[xroot]<self.rank[yroot]:
            self.parent[xroot]=yroot
        elif self.rank[yroot]<self.rank[xroot]:
            self.parent[yroot]=xroot
        else:
            self.parent[yroot]=xroot
            self.rank[xroot]=self.rank[xroot]+1
    def getval(self):
        print(self.parent)
        print(self.rank)
a=Node(5)
a.union(0,1)
a.union(1,2)
a.union(3,4)
a.union(1,4)
a.getval()

