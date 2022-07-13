class stack:
    def __init__(self,n):
        self.size=n+1
        self.stack=[]
      

    def push(self,data):
        if len(self.stack)- self.size !=0:
            
            self.stack.append(data)
            
        else:
            return "stack overflow"


    def peek(self):
        return self.stack[-1]

    def pop(self):
        if len(self.stack)<=0:
            return ("stack underflow")

        else:
            return self.stack.pop()


stack=stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.push(5))
print(stack.push(5))
#print(stack.peek())
#stack.push("a")
#stack.push("b")
#stack.push("c")

#print(stack.peek())
#print(stack.pop())
