def cmb(n, r):
    if n == 1: return 0
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

n = int(input())
S = [input() for _ in range(n)]
S_sorted = ["".join(sorted(s)) for s in S]
S_sorted = sorted(S_sorted)

ans = 0
cnt = 1
for i in range(1, len(S_sorted)):
    if S_sorted[i] == S_sorted[i-1]:
        cnt += 1
    else:
        ans += cmb(cnt, 2)
        cnt = 1

if cnt > 1:
    ans += cmb(cnt, 2)

print(int(ans))




