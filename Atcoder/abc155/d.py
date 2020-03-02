from heapq import heappush, heappop


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

d = {}

h = []
for i in range(len(a)):
    if i == 0:
        heappush(h, (a[i] * a[0], i, 0, False))
    else:
        heappush(h, (a[i] * a[0], i, 0, True))


res = []
for _ in range(k):
    seki, i, j, flag = (0, 0, 0, 0)
    while True:
        seki, i, j, flag = heappop(h)
        if flag is True:
            break
    res.append(seki)
    if j+1 < len(a):
        if j+1 == i:
            pass
        else:
            heappush(h, (a[i] * a[j+1], i, j+1, True))

print(res[-1])


