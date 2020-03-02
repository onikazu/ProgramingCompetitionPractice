a, b, c = list(map(int, input().split()))

# 全部奇数または偶数にする
# そこからそれぞれ2ずつ足していく
ans = 0
if a%2 == 0 and b%2 == 0 and c%2 == 0:
    pass
elif a%2 == 1 and b%2 == 1 and c%2 == 1:
    pass

elif a%2 == 0 and b%2 == 1 and c%2 == 1:
    b += 1
    c += 1
    ans += 1
elif a%2 == 1 and b%2 == 0 and c%2 == 1:
    a += 1
    c += 1
    ans += 1
elif a%2 == 1 and b%2 == 1 and c%2 == 0:
    a += 1
    b += 1
    ans += 1
elif a%2 == 0 and b%2 == 0 and c%2 == 1:
    a += 1
    b += 1
    ans += 1
elif a%2 == 0 and b%2 == 1 and c%2 == 0:
    a += 1
    c += 1
    ans += 1
elif a%2 == 1 and b%2 == 0 and c%2 == 0:
    b += 1
    c += 1
    ans += 1

while not a == b == c:
    if a == min(a, b, c):
        a += 2
        ans += 1
    
    if a == b == c:
        break

    if b == min(a, b, c):
        b += 2
        ans += 1

    if a == b == c:
        break

    if c == min(a, b, c):
        c += 2
        ans += 1

    if a == b == c:
        break
print(ans)

