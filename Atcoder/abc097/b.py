x = int(input())

ans = 0
for b in range(1, x+1):
    p = 2
    while True:
        tmp = b ** p
        if tmp > x:
            break
        ans = max(tmp, ans)
        p += 1
        if b == 1:
            break
print(ans)



