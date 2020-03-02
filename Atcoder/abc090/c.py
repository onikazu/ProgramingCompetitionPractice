n, m = list(map(int, input().split()))

ans = 0
if n == 1 and m == 1:
    ans = 1
elif n == 1:
    ans = m - 2
elif m == 1:
    ans = n - 2
else:
    ans = (m - 2) * (n - 2)
print(ans)
