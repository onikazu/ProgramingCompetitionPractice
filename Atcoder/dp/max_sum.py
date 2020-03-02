def max_sum(N, a):
    """
    N: length of a
    a: target array
    """
    dp = [0] * N
    for i in range(1, N):
        dp[i] = max(dp[i-1]+a[i], dp[i-1])
    return dp[N - 1]
