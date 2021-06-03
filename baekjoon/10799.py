import sys
input = sys.stdin.readline

stick = input().rstrip()
result = 0
exist = 0

for i in range(len(stick)):
    if stick[i] == '(':
        exist += 1
    else:
        exist -= 1
        if stick[i - 1] == '(':
            result += exist
        else:
            result += 1

print(result)


# my first code
"""
import sys
input = sys.stdin.readline

bracket = input().rstrip()
stack = []
count = 0
countList = ['-' for i in range(len(bracket))]
tmpStack = []
maxCount = 0

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append('(')
        if bracket[i + 1] == ')':
            continue
        else:
            count += 1
            tmpStack.append(count)
            countList[i] = count
    elif bracket[i] == ')':
        stack.pop()
        if bracket[i - 1] == '(':
            countList[i] = 'l'  # laser
            continue
        else:
            if tmpStack and tmpStack[-1] == count:
                if count > maxCount:
                    maxCount = count
                tmpStack.pop()
            else:
                count = tmpStack.pop()
            countList[i] = count

exist = 0
result = 0
tmpStack = []

for i in countList:
    if type(i) == int:
        exist += 1
        if tmpStack and tmpStack[-1] == i:
            tmpStack.pop()
            exist = len(tmpStack)
        else:
            tmpStack.append(i)
            result += 1
    
    if i == 'l':
        result += exist        

print(result)
"""