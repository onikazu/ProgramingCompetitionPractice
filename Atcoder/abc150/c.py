import itertools


n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

permu_dict = list(itertools.permutations([i for i in range(1, n+1)]))
permu_dict = sorted(permu_dict)

print(abs(permu_dict.index(p)-permu_dict.index(q)))
