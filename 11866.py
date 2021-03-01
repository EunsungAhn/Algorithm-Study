import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
seat = deque()
answer = []
for i in range(1, N+1):
    seat.append(i)

while len(seat) >= 1:
    for _ in range(K-1):
        seat.append(seat.popleft())
    answer.append(seat.popleft())

print('<%s>' % ', '.join(map(str, answer)))