a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = set([int(input()) for _ in range(n)])

for i in range(3):
    flag = True
    for j in range(3):
        if not a[i][j] in b:
            flag = False
            break
    if flag:
        print("Yes")
        exit()

for i in range(3):
    flag = True
    for j in range(3):
        if not a[j][i] in b:
            flag = False
            break
    if flag:
        print("Yes")
        exit()

flag = True
for i in range(3):
    if not a[i][i] in b:
        flag = False
if flag:
    print("Yes")
    exit()

flag = True
if a[0][2] in b and a[1][1] in b and a[2][0] in b:
    print("Yes")
else:
    print("No")










