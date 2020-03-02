n = int(input())
h = list(map(int, input().split()))

ans = 0
level = 0
for i in range(len(h)):
    if h[i] >= level:
        level = h[i]
    else:
        ans += level - h[i]
        level = h[i]

ans += level

print(ans)

