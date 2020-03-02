import fractions
from functools import reduce


def gcd(L):
    return reduce(fractions.gcd, L)

N, X = list(map(int, input().split()))
x = list(map(int, input().split()))

x_gap = [abs(x[i] - X) for i in range(N)]

ans = gcd(x_gap)
print(ans)
