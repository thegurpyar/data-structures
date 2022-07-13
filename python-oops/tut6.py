#inheritance
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

class programmer(employee):

    def __init__(self,fname,lname,salary,lan,exp):
        super().__init__(fname,lname,salary)
 
        self.exp=exp

harry=programmer("harry","jackson",44000,"js","5")     #instance variable
print(harry.exp)
