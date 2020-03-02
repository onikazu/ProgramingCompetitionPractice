n, m, c = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    code_num = 0
    for j in range(m):
        code_num += b[j] * a[i][j]
    code_num += c
    if code_num > 0:
        ans += 1
print(ans)
