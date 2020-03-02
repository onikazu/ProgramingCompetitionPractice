import numpy as np


n = int(input())
flag = [list(input()) for _ in range(5)]

dp = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
    row_colors = [flag[j][i-1] for j in range(5)]
    for j, color in enumerate(["R", "B", "W"]):
        cnt = 0
        for row_color in row_colors:
            if row_color != color:
                cnt += 1
        dp[i][j] = min(dp[i-1][:j]+dp[i-1][j:]) + cnt
print(np.asarray(dp))

print(min(dp[n]))

