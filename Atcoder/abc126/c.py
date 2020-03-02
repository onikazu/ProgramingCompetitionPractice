n, k = map(int, input().split())

ans = 0
for i in range(1, n+1):
    p = 1 / n
    point = i
    while True:
        if point >= k:
            break
        else:
            point *= 2
            p *= 0.5
    ans += p
print(ans)





