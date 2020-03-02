import numpy as np
MOD = 10 ** 9 + 7

def pow_mod(value, exp):
    r = 1
    while exp:
        if exp % 2:
            r *= value
            r %= MOD
        value *= value
        value %= MOD
        exp //= 2
    return r

fact = [1] * 1000001
for i in range(1, 1000000+1):
    fact[i] = fact[i-1] * i % MOD

x, y = map(int, input().split())
if (x + y) % 3 or x > y * 2 or y > x * 2:
    print('0')
    exit()

a, b = map(int, np.linalg.solve([[2, 1], [1, 2]], [x, y]))
ans = fact[a + b] % MOD
ans *= pow_mod(fact[a], MOD-2)
ans %= MOD

ans *= pow_mod(fact[b], MOD-2)
ans %= MOD
print(ans)
