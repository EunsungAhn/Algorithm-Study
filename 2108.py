import sys

N = int(sys.stdin.readline())
numList = []
for i in range(N):
    numList.append(int(sys.stdin.readline()))
numList.sort()

# arithmetic mean
print(round(sum(numList) / N))

# median
# excepted the case that N is even
print(numList[N // 2])

# mode
from collections import Counter
countList = Counter(numList).most_common(2)
if N == 1:
    print(numList[0])
else:
    if countList[0][1] == countList[1][1]:
        print(countList[1][0])
    else:
        print(countList[0][0])

# range
print(numList[N - 1] - numList[0])
