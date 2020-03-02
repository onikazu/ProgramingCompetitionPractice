q_num = int(input())
q_l = [tuple(map(int, input().split())) for _ in range(q_num)]

table = [1] * (10 ** 5 + 1)
table[0] = 0
table[1] = 0

# エラトステネスの篩
for i in range(2, int(len(table) ** 0.5)):
    if table[i] == 0:
        continue
    step = i * 2
    while True:
        if step >= len(table):
            break
        table[step] = 0
        step += i

# 2017 like number table
table_like_n = [0] * len(table)
for i in range(1, len(table_like_n)):
    if i % 2 == 0:
        continue
    if table[i] == 1 and table[(i+1)//2] == 1:
        table_like_n[i] = 1

# 累積和の作成
accum_sum = [0] * (len(table_like_n) + 1)
for i in range(len(table_like_n)):
    accum_sum[i+1] = accum_sum[i] + table_like_n[i]

# クエリの分析
for l, r in q_l:
    print(accum_sum[r+1]-accum_sum[l])

