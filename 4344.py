C = int(input())

for i in range(C):
    scoreList = list(map(int, input().split()))
    avg = sum(scoreList[1:]) / scoreList[0]
    count = 0
    
    for score in scoreList[1:]:
        if score > avg:
            count += 1
            
    rate = count / scoreList[0] * 100
    print(f'{rate:.3f}%')