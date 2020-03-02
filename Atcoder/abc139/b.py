a, b = list(map(int, input().split()))

ans = 0
available = 1
while True:
    if available >= b:
        break
    ans += 1
    available += a - 1

print(ans)
