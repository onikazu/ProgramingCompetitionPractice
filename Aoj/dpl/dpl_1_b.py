n, limit = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [([0] + [0] * limit) for _ in range(n+1)]

for i in range(1, n+1):
    v, w = items[i-1]
    for j in range(limit+1):
        if j < w:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v) 
print(dp[-1][-1])

