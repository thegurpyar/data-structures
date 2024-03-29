#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max=[0]
    def Push(self, a):
        self.__stack.append(a)
        if stack.max[-1] <= a:
            self.max.append(a)



    def Pop(self):
        assert(len(self.__stack))
        rm=self.__stack.pop()
        if rm == self.max[-1] :
            self.max.pop(-1)
            
    def Max(self):
        assert(len(self.__stack))
        return self.max[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
