q = int(input())
dataset = []
for i in range(q):
    data = []
    data.append(input())
    data.append(input())
    dataset.append(data)

for data in dataset:
    x, y = data
    dp = [[0] * len(x) for _ in range(len(y))]
    for i in range(len(dp[0])):
        if x[i] == y[0]:
            dp[0][i] = 1
        elif i > 0:
            dp[0][i] = dp[0][i-1]

    for i in range(len(dp)):
        if x[0] == y[i]:
            dp[i][0] = 1
        elif i > 0:
            dp[i][0] = dp[i-1][0]

    for i in range(1, len(dp[0])):
        for j in range(1, len(dp)):
            if x[i] == y[j]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])
    print(dp[-1][-1])





