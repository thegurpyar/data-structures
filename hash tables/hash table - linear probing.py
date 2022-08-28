
class HashTable:
    def __init__(self,max):
        self.max=max        #stores max val of has table
        self.arr=[[]for x in range(self.max)]  #using linked list
    
    def hash(self,key):

        hashkey=key%(self.max)
        return hashkey
    
    def rehash(self,oldhash,i):
        hashkey=(oldhash+i)%self.max
        if hashkey is not None and hashkey<self.max:
            return hashkey

    def __setitem__(self,key,value):
        hashvalue=self.hash(key)
        if self.arr[hashvalue]==[]:
            self.arr[hashvalue]=[key,value]

        elif self.arr[hashvalue][0]==key:

            self.arr[hashvalue][1]=value
        else:
            for i in range(self.max):
                nextbucket=self.rehash(hashvalue,i)
                if self.arr[nextbucket]==[]:
                    self.arr[nextbucket]=[key,value]
                    break
                else:
                    if self.arr[nextbucket][0]==key:
                        self.arr[nextbucket][1]=value
                        break


    def __getitem__(self,key):
        hashvalue=self.hash(key)
        if self.arr[hashvalue][0]==key:
            return self.arr[hashvalue][1]
        else:
            for i in range(self.max):
                nextbucket=self.rehash(hashvalue,i)
                if self.arr[nextbucket][0]==key:
                    return self.arr[nextbucket][1]
                else:
                    return None
    def __delitem__(self,key):
        hashvalue=self.hash(key)
        if self.arr[hashvalue][0]==key:
            self.arr[hashvalue]=[]
        else:
            for i in range(self.max):
                nextbucket=self.rehash(hashvalue,i)
                if self.arr[nextbucket][0]==key:
                    del self.arr[nextbucket]
                    break

        
                    
H=HashTable(10)
H[54]="books"
H[24]="cooks"
H[34]="seggs"
H[44]="seggs"
H[64]="seggs"
H[74]="seggs"
H[24]="seggs"
H[94]="seggs"
H[22]="KILLS"
H[24]="muswcte"
H[4]="ii"
H[99]="433"
print(H.arr)

