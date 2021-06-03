import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def divide(in_s, in_e, post_s, post_e):
    if (in_s > in_e) or (post_s > post_e):
        return

    root = postorder[post_e]
    print(root, end = ' ')
    
    divide(in_s, pos[root] - 1, post_s, post_s + pos[root] - in_s - 1)
    divide(pos[root] + 1, in_e, post_s + pos[root] - in_s, post_e - 1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
# position
pos = [0 for _ in range(n + 1)]

for i in range(n):
    pos[inorder[i]] = i

divide(0, n - 1, 0, n - 1)


'''
3
1 2 3
1 3 2

7
4 2 5 1 6 3 7
4 5 2 6 7 3 1
'''