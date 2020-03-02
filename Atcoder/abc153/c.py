n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

h = sorted(h)
if k == 0:
    print(sum(h))
elif k >= len(h):
    print(0)
else:
    print(sum(h[:-k]))

