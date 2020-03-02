N = input()
m = len(N)
dp = [[0] * 2 for _ in range(m + 1)]
dp[0][0] = 1

for i in range(1, m + 1):
    dp[i][0] = dp[i - 1][0]
    dp[i][1] = dp[i - 1][1] * 10 + dp[i - 1][0] * int(N[i - 1])

ans = dp[m][0] + dp[m][1]

print(ans)
