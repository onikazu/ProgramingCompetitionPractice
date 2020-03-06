n = int(input())
c = [int(input()) for _ in range(n)]
INF = float("inf")

dp = [c[0]]

for i in range(len(c)):
    v = c[i]
    l = 0
    r = len(dp) - 1

    if dp[r] < v:
        dp.append(v)
    elif len(dp) > 1:
        while r - l > 1:
            mid = (l + r) // 2
            if dp[mid] > v:
                r = mid
            else:
                l = mid
print(len(c)-len(dp))



