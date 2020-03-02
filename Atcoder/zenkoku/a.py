n = int(input())
a = list(map(int, input().split()))

ruiseki_l = []
ruiseki = 0
for i in range(len(a)):
    ruiseki += a[i]
    ruiseki_l.append(ruiseki)

for k in range(1, n+1):
    ans = ruiseki_l[k-1]
    for i in range(k, n):
        ans = max(ans, ruiseki_l[i]-ruiseki_l[i-k])
    print(ans)





