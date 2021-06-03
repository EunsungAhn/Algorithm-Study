import sys
input = sys.stdin.readline

string = input().rstrip()
explosion = input().rstrip()
length = len(explosion)
stack = []

for c in string:
    stack.append(c)
    if c == explosion[-1] and ''.join(stack[-length:]) == explosion:
        del stack[-length:]

if stack:
    print(''.join(stack))
else:
    print('FRULA')