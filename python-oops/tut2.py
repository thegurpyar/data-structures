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
        
            

harry=employee("harry","jackson",44000)     #instance variable

rohan=employee("rohan","das",10000)

#rohan.increment=0
print(rohan.salary)
rohan.increase()
print(rohan.salary)

print(employee.no_of_employees)
