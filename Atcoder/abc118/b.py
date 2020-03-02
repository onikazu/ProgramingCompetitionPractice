n, m = list(map(int, input().split()))
a = [list(map(int, input().split()))[1:] for _ in range(n)]

cnt = 0
for i in range(1, m+1):
    flag = True
    for j in range(len(a)):
        if not i in a[j]:
            flag = False
    if flag:
        cnt += 1

print(cnt)

