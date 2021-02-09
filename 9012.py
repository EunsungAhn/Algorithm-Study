import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
        # print(self.data)
    
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

T = int(input())
for i in range(T):
    line = input().rstrip()
    stk = Stack()
    isVPS = None
    
    for j in line:
        if j == '(':
            stk.push(j)
        elif j == ')' and stk.top() == '(':
            stk.pop()
        elif j == ')' and stk.top() != '(':
            isVPS = False
            break
    if isVPS == False or stk.empty() == 0:
        print('NO')
    elif isVPS != False:
        print('YES')