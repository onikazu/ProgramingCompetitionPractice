n, x = list(map(int, input().split()))
m = [int(input()) for _ in range(n)]

m = sorted(m)
ans = 0

for i in range(n):
    if x >= m[i]:
        ans += 1
        x -= m[i]
    else:
        break
if x >= min(m):
    ans += x // min(m)
print(ans)
