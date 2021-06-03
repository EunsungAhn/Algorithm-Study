N = int(input())
coor = []   # coordinate
for i in range(N):
    x, y = map(int, input().split())
    coor.append((y, x))
coor = sorted(coor)
for i in range(N):
    print(coor[i][1], coor[i][0])