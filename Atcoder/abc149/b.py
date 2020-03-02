a, b, k = list(map(int, input().split()))

if k >= a:
    print(0, max(0, b-k+a))
else:
    print(a-k, b)
