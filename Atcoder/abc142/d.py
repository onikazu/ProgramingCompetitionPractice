a, b = map(int, input().split())

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0: # i で割り切れればiは素因数
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


s = set(prime_decomposition(a))
t = set(prime_decomposition(b))
print(len(s&t) + 1)

