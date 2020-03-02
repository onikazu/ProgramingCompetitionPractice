n = int(input())
arr = list(map(int, input().split()))
flag = [-1] * n
ans = []

for i in range(n-1, -1, -1):
    cnt = 0
    for j in range(i, n, i + 1):
        if j == i:
            continue
        else:
            if flag[j] == 1:
                cnt += 1
    if (arr[i]+cnt) % 2 == 0:
        flag[i] = 0
    else:
        flag[i] = 1
        ans.append(i + 1)
num = len(ans)
if num == 0:
    print(0)
else:
    print(num)
    print(*ans)

