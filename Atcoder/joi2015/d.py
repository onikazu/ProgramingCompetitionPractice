n, m = map(int, input().split())
d = [int(input()) for _ in range(n)]
c = [int(input()) for _ in range(m)]

# initialize dp
dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(1, len(dp[0])):
    dp[0][i] = float("inf")

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = min(dp[i-1][j-1]+d[j-1]*c[i-1], dp[i-1][j])

ans = [dp[i][-1] for i in range(m+1)]
print(min(ans))



