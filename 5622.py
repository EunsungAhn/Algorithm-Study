dialList = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()
time = 0
for i in word:
    for j in dialList:
        if i in j:
            time += dialList.index(j) + 3
            
print(time)