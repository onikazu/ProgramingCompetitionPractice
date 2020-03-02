n = int(input())
p = list(map(int, input().split()))

min_v = float("inf")
ans = 0
for i in range(len(p)):
    if min_v >= p[i]:
        ans += 1
    min_v = min(min_v, p[i])
print(ans)



