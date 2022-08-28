

class HashTable:
    def __init__(self,max):
        self.max=max        #stores max val of has table
        self.arr=[[]for x in range(self.max)]   #using linked list
    
    def get_hash(self,key):         #stores date by total sum/100
        sum=0
        for c in key:
            sum+=ord(c)
        return sum % self.max
        
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=None
        for index,element in enumerate (self.arr[h]):
            if(element[0]==key and len(element)==2):
                self.arr[h][index]=(key,val)
                found=True
        if not found:
            self.arr[h].append((key,val))    
    def __getitem__(self,key):
        h=self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0]==key:          #0=key
                return kv[1]        #1=val
        

    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,elem in enumerate(self.arr[h]):
            if elem[0]==key:
                del self.arr[h][index]


H=HashTable(10)
H["march 17"]=459
H["march 17"]=1
H["march 6"]=36
H["march 65"]=56
del H["march 17"]
print(H.arr)
# array=[9,8,7,6,5,4,4,32]
# for index,elem in enumerate(array):
#     print(index,elem)