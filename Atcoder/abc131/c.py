import fractions


a, b, c, d = list(map(int, input().split()))

def lcm(x, y):
    return x * y // fractions.gcd(x, y)

def get_num(x):
    ans = x - x // c - x // d + x // lcm(c, d)
    return ans


print(get_num(b) - get_num(a -1))
