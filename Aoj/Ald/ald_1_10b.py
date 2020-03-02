n = int(input())
r = [0] * n
c = [0] * n

for i in range(n):
    r[i], c[i] = map(int, input().split())

dp = [[float("inf")] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for l in range(1, n):
    for i in range(n-l):
        a0 = r[i]
        c0 = c[i+l]
        dp[i][i+l] = min(a0*c[j]*c0 + dp[i][j] + dp[j+1][i+l] for j in range(i, i+l))

print(dp[0][n-1])


