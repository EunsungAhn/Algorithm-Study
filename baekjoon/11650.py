N = int(input())
coor = []   # coordinate
for i in range(N):
    x, y = map(int, input().split())
    coor.append((x, y))
coor = sorted(coor)
for i in range(N):
    print(coor[i][0], coor[i][1])