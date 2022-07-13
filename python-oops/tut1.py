class employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.bp=0

harry=employee("harry","jackson",44000)

rohan=employee("rohan","das",10000)

print(rohan.bp)
