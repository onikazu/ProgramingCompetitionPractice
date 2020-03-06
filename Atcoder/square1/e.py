n, q = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
MOD = 10 ** 9 + 7

def super_pow(x, n):
    ans = 1
    while(n > 0):
        if(bin(n & 1) == bin(1)):
            ans = ans*x
        x = x*x
        n = n >> 1 #ビットシフト
    return ans

    """
    print("n: ", n)
    if n == 0:
        return 1
    elif n % 2 == 0:
        return super_pow(m ** 2, n // 2) % MOD
    else:
        return m * super_pow(m, n - 1) % MOD
    """

road_dist = [0] * (n-1)
for i in range(len(road_dist)):
    # road_dist[i] = super_pow(a[i], a[i+1])
    road_dist[i] = pow(a[i], a[i+1])

cul_sum = [0] * n
cul_sum[1] = road_dist[0]
for i in range(2, len(cul_sum)):
    cul_sum[i] = (cul_sum[i-1] + road_dist[i-1]) % MOD

res = 0
c = [1] + c + [1]

for i in range(1, len(c)):
    deperture = c[i-1] - 1
    distination = c[i] - 1
    res += abs(cul_sum[distination] - cul_sum[deperture]) % MOD
print(res)



