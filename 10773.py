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
    
    def sum(self):
        return sum(self.data)

K = int(input().rstrip())
stk = Stack()

for i in range(K):
    N = int(input())
    if N == 0:
        stk.pop()
    else:
        stk.push(N)

print(stk.sum())