

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None   #right all small
        self.left=None    #left all big

    def getright(self):
        return self.right
    
    def getleft(self):
        return self.left
    


def modifiedfind(root,data):
    if root.data == data:
        return root
    elif root.data > data:
        if root.left!=None:
            return modifiedfind(root.left,data)
        return root
    else:
        if root.right !=None:

            return modifiedfind(root.right,data)

        return root


#by book
def find(root,data):
    # currentnode=root
    # while currentnode is not None and data!=currentnode.data:
    #     if data>currentnode.data:
    #         currentnode=currentnode.right
    #     else:
    #         currentnode=currentnode.left
    # return currentnode.data

    if root.data == data:
        return root.data
    elif root.data > data:
        return find(root.left,data)
    else:
        return find(root.right,data)

def insertnode(root,node):
    if root is None:
        root=node
    else:
        if root.data>node.data:
            if root.left==None:
                root.left=node
            else:
                insertnode(root.left,node)
        else:
            if root.right==None:
                root.right=node
            else:
                insertnode(root.right,node)

def successor(root):
    if root.right:
        temp=root.right
        while temp.left:
            temp=temp.left
    return temp

def predecessor(root):

    if root.left:
        temp=root.left
        while temp.right:
            temp=temp.right
    return temp


def find_min(root):
    if root.right is None:return root.data
    return find_min(root.right)

def find_max(root):
    if root.left is None:return root.data
    return find_max(root.left)
def deletenode(root,data):
    if data<root.data:
        if root.left:
            deletenode(root.left,data)
    elif data>root.data:
        if root.right:
            deletenode(root.right)
    else:
        if root.right is None and root.left is None:return None

        elif root.left is None:
            return root.right
        
        elif root.right is None:
            return root.left
        else:
            min=find_min(root.right)
            
            root.data=min
            root.right=deletenode(root.right,min)
    return root

def inorder(root):
    res=[]
    if root.left:
        res+=inorder(root.left)
    res.append(root.data)
    if root.right:
        res+=inorder(root.right)
    return res

def postorder(root):
    res=[]
    if root.left:
        res+=postorder(root.left)
    if root.right:
        res+=postorder(root.right)
    res.append(root.data)
    return res

def preorder(root):
    res=[]
    res.append(root.data)
    if root.left:
        res+=preorder(root.left)
    if root.right:
        res+=preorder(root.right)
    return res
    
def buildtree(numbers):
    root=Node(numbers[0])
    
    for i in range(1,len(numbers)):
        insertnode(root,Node(numbers[i]))
    print(preorder(root)) 
    print(inorder(root))
    print(postorder(root))
numbers=[4,2,5,1,3]
buildtree(numbers)
    