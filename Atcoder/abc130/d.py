n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
s = 0
j = 0

for i in range(n):
    while s < k:
        if j == n:
            break
        s += a[j]
        j += 1
    if s >= k:
        ans += n - j + 1
        s -= a[i]
print(ans)
