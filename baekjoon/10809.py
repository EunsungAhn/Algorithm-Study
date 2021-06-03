S = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
position = [-1 for i in range(26)]

for i in S:
    if position[alphabet.index(i)] == -1:
        position[alphabet.index(i)] = S.index(i)

for i in range(26):
    print(position[i], end = ' ')