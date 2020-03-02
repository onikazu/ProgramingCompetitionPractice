d, n = map(int, input().split())
t = [int(input()) for _ in range(d)]
clothes = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[-float("inf")] * n for _ in range(d)]

prev_max = -float("inf")
prev_clothes_c = 0 
for i in range(d):
    if i > 0:
        prev_max = max(dp[i-1])
        prev_clothes_c = clothes[dp[i-1].index(prev_max)][2]
    for j in range(n):
        a, b, c = clothes[j]
        if a <= t[i] <= b:
            if i == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = prev_max + abs(prev_clothes_c - c) 
        else:
            continue
print(max(dp[-1]))
