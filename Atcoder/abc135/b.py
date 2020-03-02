n = int(input())
p = list(map(int, input().split()))

p_sorted = sorted(p)

wrong_cnt = 0
for i in range(n):
    if p[i] != p_sorted[i]:
        wrong_cnt += 1

if wrong_cnt > 2:
    print("NO")
else:
    print("YES")


