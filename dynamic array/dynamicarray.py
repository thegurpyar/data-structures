import ctypes
from tkinter.messagebox import RETRY
class dynamicArray(object):
    
    def __init__ (self):
        self.n=0 #by default
        self.capacity=1  #by default
        self.A = self.make_array(self.capacity) #it will be defined later


    #get length
    def traverse(self):
        for i in range(self.n):
            print(self.A[i])

    def __len__(self):
        return self.n

    #get item at k

    def get_item(self,k):
        if k<0 or k>self.n:
            return IndexError ("list index out of range")
        else:
            return self.A[k]
            
            
    #append

    def append(self,element):
        if self.n == self.capacity:     #full
            #resize
            self.resize(2*self.capacity)

        # pointer
        self.A[self.n] = element
        self.n += 1

    #resize function
    def resize(self,new_cap):
        B=self.make_array(new_cap)
        for k in range(self.n):
            B[k]=self.A[k]
        self.A=B

    #making the make-array method using ctypes
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()

arr=dynamicArray()
arr.append(1)
arr.append(2)
print(arr.traverse())