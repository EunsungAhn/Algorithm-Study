import sys
from collections import deque
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.data = deque()
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.data:
            return self.data.popleft()
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
queue = Queue()
for i in range(N):
    command = input().rstrip().split()
    
    if command[0] == 'push':
        queue.push(command[1])

    elif command[0] == 'pop':
        print(queue.pop())

    elif command[0] == 'size':
        print(queue.size())

    elif command[0] == 'empty':
        print(queue.empty())

    elif command[0] == 'front':
        print(queue.front())
    
    elif command[0] == 'back':
        print(queue.back())

# queue를 구현하는 문제인데 왜 시간복잡도 때문에 deque를 사용해야 하는지 모르겠음