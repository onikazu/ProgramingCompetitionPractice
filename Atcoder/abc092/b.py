n = int(input())
d, x = list(map(int, input().split()))
a = [int(input()) for _ in range(n)]

ans = 0

for i in range(len(a)):
    ans += 1
    ans += (d - 1) // a[i]
ans += x
print(ans)


