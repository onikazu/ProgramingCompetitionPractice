a, b = list(map(int, input().split()))

def f0n(n):
    if n % 2 == 0:
        return (n // 2) % 2 ^ n
    else:
        return 0 if ((n + 1) / 2) % 2 == 0 else 1

print(int(f0n(a-1)) ^ int(f0n(b)))
