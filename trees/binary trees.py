#binary tree implementation

from turtle import tracer


class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

root=Node(10)
root.right=Node(34)

root.left = Node(89)

#inserting children to sub tress  #its like every child is its own root
root.left.left=Node(20)
root.left.right=Node(45)
root.right.left=Node(56)
root.right.right=Node(54)
root.right.right.left=Node(166)

    #traversing
    #inorder

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

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
            

def treeheight(root):
    if root is None:
        return 0
    
    leftans=treeheight(root.left)
    rightans=treeheight(root.right)
    return (max(leftans,rightans)+1)   #adding 1 of main root

def height(root):
    ans=0
    q=[]
    if root is None:
        return ans

    q.insert(0,root)
    while q:
        size=len(q)
        while size>0:
            curnode=q.pop()
            size-=1

            if curnode.left is not None:
                q.append(curnode.left)
            if curnode.right is not None:
                q.append(curnode.right)
        ans+=1
    return ans

# print(treeheight(root))
print(height(root))
# print(leveltraversal(root))