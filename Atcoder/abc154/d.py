n, k = list(map(int, input().split()))
p = list(map(int, input().split()))


def expect(n):
    res = (n + 1) / 2
    return res

p = list(map(expect, p))
ans_sum = sum(p[:k])
tmp_sum = ans_sum
idx = 0

for i in range(k, n):
    tmp_sum = tmp_sum + p[i] - p[i-k]
    if tmp_sum > ans_sum:
        ans_sum = tmp_sum

print(ans_sum)

