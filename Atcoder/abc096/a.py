a, b = list(map(int, input().split()))

ans = a if b >= a else a - 1
print(ans)
