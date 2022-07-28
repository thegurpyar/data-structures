
class Heap:
    def __init__(self, capacity):
        self.storage = [0]*capacity  # creating an empty list of n size
        self.capacity = capacity
        self.size = 0  # size a new variable prseting number of elements
        self.sorted=[0]*self.capacity
        
    def parent(self, index):
        return (index-1)//2

    def leftchild(self, index):
        return (2*index)+(1)

    def rightchild(self, index):
        return (2*index)+(2)

    def hasparent(self, index):
        return self.parent(index) >= 0

    def hasleftchild(self, index):
        return self.leftchild(index) < self.size

    def hasrightchild(self, index):
        return self.rightchild(index) < self.size

    def isfull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def shiftup(self):
        index = self.size-1
        prt = self.parent(index)
        while self.hasparent(index) and self.storage[index] > self.storage[prt]:
            self.swap(self.parent(index), index)
        index = prt

    def insert(self, data):
        if self.isfull():
            raise("error")
        else:
            self.storage[self.size] = data
            self.size += 1
            self.shiftuprec(self.size-1)

    def shiftuprec(self, index):
        prt = self.parent(index)
        if self.hasparent(index) and self.storage[index] > self.storage[prt]:
            self.swap(prt, index)
            self.shiftuprec(self.parent(index))

    
    def shiftdown(self, index):
        greater=index

        if(self.hasleftchild(index) and self.storage[greater] < self.storage[self.leftchild(index)]):
            greater=self.leftchild(index)

        if(self.hasrightchild(index) and self.storage[greater] < self.storage[self.rightchild(index)]):
            greater=self.rightchild(index)
        
        if (greater!=index):
            
            self.swap(greater,index)
            
            self.shiftdown(greater)
    def removemax(self):
        if self.size == 0:
            raise ("error")
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size-1]
            self.size -= 1
            self.shiftdown(0)
            return data

    def getval(self):
        print(self.storage)

    def heapsort(self):
        for i in range(self.size, 1, -1):  # sabse bada sabse end me
            self.sorted[i] = self.removemax()
        return self.sorted






H = Heap(10)
H.insert(50)
H.insert(30)
H.insert(18)
H.insert(29)
H.insert(40)
H.insert(19)


print(H.heapsort())
print(H.getval())