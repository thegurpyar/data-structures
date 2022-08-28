
class HashTable:
    def __init__(self,max):
        self.max=max        #stores max val of has table
        self.arr=[None]*self.max
    
    def get_hash(self,key):         #stores date by total sum/100
        sum=0
        for c in key:
            sum+=ord(c)
        return sum % self.max
        
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
        

    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None




