n = int(input())

d = {}
for i in range(1, 10):
    for j in range(1, 10):
        d[str(i)+str(j)] = 0

for i in range(1, n+1):
    if i % 10 == 0:
        continue
    i = str(i)
    d[i[0]+i[-1]] += 1

ans = 0

for i in range(1, 10):
    for j in range(1, 10):
        ans += d[str(i)+str(j)] * d[str(j)+str(i)]
print(ans)
