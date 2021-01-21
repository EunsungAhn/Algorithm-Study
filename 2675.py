T = int(input())
for i in range(T):
    N, S = input().split()
    for i in S:
        print(i * int(N), end = '')
    print() # 줄바꿈