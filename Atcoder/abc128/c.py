n, m = map(int, input().split())
connect_l = [list(map(int, input().split()))[1:] for _ in range(m)]
p_l = list(map(int, input().split()))

ans = 0
for i in range(1 << n):
    cond = []
    flag = True
    for j in range(n):
        if (i >> j) & 1 == 1:
            cond.append(1)
        else:
            cond.append(0)
    for j in range(len(connect_l)):
        num_on = 0
        for s in connect_l[j]:
            num_on += cond[s-1]
        if not num_on % 2 == p_l[j]:
            flag = False
    if flag:
        ans += 1
print(ans)
            

        





