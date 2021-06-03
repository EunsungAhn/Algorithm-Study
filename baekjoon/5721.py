import sys
input = sys.stdin.readline

M, N = map(int, input().split())
while M != 0 and N != 0:
    # 2차원 리스트에 입력받기
    candyList = []
    for i in range(M):
        candyList.append(list(map(int, input().split())))
    
    print(candyList)
    
    count = 0
    while True:
        tmpList = []
        for i in range(M):
            tmpList.append(max(candyList[i]))
        
        if sum(tmpList) = 0:
            break
        
        print(tmpList.index(max(tmpList)))
        
        
        
        
    
    print(ount)
    M, N = map(int, input().split())

"""
5 5
1 8 2 1 9
1 7 3 5 2
1 2 10 3 10
8 4 7 9 1v
7 1 3 1 6
0 0
"""


import sys
input = sys.stdin.readline

M, N = map(int, input().split())
while M != 0 and N != 0:
    # 2차원 리스트에 입력받기
    candyList = []
    for i in range(M):
        candyList.append(list(map(int, input().split())))
    # print(candyList)
    
    count = 0
    while True:
        # 각 행의 사탕의 최대 개수를 리스트로 만듦
        tmpList = []
        for i in range(M):
            tmpList.append(max(candyList[i]))
        
        # 사탕을 다 가져간 경우 while문 종료
        if sum(tmpList) == 0:
            break
        
        # row = 참가자가 고른 박스의 행
        row = tmpList.index(max(tmpList))
        # col = 참가자가 고른 박스의 열
        col = candyList[row].index(tmpList[row])
        
        count += candyList[row][col]
        
        # 고른 박스의 양 옆과 위 아래 행을 0으로 만듦
        candyList[row][col] = 0
        if col != 0:    # 좌
            candyList[row][col-1] = 0
        if col != N-1:  # 우
            candyList[row][col+1] = 0
        if row != 0:    # 위
            for i in range(N):
                candyList[row-1][i] = 0
        if row != M-1:  # 아래
            for i in range(N):
                candyList[row+1][i] = 0
        
    print(count) 
    M, N = map(int, input().split())

"""
5 5
1 8 2 1 9
1 7 3 5 2
1 2 10 3 10
8 4 7 9 1
7 1 3 1 6
4 4
10 1 1 10
1 1 1 1
1 1 1 1
10 1 1 10
2 4
9 10 2 7
5 1 1 5
0 0


5 5
1 8 2 1 9
1 7 3 5 2
1 2 10 3 10
8 4 7 9 1
7 1 3 1 6
0 0


"""