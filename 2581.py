def isPrime(n):
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
        i += 1
    return 1

M = int(input())
N = int(input())
count = 0
sum = 0
min = -1

for i in range(M, N + 1):
    if isPrime(i) == 1:
        if min == -1:
            min = i
        count += 1
        sum += i

if count == 0:
    print('-1')
else:
    print(sum)
    print(min)    