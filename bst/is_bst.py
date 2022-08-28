class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
  

def inorder(root):
  
  if root.left:
    inorder(root.left)
  print(root.data)
  if root.right:
    inorder(root.right)

positive_infinity = float('inf')
negative_infinity = float('-inf')


def isbstutil(root,min,max):
  if root==None:
    return True
  if root.data<min or root.data>max:
    return False
  else:
    return isbstutil(root.left,min,root.data-1) and isbstutil(root.right,root.data+1,max)


def isbalanced(root):
  return isbstutil(root,negative_infinity,positive_infinity)

root=Node(20)
root.left=Node(10)
root.right=Node(40)
root.left.left=Node(5)
root.left.right=Node(15)
root.right.left=Node(30)
root.right.right=Node(100)

print(isbalanced(root))