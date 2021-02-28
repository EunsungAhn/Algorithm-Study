import sys
from collections import deque
input = sys.stdin.readline

card = deque()
for i in  range(1, int(input())+1):
    card.append(i)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])