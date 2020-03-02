# first solution
n = int(input())
buy_l = [list(map(int, input().split())) for _ in range(n)]
candidates = [l[0] for l in buy_l] + [l[1] for l in buy_l]

ans = float("inf")
for s in candidates:
    for t in candidates:
        dist = 0
        for l in buy_l:
            dist += abs(l[0]-s) + abs(l[1]-l[0]) + abs(t-l[1])
        ans = min(dist, ans)
print(ans)







