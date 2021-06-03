def preToPost(start, end):
    if start > end:
        return

    div = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > preorder[start]:
            div = i
            break

    preToPost(start + 1, div - 1)
    preToPost(div, end)
    print(preorder[start])

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

preorder = []
while True:
    try:
        node = int(input())
        preorder.append(node)
    except:
        break

preToPost(0, len(preorder) - 1)





'''
50
30
24
5
28
45
98
52
60
'''