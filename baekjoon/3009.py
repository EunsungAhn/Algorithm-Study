x = []
y = []

for i in range(3):
    tmp_x, tmp_y = map(str, input().split())
    x.append(tmp_x)
    y.append(tmp_y)

x.sort()
y.sort()

forthCoor = []
if x[0] == x[1]:
    forthCoor.append(x[2])
else:
    forthCoor.append(x[0])
if y[0] == y[1]:
    forthCoor.append(y[2])
else:
    forthCoor.append(y[0])

print(' '.join(forthCoor))