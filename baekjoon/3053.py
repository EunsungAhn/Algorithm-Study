import math
R = int(input())
euclidean = (R ** 2) * math.pi
taxicab = 2 * (R ** 2)
print('%.6f' % euclidean)
print('%.6f' % taxicab)