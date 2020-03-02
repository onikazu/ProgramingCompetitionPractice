n, k = map(int, input().split())

ans = ""
while True:
    n, m = divmod(n, k)
    ans += str(m)
    if n == 0:
        break
print(len(ans))

