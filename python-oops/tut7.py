#magic method
class employee:
    increment=1.5
    no_of_employees=0
    def __init__(self,fname,lname,salary):
        
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=2
        employee.no_of_employees+=1
    def increase(self):
        self.salary = int(self.salary*employee.increment)
        
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
        
    @classmethod  
    def from_str(cls,strings):
        fname,lname,salary=strings.split("-")
        salary=int(salary)
        return cls(fname,lname,salary)

    @staticmethod
    def isopen(day):
        if day=="sunday":
            print ("no")
        else:
            print ("yes")

    #dunder/magic mthods

    def __add__(self,other):
        return self.salary + other.salary

    def __repr__(self):
        return(f"{self.fname}")

    def __eq__(self,other):
        return self.fname == other.fname
harry=employee("harry","ram",1)

preeti=employee("preeti","loli",2)
print(preeti+harry)   #+ = __add__
print(preeti == harry)