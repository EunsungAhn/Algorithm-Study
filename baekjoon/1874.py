import sys
input = sys.stdin.readline

def push(stack, integer):
    global result
    stack.append(integer)
    result.append('+')

def pop(stack):
    global maxPop
    global result
    poppedN = stack.pop()
    if poppedN > maxPop:
        maxPop = poppedN
    result.append('-')

stack = []
result = []
status = None
maxPop = 0
n = int(input())
for i in range(1, n + 1):
    progression = int(input())
    if len(stack) == 0:
        if maxPop == 0:
            for j in range(1, progression + 1):
                push(stack, j)
            pop(stack)
        else:
            for j in range(maxPop + 1, progression + 1):
                push(stack, j)
            pop(stack)
    elif stack[-1] == progression:
        pop(stack)
    elif stack[-1] < progression:
        for j in range(maxPop + 1, progression + 1):
            push(stack, j)
        pop(stack)
    else:
        status = False
        break

if status != False:
    for c in result:
        print(c)
else:
    print('NO')