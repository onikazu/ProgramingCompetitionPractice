n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

ans = 0

for i in range(len(s)):
    point = 0
    kw = s[i]
    for j in range(len(s)):
        if s[j] == kw:
            point += 1
    for j in range(len(t)):
        if t[j] == kw:
            point -= 1
    ans = max(ans, point)
print(ans)



