n = int(input())
a = list(map(int, input().split()))

def kouyakusuu(x, y):
    if x < y:
        tmp = y
        y = x
        x = tmp
    elif x == y:
        return x

    while True:
        tmp1 = x // y
        tmp2 = x % y
        if tmp2 == 0:
            return y
        x = y
        y = tmp2

ans = a[0]
for i in range(1, len(a)):
    ans = kouyakusuu(ans, a[i])
print(ans)

