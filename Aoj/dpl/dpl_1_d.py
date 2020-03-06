# o(n^2) の解法
# o(nlogn)の解法でないとtle
# python がだめ？
n = int(input())
a = [int(input()) for _ in range(n)]

"""
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
"""

dp = [a[0]]
for i in range(1, len(a)):
    l = 0
    r = len(dp) - 1
    if dp[r] < a[i]:
        dp.append(a[i])
    elif dp[l] > a[i]:
        dp[l] = a[i]
    else:
        while r - l > 1:
            mid = (l+r) // 2
            if dp[mid] > a[i]:
                mid = r
            else:
                mid = l
        dp[r] = a[i]
print(len(dp))


