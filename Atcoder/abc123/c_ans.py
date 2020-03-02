import math
n = int(input())
trans = [int(input()) for _ in range(5)]

min_trans = min(trans)
print(math.ceil(n/min_trans) + 4)
