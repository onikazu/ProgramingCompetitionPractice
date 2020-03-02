import itertools


n = int(input())
geo = [list(map(int, input().split())) for i in range(n)]

sum_dist = 0
num_pattern = 0

for pattern in itertools.permutations([i for i in range(n)], n):
    for i in range(1, n):
        x, y = geo[pattern[i]]
        x_prev, y_prev = geo[pattern[i-1]]
        d = ((x-x_prev) ** 2 + (y-y_prev) ** 2) ** 0.5
        sum_dist += d
    num_pattern += 1

print(sum_dist / num_pattern)

