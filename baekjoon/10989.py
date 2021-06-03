import sys
N = int(sys.stdin.readline())
countList = [0] * 10001
for _ in range(N):
    countList[int(sys.stdin.readline())] += 1
for i in range(10001):
    sys.stdout.write((str(i) +'\n') * countList[i])