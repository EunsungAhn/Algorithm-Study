N = int(input())
nums = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(N)]

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)


"""
20
5 4 6 9 8 41 3 2 1 5 4 7 5 52 4 5 5 4 5 45

7
5 4 6 9 8 41 3

5
7 3 5 7 8


4
3 5 2 7


4
9 5 4 8
"""