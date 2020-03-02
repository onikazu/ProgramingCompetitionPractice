v, e = map(int, input().split())
cost = [[float("inf")] * v for _ in range(v)]

for _ in range(e):
    s, t, d = map(int, input().split())
    cost[s][t] = d

dp = [float("inf")] * 2 ** v

for i in range(v):
    dp[(1 << i) + 1] = 

