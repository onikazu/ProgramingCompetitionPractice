# napsack
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
weights = [2, 5, 5, 4, 5, 6, 3, 7, 6]

dp =[[0] * (len(a) + 1)] * (n + 1)




