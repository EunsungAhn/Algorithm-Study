import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)
wantToPop = list(map(int, input().split()))

count = 0
while len(wantToPop) > 0:
    # 1
    if queue.index(wantToPop[0]) == 0:
        queue.popleft()
        wantToPop.pop(0)
    # 2
    elif queue.index(wantToPop[0]) < len(queue) / 2:
        queue.append(queue.popleft())
        count += 1
    # 3
    elif queue.index(wantToPop[0]) >= len(queue) / 2:
        queue.appendleft(queue.pop())
        count += 1

print(count)