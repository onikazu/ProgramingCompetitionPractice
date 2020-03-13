n, a, b = map(int, input().split())

x, y = divmod(n, (a+b))
ans = x * a + min(n - (a + b) * x, a)
print(ans)

