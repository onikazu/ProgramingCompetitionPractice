n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = float("inf")
for i in range(len(x)-(k-1)):
    xl = x[i]
    xr = x[i+k-1]
    candidate = min(abs(xl) + abs(xr-xl), abs(xr) + abs(xl-xr))
    ans = min(ans, candidate)

print(ans)

