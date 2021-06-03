T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    j = 1
    while True:
        min = j * j - j + 1
        max = j * j + j
        if distance >= min and distance <= max:
            break
        j += 1
    if distance >= min and distance <= (j * j):
        print(j * 2 - 1)
    else:
        print(j * 2)