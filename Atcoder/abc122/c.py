n, q = map(int, input().split())
s = input()
q_l = [tuple(map(int, input().split())) for _ in range(q)]

accum_sum = [0] * (len(s)+1)

for i in range(len(s)):
    if s[i] == "A" and s[i+1] == "C":
        accum_sum[i+1] = accum_sum[i] + 1
    else:
        accum_sum[i+1] = accum_sum[i]

for l, r in q_l:
    print(accum_sum[r-1]-accum_sum[l-1])

