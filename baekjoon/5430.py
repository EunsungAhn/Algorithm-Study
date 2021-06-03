import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = str(input().rstrip())
    n = int(input())
    array = input().rstrip()[1:-1].split(',')
    p = p.replace('RR', '')
    
    count_R = 0
    front = 0
    back = 0
    
    for i in p:
        if i == 'R':
            count_R += 1
        elif i == 'D':
            if count_R % 2 == 0:
                front += 1
            else:
                back += 1
    
    if front + back <= n:
        array = array[front:n-back]
        if count_R % 2 == 0:
            print('['+','.join(array)+']')
        else:
            print('['+','.join(array[::-1])+']')
    else:
        print('error')