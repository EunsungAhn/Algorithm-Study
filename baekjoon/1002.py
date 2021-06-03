import math
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    bigR = max(r1, r2)
    smallR = min(r1, r2)
        
    if d == 0 and r1 == r2:
        print('-1')
    elif d > r1 + r2 or d == 0 or d + smallR < bigR:
            print('0')
    # 내접의 경우를 빠트림
    elif d == r1 + r2 or d + smallR == bigR:
        print('1')
    elif d < r1 + r2:
        print('2')