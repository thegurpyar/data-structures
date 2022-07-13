#increment variables == jo user deta hai

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

harry=employee("harry","jackson",44000)     #instance variable

rohan=employee("rohan","das",10000)

print(harry.salary)

employee.change_increment(3)  #both employee or harry
harry.increase()
print(harry.salary)
