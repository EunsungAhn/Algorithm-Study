from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = {i:[] for i in range(1, N + 1)}
parents = [0] * (N + 1)

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

while queue:
    tmp = queue.popleft()
    for element in graph[tmp]:
        if parents[tmp] != element:
            parents[element] = tmp
            queue.append(element)

for i in parents[2:]:
    print(i)


'''
7
1 6
6 3
3 5
4 1
2 4
4 7


12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12

'''