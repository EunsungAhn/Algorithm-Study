import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    check = [False] * N
    check[M] = True
    count = 0
    
    while len(importance) > 0:
        maximum = max(importance)
        if importance[0] == max(importance) and check[0] == False:
            importance.pop(0)
            check.pop(0)
            count += 1
        elif importance[0] == max(importance) and check[0] == True:
            count += 1
            break
        else:
            importance.append(importance.pop(0))
            check.append(check.pop(0))
    
    print(count)