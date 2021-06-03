a, b = input().split()

def backward(n):
    units = n % 10
    tens = (n % 100) // 10
    hundreds = n // 100
    newNum = 100 * units + 10 * tens + hundreds
    return newNum

print(max(backward(int(a)), backward(int(b))))