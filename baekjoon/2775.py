import math
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(math.comb(k+n, k+1))