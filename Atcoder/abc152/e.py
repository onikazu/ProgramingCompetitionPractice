n = int(input())
a = list(map(int, input().split()))

def lcm(a):
    from fractions import gcd
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x

x = lcm(a)
ans = sum([x / a[i] for i in range(len(a))]) % (10 ** 9 + 7)
print(int(ans))

