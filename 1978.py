N = int(input())
numList = list(map(int, input().split()))
count = 0
for i in numList:
    status = True
    if i <= 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            status = False
            break
    if status == True:
        count += 1
print(count)