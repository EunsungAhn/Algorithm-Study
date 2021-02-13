import sys
from collections import deque
input = sys.stdin.readline

class Deque:
    def __init__(self):
        self.data = deque()
    
    def push_front(self, item):
        self.data.appendleft(item)
    
    def push_back(self, item):
        self.data.append(item)
    
    def pop_front(self):
        if self.data:
            return self.data.popleft()
        else:
            return -1
    
    def pop_back(self):
        if self.data:
            return self.data.pop()
        else:
            return -1
    
    def size(self):
        return len(self.data)
    
    def empty(self):
        if self.data:
            return 0
        else:
            return 1

    def front(self):
        if self.data:
            return self.data[0]
        else:
            return -1
    
    def back(self):
        if self.data:
            return self.data[-1]
        else:
            return -1

N = int(input())
deque = Deque()
for i in range(N):
    command = input().rstrip().split()
    
    if command[0] == 'push_front':
        deque.push_front(command[1])
    
    elif command[0] == 'push_back':
        deque.push_back(command[1])
    
    elif command[0] == 'pop_front':
        print(deque.pop_front())
    
    elif command[0] == 'pop_back':
        print(deque.pop_back())

    elif command[0] == 'size':
        print(deque.size())

    elif command[0] == 'empty':
        print(deque.empty())

    elif command[0] == 'front':
        print(deque.front())
    
    elif command[0] == 'back':
        print(deque.back())