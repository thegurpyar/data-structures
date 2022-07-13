 
from distutils.log import error
from turtle import right


H=[42,9,18,14,7,18,12,11]
size=9   #size of heap
maxsize=13  #max no of elem
h=len(H)
while  h > size:
    H.pop()
    h-=1

def itself(elem):
    for i in range(len(H)):
        if H[i]==elem:
            return i
def parent(elem):
    for i in range(len(H)):
        if H[i]==elem:
            return i//2
def rightChild(elem):
    for i in range(len(H)):
        if H[i]==elem:
            return (2*i)+1
def leftChild(elem):
    for i in range(len(H)):
        if H[i]==elem:
            return 2*i

def shiftUp(elem):
    prt=parent(elem)
    idx=itself(elem)
    while idx >1 and H[prt] < H[idx]:
        H[prt],H[idx]=H[idx],H[prt]
        idx=parent(elem)

# def shiftDown(elem):
#     maxindex=itself(elem)
#     l=leftChild(elem)
#     if l<=size and H[l]>H[maxindex]:
#         maxindex=l
        
        
        
#     r=rightChild(elem)
#     if r<=size and H[r]>H[maxindex]:
#         maxindex=r

#     if maxindex!= elem


def insert(p):
    if size == maxsize:
        return error("error")
    else:
        size+=1
        H[size]=p
        shiftUp(size)

insert(10)