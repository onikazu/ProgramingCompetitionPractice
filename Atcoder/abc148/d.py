n = int(input())
A = list(map(int, input().split()))

ans = 0
break_tgt = 1

for i in range(n):
    if A[i] == break_tgt:
        break_tgt += 1
    else:
        ans += 1

if ans == n:
    ans = -1

print(ans)

