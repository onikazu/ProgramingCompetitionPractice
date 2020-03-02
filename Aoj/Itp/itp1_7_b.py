from itertools import combinations


n_l = []
x_l = []
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    n_l.append(n)
    x_l.append(x)

for n, x in zip(n_l, x_l):
    ans = 0
    for comb in combinations([i for i in range(1, n+1)], 3):
        if sum(comb) == x:
            ans += 1
    print(ans)



