N = int(input())
numStr = input()
result = 0

for digit in numStr:
    result += int(digit)

print(result)