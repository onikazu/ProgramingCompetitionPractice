n, m, q_num = list(map(int, input().split()))
l_l = [0] * n
r_l = [0] * n
for _ in range(m):
    l, r = map(int, input().split())
    l_l[l-1] += 1
    r_l[r-1] += 1
q_l = [tuple(map(int, input().split())) for _ in range(q_num)]

def generate_acc_l(l):
    res = [0]
    for i in range(len(l)):
        res.append(res[-1]+l[i])
    return res

print(l_l)
print(r_l)
acc_l = generate_acc_l(l_l)
acc_r = generate_acc_l(r_l)
print(acc_l)
print(acc_r)

for p, q in q_l:
    print(min(acc_l[q]-acc_l[p-1], acc_r[q]-acc_r[p-1]))






