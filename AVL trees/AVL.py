class TreeNode:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        self.height=1
        
class AVLTree:
    #helper methods
    def getheight(self,root):
        if not root:
            return 0
        else:
            return root.height
    
    def getbalance(self,root):
        if not root:return 0
        return (self.getheight(root.left)-self.getheight(root.right))


    def insertnode(self,root,key):
        if not root:
            return TreeNode(key)
        if key < root.key:
            root.left=self.insertnode(root.left,key)
        if key > root.key:
            root.right=self.insertnode(root.right,key)
        #exit recursive call
        #get height
        self.height=1+max(self.getheight(root.left),self.getheight(root.right))
        #update balance factor
        balancefactor=self.getbalance(root)
        if balancefactor > 1:    #left is unbalanced
            if key < root.left.key:
                return self.rightrotate(root)
            else:                #if key is on right
                root.left=self.leftrotate(root.left)
                return self.rightrotate(root)
        
        if balancefactor<-1:     #right tree is unbalaned
            if key>root.right.key:
                return self.leftrotate(root)
            else:
                root.right=self.rightrotate(root.right)
                return self.leftrotate(root)
        return root

    def getminvalue(self,root):
        if root is None or root.left is None:
            return root

        return self.getminvalue(root.left)
    def rightrotate(self,z):
        y=z.left     # y is smaller thn z
        T=y.right   #greater thn y but smaller thn z
        y.right=z  #rotate  y bigger child is z
        z.left=T    #y child becomes left child of z 
        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))
        return y
    
    def leftrotate(self,z):
        y=z.right
        T=y.left
        y.left=z
        z.right=T
        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))
        return y

    def preOrder(self, root):
        if not root:
            return
        
        self.preOrder(root.left)
        print("{0} ".format(root.key), end="")
        self.preOrder(root.right)
tree=AVLTree()

nums = [33, 13, 52, 21, 61, 8, 11,9]
root=None
# for num in nums:
#     root = tree.insertnode(root, num)
#     print(root)
root=tree.insertnode(root,nums[0])
for i in range(1,len(nums)):
    tree.insertnode(root,nums[i])
tree.deleletenode(root,21)
tree.preOrder(root)