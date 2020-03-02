n, m = map(int, input().split())
a = set([int(input()) for _ in range(m)])
NUM = 10 ** 9 + 7

dp = [0] * (n+1)
dp[0] = 1
if not 1 in a:
    dp[1] = 1

for i in range(2, n+1):
    if not i in a:
        dp[i] = (dp[i-2] + dp[i-1]) % NUM
    else:
        dp[i] = 0

print(dp[n])


