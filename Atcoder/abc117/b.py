n = int(input())
l = list(map(int, input().split()))

ans = "Yes"
for i in range(len(l)):
    s = 0
    for j in range(len(l)):
        if not j == i:
            s += l[j]
    if l[i] >= s:
        ans = "No"
        break
print(ans)
