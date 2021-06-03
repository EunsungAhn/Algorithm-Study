N = int(input())

line = 0
while N > 0:
    line += 1
    N -= line
N += line

if line % 2 == 1:
    print(line + 1 - N, "/", N, sep="")
else:
    print(N, "/", line + 1 - N, sep="")