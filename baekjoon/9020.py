def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

T = int(input())
for i in range(T):
    n = int(input())
    for j in range(n // 2, 0, -1):
        if isPrime(j) == True and isPrime(n - j) == True:
            print(j, n - j)
            break