# https://www.kumilog.net/entry/two-pointers

n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

if 0 in s:
    ans = n
else:
    r, l = 0, 0
    sum_s = 1
    ans = 0
    while r < n:
        # 右端を勧めたときの積がk以下なら右端を進める
        if sum_s * s[r] <= k:
            sum_s *= s[r] 
            r += 1
            ans = max(ans, r - l)
        elif r == l:
            r += 1
            l += 1
        else:
        # 左を進める
            sum_s //= s[l]
            l += 1

print(ans)

