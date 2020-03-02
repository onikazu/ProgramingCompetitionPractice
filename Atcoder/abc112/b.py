n, t = list(map(int, input().split()))
routes = [list(map(int, input().split())) for _ in range(n)]

min_c = 1001
for (c, time) in routes:
    if time <= t:
        min_c = min(min_c, c)
if min_c == 1001:
    min_c = "TLE"
print(min_c)

