a, b, c = list(map(int, input().split()))

ans = c - (a - b)
if ans < 0:
    ans = 0
print(ans)
