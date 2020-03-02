n = int(input())
a = list(map(int, input().split()))

neg_cnt = 0
zero_cnt = 0

max_neg_v = -float("inf")
min_pos_v = float("inf")

for i in range(len(a)):
    if a[i] < 0:
        neg_cnt += 1
        max_neg_v = max(max_neg_v, a[i])
    elif a[i] == 0:
        zero_cnt += 1
    else:
        min_pos_v = min(min_pos_v, a[i])

if neg_cnt % 2 == 0 or zero_cnt > 0:
    print(sum(list(map(abs, a))))
else:
    print(max(sum(list(map(abs, a)))-2*min_pos_v, sum(list(map(abs, a)))+2*max_neg_v))


