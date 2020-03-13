n = int(input())
a = list(map(int, input().split()))

ans = []
x1 = sum(a) - 2 * sum([a[i] for i in range(1, n, 2)])
ans.append(x1)
for i in range(n-1):
    ans.append(2 * a[i]-ans[-1])

print(*ans)


