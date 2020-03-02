n, m = map(int, input().split())
q = [tuple(map(int, input().split())) for _ in range(m)]

for i in range(1000):
    i = str(i)
    if len(i) != n:
        continue
    flag = True
    for s, c in q:
        if len(i) < s:
            flag = False
            break
        if i[s-1] != str(c):
            flag = False
            break
    if flag:
        print(i)
        exit()
print(-1)

