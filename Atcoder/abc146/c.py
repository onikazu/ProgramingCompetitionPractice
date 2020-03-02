import sys


a, b, x = list(map(int, input().split()))

if x < a + b:
    print(0)
    sys.exit(0)

left = 1
right = 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if x < mid * a + len(str(mid)) * b:
        right = mid - 1
    elif x > mid * a + len(str(mid)) * b:
        left = mid + 1
    else:
        print(mid)
        sys.exit(0)
print(mid)










