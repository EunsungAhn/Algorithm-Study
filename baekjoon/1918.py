import sys
input = sys.stdin.readline

priority = {'*': 2, '/': 2,
            '+': 1, '-': 1,
            '(': 0}
operator = []
infix = input().rstrip()
for c in infix:
    if c == '(':
        operator.append(c)
    
    elif c == ')':
        while True:
            top = operator.pop()
            if top == '(':
                break
            print(top, end='')
    
    elif c in '+-*/':
        if len(operator) == 0:
            operator.append(c)
        else:
            while len(operator) != 0 and priority[operator[-1]] >= priority[c]:            
                print(operator.pop(), end='')
            operator.append(c)
    
    else:
        print(c, end='')

while len(operator) > 0:
    print(operator.pop(), end='')