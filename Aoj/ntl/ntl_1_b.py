MOD = 10 ** 9 + 7
m, n = map(int, input().split())

def fast_pow(m, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_pow(m**2, n // 2) % MOD
    else:
        return (m * fast_pow(m ** 2, (n - 1) // 2)) % MOD

if __name__ == "__main__":
    print(fast_pow(m, n))


