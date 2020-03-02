import itertools


n, k = list(map(int, input().split()))

n_l = [i for i in range(1, n+1)]
comb_l = list(itertools.combinations(n_l, 3))
comb_sum_l = list(map(sum, comb_l))

print(comb_l)
print(comb_sum_l)
