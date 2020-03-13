a, b, m = map(int, input().split())
a_l = list(map(int, input().split()))
b_l = list(map(int, input().split()))
coupons = [list(map(int, input().split())) for _ in range(m)]

ans = min(a_l) + min(b_l)
pairs = []
for a_i, b_i, c in coupons:
    pairs.append(a_l[a_i-1]+b_l[b_i-1]-c)

print(min(ans, min(pairs)))




