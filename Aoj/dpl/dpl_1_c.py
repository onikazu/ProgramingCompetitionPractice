n, w = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (w+1)

for i in range(1, w+1):
    for item in items:
        v, w = item
        if i < w:
            dp[i] = max(dp[i], dp[i-1])
        else:
            dp[i] = max(dp[i], dp[i-1], dp[i-w]+v)
print(dp[-1])


