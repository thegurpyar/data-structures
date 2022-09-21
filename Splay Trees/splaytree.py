

from operator import indexOf


class TreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.parent=None

class SplayTree:
    def __init__(self):
        self.root=None
    
    def insert(self,n):
        temp=self.root
        y=None
        while temp !=None:
            y=temp
            if n.data < temp.data:
                temp=temp.left
            else:
                temp=temp.right
        #after loop when node==NOne
        n.parent=y
        if y==None:  #no parent mean root
            self.root=n
        #for becoming left or right child of parent node
        elif n.data<y.data:
            y.left=n
        else:
            y.right=n
        self.splay(n)
        
        
    def splay(self,n):
        while n.parent !=None:
            if n.parent == self.root:  # node is child of root only one rotation required
                if n.parent.left==n:
                    self.rightrotate(n.parent)
                else:
                    self.leftrotate(n.parent)
            else: #if node has parent as well as granparent
                p=n.parent
                g=p.parent #grandparent
                #1.zig zig
                if n.parent.left ==n and p.parent.left == p:
                    self.rightrotate(g)
                    self.rightrotate(p)
                #2.zag zag
                elif n.parent.right == n and p.parent.right==p:
                    self.leftrotate(g)
                    self.leftrotate(p)
                #3.zig zag
                elif n.parent.left == n and p.parent.right == p:
                    self.rightrotate(p)
                    self.leftrotate(g)
                #4.zag zig
                elif n.parent.right == n and p.parent.left == p:
                    self.leftrotate(p)
                    self.rightrotate(g)

    
    def rightrotate(self,x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        # x is root
        if x.parent == None:
            self.root = y
        # x is right child
        elif x == x.parent.right:
            x.parent.right = y
        # x is left child
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
    
    def leftrotate(self,x):
        y=x.right
        x.right=y.left
        if y.left!=None:
            y.left.parent=x
        y.parent=x.parent

        if x.parent ==None:
            self.root=y
        
        elif x.parent.left==x:
            x.parent.left=y

        else:
            x.parent.right=y
        y.left=x
        x.parent=y


    def inOrder(self, n):
        if n != None:
            
            self.inOrder(n.left)
            print(n.data)
            self.inOrder(n.right)
tree=SplayTree()
nums=[15,10,17,7,13,16]
for i in nums:
    tree.insert(TreeNode(i))
tree.inOrder(tree.root)