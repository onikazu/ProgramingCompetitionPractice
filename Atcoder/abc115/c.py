n, k = list(map(int, input().split()))
h = [int(input()) for _ in range(n)]

h = sorted(h)
ans = 10 ** 9 + 1
for i in range(len(h) - (k-1)):
    ans = min(ans, h[i+k-1] - h[i])
print(ans)

