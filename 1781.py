import sys
input = sys.stdin.readline

N = int(input())
problemInfo = []

for i in range(N):
    deadline, number = map(int, input().split())
    problemInfo.append((deadline, number))

problemInfo.sort()

time = 0
cupramyun = []
for p in problemInfo:
    time = p[0]
    cupramyun.append(p[1])
    while time < len(cupramyun):
        cupramyun.remove(min(cupramyun))

print(sum(cupramyun))

"""
7
1 6
1 7
3 2
3 1
2 4
2 5
6 1

9
5 5
4 6
4 12
3 8
4 18
2 10
2 5
1 7
1 14
"""