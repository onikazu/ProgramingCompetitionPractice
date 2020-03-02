n, m = list(map(int, input().split()))
x =  list(map(int, input().split()))

if n >= m:
    print(0)
    exit(0)

x = sorted(x)
sub = [x[i+1] - x[i] for i in range(len(x) - 1)]
sub = sorted(sub)
ans = 0

for i in range(m - n):
    ans += sub[i]
print(ans)
