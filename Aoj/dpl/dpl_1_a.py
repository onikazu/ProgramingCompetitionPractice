n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [float("inf")] * (n+1)
dp[0] = 0

for i in range(len(dp)):
    for j in range(len(c)):
        if c[j] > i:
            dp[i] = min(dp[i], dp[i-1]+1)
        else:
            dp[i] = min(dp[i-c[j]]+1, dp[i])
print(dp[-1])

