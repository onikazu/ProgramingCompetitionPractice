n = int(input())

dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

if n < 2:
    print(1)
    exit()

for i in range(2, len(dp)):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[-1])


