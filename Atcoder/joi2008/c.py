n, m = map(int, input().split())
p = [int(input()) for _ in range(n)]
p = [0] + p

p_pair = []
for i in range(len(p)):
    for j in range(i, len(p)):
        p_pair.append(p[i]+p[j])

p_pair = sorted(p_pair)
ans = -float("inf")

for i in range(len(p)):
    for j in range(i, len(p)):
        pair_sum = p[i] + p[j]
        if pair_sum + p_pair[0] > m:
            pass
        elif pair_sum + p_pair[-1] <= m:
            ans = max(ans, pair_sum + p_pair[-1])
        else:
            left = 0
            right = len(p_pair) - 1
            while right - left > 1:
                mid = (left + right) // 2
                if pair_sum + p_pair[mid] > m:
                    right = mid
                else:
                    left = mid
            ans = max(ans, pair_sum + p_pair[left])
print(ans)




