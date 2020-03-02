n = int(input())
a = list(map(int, input().split()))
MOD = 10 ** 9 + 7

ans = 0
for k in range(60):
    cnt_z = 0
    cnt_o = 0
    for i in range(len(a)):
        if (a[i] >> k) & 1 == 1:
            cnt_o += 1
        else:
            cnt_z += 1
    ans += ((cnt_o * cnt_z) * 2 ** k)
    ans %= MOD

print(ans)


