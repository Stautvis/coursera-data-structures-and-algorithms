#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = dict()
        self.__max[0] = 0
        self.n = 0

    def Push(self, a):
        self.__stack.append(a)
        self.n += 1
        self.__max[self.n] = max(self.__max[self.n - 1], a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.n -= 1

    def Max(self):
        assert(len(self.__stack))
        return self.__max[self.n]


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
