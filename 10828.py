import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)
        
    def pop(self):
        if self.data:
            return self.data.pop(-1)
        else:
            return -1
    
    def size(self):
        return len(self.data)
    
    def empty(self):
        if self.data:
            return 0
        else:
            return 1
    
    def top(self):
        if self.data:
            return self.data[-1]
        else:
            return -1

N = int(input())
stk = Stack()
for i in range(N):
    command = input().rstrip().split()
    
    if command[0] == 'push':
        stk.push(command[1])

    elif command[0] == 'pop':
        print(stk.pop())

    elif command[0] == 'size':
        print(stk.size())

    elif command[0] == 'empty':
        print(stk.empty())

    elif command[0] == 'top':
        print(stk.top())
    