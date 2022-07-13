class queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,data):
        self.queue.insert(0,data)

    def size(self):
        return len(self.queue)


    def dequeue(self):
        if self.size():
            return self.queue.pop(0)

        else:
            return "empty queue"


que=queue()

que.enqueue(1)

print(que.dequeue())

print(que.size())