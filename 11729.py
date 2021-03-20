import sys
input = sys.stdin.readline

def hanoi(N, from_, other, to):
    if N == 1:
        print(from_, to)
    else:
        hanoi(N - 1, from_, to, other)
        print(from_, to)
        hanoi(N - 1, other, from_, to)

N = int(input())
print(pow(2, N) - 1)
hanoi(N, 1, 2, 3)