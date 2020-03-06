n, m = map(int, input().split())
cities = list(map(int, input().split()))
train_info = [tuple(map(int, input().split())) for _ in range(n-1)]

cul_sum = [0] * n

for i in range(len(cities)-1):
    dep = cities[i]-1
    arriv = cities[i+1]-1
    if dep > arriv:
        dep, arriv = arriv, dep
    cul_sum[dep] += 1
    cul_sum[arriv] -= 1

for i in range(len(cul_sum)-1):
    cul_sum[i+1] += cul_sum[i]

res = 0
for i in range(len(train_info)):
    a, b, c = train_info[i]
    times = cul_sum[i]
    if a * times > b * times + c:
        res += b * times + c
    else:
        res += a * times
print(res)

