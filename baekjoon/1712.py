A, B, C = map(int, input().split())

if B >= C:
    print('-1')
else:
    BEP = A // (C - B) + 1
    print(BEP)