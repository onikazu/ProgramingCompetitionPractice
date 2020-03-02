a, b = list(map(int, input().split()))

ans = 0
for num in range(a, b+1):
    s = str(num)
    rev_s = ""
    for i in reversed(range(len(s))):
        rev_s += s[i]
    if s == rev_s:
        ans += 1
print(ans)

