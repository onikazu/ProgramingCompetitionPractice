n, m = map(int, input().split())
dists = [int(input()) for _ in range(n-1)]
moves = [int(input()) for _ in range(m)]

MOD = 10 ** 5

accum_dists = [0] + [dists[0]]
for dist in dists[1:]:
    accum_dists.append(accum_dists[-1]+dist)
    
cur = 0
sum_dist = 0
for move in moves:
    if move > 0:
        sum_dist = (sum_dist + accum_dists[move+cur]-accum_dists[cur]) % MOD
    else:
        sum_dist = (sum_dist + accum_dists[cur] - accum_dists[move+cur]) % MOD
    cur += move
print(sum_dist)

