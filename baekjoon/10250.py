import math
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    unit = math.ceil(N/H)
    if floor == 0:
        floor = H
    print(floor*100 + unit)