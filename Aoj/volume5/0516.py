n_l = []
k_l = []
a_l = []

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    a = [int(input()) for _ in range(n)]
    a_l.append(a)
    n_l.append(n)
    k_l.append(k)

for i, n in enumerate(n_l):
    accum_sum = [0] * (n + 1)
    a = a_l[i]
    k = k_l[i]
    # 累積和の作成
    for j in range(n):
        accum_sum[j+1] = accum_sum[j] + a[j]

    res = -float("inf")
    for j in range(n-k+1):
        res = max(res, accum_sum[j+k]-accum_sum[j])
    print(res)

    
