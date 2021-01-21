nonSelfNumber = []
for i in range(1, 10001):
    tmpNum = i
    tmpSum = i
    
    while tmpNum > 0:
        tmpSum += tmpNum % 10
        tmpNum = int(tmpNum / 10)
    
    if tmpSum <= 10000:
        nonSelfNumber.append(tmpSum)

selfNumber = []
for i in range(1, 10001):
    existStatus = None
    for j in nonSelfNumber:
        if i == j:
            existStatus = True
            break
    if existStatus == None:
        selfNumber.append(i)

for n in selfNumber:
    print(n)