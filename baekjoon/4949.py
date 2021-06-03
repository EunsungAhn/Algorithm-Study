import sys
input = sys.stdin.readline

while True:
    stack = []
    balance = None
    line = input().rstrip()
    if line == '.':
        break
    
    for c in line:
        if c in '[]()':
            if c in '[(':
                stack.append(c)
            elif c == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif c == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                balance = False
                
    if balance != False and len(stack) == 0:
        print('yes')
    else:
        print('no')