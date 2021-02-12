import sys
input = sys.stdin.readline

N = int(input())
count = 0
for i in range(N):
    stack = []
    word = input().rstrip()
    for c in word:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        count += 1

print(count)