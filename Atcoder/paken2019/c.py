n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(len(a[0]) - 1):
    for j in range(1, len(a[0])):
        point = 0
        for k in range(len(a)):
            point += max(a[k][i], a[k][j])
        ans = max(point, ans)
print(ans)
